"""
TRUSTIA Komuta Merkezi (Sistem 3) — Alarm motoru.

Alarm sistemi (PLAN 3.5): çarpışma riski, bağlantı kopması, batarya
kritik. Kural motoru; aynı koşul sürdükçe aynı alarm tekrar üretilmez,
koşul düzelince alarm otomatik temizlenir.
"""

from __future__ import annotations

import itertools
import time
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, List, Optional

from core.api import TelemetryFrame


class AlarmSeverity(IntEnum):
    INFO = 0
    WARNING = 1
    CRITICAL = 2


class AlarmCode(IntEnum):
    LINK_WEAK = 0
    LINK_LOSS = 1
    BATTERY_LOW = 2
    BATTERY_CRITICAL = 3
    COLLISION_RISK = 4
    ENGINE_FAULT = 5
    POSITION_DRIFT = 6


SEVERITY_NAMES = {s: s.name for s in AlarmSeverity}


@dataclass
class Alarm:
    """Tek aktif/geçmiş alarm kaydı."""

    alarm_id: int
    vehicle_id: str
    severity: AlarmSeverity
    code: AlarmCode
    message: str
    created_at_ns: int = 0
    cleared_at_ns: int = 0
    cleared: bool = False

    def to_dict(self) -> dict:
        return {
            "alarm_id": self.alarm_id,
            "vehicle_id": self.vehicle_id,
            "severity": self.severity.name,
            "code": self.code.name,
            "message": self.message,
            "cleared": self.cleared,
        }


@dataclass
class AlarmRule:
    """Tek alarm kuralı — çerçeveye göre tetikleme değerlendirmesi."""

    code: AlarmCode
    severity: AlarmSeverity
    message: str

    def triggers(self, frame: TelemetryFrame) -> bool:
        if self.code == AlarmCode.LINK_WEAK:
            return frame.link_quality < 0.5
        if self.code == AlarmCode.LINK_LOSS:
            return frame.link_quality < 0.35
        if self.code == AlarmCode.BATTERY_LOW:
            return frame.battery_percent < 20.0
        if self.code == AlarmCode.BATTERY_CRITICAL:
            return frame.battery_percent < 10.0
        if self.code == AlarmCode.COLLISION_RISK:
            return (
                frame.clearance_m is not None and frame.clearance_m < 0.6
            )
        if self.code == AlarmCode.ENGINE_FAULT:
            return not frame.engine_ok
        if self.code == AlarmCode.POSITION_DRIFT:
            return frame.position_error_m > 3.0
        return False


DEFAULT_RULES: List[AlarmRule] = [
    AlarmRule(AlarmCode.LINK_WEAK, AlarmSeverity.WARNING, "bağlantı zayıf"),
    AlarmRule(AlarmCode.LINK_LOSS, AlarmSeverity.CRITICAL, "bağlantı kopması"),
    AlarmRule(AlarmCode.BATTERY_LOW, AlarmSeverity.WARNING, "batarya düşük"),
    AlarmRule(AlarmCode.BATTERY_CRITICAL, AlarmSeverity.CRITICAL, "batarya kritik"),
    AlarmRule(AlarmCode.COLLISION_RISK, AlarmSeverity.CRITICAL, "çarpışma riski"),
    AlarmRule(AlarmCode.ENGINE_FAULT, AlarmSeverity.CRITICAL, "motor arızası"),
    AlarmRule(AlarmCode.POSITION_DRIFT, AlarmSeverity.WARNING, "konum hatası yüksek"),
]


class AlarmEngine:
    """Çerçeve başına alarm değerlendirmesi ve aktif alarm dizini."""

    def __init__(self, rules: Optional[List[AlarmRule]] = None) -> None:
        self._rules = rules if rules is not None else list(DEFAULT_RULES)
        self._active: Dict[tuple, Alarm] = {}
        self._history: List[Alarm] = []
        self._next_id = itertools.count(1)

    def evaluate(
        self,
        frame: TelemetryFrame,
        now_ns: Optional[int] = None,
    ) -> List[Alarm]:
        """Çerçeveyi tüm kurallara karşı değerlendirir; yeni/çözülen
        alarmları döndürür."""
        now = now_ns if now_ns is not None else time.time_ns()
        produced: List[Alarm] = []
        triggered_codes = set()
        for rule in self._rules:
            if not rule.triggers(frame):
                continue
            triggered_codes.add(rule.code)
            key = (frame.vehicle_id, rule.code)
            if key in self._active:
                continue  # aynı koşul sürüyor — yeniden üretme
            alarm = Alarm(
                alarm_id=next(self._next_id),
                vehicle_id=frame.vehicle_id,
                severity=rule.severity,
                code=rule.code,
                message=rule.message,
                created_at_ns=now,
            )
            self._active[key] = alarm
            self._history.append(alarm)
            produced.append(alarm)
        for key in list(self._active):
            if key[0] == frame.vehicle_id and key[1] not in triggered_codes:
                alarm = self._active.pop(key)
                alarm.cleared = True
                alarm.cleared_at_ns = now
                produced.append(alarm)
        return produced

    def active(self) -> List[Alarm]:
        return sorted(self._active.values(),
                      key=lambda a: a.alarm_id)

    def active_snapshot(self) -> List[dict]:
        return [a.to_dict() for a in self.active()]

    def history(self) -> List[Alarm]:
        return list(self._history)

    def count(self) -> int:
        return len(self._history)

    def total_active(self) -> int:
        return len(self._active)

    def get(self, alarm_id: int) -> Optional[Alarm]:
        for alarm in self._history:
            if alarm.alarm_id == alarm_id:
                return alarm
        return None