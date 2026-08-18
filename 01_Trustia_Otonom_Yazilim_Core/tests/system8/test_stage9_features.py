"""
TRUSTIA Sistem 8 & 9 - Yeni Entegrasyon Özellikleri Birim Testleri.
"""

import pytest
import numpy as np
from integration.calibration import HardwareCalibrator, SensorExtrinsics
from ai.air_ground_swarm import AirGroundSwarmCoordinator, UavAirReconData
from slam.visual_odometry import VisualOdometryEstimator
from command.voice_command import VoiceCommandParser


def test_hardware_calibration():
    calib = HardwareCalibrator()
    calib.set_sensor_offset("LiDAR", SensorExtrinsics(x_m=1.0, y_m=0.0, z_m=0.5))
    res = calib.transform_point_to_vehicle("LiDAR", (10.0, 2.0, 1.0))
    assert res == (11.0, 2.0, 1.5)


def test_air_ground_swarm():
    coord = AirGroundSwarmCoordinator()
    data = UavAirReconData("DRONE-1", "BOMB", 10.0, 20.0, 0.9)
    res = coord.receive_uav_recon(data)
    assert res["ugv_target_enu"] == (10.0, 20.0)


def test_visual_odometry():
    vo = VisualOdometryEstimator()
    f1 = np.array([[10, 10]], dtype=float)
    f2 = np.array([[15, 12]], dtype=float)
    vo.estimate_motion(f1)
    d, y = vo.estimate_motion(f2)
    assert d > 0.0


def test_voice_command_parser():
    intent = VoiceCommandParser.parse_intent("IKA-BRAVO devriye at")
    assert intent.command_type == "PATROL"
    assert intent.target_vehicle == "IKA-BRAVO"
