"""
TRUSTIA Otonomi Platformu — KHKN / CBRN Tehlikeli Madde Algilama ve Karantina Demosu.
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.cbrn_detector import CbrnDetector, CbrnReading, CbrnThreatType


def main():
    print("=========================================================================")
    print("  TRUSTIA ASKERI KHKN / CBRN TEHLİKELİ MADDE VE GAZ ALGILAMA DEMOSU ")
    print("=========================================================================\n")

    detector = CbrnDetector(rad_threshold_usvh=2.5, chem_threshold_ppm=0.5)

    readings = [
        CbrnReading(east_m=25.0, north_m=25.0, radiation_usvh=14.2),  # Yuksek Radyasyon
        CbrnReading(east_m=50.0, north_m=50.0, chemical_ppm=2.4, wind_speed_mps=4.5),  # Kimyasal Gaz
    ]

    print("[1/2] KHKN / CBRN Sensor Taramasi Yapiliyor...")

    threats = detector.analyze_readings(readings)

    print(f"\n[2/2] {len(threats)} ADET KRITIK TEHLIKELI MADDE / GAZ Saptandi:\n")
    for t in threats:
        print(f"  * [{t.threat_id}] Tip: {t.threat_type.name:<22} | Seviye: {t.severity_level:<8} | Konum: ENU({t.location_enu[0]:.1f}m, {t.location_enu[1]:.1f}m)")
        print(f"    -> Karantina Yaricapi: {t.isolation_radius_m:.1f}m | Ruzgar Alti Tehlike: {t.downwind_hazard_m:.1f}m")
        print(f"    -> Detay: {t.description}\n")

    print("=========================================================================\n")


if __name__ == "__main__":
    main()
