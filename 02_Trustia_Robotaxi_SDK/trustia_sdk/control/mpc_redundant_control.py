"""
TRUSTIA Model Öngörülü Kontrol (MPC) ve Çift Yedekli (Fail-Operational) Aktüatör Dağıtıcısı
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class MpcControlSolution:
    optimal_steer_rad: float
    optimal_steer_deg: float
    optimal_accel_mps2: float
    predicted_terminal_cte_m: float
    horizon_cost: float


@dataclass(frozen=True)
class RedundantActuatorAllocation:
    primary_ibooster_decel_mps2: float
    secondary_esc_pump_decel_mps2: float
    epb_emergency_clamp_active: bool
    eps_primary_torque_ratio: float
    eps_secondary_torque_ratio: float
    fail_operational_mode: str


class RecedingHorizonMPC:
    """Seviye-4 Robotaksi Kinematik Bisiklet Modeli Öngörülü Kontrolcüsü (MPC)."""

    def __init__(self, wheelbase_m: float = 2.975, horizon_steps: int = 8, dt_s: float = 0.05) -> None:
        self.wheelbase_m = wheelbase_m
        self.horizon_steps = horizon_steps
        self.dt_s = dt_s
        self.max_steer_rad = math.radians(35.0)

    def solve(
        self,
        cross_track_error_m: float,
        heading_error_rad: float,
        velocity_mps: float,
        target_velocity_mps: float,
        prev_steer_rad: float = 0.0,
    ) -> MpcControlSolution:
        v = max(0.5, velocity_mps)
        best_steer, best_cost, best_cte = 0.0, float("inf"), cross_track_error_m
        for idx in range(25):
            cand = ((idx / 24.0) * 2.0 - 1.0) * self.max_steer_rad
            ey, epsi = cross_track_error_m, heading_error_rad
            cost = 6.0 * ((cand - prev_steer_rad) ** 2)
            for step in range(self.horizon_steps):
                u = cand * (0.85 ** step)
                ey += v * math.sin(epsi) * self.dt_s
                epsi += (v / self.wheelbase_m) * math.tan(u) * self.dt_s
                cost += 12.0 * (ey ** 2) + 8.0 * (epsi ** 2) + 2.5 * (u ** 2)
            if cost < best_cost:
                best_cost, best_steer, best_cte = cost, cand, ey
        accel = max(-5.0, min(2.5, 1.2 * (target_velocity_mps - velocity_mps)))
        return MpcControlSolution(
            optimal_steer_rad=round(best_steer, 5),
            optimal_steer_deg=round(math.degrees(best_steer), 3),
            optimal_accel_mps2=round(accel, 3),
            predicted_terminal_cte_m=round(best_cte, 4),
            horizon_cost=round(best_cost, 4),
        )


class RedundantActuatorAllocator:
    """ISO 26262 ASIL-D Fail-Operational çift yedekli fren/direksiyon dağıtıcısı."""

    def allocate(
        self,
        requested_decel_mps2: float,
        ibooster_primary_healthy: bool = True,
        esc_secondary_healthy: bool = True,
        eps_primary_healthy: bool = True,
    ) -> RedundantActuatorAllocation:
        decel = max(0.0, abs(requested_decel_mps2))
        eps_p = 1.0 if eps_primary_healthy else 0.0
        eps_s = 0.0 if eps_primary_healthy else 1.0
        if ibooster_primary_healthy:
            return RedundantActuatorAllocation(decel, 0.0, False, eps_p, eps_s, "NOMINAL_DUAL" if eps_primary_healthy else "DEGRADED_SECONDARY_ACTIVE")
        if esc_secondary_healthy:
            return RedundantActuatorAllocation(0.0, decel, False, eps_p, eps_s, "DEGRADED_SECONDARY_ACTIVE")
        return RedundantActuatorAllocation(0.0, 0.0, True, eps_p, eps_s, "EMERGENCY_EPB_CLAMP")
