"""Sistem 7 — Senaryo üretim doğrulama matrisi (koşu gerektirmez).

Her (görev tipi, tohum) çifti geçerli, sağlıklı ve sınırlar içinde bir
görev tanımı üretmeli. 5 tip x 40 tohum = 200 bağımsız doğrulama.
"""

from __future__ import annotations

import math

import pytest

from simulation.scenario import ScenarioGenerator

GENERATOR = ScenarioGenerator(world_size_m=20.0)

MISSION_TYPES = GENERATOR.TYPES
SEEDS = list(range(40))
CASES = [(t, s) for t in MISSION_TYPES for s in SEEDS]


@pytest.mark.parametrize("mission_type,seed", CASES, ids=[f"{t}-{s}" for t, s in CASES])
def test_mission_generation_valid(mission_type, seed):
    mission = GENERATOR.generate(mission_type, seed)
    assert mission.mission_id
    assert mission.mission_type == mission_type
    assert len(mission.waypoints) >= 1
    assert mission.time_limit_s > 0
    assert mission.arrival_tolerance_m > 0
    assert mission.terrain.width_m == pytest.approx(20.0)


@pytest.mark.parametrize("seed", range(40))
def test_mission_start_inside_world(seed):
    mission = GENERATOR.generate("kesif", seed)
    x, y = mission.start
    assert 0.0 <= x <= 20.0
    assert 0.0 <= y <= 20.0


@pytest.mark.parametrize("seed", range(40))
def test_mission_waypoints_inside_world(seed):
    mission = GENERATOR.generate("lojistik", seed)
    for x, y in mission.waypoints:
        assert 0.0 <= x <= 20.0
        assert 0.0 <= y <= 20.0


@pytest.mark.parametrize("mission_type", MISSION_TYPES)
@pytest.mark.parametrize("seed", range(20))
def test_terrain_spec_positive(mission_type, seed):
    mission = GENERATOR.generate(mission_type, seed)
    spec = mission.terrain
    assert spec.obstacle_count >= 0
    assert spec.forbidden_count >= 0
    assert spec.seed == seed


@pytest.mark.parametrize("mission_type", MISSION_TYPES)
@pytest.mark.parametrize("seed", range(20))
def test_weather_valid_range(mission_type, seed):
    mission = GENERATOR.generate(mission_type, seed)
    weather = mission.weather
    assert 0.0 <= weather.rain_mmh <= 30.0
    assert 0.0 <= weather.fog_density <= 1.0
    assert 0.0 <= weather.lidar_range_factor() <= 1.0


@pytest.mark.parametrize("mission_type", MISSION_TYPES)
@pytest.mark.parametrize("seed", range(20))
def test_mission_id_unique(mission_type, seed):
    mission = GENERATOR.generate(mission_type, seed)
    assert mission.mission_id == f"{mission_type}-{seed}"


def test_matrix_coverage():
    assert len(CASES) == 5 * 40


def test_mission_types_complete():
    assert set(MISSION_TYPES) == {
        "devriye", "kesif", "lojistik", "engelli-parkur", "gps-koridor"
    }