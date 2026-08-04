"""
TRUSTIA Yapay Zeka - KHKN / CBRN (Kimyasal, Biyolojik, Radyolojik, Nükleer) Tehlikeli Madde Algılama ve İzolasyon Modülü.

Sensör Girişleri:
  * Radyasyon / Geiger-Müller Sayacı (CPM / uSv/h)
  * Kimyasal Harp Maddeleri (Sarin, VX, Hardal Gazı PPM Konsantrasyonu)
  * Biyolojik Aerosol / Partikül Analizi
  * Gaz Yayılım Yönü ve Rüzgar Vektör Füzyon İşleme
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Tuple, Any

import numpy as np


class CbrnThreatType(IntEnum):
    """KHKN / CBRN Tehlike Tipleri."""
    SAFE = 0
    CHEMICAL_GAS = 1       # Kimyasal Harp Gazı (Sarin, VX, Tabun, Hardal)
    RADIOLOGICAL_NUCLEAR = 2  # Radyasyon / Nükleer Serpintı
    BIOLOGICAL_HAZARD = 3  # Biyolojik Tehdit / Virüs / Aerosol
    TOXIC_INDUSTRIAL = 4   # Endüstriyel Zehirli Gaz (Klor, Amonyak)


@dataclass
class CbrnReading:
    """KHKN Sensör Okuma Verisi."""
    east_m: float
    north_m: float
    radiation_usvh: float = 0.12        # Arka plan radyasyon seviyesi (uSv/h)
    chemical_ppm: float = 0.0           # Kimyasal gaz konsantrasyonu (PPM)
    bio_particle_count: float = 10.0    # Biyolojik partikül yoğunluğu
    wind_speed_mps: float = 2.0         # Rüzgar hızı (m/s)
    wind_dir_deg: float = 90.0          # Rüzgar yönü (Derece)


@dataclass
class CbrnThreatReport:
    """KHKN Tehdit ve İzolasyon Raporu."""
    threat_id: str
    threat_type: CbrnThreatType
    severity_level: str                # LOW, MEDIUM, CRITICAL, EXTREME
    location_enu: Tuple[float, float]
    isolation_radius_m: float          # Tehlikeli alan izolasyon yarıçapı
    downwind_hazard_m: float           # Rüzgar altı tehlike yayılım mesafesi
    description: str


class CbrnDetector:
    """Askeri Sınıf KHKN / CBRN Tehlikeli Madde Tespit Motoru."""

    def __init__(self, rad_threshold_usvh: float = 2.5, chem_threshold_ppm: float = 0.5) -> None:
        self.rad_threshold_usvh = rad_threshold_usvh
        self.chem_threshold_ppm = chem_threshold_ppm
        self.detected_hazards: List[CbrnThreatReport] = []

    def analyze_readings(self, readings: List[CbrnReading]) -> List[CbrnThreatReport]:
        """KHKN sensör verilerini analiz edip karantina tehlike bölgelerini çıkarır."""
        threats: List[CbrnThreatReport] = []

        for idx, r in enumerate(readings):
            # 1. Radyolojik / Nükleer Tehdit
            if r.radiation_usvh >= self.rad_threshold_usvh:
                severity = "EXTREME" if r.radiation_usvh > 10.0 else "CRITICAL"
                radius = 50.0 if severity == "EXTREME" else 30.0
                report = CbrnThreatReport(
                    threat_id=f"CBRN-R-{idx+1:03d}",
                    threat_type=CbrnThreatType.RADIOLOGICAL_NUCLEAR,
                    severity_level=severity,
                    location_enu=(r.east_m, r.north_m),
                    isolation_radius_m=radius,
                    downwind_hazard_m=radius * 1.5,
                    description=f"Yüksek Radyasyon Anomali Tespiti ({r.radiation_usvh:.2f} uSv/h)!",
                )
                threats.append(report)
                continue

            # 2. Kimyasal Harp Gazı
            if r.chemical_ppm >= self.chem_threshold_ppm:
                severity = "CRITICAL" if r.chemical_ppm > 2.0 else "MEDIUM"
                # Calculate downwind plume distance based on wind speed
                plume = 40.0 + (r.wind_speed_mps * 10.0)
                report = CbrnThreatReport(
                    threat_id=f"CBRN-C-{idx+1:03d}",
                    threat_type=CbrnThreatType.CHEMICAL_GAS,
                    severity_level=severity,
                    location_enu=(r.east_m, r.north_m),
                    isolation_radius_m=25.0,
                    downwind_hazard_m=plume,
                    description=f"Kimyasal Gaz Bulutu Tespiti ({r.chemical_ppm:.2f} PPM, Rüzgar: {r.wind_speed_mps} m/s)!",
                )
                threats.append(report)

        self.detected_hazards.extend(threats)
        return threats
