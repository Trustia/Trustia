"""
Tests for Trustia Enterprise AutonomyCore API.
"""

from core.autonomy_core import AutonomyCore


def test_autonomy_core_lifecycle():
    core = AutonomyCore()
    assert core._is_running is False
    
    start_res = core.start()
    assert start_res["status"] == "OPERATIONAL"
    assert start_res["autonomy_level"] == "SAE_LEVEL_4"
    assert core._is_running is True
    
    telemetry = core.get_telemetry()
    assert telemetry["is_active"] is True
    assert telemetry["safety_barrier"] == "ASIL_D_ACTIVE"
    
    target_res = core.set_target(100.5, 200.0, 1.57)
    assert target_res["status"] == "TRAJECTORY_COMPUTED"
    
    stop_res = core.stop()
    assert stop_res["status"] == "STANDBY"
    assert core._is_running is False


def test_autonomy_core_perception_pipeline():
    core = AutonomyCore()
    actors = [
        {"class": "car", "x": 15.0, "y": 0.0, "z": 0.0, "confidence": 0.95, "vx": 10.0},
        {"class": "pedestrian", "x": 8.0, "y": 2.0, "z": 0.0, "confidence": 0.88, "vy": -1.0}
    ]
    res = core.process_perception(simulated_actors=actors)
    assert res["num_detections"] == 2
    assert res["num_tracks"] == 2
    assert res["num_trajectories"] == 2
    assert res["is_safe"] is True
    assert res["sotif_status"] == "NOMINAL_CONTINUE"
