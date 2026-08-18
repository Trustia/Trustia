"""
TRUSTIA Algı Sistemi - Nokta bulutu filtreleme.

Endüstri standardı filtreleme algoritmaları:
  * Voxel Grid Downsampling - performans için nokta sayısı azaltma
  * Statistical Outlier Removal - gürültü temizleme
  * Radius Outlier Removal - seyrek nokta temizleme
  * Pass-Through Filter - ROI (Region of Interest) seçimi

PCL (Point Cloud Library) benzeri API.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Tuple

import math
import numpy as np

from perception.types import PointCloud


class PointCloudFilter:
    """Nokta bulutu filtresi temel sınıfı ve menzil filtresi."""

    def __init__(self, min_range_m: float = 0.0, max_range_m: float = 100.0, ground_clearance_m: float = 0.0) -> None:
        if min_range_m >= max_range_m:
            from core.errors import SensorError
            raise SensorError("min_range_m strictly less than max_range_m olmalıdır.")
        self.min_range_m = min_range_m
        self.max_range_m = max_range_m
        self.ground_clearance_m = ground_clearance_m

    def apply(self, points: list) -> list:
        res = []
        for p in points:
            r = getattr(p, "range_m", None)
            if r is None and hasattr(p, "x") and hasattr(p, "y"):
                r = math.hypot(p.x, p.y)
            if r is not None and self.min_range_m <= r <= self.max_range_m:
                el = getattr(p, "elevation_rad", 0.0)
                height = abs(r * math.sin(el))
                if self.ground_clearance_m > 0 and height < self.ground_clearance_m:
                    continue
                res.append(p)
        return res

    def filter(self, cloud: PointCloud) -> PointCloud:
        """Filtreyi uygula, yeni bulut döndür."""
        if cloud.size == 0:
            return PointCloud.empty()
        xyz = cloud.xyz()
        dists = np.linalg.norm(xyz[:, :2], axis=1)
        mask = (dists >= self.min_range_m) & (dists <= self.max_range_m)
        return PointCloud(points=cloud.points[mask], timestamp_ns=cloud.timestamp_ns, frame_id=cloud.frame_id)



class VoxelGridFilter(PointCloudFilter):
    """Voxel Grid Downsampling - 3D ızgara ortalama.
    
    Bulut binlerce noktayı üç boyutlu ızgaraya böler; her hücredeki
    noktaların ortalamasını tek nokta olarak döndürür. Performans
    için kritik (30K nokta → 5K nokta).
    
    Parametre:
        leaf_size: Voxel kenar uzunluğu (metre)
    """

    def __init__(self, leaf_size: float = 0.1) -> None:
        if leaf_size <= 0.0:
            raise ValueError(f"leaf_size pozitif olmalı: {leaf_size}")
        self.leaf_size = leaf_size

    def filter(self, cloud: PointCloud) -> PointCloud:
        if cloud.size == 0:
            return PointCloud.empty()
        
        xyz = cloud.xyz()
        min_bound, max_bound = cloud.bounds()
        
        # Voxel grid indisleri
        grid_indices = np.floor((xyz - min_bound) / self.leaf_size).astype(np.int32)
        
        # Her voxel için unique key oluştur
        # (i, j, k) -> i + j*Nx + k*Nx*Ny şeklinde tek sayıya çevir
        grid_size = np.ceil((max_bound - min_bound) / self.leaf_size).astype(np.int32) + 1
        voxel_keys = (
            grid_indices[:, 0]
            + grid_indices[:, 1] * grid_size[0]
            + grid_indices[:, 2] * grid_size[0] * grid_size[1]
        )
        
        # Her voxel için nokta ortalamalarını hesapla
        unique_keys, inverse_indices = np.unique(voxel_keys, return_inverse=True)
        downsampled = np.zeros((len(unique_keys), cloud.points.shape[1]))
        
        for i, key in enumerate(unique_keys):
            mask = (inverse_indices == i)
            downsampled[i] = cloud.points[mask].mean(axis=0)
        
        return PointCloud(
            points=downsampled,
            timestamp_ns=cloud.timestamp_ns,
            frame_id=cloud.frame_id,
        )


class StatisticalOutlierFilter(PointCloudFilter):
    """İstatistiksel gürültü temizleme.
    
    Her nokta için K-nearest neighbors mesafe ortalaması hesaplanır.
    Ortalama + sigma*std sapmadan uzak noktalar gürültü kabul edilir.
    
    Parametreler:
        k_neighbors: Komşu sayısı
        std_dev_mul: Standart sapma çarpanı (2.0 → %95 confidence)
    """

    def __init__(self, k_neighbors: int = 50, std_dev_mul: float = 2.0) -> None:
        if k_neighbors < 1:
            raise ValueError(f"k_neighbors >= 1 olmalı: {k_neighbors}")
        if std_dev_mul <= 0.0:
            raise ValueError(f"std_dev_mul pozitif olmalı: {std_dev_mul}")
        self.k_neighbors = k_neighbors
        self.std_dev_mul = std_dev_mul

    def filter(self, cloud: PointCloud) -> PointCloud:
        if cloud.size < self.k_neighbors:
            return cloud
        
        xyz = cloud.xyz()
        k = min(self.k_neighbors + 1, cloud.size)  # +1 çünkü nokta kendini bulur
        
        # K-NN mesafe hesabı (basit, performans için optimize edilebilir)
        distances = np.zeros(cloud.size)
        for i in range(cloud.size):
            dists = np.linalg.norm(xyz - xyz[i], axis=1)
            dists[i] = np.inf  # Kendini hariç tut
            nearest = np.partition(dists, k - 1)[:k]
            distances[i] = nearest.mean()
        
        # İstatistiksel outlier tespiti
        mean_dist = distances.mean()
        std_dist = distances.std()
        threshold = mean_dist + self.std_dev_mul * std_dist
        
        inliers = distances <= threshold
        return cloud.filter_by_mask(inliers)


class RadiusOutlierFilter(PointCloudFilter):
    """Yarıçap bazlı gürültü temizleme.
    
    Belirtilen yarıçapta minimum komşu sayısı yoksa nokta silinir.
    Seyrek noktaları (tek başına kalan) temizler.
    
    Parametreler:
        radius: Arama yarıçapı (metre)
        min_neighbors: Minimum komşu sayısı
    """

    def __init__(self, radius: float = 0.5, min_neighbors: int = 5) -> None:
        if radius <= 0.0:
            raise ValueError(f"radius pozitif olmalı: {radius}")
        if min_neighbors < 1:
            raise ValueError(f"min_neighbors >= 1 olmalı: {min_neighbors}")
        self.radius = radius
        self.min_neighbors = min_neighbors

    def filter(self, cloud: PointCloud) -> PointCloud:
        if cloud.size == 0:
            return PointCloud.empty()
        
        xyz = cloud.xyz()
        keep = np.zeros(cloud.size, dtype=bool)
        
        for i in range(cloud.size):
            dists = np.linalg.norm(xyz - xyz[i], axis=1)
            neighbors = np.sum((dists < self.radius) & (dists > 0))
            keep[i] = neighbors >= self.min_neighbors
        
        return cloud.filter_by_mask(keep)


class PassThroughFilter(PointCloudFilter):
    """Eksen bazlı aralık filtresi - ROI seçimi.
    
    Belirtilen eksende min/max aralığı dışındaki noktaları siler.
    Örnek: Aracın 30m önünü al, arkasını unut.
    
    Parametreler:
        axis: Eksen adı ('x', 'y', 'z')
        min_val, max_val: Aralık sınırları
    """

    def __init__(self, axis: str = 'x', min_val: float = -float('inf'),
                 max_val: float = float('inf')) -> None:
        if axis not in ('x', 'y', 'z'):
            raise ValueError(f"axis 'x', 'y' veya 'z' olmalı: {axis}")
        self.axis = {'x': 0, 'y': 1, 'z': 2}[axis]
        self.min_val = min_val
        self.max_val = max_val

    def filter(self, cloud: PointCloud) -> PointCloud:
        if cloud.size == 0:
            return PointCloud.empty()
        
        xyz = cloud.xyz()
        axis_values = xyz[:, self.axis]
        mask = (axis_values >= self.min_val) & (axis_values <= self.max_val)
        return cloud.filter_by_mask(mask)


class CropBoxFilter(PointCloudFilter):
    """3D kutu kırpma - dikdörtgen prizma ROI.
    
    Parametreler:
        min_point: (x_min, y_min, z_min)
        max_point: (x_max, y_max, z_max)
    """

    def __init__(self, min_point: Tuple[float, float, float],
                 max_point: Tuple[float, float, float]) -> None:
        self.min_point = np.array(min_point)
        self.max_point = np.array(max_point)
        if np.any(self.min_point >= self.max_point):
            raise ValueError("min_point < max_point olmalı")

    def filter(self, cloud: PointCloud) -> PointCloud:
        if cloud.size == 0:
            return PointCloud.empty()
        
        xyz = cloud.xyz()
        mask = np.all((xyz >= self.min_point) & (xyz <= self.max_point), axis=1)
        return cloud.filter_by_mask(mask)


class FilterPipeline(PointCloudFilter):
    """Filtre zinciri - sıralı uygulama.
    
    Kullanım:
        pipeline = FilterPipeline([
            VoxelGridFilter(0.1),
            StatisticalOutlierFilter(50, 2.0),
            PassThroughFilter('z', -2.0, 5.0),
        ])
        filtered = pipeline.filter(cloud)
    """

    def __init__(self, filters: list[PointCloudFilter]) -> None:
        self.filters = filters

    def filter(self, cloud: PointCloud) -> PointCloud:
        result = cloud
        for f in self.filters:
            result = f.filter(result)
            if result.size == 0:
                break
        return result

    def add(self, filter: PointCloudFilter) -> None:
        self.filters.append(filter)
