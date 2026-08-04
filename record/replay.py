"""
TRUSTIA Veri Kayıt (Sistem 4) — Kayıt oynatma.

Kaydedilmiş görevi adım adım yeniden oynatır: telemetri çerçeveleri,
olaylar ve sonuç. Telemetri grafikleri ve görev raporları bu
oynatıcıdan beslenir (PLAN: "kayıt oynatma, telemetri grafikleri,
görev raporları, hata analizi").
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional

from record.recorder import read_recording


@dataclass
class Replay:
    """Bir görev kaydının belleğe alınmış oynatma görünümü."""

    metadata: Dict[str, object] = field(default_factory=dict)
    frames: List[dict] = field(default_factory=list)
    events: List[dict] = field(default_factory=list)
    result: Optional[dict] = None
    started_at_ns: Optional[int] = None
    stopped_at_ns: Optional[int] = None

    @classmethod
    def load(cls, path: str) -> "Replay":
        replay = cls()
        for record in read_recording(path):
            record_type = record.get("type")
            if record_type == "meta":
                replay.metadata.update(record.get("data", {}))
            elif record_type == "telemetry":
                replay.frames.append(record["frame"])
            elif record_type == "event":
                replay.events.append(record)
            elif record_type == "result":
                replay.result = record.get("metrics")
            elif record_type == "start":
                replay.started_at_ns = record.get("at_ns")
            elif record_type == "stop":
                replay.stopped_at_ns = record.get("at_ns")
        return replay

    def frame_iterator(self) -> Iterator[dict]:
        return iter(self.frames)

    # ---- özet seriler (grafik ve istatistik için) ----

    def time_series(self, key: str) -> List[float]:
        """Çerçeve serilerini (hız, batarya, link, konum hatası...) döndürür."""
        return [f[key] for f in self.frames if key in f]

    def positions(self) -> List[tuple]:
        return [tuple(f["position_m"]) for f in self.frames]

    def speeds(self) -> List[float]:
        return self.time_series("speed_mps")

    def battery(self) -> List[float]:
        return self.time_series("battery_percent")

    def link_quality(self) -> List[float]:
        return self.time_series("link_quality")

    def position_error(self) -> List[float]:
        return self.time_series("position_error_m")

    def step_numbers(self) -> List[int]:
        return [f["step"] for f in self.frames]

    def sim_times(self) -> List[float]:
        return [f["sim_time_s"] for f in self.frames]

    # ---- istatistikler ----

    def stats(self) -> dict:
        speeds = self.speeds()
        errors = self.position_error()
        links = self.link_quality()
        return {
            "frame_count": len(self.frames),
            "mean_speed_mps": round(_mean(speeds), 3),
            "max_speed_mps": round(max(speeds), 3) if speeds else 0.0,
            "mean_position_error_m": round(_mean(errors), 3),
            "max_position_error_m": round(max(errors), 3) if errors else 0.0,
            "min_link_quality": round(min(links), 3) if links else 0.0,
            "mean_battery_percent": round(_mean(self.battery()), 2),
            "duration_s": (
                round(self.frames[-1]["sim_time_s"], 3) if self.frames else 0.0
            ),
        }

    def event_summary(self) -> List[dict]:
        return [
            {
                "at_ns": e.get("at_ns", 0),
                "category": e.get("category", ""),
                "message": e.get("message", ""),
            }
            for e in self.events
        ]

    def success(self) -> bool:
        return bool(self.result and self.result.get("success"))


def _mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)
