"""
TRUSTIA Otonomi Platformu — Ticari Lisanslama & Dijital Doğrulama Motoru (SDK v2.4).
Milli Seviye-4 Robotaksi Kurumsal Lisans Yöneticisi.

Fikri Mülkiyet: Murat Furkan Bayram (%100 Hak Sahibi)
Tesciller: AB PIC #861711529 • EIT Urban Mobility #CUS15554
"""

from __future__ import annotations

import os
import json
import hmac
import hashlib
import uuid
from datetime import datetime, date
from typing import Dict, Any, Tuple, Optional


_TRUSTIA_ROOT_SIGNING_SALT = b"TRUSTIA_L4_ROBOTAXI_SDK_MURAT_FURKAN_BAYRAM_2026_SECRET_KEY"


class LicenseManager:
    """
    Trustia Seviye-4 Robotaksi Kurumsal Lisans Yöneticisi.
    Kriptografik HMAC-SHA256 imza doğrulama, donanım kilidi ve yetki denetimi.
    """

    DEFAULT_LICENSE_FILENAME = "trustia_robotaxi.lic"

    @classmethod
    def get_hardware_fingerprint(cls) -> str:
        """
        Hedef araç veya ECU'nun benzersiz donanım parmak izini üretir
        (MAC Adresi + Bilgisayar Kimliği).
        """
        node_id = uuid.getnode()
        host = os.environ.get("COMPUTERNAME", os.environ.get("HOSTNAME", "TRUSTIA_L4_NODE"))
        raw = f"{node_id}_{host}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16].upper()

    @classmethod
    def _compute_signature(cls, payload: Dict[str, Any]) -> str:
        """Lisans verisini HMAC-SHA256 ile imzalar."""
        signable_keys = [
            "client_name", "license_id", "tier", "issue_date",
            "expiry_date", "max_vehicles", "hardware_lock", "features"
        ]
        canonical_str = "|".join(f"{k}:{payload.get(k)}" for k in signable_keys)
        return hmac.new(_TRUSTIA_ROOT_SIGNING_SALT, canonical_str.encode("utf-8"), hashlib.sha256).hexdigest()

    @classmethod
    def create_license(
        cls,
        client_name: str,
        expiry_date: str = "2027-12-31",
        max_vehicles: str = "50",
        hardware_lock: str = "ANY",
        tier: str = "L4_ROBOTAXI_COMMERCIAL_FLEET",
        features: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Tripy Mobility veya kurumsal müşteriler için resmi dijital ticari lisans üretir.
        """
        if features is None:
            features = [
                "3D_LIDAR_SLAM_NDT",
                "HYBRID_A_STAR_ROBOTAXI",
                "MAXUS_MIFA7_CAN_FD",
                "CALMCAR_SAFETY_ARBITER",
                "ASIL_D_MINIMAL_RISK_MANEUVER",
                "EDGE_SEALING_KVKK_FIREWALL",
                "ROBOTAXI_TELEMETRY_API",
                "COCKPIT_DIAGNOSTIC_GUI"
            ]

        license_id = f"TRU-RTX-{date.today().year}-{uuid.uuid4().hex[:8].upper()}"
        issue_date = date.today().isoformat()

        payload = {
            "issuer": "Trustia AI Technologies (Murat Furkan Bayram)",
            "client_name": client_name.strip(),
            "license_id": license_id,
            "tier": tier,
            "issue_date": issue_date,
            "expiry_date": expiry_date.strip().upper(),
            "max_vehicles": str(max_vehicles),
            "hardware_lock": hardware_lock.strip().upper(),
            "features": features,
            "legal_basis": "5846 Sayılı FSEK & Uluslararası Bern Sözleşmesi Korumalı Eser",
            "registrations": {
                "eu_pic": "861711529",
                "eit_mobility": "CUS15554"
            }
        }

        signature = cls._compute_signature(payload)
        payload["digital_signature"] = signature
        return payload

    @classmethod
    def verify_license(cls, license_data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Lisans anahtarının geçerliliğini ve kurcalanıp kurcalanmadığını doğrular.
        """
        required_keys = ["client_name", "license_id", "tier", "issue_date", "expiry_date", "digital_signature"]
        for rk in required_keys:
            if rk not in license_data:
                return False, f"Eksik lisans parametresi: {rk}"

        # 1. Kriptografik imza doğrulaması
        expected_sig = cls._compute_signature(license_data)
        given_sig = license_data.get("digital_signature", "")
        if not hmac.compare_digest(expected_sig, given_sig):
            return False, "Kriptografik lisans imzası geçersiz veya dosya kurcalanmış!"

        # 2. Donanım kilidi doğrulaması
        hw_lock = license_data.get("hardware_lock", "ANY")
        if hw_lock != "ANY":
            current_hw = cls.get_hardware_fingerprint()
            if hw_lock != current_hw:
                return False, f"Donanım parmak izi uyuşmazlığı (Kayıtlı: {hw_lock}, Algılanan: {current_hw})"

        # 3. Son kullanma tarihi kontrolü
        exp_str = license_data.get("expiry_date", "")
        if exp_str != "LIFETIME":
            try:
                exp_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
                if date.today() > exp_date:
                    return False, f"Lisans süresi dolmuş ({exp_str})"
            except ValueError:
                return False, f"Geçersiz tarih formatı: {exp_str}"

        return True, "Lisans geçerli ve dijital olarak doğrulandı (ASIL-D Otonomi Aktif)."

    @classmethod
    def save_license(cls, license_data: Dict[str, Any], filepath: str = DEFAULT_LICENSE_FILENAME) -> None:
        """Lisans verisini JSON dosyası olarak diske yazar."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(license_data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load_license(cls, filepath: str = DEFAULT_LICENSE_FILENAME) -> Dict[str, Any]:
        """Diskteki lisans dosyasını okur."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Lisans dosyası bulunamadı: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def get_system_status(cls, license_path: Optional[str] = None) -> Dict[str, Any]:
        """Sistemin anlık lisans ve otonomi çalışma modunu döner."""
        path = license_path or cls.DEFAULT_LICENSE_FILENAME
        if os.path.exists(path):
            try:
                lic = cls.load_license(path)
                valid, msg = cls.verify_license(lic)
                if valid:
                    return {
                        "mode": "COMMERCIAL_PRODUCTION",
                        "client_name": lic.get("client_name"),
                        "license_id": lic.get("license_id"),
                        "tier": lic.get("tier"),
                        "expiry": lic.get("expiry_date"),
                        "vehicles": lic.get("max_vehicles"),
                        "features": lic.get("features", []),
                        "message": msg
                    }
            except Exception as e:
                pass

        # Lisans dosyası yoksa PoC / Geliştirici Modunda çalışır
        return {
            "mode": "EVALUATION_POC_MODE",
            "client_name": "Tripy Mobility (PoC Evaluation)",
            "license_id": "TRU-EVAL-POC-2026",
            "tier": "EVALUATION_60_DAYS",
            "expiry": "2026-12-31",
            "vehicles": "1 (SAIC Maxus MIFA 7 Testbed)",
            "features": [
                "3D_LIDAR_SLAM_NDT",
                "HYBRID_A_STAR_ROBOTAXI",
                "MAXUS_MIFA7_CAN_FD",
                "CALMCAR_SAFETY_ARBITER",
                "ASIL_D_MINIMAL_RISK_MANEUVER",
                "COCKPIT_DIAGNOSTIC_GUI"
            ],
            "message": "PoC / Doğrulama Modu Aktif (Tam Güvenlikli Çalışma)"
        }
