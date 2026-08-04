"""
TRUSTIA Güvenlik (Sistem 5) — Komut doğrulama.

PLAN 3.6: "Komut doğrulama: geçersiz/tehlikeli komut engelleme".
Araca inen her komut fiziksel sınırlar (hız, baş açısı, hedef
dünya içi) ve güvenlik bağlamı (acil durma, bağlantı) açısından
doğrulanır; ihlal yükseltilir, komut araca iletilmez.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class ValidationResult:
    """Komut doğrulama sonucu."""

    valid: bool
    reason: str = ""

    def ok(self) -> bool:
        return self.valid


def _check(ok: bool, reason: str) -> Optional[ValidationResult]:
    if ok:
        return None
    return ValidationResult(False, reason)


class CommandGuard:
    """Araç komutları için güvenlik süzgeci."""

    def __init__(
        self,
        max_speed_mps: float = 2.5,
        min_clearance_m: float = 0.3,
        world_bounds_m: Tuple[float, float] = (40.0, 40.0),
    ) -> None:
        self._max_speed = max_speed_mps
        self._min_clearance = min_clearance_m
        self._world = world_bounds_m

    def validate_speed(self, speed_mps: float) -> ValidationResult:
        checks = [
            _check(speed_mps >= 0.0, f"hız negatif olamaz: {speed_mps}"),
            _check(speed_mps <= self._max_speed,
                   f"hız sınırı aşıldı: {speed_mps} > {self._max_speed}"),
        ]
        return self._first_fail(checks) or ValidationResult(True)

    def validate_heading(self, heading_deg: float) -> ValidationResult:
        checks = [
            _check(0.0 <= heading_deg <= 360.0,
                   f"baş açısı aralık dışı: {heading_deg}"),
        ]
        return self._first_fail(checks) or ValidationResult(True)

    def validate_target(self, x_m: float, y_m: float) -> ValidationResult:
        width, height = self._world
        checks = [
            _check(0.0 <= x_m <= width, f"hedef x dünya dışı: {x_m}"),
            _check(0.0 <= y_m <= height, f"hedef y dünya dışı: {y_m}"),
        ]
        return self._first_fail(checks) or ValidationResult(True)

    def validate_clearance(self, clearance_m: float) -> ValidationResult:
        if clearance_m is None:
            return ValidationResult(True)
        return _check(
            clearance_m > self._min_clearance,
            f"güvenlik payı aşıldı: {clearance_m:.2f} m",
        ) or ValidationResult(True)

    def validate_speed_command(self, speed_mps: float,
                               clearance_m: Optional[float] = None,
                               emergency: bool = False) -> ValidationResult:
        """Sürüş komutu — emniyet zinciri: acil durum varsa hareket yasak."""
        checks = [
            _check(not emergency, "acil durumda sürüş komutu engellendi"),
            self.validate_speed(speed_mps),
            self.validate_clearance(clearance_m),
        ]
        return self._first_fail(checks) or ValidationResult(True)

    def _first_fail(self, checks: List[Optional[ValidationResult]]) -> ValidationResult:
        for result in checks:
            if result is not None and not result.valid:
                return result
        return ValidationResult(True)