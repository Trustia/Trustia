"""Sistem 4 — Veri Kayıt birim testleri.

Görev kaydedici (JSONL), kayıt oynatma, telemetri grafikleri (SVG)
ve görev raporu + hata analizi üretimini doğrular.
"""

from __future__ import annotations

import os

import pytest

from core.api import TelemetryFrame
from record import MissionRecorder, MissionReport, Replay
from record.graphs import line_svg, trajectory_svg
from record.recorder import read_recording
from simulation.runner import MissionMetrics


def make_frame(step=1, x=2.0, y=3.0, speed=1.0, battery=90.0, link=0.9):
    return TelemetryFrame(
        vehicle_id="A-01",
        sim_time_s=step * 0.1,
        step=step,
        position_m=(x, y),
        heading_deg=10.0,
        speed_mps=speed,
        target_m=(30.0, 30.0),
        clearance_m=2.0,
        obstacle_count=1,
        waypoint_index=0,
        waypoint_count=1,
        mission_phase="ACTIVE",
        gps_available=False,
        position_error_m=0.4,
        battery_percent=battery,
        link_quality=link,
        engine_ok=True,
    )


def make_metrics(success=True):
    return MissionMetrics(
        mission_id="G-0001",
        mission_type="kesif",
        success=success,
        steps=10,
        duration_s=1.0,
        position_error_m=0.5,
        final_position_error_m=0.7,
        route_deviation_m=0.3,
        reaction_time_s=0.27,
        min_obstacle_clearance_m=1.2,
    )


def record_mission(tmp_path):
    recorder = MissionRecorder(str(tmp_path), record_id="test_kayit").start()
    recorder.set_metadata(mission_id="G-0001", vehicle_id="A-01")
    for step in range(1, 6):
        recorder.record_frame(make_frame(step=step))
    recorder.record_event("analiz", "görev tamam")
    recorder.record_result(make_metrics())
    recorder.close()
    return recorder


# ---------------------------------------------------------- Recorder


def test_recorder_writes_jsonl_file(tmp_path):
    recorder = record_mission(tmp_path)
    assert recorder.path.endswith(".jsonl")
    assert recorder.frame_count() == 5
    assert os.path.getsize(recorder.path) > 0
    assert recorder.frame_count() == 5


def test_recording_has_all_record_types(tmp_path):
    record_mission(tmp_path)
    entries = read_recording(str(tmp_path / "test_kayit.jsonl"))
    types = {e["type"] for e in entries}
    assert {"meta", "start", "telemetry", "event", "result", "stop"} <= types


def test_recorder_context_manager(tmp_path):
    with MissionRecorder(str(tmp_path), record_id="ctx") as recorder:
        recorder.record_frame(make_frame())
    entries = read_recording(str(tmp_path / "ctx.jsonl"))
    assert len(entries) == 3  # start + telemetry + stop


def test_recorder_metadata_stored(tmp_path):
    record_mission(tmp_path)
    entries = read_recording(str(tmp_path / "test_kayit.jsonl"))
    meta = next(e for e in entries if e["type"] == "meta")
    assert meta["data"]["mission_id"] == "G-0001"


# ------------------------------------------------------------ Replay


def test_replay_load_frames_and_result(tmp_path):
    record_mission(tmp_path)
    replay = Replay.load(str(tmp_path / "test_kayit.jsonl"))
    assert len(replay.frames) == 5
    assert replay.success()
    assert replay.result["mission_type"] == "kesif"
    assert replay.metadata["vehicle_id"] == "A-01"
    assert len(replay.events) == 1


def test_replay_series_extraction(tmp_path):
    record_mission(tmp_path)
    replay = Replay.load(str(tmp_path / "test_kayit.jsonl"))
    assert replay.speeds() == [1.0] * 5
    assert replay.battery() == [90.0] * 5
    assert replay.positions() == [(2.0, 3.0)] * 5
    assert replay.step_numbers() == [1, 2, 3, 4, 5]
    assert replay.sim_times() == [0.1, 0.2, 0.3, 0.4, 0.5]


def test_replay_stats(tmp_path):
    record_mission(tmp_path)
    replay = Replay.load(str(tmp_path / "test_kayit.jsonl"))
    stats = replay.stats()
    assert stats["frame_count"] == 5
    assert stats["mean_speed_mps"] == 1.0
    assert stats["max_speed_mps"] == 1.0
    assert stats["mean_battery_percent"] == 90.0
    assert stats["duration_s"] == 0.5


def test_replay_frame_iterator(tmp_path):
    record_mission(tmp_path)
    replay = Replay.load(str(tmp_path / "test_kayit.jsonl"))
    frames = list(replay.frame_iterator())
    assert len(frames) == 5
    assert frames[0]["step"] == 1


# ----------------------------------------------------------- Graphs


def test_line_svg_written_and_valid(tmp_path):
    path = line_svg(
        str(tmp_path / "cizgi.svg"),
        [1, 2, 3, 4],
        {"hız": [0.5, 1.0, 0.8, 1.2]},
        title="Test",
    )
    content = open(path, encoding="utf-8").read()
    assert content.startswith("<svg")
    assert "polyline" in content
    assert "hız" in content


def test_trajectory_svg_written(tmp_path):
    path = trajectory_svg(
        str(tmp_path / "iz.svg"),
        [(1.0, 1.0), (5.0, 5.0), (10.0, 2.0)],
        world_size_m=20.0,
        obstacles=[(8.0, 8.0, 1.0)],
    )
    content = open(path, encoding="utf-8").read()
    assert "<circle" in content
    assert "<polyline" in content


# ----------------------------------------------------------- Report


def test_mission_report_writes_markdown_and_charts(tmp_path):
    record_mission(tmp_path)
    replay = Replay.load(str(tmp_path / "test_kayit.jsonl"))
    report_path = MissionReport(
        replay, world_size_m=20.0, record_path=str(tmp_path / "test_kayit.jsonl")
    ).write(str(tmp_path))
    content = open(report_path, encoding="utf-8").read()
    assert "# TRUSTIA GÖREV RAPORU" in content
    assert "Başarı | EVET" in content
    assert "G-0001" in content
    svg_count = len([f for f in os.listdir(tmp_path) if f.endswith(".svg")])
    assert svg_count == 3
    for chart in ("telemetry", "error", "trail"):
        assert chart in content


def test_mission_report_failure_analysis(tmp_path):
    recorder = MissionRecorder(str(tmp_path), record_id="basarisiz").start()
    for step in range(1, 4):
        recorder.record_frame(make_frame(step=step))
    recorder.record_result(make_metrics(success=False))
    recorder.close()
    replay = Replay.load(str(tmp_path / "basarisiz.jsonl"))
    assert not replay.success()
    assert replay.result["failure_reason"] == "adım limiti"
    # varsayılan: adım limiti dışında nedensiz başarısızlık metni üretir
    report = MissionReport(replay).write(str(tmp_path), base_name="basarisiz_rapor")
    content = open(report, encoding="utf-8").read()
    assert "Başarı | HAYIR" in content
    assert "HATA ANALİZİ" in content


def test_mission_report_empty_replay(tmp_path):
    recorder = MissionRecorder(str(tmp_path), record_id="bos").start()
    recorder.close()
    replay = Replay.load(str(tmp_path / "bos.jsonl"))
    report_path = MissionReport(replay).write(str(tmp_path), base_name="bos_rapor")
    content = open(report_path, encoding="utf-8").read()
    assert "Çerçeve sayısı" in content
    assert "Çerçeve sayısı:** 0" in content
