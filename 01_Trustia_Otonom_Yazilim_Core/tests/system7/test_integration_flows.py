"""Sistem 7 — Çapraz sistem entegrasyon akışları.

Komuta → simülasyon → kayıt → rapor → güvenlik → algı zincirini uçtan
uca doğrular (Sistem 3+2+4+5+9 birlikte çalışır).
"""

from __future__ import annotations

import os

import pytest

from ai.training import make_terrain_dataset, train_classifier
from ai.traversability import TRAVERSABILITY
from command import CommandCenter
from command.auth import Role
from command.mission import MissionOrder
from core.api import TelemetryFrame
from core.transforms import EnuPoint
from record.recorder import MissionRecorder, read_recording
from security import Shield
from simulation.runner import MissionRunner
from simulation.scenario import ScenarioGenerator
from simulation.terrain import Terrain


def _build_mission(mission_type="kesif", seed=11):
    mission = ScenarioGenerator(world_size_m=20.0).generate(mission_type, seed)
    spec = mission.terrain
    terrain = Terrain(
        width_m=spec.width_m,
        height_m=spec.height_m,
        seed=spec.seed,
        obstacle_count=spec.obstacle_count,
        forbidden_count=spec.forbidden_count,
    )
    return terrain, mission


class TestCommandToSimulation:
    def test_command_mission_order_lifecycle(self):
        from command import CommandCenter

        center = CommandCenter()
        center.access.set_role("operator", Role.ADMIN)
        center.register_vehicle("operator", "A-1")
        order = MissionOrder(
            order_id="m-1",
            vehicle_id="A-1",
            waypoints=[EnuPoint(east_m=12.0, north_m=10.0)],
            mission_type="kesif",
            time_limit_s=40.0,
        )
        order_id = center.submit_mission("operator", order)
        result = center.order("operator", order_id)
        assert result["state"] == "APPROVED"
        assert result["waypoints"] == [(12.0, 10.0)]

    def test_command_rejects_unknown_vehicle(self):
        from command import CommandCenter

        center = CommandCenter()
        center.access.set_role("operator", Role.ADMIN)
        center.register_vehicle("operator", "A-1")
        order = MissionOrder(
            order_id="m-2",
            vehicle_id="YOK",
            waypoints=[EnuPoint(east_m=5.0, north_m=5.0)],
            time_limit_s=40.0,
        )
        with pytest.raises(ValueError):
            center.submit_mission("operator", order)

    def test_mission_order_validation(self):
        order = MissionOrder(
            order_id="m-3", vehicle_id="A-1", waypoints=[], time_limit_s=40.0
        )
        with pytest.raises(ValueError):
            order.validate()


class TestSimulationToRecording:
    def test_recording_roundtrip(self, tmp_path):
        frames = []
        terrain, mission = _build_mission("kesif", seed=12)
        runner = MissionRunner(dt_s=0.05, beam_count=24, lidar_max_range_m=8.0)
        runner.run(
            terrain,
            mission.weather,
            mission,
            telemetry_callback=frames.append,
        )
        path = os.path.join(str(tmp_path), "kayit.jsonl")
        recorder = MissionRecorder(str(tmp_path), record_id="kayit")
        recorder.set_metadata(mission_id="t-1", vehicle_id="A-1")
        for frame in frames[::50]:
            recorder.record_frame(frame)
        recorder.record_event("tamamlandi", "görev bitti")
        metrics = runner.run(terrain, mission.weather, mission)
        recorder.record_result(metrics)
        recorder.close()
        lines = list(read_recording(path))
        assert lines
        assert lines[0]["type"] == "meta"
        assert lines[0]["data"]["mission_id"] == "t-1"
        assert any(l.get("category") == "tamamlandi" for l in lines)

    def test_recording_frame_content(self, tmp_path):
        terrain, mission = _build_mission("kesif", seed=12)
        frames = []
        MissionRunner(dt_s=0.05, beam_count=24, lidar_max_range_m=8.0).run(
            terrain, mission.weather, mission, telemetry_callback=frames.append
        )
        frame = frames[0]
        assert frame.vehicle_id == mission.mission_id
        assert frame.mission_phase == "ACTIVE"
        assert frame.gps_available is True
        assert frame.step >= 1


class TestSafetyAndAI:
    def test_estop_blocks_drive(self, tmp_path):
        shield = Shield(audit_directory=str(tmp_path))
        decision = shield.validate_command(
            user="operator", action="drive", speed_mps=2.0, heading_deg=90.0
        )
        assert decision.valid
        shield.emergency_stop(source="test", message="acil")
        blocked = shield.validate_command(
            user="operator", action="drive", speed_mps=2.0, heading_deg=90.0
        )
        assert not blocked.valid
        shield.close()

    def test_audit_log_written(self, tmp_path):
        shield = Shield(audit_directory=str(tmp_path))
        shield.validate_command(
            user="x", action="drive", speed_mps=1.0
        )
        shield.emergency_stop(source="op", message="r")
        records = shield.audit_query()
        assert len(records) >= 2
        shield.close()

    def test_terrain_classes_match_traversability(self):
        assert set(TRAVERSABILITY) == {
            "asfalt", "cimen", "camur", "kaya", "cukur", "su"
        }

    def test_ai_model_trains_with_dataset(self):
        samples = make_terrain_dataset(per_class=10)
        result = train_classifier(samples, epochs=30)
        assert result.train_accuracy >= 0.7
        assert result.eval_accuracy >= 0.5


class TestFleetTelemetry:
    @staticmethod
    def _frame(vehicle_id="A-2", **overrides):
        values = dict(
            vehicle_id=vehicle_id,
            sim_time_s=5.0,
            step=100,
            position_m=(10.0, 10.0),
            heading_deg=90.0,
            speed_mps=1.0,
            target_m=(20.0, 20.0),
            clearance_m=1.0,
            obstacle_count=1,
            waypoint_index=0,
            waypoint_count=3,
            mission_phase="ACTIVE",
            gps_available=True,
            position_error_m=0.5,
            battery_percent=90.0,
            link_quality=0.9,
            engine_ok=True,
        )
        values.update(overrides)
        return TelemetryFrame(**values)

    def test_fleet_snapshot(self):
        center = CommandCenter()
        center.access.set_role("operator", Role.ADMIN)
        center.register_vehicle("operator", "A-1")
        snapshot = center.live_snapshot("operator")
        assert isinstance(snapshot["fleet"], dict)
        assert snapshot["fleet"]

    def test_ingest_telemetry_updates_fleet(self):
        center = CommandCenter()
        center.access.set_role("operator", Role.ADMIN)
        center.register_vehicle("operator", "A-2")
        vehicle, alarms = center.ingest_telemetry(self._frame())
        assert vehicle.is_online
        assert alarms == []

    def test_telemetry_frame_to_dict(self):
        data = self._frame().to_dict()
        assert data["vehicle_id"] == "A-2"
        assert data["speed_mps"] == 1.0
        assert "position_m" in data