"""Sistem 3+4 — Uçtan uca "görev ver-izle-rapor al" entegrasyon testleri.

Komuta merkezinden görev siparişi → simülasyon dünyasında koşum →
canlı telemetri/alarm akışı → kayıt oynatma → görev raporu.
"""

from __future__ import annotations

import os

from command import CommandCenter, MissionOrder
from command.auth import Role, Session
from core.transforms import EnuPoint
from record import MissionRecorder, MissionReport, Replay
from simulation.runner import MissionRunner
from simulation.terrain import Terrain, Weather


def build_center():
    center = CommandCenter()
    center.access.set_role("admin", Role.ADMIN)
    center.access.set_role("op", Role.OPERATOR)
    center.register_vehicle("admin", "A-01", "Keşif Aracı 1")
    return center


def test_end_to_end_mission_flow(tmp_path):
    center = build_center()
    order = MissionOrder(
        order_id="G-1001",
        vehicle_id="A-01",
        mission_type="kesif",
        waypoints=[EnuPoint(east_m=30, north_m=30)],
        time_limit_s=180.0,
    )
    order_id = center.submit_mission("op", order)
    assert center.order("op", order_id)["state"] == "APPROVED"

    terrain = Terrain(width_m=40, height_m=40, seed=5)
    terrain.add_obstacle(15, 15, 1.5)
    terrain.add_forbidden(25, 10, 2.0)
    recorder = MissionRecorder(str(tmp_path), record_id="u2u").start()
    recorder.set_metadata(mission_id=order_id, vehicle_id="A-01", world_size_m=40.0)

    session = Session("op", center.access)
    metrics = center.dispatch(
        session,
        order_id,
        terrain,
        Weather(),
        MissionRunner(seed=3),
        start=(2, 2),
        telemetry_callback=recorder.record_frame,
    )
    recorder.record_result(metrics)
    recorder.close()

    assert recorder.frame_count() > 50
    assert center.order("op", order_id)["state"] in ("COMPLETE", "FAILED")
    snapshot = center.live_snapshot("op")
    assert snapshot["fleet"]["total_vehicles"] == 1
    assert snapshot["fleet"]["vehicles"][0]["frame_count"] > 50

    replay = Replay.load(recorder.path)
    assert replay.success() == metrics.success
    assert len(replay.frames) == recorder.frame_count()

    report_path = MissionReport(
        replay, world_size_m=40.0, record_path=recorder.path
    ).write(str(tmp_path))
    assert os.path.exists(report_path)
    content = open(report_path, encoding="utf-8").read()
    assert "G-1001" in content
    assert "Başarı |" in content


def test_end_to_end_unknown_vehicle_rejected():
    center = build_center()
    order = MissionOrder(
        order_id="G-1002",
        vehicle_id="YOK",
        waypoints=[EnuPoint(east_m=10, north_m=10)],
    )
    import pytest
    with pytest.raises(ValueError):
        center.submit_mission("op", order)


def test_end_to_end_dispatch_requires_approved():
    center = build_center()
    import pytest
    order = MissionOrder(
        order_id="G-1003",
        vehicle_id="A-01",
        waypoints=[EnuPoint(east_m=10, north_m=10)],
    )
    order_id = center.missions.submit(order)
    # onaylanmamış sipariş gönderilemez
    with pytest.raises(ValueError):
        center.dispatch(
            Session("op", center.access),
            order_id,
            Terrain(width_m=20, height_m=20, seed=1),
            Weather(),
            MissionRunner(seed=1),
            start=(1, 1),
        )


def test_end_to_end_viewer_cannot_dispatch():
    center = build_center()
    center.access.set_role("izleyici", Role.VIEWER)
    order = MissionOrder(
        order_id="G-1004",
        vehicle_id="A-01",
        waypoints=[EnuPoint(east_m=10, north_m=10)],
    )
    center.submit_mission("op", order)
    import pytest
    from command.auth import AccessDenied
    with pytest.raises(AccessDenied):
        center.dispatch(
            Session("izleyici", center.access),
            "G-1004",
            Terrain(width_m=20, height_m=20, seed=1),
            Weather(),
            MissionRunner(seed=1),
            start=(1, 1),
        )
