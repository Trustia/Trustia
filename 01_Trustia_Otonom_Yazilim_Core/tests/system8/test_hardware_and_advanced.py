"""
TRUSTIA Sistem 8 Testleri — Donanım Sürücüleri, ESKF, Anti-Spoofing ve Telemetri Doğrulaması.
"""

import math
import time
import pytest

from slam.eskf import ErrorStateKalmanFilter, ImuMeasurement, OdometryMeasurement, LidarPoseMeasurement
from security.anti_spoof import AntiGpsSpoofGuard, GpsFix, GpsSecurityStatus
from integration.can import SocketCanBus, CanFrame, ID_MOTOR_SPEED, MotorController
from integration.ros2_bridge import Ros2Bridge, Ros2Twist, Ros2QosProfile, Ros2QosPolicy
from core.api.telemetry_server import TelemetryDataHub, VehicleTelemetrySnapshot


def test_eskf_prediction_and_updates():
    """400Hz ESKF IMU tahmini, odometri ve LiDAR ICP düzeltme testi."""
    eskf = ErrorStateKalmanFilter(initial_east=10.0, initial_north=20.0, initial_yaw=0.0)

    # 1. IMU İleri İvme Tahmini
    t0 = 100.0
    for i in range(10):
        imu = ImuMeasurement(
            timestamp_s=t0 + i * 0.0025,  # 400 Hz (2.5ms)
            accel_x=1.0,
            accel_y=0.0,
            accel_z=9.81,
            gyro_z=0.05,
        )
        st = eskf.predict_imu(imu)

    assert st.velocity_mps > 0.0
    assert st.east_m > 10.0

    # 2. Odometri Hız Düzeltmesi (Kalman Konverjansı)
    for _ in range(3):
        odom = OdometryMeasurement(timestamp_s=t0 + 0.05, speed_mps=1.2, steer_angle_rad=0.0)
        st = eskf.update_odometry(odom)
    assert abs(st.velocity_mps - 1.2) < 0.3

    # 3. LiDAR ICP Poz Güncellemesi (Kalman Konverjansı)
    for _ in range(5):
        lidar = LidarPoseMeasurement(timestamp_s=t0 + 0.1, east_m=10.5, north_m=20.1, yaw_rad=0.02)
        st = eskf.update_lidar_pose(lidar)
    assert abs(st.east_m - 10.5) < 0.1
    assert abs(st.north_m - 20.1) < 0.1


def test_anti_gps_spoofing_guard():
    """Anti-GPS Spoofing ve Jamming algılama kalkanı testi."""
    guard = AntiGpsSpoofGuard(max_speed_discrepancy_mps=3.0, max_pos_jump_m=10.0)

    # 1. Normal Güvenli GPS Sinyali
    gps1 = GpsFix(timestamp_s=1.0, east_m=0.0, north_m=0.0, speed_mps=2.0, heading_deg=45.0, num_satellites=12)
    status, ok = guard.evaluate_signal(gps1, imu_speed_estimate_mps=2.0, imu_accel_norm=0.1)
    assert status == GpsSecurityStatus.TRUSTED
    assert ok is True

    # 2. Sahte Sinyal (Hız Uyuşmazlığı & Işınlanma Sıçraması)
    gps2 = GpsFix(timestamp_s=2.0, east_m=500.0, north_m=500.0, speed_mps=50.0, heading_deg=45.0, num_satellites=12)
    status, ok = guard.evaluate_signal(gps2, imu_speed_estimate_mps=2.1, imu_accel_norm=0.1)
    assert status in (GpsSecurityStatus.SUSPECTED, GpsSecurityStatus.SPOOFED_ATTACK)
    assert ok is False

    # İkinci saldırı karesinde tamamen izole edilmeli
    gps3 = GpsFix(timestamp_s=3.0, east_m=600.0, north_m=600.0, speed_mps=60.0, heading_deg=45.0, num_satellites=12)
    status, ok = guard.evaluate_signal(gps3, imu_speed_estimate_mps=2.1, imu_accel_norm=0.1)
    assert status == GpsSecurityStatus.SPOOFED_ATTACK
    assert guard.is_safe_to_navigate_gps() is False


def test_socket_can_bus_fallback():
    """SocketCAN donanım sınıfı sanal fallback ve iletim testi."""
    bus = SocketCanBus(interface="vcan0", fallback_to_virtual=True)
    frame = CanFrame(ID_MOTOR_SPEED, MotorController.encode_speed(2.5))
    bus.transmit(frame)

    assert bus.tx_count() == 1
    assert bus.last() is not None
    assert MotorController.decode_speed(bus.last()) == 2.5


def test_telemetry_data_hub():
    """Canlı telemetri veri havuzu anlık görüntü testi."""
    hub = TelemetryDataHub()
    snap = VehicleTelemetrySnapshot(
        vehicle_id="IKA-ALPHA",
        east_m=15.2,
        north_m=34.8,
        speed_mps=3.2,
        heading_deg=90.0,
        battery_pct=88.5,
    )
    hub.update_telemetry(snap)

    data = hub.get_snapshot("IKA-ALPHA")
    assert data is not None
    assert data["vehicle_id"] == "IKA-ALPHA"
    assert data["east_m"] == 15.2
    assert data["battery_pct"] == 88.5

    all_data = hub.get_all_snapshots()
    assert "IKA-ALPHA" in all_data


def test_ros2_advanced_bridge():
    """Gelişmiş ROS 2 köprüsü, odometri ve QoS testi."""
    twist = Ros2Twist(linear_x=2.0, angular_z=0.1)
    cmd = Ros2Bridge.twist_to_drive_command(twist)
    assert cmd["speed_mps"] == 2.0
    assert cmd["steer_rad"] == 0.1

    odom = Ros2Bridge.pose_to_ros2_odometry(east_m=12.0, north_m=24.0, yaw_rad=1.57, speed_mps=2.5)
    assert odom.header.frame_id == "odom"
    assert odom.pos_x == 12.0
    assert odom.speed_mps == 2.5

    qos_sensor = Ros2QosProfile.sensor_data()
    assert qos_sensor.reliability == Ros2QosPolicy.BEST_EFFORT
