"""Sistem 1 — SLAM (GPS'siz konum + occupancy grid) birim testleri."""

import math

import pytest

from core.errors import SensorError
from slam import (
    OdometryIntegrator,
    OdometryMeasurement,
    OccupancyGrid,
    SlamEngine,
    SlamState,
    Pose2D,
    angular_difference,
)


def measure(distance, heading_delta=0.0):
    return OdometryMeasurement(
        delta_distance_m=distance,
        delta_heading_rad=heading_delta,
    )


def test_straight_line_integration():
    odom = OdometryIntegrator()
    for _ in range(10):
        odom.update(measure(1.0))
    pose = odom.pose
    assert abs(pose.x_m - 10.0) < 1e-9
    assert abs(pose.y_m) < 1e-9
    assert abs(odom.total_distance_m - 10.0) < 1e-9


def test_turn_heading_integration():
    odom = OdometryIntegrator()
    odom.update(measure(1.0, math.pi / 2))
    pose = odom.pose
    assert abs(pose.heading_rad - math.pi / 2) < 1e-9


def test_heading_wraps_to_pi():
    odom = OdometryIntegrator()
    odom.update(measure(0.0, math.pi + 0.5))
    pose = odom.pose
    assert -math.pi < pose.heading_rad <= math.pi


def test_circular_turn_returns_center():
    odom = OdometryIntegrator()
    radius = 2.0
    steps = 8
    for _ in range(steps):
        # Yol uzunluğu = r * dθ
        odom.update(measure(radius * 2 * math.pi / steps, 2 * math.pi / steps))
    pose = odom.pose
    assert abs(pose.x_m - 0.0) < 1e-6
    assert abs(pose.y_m - 0.0) < 1e-6


def test_negative_distance_rejected():
    odom = OdometryIntegrator()
    with pytest.raises(SensorError):
        odom.update(measure(-1.0))


def test_reset_returns_origin():
    odom = OdometryIntegrator()
    odom.update(measure(5.0))
    odom.reset()
    pose = odom.pose
    assert pose.x_m == 0.0 and pose.y_m == 0.0


def test_grid_default_state_unknown():
    grid = OccupancyGrid(resolution_m=0.5)
    assert grid.get_cell(0.0, 0.0) == OccupancyGrid.UNKNOWN
    assert grid.known_ratio() == 0.0


def test_grid_mark_free_and_occupied():
    grid = OccupancyGrid(resolution_m=0.5)
    grid.mark_free(0.0, 0.0)
    assert grid.is_free(0.0, 0.0)
    grid.mark_occupied(1.0, 1.0)
    assert grid.is_occupied(1.0, 1.0)
    assert grid.count_state(OccupancyGrid.OCCUPIED) == 1


def test_grid_out_of_bounds_unknown():
    grid = OccupancyGrid(resolution_m=0.5, width_m=10.0, height_m=10.0)
    assert grid.get_cell(100.0, 100.0) == OccupancyGrid.UNKNOWN
    assert grid.is_occupied(100.0, 100.0) is False


def test_grid_invalid_size():
    with pytest.raises(SensorError):
        OccupancyGrid(width_m=0.0)


def test_grid_scan_marks_free_path_and_hit():
    grid = OccupancyGrid(resolution_m=1.0, width_m=40.0, height_m=40.0)
    origin = (0.0, 0.0)
    hits = [(10.0, 0.0), (10.0, 5.0)]
    updated = grid.update_scan(origin, hits)
    assert updated >= 2
    # hedef hücreler işgal
    assert grid.is_occupied(10.0, 0.0)
    assert grid.is_occupied(10.0, 5.0)
    # ışın yolu serbest
    assert grid.is_free(5.0, 0.0)
    assert grid.known_ratio() > 0.0


def test_grid_known_ratio_after_scan():
    grid = OccupancyGrid(resolution_m=1.0, width_m=40.0, height_m=40.0)
    assert grid.known_ratio() == 0.0
    grid.update_scan((0.0, 0.0), [(10.0, 0.0)])
    assert grid.known_ratio() > 0.0


def test_raycast_returns_cells():
    grid = OccupancyGrid(resolution_m=1.0, width_m=40.0, height_m=40.0)
    cells = grid.raycast((0.0, 0.0), (5.0, 0.0))
    assert len(cells) >= 5
    assert (0.5, 0.5) in cells
    assert (5.5, 0.5) in cells


def test_neighbors_4():
    grid = OccupancyGrid(resolution_m=1.0, width_m=40.0, height_m=40.0)
    neighbors = grid.neighbors_4(5.0, 5.0)
    assert len(neighbors) == 4


def test_slam_engine_step_state():
    engine = SlamEngine()
    state = engine.step(measure(2.0), scan_hits=[(5.0, 0.0)])
    assert isinstance(state, SlamState)
    assert abs(state.pose.x_m - 2.0) < 1e-9
    assert state.occupied_cells >= 1
    assert state.total_distance_m == 2.0


def test_slam_engine_correction():
    engine = SlamEngine()
    engine.step(measure(100.0))  # odometri sapması
    engine.apply_correction(Pose2D(x_m=3.0, y_m=0.0))
    pose = engine.pose
    assert abs(pose.x_m - 3.0) < 1e-9
    assert engine.step(measure(1.0)).correction_count == 1


def test_slam_engine_reset():
    engine = SlamEngine()
    engine.step(measure(5.0))
    engine.reset()
    assert engine.pose.x_m == 0.0
    assert engine.grid.known_ratio() == 0.0


def test_angular_difference():
    assert abs(angular_difference(0.0, math.pi / 2) - math.pi / 2) < 1e-9
    # en kısa yol: 170° → -170° yönünde 340° değil
    assert abs(angular_difference(0.0, math.radians(170))) - math.pi < 1e-6
