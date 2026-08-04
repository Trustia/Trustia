"""
TRUSTIA Otonomi Platformu — Hava-Kara Hibrit Suru, Gorsel Odometri ve Taktik Sesli Komut Demosu.
"""

from __future__ import annotations

import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from integration.calibration import HardwareCalibrator, SensorExtrinsics
from ai.air_ground_swarm import AirGroundSwarmCoordinator, UavAirReconData
from slam.visual_odometry import VisualOdometryEstimator
from command.voice_command import VoiceCommandParser


def main():
    print("=========================================================================")
    print("  TRUSTIA AŞAMA 9 — HAVA-KARA HİBRİT SÜRÜ VE TAKTİK SESLİ KOMUT DEMOSU ")
    print("=========================================================================\n")

    # 1. Hardware Calibration
    calib = HardwareCalibrator()
    calib.set_sensor_offset("LiDAR_3D", SensorExtrinsics(x_m=1.2, y_m=0.0, z_m=1.8))
    transformed = calib.transform_point_to_vehicle("LiDAR_3D", (10.0, 5.0, 0.5))
    print(f"[1/4] Sensör Kalibrasyonu: LiDAR Noktası Araç Merkezine Dönüştürüldü -> BaseLink: {transformed}")

    # 2. Air-Ground Swarm (UAV Scouting -> UGV Dispatch)
    air_coordinator = AirGroundSwarmCoordinator()
    uav_data = UavAirReconData(uav_id="BAYRAKTAR-UAV", target_type="HAZARD_BOMB", east_m=45.0, north_m=55.0, confidence=0.95)
    dispatch = air_coordinator.receive_uav_recon(uav_data)
    print(f"\n[2/4] Hava-Kara Hibrit Sürü: İHA'dan Gelen İhbar -> {dispatch['uav_id']} Hedef: ENU({dispatch['ugv_target_enu'][0]}m, {dispatch['ugv_target_enu'][1]}m)")

    # 3. Visual Odometry (Camera Motion Estimation)
    vo = VisualOdometryEstimator()
    feat1 = np.array([[100, 150], [200, 250]], dtype=float)
    feat2 = np.array([[105, 152], [205, 252]], dtype=float)
    dist, yaw = vo.estimate_motion(feat1)
    dist, yaw = vo.estimate_motion(feat2)
    print(f"\n[3/4] Görsel Kameralı Odometri: Tahmini İlerleme Mesafesi = {dist:.3f}m | Açı = {yaw:.4f} rad")

    # 4. Tactical Voice Command Parsing
    voice_input = "IKA-ALPHA, B1 bölgesine git ve devriye at"
    intent = VoiceCommandParser.parse_intent(voice_input)
    print(f"\n[4/4] Taktik Sesli Komut Çözümleme: '{voice_input}'")
    print(f"      -> Çözümlenen İrade: Tip = {intent.command_type} | Hedef Araç = {intent.target_vehicle} | Bölge = {intent.target_location}")

    print("\n=========================================================================\n")


if __name__ == "__main__":
    main()
