"""Sistem 7 — Determinizm testleri (aynı girdi → aynı çıktı)."""

from __future__ import annotations

import pytest

from ai.mlp import MiniMlp
from ai.training import make_terrain_dataset, train_classifier
from simulation.runner import MissionRunner
from simulation.scenario import ScenarioGenerator
from simulation.terrain import Terrain


@pytest.mark.parametrize("seed", [1, 7, 13])
def test_terrain_generation_deterministic(seed):
    a = ScenarioGenerator(world_size_m=20.0).generate("kesif", seed=seed)
    b = ScenarioGenerator(world_size_m=20.0).generate("kesif", seed=seed)
    assert a.start == b.start
    assert a.waypoints == b.waypoints
    assert a.terrain.seed == b.terrain.seed


@pytest.mark.parametrize("seed", range(4))
def test_runner_deterministic_metrics(seed):
    mission = ScenarioGenerator(world_size_m=20.0).generate("lojistik", seed=seed)
    spec = mission.terrain
    terrain = Terrain(
        width_m=spec.width_m,
        height_m=spec.height_m,
        seed=spec.seed,
        obstacle_count=spec.obstacle_count,
        forbidden_count=spec.forbidden_count,
    )
    runner = MissionRunner(dt_s=0.05, beam_count=24, lidar_max_range_m=8.0)
    first = runner.run(terrain, mission.weather, mission)
    second = runner.run(terrain, mission.weather, mission)
    assert first == second


@pytest.mark.parametrize("seed", range(3))
def test_mlp_training_deterministic(seed):
    samples = make_terrain_dataset(per_class=8, seed=seed)
    a = train_classifier(samples, seed=seed)
    b = train_classifier(samples, seed=seed)
    assert a.final_loss == b.final_loss
    assert a.train_accuracy == b.train_accuracy


@pytest.mark.parametrize("seed", range(3))
def test_init_weight_deterministic_json(seed):
    assert MiniMlp([2, 4, 2], seed=seed).to_json() == MiniMlp(
        [2, 4, 2], seed=seed
    ).to_json()


def test_gaussian_dataset_deterministic():
    a = make_terrain_dataset(per_class=5, seed=9)
    b = make_terrain_dataset(per_class=5, seed=9)
    assert a == b