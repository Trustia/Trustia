"""
TRUSTIA API Katmanı — Görev komut arayüzü ve araç durumu.

Bu katman, üst seviye kullanıcı/düğüm komutlarını (görev başlat,
görev durdur, acil durma, rota yükle) yapılandırılmış komut
nesnelerine çevirir ve sonuçları durum nesneleriyle raporlar.

Hedef arayüzler:
  * Yer kontrol istasyonu (GCS) bağlantısı
  * JAUS protokol uyumluluğu (komut eşlemesi)
  * Otonom görev yönetimi (tezgah / görev / geri dön)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional, Tuple

from core.errors import TrustiaError
from core.transforms import EnuPoint, GeoPoint


class VehicleState(IntEnum):
    STANDBY = 0
    INITIALIZING = 1
    READY = 2
    NAVIGATING = 3
    MISSION_COMPLETE = 4
    FAULT = 5
    EMERGENCY_STOP = 6
    PAUSED = 7


class MissionPhase(IntEnum):
    IDLE = 0
    PENDING = 1
    ACTIVE = 2
    PAUSED = 3
    COMPLETE = 4
    ABORTED = 5


class CommandType(IntEnum):
    STANDUP = 0
    SHUTDOWN = 1
    START_MISSION = 2
    PAUSE_MISSION = 3
    RESUME_MISSION = 4
    STOP_MISSION = 5
    ABORT = 6
    EMERGENCY_STOP = 7
    EMERGENCY_CLEAR = 8
    SET_SPEED = 9
    SET_HEADING = 10
    LOAD_WAYPOINTS = 11
    RETURN_HOME = 12


@dataclass(frozen=True)
class Waypoint:
    """Görevde izlenecek tek rota noktası."""

    point: EnuPoint
    speed_mps: float = 1.0
    radius_m: float = 1.5
    pause_s: float = 0.0
    metadata: str = ""

    @classmethod
    def from_geo(cls, geo: GeoPoint, origin_frame, **kwargs) -> "Waypoint":
        """Küresel koordinatı yerel çerçeveye çevirerek rota noktası üretir."""
        return cls(point=origin_frame.to_local(geo), **kwargs)


@dataclass
class Command:
    """Sisteme verilen yapılandırılmış komut."""

    command_id: int
    command_type: CommandType
    issued_at_ns: int = 0
    params: dict = field(default_factory=dict)
    source: str = "local"

    def param(self, key: str, default=None):
        return self.params.get(key, default)


@dataclass
class CommandResult:
    """Komut yürütmesinin sonucu."""

    command_id: int
    success: bool
    message: str = ""
    executed_at_ns: int = 0


@dataclass
class VehicleStatus:
    """Aracın güncel operasyonel durumu — GCS'e yayınlanır."""

    state: VehicleState = VehicleState.STANDBY
    phase: MissionPhase = MissionPhase.IDLE
    position_m: Optional[EnuPoint] = None
    heading_deg: float = 0.0
    speed_mps: float = 0.0
    battery_percent: float = 100.0
    active_mission_id: Optional[int] = None
    waypoint_index: int = 0
    waypoint_count: int = 0
    last_error: str = ""
    timestamp_ns: int = 0

    def is_operational(self) -> bool:
        return self.state in (
            VehicleState.READY,
            VehicleState.NAVIGATING,
            VehicleState.MISSION_COMPLETE,
        )

    def to_dict(self) -> dict:
        pos = self.position_m
        return {
            "state": self.state.name,
            "phase": self.phase.name,
            "position": (
                {"east_m": pos.east_m, "north_m": pos.north_m, "up_m": pos.up_m}
                if pos is not None
                else None
            ),
            "heading_deg": self.heading_deg,
            "speed_mps": self.speed_mps,
            "battery_percent": self.battery_percent,
            "active_mission_id": self.active_mission_id,
            "waypoint_index": self.waypoint_index,
            "waypoint_count": self.waypoint_count,
            "last_error": self.last_error,
            "timestamp_ns": self.timestamp_ns,
        }


@dataclass
class TelemetryFrame:
    """Simülasyon/araç telemetri çerçevesi — komuta merkezine akar.

    Her kontrol adımında üretilir; kayıt (Sistem 4), canlı harita ve
    alarm motoru (Sistem 3) bu çerçeveyi tüketir.
    """

    vehicle_id: str
    sim_time_s: float
    step: int
    position_m: Tuple[float, float]
    heading_deg: float
    speed_mps: float
    target_m: Tuple[float, float]
    clearance_m: float
    obstacle_count: int
    waypoint_index: int
    waypoint_count: int
    mission_phase: str
    gps_available: bool
    position_error_m: float
    battery_percent: float
    link_quality: float
    engine_ok: bool

    def to_dict(self) -> dict:
        return {
            "vehicle_id": self.vehicle_id,
            "sim_time_s": round(self.sim_time_s, 3),
            "step": self.step,
            "position_m": (round(self.position_m[0], 3), round(self.position_m[1], 3)),
            "heading_deg": round(self.heading_deg, 2),
            "speed_mps": round(self.speed_mps, 3),
            "target_m": (round(self.target_m[0], 3), round(self.target_m[1], 3)),
            "clearance_m": (
                round(self.clearance_m, 3)
                if math.isfinite(self.clearance_m)
                else None
            ),
            "obstacle_count": self.obstacle_count,
            "waypoint_index": self.waypoint_index,
            "waypoint_count": self.waypoint_count,
            "mission_phase": self.mission_phase,
            "gps_available": self.gps_available,
            "position_error_m": round(self.position_error_m, 3),
            "battery_percent": round(self.battery_percent, 2),
            "link_quality": round(self.link_quality, 3),
            "engine_ok": self.engine_ok,
        }


class CommandExecutor:
    """Komutları doğrular ve yürütmeyi komut işleyicisine iletir.

    handler arayüzü::

        def execute(self, command: Command) -> CommandResult: ...
    """

    def __init__(self, handler) -> None:
        self._handler = handler
        self._next_id = 1

    def _issue(self, command_type: CommandType, params: dict,
               source: str = "local") -> Command:
        command = Command(
            command_id=self._next_id,
            command_type=command_type,
            params=params,
            source=source,
        )
        self._next_id += 1
        return command

    def issue_and_execute(self, command_type: CommandType,
                          params: Optional[dict] = None,
                          source: str = "local") -> CommandResult:
        command = self._issue(command_type, params or {}, source)
        return self._handler.execute(command)

    def standup(self) -> CommandResult:
        return self.issue_and_execute(CommandType.STANDUP)

    def shutdown(self) -> CommandResult:
        return self.issue_and_execute(CommandType.SHUTDOWN)

    def start_mission(self, mission_id: int) -> CommandResult:
        return self.issue_and_execute(
            CommandType.START_MISSION, {"mission_id": mission_id}
        )

    def pause_mission(self) -> CommandResult:
        return self.issue_and_execute(CommandType.PAUSE_MISSION)

    def resume_mission(self) -> CommandResult:
        return self.issue_and_execute(CommandType.RESUME_MISSION)

    def stop_mission(self) -> CommandResult:
        return self.issue_and_execute(CommandType.STOP_MISSION)

    def emergency_stop(self) -> CommandResult:
        return self.issue_and_execute(CommandType.EMERGENCY_STOP)

    def emergency_clear(self) -> CommandResult:
        return self.issue_and_execute(CommandType.EMERGENCY_CLEAR)

    def set_speed(self, speed_mps: float) -> CommandResult:
        if speed_mps < 0.0:
            raise TrustiaError(f"hız negatif olamaz: {speed_mps}")
        return self.issue_and_execute(
            CommandType.SET_SPEED, {"speed_mps": speed_mps}
        )

    def set_heading(self, heading_deg: float) -> CommandResult:
        if not 0.0 <= heading_deg <= 360.0:
            raise TrustiaError(f"baş açısı aralık dışı: {heading_deg}")
        return self.issue_and_execute(
            CommandType.SET_HEADING, {"heading_deg": heading_deg}
        )

    def load_waypoints(self, waypoints: List[Waypoint]) -> CommandResult:
        if not waypoints:
            raise TrustiaError("rota boş olamaz")
        return self.issue_and_execute(
            CommandType.LOAD_WAYPOINTS, {"waypoints": waypoints}
        )

    def return_home(self) -> CommandResult:
        return self.issue_and_execute(CommandType.RETURN_HOME)
