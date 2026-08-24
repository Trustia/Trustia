"""
TRUSTIA Siber ve Elektronik Harp Koruması (Sistem 5) — Anti-GPS Spoofing & Karıştırma Dedektörü.

Savaş Alanı Elektronik Harp Tehditlerine Karşı:
  * GNSS Hız Vektörü ile IMU Fiziksel İvme Entegrasyonu Karşılaştırması
  * Ani Koordinat/HDOP Sıçraması ve Uydu Sayısı Anomali Tespiti
  * Sahte Sinyal (Spoofing) durumunda GPS'i devreden çıkarıp %100 LiDAR/ESKF SLAM moduna kilitleme
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple


class GpsSecurityStatus(Enum):
    """GPS Güvenlik ve Doğruluk Durumu."""
    TRUSTED = "TRUSTED"
    SUSPECTED = "SUSPECTED"
    SPOOFED_ATTACK = "SPOOFED_ATTACK"
    JAMMED_DENIED = "JAMMED_DENIED"


@dataclass
class GpsFix:
    """GNSS/RTK Alıcı Ölçüm Paketi."""
    timestamp_s: float
    east_m: float
    north_m: float
    speed_mps: float
    heading_deg: float
    hdop: float = 1.0
    num_satellites: int = 12
    fix_type: int = 3  # 0: No fix, 2: 2D, 3: 3D, 4: RTK Float, 5: RTK Fixed


class AntiGpsSpoofGuard:
    """Elektronik Harp Sahte GPS (Spoofing) ve Karıştırma (Jamming) Kalkanı."""

    def __init__(
        self,
        max_speed_discrepancy_mps: float = 4.0,
        max_pos_jump_m: float = 15.0,
        min_satellites: int = 4,
    ) -> None:
        self.max_speed_discrepancy_mps = max_speed_discrepancy_mps
        self.max_pos_jump_m = max_pos_jump_m
        self.min_satellites = min_satellites

        self.last_valid_gps: Optional[GpsFix] = None
        self.status = GpsSecurityStatus.TRUSTED
        self.spoof_counter = 0
        self.isolation_active = False

    def evaluate_signal(
        self,
        gps: GpsFix,
        imu_speed_estimate_mps: float,
        imu_accel_norm: float,
    ) -> Tuple[GpsSecurityStatus, bool]:
        """GNSS sinyalini fiziksel IMU verileriyle çapraz sorgular.

        Döndürür: (GpsSecurityStatus, use_gps_in_fusion: bool)
        """
        # 1. Jamming (Karıştırma) Kontrolü
        if gps.fix_type < 2 or gps.num_satellites < self.min_satellites:
            self.status = GpsSecurityStatus.JAMMED_DENIED
            return (self.status, False)

        # 2. İlk Geçerli Ölçüm Başlatma
        if self.last_valid_gps is None:
            self.last_valid_gps = gps
            self.status = GpsSecurityStatus.TRUSTED
            return (self.status, True)

        dt = max(0.01, gps.timestamp_s - self.last_valid_gps.timestamp_s)

        # 3. İmkansız Pozisyon Sıçraması (Teleportation check)
        dist_jump = math.hypot(gps.east_m - self.last_valid_gps.east_m, gps.north_m - self.last_valid_gps.north_m)
        apparent_speed = dist_jump / dt

        # 4. IMU Hız Tutarsızlığı (Physical Acceleration vs GPS Reported Velocity)
        speed_diff = abs(gps.speed_mps - imu_speed_estimate_mps)

        # Anomali Değerlendirmesi
        is_anomalous = False
        if speed_diff > self.max_speed_discrepancy_mps:
            is_anomalous = True
        if dist_jump > (self.max_pos_jump_m + imu_speed_estimate_mps * dt * 2.0):
            is_anomalous = True
        if gps.hdop > 8.0:
            is_anomalous = True

        if is_anomalous:
            self.spoof_counter += 1
            if self.spoof_counter >= 2:
                self.status = GpsSecurityStatus.SPOOFED_ATTACK
                self.isolation_active = True
            else:
                self.status = GpsSecurityStatus.SUSPECTED
            return (self.status, False)
        else:
            self.spoof_counter = max(0, self.spoof_counter - 1)
            if self.spoof_counter == 0:
                self.status = GpsSecurityStatus.TRUSTED
                self.isolation_active = False
            self.last_valid_gps = gps
            return (self.status, True)

    def is_safe_to_navigate_gps(self) -> bool:
        """GPS verisinin otonom navigasyonda kullanılıp kullanılamayacağı."""
        return (self.status == GpsSecurityStatus.TRUSTED) and not self.isolation_active
