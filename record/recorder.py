"""
TRUSTIA Veri Kayıt (Sistem 4) — Görev kayıt cihazı.

Telemetri çerçeveleri, olaylar ve görev sonucunu JSONL biçiminde
diske kaydeder (her satır bağımsız JSON nesnesi → akışa dayanıklı,
hata anında kayıp minimal). Oynatma (replay) aynı dosyadan beslenir.
"""

from __future__ import annotations

import json
import os
import time
from typing import Dict, Iterator, List, Tuple

from core.api import TelemetryFrame
from simulation.runner import MissionMetrics


class MissionRecorder:
    """Tek görevin kaydını JSONL dosyasına yazar."""

    def __init__(self, directory: str, record_id: str = "") -> None:
        self.directory = directory
        os.makedirs(directory, exist_ok=True)
        self.record_id = record_id or f"kayit-{time.time_ns()}"
        self.path = os.path.join(directory, f"{self.record_id}.jsonl")
        self._metadata: Dict[str, object] = {}
        self._frame_count = 0
        self._file = open(self.path, "w", encoding="utf-8")

    # ---- meta / akış ----

    def set_metadata(self, **fields) -> None:
        self._metadata.update(fields)
        self._write_line({"type": "meta", "data": self._metadata})

    def start(self) -> "MissionRecorder":
        self._write_line({"type": "start", "at_ns": time.time_ns()})
        return self

    def stop(self) -> None:
        if self._file.closed:
            return
        self._write_line({"type": "stop", "at_ns": time.time_ns()})
        self._file_flush_close()

    def record_frame(self, frame: TelemetryFrame) -> None:
        self._write_line({"type": "telemetry", "frame": frame.to_dict()})
        self._frame_count += 1

    def record_event(self, category: str, message: str) -> None:
        self._write_line({
            "type": "event",
            "at_ns": time.time_ns(),
            "category": category,
            "message": message,
        })

    def record_result(self, metrics: MissionMetrics) -> None:
        self._write_line({"type": "result", "metrics": _metrics_dict(metrics)})

    def frame_count(self) -> int:
        return self._frame_count

    def close(self) -> None:
        self.stop()

    def __enter__(self) -> "MissionRecorder":
        return self.start()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    # ---- iç ----

    def _write_line(self, obj: dict) -> None:
        self._file.write(json.dumps(obj, ensure_ascii=False) + "\n")
        self._file.flush()

    def _file_flush_close(self) -> None:
        if self._file.closed:
            return
        self._file.flush()
        self._file.close()


def _metrics_dict(metrics: MissionMetrics) -> dict:
    return {
        "mission_id": metrics.mission_id,
        "mission_type": metrics.mission_type,
        "success": metrics.success,
        "failure_reason": metrics.failure_reason(),
        "collision": metrics.collision,
        "forbidden_violation": metrics.forbidden_violation,
        "time_out": metrics.time_out,
        "out_of_bounds": metrics.out_of_bounds,
        "stuck": metrics.stuck,
        "stuck_recoveries": metrics.stuck_recoveries,
        "steps": metrics.steps,
        "duration_s": round(metrics.duration_s, 3),
        "position_error_m": round(metrics.position_error_m, 4),
        "final_position_error_m": round(metrics.final_position_error_m, 4),
        "route_deviation_m": round(metrics.route_deviation_m, 4),
        "reaction_time_s": round(metrics.reaction_time_s, 4),
        "min_obstacle_clearance_m": round(metrics.min_obstacle_clearance_m, 4),
        "map_known_ratio": round(metrics.map_known_ratio, 4),
    }


def read_recording(path: str) -> List[dict]:
    """Kayıt dosyasını sıralı kayıt listesine okur (her kayıt bir dict)."""
    entries: List[dict] = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            entries.append(json.loads(line))
    return entries