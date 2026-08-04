"""
TRUSTIA Komuta Merkezi (Sistem 3) — Görev siparişi ve görev sicili.

Görev atama (PLAN 3.5): harita üzerinde hedef nokta seç → araç
görevlendir. Siparişler onay akışından geçer (PENDING → APPROVED
→ ACTIVE → COMPLETE / ABORTED / FAILED).
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional, Tuple

from core.transforms import EnuPoint
from simulation.scenario import Mission
from simulation.terrain import Terrain, TerrainSpec, Weather


class OrderState(IntEnum):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2
    ACTIVE = 3
    COMPLETE = 4
    FAILED = 5
    ABORTED = 6


@dataclass
class MissionOrder:
    """Komuta merkezinden araç için verilen görev siparişi."""

    order_id: str
    vehicle_id: str
    waypoints: List[EnuPoint] = field(default_factory=list)
    mission_type: str = "kesif"
    time_limit_s: float = 300.0
    forbidden_zones: List[Tuple[EnuPoint, float]] = field(default_factory=list)
    priority: int = 5
    created_at_ns: int = field(default_factory=time.time_ns)
    issued_by: str = "unknown"

    def validate(self) -> None:
        if not self.waypoints:
            raise ValueError(f"sipariş rota noktası içermiyor: {self.order_id}")
        if self.time_limit_s < 1.0:
            raise ValueError(f"süre limiti geçersiz: {self.time_limit_s}")
        if not (0 <= self.priority <= 10):
            raise ValueError(f"öncelik aralık dışı: {self.priority}")

    def waypoint_tuples(self) -> List[Tuple[float, float]]:
        return [(w.east_m, w.north_m) for w in self.waypoints]

    def to_simulation_mission(
        self,
        start: Tuple[float, float],
        start_heading_rad: float = 0.0,
        terrain: Optional[Terrain] = None,
        weather: Optional[Weather] = None,
        arrival_tolerance_m: float = 1.5,
        gps_available: bool = True,
    ) -> Mission:
        """Siparişi simülasyon dünyasının görev tanımına çevirir."""
        spec = None
        if terrain is not None:
            spec = TerrainSpec(
                width_m=terrain.width_m,
                height_m=terrain.height_m,
                seed=terrain.seed,
                obstacle_count=len(terrain.obstacles),
                forbidden_count=len(terrain.forbidden),
            )
        return Mission(
            mission_id=self.order_id,
            mission_type=self.mission_type,
            start=start,
            start_heading_rad=start_heading_rad,
            waypoints=self.waypoint_tuples(),
            arrival_tolerance_m=arrival_tolerance_m,
            time_limit_s=self.time_limit_s,
            gps_available=gps_available,
            terrain=spec,
            weather=weather,
        )


@dataclass
class OrderRecord:
    """Siparişin sicil kaydı — durum makinesi ve zaman damgaları."""

    order: MissionOrder
    state: OrderState = OrderState.PENDING
    approved_at_ns: int = 0
    started_at_ns: int = 0
    finished_at_ns: int = 0
    outcome: str = ""
    history: List[str] = field(default_factory=list)

    def note(self, event: str) -> None:
        self.history.append(f"{time.time_ns()}: {event}")


class MissionRegistry:
    """Görev siparişlerinin onay akışı ve sicil yönetimi."""

    def __init__(self) -> None:
        self._orders: dict = {}
        self._next_id = 1

    def _new_order_id(self) -> str:
        order_id = f"G-{self._next_id:04d}"
        self._next_id += 1
        return order_id

    def submit(self, order: MissionOrder) -> str:
        """Siparişi sicile işler (PENDING) — komuta merkezi onaylar."""
        order.validate()
        order_id = order.order_id or self._new_order_id()
        if order_id in self._orders:
            raise ValueError(f"sipariş zaten var: {order_id}")
        record = OrderRecord(order=order)
        record.note("sipariş alındı")
        self._orders[order_id] = record
        return order_id

    def approve(self, order_id: str) -> None:
        record = self._require(order_id)
        if record.state != OrderState.PENDING:
            raise ValueError(f"sipariş onaylanamaz durumda: {record.state.name}")
        record.state = OrderState.APPROVED
        record.approved_at_ns = time.time_ns()
        record.note("onaylandı")

    def reject(self, order_id: str, reason: str) -> None:
        record = self._require(order_id)
        record.state = OrderState.REJECTED
        record.outcome = reason
        record.note(f"reddedildi: {reason}")

    def start(self, order_id: str) -> None:
        record = self._require(order_id)
        record.state = OrderState.ACTIVE
        record.started_at_ns = time.time_ns()
        record.note("görev başladı")

    def finish(self, order_id: str, success: bool, outcome: str = "") -> None:
        record = self._require(order_id)
        record.state = OrderState.COMPLETE if success else OrderState.FAILED
        record.finished_at_ns = time.time_ns()
        record.outcome = outcome
        record.note(f"bitti: {outcome}")

    def abort(self, order_id: str, reason: str) -> None:
        record = self._require(order_id)
        record.state = OrderState.ABORTED
        record.finished_at_ns = time.time_ns()
        record.outcome = reason
        record.note(f"iptal: {reason}")

    def get(self, order_id: str) -> OrderRecord:
        return self._require(order_id)

    def state(self, order_id: str) -> OrderState:
        return self._require(order_id).state

    def orders_for(self, vehicle_id: str) -> List[OrderRecord]:
        return [r for r in self._orders.values()
                if r.order.vehicle_id == vehicle_id]

    def count(self) -> int:
        return len(self._orders)

    def snapshot(self) -> dict:
        return {
            "total_orders": self.count(),
            "orders": [
                {
                    "order_id": oid,
                    "vehicle_id": r.order.vehicle_id,
                    "state": r.state.name,
                    "mission_type": r.order.mission_type,
                    "waypoints": r.order.waypoint_tuples(),
                    "priority": r.order.priority,
                    "outcome": r.outcome,
                    "issued_by": r.order.issued_by,
                }
                for oid, r in sorted(self._orders.items())
            ],
        }

    def _require(self, order_id: str) -> OrderRecord:
        if order_id not in self._orders:
            raise KeyError(f"bilinmeyen sipariş: {order_id}")
        return self._orders[order_id]
