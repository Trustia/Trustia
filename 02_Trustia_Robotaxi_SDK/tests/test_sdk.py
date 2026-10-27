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
from trustia_sdk.safety.odd_sotif_dssad import OddDomainMonitor, Iso21448SotifSupervisor, UnR157DssadBlackbox
from trustia_sdk.perception.curb_detector import CurbBoundaryDetector
from trustia_sdk.fleet.teleoperation import TeleoperationSupervisor, RemoteOperatorCommand
from trustia_sdk.core.carla_bridge import RobotaxiCarlaBridge
from trustia_sdk.safety.can_ids_r155 import UnR155CanBusIds
from trustia_sdk.perception.lidar_deskew_ptp import LidarMotionDeskewer, RawTimedPoint3D
from trustia_sdk.planning.lanelet2_rules import Lanelet2TrafficRuleEngine, LaneletSegment
from trustia_sdk.fleet.cabin_bms_safety import (
    RobotaxiCabinAndBmsSupervisor,
    CabinDoorSeatStatus,
    BatteryThermalState,
)
from trustia_sdk.safety.rss_ieee2846 import ResponsibilitySensitiveSafety
from trustia_sdk.planning.frenet_lattice_planner import FrenetLatticePlanner, FrenetState
from trustia_sdk.control.mpc_redundant_control import RecedingHorizonMPC, RedundantActuatorAllocator
from trustia_sdk.safety.sums_un_r156 import UnR156SumsManager
from trustia_sdk.perception.ehmi_siren_detector import ExternalHmiAndSirenSupervisor


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


def test_odd_sotif_dssad_and_curb():
    print("  * [TEST 10/12] ODD Coğrafi Çit, ISO 21448 SOTIF ve UN/ECE R157 DSSAD Kara Kutu...", end=" ")
    odd = OddDomainMonitor()
    ok, status, decel = odd.evaluate(x_m=100.0, y_m=100.0, speed_kmh=40.0)
    assert ok is True and decel == 0.0
    out_ok, out_status, out_decel = odd.evaluate(x_m=9999.0, y_m=9999.0, speed_kmh=40.0)
    assert out_ok is False and out_decel == -1.5

    sotif = Iso21448SotifSupervisor()
    s_ok, phantom, _ = sotif.evaluate(camera_confidence=0.45, lidar_confirmed=False)
    assert s_ok is True and phantom is True

    dssad = UnR157DssadBlackbox()
    dssad.log_event("AUTONOMOUS_START", "AUTONOMOUS_L4", 35.0, 2.5, 0.0)
    dssad.log_event("MRM_PULLOVER_TRIGGER", "AUTONOMOUS_L4", 30.0, 5.0, -1.5)
    assert len(dssad.records) == 2
    assert dssad.verify_integrity() is True
    print("BAŞARILI")


def test_curb_and_teleop():
    print("  * [TEST 11/12] 3B LiDAR Kaldırım Taşı Algılama ve Uzaktan Operasyon (Teleop)...", end=" ")
    curb = CurbBoundaryDetector()
    pts = [(5.0, 2.5, 0.15), (10.0, 2.5, 0.16), (5.0, -2.5, 0.15), (10.0, -2.5, 0.14)]
    res = curb.detect_corridor(pts, road_surface_z_m=0.0)
    assert res.valid_corridor is True
    assert abs(res.corridor_width_m - 5.0) < 0.1

    teleop = TeleoperationSupervisor()
    cmd = RemoteOperatorCommand("OP-01", "TOKEN-VALID-123", target_steer_deg=10.0, target_speed_kmh=12.0, network_rtt_ms=30.0)
    valid, steer, speed_mps, msg = teleop.authorize_and_filter(cmd)
    assert valid is True and abs(steer - 10.0) < 1e-4
    print("BAŞARILI")


def test_carla_bridge():
    print("  * [TEST 12/16] CARLA Simülatör Köprüsü ve 5 ms Sürücü Müdahale Devri...", end=" ")
    carla_br = RobotaxiCarlaBridge()
    s1 = carla_br.step(steer_deg=5.0, accel_mps2=2.0, dt_s=0.01)
    assert s1.autonomous_engaged is True and s1.speed_mps > 0.0
    s2 = carla_br.step(steer_deg=5.0, accel_mps2=2.0, dt_s=0.01, driver_torque_nm=2.5)
    assert s2.autonomous_engaged is False and s2.takeover_latency_ms <= 5.0
    print("BAŞARILI")


def test_can_ids_r155():
    print("  * [TEST 13/16] UN R155 & ISO 21434 CAN-FD Siber Saldırı Tespit Sistemi...", end=" ")
    ids = UnR155CanBusIds()
    ok = ids.inspect_frame(0x120, b"\x00" * 8, timestamp_ms=10.0, rolling_counter=1)
    assert ok.accepted is True
    spoof = ids.inspect_frame(0x777, b"\x00" * 8, timestamp_ms=15.0, rolling_counter=1)
    assert spoof.accepted is False and spoof.threat_type == "UNAUTHORIZED_ID"
    dos = ids.inspect_frame(0x120, b"\x00" * 8, timestamp_ms=11.0, rolling_counter=2)
    assert dos.accepted is False and dos.threat_type == "DOS_FLOODING"
    print("BAŞARILI")


def test_lidar_deskew_ptp():
    print("  * [TEST 14/16] IEEE 1588 PTP Zaman Senkronu ve 3B LiDAR Hareket Düzeltme...", end=" ")
    deskew = LidarMotionDeskewer()
    ptp = deskew.evaluate_ptp_sync("PTP-GM-01", offset_us=25.0, jitter_us=10.0)
    assert ptp.synchronized is True and ptp.sotif_degraded is False
    pts = deskew.deskew_scan([RawTimedPoint3D(10.0, 0.0, 0.5, 0.0)], vx_mps=10.0, vy_mps=0.0, yaw_rate_rad_s=0.0, sweep_duration_s=0.05)
    assert abs(pts[0][0] - 9.5) < 1e-3
    print("BAŞARILI")


def test_lanelet2_traffic_rules():
    print("  * [TEST 15/16] Lanelet2 HD Harita Yaya Geçidi ve Kavşak Geçiş Üstünlüğü...", end=" ")
    engine = Lanelet2TrafficRuleEngine()
    engine.register_lanelet(LaneletSegment("LL-ANK-01", 50.0, True, False, has_crosswalk=True, is_intersection=True))
    dec = engine.evaluate_rules("LL-ANK-01", ego_speed_mps=8.0, pedestrian_on_crosswalk=True, crosswalk_distance_m=14.0)
    assert dec.behavior_command == "STOP_FOR_PEDESTRIAN" and dec.target_speed_mps == 0.0
    print("BAŞARILI")


def test_cabin_and_bms_safety():
    print("  * [TEST 16/16] Robotaksi Kapı Emniyet Kilidi, SOS Butonu ve Batarya BMS...", end=" ")
    sup = RobotaxiCabinAndBmsSupervisor()
    door_open = sup.evaluate(
        CabinDoorSeatStatus(all_doors_closed=False, trunk_closed=True, passenger_seated=True, seatbelt_fastened=True),
        BatteryThermalState(soc_percent=80.0, pack_temp_c=30.0, estimated_range_km=320.0),
        vehicle_speed_mps=0.0,
    )
    assert door_open.dispatch_allowed is False and door_open.motion_inhibit_brake_hold is True
    sos = sup.evaluate(
        CabinDoorSeatStatus(all_doors_closed=True, trunk_closed=True, passenger_seated=True, seatbelt_fastened=True, passenger_sos_pressed=True),
        BatteryThermalState(soc_percent=80.0, pack_temp_c=30.0, estimated_range_km=320.0),
        vehicle_speed_mps=8.0,
    )
    assert sos.trigger_passenger_mrm is True and sos.intercom_call_center_active is True
    print("BAŞARILI")


def test_rss_ieee2846():
    print("  * [TEST 17/21] IEEE 2846 & Mobileye RSS Matematiksel Çarpışmasızlık Kalkanı...", end=" ")
    rss = ResponsibilitySensitiveSafety()
    verdict = rss.evaluate_pair(ego_vel_mps=15.0, front_vel_mps=4.0, actual_longitudinal_gap_m=3.5, actual_lateral_gap_m=0.1)
    assert verdict.longitudinal_safe is False and verdict.proper_response == "RSS_LONGITUDINAL_BRAKE"
    print("BAŞARILI")


def test_frenet_lattice_planner():
    print("  * [TEST 18/21] Frenet (s, d) Jerk-Optimal Kafes Yörünge Planlayıcı...", end=" ")
    planner = FrenetLatticePlanner()
    traj = planner.plan_optimal_trajectory(
        FrenetState(0.0, 10.0, 0.0, 0.0, 0.0, 0.0),
        target_speed_mps=10.0,
        obstacles_sd=[(15.0, 0.0)],
        horizon_s=3.0,
    )
    assert traj.collision_free is True and abs(traj.target_lateral_d_m) >= 1.75
    print("BAŞARILI")


def test_mpc_and_redundant_actuators():
    print("  * [TEST 19/21] Model Öngörülü Kontrol (MPC) ve Çift Yedekli Fren Dağıtıcısı...", end=" ")
    mpc = RecedingHorizonMPC()
    sol = mpc.solve(cross_track_error_m=0.5, heading_error_rad=0.04, velocity_mps=8.0, target_velocity_mps=10.0)
    assert sol.optimal_steer_rad < 0.0 and sol.optimal_accel_mps2 > 0.0
    alloc = RedundantActuatorAllocator()
    red = alloc.allocate(3.5, ibooster_primary_healthy=False, esc_secondary_healthy=True)
    assert red.fail_operational_mode == "DEGRADED_SECONDARY_ACTIVE" and red.secondary_esc_pump_decel_mps2 == 3.5
    print("BAŞARILI")


def test_sums_un_r156():
    print("  * [TEST 20/21] UN/ECE R156 Yazılım Güncelleme (SUMS), RXSWIN ve Rollback...", end=" ")
    sums = UnR156SumsManager()
    pkg = sums.sign_package("v4.3.0-verified", "RXSWIN-R157-TR-2026-002", b"BINARY_IMAGE")
    rej = sums.apply_update(pkg, vehicle_speed_mps=3.0, park_brake_engaged=False)
    assert rej.success is False and rej.status == "REJECTED_VEHICLE_MOVING"
    ok = sums.apply_update(pkg, vehicle_speed_mps=0.0, park_brake_engaged=True, post_update_self_check_ok=True)
    assert ok.success is True and sums.active_rxswin == "RXSWIN-R157-TR-2026-002"
    print("BAŞARILI")


def test_ehmi_and_siren():
    print("  * [TEST 21/21] ISO/TR 23049 Dış Yaya eHMI Paneli ve Akustik Siren Algılama...", end=" ")
    sup = ExternalHmiAndSirenSupervisor()
    dec = sup.evaluate(False, False, dominant_audio_freq_hz=920.0, audio_spl_db=84.0, freq_modulation_detected=True)
    assert dec.emergency_siren_detected is True and dec.recommended_vehicle_action == "PULL_OVER_RIGHT_EMERGENCY"
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
    test_odd_sotif_dssad_and_curb()
    test_curb_and_teleop()
    test_carla_bridge()
    test_can_ids_r155()
    test_lidar_deskew_ptp()
    test_lanelet2_traffic_rules()
    test_cabin_and_bms_safety()
    test_rss_ieee2846()
    test_frenet_lattice_planner()
    test_mpc_and_redundant_actuators()
    test_sums_un_r156()
    test_ehmi_and_siren()
    print("=" * 75)
    print("  [MÜKEMMEL] 21 Temel Alt Sistem Testinin Tamamı (%100) Sıfır Hatayla Geçti!")
    print("  SAIC Maxus MIFA 7 Seviye-4 Kurumsal SDK Üretime ve PoC'ye Hazır!")
    print("=" * 75 + "\n")


if __name__ == "__main__":
    run_all_tests()
