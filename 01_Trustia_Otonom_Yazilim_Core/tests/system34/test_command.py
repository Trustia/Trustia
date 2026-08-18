"""Sistem 3 — Komuta Merkezi birim testleri.

Filo yönetimi (çoklu araç, bağlantı durumu), görev siparişi/onay
akışı, alarm motoru (çarpışma riski, bağlantı kopması, batarya
kritik) ve rol tabanlı erişim kontrolünü doğrular.
"""

from __future__ import annotations

import time

import pytest

from command import CommandCenter, MissionOrder
from command.alarm import AlarmCode, AlarmEngine
from command.auth import AccessControl, AccessDenied, Permission, Role
from command.fleet import Fleet
from command.mission import MissionRegistry, OrderState
from core.api import TelemetryFrame, VehicleState
from core.transforms import EnuPoint


def make_frame(
    vehicle_id="A-01",
    battery=90.0,
    link=0.9,
    clearance=None,
    engine_ok=True,
    error=0.5,
    step=1,
):
    return TelemetryFrame(
        vehicle_id=vehicle_id,
        sim_time_s=step * 0.1,
        step=step,
        position_m=(2.0, 3.0),
        heading_deg=10.0,
        speed_mps=1.2,
        target_m=(30.0, 30.0),
        clearance_m=clearance,
        obstacle_count=1 if clearance is not None else 0,
        waypoint_index=0,
        waypoint_count=1,
        mission_phase="ACTIVE",
        gps_available=False,
        position_error_m=error,
        battery_percent=battery,
        link_quality=link,
        engine_ok=engine_ok,
    )


# ------------------------------------------------------------- Fleet


def test_fleet_register_and_count():
    fleet = Fleet()
    fleet.register("A-01")
    fleet.register("A-02", "İkinci Araç")
    assert fleet.count() == 2
    assert fleet.get("A-01").name == "A-01"
    assert fleet.get("A-02").name == "İkinci Araç"


def test_fleet_register_duplicate_rejected():
    fleet = Fleet()
    fleet.register("A-01")
    with pytest.raises(ValueError):
        fleet.register("A-01")


def test_fleet_unknown_vehicle_raises():
    fleet = Fleet()
    with pytest.raises(KeyError):
        fleet.get("YOK")


def test_fleet_ingest_telemetry_registers_unknown_vehicle():
    fleet = Fleet()
    fleet.ingest_telemetry(make_frame("A-99"))
    assert fleet.count() == 1
    assert fleet.get("A-99").last_frame.vehicle_id == "A-99"


def test_fleet_telemetry_updates_history():
    fleet = Fleet()
    for step in range(1, 6):
        fleet.ingest_telemetry(make_frame(step=step))
    vehicle = fleet.get("A-01")
    assert vehicle.frame_count() == 5
    assert vehicle.speed_mps == 1.2
    assert vehicle.position_m == (2.0, 3.0)


def test_fleet_history_limited():
    from command.fleet import RegisteredVehicle
    vehicle = RegisteredVehicle("A-01", max_history=10)
    for step in range(1, 20):
        vehicle.update(make_frame(step=step))
    assert vehicle.frame_count() == 10


def test_fleet_online_offline_detection():
    fleet = Fleet(link_timeout_s=1.0)
    fleet.ingest_telemetry(make_frame())
    now = time.time_ns()
    assert fleet.online_count(now) == 1
    assert fleet.offline_ids(now + 2_000_000_000) == ["A-01"]
    assert fleet.online_count(now + 2_000_000_000) == 0


def test_fleet_snapshot_shape():
    fleet = Fleet()
    fleet.ingest_telemetry(make_frame())
    snapshot = fleet.snapshot()
    assert snapshot["total_vehicles"] == 1
    assert snapshot["vehicles"][0]["vehicle_id"] == "A-01"
    assert snapshot["vehicles"][0]["state"] == VehicleState.STANDBY.name


# ------------------------------------------------------ Mission flow


def order(vehicle_id="A-01", waypoints=None, order_id="G-TEST"):
    points = waypoints if waypoints is not None else [EnuPoint(east_m=20, north_m=20)]
    return MissionOrder(
        order_id=order_id,
        vehicle_id=vehicle_id,
        mission_type="kesif",
        waypoints=points,
        time_limit_s=120.0,
    )


def test_mission_order_validate_empty_waypoints():
    with pytest.raises(ValueError):
        order(waypoints=[]).validate()


def test_mission_order_validate_bad_time_limit():
    bad = order()
    bad.time_limit_s = 0.0
    with pytest.raises(ValueError):
        bad.validate()


def test_mission_registry_lifecycle():
    registry = MissionRegistry()
    order_id = registry.submit(order())
    assert registry.state(order_id) == OrderState.PENDING
    registry.approve(order_id)
    assert registry.state(order_id) == OrderState.APPROVED
    registry.start(order_id)
    assert registry.state(order_id) == OrderState.ACTIVE
    registry.finish(order_id, success=True)
    assert registry.state(order_id) == OrderState.COMPLETE


def test_mission_registry_approve_requires_pending():
    registry = MissionRegistry()
    order_id = registry.submit(order())
    registry.approve(order_id)
    with pytest.raises(ValueError):
        registry.approve(order_id)


def test_mission_registry_reject_and_abort():
    registry = MissionRegistry()
    order_id = registry.submit(order())
    registry.reject(order_id, "yetki yok")
    assert registry.state(order_id) == OrderState.REJECTED
    order_id2 = registry.submit(order(order_id="G-TEST2"))
    registry.approve(order_id2)
    registry.abort(order_id2, "operatör iptal etti")
    assert registry.state(order_id2) == OrderState.ABORTED


def test_mission_order_to_simulation_mission():
    mission = order().to_simulation_mission(
        start=(1.0, 1.0), start_heading_rad=0.5, gps_available=False
    )
    assert mission.start == (1.0, 1.0)
    assert mission.waypoints == [(20.0, 20.0)]
    assert not mission.gps_available
    assert mission.mission_id == "G-TEST"


# ------------------------------------------------------------ Alarms


def test_alarm_engine_collision_risk():
    engine = AlarmEngine()
    produced = engine.evaluate(make_frame(clearance=0.4))
    codes = {a.code for a in produced if not a.cleared}
    assert AlarmCode.COLLISION_RISK in codes


def test_alarm_engine_dedupes_while_active():
    engine = AlarmEngine()
    first = engine.evaluate(make_frame(battery=15.0))
    second = engine.evaluate(make_frame(battery=14.0))
    active = engine.active_snapshot()
    low_battery = [a for a in active if a["code"] == "BATTERY_LOW"]
    assert len(low_battery) == 1


def test_alarm_engine_auto_clears_when_condition_fixes():
    engine = AlarmEngine()
    engine.evaluate(make_frame(battery=15.0))
    produced = engine.evaluate(make_frame(battery=80.0))
    cleared = [a for a in produced if a.cleared]
    assert any(a.code == AlarmCode.BATTERY_LOW for a in cleared)
    assert engine.total_active() == 0


def test_alarm_engine_link_loss_critical():
    engine = AlarmEngine()
    produced = engine.evaluate(make_frame(link=0.2))
    codes = {a.code for a in produced if not a.cleared}
    assert AlarmCode.LINK_LOSS in codes
    assert AlarmCode.LINK_WEAK in codes


def test_alarm_engine_engine_fault():
    engine = AlarmEngine()
    produced = engine.evaluate(make_frame(engine_ok=False))
    assert any(a.code == AlarmCode.ENGINE_FAULT for a in produced)


def test_alarm_engine_position_drift():
    engine = AlarmEngine()
    produced = engine.evaluate(make_frame(error=4.2))
    assert any(a.code == AlarmCode.POSITION_DRIFT for a in produced)


def test_alarm_engine_history_grows():
    engine = AlarmEngine()
    engine.evaluate(make_frame(battery=15.0))
    engine.evaluate(make_frame(battery=5.0))
    engine.evaluate(make_frame(battery=90.0))
    assert engine.count() == 2


# -------------------------------------------------------------- Auth


def test_role_permissions_matrix():
    access = AccessControl()
    access.set_role("operator", Role.OPERATOR)
    access.set_role("auditor", Role.AUDITOR)
    access.set_role("admin", Role.ADMIN)
    assert access.can("viewer", Permission.VIEW)
    assert not access.can("viewer", Permission.COMMAND)
    assert access.can("operator", Permission.ASSIGN_MISSION)
    assert not access.can("operator", Permission.MANAGE_FLEET)
    assert access.can("auditor", Permission.READ_LOG)
    assert not access.can("auditor", Permission.COMMAND)
    assert access.can("admin", Permission.MANAGE_ROLES)


def test_access_require_denied():
    access = AccessControl()
    access.set_role("op", Role.OPERATOR)
    with pytest.raises(AccessDenied):
        access.require("op", Permission.MANAGE_FLEET)


def test_access_default_role_is_viewer():
    access = AccessControl()
    assert access.role_of("kimse") == Role.VIEWER


# ------------------------------------------------------ CommandCenter


def test_command_center_submit_mission_requires_vehicle():
    cc = CommandCenter()
    cc.access.set_role("op", Role.OPERATOR)
    with pytest.raises(ValueError):
        cc.submit_mission("op", order())


def test_command_center_submit_mission_flow():
    cc = CommandCenter()
    cc.access.set_role("admin", Role.ADMIN)
    cc.access.set_role("op", Role.OPERATOR)
    cc.register_vehicle("admin", "A-01")
    order_id = cc.submit_mission("op", order())
    detail = cc.order("op", order_id)
    assert detail["state"] == OrderState.APPROVED.name
    assert detail["issued_by"] == "op"
    assert len(detail["waypoints"]) == 1


def test_command_center_viewer_cannot_submit():
    cc = CommandCenter()
    cc.access.set_role("izleyici", Role.VIEWER)
    cc.access.set_role("admin", Role.ADMIN)
    cc.register_vehicle("admin", "A-01")
    with pytest.raises(AccessDenied):
        cc.submit_mission("izleyici", order())


def test_command_center_live_snapshot():
    cc = CommandCenter()
    cc.access.set_role("op", Role.OPERATOR)
    cc.access.set_role("admin", Role.ADMIN)
    cc.register_vehicle("admin", "A-01")
    cc.submit_mission("op", order())
    cc.ingest_telemetry(make_frame(clearance=0.5, battery=12.0))
    snapshot = cc.live_snapshot("op")
    assert snapshot["fleet"]["total_vehicles"] == 1
    assert snapshot["missions"]["total_orders"] == 1
    assert len(snapshot["alarms"]) == 2  # çarpışma riski + batarya düşük


def test_command_center_orders_snapshot():
    cc = CommandCenter()
    cc.access.set_role("admin", Role.ADMIN)
    cc.access.set_role("op", Role.OPERATOR)
    cc.register_vehicle("admin", "A-01")
    cc.submit_mission("op", order())
    snapshot = cc.orders("op")
    assert snapshot["orders"][0]["state"] == "APPROVED"
