"""
TRUSTIA Otonomi Platformu — Stanley & Boyuna Hız Denetleyicisi (SDK v2.4).
SAIC Maxus MIFA 7 Yol Takip ve Direksiyon Kontrolörü.

Standart: ISO 15622 (Adaptive Cruise Control) & ISO 26262 ASIL-D Yolcu Konfor Sınırları.
"""

from __future__ import annotations

import math
from typing import List, Tuple, Optional
from trustia_sdk.core.transforms import Pose2D, KinematicState, normalize_angle


class StanleyController:
    """
    Ön Aks Tabanlı Stanley Yol Takip Kontrolörü.
    Yanal sapma (Cross-Track Error) ve rota yönelim hatasını minimize eder.
    """

    def __init__(
        self,
        wheel_base_m: float = 2.975,
        gain_k: float = 1.2,
        softening_k_soft: float = 1.0,
        max_steer_deg: float = 35.0
    ) -> None:
        self.L = wheel_base_m
        self.k = gain_k
        self.k_soft = softening_k_soft
        self.max_steer_rad = math.radians(max_steer_deg)

        # Boyuna PID Hız Kontrolü Değişkenleri
        self.kp_v = 0.8
        self.ki_v = 0.05
        self.kd_v = 0.02
        self.integral_v_error = 0.0
        self.prev_v_error = 0.0

    def compute_steering(self, state: KinematicState, path: List[Pose2D]) -> Tuple[float, float, int]:
        """
        Hedef rotaya göre gereken ön tekerlek direksiyon açısını (radyan) hesaplar.
        Dönüş: (Direksiyon Açısı rad, Yanal Hata metre, En Yakın Yol İndeksi)
        """
        if not path:
            return 0.0, 0.0, 0

        # Ön aks konumunu hesapla: x_front = x + L * cos(yaw), y_front = y + L * sin(yaw)
        fx = state.x + self.L * math.cos(state.yaw_rad)
        fy = state.y + self.L * math.sin(state.yaw_rad)

        # Ön aksa en yakın yol noktasını bul
        min_dist = float("inf")
        nearest_idx = 0
        for i, pt in enumerate(path):
            d = math.hypot(fx - pt.x, fy - pt.y)
            if d < min_dist:
                min_dist = d
                nearest_idx = i

        target_pt = path[nearest_idx]

        # Yol yönelimi (Heading of the path segment)
        if nearest_idx < len(path) - 1:
            next_pt = path[nearest_idx + 1]
            path_yaw = math.atan2(next_pt.y - target_pt.y, next_pt.x - target_pt.x)
        else:
            path_yaw = target_pt.yaw

        # 1. Yönelim Hatası (Heading Error): theta_e = yaw_path - yaw_vehicle
        theta_e = normalize_angle(path_yaw - state.yaw_rad)

        # 2. Yanal Sapma Hatası (Cross-Track Error e_fa)
        # Araç yolun solundaysa sağa kırmalı (negatif açı), sağındaysa sola kırmalı (pozitif açı)
        dx = fx - target_pt.x
        dy = fy - target_pt.y
        cross_track_error = math.sin(path_yaw) * dx - math.cos(path_yaw) * dy

        # 3. Stanley Kontrol Formülü: delta = theta_e + atan2(k * e_fa, v + k_soft)
        v = max(0.5, state.velocity_mps)
        crosstrack_steering = math.atan2(self.k * cross_track_error, v + self.k_soft)
        steer_cmd = theta_e + crosstrack_steering

        # Mekanik sınırlarla kısıtla (+/- 35 derece)
        clamped_steer = max(-self.max_steer_rad, min(self.max_steer_rad, steer_cmd))

        return clamped_steer, cross_track_error, nearest_idx

    def compute_longitudinal_accel(
        self,
        current_speed_mps: float,
        target_speed_mps: float,
        dt_s: float = 0.02
    ) -> float:
        """
        Boyuna hız kontrolü için hedef ivmeyi (m/s2) hesaplar (PID).
        """
        error = target_speed_mps - current_speed_mps
        self.integral_v_error += error * dt_s
        self.integral_v_error = max(-2.0, min(2.0, self.integral_v_error)) # Anti-windup
        derivative = (error - self.prev_v_error) / max(0.001, dt_s)
        self.prev_v_error = error

        raw_accel = (self.kp_v * error) + (self.ki_v * self.integral_v_error) + (self.kd_v * derivative)

        # ISO 15622 konfor sınırları: [-3.5 m/s2 (fren), +2.0 m/s2 (gaz)]
        return max(-3.5, min(2.0, raw_accel))
