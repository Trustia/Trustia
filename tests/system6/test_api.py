"""Sistem 6 — API katmanı birim testleri."""

import pytest

from core.api import (
    CommandExecutor,
    CommandResult,
    CommandType,
    VehicleState,
    MissionPhase,
    VehicleStatus,
    Waypoint,
)
from core.errors import TrustiaError
from core.transforms import EnuPoint, GeoPoint, LocalFrame


class RecordingHandler:
    """Tüm komutları kaydeden ve sonucu döndüren test işleyicisi."""

    def __init__(self, success: bool = True) -> None:
        self.commands = []
        self.success = success

    def execute(self, command) -> CommandResult:
        self.commands.append(command)
        return CommandResult(
            command_id=command.command_id,
            success=self.success,
            message="tamam",
        )


def make_executor(handler=None):
    return CommandExecutor(handler or RecordingHandler())


def test_command_ids_increment():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    executor.standup()
    executor.shutdown()
    assert handler.commands[0].command_id == 1
    assert handler.commands[1].command_id == 2


def test_standup_command_type():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    result = executor.standup()
    assert result.success is True
    assert handler.commands[0].command_type == CommandType.STANDUP


def test_mission_commands():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    executor.start_mission(7)
    executor.pause_mission()
    executor.resume_mission()
    executor.stop_mission()
    types = [c.command_type for c in handler.commands]
    assert types == [
        CommandType.START_MISSION,
        CommandType.PAUSE_MISSION,
        CommandType.RESUME_MISSION,
        CommandType.STOP_MISSION,
    ]
    assert handler.commands[0].param("mission_id") == 7


def test_emergency_stop_type():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    executor.emergency_stop()
    executor.emergency_clear()
    types = [c.command_type for c in handler.commands]
    assert types == [
        CommandType.EMERGENCY_STOP,
        CommandType.EMERGENCY_CLEAR,
    ]


def test_negative_speed_rejected():
    executor = make_executor()
    with pytest.raises(TrustiaError):
        executor.set_speed(-1.0)


def test_out_of_range_heading_rejected():
    executor = make_executor()
    with pytest.raises(TrustiaError):
        executor.set_heading(361.0)


def test_empty_waypoints_rejected():
    executor = make_executor()
    with pytest.raises(TrustiaError):
        executor.load_waypoints([])


def test_load_waypoints_passes_list():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    wp = [Waypoint(point=EnuPoint(10.0, 20.0), speed_mps=2.0)]
    executor.load_waypoints(wp)
    assert handler.commands[0].param("waypoints") == wp


def test_return_home_type():
    handler = RecordingHandler()
    executor = CommandExecutor(handler)
    executor.return_home()
    assert handler.commands[0].command_type == CommandType.RETURN_HOME


def test_waypoint_from_geo_uses_frame():
    frame = LocalFrame(GeoPoint(39.92077, 32.85411))
    wp = Waypoint.from_geo(GeoPoint(39.9215, 32.855), origin_frame=frame)
    assert wp.point.north_m > 50.0


def test_failure_result_propagates():
    handler = RecordingHandler(success=False)
    executor = CommandExecutor(handler)
    result = executor.standup()
    assert result.success is False
    assert result.message == "tamam"


def test_vehicle_status_defaults():
    status = VehicleStatus()
    assert status.state == VehicleState.STANDBY
    assert status.phase == MissionPhase.IDLE
    assert status.is_operational() is False


def test_vehicle_status_operational_states():
    assert VehicleStatus(state=VehicleState.READY).is_operational() is True
    assert VehicleStatus(state=VehicleState.NAVIGATING).is_operational() is True
    assert VehicleStatus(state=VehicleState.FAULT).is_operational() is False


def test_vehicle_status_to_dict():
    status = VehicleStatus(
        state=VehicleState.NAVIGATING,
        position_m=EnuPoint(1.0, 2.0, 0.0),
        heading_deg=90.0,
    )
    data = status.to_dict()
    assert data["state"] == "NAVIGATING"
    assert data["position"]["east_m"] == 1.0
    assert data["heading_deg"] == 90.0
