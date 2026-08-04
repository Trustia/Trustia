"""
TRUSTIA Simülasyon Dünyası — Senaryo motoru.

Senaryo = arazi parametreleri + görev tanımı (hedef noktalar,
süre limiti, hedef yarıçapı, hava durumu, GPS modu).

Hazır senaryo tipleri (PLAN 3.4):
  * devriye      : birden çok hedef nokta sırayla
  * keşif        : uzun tek hedef, yasak bölgeler
  * lojistik     : uzun mesafe, yük yoğunluğu yüksek
  * engelli park : sık engel, dar geçitler
  * gps'siz koridor: GPS kapalı — odometri + algı ile hedefe
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from simulation.terrain import Terrain, TerrainSpec, Weather


@dataclass
class Mission:
    """Tek görev tanımı."""

    mission_id: str
    mission_type: str
    start: Tuple[float, float]
    start_heading_rad: float
    waypoints: List[Tuple[float, float]]
    arrival_tolerance_m: float = 1.5
    time_limit_s: float = 300.0
    gps_available: bool = True
    terrain: Optional[TerrainSpec] = None
    weather: Optional[Weather] = None


class ScenarioGenerator:
    """Seed'den deterministik görev üretir — aynı seed aynı görev."""

    TYPES = ("devriye", "kesif", "lojistik", "engelli-parkur", "gps-koridor")

    def __init__(
        self,
        world_size_m: float = 50.0,
        default_seed: int = 0,
    ) -> None:
        self._world_size = world_size_m
        self._seed = default_seed

    def generate(self, mission_type: str, seed: int) -> Mission:
        """Belirtilen tipte deterministik görev üretir."""
        if mission_type not in self.TYPES:
            raise ValueError(f"bilinmeyen görev tipi: {mission_type}")
        rng = random.Random(seed)
        size = self._world_size
        terrain_spec = self._terrain_spec(mission_type, seed, rng)
        terrain = Terrain(
            width_m=terrain_spec.width_m,
            height_m=terrain_spec.height_m,
            seed=terrain_spec.seed,
            obstacle_count=terrain_spec.obstacle_count,
            forbidden_count=terrain_spec.forbidden_count,
        )
        start = terrain.sample_clear_point(rng, clearance_m=2.5)
        waypoints = self._waypoints(mission_type, terrain, rng)
        weather = Weather(
            rain_mmh=rng.choice([0.0, 0.0, 5.0, 15.0]),
            fog_density=rng.choice([0.0, 0.0, 0.2, 0.5]),
            night=rng.random() < 0.25,
        )
        time_limit = {
            "devriye": 400.0,
            "kesif": 250.0,
            "lojistik": 500.0,
            "engelli-parkur": 260.0,
            "gps-koridor": 400.0,
        }[mission_type]
        return Mission(
            mission_id=f"{mission_type}-{seed}",
            mission_type=mission_type,
            start=start,
            start_heading_rad=rng.uniform(-3.14, 3.14),
            waypoints=waypoints,
            arrival_tolerance_m=1.5,
            time_limit_s=time_limit,
            gps_available=mission_type != "gps-koridor",
            terrain=terrain_spec,
            weather=weather,
        )

    def _terrain_spec(
        self, mission_type: str, seed: int, rng: random.Random
    ) -> TerrainSpec:
        size = self._world_size
        counts = {
            "devriye": (12, 3),
            "kesif": (18, 5),
            "lojistik": (15, 2),
            "engelli-parkur": (28, 0),
            "gps-koridor": (10, 0),
        }
        obstacles, forbidden = counts[mission_type]
        return TerrainSpec(
            width_m=size,
            height_m=size,
            seed=seed,
            obstacle_count=obstacles,
            forbidden_count=forbidden,
        )

    def _waypoints(
        self,
        mission_type: str,
        terrain: Terrain,
        rng: random.Random,
    ) -> List[Tuple[float, float]]:
        counts = {
            "devriye": 3,
            "kesif": 1,
            "lojistik": 1,
            "engelli-parkur": 1,
            "gps-koridor": 1,
        }
        count = counts[mission_type]
        points = []
        for _ in range(count):
            point = terrain.sample_clear_point(rng, clearance_m=2.0)
            points.append(point)
        return points
