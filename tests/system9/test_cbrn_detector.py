"""
TRUSTIA Sistem 9 - KHKN / CBRN Tehlikeli Madde Algılama Birim Testleri.
"""

import pytest
from ai.cbrn_detector import CbrnDetector, CbrnReading, CbrnThreatType


def test_cbrn_radiation_detection():
    detector = CbrnDetector(rad_threshold_usvh=2.5)
    readings = [
        CbrnReading(east_m=20.0, north_m=20.0, radiation_usvh=12.5)
    ]
    threats = detector.analyze_readings(readings)
    assert len(threats) == 1
    t = threats[0]
    assert t.threat_type == CbrnThreatType.RADIOLOGICAL_NUCLEAR
    assert t.severity_level == "EXTREME"
    assert t.isolation_radius_m == 50.0


def test_cbrn_chemical_gas_detection():
    detector = CbrnDetector(chem_threshold_ppm=0.5)
    readings = [
        CbrnReading(east_m=30.0, north_m=40.0, chemical_ppm=1.8, wind_speed_mps=3.0)
    ]
    threats = detector.analyze_readings(readings)
    assert len(threats) == 1
    t = threats[0]
    assert t.threat_type == CbrnThreatType.CHEMICAL_GAS
    assert t.downwind_hazard_m == 70.0
