"""
TRUSTIA Güvenlik (Sistem 5) — Güvenlik kalkanı (Shield).

Acil durma anahtarı, bağlantı kaybı davranışı, komut doğrulama,
denetim kaydı ve mesaj kimlik doğrulamasını tek kalkan altında
toplar. Tüm güvenlik olayları denetim kaydına düşer.

PLAN 3.6: bağlantı kaybında güvenli durma, komut doğrulama,
yetkilendirme + şifreleme, denetim kaydı, acil durma anahtarı.
"""

from __future__ import annotations

from typing import Optional, Tuple

from security.audit import AuditLog
from security.crypto import SecureMessage
from security.estop import EmergencyStop, EstopEvent, EstopListener, EstopState
from security.linkloss import LinkLossDecision, LinkLossManager, LinkState
from security.validate import CommandGuard, ValidationResult


class Shield:
    """Güvenlik katmanının tek giriş noktası."""

    def __init__(
        self,
        audit_directory: str,
        link_key: bytes = b"",
        lost_after_s: float = 2.0,
        safe_stop_s: float = 1.0,
        wait_before_return_s: float = 5.0,
        max_speed_mps: float = 2.5,
    ) -> None:
        self.audit = AuditLog(audit_directory)
        self.estop = EmergencyStop()
        self.linkloss = LinkLossManager(
            lost_after_s=lost_after_s,
            safe_stop_s=safe_stop_s,
            wait_before_return_s=wait_before_return_s,
        )
        self.guard = CommandGuard(max_speed_mps=max_speed_mps)
        self.crypto = SecureMessage(link_key) if link_key else None
        self._listeners = []
        self.estop.attach(_AuditBridge(self.audit))

    def close(self) -> None:
        self.audit.close()

    # ---- acil durum ----

    def emergency_stop(self, source: str, message: str = "") -> None:
        self.estop.stop(source, message=message)
        self.audit.record("shield", "emergency_stop", source, message)

    def emergency_clear(self, source: str, message: str = "") -> None:
        self.estop.clear(source, message=message)
        self.audit.record("shield", "emergency_clear", source, message)

    def vehicle_enabled(self) -> bool:
        return self.estop.vehicle_enabled()

    # ---- bağlantı kaybı ----

    def link_frame(self, time_s: float) -> None:
        self.linkloss.on_frame(time_s)

    def evaluate_link(self, now_s: float) -> LinkLossDecision:
        decision = self.linkloss.evaluate(now_s)
        if decision.action == "RETURN_HOME":
            self.audit.record("shield", "return_home", decision.detail)
        return decision

    # ---- komut doğrulama ----

    def validate_command(self, user: str, action: str,
                         speed_mps: Optional[float] = None,
                         heading_deg: Optional[float] = None,
                         target_m: Optional[Tuple[float, float]] = None,
                         clearance_m: Optional[float] = None,
                         detail: str = "") -> ValidationResult:
        """Komutu doğrular; tüm komutlar denetim kaydına düşer."""
        result = self.guard.validate_speed_command(
            speed_mps or 0.0, clearance_m, emergency=not self.vehicle_enabled()
        )
        if result.valid and heading_deg is not None:
            result = self.guard.validate_heading(heading_deg)
        if result.valid and target_m is not None:
            result = self.guard.validate_target(*target_m)
        if result.valid:
            self.audit.record(user, f"accept_{action}", detail, "onaylandı")
        else:
            self.audit.record(user, f"reject_{action}", detail, result.reason)
        return result

    # ---- denetim ----

    def audit_query(self, user: Optional[str] = None,
                    action: Optional[str] = None, limit: int = 100):
        return self.audit.query(user, action, limit)

    def audit_count(self) -> int:
        return self.audit.count()

    # ---- mesaj doğrulama ----

    def sign_message(self, payload: dict, at_s: Optional[float] = None):
        if self.crypto is None:
            raise RuntimeError("kripto anahtarı tanımlı değil")
        return self.crypto.sign_payload(payload, at_s)

    def verify_message(self, envelope: dict, now_s: Optional[float] = None):
        if self.crypto is None:
            raise RuntimeError("kripto anahtarı tanımlı değil")
        return self.crypto.verify(envelope, now_s)


class _AuditBridge(EstopListener):
    """Acil durma olaylarını denetim kaydına köprüler."""

    def __init__(self, audit: AuditLog) -> None:
        self._audit = audit

    def on_estop(self, event: EstopEvent) -> None:
        self._audit.record(
            "estop", event.action, event.source, event.message
        )
