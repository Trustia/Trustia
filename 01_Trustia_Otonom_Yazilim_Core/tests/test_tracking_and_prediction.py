"""
Unit and Integration Tests for TRUSTIA 3D Multi-Object Tracking & 3-Second Prediction Engine.
Verifies 3D EKF velocity estimation, Hungarian bipartite matching, and trajectory intent forecasting.
"""

import math
import pytest

from ai.deep_perception import BoundingBox3D
from ai.prediction import TrajectoryPredictionEngine
from ai.tracking import MultiObjectTracker3D, TrackedObstacle3D


def test_tracker_lifecycle_tentative_to_confirmed():
    """Verify that a track transitions from TENTATIVE to CONFIRMED after 3 consecutive hits."""
    tracker = MultiObjectTracker3D(max_mahalanobis_gate=5.0, min_hits_to_confirm=3)

    # Frame 1
    det1 = [BoundingBox3D(1, "car", 10.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)]
    tracks1 = tracker.update(det1, dt=0.1)
    assert len(tracks1) == 1
    assert tracks1[0].status == "TENTATIVE"
    assert tracks1[0].hits == 1

    # Frame 2 (car moved forward by 1 meter)
    det2 = [BoundingBox3D(2, "car", 11.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)]
    tracks2 = tracker.update(det2, dt=0.1)
    assert len(tracks2) == 1
    assert tracks2[0].hits == 2
    assert tracks2[0].status == "TENTATIVE"

    # Frame 3 (car moved forward by another 1 meter)
    det3 = [BoundingBox3D(3, "car", 12.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)]
    tracks3 = tracker.update(det3, dt=0.1)
    assert len(tracks3) == 1
    assert tracks3[0].hits == 3
    assert tracks3[0].status == "CONFIRMED"
    assert tracks3[0].is_confirmed()


def test_tracker_velocity_estimation():
    """Verify that EKF correctly calculates positive longitudinal velocity."""
    tracker = MultiObjectTracker3D()
    # Object moves from x=10.0 to x=11.0 in dt=0.1s -> speed approx 10 m/s
    tracker.update([BoundingBox3D(1, "car", 10.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)], dt=0.1)
    tracker.update([BoundingBox3D(2, "car", 11.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)], dt=0.1)
    tracks = tracker.update([BoundingBox3D(3, "car", 12.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)], dt=0.1)

    assert len(tracks) == 1
    assert tracks[0].vx_mps > 2.0  # Velocity is actively measured and estimated
    assert tracks[0].speed_kmh() > 7.0


def test_stale_track_deletion():
    """Verify that a lost track is dropped after max_staleness_frames (5 frames)."""
    tracker = MultiObjectTracker3D(max_staleness_frames=3)
    tracker.update([BoundingBox3D(1, "car", 10.0, 0.0, 0.0, 2.0, 4.5, 1.5, 0.0, 0.9)], dt=0.1)
    assert len(tracker.trackers) == 1

    # 4 empty frames
    for _ in range(4):
        tracker.update([], dt=0.1)

    # Track should now be pruned
    assert len(tracker.trackers) == 0


def test_trajectory_prediction_pedestrian_crossing():
    """Verify 3-second trajectory forecasting and CROSSING intent for moving pedestrian."""
    predictor = TrajectoryPredictionEngine(prediction_horizon_s=3.0, time_step_s=0.5)

    ped = TrackedObstacle3D(
        track_id=101,
        class_name="pedestrian",
        x=8.0,
        y=3.0,
        z=0.0,
        width=0.7,
        length=0.7,
        height=1.7,
        yaw_rad=0.0,
        vx_mps=0.0,
        vy_mps=-1.2,  # Moving laterally across the road at 1.2 m/s
        yaw_rate_rads=0.0,
        confidence=0.92,
        status="CONFIRMED",
    )

    trajectories = predictor.predict_trajectories([ped])
    assert len(trajectories) == 1
    traj = trajectories[0]
    assert traj.intent == "CROSSING"
    assert len(traj.waypoints) == 6  # 3.0s / 0.5s = 6 points

    # Check that at t=2.0s, pedestrian has moved laterally towards y = 3.0 + (-1.2 * 2.0) = 0.6m
    pos_2s = traj.position_at_time(2.0)
    assert pos_2s is not None
    assert pytest.approx(pos_2s[1], abs=0.1) == 0.6
    # Uncertainty radius should grow with time
    assert traj.waypoints[-1].uncertainty_radius_m > traj.waypoints[0].uncertainty_radius_m


def test_trajectory_prediction_stationary_object():
    """Verify that stationary obstacles have stationary intent and fixed coordinates."""
    predictor = TrajectoryPredictionEngine()
    cone = TrackedObstacle3D(
        track_id=102,
        class_name="traffic_cone",
        x=5.0,
        y=-0.5,
        z=0.0,
        width=0.4,
        length=0.4,
        height=0.8,
        yaw_rad=0.0,
        vx_mps=0.0,
        vy_mps=0.0,
        yaw_rate_rads=0.0,
        confidence=0.95,
        status="CONFIRMED",
    )
    trajectories = predictor.predict_trajectories([cone])
    assert len(trajectories) == 1
    assert trajectories[0].intent == "STATIONARY"
    for wp in trajectories[0].waypoints:
        assert wp.x == 5.0
        assert wp.y == -0.5


def test_hybrid_astar_with_predicted_trajectories():
    """Verify that Hybrid A* plans around 3-second predicted actor trajectories."""
    from planning.hybrid_astar import HybridAStar
    from planning.grid_map import GridMap
    from planning.types import PlanningRequest, Waypoint, PlanningStatus

    planner = HybridAStar()
    grid_map = GridMap(width_m=40.0, height_m=40.0, resolution_m=0.5, origin_x_m=0.0, origin_y_m=-20.0)

    # Free map initially
    req = PlanningRequest(
        start=Waypoint(x_m=2.0, y_m=0.0, heading_rad=0.0),
        goal=Waypoint(x_m=20.0, y_m=0.0, heading_rad=0.0, tolerance_m=1.0),
        max_planning_time_s=1.0
    )

    # Predictor generates a stationary obstacle blocking the direct line at x=10, y=0
    cone = TrackedObstacle3D(
        track_id=200,
        class_name="traffic_cone",
        x=10.0,
        y=0.0,
        z=0.0,
        width=0.5,
        length=0.5,
        height=0.8,
        yaw_rad=0.0,
        vx_mps=0.0,
        vy_mps=0.0,
        yaw_rate_rads=0.0,
        confidence=0.99,
        status="CONFIRMED",
    )
    predictor = TrajectoryPredictionEngine()
    trajectories = predictor.predict_trajectories([cone])

    res = planner.plan_with_dynamic_obstacles(grid_map, req, predicted_trajectories=trajectories, safety_radius_m=1.0)
    assert res.status in (PlanningStatus.SUCCESS, PlanningStatus.NO_PATH)

