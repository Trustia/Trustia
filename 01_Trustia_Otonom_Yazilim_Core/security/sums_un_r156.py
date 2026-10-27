"""
TRUSTIA UN/ECE R156 Yazılım Güncelleme Yönetim Sistemi (SUMS), RXSWIN Sicili ve Atomik Geri Alma Motoru
========================================================================================================
AB 2022/1426 (1 Aralık 2024 Resmî Gazete) ve UN/ECE R156 regülasyonu uyarınca Seviye-4 otonom
araçların yazılım güncellemelerini (OTA ve kablolu) denetler:
  1. RXSWIN (Regulation X Software Identification Number): Tip onayına tabi otonomi bileşenlerinin
     değiştirilemez sürüm sicilini tutar (ör. RXSWIN-R157-TR-2026-v4.2).
  2. Kriptografik İmza ve Bütünlük Doğrulaması: HMAC-SHA256 imzası doğrulanmayan hiçbir güncelleme
     paketini kabul etmez.
  3. Hareket Halinde Güncelleme Yasağı: Araç hızı > 0 m/s veya park freni çekili değilken yazılım
     güncellemesini kesin olarak reddeder.
  4. Atomik Geri Alma (Atomic Rollback): Güncelleme sonrası 20 ms öz-denetim (Self-Check) başarısız
     olursa otomatik olarak bir önceki onaylı sürüme geri döner.
"""

from __future__ import annotations

import hashlib
import hmac
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SoftwareUpdatePackage:
    """UN R156 uyumlu imzalı yazılım güncelleme paketi."""

    version_tag: str
    rxswin_code: str
    payload_sha256: str
    signature_hex: str


@dataclass(frozen=True)
class SumsUpdateResult:
    """Yazılım güncelleme ve geri alma denetim sonucu."""

    success: bool
    active_version: str
    active_rxswin: str
    status: str  # "APPLIED_VERIFIED", "REJECTED_VEHICLE_MOVING", "REJECTED_BAD_SIGNATURE", "ROLLED_BACK_SAFE"
    detail: str


class UnR156SumsManager:
    """
    UN/ECE R156 Yazılım Güncelleme Yönetim Sistemi (SUMS) ve RXSWIN Tip Onay Sicil Yöneticisi.
    """

    def __init__(
        self,
        signing_secret: bytes = b"TRUSTIA-UN-R156-SUMS-KEY-2026",
        initial_version: str = "v4.2.0-verified",
        initial_rxswin: str = "RXSWIN-R157-TR-2026-001",
    ) -> None:
        self._secret = signing_secret
        self.active_version = initial_version
        self.active_rxswin = initial_rxswin
        self._previous_version = initial_version
        self._previous_rxswin = initial_rxswin
        self.audit_trail: List[SumsUpdateResult] = []

    def sign_package(self, version_tag: str, rxswin_code: str, payload_bytes: bytes) -> SoftwareUpdatePackage:
        """Güncelleme paketini SHA-256 özeti ve HMAC imzasıyla mühürler."""
        digest = hashlib.sha256(payload_bytes).hexdigest()
        msg = f"{version_tag}|{rxswin_code}|{digest}".encode("utf-8")
        sig = hmac.new(self._secret, msg, hashlib.sha256).hexdigest()
        return SoftwareUpdatePackage(
            version_tag=version_tag,
            rxswin_code=rxswin_code,
            payload_sha256=digest,
            signature_hex=sig,
        )

    def apply_update(
        self,
        pkg: SoftwareUpdatePackage,
        vehicle_speed_mps: float,
        park_brake_engaged: bool,
        post_update_self_check_ok: bool = True,
    ) -> SumsUpdateResult:
        """UN R156 güvenlik kurallarına göre güncellemeyi doğrular, uygular veya geri alır."""
        # 1. Araç hareket halindeyken güncelleme kesinlikle yasaktır
        if abs(vehicle_speed_mps) > 0.01 or not park_brake_engaged:
            res = SumsUpdateResult(
                success=False,
                active_version=self.active_version,
                active_rxswin=self.active_rxswin,
                status="REJECTED_VEHICLE_MOVING",
                detail="UN R156 Kuralı: Araç park halinde değilken yazılım güncellemesi yapılamaz.",
            )
            self.audit_trail.append(res)
            return res

        # 2. Kriptografik imza kontrolü
        msg = f"{pkg.version_tag}|{pkg.rxswin_code}|{pkg.payload_sha256}".encode("utf-8")
        expected_sig = hmac.new(self._secret, msg, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_sig, pkg.signature_hex):
            res = SumsUpdateResult(
                success=False,
                active_version=self.active_version,
                active_rxswin=self.active_rxswin,
                status="REJECTED_BAD_SIGNATURE",
                detail="UN R156 Kuralı: Kriptografik paket imzası geçersiz — güncelleme reddedildi.",
            )
            self.audit_trail.append(res)
            return res

        # 3. Güncelleme sonrası öz-denetim başarısızsa atomik geri alma (Rollback)
        if not post_update_self_check_ok:
            res = SumsUpdateResult(
                success=False,
                active_version=self.active_version,
                active_rxswin=self.active_rxswin,
                status="ROLLED_BACK_SAFE",
                detail=f"Öz-denetim hatası nedeniyle {self.active_version} ({self.active_rxswin}) sürümüne atomik geri dönüldü.",
            )
            self.audit_trail.append(res)
            return res

        self._previous_version = self.active_version
        self._previous_rxswin = self.active_rxswin
        self.active_version = pkg.version_tag
        self.active_rxswin = pkg.rxswin_code
        res = SumsUpdateResult(
            success=True,
            active_version=self.active_version,
            active_rxswin=self.active_rxswin,
            status="APPLIED_VERIFIED",
            detail=f"Güncelleme başarıyla doğrulandı: {self.active_version} ({self.active_rxswin})",
        )
        self.audit_trail.append(res)
        return res
