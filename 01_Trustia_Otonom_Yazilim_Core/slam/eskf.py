"""
TRUSTIA Otonom Navigasyon (Sistem 1, Katman 2) — 400Hz Hata Durumu Kalman Filtresi (ESKF).

Elektronik Harp ve GPS Engelleme (GPS-Denial) Ortamlarında:
  * 400Hz IMU (İvmeölçer + Jiroskop) yüksek frekanslı durum tahmini
  * 20Hz Tekerlek Odometrisi (Wheel Odometry) hız düzeltmesi
  * 10Hz LiDAR ICP Poz Güncellemesi (Position & Yaw correction)
  * Santimetre hassasiyetinde yönelim ve konum hata kovaryans kovaryansı
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class ImuMeasurement:
    """Yüksek frekanslı IMU ölçümü (Gövde ekseni)."""
    timestamp_s: float
    accel_x: float  # m/s^2 (İleri ivme)
    accel_y: float  # m/s^2 (Yanal ivme)
    accel_z: float  # m/s^2 (Dikey ivme)
    gyro_z: float   # rad/s (Dönüş hızı / Yaw rate)


@dataclass
class OdometryMeasurement:
    """Tekerlek odometrisi hız ölçümü."""
    timestamp_s: float
    speed_mps: float
    steer_angle_rad: float


@dataclass
class LidarPoseMeasurement:
    """LiDAR ICP tarama eşleme pozisyon ölçümü (Global ENU ekseni)."""
    timestamp_s: float
    east_m: float
    north_m: float
    yaw_rad: float
    confidence: float = 0.95


@dataclass
class EskfState:
    """ESKF Nominal Durum Vektörü."""
    timestamp_s: float = 0.0
    east_m: float = 0.0
    north_m: float = 0.0
    velocity_mps: float = 0.0
    yaw_rad: float = 0.0
    accel_bias: float = 0.0
    gyro_bias: float = 0.0


class ErrorStateKalmanFilter:
    """400Hz Çoklu Sensör Hata Durumu Kalman Filtresi (ESKF)."""

    def __init__(
        self,
        initial_east: float = 0.0,
        initial_north: float = 0.0,
        initial_yaw: float = 0.0,
        accel_noise: float = 0.05,
        gyro_noise: float = 0.01,
    ) -> None:
        self.state = EskfState(
            east_m=initial_east,
            north_m=initial_north,
            yaw_rad=initial_yaw,
        )
        self.accel_noise = accel_noise
        self.gyro_noise = gyro_noise

        # Hata durumu kovaryans matrisi diyagonalleri: [d_east, d_north, d_vel, d_yaw, d_abias, d_gbias]
        self.P = [0.1, 0.1, 0.05, 0.02, 0.01, 0.005]
        self.last_predict_time: Optional[float] = None

    def predict_imu(self, imu: ImuMeasurement) -> EskfState:
        """IMU ölçümüyle nominal durumu ileriye taşır ve kovaryansı günceller."""
        if self.last_predict_time is None:
            self.last_predict_time = imu.timestamp_s
            self.state.timestamp_s = imu.timestamp_s
            return self.state

        dt = max(0.001, min(0.1, imu.timestamp_s - self.last_predict_time))
        self.last_predict_time = imu.timestamp_s
        self.state.timestamp_s = imu.timestamp_s

        # Düzeltilmiş sensör değerleri
        corr_accel = imu.accel_x - self.state.accel_bias
        corr_gyro = imu.gyro_z - self.state.gyro_bias

        # Nominal Durum Entegrasyonu
        self.state.yaw_rad = (self.state.yaw_rad + corr_gyro * dt + math.pi) % (2.0 * math.pi) - math.pi
        self.state.velocity_mps = max(0.0, self.state.velocity_mps + corr_accel * dt)

        # Konum güncellemesi (ENU)
        self.state.east_m += self.state.velocity_mps * math.cos(self.state.yaw_rad) * dt
        self.state.north_m += self.state.velocity_mps * math.sin(self.state.yaw_rad) * dt

        # Süreç Gürültüsü Yayılımı (Process Noise)
        self.P[0] += dt * (self.P[2] + self.accel_noise * dt)
        self.P[1] += dt * (self.P[2] + self.accel_noise * dt)
        self.P[2] += self.accel_noise * dt
        self.P[3] += self.gyro_noise * dt
        self.P[4] += 0.0001 * dt
        self.P[5] += 0.00005 * dt

        return self.state

    def update_odometry(self, odom: OdometryMeasurement, noise: float = 0.05) -> EskfState:
        """Tekerlek odometrisi hız güncellemesi (İnovasyon düzeltmesi)."""
        # Hata İnovasyonu
        innov_vel = odom.speed_mps - self.state.velocity_mps
        s_vel = self.P[2] + noise
        k_vel = self.P[2] / s_vel

        # Durum Düzeltmesi
        self.state.velocity_mps += k_vel * innov_vel
        self.P[2] = (1.0 - k_vel) * self.P[2]

        return self.state

    def update_lidar_pose(self, lidar: LidarPoseMeasurement, pos_noise: float = 0.08, yaw_noise: float = 0.03) -> EskfState:
        """LiDAR ICP pozisyon ve yönelim güncellemesi."""
        # Konum İnovasyonları
        innov_east = lidar.east_m - self.state.east_m
        innov_north = lidar.north_m - self.state.north_m

        # Kalman Kazançları
        k_east = self.P[0] / (self.P[0] + pos_noise)
        k_north = self.P[1] / (self.P[1] + pos_noise)

        # Durum Düzeltmeleri
        self.state.east_m += k_east * innov_east
        self.state.north_m += k_north * innov_north
        self.P[0] = (1.0 - k_east) * self.P[0]
        self.P[1] = (1.0 - k_north) * self.P[1]

        # Açısal İnovasyon (Normalleştirilmiş)
        raw_diff = lidar.yaw_rad - self.state.yaw_rad
        innov_yaw = (raw_diff + math.pi) % (2.0 * math.pi) - math.pi
        k_yaw = self.P[3] / (self.P[3] + yaw_noise)

        self.state.yaw_rad = (self.state.yaw_rad + k_yaw * innov_yaw + math.pi) % (2.0 * math.pi) - math.pi
        self.P[3] = (1.0 - k_yaw) * self.P[3]

        return self.state

    def get_estimated_pose(self) -> Tuple[float, float, float, float]:
        """Tahmini (East, North, Speed, Yaw) döndürür."""
        return (self.state.east_m, self.state.north_m, self.state.velocity_mps, self.state.yaw_rad)
