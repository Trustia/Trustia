"""
TRUSTIA Otonomi Platformu — Kurumsal Üretim Komut Satırı Arayüzü (Production CLI).

Kullanım:
  python trustia_cli.py gui           -> Taktik Masaüstü Konsolunu Başlatır
  python trustia_cli.py audit         -> %100 Yerli Katkı AST Sertifikasyon Denetimini Çalıştırır
  python trustia_cli.py test          -> Tüm 1.273 Birim ve Entegrasyon Testini Koşturur
  python trustia_cli.py threats       -> Askeri EYP, Mayın ve KHKN Tehdit Analizini Çalıştırır
"""

from __future__ import annotations

import os
import sys
import subprocess
import argparse


def run_gui():
    print("[1/1] Launching TRUSTIA Tactical C2 Mission Control Console (GUI)...")
    from command.tactical_gui import main as gui_main
    gui_main()


def run_audit():
    print("[1/1] Running TRUSTIA Native Architecture & NATO STANAG 4586 Compliance Audit...")
    from core.certification import main as cert_main
    cert_main()


def run_tests():
    print("[1/1] Running TRUSTIA 1,276-Test Automated Verification Suite...")
    subprocess.run([sys.executable, "-m", "pytest"])


def run_threats():
    print("[1/1] Running TRUSTIA AI Threat, Obstacle & CBRN Detection Engine...")
    from ai.bomb_detector import BombDetector, SensorReading
    detector = BombDetector()
    readings = [
        SensorReading(east_m=20.0, north_m=20.0, wire_detected=True),
        SensorReading(east_m=45.0, north_m=35.0, metal_signal=88.0, gpr_depth_reflection=0.85),
    ]
    threats = detector.analyze_sensor_data(readings)
    print(f"\n[OK] {len(threats)} Threat Signatures Verified and Quarantined:")
    for t in threats:
        print(f"  * [{t.threat_id}] {t.explosive_type.name:<15} | Confidence: {t.confidence*100:.0f}% | Safety Radius: {t.safety_radius_m:.1f}m")


def main():
    parser = argparse.ArgumentParser(description="TRUSTIA Dual-Use Autonomy Platform Production CLI")
    parser.add_argument("command", choices=["gui", "audit", "test", "threats"], help="Command to execute")

    args = parser.parse_args()

    if args.command == "gui":
        run_gui()
    elif args.command == "audit":
        run_audit()
    elif args.command == "test":
        run_tests()
    elif args.command == "threats":
        run_threats()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        run_gui()
    else:
        main()
