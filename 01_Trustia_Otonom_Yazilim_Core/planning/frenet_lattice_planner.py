"""
TRUSTIA Frenet (s, d) Koordinat Çerçevesi ve Jerk-Optimal Kafes (Lattice) Yörünge Planlayıcı
============================================================================================
Autoware Universe ve Baidu Apollo Seviye-4 Robotaksi mimarilerinde kullanılan standart
yerel yörünge planlama yöntemidir:
  1. Kartezyen (x, y) koordinatlarını şerit merkez çizgisine göre boylamsal ilerleme (s)
     ve şerit merkezinden yanal sapma (d) koordinatlarına dönüştürür.
  2. Farklı yanal hedef kaymaları (ör. d in [-3.5m, -1.75m, 0.0m, +1.75m, +3.5m]) için
     5. dereceden (Quintic) sarsıntısız (Jerk-Optimal) aday yörüngeler üretir.
  3. Çarpışma kontrolü, yanal sarsıntı (Jerk) ve şerit merkezine yakınlık maliyet fonksiyonuna
     göre en konforlu ve güvenli yörüngeyi seçer.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class FrenetState:
    """Frenet (s, d) koordinat çerçevesinde araç durumu."""

    s: float       # Boylamsal konum (m)
    ds: float      # Boylamsal hız (m/s)
    dds: float     # Boylamsal ivme (m/s²)
    d: float       # Yanal sapma (m)
    dd: float      # Yanal hız (m/s)
    ddd: float     # Yanal ivme (m/s²)


@dataclass(frozen=True)
class FrenetCandidateTrajectory:
    """Aday bir Frenet kafes yörüngesi ve maliyet skoru."""

    target_lateral_d_m: float
    horizon_s: float
    points_sd: List[Tuple[float, float]]
    max_lateral_jerk_mps3: float
    collision_free: bool
    total_cost: float


class FrenetLatticePlanner:
    """
    Şerit içi engellerden sarsıntısız kaçınma ve konforlu şerit değiştirme için
    Frenet (s, d) kafes yörünge planlayıcısı.
    """

    def __init__(
        self,
        lane_width_m: float = 3.5,
        safety_radius_m: float = 1.6,
        weight_jerk: float = 2.0,
        weight_lateral_offset: float = 4.0,
    ) -> None:
        self.lane_width_m = lane_width_m
        self.safety_radius_m = safety_radius_m
        self.weight_jerk = weight_jerk
        self.weight_lateral_offset = weight_lateral_offset

    @staticmethod
    def cartesian_to_frenet(
        x: float,
        y: float,
        ref_x: float,
        ref_y: float,
        ref_yaw_rad: float,
        ref_s: float,
    ) -> Tuple[float, float]:
        """Kartezyen (x, y) noktasını referans şerit noktasına göre (s, d) koordinatına çevirir."""
        dx = x - ref_x
        dy = y - ref_y
        cos_y = math.cos(ref_yaw_rad)
        sin_y = math.sin(ref_yaw_rad)
        s = ref_s + (dx * cos_y + dy * sin_y)
        d = -dx * sin_y + dy * cos_y
        return (s, d)

    @staticmethod
    def frenet_to_cartesian(
        s: float,
        d: float,
        ref_x: float,
        ref_y: float,
        ref_yaw_rad: float,
        ref_s: float,
    ) -> Tuple[float, float]:
        """Frenet (s, d) koordinatını Kartezyen (x, y) koordinatına geri dönüştürür."""
        ds = s - ref_s
        cos_y = math.cos(ref_yaw_rad)
        sin_y = math.sin(ref_yaw_rad)
        x = ref_x + ds * cos_y - d * sin_y
        y = ref_y + ds * sin_y + d * cos_y
        return (x, y)

    def plan_optimal_trajectory(
        self,
        initial: FrenetState,
        target_speed_mps: float,
        obstacles_sd: List[Tuple[float, float]],
        horizon_s: float = 3.0,
        candidate_offsets_m: List[float] | None = None,
    ) -> FrenetCandidateTrajectory:
        """
        Aday yanal kaymaları değerlendirerek engellere çarpmayan en düşük maliyetli
        Jerk-Optimal Frenet yörüngesini seçer.
        """
        if candidate_offsets_m is None:
            candidate_offsets_m = [-3.5, -1.75, -0.8, 0.0, 0.8, 1.75, 3.5]

        T = max(0.5, horizon_s)
        steps = 15
        dt = T / steps
        candidates: List[FrenetCandidateTrajectory] = []

        for d_target in candidate_offsets_m:
            # 5. dereceden (Quintic) sınır koşulları: d(0)=d0, d(T)=d_target, uç hız/ivmeler=0
            delta_d = d_target - initial.d
            a0 = initial.d
            a1 = initial.dd
            a2 = 0.5 * initial.ddd
            a3 = (20.0 * delta_d - (8.0 * 0.0 + 12.0 * a1) * T - (3.0 * 0.0 - 0.0) * (T ** 2)) / (2.0 * (T ** 3))
            a4 = (-30.0 * delta_d + (14.0 * 0.0 + 16.0 * a1) * T) / (2.0 * (T ** 4))
            a5 = (12.0 * delta_d - 6.0 * a1 * T) / (2.0 * (T ** 5))

            pts_sd: List[Tuple[float, float]] = []
            max_jerk = 0.0
            collision_free = True

            for i in range(steps + 1):
                t = i * dt
                s_t = initial.s + 0.5 * (initial.ds + target_speed_mps) * t
                d_t = a0 + a1 * t + a2 * (t ** 2) + a3 * (t ** 3) + a4 * (t ** 4) + a5 * (t ** 5)
                jerk_d = 6.0 * a3 + 24.0 * a4 * t + 60.0 * a5 * (t ** 2)
                max_jerk = max(max_jerk, abs(jerk_d))
                pts_sd.append((s_t, d_t))

                for obs_s, obs_d in obstacles_sd:
                    if math.hypot(s_t - obs_s, d_t - obs_d) < self.safety_radius_m:
                        collision_free = False
                        break

            cost = (
                self.weight_jerk * max_jerk
                + self.weight_lateral_offset * abs(d_target)
                + (0.0 if collision_free else 10000.0)
            )
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
