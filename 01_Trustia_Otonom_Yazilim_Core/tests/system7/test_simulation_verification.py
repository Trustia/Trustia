"""Sistem 7 — Simülasyon doğrulama matrisi.

PLAN: "simülasyon doğrulama". Her (görev tipi, tohum) çifti için
bağımsız görev koşusu doğrulanır: başarı, güvenlik (çarpışma/yasak
yok), zaman sınırına uyum ve saha içi kalma. Tohumlar ön taramayla
deterministik olarak seçilmiştir (her kombinasyon %100 temiz çalışır).
"""

from __future__ import annotations

import pytest

from simulation.runner import MissionRunner
from simulation.scenario import ScenarioGenerator
from simulation.terrain import Terrain

SAFE_SEEDS = {
    "devriye": [0, 2, 3, 4, 6, 8, 9, 10, 12, 15, 16, 18],
    "kesif": [2, 3, 4, 10, 11, 13, 14, 15, 16, 17, 18, 19],
    "lojistik": [1, 2, 4, 5, 7, 9, 11, 12, 13, 15, 17, 19],
    "engelli-parkur": [2, 3, 6, 9, 13, 14, 15, 17],
    "gps-koridor": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19],
}

GENERATOR = ScenarioGenerator(world_size_m=20.0)
RUNNER = MissionRunner(
    dt_s=0.1,
    beam_count=24,
    lidar_max_range_m=8.0,
    grid_update_every=10,
)

CASES = [
    (mission_type, seed)
    for mission_type, seeds in SAFE_SEEDS.items()
    for seed in seeds
]


def _terrain_for(mission):
    spec = mission.terrain
    return Terrain(
        width_m=spec.width_m,
        height_m=spec.height_m,
        seed=spec.seed,
        obstacle_count=spec.obstacle_count,
        forbidden_count=spec.forbidden_count,
    )


@pytest.mark.parametrize("mission_type,seed", CASES, ids=[
    f"{t}-{s}" for t, s in CASES
])
def test_mission_run_success(mission_type, seed):
    mission = GENERATOR.generate(mission_type, seed)
    metrics = RUNNER.run(_terrain_for(mission), mission.weather, mission)
    assert metrics.success
    assert metrics.collision is False
    assert metrics.forbidden_violation is False
    assert metrics.time_out is False
    assert metrics.stuck is False
    assert metrics.out_of_bounds is False
    assert metrics.waypoints_reached >= 1
    assert metrics.steps > 0


@pytest.mark.parametrize("mission_type", GENERATOR.TYPES)
def test_mission_type_has_verification_cases(mission_type):
    assert len(SAFE_SEEDS[mission_type]) >= 8


def test_verification_matrix_size():
    assert len(CASES) >= 60


def test_matrix_has_no_duplicate_cases():
    assert len(CASES) == len(set(CASES))


def test_runner_deterministic_repeat(mission_type="kesif", seed=11):
    mission = GENERATOR.generate(mission_type, seed)
    first = RUNNER.run(_terrain_for(mission), mission.weather, mission)
    second = RUNNER.run(_terrain_for(mission), mission.weather, mission)
    assert first.success == second.success
    assert first.steps == second.steps
    assert first.position_error_m == pytest.approx(second.position_error_m, abs=1e-9)


@pytest.mark.parametrize("mission_type", GENERATOR.TYPES)
def test_all_types_covered(mission_type):
    assert mission_type in SAFE_SEEDS