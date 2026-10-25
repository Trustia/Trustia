"""
TRUSTIA Otonomi Platformu — Koordinat Dönüşümleri ve Kinematik Durum Modülü.
ISO 8855 Araç Dinamiği Koordinat Sistemi (x: ileri, y: sol, z: yukarı).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Pose2D:
    """2B Düzlemde Araç Pozu (x: Doğu/İleri metre, y: Kuzey/Sol metre, yaw: radyan)."""
    x: float
    y: float
    yaw: float = 0.0

    def distance_to(self, other: Pose2D) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def angle_to(self, other: Pose2D) -> float:
        return math.atan2(other.y - self.y, other.x - self.x)


@dataclass
class KinematicState:
    """Tam Araç Kinematik Durumu."""
    x: float
    y: float
    yaw_rad: float
    velocity_mps: float
    steering_angle_rad: float = 0.0
    acceleration_mps2: float = 0.0
    yaw_rate_radps: float = 0.0

    @property
    def velocity_kmh(self) -> float:
        return self.velocity_mps * 3.6

    @property
    def steering_angle_deg(self) -> float:
        return math.degrees(self.steering_angle_rad)

    def to_pose(self) -> Pose2D:
        return Pose2D(self.x, self.y, self.yaw_rad)

    def local_to_global(self, local_x: float, local_y: float) -> Tuple[float, float]:
        """Araç gövde koordinatındaki (body frame) bir noktayı harita koordinatına çevirir."""
        c = math.cos(self.yaw_rad)
        s = math.sin(self.yaw_rad)
        gx = self.x + (local_x * c - local_y * s)
        gy = self.y + (local_x * s + local_y * c)
        return gx, gy

    def global_to_local(self, gx: float, gy: float) -> Tuple[float, float]:
        """Harita koordinatındaki bir noktayı araç gövde koordinatına çevirir."""
        dx = gx - self.x
        dy = gy - self.y
        c = math.cos(self.yaw_rad)
        s = math.sin(self.yaw_rad)
        lx = dx * c + dy * s
        ly = -dx * s + dy * c
        return lx, ly


def normalize_angle(angle_rad: float) -> float:
    """Açıyı [-pi, pi] aralığına normalize eder."""
    while angle_rad > math.pi:
        angle_rad -= 2.0 * math.pi
    while angle_rad < -math.pi:
        angle_rad += 2.0 * math.pi
    return angle_rad
