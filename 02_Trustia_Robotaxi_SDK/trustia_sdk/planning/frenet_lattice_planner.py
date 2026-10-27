"""
TRUSTIA Frenet (s, d) Koordinat Çerçevesi ve Jerk-Optimal Kafes (Lattice) Yörünge Planlayıcı
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class FrenetState:
    s: float
    ds: float
    dds: float
    d: float
    dd: float
    ddd: float


@dataclass(frozen=True)
class FrenetCandidateTrajectory:
    target_lateral_d_m: float
    horizon_s: float
    points_sd: List[Tuple[float, float]]
    max_lateral_jerk_mps3: float
    collision_free: bool
    total_cost: float


class FrenetLatticePlanner:
    """Frenet (s, d) koordinat çerçevesinde sarsıntısız (Jerk-Optimal) kafes yörünge planlayıcısı."""

    def __init__(self, safety_radius_m: float = 1.6) -> None:
        self.safety_radius_m = safety_radius_m

    def plan_optimal_trajectory(
        self,
        initial: FrenetState,
        target_speed_mps: float,
        obstacles_sd: List[Tuple[float, float]],
        horizon_s: float = 3.0,
        candidate_offsets_m: List[float] | None = None,
    ) -> FrenetCandidateTrajectory:
        if candidate_offsets_m is None:
            candidate_offsets_m = [-3.5, -1.75, 0.0, 1.75, 3.5]
        T = max(0.5, horizon_s)
        steps = 15
        dt = T / steps
        candidates: List[FrenetCandidateTrajectory] = []
        for d_target in candidate_offsets_m:
            delta_d = d_target - initial.d
            a0, a1 = initial.d, initial.dd
            a3 = (20.0 * delta_d - 12.0 * a1 * T) / (2.0 * (T ** 3))
            a4 = (-30.0 * delta_d + 16.0 * a1 * T) / (2.0 * (T ** 4))
            a5 = (12.0 * delta_d - 6.0 * a1 * T) / (2.0 * (T ** 5))
            pts_sd: List[Tuple[float, float]] = []
            max_jerk = 0.0
            collision_free = True
            for i in range(steps + 1):
                t = i * dt
                s_t = initial.s + 0.5 * (initial.ds + target_speed_mps) * t
                d_t = a0 + a1 * t + a3 * (t ** 3) + a4 * (t ** 4) + a5 * (t ** 5)
                jerk_d = abs(6.0 * a3 + 24.0 * a4 * t + 60.0 * a5 * (t ** 2))
                max_jerk = max(max_jerk, jerk_d)
                pts_sd.append((s_t, d_t))
                for obs_s, obs_d in obstacles_sd:
                    if math.hypot(s_t - obs_s, d_t - obs_d) < self.safety_radius_m:
                        collision_free = False
                        break
            cost = 2.0 * max_jerk + 4.0 * abs(d_target) + (0.0 if collision_free else 10000.0)
            candidates.append(
                FrenetCandidateTrajectory(
                    target_lateral_d_m=d_target,
                    horizon_s=T,
                    points_sd=pts_sd,
                    max_lateral_jerk_mps3=round(max_jerk, 3),
                    collision_free=collision_free,
                    total_cost=round(cost, 3),
                )
            )
        candidates.sort(key=lambda c: c.total_cost)
        return candidates[0]
