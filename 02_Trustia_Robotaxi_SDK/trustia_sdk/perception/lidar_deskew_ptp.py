"""
TRUSTIA IEEE 1588 PTP Hassas Zaman Senkronizasyonu ve 3B LiDAR Hareket Bozulması Düzeltme (Deskewing)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class PtpSyncStatus:
    master_clock_id: str
    offset_us: float
    jitter_us: float
    synchronized: bool
    sotif_degraded: bool
    detail: str


@dataclass(frozen=True)
class RawTimedPoint3D:
    x: float
    y: float
    z: float
    relative_time_s: float


class LidarMotionDeskewer:
    """IEEE 1588v2 PTP saat denetleyicisi ve 3B LiDAR hareket bozulması düzeltici."""

    def __init__(
        self,
        max_nominal_ptp_offset_us: float = 100.0,
        max_safe_ptp_offset_us: float = 1000.0,
    ) -> None:
        self.max_nominal_ptp_offset_us = max_nominal_ptp_offset_us
        self.max_safe_ptp_offset_us = max_safe_ptp_offset_us

    def evaluate_ptp_sync(
        self,
        master_clock_id: str,
        offset_us: float,
        jitter_us: float,
    ) -> PtpSyncStatus:
        abs_off = abs(offset_us)
        if abs_off <= self.max_nominal_ptp_offset_us and jitter_us <= 250.0:
            return PtpSyncStatus(
                master_clock_id=master_clock_id,
                offset_us=offset_us,
                jitter_us=jitter_us,
                synchronized=True,
                sotif_degraded=False,
                detail="PTP Senkronize",
            )
        if abs_off <= self.max_safe_ptp_offset_us:
            return PtpSyncStatus(
                master_clock_id=master_clock_id,
                offset_us=offset_us,
                jitter_us=jitter_us,
                synchronized=True,
                sotif_degraded=True,
                detail="PTP Sapması Yüksek (SOTIF Uyarı)",
            )
        return PtpSyncStatus(
            master_clock_id=master_clock_id,
            offset_us=offset_us,
            jitter_us=jitter_us,
            synchronized=False,
            sotif_degraded=True,
            detail="Kritik PTP Senkron Kaybı",
        )

    def deskew_scan(
        self,
        points: List[RawTimedPoint3D],
        vx_mps: float,
        vy_mps: float,
        yaw_rate_rad_s: float,
        sweep_duration_s: float = 0.050,
    ) -> List[Tuple[float, float, float]]:
        corrected: List[Tuple[float, float, float]] = []
        for pt in points:
            dt = max(0.0, sweep_duration_s - pt.relative_time_s)
            px = pt.x - vx_mps * dt
            py = pt.y - vy_mps * dt
            dtheta = yaw_rate_rad_s * dt
            cos_t = math.cos(-dtheta)
            sin_t = math.sin(-dtheta)
            corrected.append((cos_t * px - sin_t * py, sin_t * px + cos_t * py, pt.z))
        return corrected
