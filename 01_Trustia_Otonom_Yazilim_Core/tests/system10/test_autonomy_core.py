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
