"""
TRUSTIA Komuta Merkezi (Sistem 3).

Filo yönetimi + görev atama + alarm motoru + rol tabanlı erişimi
tek merkezde toplar. Uçtan uca akış (PLAN: "görev ver-izle-rapor al"):
  * operator görev siparişi verir (MissionOrder)
  * onaylanan sipariş simülasyon dünyasına gönderilir (dispatch)
  * telemetri merkeze akar (ingest_telemetry) — canlı harita + alarm
  * görev sonucu sicile düşer, rapor alınır (record paketiyle)
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional, Tuple

from command.alarm import Alarm, AlarmEngine
from command.auth import AccessControl, Permission, Role, Session
from command.fleet import Fleet, RegisteredVehicle
from command.mission import (
    MissionOrder,
    MissionRegistry,
    OrderRecord,
    OrderState,
)
from core.api import TelemetryFrame
from core.transforms import EnuPoint
from simulation.terrain import Terrain, Weather


class CommandCenter:
    """Komuta merkezinin tek giriş noktası."""

    def __init__(self, link_timeout_s: float = 5.0) -> None:
        self.fleet = Fleet(link_timeout_s=link_timeout_s)
        self.missions = MissionRegistry()
        self.alarms = AlarmEngine()
        self.access = AccessControl()
        self._default_operator = "operator"

    # ---- Filo yönetimi (MANAGE_FLEET) ----

    def register_vehicle(self, user: str, vehicle_id: str, name: str = "") -> RegisteredVehicle:
        self.access.require(user, Permission.MANAGE_FLEET)
        return self.fleet.register(vehicle_id, name)

    def vehicles(self, user: str) -> dict:
        self.access.require(user, Permission.VIEW)
        return self.fleet.snapshot()

    # ---- Görev atama (ASSIGN_MISSION) ----

    def submit_mission(self, user: str, order: MissionOrder) -> str:
        """Operatör görev siparişi verir; merkez doğrular ve onaylar."""
        self.access.require(user, Permission.ASSIGN_MISSION)
        if not self.fleet.count():
            raise ValueError("filosu boş — önce araç kaydedilmeli")
        try:
            self.fleet.get(order.vehicle_id)
        except KeyError as exc:
            raise ValueError(f"araç kayıtlı değil: {order.vehicle_id}") from exc
        order.issued_by = user
        order_id = self.missions.submit(order)
        self.missions.approve(order_id)
        return order_id

    def order(self, user: str, order_id: str) -> dict:
        self.access.require(user, Permission.VIEW)
        record = self.missions.get(order_id)
        return {
            "order_id": order_id,
            "vehicle_id": record.order.vehicle_id,
            "state": record.state.name,
            "outcome": record.outcome,
            "mission_type": record.order.mission_type,
            "waypoints": record.order.waypoint_tuples(),
            "issued_by": record.order.issued_by,
            "history": record.history,
        }

    def orders(self, user: str) -> dict:
        self.access.require(user, Permission.VIEW)
        return self.missions.snapshot()

    # ---- Telemetri akışı (canlı harita + alarm) ----

    def ingest_telemetry(self, frame: TelemetryFrame) -> tuple:
        """Telemetriyi filoya işler ve alarm kurallarını değerlendirir."""
        vehicle = self.fleet.ingest_telemetry(frame)
        alarms = self.alarms.evaluate(frame)
        return vehicle, alarms

    def live_snapshot(self, user: str) -> dict:
        """Canlı harita görünümü: filo + aktif görevler + aktif alarmlar."""
        self.access.require(user, Permission.VIEW)
        return {
            "fleet": self.fleet.snapshot(),
            "missions": self.missions.snapshot(),
            "alarms": self.alarms.active_snapshot(),
        }

    # ---- Rol yönetimi (MANAGE_ROLES) ----

    def grant_role(self, admin: str, user: str, role: Role) -> None:
        self.access.require(admin, Permission.MANAGE_ROLES)
        self.access.set_role(user, role)

    def users(self, admin: str) -> dict:
        self.access.require(admin, Permission.VIEW)
        return self.access.list_users()

    # ---- Görev sevkiyatı (uçtan uca köprü) ----

    def dispatch(
        self,
        session: Session,
        order_id: str,
        terrain: Terrain,
        weather: Weather,
        runner,
        start: Tuple[float, float],
        start_heading_rad: float = 0.0,
        arrival_tolerance_m: float = 1.5,
        gps_available: bool = True,
        telemetry_callback=None,
    ):
        """Onaylı siparişi simülasyon dünyasına gönderip koşturur.

        Görev koşusu boyunca üretilen telemetri merkeze geri akar
        (canlı harita + alarm); sonuç sicile işlenir.
        """
        session.require(Permission.ASSIGN_MISSION)
        record = self.missions.get(order_id)
        if record.state != OrderState.APPROVED:
            raise ValueError(
                f"sipariş gönderilemez durumda: {record.state.name}"
            )
        mission = record.order.to_simulation_mission(
            start=start,
            start_heading_rad=start_heading_rad,
            terrain=terrain,
            weather=weather,
            arrival_tolerance_m=arrival_tolerance_m,
            gps_available=gps_available,
        )
        self.missions.start(order_id)

        def _callback(frame: TelemetryFrame) -> None:
            # Görev koşucusu çerçeveyi görev kimliğiyle üretir; komuta
            # merkezi telemetriyi siparişin aracına işler.
            frame = replace(frame, vehicle_id=record.order.vehicle_id)
            self.ingest_telemetry(frame)
            if telemetry_callback is not None:
                telemetry_callback(frame)

        metrics = runner.run(
            terrain, weather, mission, telemetry_callback=_callback
        )
        self.missions.finish(
            order_id,
            metrics.success,
            outcome=(
                ""
                if metrics.success
                else f"başarısız: {metrics.failure_reason()}"
            ),
        )
        return metrics
