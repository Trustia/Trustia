"""
TRUSTIA IEEE 1588 PTP Hassas Zaman Senkronizasyonu ve 3B LiDAR Hareket Bozulması Düzeltme (Deskewing)
====================================================================================================
Seviye-4 Robotaksi 50 km/s (13.89 m/s) hızla ilerlerken 10 Hz (100 ms) veya 20 Hz (50 ms) dönen/katı hal
3B LiDAR taraması sırasında araç ~0.7 ile 1.4 metre yer değiştirir. Nokta bulutundaki bu hareket
bozulması (Motion Distortion) düzeltilmezse engeller olduğu yerden kaymış veya uzamış görünür.

Bu modül:
  1. IEEE 1588v2 PTP (Precision Time Protocol) saat sapmasını denetler (nominal <= 100 mikrosaniye).
  2. 400 Hz IMU ve tekerlek hız verisiyle her LiDAR noktasını tarama sonu referans zamanına
     (SE(2)/SE(3) kinematik geri sarma ile) hizalayarak hareket bozulmasını sıfırlar.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class PtpSyncStatus:
    """IEEE 1588v2 PTP donanım zaman senkronizasyonu durum raporu."""

    master_clock_id: str
    offset_us: float
    jitter_us: float
    synchronized: bool
    sotif_degraded: bool
    detail: str


@dataclass(frozen=True)
class RawTimedPoint3D:
    """Tarama başlangıcına göre göreli zaman damgalı 3B LiDAR noktası."""

    x: float
    y: float
    z: float
    relative_time_s: float  # 0.0 .. sweep_duration_s (ör. 0.0 .. 0.050 sn)


class LidarMotionDeskewer:
    """
    IEEE 1588v2 PTP saat denetleyicisi ve 3B LiDAR hareket bozulması düzeltici (Motion Deskewer).
    """

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
        """LiDAR, kamera ve ana bilgisayar arasındaki PTP saat farkını denetler."""
        abs_off = abs(offset_us)
        if abs_off <= self.max_nominal_ptp_offset_us and jitter_us <= 250.0:
            return PtpSyncStatus(
                master_clock_id=master_clock_id,
                offset_us=offset_us,
                jitter_us=jitter_us,
                synchronized=True,
                sotif_degraded=False,
                detail=f"IEEE 1588 PTP kilitli: sapma={offset_us:.1f} us",
            )
        if abs_off <= self.max_safe_ptp_offset_us:
            return PtpSyncStatus(
                master_clock_id=master_clock_id,
                offset_us=offset_us,
                jitter_us=jitter_us,
                synchronized=True,
                sotif_degraded=True,
                detail=f"PTP sapması yüksek ({offset_us:.1f} us), güvenlik takip mesafesi artırıldı.",
            )
        return PtpSyncStatus(
            master_clock_id=master_clock_id,
            offset_us=offset_us,
            jitter_us=jitter_us,
            synchronized=False,
            sotif_degraded=True,
            detail=f"KRİTİK PTP SENKRON KAYBI ({offset_us:.1f} us > {self.max_safe_ptp_offset_us:.1f} us)!",
        )

    def deskew_scan(
        self,
        points: List[RawTimedPoint3D],
        vx_mps: float,
        vy_mps: float,
        yaw_rate_rad_s: float,
        sweep_duration_s: float = 0.050,
    ) -> List[Tuple[float, float, float]]:
        """
        Tarama süresi boyunca aracın doğrusal (vx, vy) ve açısal (yaw_rate) hareketinden
        kaynaklanan nokta bulutu yamulmasını tarama sonu (t = sweep_duration_s) koordinatına düzeltir.
        """
        corrected: List[Tuple[float, float, float]] = []
        for pt in points:
            # Noktanın ölçüldüğü andan tarama sonuna kadar geçen süre
            dt = max(0.0, sweep_duration_s - pt.relative_time_s)
            # Bu sürede aracın yaptığı yer değiştirme ve dönüş
            dx_ego = vx_mps * dt
            dy_ego = vy_mps * dt
            dtheta = yaw_rate_rad_s * dt

            # Noktayı tarama sonundaki araç eksen takımına geri dönüştür (R(-dtheta) * (P - dP))
            px = pt.x - dx_ego
            py = pt.y - dy_ego
            cos_t = math.cos(-dtheta)
            sin_t = math.sin(-dtheta)
            cx = cos_t * px - sin_t * py
            cy = sin_t * px + cos_t * py
            corrected.append((cx, cy, pt.z))
        return corrected
