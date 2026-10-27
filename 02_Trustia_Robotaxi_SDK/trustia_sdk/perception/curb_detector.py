"""
TRUSTIA Robotaksi SDK — 3B LiDAR Kaldırım Taşı (Curb) ve Yol Sınırı Algılama Modülü.
Yol çizgileri silinmiş veya hava yağışlı olsa bile 2.6 Milyon nokta/saniye LiDAR
yükseklik sıçraması (8 cm - 28 cm) ve zemin yapısından şerit koridorunu çıkarır.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class RoadCorridorResult:
    left_curb_y_m: float
    right_curb_y_m: float
    corridor_width_m: float
    center_offset_m: float
    valid_corridor: bool


class CurbBoundaryDetector:
    """3B LiDAR nokta bulutundan kaldırım taşı basamağını ve yol sınırını tespit eder."""

    def __init__(self, min_curb_h_m: float = 0.08, max_curb_h_m: float = 0.28) -> None:
        self.min_curb_h = min_curb_h_m
        self.max_curb_h = max_curb_h_m

    def detect_corridor(
        self,
        lidar_points_xyz: List[Tuple[float, float, float]],
        road_surface_z_m: float = 0.0,
    ) -> RoadCorridorResult:
        left_candidates: List[float] = []
        right_candidates: List[float] = []

        for x, y, z in lidar_points_xyz:
            if 0.5 <= x <= 35.0:
                dz = z - road_surface_z_m
                if self.min_curb_h <= dz <= self.max_curb_h:
                    if y > 0.8:
                        left_candidates.append(y)
                    elif y < -0.8:
                        right_candidates.append(y)

        left_y = sorted(left_candidates)[len(left_candidates) // 2] if left_candidates else 3.5
        right_y = sorted(right_candidates)[len(right_candidates) // 2] if right_candidates else -3.5
        width = max(0.0, left_y - right_y)
        center = (left_y + right_y) / 2.0
        return RoadCorridorResult(
            left_curb_y_m=round(left_y, 3),
            right_curb_y_m=round(right_y, 3),
            corridor_width_m=round(width, 3),
            center_offset_m=round(center, 3),
            valid_corridor=(width >= 2.2),
        )
