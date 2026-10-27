"""
TRUSTIA UN/ECE R156 Yazılım Güncelleme Yönetim Sistemi (SUMS), RXSWIN Sicili ve Atomik Geri Alma Motoru
"""

from __future__ import annotations

import hashlib
import hmac
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SoftwareUpdatePackage:
    version_tag: str
    rxswin_code: str
    payload_sha256: str
    signature_hex: str


@dataclass(frozen=True)
class SumsUpdateResult:
    success: bool
    active_version: str
    active_rxswin: str
    status: str
    detail: str


class UnR156SumsManager:
    """UN/ECE R156 Yazılım Güncelleme Yönetim Sistemi (SUMS) ve RXSWIN Sicil Yöneticisi."""

    def __init__(
        self,
        signing_secret: bytes = b"TRUSTIA-UN-R156-SUMS-KEY-2026",
        initial_version: str = "v4.2.0-verified",
        initial_rxswin: str = "RXSWIN-R157-TR-2026-001",
    ) -> None:
        self._secret = signing_secret
        self.active_version = initial_version
        self.active_rxswin = initial_rxswin
        self.audit_trail: List[SumsUpdateResult] = []

    def sign_package(self, version_tag: str, rxswin_code: str, payload_bytes: bytes) -> SoftwareUpdatePackage:
        digest = hashlib.sha256(payload_bytes).hexdigest()
        msg = f"{version_tag}|{rxswin_code}|{digest}".encode("utf-8")
        sig = hmac.new(self._secret, msg, hashlib.sha256).hexdigest()
        return SoftwareUpdatePackage(version_tag, rxswin_code, digest, sig)

    def apply_update(
        self,
        pkg: SoftwareUpdatePackage,
        vehicle_speed_mps: float,
        park_brake_engaged: bool,
        post_update_self_check_ok: bool = True,
    ) -> SumsUpdateResult:
        if abs(vehicle_speed_mps) > 0.01 or not park_brake_engaged:
            res = SumsUpdateResult(False, self.active_version, self.active_rxswin, "REJECTED_VEHICLE_MOVING", "Araç hareket halinde.")
            self.audit_trail.append(res)
            return res
        msg = f"{pkg.version_tag}|{pkg.rxswin_code}|{pkg.payload_sha256}".encode("utf-8")
        expected_sig = hmac.new(self._secret, msg, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_sig, pkg.signature_hex):
            res = SumsUpdateResult(False, self.active_version, self.active_rxswin, "REJECTED_BAD_SIGNATURE", "Geçersiz imza.")
            self.audit_trail.append(res)
            return res
        if not post_update_self_check_ok:
            res = SumsUpdateResult(False, self.active_version, self.active_rxswin, "ROLLED_BACK_SAFE", "Atomik geri alma uygulandı.")
            self.audit_trail.append(res)
            return res
        self.active_version = pkg.version_tag
        self.active_rxswin = pkg.rxswin_code
        res = SumsUpdateResult(True, self.active_version, self.active_rxswin, "APPLIED_VERIFIED", "Güncelleme doğrulandı.")
        self.audit_trail.append(res)
        return res
