"""
TRUSTIA Otonomi Platformu — Askeri Sınıf EYP, Mayın ve Bomba Algılama Gösterim Demosu.
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.bomb_detector import BombDetector, ExplosiveType, SensorReading
from planning.grid_map import GridMap
from planning.astar import AStarPlanner


def main():
    print("=========================================================================")
    print("  TRUSTIA ASKERI SINIF EYP / MAYIN / BOMBA ALGILAMA VE IZOLASYON DEMOSU ")
    print("=========================================================================\n")

    detector = BombDetector(min_confidence=0.65)
    grid = GridMap(width_m=80.0, height_m=80.0, resolution_m=1.0)

    # Sensör Verileri (Metal Dedektörü, Termal Anomali, GPR Radar, LiDAR)
    readings = [
        SensorReading(east_m=20.0, north_m=20.0, wire_detected=True),  # Tuzak Teli
        SensorReading(east_m=40.0, north_m=30.0, metal_signal=88.0, gpr_depth_reflection=0.85),  # Anti-Tank Mayını
        SensorReading(east_m=30.0, north_m=60.0, thermal_temp_c=28.5, ambient_temp_c=21.0, surface_anomaly=0.7),  # Plastik EYP
        SensorReading(east_m=65.0, north_m=65.0, metal_signal=75.0, surface_anomaly=0.85),  # UXO Havan Mühimmatı
    ]

    print("[1/3] Coklu Sensor Fuzyonu Ile Tarama Baslatiliyor...")

    threats = detector.analyze_sensor_data(readings)

    print(f"\n[2/3] {len(threats)} ADET ASKERI TEHDIT Saptandi ve Siniflandirildi:\n")
    for t in threats:
        print(f"  * [{t.threat_id}] Tip: {t.explosive_type.name:<15} | Guven: %{t.confidence*100:.1f} | Konum: ENU({t.location_enu[0]:.1f}m, {t.location_enu[1]:.1f}m) | Karantina Yaricapi: {t.safety_radius_m:.1f}m")
        print(f"    -> Detay: {t.description}\n")

    # Tehlike Bölgelerini Haritada İzolasyon
    isolated_count = detector.isolate_threat_zones_on_grid(grid, threats)
    print(f"[3/3] {isolated_count} Kritik Tehdit Bolgesi Otonom Haritada Izolasyon Karantinasina Alindi.")

    # Otonom Rota Planlayıcısı (A*) Testi
    planner = AStarPlanner(grid)
    start = (2.0, 2.0)
    goal = (10.0, 70.0)

    path = planner.plan(start, goal)
    print(f"\n[SONUC] OTONOM SURUS ROTASI: Arac patlayici karantina bolgelerinden teget gecerek hedefe ulasti!")
    print(f"        Rota Uzunlugu: {path.length_m:.2f} metre | Waypoint Sayisi: {len(path.waypoints)}")
    print("=========================================================================\n")


if __name__ == "__main__":
    main()
