"""
Unit and Integration Tests for TRUSTIA ISO 21448 (SOTIF) Perception Safety Monitor.
Verifies phantom obstacle suppression, kinematic plausibility, and ASIL-D MRM timeout triggers.
"""

import pytest

from ai.tracking import TrackedObstacle3D
from security.sotif_monitor import Iso21448SotifMonitor, SotifPlausibilityReport


def test_sotif_nominal_operation():
    """Verify nominal SOTIF clearance when objects are physically plausible and latency is low."""
    monitor = Iso21448SotifMonitor(max_inference_latency_ms=35.0)

    obs = TrackedObstacle3D(
        track_id=1,
        class_name="car",
        x=20.0,
        y=0.0,
        z=0.0,
        width=2.0,
        length=4.5,
        height=1.5,
        yaw_rad=0.0,
        vx_mps=12.0,  # ~43 km/h
        vy_mps=0.0,
        yaw_rate_rads=0.0,
        confidence=0.92,
        status="CONFIRMED",
    )

    report = monitor.evaluate_perception([obs], inference_latency_ms=22.0)
    assert report.is_safe_to_proceed
    assert report.recommended_action == "NOMINAL_CONTINUE"
    assert report.target_decel_mps2 == 0.0
    assert len(report.verified_obstacles) == 1
    assert report.phantom_detections_rejected == 0


def test_sotif_kinematic_violation_rejection():
    """Verify that physically impossible actor velocities (e.g. pedestrian at 50 km/h) are rejected."""
    monitor = Iso21448SotifMonitor()

    super_ped = TrackedObstacle3D(
        track_id=2,
        class_name="pedestrian",
        x=10.0,
        y=1.0,
        z=0.0,
        width=0.7,
        length=0.7,
        height=1.7,
        yaw_rad=0.0,
        vx_mps=15.0,  # 54 km/h (Physically impossible for human runner in urban area)
        vy_mps=0.0,
        yaw_rate_rads=0.0,
        confidence=0.90,
        status="CONFIRMED",
    )

    report = monitor.evaluate_perception([super_ped], inference_latency_ms=20.0)
    assert report.kinematic_violations_count == 1
    assert len(report.verified_obstacles) == 0  # Unphysical object dropped


def test_sotif_phantom_braking_suppression():
    """Verify that low-confidence camera hallucinations unsupported by LiDAR are suppressed."""
    monitor = Iso21448SotifMonitor(min_lidar_points_in_box=3)

    phantom = TrackedObstacle3D(
        track_id=3,
        class_name="car",
        x=15.0,
        y=0.0,
        z=0.0,
        width=2.0,
        length=4.5,
        height=1.5,
        yaw_rad=0.0,
        vx_mps=0.0,
        vy_mps=0.0,
        yaw_rate_rads=0.0,
        confidence=0.55,  # Low confidence
        status="TENTATIVE",
    )

    # Raw LiDAR points elsewhere (no points inside x in [12.75, 17.25], y in [-1, 1])
    raw_points = [(5.0, 5.0, 0.0, 10.0), (30.0, 10.0, 0.0, 15.0)]

    report = monitor.evaluate_perception([phantom], inference_latency_ms=20.0, raw_lidar_points=raw_points)
    assert report.phantom_detections_rejected == 1
    assert len(report.verified_obstacles) == 0  # Phantom obstacle suppressed to prevent ghost braking


def test_sotif_latency_consecutive_timeout_mrm():
    """Verify that consecutive perception latency overruns (>35ms) trigger ISO 26262 ASIL-D MRM."""
    monitor = Iso21448SotifMonitor(max_inference_latency_ms=35.0, watchdog_consecutive_timeout_limit=2)

    # Cycle 1: Single timeout triggers CAUTION_SLOWDOWN
    report1 = monitor.evaluate_perception([], inference_latency_ms=40.0)
    assert report1.latency_violation
    assert report1.recommended_action == "CAUTION_SLOWDOWN"
    assert report1.target_decel_mps2 == -0.8

    # Cycle 2: Second consecutive timeout trips ASIL-D Watchdog -> MRM_SAFE_STOP
    report2 = monitor.evaluate_perception([], inference_latency_ms=42.0)
    assert report2.latency_violation
    assert not report2.is_safe_to_proceed
    assert report2.recommended_action == "MRM_SAFE_STOP"
    assert report2.target_decel_mps2 == -1.5
