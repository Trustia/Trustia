"""
TRUSTIA Yapay Zeka - EYP / Mayın / Patlayıcı Maddeler Algılama ve Tehdit Değerlendirme Modülü.

Sensör Füzyonu (LiDAR, Termal Anomali, Metal Dedektör Sinyali, GPR Radar):
  * EYP (El Yapımı Patlayıcı) Tespiti
  * Anti-Personel / Anti-Tank Mayını Tespiti
  * UXO (Patlamamış Mühimmat / Havan-Top Mermisi) Tespiti
  * Tuzak Teli / Kablo Tespiti (Tripwire)

Tehlike Yönetimi:
  * Güvenli Karantina Yarıçapı Hesaplama (Stand-off Blast Radius)
  * EOD (Bomba İmha) Acil Durum Alarmı Üretimi
  * Haritaya Otomatik Tehdit Bölgesi İzolasyonu (Infinite Cost Hazard Area)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional, Tuple, Dict, Any

import numpy as np


class ExplosiveType(IntEnum):
    """Patlayıcı ve Mühimmat Tipleri."""
    SAFE = 0             # Güvenli / Tehdit Yok
    IED_BOMB = 1         # El Yapımı Patlayıcı (EYP)
    LANDMINE_AP = 2      # Anti-Personel Mayını
    LANDMINE_AT = 3      # Anti-Tank Mayını
    UXO = 4              # Patlamamış Mühimmat (Unexploded Ordnance)
    TRIPWIRE = 5         # Tuzak Teli / Kablo Nem/Gerilim Hattı


@dataclass
class ThreatReport:
    """Tekil Patlayıcı Tehdit Raporu."""
    threat_id: str
    explosive_type: ExplosiveType
    confidence: float                  # [0.0 - 1.0] Güven skoru
    location_enu: Tuple[float, float]  # (East_m, North_m)
    depth_m: float                     # Toprak altı derinliği (0 = yüzeyde)
    safety_radius_m: float             # Güvenli durma / karantina yarıçapı
    metal_signature: float             # Metal indüksiyon sinyali
    thermal_anomaly_degc: float        # Toprak ısı gradyan farkı
    description: str = ""

    @property
    def is_critical(self) -> bool:
        return self.confidence >= 0.65 and self.explosive_type != ExplosiveType.SAFE


@dataclass
class SensorReading:
    """Çoklu Sensör Giriş Verisi."""
    east_m: float
    north_m: float
    metal_signal: float = 0.0          # [0 - 100] Metal dedektör şiddeti
    thermal_temp_c: float = 20.0       # Termal kamera sıcaklığı (°C)
    ambient_temp_c: float = 20.0       # Ortam sıcaklığı (°C)
    surface_anomaly: float = 0.0       # LiDAR/Kamera zemin bozulma oranı [0 - 1]
    gpr_depth_reflection: float = 0.0  # GPR Yere nüfuz eden radar yansıması [0 - 1]
    wire_detected: bool = False        # Kablo/Tel tespiti


class BombDetector:
    """Askeri Sınıf EYP ve Mayın Tespit Motoru."""

    def __init__(self, min_confidence: float = 0.65) -> None:
        self.min_confidence = min_confidence
        self.detected_threats: List[ThreatReport] = []

    def analyze_sensor_data(self, readings: List[SensorReading]) -> List[ThreatReport]:
        """Sensör okumalarını analiz edip patlayıcı tehditlerini saptar."""
        new_threats: List[ThreatReport] = []

        for idx, r in enumerate(readings):
            temp_diff = abs(r.thermal_temp_c - r.ambient_temp_c)

            # 1. Tuzak teli tespiti
            if r.wire_detected:
                report = ThreatReport(
                    threat_id=f"BMB-{idx+1:03d}",
                    explosive_type=ExplosiveType.TRIPWIRE,
                    confidence=0.92,
                    location_enu=(r.east_m, r.north_m),
                    depth_m=0.0,
                    safety_radius_m=15.0,
                    metal_signature=r.metal_signal,
                    thermal_anomaly_degc=temp_diff,
                    description="Kablo / Tuzak Teli Algılandı!",
                )
                new_threats.append(report)
                continue

            # 2. Anti-Tank veya Ağır EYP (Yüksek Metal + GPR Yansıması + Zemin Anomalisi)
            if r.metal_signal > 70.0 and r.gpr_depth_reflection > 0.6:
                exp_type = ExplosiveType.LANDMINE_AT if r.gpr_depth_reflection > 0.8 else ExplosiveType.IED_BOMB
                confidence = min(0.99, (r.metal_signal / 100.0) * 0.5 + r.gpr_depth_reflection * 0.5)
                report = ThreatReport(
                    threat_id=f"BMB-{idx+1:03d}",
                    explosive_type=exp_type,
                    confidence=confidence,
                    location_enu=(r.east_m, r.north_m),
                    depth_m=round(r.gpr_depth_reflection * 0.5, 2),
                    safety_radius_m=25.0 if exp_type == ExplosiveType.IED_BOMB else 20.0,
                    metal_signature=r.metal_signal,
                    thermal_anomaly_degc=temp_diff,
                    description="Yüksek Metal & GPR Derinlik Yansıması (Ağır EYP / Anti-Tank Mayını)",
                )
                new_threats.append(report)
                continue

            # 3. Gömülü Düşük Metal EYP / Anti-Personel Mayın (Termal Anomali + Zemin Bozulması)
            if temp_diff > 3.5 and (r.surface_anomaly > 0.5 or r.gpr_depth_reflection > 0.4):
                confidence = min(0.95, 0.4 + (temp_diff / 10.0) + r.surface_anomaly * 0.3)
                report = ThreatReport(
                    threat_id=f"BMB-{idx+1:03d}",
                    explosive_type=ExplosiveType.LANDMINE_AP,
                    confidence=confidence,
                    location_enu=(r.east_m, r.north_m),
                    depth_m=0.15,
                    safety_radius_m=10.0,
                    metal_signature=r.metal_signal,
                    thermal_anomaly_degc=temp_diff,
                    description="Toprak Altı Isı Anomalisi (Anti-Personel Mayını / Plastik EYP)",
                )
                new_threats.append(report)
                continue

            # 4. Yüzeyde Patlamamış Mühimmat (UXO)
            if r.metal_signal > 50.0 and r.surface_anomaly > 0.7:
                report = ThreatReport(
                    threat_id=f"BMB-{idx+1:03d}",
                    explosive_type=ExplosiveType.UXO,
                    confidence=0.85,
                    location_enu=(r.east_m, r.north_m),
                    depth_m=0.0,
                    safety_radius_m=30.0,
                    metal_signature=r.metal_signal,
                    thermal_anomaly_degc=temp_diff,
                    description="Yüzeyde Patlamamış Top/Havan Mühimmatı (UXO)",
                )
                new_threats.append(report)

        self.detected_threats.extend(new_threats)
        return new_threats

    def isolate_threat_zones_on_grid(self, grid_map: Any, threats: List[ThreatReport]) -> int:
        """Haritada tespit edilen bomba ve EYP bölgelerini aşılmaz engel (infinite cost) olarak işaretler."""
        marked_count = 0
        for t in threats:
            if t.is_critical:
                if hasattr(grid_map, "mark_obstacle"):
                    grid_map.mark_obstacle(t.location_enu[0], t.location_enu[1], radius_m=t.safety_radius_m)
                    marked_count += 1
        return marked_count
