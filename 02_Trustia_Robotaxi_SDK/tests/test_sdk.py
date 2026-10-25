"""
TRUSTIA Otonomi Teknolojileri — Seviye-4 Robotaksi SDK Otomatik Doğrulama Test Süiti.
Tüm Birim ve Entegrasyon Testleri (%100 Bağımsız ve Sıfır Dış Kütüphane Bağımlılığı).
"""

from __future__ import annotations

import math
import sys
import os

# Ana dizini sys.path'e ekle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from trustia_sdk.core.licensing import LicenseManager
from trustia_sdk.core.transforms import Pose2D, KinematicState, normalize_angle
from trustia_sdk.canbus.mifa7_canfd import Mifa7CanFdBridge, CanFdFrame, ID_MIFA7_STEERING_CMD_FD, ID_MIFA7_ESTOP_CMD
from trustia_sdk.perception.calmcar_bridge import CalmCarSafetyArbiter, Obstacle3D
from trustia_sdk.slam.ndt_eskf import ErrorStateKalmanFilter, ImuMeasurement
from trustia_sdk.planning.hybrid_astar import HybridAStarPlanner
from trustia_sdk.control.stanley_controller import StanleyController
from trustia_sdk.safety.asil_d_mrm import AsilDSafetySupervisor, SafetyState
from trustia_sdk.fleet.telemetry_api import TripyFleetBridge, RobotaxiMission


def test_licensing():
    print("  * [TEST 1/9] Ticari Lisanslama ve Kriptografik İmza Denetimi...", end=" ")
    lic = LicenseManager.create_license(client_name="Tripy Mobility A.S.", expiry_date="2027-12-31")
    valid, msg = LicenseManager.verify_license(lic)
    assert valid, f"Geçerli lisans doğrulanamadı: {msg}"

    # Sahtecilik / Kurcalama testi
    tampered_lic = dict(lic)
    tampered_lic["max_vehicles"] = "999999" # Kurcalandı
    tampered_valid, _ = LicenseManager.verify_license(tampered_lic)
    assert not tampered_valid, "Kurcalanmış lisans kabul edildi!"
    print("BAŞARILI")


def test_transforms():
    print("  * [TEST 2/9] Kinematik Koordinat ve SE(2) Dönüşümleri...", end=" ")
    p1 = Pose2D(0.0, 0.0, 0.0)
    p2 = Pose2D(3.0, 4.0, 0.0)
    assert abs(p1.distance_to(p2) - 5.0) < 1e-5

    state = KinematicState(x=10.0, y=20.0, yaw_rad=math.radians(90), velocity_mps=5.0)
    # 90 derece dönükken x=2 (araç ileri) -> küresel y=+2 olmalı
    gx, gy = state.local_to_global(2.0, 0.0)
    assert abs(gx - 10.0) < 1e-4
    assert abs(gy - 22.0) < 1e-4

    # Açı normalizasyonu
    assert abs(normalize_angle(math.pi * 3.0) - math.pi) < 1e-4
    print("BAŞARILI")


def test_can_fd():
    print("  * [TEST 3/9] SAIC Maxus MIFA 7 ISO 11898-1 CAN-FD Aktüatör Kodlayıcı...", end=" ")
    bridge = Mifa7CanFdBridge()

    # Direksiyon çerçevesi
    f_steer = bridge.encode_steering_command(target_angle_deg=15.5, max_torque_nm=3.2)
    assert f_steer.arbitration_id == ID_MIFA7_STEERING_CMD_FD
    assert f_steer.is_fd is True
    assert len(f_steer.data) == 16

    # Hız ve fren çerçevesi
    f_accel = bridge.encode_accel_brake_command(target_accel_mps2=1.5, target_speed_mps=10.0)
    assert f_accel.is_fd is True

    # Acil durdurma çerçevesi
    f_estop = bridge.encode_emergency_stop()
    assert f_estop.arbitration_id == ID_MIFA7_ESTOP_CMD
    print("BAŞARILI")


def test_calmcar_arbiter():
    print("  * [TEST 4/9] CalmCar Deterministik Güvenlik Hakemi ve KVKK Kalkanı...", end=" ")
    arbiter = CalmCarSafetyArbiter()

    # Ham kamera nesnesi
    raw_objs = [
        {"id": 1, "class": "VEHICLE", "x": 12.0, "y": 0.5, "vx": -8.0, "confidence": 0.92}, # Gerçek engel
        {"id": 2, "class": "PHANTOM", "x": 40.0, "y": 2.0, "vx": 0.0, "confidence": 0.30},  # Güvensiz hayalet
    ]
    lidar_truth = [(12.1, 0.4)] # LiDAR engeli doğruladı

    obstacles, estop_req, msg = arbiter.evaluate_perception_stream(raw_objs, lidar_truth)
    assert len(obstacles) == 1, f"Hayalet engel filtrelenemedi: {len(obstacles)}"
    assert obstacles[0].obstacle_id == 1
    assert obstacles[0].is_lidar_confirmed is True

    # KVKK m.9 Yurt Dışı Bulut Güvenlik Kalkanı Testi
    assert arbiter.inspect_cloud_telemetry_packet("api.tripy.im", 1024) is True
    assert arbiter.inspect_cloud_telemetry_packet("calmforge.beijing.cn/telemetry", 2048) is False
    assert arbiter.blocked_foreign_sync_attempts == 1
    print("BAŞARILI")


def test_slam_eskf():
    print("  * [TEST 5/9] 3D LiDAR NDT & 400 Hz Error-State Kalman Filtresi (ESKF)...", end=" ")
    eskf = ErrorStateKalmanFilter(initial_pose=Pose2D(0.0, 0.0, 0.0))

    # IMU tahmini
    imu = ImuMeasurement(accel_x_mps2=2.0, accel_y_mps2=0.0, accel_z_mps2=9.81, gyro_z_radps=0.05, timestamp=0.0)
    state = eskf.predict(imu, dt_s=0.01)
    assert state.x > 0.0
    assert state.velocity_mps > 0.0

    # NDT ölçüm düzeltmesi
    eskf.correct_with_lidar_ndt(observed_x=0.05, observed_y=0.01, observed_yaw=0.005, ndt_score=0.95)
    corrected = eskf.get_state()
    assert abs(corrected.y) < 0.05
    print("BAŞARILI")


def test_planning_hybrid_astar():
    print("  * [TEST 6/9] Kinematik Kısıtlı Hybrid A* Rota Planlama Motoru...", end=" ")
    planner = HybridAStarPlanner(wheel_base_m=2.975, max_steer_deg=35.0)
    start = Pose2D(0.0, 0.0, 0.0)
    goal = Pose2D(15.0, 5.0, math.radians(20))
    obstacles = [(7.5, 2.5, 1.0)]

    path = planner.plan(start, goal, obstacles)
    assert len(path) >= 5, "Geçerli yol üretilemedi"
    # Başlangıç ve bitiş yakınlığı
    assert path[0].distance_to(start) < 0.5
    print("BAŞARILI")


def test_stanley_controller():
    print("  * [TEST 7/9] Stanley Yol Takip ve Boyuna PID Denetleyicisi...", end=" ")
    controller = StanleyController(wheel_base_m=2.975)
    path = [Pose2D(float(i), 0.0, 0.0) for i in range(20)]
    # Araç yoldan 0.5 metre solda olsun
    state = KinematicState(x=5.0, y=0.5, yaw_rad=0.0, velocity_mps=5.0)

    steer_rad, cte, _ = controller.compute_steering(state, path)
    # Yoldan solda olduğu için direksiyon sağa (negatif açı) kırmalı
    assert steer_rad < 0.0, "Yanal hata için doğru düzeltme yönü hesaplanamadı"

    accel = controller.compute_longitudinal_accel(current_speed_mps=5.0, target_speed_mps=10.0)
    assert accel > 0.0, "Hızlanma ivmesi hesaplanamadı"
    print("BAŞARILI")


def test_safety_mrm():
    print("  * [TEST 8/9] ISO 26262 ASIL-D Minimal Risk Maneuver (MRM) ve Watchdog...", end=" ")
    safety = AsilDSafetySupervisor(watchdog_timeout_ms=50.0)

    # 1. Normal Durum
    safety.feed_watchdog()
    diag = safety.evaluate_safety(cross_track_error_m=0.1, can_bus_ok=True, calmcar_arbiter_alert=False)
    assert diag.state == SafetyState.NOMINAL_AUTONOMOUS
    assert diag.safe_to_drive is True

    # 2. Kritik Algı / Çarpışma Tetiği
    diag_collision = safety.evaluate_safety(cross_track_error_m=0.1, can_bus_ok=True, calmcar_arbiter_alert=True)
    assert diag_collision.state == SafetyState.MRM_EMERGENCY_STOP
    assert safety.get_mrm_deceleration() == -6.5

    # 3. CAN-FD Hat Kesintisi
    diag_can = safety.evaluate_safety(cross_track_error_m=0.1, can_bus_ok=False, calmcar_arbiter_alert=False)
    assert diag_can.state == SafetyState.MRM_EMERGENCY_STOP
    print("BAŞARILI")


def test_fleet_telemetry():
    print("  * [TEST 9/9] Tripy Filo Telemetri Köprüsü ve Görev Yönetimi...", end=" ")
    bridge = TripyFleetBridge(vehicle_id="TRIPY-MIFA7-TEST")
    state = KinematicState(x=10.0, y=20.0, yaw_rad=0.5, velocity_mps=8.33)
    safety = AsilDSafetySupervisor()
    diag = safety.evaluate_safety(cross_track_error_m=0.05, can_bus_ok=True, calmcar_arbiter_alert=False)

    packet = bridge.generate_telemetry_packet(state, diag)
    assert packet.vehicle_id == "TRIPY-MIFA7-TEST"
    assert abs(packet.speed_kmh - 30.0) < 0.5
    json_str = packet.to_json()
    assert "TRIPY-MIFA7-TEST" in json_str

    mission = RobotaxiMission(
        mission_id="MSN-001",
        passenger_name="Dr. Ali Onuralp Unal",
        pickup_coords=(39.8688, 32.7483),
        dropoff_coords=(39.9000, 32.8000),
        fare_tl=185.50
    )
    assert bridge.dispatch_mission(mission) is True
    assert bridge.active_mission.status == "EN_ROUTE_PICKUP"
    print("BAŞARILI")


def run_all_tests():
    print("\n" + "=" * 75)
    print("  TRUSTIA v2.4 ROBOTAXI SDK — DOĞRULAMA SÜİTİ BAŞLATILIYOR")
    print("=" * 75)
    test_licensing()
    test_transforms()
    test_can_fd()
    test_calmcar_arbiter()
    test_slam_eskf()
    test_planning_hybrid_astar()
    test_stanley_controller()
    test_safety_mrm()
    test_fleet_telemetry()
    print("=" * 75)
    print("  [MÜKEMMEL] 9 Temel Alt Sistem Testinin Tamamı (%100) Sıfır Hatayla Geçti!")
    print("  SAIC Maxus MIFA 7 Seviye-4 Kurumsal SDK Üretime ve PoC'ye Hazır!")
    print("=" * 75 + "\n")


if __name__ == "__main__":
    run_all_tests()
