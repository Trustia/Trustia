"""
TRUSTIA Algı Sistemi - Temel veri yapıları.

Nokta bulutu, lazer tarama, engel ve bounding box tanımları.
NumPy tabanlı performanslı veri yapıları.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional, Tuple

import numpy as np


class ObstacleClass(IntEnum):
    """Engel sınıfları - AI modülü çıktısıyla uyumlu."""
    UNKNOWN = 0
    VEHICLE = 1
    PEDESTRIAN = 2
    BICYCLE = 3
    ROCK = 4
    TREE = 5
    BUILDING = 6
    TERRAIN = 7


@dataclass(frozen=True)
class Point3D:
    """3D nokta - konum + yoğunluk."""
    x: float
    y: float
    z: float
    intensity: float = 0.0

    def distance_to(self, other: "Point3D") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def to_array(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z, self.intensity])


@dataclass
class PointCloud:
    """3D nokta bulutu - NumPy tabanlı performanslı işleme.
    
    points: (N, 3) veya (N, 4) array (x, y, z) veya (x, y, z, intensity)
    timestamp_ns: Yakalama zamanı
    frame_id: Koordinat çerçevesi tanımlayıcı
    """
    points: np.ndarray
    timestamp_ns: int = 0
    frame_id: str = "lidar"

    def __post_init__(self):
        if self.points.ndim != 2:
            raise ValueError(f"points 2D array olmalı, alınan: {self.points.shape}")
        if self.points.shape[1] not in (3, 4):
            raise ValueError(f"points (N,3) veya (N,4) olmalı, alınan: {self.points.shape}")

    @property
    def size(self) -> int:
        return self.points.shape[0]

    @property
    def has_intensity(self) -> bool:
        return self.points.shape[1] == 4

    def xyz(self) -> np.ndarray:
        """(N, 3) konum array'i döndürür."""
        return self.points[:, :3]

    def intensity(self) -> Optional[np.ndarray]:
        """(N,) yoğunluk array'i döndürür, yoksa None."""
        if self.has_intensity:
            return self.points[:, 3]
        return None

    def filter_by_indices(self, indices: np.ndarray) -> "PointCloud":
        """Belirtilen indislerdeki noktalarla yeni bulut oluşturur."""
        return PointCloud(
            points=self.points[indices],
            timestamp_ns=self.timestamp_ns,
            frame_id=self.frame_id,
        )

    def filter_by_mask(self, mask: np.ndarray) -> "PointCloud":
        """Boolean mask ile filtreleme."""
        return PointCloud(
            points=self.points[mask],
            timestamp_ns=self.timestamp_ns,
            frame_id=self.frame_id,
        )

    def transform(self, matrix: np.ndarray) -> "PointCloud":
        """4x4 homojen dönüşüm matrisi uygular."""
        if matrix.shape != (4, 4):
            raise ValueError("Dönüşüm matrisi 4x4 olmalı")
        xyz = self.xyz()
        ones = np.ones((xyz.shape[0], 1))
        homogeneous = np.hstack([xyz, ones])
        transformed = (matrix @ homogeneous.T).T[:, :3]
        if self.has_intensity:
            new_points = np.hstack([transformed, self.intensity()[:, None]])
        else:
            new_points = transformed
        return PointCloud(
            points=new_points,
            timestamp_ns=self.timestamp_ns,
            frame_id=self.frame_id,
        )

    def downsample_random(self, target_size: int, seed: int = 0) -> "PointCloud":
        """Rastgele örnekleme ile nokta sayısını azalt."""
        if self.size <= target_size:
            return self
        rng = np.random.RandomState(seed)
        indices = rng.choice(self.size, size=target_size, replace=False)
        return self.filter_by_indices(indices)

    def bounds(self) -> Tuple[np.ndarray, np.ndarray]:
        """Bulut sınırları: (min_xyz, max_xyz)."""
        xyz = self.xyz()
        return xyz.min(axis=0), xyz.max(axis=0)

    @classmethod
    def from_points(cls, points: List[Point3D], timestamp_ns: int = 0) -> "PointCloud":
        """Point3D listesinden bulut oluştur."""
        array = np.array([p.to_array() for p in points])
        return cls(points=array, timestamp_ns=timestamp_ns)

    @classmethod
    def empty(cls) -> "PointCloud":
        """Boş bulut."""
        return cls(points=np.zeros((0, 3)))


@dataclass
class LaserScan:
    """2D lazer tarama - döner LiDAR."""
    ranges: np.ndarray  # (N,) mesafeler
    angles: np.ndarray  # (N,) açılar (radyan)
    intensities: Optional[np.ndarray] = None  # (N,) yoğunluklar
    timestamp_ns: int = 0
    frame_id: str = "laser"
    range_min: float = 0.0
    range_max: float = 100.0
    angle_min: float = -math.pi
    angle_max: float = math.pi

    def __post_init__(self):
        if self.ranges.shape != self.angles.shape:
            raise ValueError("ranges ve angles aynı boyutta olmalı")
        if self.intensities is not None:
            if self.intensities.shape != self.ranges.shape:
                raise ValueError("intensities ranges ile aynı boyutta olmalı")

    @property
    def size(self) -> int:
        return self.ranges.shape[0]

    def to_pointcloud(self, z: float = 0.0) -> PointCloud:
        """2D taramayı 3D buluta çevir (z sabit)."""
        valid = np.isfinite(self.ranges)
        ranges = self.ranges[valid]
        angles = self.angles[valid]
        x = ranges * np.cos(angles)
        y = ranges * np.sin(angles)
        z_arr = np.full_like(x, z)
        if self.intensities is not None:
            intensities = self.intensities[valid]
            points = np.stack([x, y, z_arr, intensities], axis=1)
        else:
            points = np.stack([x, y, z_arr], axis=1)
        return PointCloud(
            points=points,
            timestamp_ns=self.timestamp_ns,
            frame_id=self.frame_id,
        )

    def filter_range(self, min_range: float, max_range: float) -> "LaserScan":
        """Mesafe filtresi."""
        mask = (self.ranges >= min_range) & (self.ranges <= max_range)
        return LaserScan(
            ranges=self.ranges[mask],
            angles=self.angles[mask],
            intensities=self.intensities[mask] if self.intensities is not None else None,
            timestamp_ns=self.timestamp_ns,
            frame_id=self.frame_id,
            range_min=self.range_min,
            range_max=self.range_max,
            angle_min=self.angle_min,
            angle_max=self.angle_max,
        )


@dataclass
class BoundingBox:
    """3D bounding box - engel etrafında kutu."""
    center: np.ndarray  # (3,) merkez konum
    size: np.ndarray    # (3,) boyutlar (uzunluk, genişlik, yükseklik)
    heading: float      # Baş açısı (radyan, z-axis rotation)

    @property
    def volume(self) -> float:
        return float(np.prod(self.size))

    @property
    def corners(self) -> np.ndarray:
        """8 köşe noktası (8, 3)."""
        l, w, h = self.size / 2.0
        corners_local = np.array([
            [-l, -w, -h], [l, -w, -h], [l, w, -h], [-l, w, -h],
            [-l, -w, h], [l, -w, h], [l, w, h], [-l, w, h],
        ])
        # Rotasyon (z-axis)
        cos_h = math.cos(self.heading)
        sin_h = math.sin(self.heading)
        rot = np.array([
            [cos_h, -sin_h, 0],
            [sin_h, cos_h, 0],
            [0, 0, 1],
        ])
        corners_world = (rot @ corners_local.T).T + self.center
        return corners_world

    def contains(self, point: np.ndarray) -> bool:
        """Nokta kutu içinde mi?"""
        # Noktayı yerel koordinata çevir
        cos_h = math.cos(-self.heading)
        sin_h = math.sin(-self.heading)
        rot_inv = np.array([
            [cos_h, -sin_h, 0],
            [sin_h, cos_h, 0],
            [0, 0, 1],
        ])
        local = rot_inv @ (point - self.center)
        half = self.size / 2.0
        return np.all(np.abs(local) <= half)

    def iou(self, other: "BoundingBox") -> float:
        """2D IoU (z-axis projection) - basit yaklaşım."""
        # Basitleştirilmiş 2D overlap hesabı
        dx = abs(self.center[0] - other.center[0])
        dy = abs(self.center[1] - other.center[1])
        overlap_x = max(0, (self.size[0] + other.size[0]) / 2.0 - dx)
        overlap_y = max(0, (self.size[1] + other.size[1]) / 2.0 - dy)
        intersection = overlap_x * overlap_y
        area1 = self.size[0] * self.size[1]
        area2 = other.size[0] * other.size[1]
        union = area1 + area2 - intersection
        return intersection / union if union > 0 else 0.0


@dataclass
class Obstacle:
    """Tespit edilen engel - 3D konum, sınıf, bounding box."""
    center: Any = None
    bbox: Optional[BoundingBox] = None
    obstacle_class: ObstacleClass = ObstacleClass.UNKNOWN
    confidence: float = 0.0
    velocity: Optional[np.ndarray] = None
    track_id: Optional[int] = None
    id: Optional[int] = None
    radius_m: float = 0.5
    point_count: int = 1
    max_range_m: float = 10.0
    danger_level: float = 0.0
    timestamp_ns: int = 0

    def __post_init__(self):
        if self.id is not None and self.track_id is None:
            self.track_id = self.id
        elif self.track_id is not None and self.id is None:
            self.id = self.track_id

    @property
    def distance(self) -> float:
        """Sensöre olan mesafe (center'dan)."""
        if isinstance(self.center, np.ndarray):
            return float(np.linalg.norm(self.center[:2]))
        if hasattr(self.center, "east_m") and hasattr(self.center, "north_m"):
            return math.hypot(self.center.east_m, self.center.north_m)
        return 0.0

    def distance_to(self, point: Any) -> float:
        if hasattr(self.center, "east_m") and hasattr(point, "east_m"):
            dx = self.center.east_m - point.east_m
            dy = self.center.north_m - point.north_m
            return max(0.0, math.hypot(dx, dy) - self.radius_m)
        if isinstance(self.center, np.ndarray) and hasattr(point, "x"):
            return max(0.0, math.hypot(self.center[0] - point.x, self.center[1] - point.y) - self.radius_m)
        return max(0.0, self.distance - self.radius_m)

    def to_dict(self) -> dict:
        return {
            "center": self.center.tolist() if isinstance(self.center, np.ndarray) else [getattr(self.center, "east_m", 0), getattr(self.center, "north_m", 0), 0],
            "class": self.obstacle_class.name,
            "confidence": self.confidence,
            "track_id": self.track_id,
            "distance": self.distance,
        }


@dataclass(frozen=True)
class LaserPoint:
    """Polar/2D Lazer noktası desteği."""
    range_m: float
    angle_rad: float = 0.0
    elevation_rad: float = 0.0


class FieldOfView:
    """Görüş alanı tanımlayıcı."""
    def __init__(
        self,
        min_angle_rad: float = -math.pi,
        max_angle_rad: float = math.pi,
        max_range_m: float = 100.0,
        min_range_m: float = 0.1,
    ) -> None:
        if min_angle_rad >= max_angle_rad or min_range_m >= max_range_m:
            from core.errors import SensorError
            raise SensorError("Invalid FieldOfView parameters.")
        self.min_angle_rad = min_angle_rad
        self.max_angle_rad = max_angle_rad
        self.max_range_m = max_range_m
        self.min_range_m = min_range_m

    @property
    def angular_width_deg(self) -> float:
        return math.degrees(self.max_angle_rad - self.min_angle_rad)

    def contains(self, point: Any) -> bool:
        ang = getattr(point, "angle_rad", 0.0)
        rng = getattr(point, "range_m", 0.0)
        return (self.min_angle_rad <= ang <= self.max_angle_rad) and (self.min_range_m <= rng <= self.max_range_m)

    def coverage_ratio(self, points: List[Any]) -> float:
        if not points:
            return 0.0
        inside = sum(1 for p in points if self.contains(p))
        return inside / len(points)

