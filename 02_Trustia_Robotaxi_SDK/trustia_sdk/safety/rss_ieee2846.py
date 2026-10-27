"""
TRUSTIA IEEE 2846 & Mobileye RSS (Responsibility-Sensitive Safety) Matematiksel Güvenlik Kalkanı
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RssParameters:
    response_time_s: float = 0.20
    lon_max_accel_mps2: float = 2.5
    lon_min_brake_mps2: float = 3.5
    lon_max_brake_mps2: float = 6.5
    lat_max_accel_mps2: float = 1.2
    lat_min_brake_mps2: float = 1.8
    lateral_fluctuation_margin_m: float = 0.30


@dataclass(frozen=True)
class RssSafetyVerdict:
    longitudinal_safe: bool
    lateral_safe: bool
    min_safe_longitudinal_m: float
    min_safe_lateral_m: float
    actual_longitudinal_m: float
    actual_lateral_m: float
    proper_response: str
    required_decel_mps2: float


class ResponsibilitySensitiveSafety:
    """IEEE 2846 ve Mobileye RSS formüllerini işleten matematiksel güvenlik denetleyicisi."""

    def __init__(self, params: RssParameters | None = None) -> None:
        self.params = params or RssParameters()

    def compute_min_longitudinal_distance(self, ego_vel_mps: float, front_vel_mps: float) -> float:
        p = self.params
        v_r = max(0.0, ego_vel_mps)
        v_f = max(0.0, front_vel_mps)
        rho = p.response_time_s
        v_r_rho = v_r + rho * p.lon_max_accel_mps2
        d_min = (
            v_r * rho
            + 0.5 * p.lon_max_accel_mps2 * (rho ** 2)
            + (v_r_rho ** 2) / (2.0 * p.lon_min_brake_mps2)
            - (v_f ** 2) / (2.0 * p.lon_max_brake_mps2)
        )
        return max(0.0, d_min)

    def compute_min_lateral_distance(self, ego_lat_vel_mps: float, other_lat_vel_mps: float) -> float:
        p = self.params
        rho = p.response_time_s
        v1, v2 = abs(ego_lat_vel_mps), abs(other_lat_vel_mps)
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
        d_min_lon = self.compute_min_longitudinal_distance(ego_vel_mps, front_vel_mps)
        d_min_lat = self.compute_min_lateral_distance(ego_lat_vel_mps, other_lat_vel_mps)
        lon_safe = actual_longitudinal_gap_m >= d_min_lon
        lat_safe = actual_lateral_gap_m >= d_min_lat
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
