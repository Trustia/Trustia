"""
TRUSTIA Komuta Merkezi (Sistem 3) — Araç filosu yönetimi.

Çoklu araç (hedef: aynı anda 100+ araç) kaydı, canlı telemetri
tamponu ve filo sağlık özeti. PLAN 3.5:
  * Çoklu araç yönetimi
  * Canlı harita (araç pozisyonları, rotalar, sensör durumu)
  * Telemetri: hız, konum, batarya, motor durumu, bağlantı kalitesi
"""

from __future__ import annotations

import time
from typing import Dict, List, Optional

from core.api import TelemetryFrame, VehicleState


class RegisteredVehicle:
    """Komuta merkezinde kayıtlı tek araç."""

    def __init__(
        self,
        vehicle_id: str,
        name: str = "",
        max_history: int = 3600,
    ) -> None:
        self.vehicle_id = vehicle_id
        self.name = name or vehicle_id
        self.state = VehicleState.STANDBY
        self.last_frame: Optional[TelemetryFrame] = None
        self._history: List[TelemetryFrame] = []
        self._max_history = max(1, max_history)
        self.last_telemetry_ns: int = 0
        self.registered_at_ns: int = time.time_ns()

    def update(self, frame: TelemetryFrame) -> None:
        """Yeni telemetri çerçevesini kaydeder (canlı tampon)."""
        self.last_frame = frame
        self.last_telemetry_ns = time.time_ns()
        self._history.append(frame)
        if len(self._history) > self._max_history:
            del self._history[: len(self._history) - self._max_history]

    @property
    def history(self) -> List[TelemetryFrame]:
        return list(self._history)

    @property
    def position_m(self) -> Optional[tuple]:
        if self.last_frame is None:
            return None
        return self.last_frame.position_m

    @property
    def battery_percent(self) -> float:
        return self.last_frame.battery_percent if self.last_frame else 100.0

    @property
    def link_quality(self) -> float:
        return self.last_frame.link_quality if self.last_frame else 0.0

    @property
    def speed_mps(self) -> float:
        return self.last_frame.speed_mps if self.last_frame else 0.0

    def frame_count(self) -> int:
        return len(self._history)

    def is_online(self, now_ns: int, timeout_s: float = 5.0) -> bool:
        """Bağlantı kopması kontrolü: son çerçeve yaşı eşik altındaysa çevrim içi."""
        if self.last_telemetry_ns == 0:
            return False
        return (now_ns - self.last_telemetry_ns) < timeout_s * 1_000_000_000

    def to_dict(self) -> dict:
        frame = self.last_frame
        return {
            "vehicle_id": self.vehicle_id,
            "name": self.name,
            "state": self.state.name,
            "online": self.last_telemetry_ns != 0,
            "position_m": frame.position_m if frame else None,
            "heading_deg": frame.heading_deg if frame else 0.0,
            "speed_mps": self.speed_mps,
            "battery_percent": round(self.battery_percent, 2),
            "link_quality": round(self.link_quality, 3),
            "engine_ok": frame.engine_ok if frame else True,
            "obstacle_count": frame.obstacle_count if frame else 0,
            "frame_count": self.frame_count(),
        }


class Fleet:
    """Araç filosu: kayıt, arama ve filo düzeyi özetler."""

    def __init__(self, link_timeout_s: float = 5.0) -> None:
        self._vehicles: Dict[str, RegisteredVehicle] = {}
        self._link_timeout_s = link_timeout_s

    def register(self, vehicle_id: str, name: str = "") -> RegisteredVehicle:
        if vehicle_id in self._vehicles:
            raise ValueError(f"araç zaten kayıtlı: {vehicle_id}")
        vehicle = RegisteredVehicle(vehicle_id, name)
        self._vehicles[vehicle_id] = vehicle
        return vehicle

    def unregister(self, vehicle_id: str) -> None:
        if vehicle_id not in self._vehicles:
            raise KeyError(f"kayıtlı araç değil: {vehicle_id}")
        del self._vehicles[vehicle_id]

    def get(self, vehicle_id: str) -> RegisteredVehicle:
        if vehicle_id not in self._vehicles:
            raise KeyError(f"kayıtlı araç değil: {vehicle_id}")
        return self._vehicles[vehicle_id]

    def get_or_register(self, vehicle_id: str, name: str = "") -> RegisteredVehicle:
        try:
            return self.get(vehicle_id)
        except KeyError:
            return self.register(vehicle_id, name)

    def ingest_telemetry(self, frame: TelemetryFrame) -> RegisteredVehicle:
        """Telemetriyi ilgili aracın tamponuna işler; bilinmeyen araç kaydedilir."""
        vehicle = self.get_or_register(frame.vehicle_id)
        vehicle.update(frame)
        return vehicle

    def count(self) -> int:
        return len(self._vehicles)

    def online_count(self, now_ns: Optional[int] = None) -> int:
        now = now_ns if now_ns is not None else time.time_ns()
        return sum(1 for v in self._vehicles.values()
                   if v.is_online(now, self._link_timeout_s))

    def offline_ids(self, now_ns: Optional[int] = None) -> List[str]:
        now = now_ns if now_ns is not None else time.time_ns()
        return [vid for vid, v in self._vehicles.items()
                if not v.is_online(now, self._link_timeout_s)]

    def all(self) -> List[RegisteredVehicle]:
        return list(self._vehicles.values())

    def snapshot(self, now_ns: Optional[int] = None) -> dict:
        """Canlı harita / filo görünümü için özet."""
        now = now_ns if now_ns is not None else time.time_ns()
        return {
            "total_vehicles": self.count(),
            "online_vehicles": self.online_count(now),
            "offline_vehicles": len(self.offline_ids(now)),
            "vehicles": [v.to_dict() for v in self.all()],
        }
