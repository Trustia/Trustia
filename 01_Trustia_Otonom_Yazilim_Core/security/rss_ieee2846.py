"""
TRUSTIA IEEE 2846 & Mobileye RSS (Responsibility-Sensitive Safety) Matematiksel Güvenlik Kalkanı
================================================================================================
AB 2022/1426 (1 Aralık 2024 Resmî Gazete) Ek-II ve IEEE Std 2846-2022 uyarınca otonom aracın
hiçbir koşulda kusurlu bir çarpışmaya sebep olmamasını garanti altına alan matematiksel
emniyet zarfı (Safety Envelope) denetleyicisidir.

Temel RSS Denklemleri:
  1. Boylamsal Güvenli Takip Mesafesi (Aynı Yön):
     d_min_long = max(0, v_r * rho + 0.5 * a_max_accel * rho^2
                         + (v_r + rho * a_max_accel)^2 / (2 * a_min_brake)
                         - v_f^2 / (2 * a_max_brake))
  2. Yanal Güvenli Mesafe (Şerit İçi / Yan Şerit):
     d_min_lat = mu + 0.5 * (v_lat_1 + v_lat_1_rho) * rho + v_lat_1_rho^2 / (2 * a_lat_min_brake)
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class RssParameters:
    """IEEE 2846 / RSS matematiksel güvenlik parametreleri."""

    response_time_s: float = 0.20          # Sistem tepki süresi rho (sn)
    lon_max_accel_mps2: float = 2.5        # Maksimum boylamsal ivmelenme (m/s²)
    lon_min_brake_mps2: float = 3.5        # Otonom aracın garanti edilen minimum fren ivmesi (m/s²)
    lon_max_brake_mps2: float = 6.5        # Öndeki aracın yapabileceği maksimum panik fren (m/s²)
    lat_max_accel_mps2: float = 1.2        # Maksimum yanal ivmelenme (m/s²)
    lat_min_brake_mps2: float = 1.8        # Minimum yanal düzeltme ivmesi (m/s²)
    lateral_fluctuation_margin_m: float = 0.30  # Yanal dalgalanma payı mu (m)


@dataclass(frozen=True)
class RssSafetyVerdict:
    """RSS güvenlik zarfı değerlendirme kararı."""

    longitudinal_safe: bool
    lateral_safe: bool
    min_safe_longitudinal_m: float
    min_safe_lateral_m: float
    actual_longitudinal_m: float
    actual_lateral_m: float
    proper_response: str  # "NOMINAL_SAFE", "RSS_LONGITUDINAL_BRAKE", "RSS_LATERAL_EVASION", "RSS_BOTH_BRAKE_AND_STEER"
    required_decel_mps2: float


class ResponsibilitySensitiveSafety:
    """
    IEEE 2846 ve Mobileye RSS formüllerini işleten bağımsız matematiksel güvenlik denetleyicisi.
    Planlayıcıdan çıkan her yörüngeyi aktüatöre gitmeden önce denetler.
    """

    def __init__(self, params: RssParameters | None = None) -> None:
        self.params = params or RssParameters()

    def compute_min_longitudinal_distance(
        self,
        ego_vel_mps: float,
        front_vel_mps: float,
    ) -> float:
        """Aynı yönde giden öndeki araçla bırakılması gereken minimum boylamsal güvenli mesafe."""
        p = self.params
        v_r = max(0.0, ego_vel_mps)
        v_f = max(0.0, front_vel_mps)
        rho = p.response_time_s

        v_r_after_rho = v_r + rho * p.lon_max_accel_mps2
        term_reaction = v_r * rho + 0.5 * p.lon_max_accel_mps2 * (rho ** 2)
        term_ego_brake = (v_r_after_rho ** 2) / (2.0 * p.lon_min_brake_mps2)
        term_front_brake = (v_f ** 2) / (2.0 * p.lon_max_brake_mps2)

        d_min = term_reaction + term_ego_brake - term_front_brake
        return max(0.0, d_min)

    def compute_min_lateral_distance(
        self,
        ego_lat_vel_mps: float,
        other_lat_vel_mps: float,
    ) -> float:
        """Yan şeritteki araç veya yaya ile bırakılması gereken minimum yanal güvenli mesafe."""
        p = self.params
        rho = p.response_time_s
        v1 = abs(ego_lat_vel_mps)
        v2 = abs(other_lat_vel_mps)

        v1_rho = v1 + rho * p.lat_max_accel_mps2
        v2_rho = v2 + rho * p.lat_max_accel_mps2

        d_ego = 0.5 * (v1 + v1_rho) * rho + (v1_rho ** 2) / (2.0 * p.lat_min_brake_mps2)
        d_other = 0.5 * (v2 + v2_rho) * rho + (v2_rho ** 2) / (2.0 * p.lat_min_brake_mps2)
        return p.lateral_fluctuation_margin_m + d_ego + d_other

    def evaluate_pair(
        self,
        ego_vel_mps: float,
        front_vel_mps: float,
        actual_longitudinal_gap_m: float,
        actual_lateral_gap_m: float,
        ego_lat_vel_mps: float = 0.0,
        other_lat_vel_mps: float = 0.0,
    ) -> RssSafetyVerdict:
        """Ego araç ile trafikteki bir nesne arasındaki RSS güvenlik durumunu hesaplar."""
        d_min_lon = self.compute_min_longitudinal_distance(ego_vel_mps, front_vel_mps)
        d_min_lat = self.compute_min_lateral_distance(ego_lat_vel_mps, other_lat_vel_mps)

        lon_safe = actual_longitudinal_gap_m >= d_min_lon
        lat_safe = actual_lateral_gap_m >= d_min_lat

        # RSS kuralı: Bir tehlike ancak hem boylamsal hem yanal mesafe aynı anda ihlal edilirse oluşur
        if lon_safe or lat_safe:
            return RssSafetyVerdict(
                longitudinal_safe=lon_safe,
                lateral_safe=lat_safe,
                min_safe_longitudinal_m=round(d_min_lon, 3),
                min_safe_lateral_m=round(d_min_lat, 3),
                actual_longitudinal_m=actual_longitudinal_gap_m,
                actual_lateral_m=actual_lateral_gap_m,
                proper_response="NOMINAL_SAFE",
                required_decel_mps2=0.0,
            )

        return RssSafetyVerdict(
            longitudinal_safe=False,
            lateral_safe=False,
            min_safe_longitudinal_m=round(d_min_lon, 3),
            min_safe_lateral_m=round(d_min_lat, 3),
            actual_longitudinal_m=actual_longitudinal_gap_m,
            actual_lateral_m=actual_lateral_gap_m,
            proper_response="RSS_LONGITUDINAL_BRAKE",
            required_decel_mps2=-self.params.lon_min_brake_mps2,
        )
