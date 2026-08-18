"""
TRUSTIA Sistem 9 - EYP, Mayın ve Bomb Tehdit Tespit Modülü Birim Testleri.
"""

import pytest
from ai.bomb_detector import BombDetector, ExplosiveType, SensorReading, ThreatReport
from planning.grid_map import GridMap


def test_bomb_detector_tripwire():
    detector = BombDetector()
    readings = [
        SensorReading(east_m=10.0, north_m=5.0, wire_detected=True)
    ]
    threats = detector.analyze_sensor_data(readings)
    assert len(threats) == 1
    t = threats[0]
    assert t.explosive_type == ExplosiveType.TRIPWIRE
    assert t.is_critical is True
    assert t.safety_radius_m == 15.0


def test_bomb_detector_anti_tank_mine():
    detector = BombDetector()
    readings = [
        SensorReading(
            east_m=20.0,
            north_m=15.0,
            metal_signal=85.0,
            gpr_depth_reflection=0.85,
        )
    ]
    threats = detector.analyze_sensor_data(readings)
    assert len(threats) == 1
    t = threats[0]
    assert t.explosive_type == ExplosiveType.LANDMINE_AT
    assert t.confidence > 0.8


def test_bomb_detector_threat_isolation_on_grid():
    detector = BombDetector()
    grid = GridMap(width_m=50.0, height_m=50.0, resolution_m=1.0)
    readings = [
        SensorReading(east_m=25.0, north_m=25.0, wire_detected=True)
    ]
    threats = detector.analyze_sensor_data(readings)
    marked = detector.isolate_threat_zones_on_grid(grid, threats)
    assert marked == 1
    assert grid.is_traversable(25.0, 25.0) is False
