"""Sistem 7 — Performans ölçümleri.

Zaman bütçesi eşikleri: gerçek zamanlı çalışma iddiası için her
modülün adım/çağrı maliyeti sınırlıdır (geliştirme ortamında ölçülür).
"""

from __future__ import annotations

import time

import pytest

from ai.features import cluster_shape, lidar_features, terrain_cell
from ai.mlp import MiniMlp
from integration.jaus import (
    JausEndpoint,
    JausMessage,
    MessageType,
    MobilityCode,
    ServiceId,
)
from simulation.runner import MissionRunner
from simulation.scenario import ScenarioGenerator
from simulation.sensors import LidarModel
from simulation.terrain import Terrain, Weather

WALL_S = 0.5  # tek çağrı bütçesi


def _timed(fn, repeat: int = 50):
    start = time.perf_counter()
    for _ in range(repeat):
        fn()
    return (time.perf_counter() - start) / repeat


def _jaus_message():
    return JausMessage(
        message_type=MessageType.COMMAND,
        service=ServiceId.MOBILITY,
        message_code=MobilityCode.SET_SPEED,
        source_uid=1,
        destination_uid=2,
        sequence=0,
        payload={"speed_mps": 1.5},
    )


def test_lidar_scan_time_budget():
    terrain = Terrain(width_m=20.0, height_m=20.0, seed=3, obstacle_count=8)
    lidar = LidarModel(beam_count=48, max_range_m=10.0)
    import random

    rng = random.Random(0)
    dt = _timed(lambda: lidar.scan(terrain, (10.0, 10.0), 0.0, Weather(), rng), 10)
    assert dt < WALL_S


def test_mlp_forward_time_budget():
    model = MiniMlp([4, 8, 8, 6])
    x = [0.2, 0.4, 0.6, 0.8]
    dt = _timed(lambda: model.predict(x), 100)
    assert dt < 0.05


def test_mlp_train_small_time_budget():
    model = MiniMlp([2, 8, 2])
    dt = _timed(lambda: model.train([[0, 0], [0, 1]], [0, 1], epochs=2), 3)
    assert dt < WALL_S


def test_feature_extraction_time_budget():
    scan = [5.0] * 48
    dt = _timed(lambda: lidar_features(scan), 200)
    assert dt < 0.01


def test_terrain_cell_features_time_budget():
    samples = [1.0 + i * 0.1 for i in range(16)]
    dt = _timed(lambda: terrain_cell(samples), 200)
    assert dt < 0.01


def test_cluster_shape_time_budget():
    points = [(i % 8, i // 8, 0.4) for i in range(64)]
    dt = _timed(lambda: cluster_shape(points), 100)
    assert dt < 0.01


def test_jaus_roundtrip_time_budget():
    endpoint = JausEndpoint(uid=1)
    data = endpoint.send(_jaus_message())
    dt = _timed(lambda: endpoint.receive(data), 100)
    assert dt < 0.05


def test_jaus_encode_time_budget():
    endpoint = JausEndpoint(uid=1)
    dt = _timed(lambda: endpoint.send(_jaus_message()), 200)
    assert dt < 0.01


def test_runner_step_time_budget():
    mission = ScenarioGenerator(world_size_m=20.0).generate("kesif", seed=2)
    spec = mission.terrain
    terrain = Terrain(
        width_m=spec.width_m,
        height_m=spec.height_m,
        seed=spec.seed,
        obstacle_count=spec.obstacle_count,
        forbidden_count=spec.forbidden_count,
    )
    runner = MissionRunner(dt_s=0.05, beam_count=24, lidar_max_range_m=8.0)
    start = time.perf_counter()
    metrics = runner.run(terrain, mission.weather, mission)
    total = time.perf_counter() - start
    assert total < 5.0
    assert metrics.steps > 0
    per_step = total / metrics.steps
    assert per_step < 0.01  # adım maliyeti 10 ms altında (10 Hz için geniş bütçe)


def test_performance_measurements_positive():
    assert WALL_S > 0.0