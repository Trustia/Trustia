"""
TRUSTIA Güvenlik (Sistem 5) — Acil durma anahtarı protokolü.

PLAN 3.6: "Acil durma anahtarı protokolü (fiziksel ve yazılımsal)".
Araç iki kaynaktan da acil durdurulabilir; durduktan sonra yeniden
çalışmak için açık kurtarma (clear) gerekir. Güvenlik zinciri
normalde kapalı (fail-safe) mantığıyla çalışır: sürüş yalnızca
zincir sağlamken serbesttir.
"""

from __future__ import annotations

import time as _time
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional


class EstopState(IntEnum):
    NORMAL = 0
    STOPPED = 1
    RECOVERY_REQUIRED = 2
    HARDWARE_FAULT = 3


@dataclass
class EstopEvent:
    """Acil durma olayı — denetim kaydına akar."""

    at_ns: int
    source: str
    action: str
    message: str = ""
    latched: bool = False


class EstopListener:
    """Acil durma olaylarını dinler (güvenlik hattına bağlanır)."""

    def on_estop(self, event: EstopEvent) -> None:
        pass


class EmergencyStop:
    """Acil durma anahtarı protokolü.

    Fiziksel (buton/sinyal) ve yazılımsal (operatör komutu) kaynaklar
    eşit ağırlıktadır. STOPPED durumundan yalnızca `clear()` ile
    çıkılır; durum değişimleri olay listesine ve dinleyicilere düşer.
    """

    def __init__(self) -> None:
        self._state: EstopState = EstopState.NORMAL
        self._stopped_at_ns: int = 0
        self._events: List[EstopEvent] = []
        self._listeners: List[EstopListener] = []

    def attach(self, listener: EstopListener) -> None:
        self._listeners.append(listener)

    @property
    def state(self) -> EstopState:
        return self._state

    @property
    def stopped(self) -> bool:
        return self._state == EstopState.STOPPED

    def events(self) -> List[EstopEvent]:
        return list(self._events)

    def stop(self, source: str, at_ns: Optional[int] = None,
             message: str = "") -> None:
        """Aracı güvenli duruma getirir (sürüş derhal kesilir)."""
        at_ns = at_ns or self._now()
        self._stopped_at_ns = at_ns
        if self._state == EstopState.STOPPED:
            return
        self._state = EstopState.STOPPED
        self._log(source, "stop", message, at_ns)

    def clear(self, source: str, at_ns: Optional[int] = None,
              message: str = "") -> None:
        """Açık kurtarma: yetkili operatör emniyet kontrollerini geçtiyse
        sürüşü yeniden serbest bırakır."""
        at_ns = at_ns or self._now()
        if self._state == EstopState.HARDWARE_FAULT:
            self._log(
                source, "clear",
                "donanım arızası giderilmeden açılamaz", at_ns,
            )
            return
        self._state = EstopState.NORMAL
        self._log(source, "clear", message, at_ns)

    def hardware_fault(self, source: str, at_ns: Optional[int] = None) -> None:
        at_ns = at_ns or self._now()
        self._state = EstopState.HARDWARE_FAULT
        self._log(source, "hardware_fault", "acil durum zinciri arızalı", at_ns)

    def vehicle_enabled(self) -> bool:
        """Sürüş serbest mi — emniyet zinciri normalde kapalı (fail-safe)."""
        return self._state == EstopState.NORMAL

    def _log(self, source: str, action: str, message: str, at_ns: int) -> None:
        event = EstopEvent(
            at_ns=at_ns,
            source=source,
            action=action,
            message=message,
            latched=self.stopped,
        )
        self._events.append(event)
        for listener in self._listeners:
            try:
                listener.on_estop(event)
            except Exception:
                pass

    @staticmethod
    def _now() -> int:
        return _time.time_ns()