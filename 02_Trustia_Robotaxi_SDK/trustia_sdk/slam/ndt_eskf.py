"""
TRUSTIA Otonomi Platformu — 3D LiDAR NDT & 400 Hz ESKF Konumlandırma Motoru.
GPS-Kısıtlı Alanlar (Tüneller, Katlı Otoparklar, Şehir Kanyonları) için Kesintisiz Konumlandırma.

Standart: ISO 26262 ASIL-D & ISO 8855 Araç Koordinat Sistemi.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import List, Tuple, Optional
from trustia_sdk.core.transforms import Pose2D, KinematicState, normalize_angle


@dataclass
class ImuMeasurement:
    """IMU 6-Eksen Ölçüm Verisi (400 Hz)."""
    accel_x_mps2: float
    accel_y_mps2: float
    accel_z_mps2: float
    gyro_z_radps: float
    timestamp: float


class ErrorStateKalmanFilter:
    """
    400 Hz Error-State Kalman Filtresi (ESKF).
    Yüksek frekanslı IMU entegrasyonu ile düşük frekanslı LiDAR/GNSS düzeltmelerini birleştirir.
    """

    def __init__(self, initial_pose: Pose2D) -> None:
        self.x = initial_pose.x
        self.y = initial_pose.y
        self.yaw = initial_pose.yaw
        self.v_x = 0.0
        self.v_y = 0.0
        self.yaw_rate = 0.0

        # Kovaryans Matrisi Köşegenleri (Hata Belirsizliği)
        self.P_pos = 0.05  # 5 cm başlangıç belirsizliği
        self.P_vel = 0.02
        self.P_yaw = 0.005 # ~0.3 derece başlangıç yaw belirsizliği

        self.last_update_time = time.time()

    def predict(self, imu: ImuMeasurement, dt_s: float = 0.0025) -> KinematicState:
        """Nominal durum tahmini (400 Hz IMU entegrasyonu)."""
        dt = max(0.0001, min(0.05, dt_s))

        # Gövde ivmesini harita çerçevesine dönüştür
        c = math.cos(self.yaw)
        s = math.sin(self.yaw)
        acc_x_map = imu.accel_x_mps2 * c - imu.accel_y_mps2 * s
        acc_y_map = imu.accel_x_mps2 * s + imu.accel_y_mps2 * c

        # Hız ve konum integrasyonu
        self.v_x += acc_x_map * dt
        self.v_y += acc_y_map * dt
        self.x += self.v_x * dt
        self.y += self.v_y * dt

        # Yaw integrasyonu
        self.yaw_rate = imu.gyro_z_radps
        self.yaw = normalize_angle(self.yaw + self.yaw_rate * dt)

        # Kovaryans büyümesi (Süreç Gürültüsü)
        self.P_pos += 0.0001 * dt
        self.P_yaw += 0.00005 * dt

        total_v = math.hypot(self.v_x, self.v_y)
        return KinematicState(
            x=self.x,
            y=self.y,
            yaw_rad=self.yaw,
            velocity_mps=total_v,
            yaw_rate_radps=self.yaw_rate
        )

    def correct_with_lidar_ndt(self, observed_x: float, observed_y: float, observed_yaw: float, ndt_score: float) -> None:
        """3D LiDAR NDT tarama eşleşmesi ile hata durumunu düzeltir (20 Hz)."""
        # NDT eşleşme kalitesine göre Kalman Kazancı (K) hesabı
        r_pos = 0.04 / max(0.2, ndt_score) # İyi skorda düşük ölçüm gürültüsü
        r_yaw = 0.002 / max(0.2, ndt_score)

        k_pos = self.P_pos / (self.P_pos + r_pos)
        k_yaw = self.P_yaw / (self.P_yaw + r_yaw)

        # Yenilik (Innovation / Residual)
        res_x = observed_x - self.x
        res_y = observed_y - self.y
        res_yaw = normalize_angle(observed_yaw - self.yaw)

        # Durum güncellemesi
        self.x += k_pos * res_x
        self.y += k_pos * res_y
        self.yaw = normalize_angle(self.yaw + k_yaw * res_yaw)

        # Kovaryans güncellemesi
        self.P_pos = (1.0 - k_pos) * self.P_pos
        self.P_yaw = (1.0 - k_yaw) * self.P_yaw

    def get_state(self) -> KinematicState:
        return KinematicState(
            x=self.x,
            y=self.y,
            yaw_rad=self.yaw,
            velocity_mps=math.hypot(self.v_x, self.v_y),
            yaw_rate_radps=self.yaw_rate
        )
