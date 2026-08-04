"""
TRUSTIA Simülasyon Dünyası — Sanal sensörler ve araç modeli.

Sanal sensörler (PLAN 3.4):
  * Döner LiDAR: araziden ışın izleme (mesafe + gürültü + hava etkisi)
  * Teker kodlayıcı (odometri): gürültülü hareket ölçümü

Araç: diferansiyel kinematik model — (hız, açısal hız) komutlarından
gerçek pozisyon güncellemesi.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from simulation.terrain import Terrain, Weather


@dataclass
class ScanPoint:
    """LiDAR ölçümü — algı katmanının LaserPoint'iyle uyumlu."""

    range_m: float
    angle_rad: float
    intensity: float = 0.0
    elevation_rad: float = 0.0


class LidarModel:
    """Döner 2D LiDAR — ışın izleme + gürültü + hava etkisi."""

    def __init__(
        self,
        beam_count: int = 36,
        max_range_m: float = 20.0,
        noise_sigma_m: float = 0.02,
    ) -> None:
        if beam_count <= 0 or max_range_m <= 0.0:
            raise ValueError("geçersiz LiDAR parametreleri")
        self._beam_count = beam_count
        self._max_range = max_range_m
        self._noise_sigma = noise_sigma_m

    @property
    def beam_count(self) -> int:
        return self._beam_count

    def scan(
        self,
        terrain: Terrain,
        origin: Tuple[float, float],
        heading_rad: float,
        weather: Weather,
        rng: random.Random,
    ) -> List[ScanPoint]:
        """Araç konumundan 360° tarama üretir."""
        max_range = self._max_range * weather.lidar_range_factor()
        sigma = weather.lidar_noise_sigma_m(self._noise_sigma)
        points: List[ScanPoint] = []
        for i in range(self._beam_count):
            angle = heading_rad + 2.0 * math.pi * i / self._beam_count
            distance = terrain.raycast(origin, angle, max_range)
            if distance >= max_range - 1e-9:
                # Menzil dışı = ölçüm yok (algı katmanı bunu eler)
                points.append(ScanPoint(range_m=math.inf, angle_rad=angle))
                continue
            measured = distance + rng.gauss(0.0, sigma)
            points.append(ScanPoint(
                range_m=max(0.0, measured),
                angle_rad=angle,
            ))
        return points


class OdometryModel:
    """Teker kodlayıcı modeli — gerçek hareketi gürültülü ölçer.

    Gürültü: sistematik sapma (periyodik) + beyaz gauss. Yağmur
    zemin kaymasını artırır.
    """

    def __init__(
        self,
        distance_noise_ratio: float = 0.01,
        heading_noise_std_deg: float = 0.5,
    ) -> None:
        if distance_noise_ratio < 0.0 or heading_noise_std_deg < 0.0:
            raise ValueError("geçersiz odometri gürültüsü")
        self._distance_noise = distance_noise_ratio
        self._heading_noise = math.radians(heading_noise_std_deg)

    def measure(
        self,
        true_delta_m: float,
        true_delta_heading_rad: float,
        weather: Weather,
        rng: random.Random,
    ) -> Tuple[float, float]:
        """Gerçek hareketten gürültülü (mesafe, baş değişimi) döndürür."""
        factor = weather.odometry_noise_factor()
        dist_noise = (true_delta_m * self._distance_noise * factor
                      + rng.gauss(0.0, self._distance_noise * factor))
        heading_noise = self._heading_noise * factor
        return (
            max(0.0, true_delta_m + dist_noise),
            true_delta_heading_rad + rng.gauss(0.0, heading_noise),
        )


class SimulatedVehicle:
    """Diferansiyel kinematik araç — fizik sadeleştirilmiş model.

    Komut (v, w) → konum güncellemesi:
        x' = x + v·dt·cos(θ), y' = y + v·dt·sin(θ), θ' = θ + w·dt
    """

    def __init__(
        self,
        x_m: float = 0.0,
        y_m: float = 0.0,
        heading_rad: float = 0.0,
        max_speed_mps: float = 2.0,
        max_turn_radps: float = 1.5,
    ) -> None:
        if max_speed_mps <= 0.0 or max_turn_radps <= 0.0:
            raise ValueError("geçersiz araç sınırları")
        self._x = x_m
        self._y = y_m
        self._heading = heading_rad
        self._max_speed = max_speed_mps
        self._max_turn = max_turn_radps

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def heading(self) -> float:
        return self._heading

    @property
    def position(self) -> Tuple[float, float]:
        return self._x, self._y

    def step(self, forward_mps: float, angular_radps: float, dt: float) -> None:
        """Tek hareket adımı — komut sınırlanır."""
        if dt <= 0.0:
            raise ValueError(f"zaman adımı pozitif olmalı: {dt}")
        v = max(-self._max_speed, min(self._max_speed, forward_mps))
        w = max(-self._max_turn, min(self._max_turn, angular_radps))
        self._x += v * math.cos(self._heading) * dt
        self._y += v * math.sin(self._heading) * dt
        self._heading += w * dt
        self._heading = math.atan2(math.sin(self._heading),
                                   math.cos(self._heading))

    def distance_to(self, x: float, y: float) -> float:
        return math.hypot(x - self._x, y - self._y)
