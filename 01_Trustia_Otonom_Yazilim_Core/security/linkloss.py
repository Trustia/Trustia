"""
TRUSTIA Güvenlik (Sistem 5) — Bağlantı kaybı yönetimi.

PLAN 3.6: "Bağlantı kaybında güvenli durma
(link loss → dur → bekle → geri dön)".

Komuta merkezinden düzenli telemetri beklenir; beklenen dönem aşılırsa
araç önce güvenli durma, ardından bekleme ve sonunda ana üsse dönme
davranışını uygular. Bağlantı yeniden kurulunca sürüş serbest kalır.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional


class LinkState(IntEnum):
    NOMINAL = 0
    LOST = 1
    STOPPING = 2
    STOPPED = 3
    RETURNING = 4


@dataclass
class LinkLossDecision:
    """Değerlendirme çıktısı — araca uygulanacak güvenlik talimatı."""

    state: LinkState
    action: str
    detail: str = ""

    @property
    def is_safe_stop(self) -> bool:
        return self.action.lower() in ("stop", "hold")

    @property
    def is_return_home(self) -> bool:
        return self.action == "RETURN_HOME"


class LinkLossManager:
    """Telemetri aralığına göre güvenli durma davranışını yönetir.

    Parametreler (saniye):
      * lost_after_s     : çerçeve beklemesinden sonra bağlantı kopmuş sayılır
      * safe_stop_s      : durmanın tamamlanacağı süre
      * wait_before_return_s: durduktan sonra bekleme; süre dolunca geri dön
    """

    def __init__(
        self,
        lost_after_s: float = 2.0,
        safe_stop_s: float = 1.0,
        wait_before_return_s: float = 5.0,
    ) -> None:
        if lost_after_s <= 0 or safe_stop_s < 0 or wait_before_return_s < 0:
            raise ValueError("geçersiz bağlantı kaybı parametresi")
        self._lost_after_s = lost_after_s
        self._safe_stop_s = safe_stop_s
        self._wait_before_return_s = wait_before_return_s
        self._last_seen_s: Optional[float] = None
        self._state: LinkState = LinkState.NOMINAL
        self._lost_at_s: Optional[float] = None
        self._return_events = False

    @property
    def state(self) -> LinkState:
        return self._state

    def on_frame(self, time_s: float) -> None:
        """Telemetri çerçevesi geldi — bağlantı canlı."""
        self._last_seen_s = time_s
        if self._state != LinkState.NOMINAL:
            self._state = LinkState.NOMINAL
            self._return_events = False

    def gap_seconds(self, now_s: float) -> Optional[float]:
        if self._last_seen_s is None:
            return None
        return max(0.0, now_s - self._last_seen_s)

    def evaluate(self, now_s: float) -> LinkLossDecision:
        """Geçerli anda güvenlik eylemini üretir."""
        gap = self.gap_seconds(now_s)
        if gap is None:
            return LinkLossDecision(self._state, "STANDBY")
        if gap < self._lost_after_s:
            if self._state in (LinkState.STOPPING, LinkState.STOPPED):
                self._state = LinkState.NOMINAL
            return LinkLossDecision(self._state, "")

        if self._state == LinkState.NOMINAL:
            self._state = LinkState.LOST
            self._lost_at_s = now_s
            return LinkLossDecision(self._state, "")

        lapse_s = now_s - (self._lost_at_s or now_s)
        if self._state == LinkState.LOST:
            if lapse_s >= self._safe_stop_s:
                self._state = LinkState.STOPPED
                return LinkLossDecision(self._state, "stop", "bağlantı yok — güvenli durma")
            return LinkLossDecision(self._state, "stop", "bağlantı yok — duruluyor")
        if self._state == LinkState.STOPPED:
            wait_elapsed = now_s - self._lost_at_s - self._safe_stop_s
            if wait_elapsed >= self._wait_before_return_s:
                self._state = LinkState.RETURNING
                self._return_events = True
                return LinkLossDecision(self._state, "RETURN_HOME",
                                        "bekleme doldu — ana üsse dön")
            return LinkLossDecision(self._state, "stop",
                                    f"kalan bekleme {wait_elapsed:.1f} sn")
        if self._state == LinkState.RETURNING:
            return LinkLossDecision(self._state, "RETURN_HOME",
                                    "bağlantı yok — geri dönüş sürer")
        return LinkLossDecision(self._state, "STANDBY")

    def return_requested(self) -> bool:
        """Geri dönüş komutunun bir kez üretilip henüz kullanılmadığı."""
        was = self._return_events
        self._return_events = False
        return was