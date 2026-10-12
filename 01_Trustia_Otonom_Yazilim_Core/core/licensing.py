"""
TRUSTIA Otonomi Platformu — Ticari Lisanslama & Dijital Doğrulama Motoru (v2.4).
Milli Seviye-4 Robotaksi & Taktik Savunma Seyrüsefer Motoru.

Kurucu & Sistem Mimarı: Murat Furkan Bayram (%100 Hisse)
Tesciller: AB PIC #861711529 • EIT #CUS15554 • ASELSAN #0050569 • NATO NCAGE TR26258467723

Bu modül; Trustia Seviye-4 otonom sürüş yazılımının müşterilere ve kurumsal alıcılara
resmi ticari lisansla (Commercial License Key) teslim edilmesini, sahteciliğe karşı
HMAC-SHA256 kriptografik dijital imzayla korunmasını ve doğrulanmasını sağlar.
"""

from __future__ import annotations

import os
import json
import hmac
import hashlib
import uuid
from datetime import datetime, date
from typing import Dict, Any, Tuple, Optional


# Ticari lisans imzalama gizli çekirdeği (Murat Furkan Bayram / Trustia AI IP)
_TRUSTIA_ROOT_SIGNING_SALT = b"TRUSTIA_L4_AUTONOMY_CORE_MURAT_FURKAN_BAYRAM_2026_SECRET_SALT"


class LicenseManager:
    """
    Trustia Seviye-4 Otonomi Motoru Ticari Lisans Yöneticisi.
    Kriptografik HMAC-SHA256 imza doğrulama ve anahtar üretim motoru.
    """

    DEFAULT_LICENSE_FILENAME = "trustia.lic"

    @classmethod
    def _compute_signature(cls, payload: Dict[str, Any]) -> str:
        """Lisans verisini HMAC-SHA256 ile imzalar."""
        # İmzalanacak alanları deterministik sırala
        signable_keys = ["client_name", "license_id", "tier", "issue_date", "expiry_date", "max_vehicles", "features"]
        canonical_str = "|".join(f"{k}:{payload.get(k)}" for k in signable_keys)
        return hmac.new(_TRUSTIA_ROOT_SIGNING_SALT, canonical_str.encode("utf-8"), hashlib.sha256).hexdigest()

    @classmethod
    def create_license(
        cls,
        client_name: str,
        expiry_date: str = "LIFETIME",
        max_vehicles: str = "UNLIMITED",
        tier: str = "L4_ENTERPRISE_FULL_STACK",
        features: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Alıcı şirket veya müşteri için resmi dijital ticari lisans anahtarı üretir.
        """
        if features is None:
            features = [
                "3D_LIDAR_SLAM",
                "HYBRID_A_STAR_PLANNING",
                "CAN_FD_DRIVE_BY_WIRE",
                "ASIL_D_SAFETY_MRM",
                "AI_THREAT_DETECTION",
                "ROBOTAXI_FLEET_DISPATCH",
                "LIVE_3D_WEBGL_COCKPIT"
            ]

        license_id = f"TRU-L4-{date.today().year}-{uuid.uuid4().hex[:8].upper()}"
        issue_date = date.today().isoformat()

        payload = {
            "issuer": "Trustia AI Technologies (Murat Furkan Bayram)",
            "client_name": client_name.strip(),
            "license_id": license_id,
            "tier": tier,
            "issue_date": issue_date,
            "expiry_date": expiry_date.strip().upper(),
            "max_vehicles": max_vehicles,
            "features": features,
            "legal_basis": "5846 Sayılı FSEK & Uluslararası Bern Sözleşmesi Korumalı Eser",
            "registrations": {
                "eu_pic": "861711529",
                "aselsan_supplier": "0050569",
                "nato_ncage": "TR26258467723"
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

        # İmzayı doğrula
        expected_sig = cls._compute_signature(license_data)
        given_sig = license_data.get("digital_signature", "")

        if not hmac.compare_digest(expected_sig, given_sig):
            return False, "GEÇERSİZ LİSANS İMZASI: Lisans dosyası kurcalanmış veya yetkisiz üretilmiş!"

        # Tarih kontrolü
        expiry_str = license_data.get("expiry_date", "LIFETIME")
        if expiry_str != "LIFETIME":
            try:
                exp_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
                if date.today() > exp_date:
                    return False, f"LİSANS SÜRESİ DOLMUŞ ({expiry_str})"
            except ValueError:
                return False, f"Geçersiz lisans son kullanma tarihi formatı: {expiry_str}"

        return True, "LİSANS GEÇERLİ VE ONAYLI"

    @classmethod
    def save_license_file(cls, license_data: Dict[str, Any], file_path: str = DEFAULT_LICENSE_FILENAME) -> str:
        """Lisans verisini dosyaya kaydeder."""
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(license_data, f, indent=2, ensure_ascii=False)
        return os.path.abspath(file_path)

    @classmethod
    def load_license_file(cls, file_path: str = DEFAULT_LICENSE_FILENAME) -> Tuple[Optional[Dict[str, Any]], bool, str]:
        """Lisans dosyasını yükler ve doğrular."""
        if not os.path.exists(file_path):
            return None, False, f"Lisans dosyası bulunamadı ({file_path})"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            is_valid, msg = cls.verify_license(data)
            return data, is_valid, msg
        except Exception as e:
            return None, False, f"Lisans dosyası okuma hatası: {str(e)}"

    @classmethod
    def get_system_status(cls, license_path: str = DEFAULT_LICENSE_FILENAME) -> Dict[str, Any]:
        """
        Sistemin anlık lisans durumunu döndürür.
        Eğer dosya yoksa geriye dönük uyumluluk için Değerlendirme/Demo modu açılır.
        """
        data, is_valid, msg = cls.load_license_file(license_path)
        if data and is_valid:
            return {
                "mode": "COMMERCIAL_ACTIVE",
                "client_name": data.get("client_name"),
                "license_id": data.get("license_id"),
                "tier": data.get("tier"),
                "expiry": data.get("expiry_date"),
                "vehicles": data.get("max_vehicles"),
                "message": msg,
                "is_authorized": True
            }

        return {
            "mode": "EVALUATION_DEMO",
            "client_name": "Laboratuvar & Doğrulama Modu (Dahili)",
            "license_id": "TRU-EVAL-INTERNAL",
            "tier": "FULL_TEST_SUITE_ACTIVE",
            "expiry": "N/A",
            "vehicles": "SIMULATION_ONLY",
            "message": "Ticari lisans anahtarı tanımlanmadı. Sistem Ar-Ge / Test modunda çalışıyor.",
            "is_authorized": True
        }
