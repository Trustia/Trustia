"""
TRUSTIA SLAM - Temel veri yapıları.

Pose (pozisyon + rotasyon), odometry, scan match sonuçları.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np


@dataclass
class Pose2D:
    """2D pose - (x, y, theta)."""
    x_m: float
    y_m: float
    heading_rad: float = 0.0

    def to_matrix(self) -> np.ndarray:
        """3x3 homojen dönüşüm matrisi."""
        c = math.cos(self.heading_rad)
        s = math.sin(self.heading_rad)
        return np.array([
            [c, -s, self.x_m],
            [s, c, self.y_m],
            [0, 0, 1],
        ])

    @classmethod
    def from_matrix(cls, matrix: np.ndarray) -> "Pose2D":
        """3x3 matris → Pose2D."""
        x = float(matrix[0, 2])
        y = float(matrix[1, 2])
        theta = math.atan2(matrix[1, 0], matrix[0, 0])
        return cls(x_m=x, y_m=y, heading_rad=theta)

    def transform_point(self, point: Tuple[float, float]) -> Tuple[float, float]:
        """Noktayı bu pose'un koordinat sistemine dönüştür."""
        c = math.cos(self.heading_rad)
        s = math.sin(self.heading_rad)
        px, py = point
        x = c * px - s * py + self.x_m
        y = s * px + c * py + self.y_m
        return x, y

    def inverse(self) -> "Pose2D":
        """Ters dönüşüm."""
        c = math.cos(self.heading_rad)
        s = math.sin(self.heading_rad)
        x = -(c * self.x_m + s * self.y_m)
        y = -(-s * self.x_m + c * self.y_m)
        return Pose2D(x_m=x, y_m=y, heading_rad=-self.heading_rad)

    def compose(self, other: "Pose2D") -> "Pose2D":
        """İki pose'u birleştir (T1 * T2)."""
        matrix = self.to_matrix() @ other.to_matrix()
        return Pose2D.from_matrix(matrix)

    def distance_to(self, other: "Pose2D") -> float:
        """Euclidean mesafe (pozisyon)."""
        dx = self.x_m - other.x_m
        dy = self.y_m - other.y_m
        return math.sqrt(dx * dx + dy * dy)

    def angle_diff(self, other: "Pose2D") -> float:
        """Açı farkı [-π, π]."""
        diff = other.heading_rad - self.heading_rad
        while diff > math.pi:
            diff -= 2 * math.pi
        while diff < -math.pi:
            diff += 2 * math.pi
        return diff

    def to_array(self) -> np.ndarray:
        """[x, y, theta] array."""
        return np.array([self.x_m, self.y_m, self.heading_rad])

    @classmethod
    def from_array(cls, arr: np.ndarray) -> "Pose2D":
        return cls(x_m=float(arr[0]), y_m=float(arr[1]), heading_rad=float(arr[2]))

    def __repr__(self) -> str:
        return f"Pose2D(x={self.x_m:.3f}, y={self.y_m:.3f}, θ={math.degrees(self.heading_rad):.1f}°)"


@dataclass
class Pose3D:
    """3D pose - pozisyon + kuaterniyon rotasyon."""
    position: np.ndarray  # (3,) [x, y, z]
    quaternion: np.ndarray  # (4,) [qx, qy, qz, qw]

    def to_matrix(self) -> np.ndarray:
        """4x4 homojen dönüşüm matrisi."""
        qx, qy, qz, qw = self.quaternion
        
        # Quaternion → rotation matrix
        R = np.array([
            [1 - 2*(qy**2 + qz**2), 2*(qx*qy - qz*qw), 2*(qx*qz + qy*qw)],
            [2*(qx*qy + qz*qw), 1 - 2*(qx**2 + qz**2), 2*(qy*qz - qx*qw)],
            [2*(qx*qz - qy*qw), 2*(qy*qz + qx*qw), 1 - 2*(qx**2 + qy**2)],
        ])
        
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = self.position
        return T

    @classmethod
    def from_matrix(cls, matrix: np.ndarray) -> "Pose3D":
        """4x4 matris → Pose3D."""
        position = matrix[:3, 3]
        
        # Rotation matrix → quaternion
        R = matrix[:3, :3]
        trace = np.trace(R)
        
        if trace > 0:
            s = 0.5 / math.sqrt(trace + 1.0)
            qw = 0.25 / s
            qx = (R[2, 1] - R[1, 2]) * s
            qy = (R[0, 2] - R[2, 0]) * s
            qz = (R[1, 0] - R[0, 1]) * s
        else:
            if R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
                s = 2.0 * math.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2])
                qw = (R[2, 1] - R[1, 2]) / s
                qx = 0.25 * s
                qy = (R[0, 1] + R[1, 0]) / s
                qz = (R[0, 2] + R[2, 0]) / s
            elif R[1, 1] > R[2, 2]:
                s = 2.0 * math.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2])
                qw = (R[0, 2] - R[2, 0]) / s
                qx = (R[0, 1] + R[1, 0]) / s
                qy = 0.25 * s
                qz = (R[1, 2] + R[2, 1]) / s
            else:
                s = 2.0 * math.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1])
                qw = (R[1, 0] - R[0, 1]) / s
                qx = (R[0, 2] + R[2, 0]) / s
                qy = (R[1, 2] + R[2, 1]) / s
                qz = 0.25 * s
        
        quaternion = np.array([qx, qy, qz, qw])
        return cls(position=position, quaternion=quaternion)


@dataclass
class OdometryMeasurement:
    """Tek odometry ölçümü."""
    delta_distance_m: float
    delta_heading_rad: float
    timestamp_ns: int = 0
    covariance: Optional[np.ndarray] = None  # 2x2 [dist, heading]

    def to_pose2d(self) -> Pose2D:
        """Göreli hareket → Pose2D."""
        return Pose2D(
            x_m=self.delta_distance_m * math.cos(self.delta_heading_rad / 2),
            y_m=self.delta_distance_m * math.sin(self.delta_heading_rad / 2),
            heading_rad=self.delta_heading_rad,
        )


@dataclass
class ScanMatch:
    """ICP scan matching sonucu."""
    transform: Pose2D  # Bulunan dönüşüm
    fitness_score: float  # Eşleşme kalitesi (düşük = iyi)
    inlier_rmse: float  # RMS hata (metre)
    converged: bool
    iterations: int


@dataclass
class LoopClosure:
    """Loop closure tespiti."""
    current_node_id: int
    matched_node_id: int
    relative_pose: Pose2D
    confidence: float
    distance_m: float  # Graf üzerinde mesafe
    timestamp_ns: int = 0


def angular_difference(a: float, b: float) -> float:
    """İki açı arasındaki en kısa farkı hesaplar."""
    diff = abs(a - b) % (2 * math.pi)
    if diff > math.pi:
        diff = 2 * math.pi - diff
    return diff

