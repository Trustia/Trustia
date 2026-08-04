"""
TRUSTIA Algı Sistemi - Engel tespiti ve takip.

Kümeleri engellere çevirir, sınıflandırır ve zaman içinde takip eder.

Bileşenler:
  * ObstacleDetector - Küme → Engel dönüşümü
  * ObstacleTracker - Kalman filtresi ile multi-object tracking
  * Hungarian algoritması - Tespit ↔ Track eşleştirme
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np

from perception.clustering import Cluster
from perception.types import Obstacle, ObstacleClass, BoundingBox, PointCloud


@dataclass
class DetectionResult:
    """Tek frame'deki tüm engel tespitleri."""
    obstacles: List[Obstacle]
    timestamp_ns: int
    frame_id: str = "lidar"

    def __len__(self) -> int:
        return len(self.obstacles)

    def nearest(self) -> Optional[Obstacle]:
        """En yakın engel."""
        if not self.obstacles:
            return None
        return min(self.obstacles, key=lambda o: o.distance)


import math
import numpy as np


class ObstacleDetector:
    """Kümeleri engellere çevirir."""

    def __init__(
        self,
        min_points: int = 2,
        max_distance: float = 100.0,
        filter: Optional[Any] = None,
        clusterer: Optional[Any] = None,
        safety_radius_m: float = 0.4,
    ) -> None:
        self.min_points = min_points
        self.max_distance = max_distance
        self.filter = filter
        self.clusterer = clusterer
        self.safety_radius_m = safety_radius_m

    def detect(self, clusters_or_scan: Any, timestamp_ns_or_origin: Any = 0) -> Any:
        """Kümeleri veya simülasyon taramalarını engellere çevir."""
        if not clusters_or_scan:
            return []

        timestamp_ns = timestamp_ns_or_origin if isinstance(timestamp_ns_or_origin, int) else 0

        clusters = clusters_or_scan
        if self.clusterer and isinstance(clusters, list) and len(clusters) > 0 and hasattr(clusters[0], "range_m"):
            clusters = self.clusterer.cluster(clusters)
        elif isinstance(clusters_or_scan, list) and len(clusters_or_scan) > 0:
            first = clusters_or_scan[0]
            if not isinstance(first, Cluster) and not hasattr(first, "range_m"):
                obstacles = []
                for item in clusters_or_scan:
                    if hasattr(item, "x_m") and hasattr(item, "y_m"):
                        ox, oy = item.x_m, item.y_m
                    elif isinstance(item, tuple) and len(item) >= 2:
                        ox, oy = item[0], item[1]
                    elif hasattr(item, "x") and hasattr(item, "y"):
                        ox, oy = item.x, item.y
                    else:
                        continue
                    obs = Obstacle(
                        center=np.array([ox, oy, 0.0]),
                        bbox=BoundingBox(center=np.array([ox, oy, 0.0]), size=np.array([0.5, 0.5, 0.5]), heading=0.0),
                        obstacle_class=ObstacleClass.ROCK,
                        confidence=0.9,
                    )
                    obstacles.append(obs)
                return obstacles

        clusters = clusters_or_scan
        timestamp_ns = timestamp_ns_or_origin if isinstance(timestamp_ns_or_origin, int) else 0

        if self.clusterer and isinstance(clusters, list) and clusters and hasattr(clusters[0], "range_m"):
            clusters = self.clusterer.cluster(clusters)

        obstacles = []
        for cluster in clusters:
            if isinstance(cluster, list):
                if len(cluster) < self.min_points:
                    continue
                # Calculate center from polar points
                avg_range = sum(p.range_m for p in cluster) / len(cluster)
                avg_angle = sum(p.angle_rad for p in cluster) / len(cluster)
                east = avg_range * math.cos(avg_angle)
                north = avg_range * math.sin(avg_angle)
                from core.transforms import EnuPoint
                center = EnuPoint(east, north)
                obs = Obstacle(
                    center=center,
                    point_count=len(cluster),
                    radius_m=0.5,
                    max_range_m=10.0,
                    confidence=0.9,
                    timestamp_ns=timestamp_ns,
                )
                obstacles.append(obs)
            elif isinstance(cluster, Cluster):
                if cluster.size < self.min_points:
                    continue
                distance = float(np.linalg.norm(cluster.centroid[:2]))
                if distance > self.max_distance:
                    continue
                obs_class, confidence = self._classify_cluster(cluster)
                obstacle = Obstacle(
                    center=cluster.centroid,
                    bbox=cluster.bbox,
                    obstacle_class=obs_class,
                    confidence=confidence,
                    timestamp_ns=timestamp_ns,
                )
                obstacles.append(obstacle)

        if isinstance(clusters_or_scan, list) and clusters_or_scan and hasattr(clusters_or_scan[0], "range_m"):
            return obstacles

        return DetectionResult(
            obstacles=obstacles,
            timestamp_ns=timestamp_ns,
        )

    @staticmethod
    def _assess_danger(obstacle: Obstacle, vehicle: Any) -> Obstacle:
        if hasattr(obstacle.center, "east_m") and hasattr(vehicle, "east_m"):
            c_dist = math.hypot(obstacle.center.east_m - vehicle.east_m, obstacle.center.north_m - vehicle.north_m)
        else:
            c_dist = obstacle.distance

        max_d = 0.9 * obstacle.max_range_m
        min_d = obstacle.radius_m

        if c_dist <= min_d:
            obstacle.danger_level = 1.0
        elif c_dist >= max_d:
            obstacle.danger_level = 0.0
        else:
            obstacle.danger_level = (max_d - c_dist) / (max_d - min_d)
        return obstacle

    def _classify_cluster(self, cluster: Cluster) -> Tuple[ObstacleClass, float]:
        """Basit geometri bazlı sınıflandırma."""
        bbox = cluster.bbox
        size = bbox.size
        
        # Boyutlara göre basit kuralllar
        length, width, height = size
        
        # İnsan: dar, uzun (0.5m x 0.5m x 1.5-2m)
        if 0.3 < length < 0.8 and 0.3 < width < 0.8 and 1.2 < height < 2.5:
            return ObstacleClass.PEDESTRIAN, 0.7
        
        # Araç: geniş, uzun (2-5m x 1.5-2.5m x 1.5-3m)
        if 1.5 < length < 6.0 and 1.2 < width < 3.0 and 1.0 < height < 3.5:
            return ObstacleClass.VEHICLE, 0.8
        
        # Bisiklet: orta boy (1-2m x 0.5-1m x 1-1.5m)
        if 0.8 < length < 2.5 and 0.4 < width < 1.2 and 0.8 < height < 1.8:
            return ObstacleClass.BICYCLE, 0.6
        
        # Büyük statik: bina, ağaç
        if length > 5.0 or width > 5.0 or height > 4.0:
            if height > 3.0:
                return ObstacleClass.BUILDING, 0.9
            else:
                return ObstacleClass.TREE, 0.7
        
        # Küçük: kaya, arazi objesi
        if length < 1.0 and width < 1.0 and height < 1.0:
            return ObstacleClass.ROCK, 0.7
        
        # Bilinmeyen
        return ObstacleClass.UNKNOWN, 0.5


@dataclass
class Track:
    """Tek engel track'i - Kalman filtresi durumu."""
    track_id: int
    state: np.ndarray  # [x, y, z, vx, vy, vz] - pozisyon + hız
    covariance: np.ndarray  # 6x6 kovaryans matrisi
    last_update_ns: int
    age: int = 0  # Kaç frame görüldü
    hits: int = 0  # Kaç kez eşleşti
    time_since_update: int = 0  # Kaç frame eşleşmedi
    bbox: Optional[BoundingBox] = None
    obstacle_class: ObstacleClass = ObstacleClass.UNKNOWN

    @property
    def position(self) -> np.ndarray:
        return self.state[:3]

    @property
    def velocity(self) -> np.ndarray:
        return self.state[3:]


class KalmanTracker:
    """Kalman filtresi bazlı multi-object tracker.
    
    Sürekli hız modeli (constant velocity):
        x_k = F @ x_{k-1} + w
        z_k = H @ x_k + v
    
    Parametreler:
        max_age: Track kaç frame eşleşmezse silinir
        min_hits: Track kaç kez eşleşirse yayınlanır
        iou_threshold: Eşleştirme IoU eşiği
    """

    def __init__(
        self,
        max_age: int = 5,
        min_hits: int = 3,
        iou_threshold: float = 0.3,
    ) -> None:
        self.max_age = max_age
        self.min_hits = min_hits
        self.iou_threshold = iou_threshold
        self._tracks: Dict[int, Track] = {}
        self._next_id = 1

    def update(self, detections: DetectionResult, dt: float = 0.1) -> List[Obstacle]:
        """Yeni tespitlerle track'leri güncelle.
        
        Args:
            detections: Frame tespitleri
            dt: Zaman adımı (saniye)
        
        Returns:
            Takip edilen engeller (track_id ile)
        """
        # 1. Predict: Mevcut track'leri ileri tahmin et
        for track in self._tracks.values():
            self._predict(track, dt)
        
        # 2. Associate: Tespit ↔ Track eşleştir (Hungarian)
        matched, unmatched_dets, unmatched_tracks = self._associate(detections)
        
        # 3. Update: Eşleşen track'leri güncelle
        for det_idx, track_id in matched:
            detection = detections.obstacles[det_idx]
            track = self._tracks[track_id]
            self._update_track(track, detection, detections.timestamp_ns)
        
        # 4. Create: Yeni track'ler oluştur
        for det_idx in unmatched_dets:
            detection = detections.obstacles[det_idx]
            self._create_track(detection, detections.timestamp_ns)
        
        # 5. Delete: Eski track'leri sil
        for track_id in list(self._tracks.keys()):
            track = self._tracks[track_id]
            if track.time_since_update > self.max_age:
                del self._tracks[track_id]
        
        # 6. Output: Yeterince eşleşmiş track'leri döndür
        output = []
        for track in self._tracks.values():
            if track.hits >= self.min_hits:
                obstacle = Obstacle(
                    center=track.position,
                    bbox=track.bbox or BoundingBox(
                        center=track.position,
                        size=np.array([1.0, 1.0, 1.0]),
                        heading=0.0,
                    ),
                    obstacle_class=track.obstacle_class,
                    confidence=min(1.0, track.hits / (track.age + 1)),
                    velocity=track.velocity,
                    track_id=track.track_id,
                    timestamp_ns=track.last_update_ns,
                )
                output.append(obstacle)
        
        return output

    def _predict(self, track: Track, dt: float) -> None:
        """Kalman predict adımı."""
        # State transition matrix (constant velocity)
        F = np.eye(6)
        F[:3, 3:] = np.eye(3) * dt
        
        # Process noise (basit)
        Q = np.eye(6) * 0.1
        
        track.state = F @ track.state
        track.covariance = F @ track.covariance @ F.T + Q
        track.time_since_update += 1
        track.age += 1

    def _update_track(self, track: Track, detection: Obstacle, timestamp_ns: int) -> None:
        """Kalman update adımı."""
        # Measurement matrix (sadece pozisyon gözleniyor)
        H = np.zeros((3, 6))
        H[:3, :3] = np.eye(3)
        
        # Measurement noise
        R = np.eye(3) * 0.5
        
        # Innovation
        z = detection.center
        y = z - H @ track.state
        
        # Innovation covariance
        S = H @ track.covariance @ H.T + R
        
        # Kalman gain
        K = track.covariance @ H.T @ np.linalg.inv(S)
        
        # State update
        track.state = track.state + K @ y
        track.covariance = (np.eye(6) - K @ H) @ track.covariance
        
        # Track metadata güncelle
        track.hits += 1
        track.time_since_update = 0
        track.last_update_ns = timestamp_ns
        track.bbox = detection.bbox
        track.obstacle_class = detection.obstacle_class

    def _create_track(self, detection: Obstacle, timestamp_ns: int) -> None:
        """Yeni track oluştur."""
        # Initial state: pozisyon biliniyor, hız 0
        state = np.zeros(6)
        state[:3] = detection.center
        
        # Initial covariance (pozisyon kesin, hız belirsiz)
        covariance = np.eye(6)
        covariance[:3, :3] *= 1.0  # Pozisyon varyansı
        covariance[3:, 3:] *= 10.0  # Hız varyansı
        
        track = Track(
            track_id=self._next_id,
            state=state,
            covariance=covariance,
            last_update_ns=timestamp_ns,
            bbox=detection.bbox,
            obstacle_class=detection.obstacle_class,
            age=1,
            hits=1,
            time_since_update=0,
        )
        
        self._tracks[self._next_id] = track
        self._next_id += 1

    def _associate(
        self, detections: DetectionResult
    ) -> Tuple[List[Tuple[int, int]], List[int], List[int]]:
        """Tespit ↔ Track eşleştirme (Hungarian).
        
        Returns:
            matched: [(det_idx, track_id), ...]
            unmatched_detections: [det_idx, ...]
            unmatched_tracks: [track_id, ...]
        """
        if len(detections) == 0:
            return [], [], list(self._tracks.keys())
        
        if len(self._tracks) == 0:
            return [], list(range(len(detections))), []
        
        # Maliyet matrisi: IoU bazlı
        det_list = detections.obstacles
        track_list = list(self._tracks.values())
        
        cost_matrix = np.zeros((len(det_list), len(track_list)))
        
        for i, detection in enumerate(det_list):
            for j, track in enumerate(track_list):
                # Basit mesafe bazlı (IoU yerine)
                distance = np.linalg.norm(detection.center - track.position)
                cost_matrix[i, j] = distance
        
        # Greedy eşleştirme (Hungarian yerine basit)
        matched = []
        unmatched_dets = set(range(len(det_list)))
        unmatched_tracks = set(t.track_id for t in track_list)
        
        # En küçük maliyetleri eşleştir
        while cost_matrix.size > 0:
            min_idx = np.unravel_index(np.argmin(cost_matrix), cost_matrix.shape)
            det_idx, track_idx = min_idx
            
            if cost_matrix[det_idx, track_idx] > 5.0:  # Eşik aşıldı
                break
            
            track_id = track_list[track_idx].track_id
            matched.append((det_idx, track_id))
            unmatched_dets.discard(det_idx)
            unmatched_tracks.discard(track_id)
            
            # Satır ve sütunu sil
            cost_matrix[det_idx, :] = np.inf
            cost_matrix[:, track_idx] = np.inf
        
        return matched, list(unmatched_dets), list(unmatched_tracks)


class ObstacleTracker:
    """High-level engel tracker - Kalman tracker wrapper."""

    def __init__(self, **kwargs) -> None:
        self.tracker = KalmanTracker(**kwargs)

    def update(self, detections: DetectionResult, dt: float = 0.1) -> DetectionResult:
        """Track güncelle ve takipli engeller döndür."""
        tracked = self.tracker.update(detections, dt)
        return DetectionResult(
            obstacles=tracked,
            timestamp_ns=detections.timestamp_ns,
            frame_id=detections.frame_id,
        )
