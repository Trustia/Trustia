"""
TRUSTIA Algı Sistemi - Zemin segmentasyonu.

Arazi yüzeyini tespit edip noktalardan ayırır. Engel tespiti için
kritik ön işlem: zemin noktaları çıkarılınca sadece engelrer kalır.

Algoritmalar:
  * RANSAC Ground Segmentation - düzlem fitting
  * Multi-Plane Segmentation - çoklu düzlem (eğimli arazi)
  * Progressive Morphological Filter (gelecek implementasyon)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

from perception.types import PointCloud


@dataclass
class GroundPlane:
    """Zemin düzlemi - ax + by + cz + d = 0 denklemi."""
    normal: np.ndarray  # (3,) - (a, b, c) normal vektör
    offset: float       # d - orijinden uzaklık
    inliers: np.ndarray # Düzlem üzerindeki nokta indisleri

    @property
    def inlier_count(self) -> int:
        return len(self.inliers)

    def distance_to_point(self, point: np.ndarray) -> float:
        """Noktanın düzleme mesafesi (işaretli)."""
        return float(np.dot(self.normal, point) + self.offset)

    def distance_to_points(self, points: np.ndarray) -> np.ndarray:
        """Nokta kümesinin düzleme mesafeleri."""
        return np.abs(points @ self.normal + self.offset)


class GroundSegmenter(ABC):
    """Zemin segmentasyon algoritması temel sınıfı."""

    @abstractmethod
    def segment(self, cloud: PointCloud) -> Tuple[PointCloud, PointCloud, GroundPlane]:
        """Bulutu zemin/engel olarak ayır.
        
        Returns:
            ground_cloud: Zemin noktaları
            obstacle_cloud: Engel noktaları
            plane: Tespit edilen zemin düzlemi
        """


class RANSACGroundSegmenter(GroundSegmenter):
    """RANSAC ile zemin düzlemi bulma.
    
    Random Sample Consensus: Rastgele 3 nokta seç, düzlem fit et,
    inlier sayısına bak. En fazla inlier veren düzlem zemin.
    
    Parametreler:
        distance_threshold: Düzleme maksimum mesafe (metre)
        iterations: RANSAC iterasyon sayısı
        min_inliers: Minimum inlier oranı (geçerli düzlem için)
    """

    def __init__(
        self,
        distance_threshold: float = 0.1,
        iterations: int = 100,
        min_inliers: float = 0.3,
    ) -> None:
        if distance_threshold <= 0.0:
            raise ValueError("distance_threshold pozitif olmalı")
        if iterations < 1:
            raise ValueError("iterations >= 1 olmalı")
        if not 0.0 < min_inliers <= 1.0:
            raise ValueError("min_inliers (0, 1] aralığında olmalı")
        
        self.distance_threshold = distance_threshold
        self.iterations = iterations
        self.min_inliers = min_inliers

    def segment(self, cloud: PointCloud) -> Tuple[PointCloud, PointCloud, GroundPlane]:
        if cloud.size < 3:
            return PointCloud.empty(), cloud, None
        
        xyz = cloud.xyz()
        best_plane = None
        best_inliers = np.array([], dtype=int)
        min_inlier_count = int(cloud.size * self.min_inliers)
        
        rng = np.random.RandomState(42)
        
        for _ in range(self.iterations):
            # 3 rastgele nokta seç
            sample_indices = rng.choice(cloud.size, 3, replace=False)
            points = xyz[sample_indices]
            
            # Düzlem denklemi hesapla: ax + by + cz + d = 0
            # İki vektör: v1 = p1-p0, v2 = p2-p0
            # Normal: n = v1 x v2
            v1 = points[1] - points[0]
            v2 = points[2] - points[0]
            normal = np.cross(v1, v2)
            
            norm = np.linalg.norm(normal)
            if norm < 1e-6:
                continue  # Dejenere üçgen (collinear noktalar)
            
            normal = normal / norm  # Normalize
            offset = -np.dot(normal, points[0])
            
            # Tüm noktaların düzleme mesafesini hesapla
            distances = np.abs(xyz @ normal + offset)
            inliers = np.where(distances < self.distance_threshold)[0]
            
            # En iyi modeli güncelle
            if len(inliers) > len(best_inliers):
                best_inliers = inliers
                best_plane = GroundPlane(
                    normal=normal,
                    offset=offset,
                    inliers=inliers,
                )
        
        # Yeterli inlier yoksa başarısız
        if best_plane is None or len(best_inliers) < min_inlier_count:
            return PointCloud.empty(), cloud, None
        
        # Zemini ayır
        ground_mask = np.zeros(cloud.size, dtype=bool)
        ground_mask[best_inliers] = True
        
        ground_cloud = cloud.filter_by_mask(ground_mask)
        obstacle_cloud = cloud.filter_by_mask(~ground_mask)
        
        return ground_cloud, obstacle_cloud, best_plane


class MultiPlaneSegmenter(GroundSegmenter):
    """Çoklu düzlem segmentasyonu - eğimli/basamaklı arazi.
    
    Tek düzlem yerine birden fazla düzlem fit eder. Basamaklı
    arazi, rampa gibi karmaşık geometrilerde daha iyi.
    
    Parametreler:
        max_planes: Maksimum düzlem sayısı
        distance_threshold: Düzlem mesafe eşiği
        min_plane_points: Düzlem için minimum nokta sayısı
    """

    def __init__(
        self,
        max_planes: int = 3,
        distance_threshold: float = 0.1,
        min_plane_points: int = 100,
    ) -> None:
        self.max_planes = max_planes
        self.distance_threshold = distance_threshold
        self.min_plane_points = min_plane_points
        self._ransac = RANSACGroundSegmenter(
            distance_threshold=distance_threshold,
            iterations=50,
            min_inliers=0.1,
        )

    def segment(self, cloud: PointCloud) -> Tuple[PointCloud, PointCloud, List[GroundPlane]]:
        if cloud.size == 0:
            return PointCloud.empty(), cloud, []
        
        remaining = cloud
        ground_indices = []
        planes = []
        
        for _ in range(self.max_planes):
            if remaining.size < self.min_plane_points:
                break
            
            # RANSAC ile bir düzlem bul
            ground, obstacles, plane = self._ransac.segment(remaining)
            
            if plane is None or ground.size < self.min_plane_points:
                break
            
            # Zemni indisleri sakla
            ground_indices.extend(plane.inliers)
            planes.append(plane)
            
            # Kalan noktalarla devam et
            remaining = obstacles
        
        # Tüm zemin noktalarını birleştir
        if ground_indices:
            ground_mask = np.zeros(cloud.size, dtype=bool)
            ground_mask[ground_indices] = True
            ground_cloud = cloud.filter_by_mask(ground_mask)
            obstacle_cloud = cloud.filter_by_mask(~ground_mask)
        else:
            ground_cloud = PointCloud.empty()
            obstacle_cloud = cloud
        
        return ground_cloud, obstacle_cloud, planes


class HeightMapGroundSegmenter(GroundSegmenter):
    """Yükseklik haritası bazlı zemin segmentasyonu.
    
    XY düzlemde grid'e böl, her hücrede en düşük Z değerini zemin
    kabul et. Hızlı ama basit - düz arazi için uygun.
    
    Parametreler:
        grid_resolution: Grid hücre boyutu (metre)
        height_threshold: Zeminden maksimum yükseklik (metre)
    """

    def __init__(
        self,
        grid_resolution: float = 0.5,
        height_threshold: float = 0.3,
    ) -> None:
        self.grid_resolution = grid_resolution
        self.height_threshold = height_threshold

    def segment(self, cloud: PointCloud) -> Tuple[PointCloud, PointCloud, None]:
        if cloud.size == 0:
            return PointCloud.empty(), cloud, None
        
        xyz = cloud.xyz()
        
        # XY grid indisleri
        xy = xyz[:, :2]
        min_xy = xy.min(axis=0)
        grid_indices = np.floor((xy - min_xy) / self.grid_resolution).astype(int)
        
        # Her grid hücresinde minimum Z bul
        unique_cells, inverse = np.unique(
            grid_indices, axis=0, return_inverse=True
        )
        
        ground_mask = np.zeros(cloud.size, dtype=bool)
        
        for cell_idx in range(len(unique_cells)):
            cell_mask = (inverse == cell_idx)
            cell_z = xyz[cell_mask, 2]
            min_z = cell_z.min()
            
            # Min Z'ye yakın noktalar zemin
            local_ground = cell_mask & (
                np.abs(xyz[:, 2] - min_z) < self.height_threshold
            )
            ground_mask |= local_ground
        
        ground_cloud = cloud.filter_by_mask(ground_mask)
        obstacle_cloud = cloud.filter_by_mask(~ground_mask)
        
        return ground_cloud, obstacle_cloud, None


@dataclass
class CurbBoundaryResult:
    """
    Kaldırım taşı ve yol sınırı algılama sonucu.
    Yol çizgileri silinmiş veya hava yağışlı olsa bile 3B LiDAR yükseklik
    farklarından (8 cm - 28 cm basamak sıçraması) sürüş koridorunu çıkarır.
    """
    left_boundary_y_m: float
    right_boundary_y_m: float
    corridor_width_m: float
    lane_center_offset_m: float
    left_curb_points: List[Tuple[float, float, float]]
    right_curb_points: List[Tuple[float, float, float]]
    valid_corridor: bool


class CurbAndRoadBoundaryDetector:
    """
    3B LiDAR Nokta Bulutu Tabanlı Kaldırım Taşı (Curb) ve Yol Sınırı Algılayıcısı.

    Yol şerit çizgileri tamamen silindiğinde, kar/yağmur altında veya asfalt-toprak
    geçişlerinde yanal yükseklik sıçraması (delta-Z) ve eğim gradyanı analiziyle
    aracın güvenli sürüş koridorunu santimetre hassasiyetinde belirler.
    """

    def __init__(
        self,
        min_curb_height_m: float = 0.08,
        max_curb_height_m: float = 0.28,
        longitudinal_slice_m: float = 2.0,
        max_lookahead_m: float = 35.0,
        default_half_width_m: float = 3.5,
    ) -> None:
        self.min_curb_h = min_curb_height_m
        self.max_curb_h = max_curb_height_m
        self.slice_step = longitudinal_slice_m
        self.max_lookahead = max_lookahead_m
        self.default_half_w = default_half_width_m

    def detect_road_boundaries(self, cloud: PointCloud) -> CurbBoundaryResult:
        """
        Nokta bulutundan sol ve sağ kaldırım sınırlarını ve şerit merkez sapmasını hesaplar.
        """
        if cloud.size == 0:
            return CurbBoundaryResult(
                left_boundary_y_m=self.default_half_w,
                right_boundary_y_m=-self.default_half_w,
                corridor_width_m=self.default_half_w * 2.0,
                lane_center_offset_m=0.0,
                left_curb_points=[],
                right_curb_points=[],
                valid_corridor=False,
            )

        xyz = cloud.xyz()
        # İleri görüş (0.5 m ile max_lookahead m arası) noktaları filtrele
        forward_mask = (xyz[:, 0] >= 0.5) & (xyz[:, 0] <= self.max_lookahead)
        pts = xyz[forward_mask]
        if len(pts) == 0:
            pts = xyz

        # Yol merkezine yakın noktaların medyan Z değerini asfalt referans yüksekliği al
        center_mask = np.abs(pts[:, 1]) < 1.5
        road_z = float(np.median(pts[center_mask, 2])) if np.any(center_mask) else float(np.median(pts[:, 2]))

        # Kaldırım yüksekliği aralığındaki (road_z + 8cm .. 28cm) noktaları bul
        dz = pts[:, 2] - road_z
        curb_mask = (dz >= self.min_curb_h) & (dz <= self.max_curb_h)
        curb_pts = pts[curb_mask]

        left_pts = curb_pts[curb_pts[:, 1] > 0.8]
        right_pts = curb_pts[curb_pts[:, 1] < -0.8]

        left_y = float(np.median(left_pts[:, 1])) if len(left_pts) > 0 else self.default_half_w
        right_y = float(np.median(right_pts[:, 1])) if len(right_pts) > 0 else -self.default_half_w

        corridor_w = max(0.0, left_y - right_y)
        center_offset = (left_y + right_y) / 2.0

        left_list = [(float(p[0]), float(p[1]), float(p[2])) for p in left_pts[:50]]
        right_list = [(float(p[0]), float(p[1]), float(p[2])) for p in right_pts[:50]]

        return CurbBoundaryResult(
            left_boundary_y_m=left_y,
            right_boundary_y_m=right_y,
            corridor_width_m=corridor_w,
            lane_center_offset_m=center_offset,
            left_curb_points=left_list,
            right_curb_points=right_list,
            valid_corridor=(corridor_w >= 2.2),
        )

