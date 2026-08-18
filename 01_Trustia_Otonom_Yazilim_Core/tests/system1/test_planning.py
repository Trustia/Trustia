"""Sistem 1 — Planlama (A*, RRT, yerel kaçınma) birim testleri."""

import math

import pytest

from core.errors import PlanningError
from planning import (
    GridMap,
    AStarPlanner,
    RrtPlanner,
    Path,
    Waypoint,
    LocalAvoidance,
    PathFollower,
)


def open_grid(width=50.0, height=50.0):
    return GridMap(resolution_m=1.0, width_m=width, height_m=height)


def test_grid_traversable_defaults():
    grid = open_grid()
    assert grid.is_traversable(2.5, 2.5) is True
    assert grid.is_traversable(-5.0, -5.0) is False  # harita dışı


def test_grid_mark_obstacle():
    grid = open_grid()
    grid.mark_obstacle(5.0, 5.0)
    assert grid.is_traversable(5.0, 5.0) is False
    assert grid.is_traversable(1.0, 1.0) is True


def test_grid_mark_obstacle_with_radius():
    grid = open_grid()
    grid.mark_obstacle(10.0, 10.0, radius_m=2.0)
    assert grid.is_traversable(10.0, 10.0) is False
    assert grid.is_traversable(11.0, 10.0) is False
    assert grid.is_traversable(14.0, 10.0) is True


def test_a_star_straight_line():
    grid = open_grid()
    planner = AStarPlanner(grid)
    path = planner.plan((0.5, 0.5), (10.5, 0.5))
    assert len(path.waypoints) >= 2
    assert abs(path.length_m - 10.0) < 1.5


def test_a_star_around_wall():
    grid = open_grid()
    # x=5 sütununu engelle → A* dolanmalı
    for y in range(0, 30):
        grid.mark_obstacle(5.0, y)
    planner = AStarPlanner(grid)
    path = planner.plan((0.5, 15.5), (20.5, 15.5))
    assert len(path.waypoints) >= 2
    for wp in path.waypoints:
        assert grid.is_traversable(wp.x_m, wp.y_m) or wp.y_m in (15.5,)
    # duvar etrafında dolandığı için düzden uzun
    assert path.length_m > 20.0


def test_a_star_impossible_raises():
    grid = open_grid(width=10.0, height=10.0)
    for x in range(0, 10):
        for y in range(0, 10):
            grid.mark_obstacle(x + 0.5, y + 0.5)
    planner = AStarPlanner(grid)
    with pytest.raises(PlanningError):
        planner.plan((0.5, 0.5), (9.5, 9.5))


def test_a_star_start_on_obstacle_raises():
    grid = open_grid()
    grid.mark_obstacle(0.5, 0.5)
    planner = AStarPlanner(grid)
    with pytest.raises(PlanningError):
        planner.plan((0.5, 0.5), (5.5, 5.5))


def test_path_smooth_removes_collinear():
    points = [
        Waypoint(0.0, 0.0),
        Waypoint(1.0, 0.0),
        Waypoint(2.0, 0.0),
        Waypoint(3.0, 1.0),
        Waypoint(4.0, 2.0),
    ]
    path = Path(points)
    smoothed = path.smooth()
    assert len(smoothed.waypoints) < len(points)
    assert smoothed.waypoints[0] == points[0]
    assert smoothed.waypoints[-1] == points[-1]


def test_path_length():
    points = [Waypoint(0.0, 0.0), Waypoint(3.0, 0.0), Waypoint(3.0, 4.0)]
    path = Path(points)
    assert abs(path.length_m - 7.0) < 1e-9


def test_rrt_finds_path_open_space():
    grid = open_grid()
    planner = RrtPlanner(
        is_traversable=grid.is_traversable,
        step_size_m=1.5,
        max_iterations=3000,
        goal_bias=0.15,
        seed=42,
    )
    path = planner.plan(
        (0.5, 0.5),
        (30.5, 30.5),
        bounds=(0.0, 50.0, 0.0, 50.0),
    )
    assert len(path.waypoints) >= 2
    first = path.waypoints[0]
    last = path.waypoints[-1]
    assert abs(first.x_m - 0.5) < 1e-6
    assert abs(last.x_m - 30.5) < 1e-6


def test_rrt_impossible_raises():
    grid = open_grid(width=10.0, height=10.0)
    for x in range(0, 10):
        for y in range(0, 10):
            grid.mark_obstacle(x + 0.5, y + 0.5)
    planner = RrtPlanner(grid.is_traversable, max_iterations=50, seed=1)
    with pytest.raises(PlanningError):
        planner.plan((0.5, 0.5), (9.5, 9.5), (0.0, 10.0, 0.0, 10.0))


def test_rrt_invalid_params():
    with pytest.raises(PlanningError):
        RrtPlanner(lambda x, y: True, step_size_m=0.0)


def test_local_avoidance_no_obstacle():
    avoidance = LocalAvoidance(avoidance_radius_m=5.0)
    heading = avoidance.avoid(math.radians(0.0), [])
    assert abs(heading - 0.0) < 1e-9


def test_local_avoidance_pushes_away():
    avoidance = LocalAvoidance(avoidance_radius_m=5.0)
    # engel tam ileride (2 m, 0°) → araç sağa/sola kaçmalı
    heading = avoidance.avoid(math.radians(0.0), [(2.0, 0.0, 0.5)])
    assert heading != 0.0
    assert abs(heading) > math.radians(10.0)


def test_local_avoidance_far_obstacle_ignored():
    avoidance = LocalAvoidance(avoidance_radius_m=5.0)
    heading = avoidance.avoid(math.radians(0.0), [(50.0, 0.0, 0.5)])
    assert abs(heading - 0.0) < 1e-9


def test_follower_targets_first_waypoint():
    path = Path([Waypoint(5.0, 0.0), Waypoint(10.0, 0.0)])
    follower = PathFollower(path)
    assert follower.index == 0
    target = follower.current_target()
    assert target.x_m == 5.0


def test_follower_advance_and_complete():
    path = Path([Waypoint(1.0, 0.0), Waypoint(2.0, 0.0)])
    follower = PathFollower(path, arrival_tolerance_m=0.3)
    assert follower.advance((1.0, 0.0)) is False  # ilk noktaya vardık, ikinciye geçti
    assert follower.index == 1
    assert follower.advance((2.0, 0.0)) is True   # rota bitti
    with pytest.raises(PlanningError):
        follower.current_target()


def test_follower_steer_towards_target():
    path = Path([Waypoint(5.0, 0.0)])
    follower = PathFollower(path)
    # araç (0,0) ve baş 90° → sola 90° dönüş gerekir
    steer = follower.steer((0.0, 0.0), math.pi / 2)
    assert abs(steer - (-math.pi / 2)) < 1e-9


def test_follower_empty_path_raises():
    with pytest.raises(PlanningError):
        PathFollower(Path([]))
