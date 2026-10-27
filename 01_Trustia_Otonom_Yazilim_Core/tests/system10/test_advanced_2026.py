"""Comprehensive System 10 Unit & Integration Tests.

Validates:
1. V2X (Vehicle-to-Everything) Communication & GLOSA Engine
2. 5-Second Multimodal Trajectory Prediction & TTC Engine
3. Level-4 Teleoperation & Remote Dispatch Bridge
4. Adverse Weather & Dynamic Sensor Weighting Compensation
"""

import pytest
import time
import math

from v2x.v2x_engine import (
    V2XEngine,
    TrafficLightState,
    EmergencyVehicleAlert,
    SignalPhase
)
from perception.prediction import (
    TrajectoryPredictionEngine,
    AgentType,
    IntentionType
)
from control.teleoperation import (
    TeleoperationBridge,
    TeleopCommand,
    TeleopMode
)
from perception.weather_filter import (
    AdverseWeatherFilter,
    WeatherCondition
)


# ============================================================================
# 1. V2X COMMUNICATION & GLOSA TESTS
# ============================================================================

def test_v2x_spat_message_processing():
    engine = V2XEngine(vehicle_id="TRUSTIA-EGO-01")
    phase = engine.process_spat_message(
        intersection_id="INT-LEVENT-04",
        phase_id=1,
        state_str="GREEN",
        time_to_change=12.5
    )
    assert phase.state == TrafficLightState.GREEN
    assert phase.time_to_change_sec == 12.5
    assert engine.rx_count == 1


def test_v2x_glosa_green_light_cruise():
    engine = V2XEngine()
    phase = SignalPhase("INT-01", 1, TrafficLightState.GREEN, 10.0)
    # 50m to light, current speed 10 m/s -> needs 5s -> well within 10s green
    speed, action = engine.calculate_glosa_speed(distance_to_light_m=50.0, phase=phase, current_speed_mps=10.0)
    assert action == "CRUISE_GREEN"
    assert speed == 10.0


def test_v2x_glosa_red_light_smooth_arrival():
    engine = V2XEngine()
    phase = SignalPhase("INT-01", 1, TrafficLightState.RED, 5.0)
    # 30m to light, red for 5 more seconds -> optimal speed 30 / (5+1) = 5 m/s
    speed, action = engine.calculate_glosa_speed(distance_to_light_m=30.0, phase=phase, current_speed_mps=10.0)
    assert action == "GLOSA_SMOOTH_ARRIVAL"
    assert math.isclose(speed, 5.0, rel_tol=1e-2)


def test_v2x_v2v_bsm_eebl_hazard_detection():
    engine = V2XEngine()
    # Car in front hard braking at (0, 25)
    engine.process_bsm(
        sender_id="VEH-FRONT-99",
        x=0.0,
        y=25.0,
        vx=0.0,
        vy=0.0,
        brake_active=True,
        hard_braking=True
    )
    risk_detected, hazard_id = engine.check_eebl_risk(my_x=0.0, my_y=0.0, my_heading=0.0)
    assert risk_detected is True
    assert hazard_id == "VEH-FRONT-99"


def test_v2x_emergency_vehicle_alert():
    engine = V2XEngine()
    eva = EmergencyVehicleAlert(
        vehicle_id="AMB-112-IST",
        vehicle_type="AMBULANCE",
        position_x=10.0,
        position_y=50.0,
        heading_deg=180.0,
        speed_mps=20.0,
        siren_active=True,
        timestamp=time.time()
    )
    advisory = engine.process_eva(eva)
    assert advisory["status"] == "YIELD_REQUIRED"
    assert advisory["recommended_action"] == "PULL_OVER_RIGHT"


def test_v2x_outbound_bsm_generation():
    engine = V2XEngine(vehicle_id="TRUSTIA-EGO")
    msg = engine.generate_bsm(my_x=12.0, my_y=45.0, my_vx=8.0, my_vy=0.0, brake_active=False)
    assert msg.sender_id == "TRUSTIA-EGO"
    assert msg.payload["vx"] == 8.0
    assert engine.tx_count == 1


# ============================================================================
# 2. 5-SECOND TRAJECTORY PREDICTION TESTS
# ============================================================================

def test_pedestrian_crossing_prediction():
    predictor = TrajectoryPredictionEngine(horizon_sec=5.0, dt=0.5)
    # Pedestrian walking laterally across road (vx=0, vy=1.2 m/s, heading=pi/2)
    trajs = predictor.predict_agent_trajectory(
        agent_id="PED-01",
        agent_type_str="PEDESTRIAN",
        x=5.0,
        y=0.0,
        vx=0.0,
        vy=1.2,
        heading_rad=math.pi / 2,
        ego_x=5.0,
        ego_y=-10.0,
        ego_vx=0.0,
        ego_vy=5.0
    )
    assert len(trajs) >= 2
    crossing_traj = next(t for t in trajs if t.intention == IntentionType.CROSSING)
    assert crossing_traj.probability == 0.75
    assert len(crossing_traj.waypoints) == 10
    # At t=5.0s, y = 1.2 * 5.0 = 6.0m
    assert math.isclose(crossing_traj.waypoints[-1].y, 6.0, rel_tol=1e-2)


def test_vehicle_lane_keep_and_cutin_prediction():
    predictor = TrajectoryPredictionEngine(horizon_sec=5.0, dt=0.5)
    trajs = predictor.predict_agent_trajectory(
        agent_id="VEH-LEAD",
        agent_type_str="VEHICLE",
        x=0.0,
        y=30.0,
        vx=0.0,
        vy=10.0,
        heading_rad=0.0
    )
    assert len(trajs) >= 2
    lane_keep = next(t for t in trajs if t.intention == IntentionType.LANE_KEEP)
    assert lane_keep.probability == 0.85
    # Waypoint at step 10 (t=5s): y = 30 + 10*5 = 80m
    assert math.isclose(lane_keep.waypoints[-1].y, 80.0, rel_tol=1e-2)


def test_trajectory_critical_collision_risk():
    predictor = TrajectoryPredictionEngine()
    # Obstacle is on imminent collision path with ego vehicle
    trajs = predictor.predict_agent_trajectory(
        agent_id="PED-RISK",
        agent_type_str="PEDESTRIAN",
        x=0.0,
        y=3.0,
        vx=0.0,
        vy=0.0,
        heading_rad=0.0,
        ego_x=0.0,
        ego_y=1.0,
        ego_vx=0.0,
        ego_vy=0.5
    )
    critical_traj = trajs[0]
    assert critical_traj.collision_risk_score == 1.0


# ============================================================================
# 3. TELEOPERATION & REMOTE INTERVENTION TESTS
# ============================================================================

def test_teleop_heartbeat_and_latency():
    bridge = TeleoperationBridge(heartbeat_timeout_sec=0.300)
    client_ts = time.time() - 0.025  # 25ms latency
    state = bridge.handle_operator_heartbeat(operator_id="OP-ISTANBUL-C2", client_time=client_ts)
    assert state.operator_connected is True
    assert state.latency_ms >= 20.0
    assert state.link_quality_pct > 90.0


def test_teleop_watchdog_timeout_failsafe():
    bridge = TeleoperationBridge(heartbeat_timeout_sec=0.100)
    # Simulate old heartbeat from 500ms ago
    bridge.state.last_heartbeat_timestamp = time.time() - 0.500
    
    cmd = TeleopCommand(
        mode=TeleopMode.DIRECT_DRIVE,
        operator_id="OP-01",
        timestamp=time.time(),
        throttle_pct=50.0
    )
    steer, throttle, brake, msg = bridge.process_command(cmd, current_speed_mps=5.0, closest_obstacle_dist_m=20.0)
    assert throttle == 0.0
    assert brake == 100.0
    assert "TIMEOUT_FAILSAFE_BRAKE" in msg


def test_teleop_remote_estop():
    bridge = TeleoperationBridge()
    bridge.handle_operator_heartbeat("OP-01", time.time())
    
    cmd = TeleopCommand(
        mode=TeleopMode.REMOTE_ESTOP,
        operator_id="OP-01",
        timestamp=time.time()
    )
    steer, throttle, brake, msg = bridge.process_command(cmd, current_speed_mps=8.0, closest_obstacle_dist_m=15.0)
    assert brake == 100.0
    assert "OPERATOR_EMERGENCY_STOP" in msg


def test_teleop_obstacle_proximity_safety_override():
    bridge = TeleoperationBridge()
    bridge.handle_operator_heartbeat("OP-01", time.time())
    
    # Operator tries to accelerate directly into a wall at 1.2m
    cmd = TeleopCommand(
        mode=TeleopMode.DIRECT_DRIVE,
        operator_id="OP-01",
        timestamp=time.time(),
        throttle_pct=80.0
    )
    steer, throttle, brake, msg = bridge.process_command(cmd, current_speed_mps=2.0, closest_obstacle_dist_m=1.2)
    assert throttle == 0.0
    assert brake == 100.0
    assert "OBSTACLE_PROXIMITY_BRAKE_OVERRIDE" in msg


def test_teleop_waypoint_guidance():
    bridge = TeleoperationBridge()
    bridge.handle_operator_heartbeat("OP-01", time.time())
    
    waypoints = [(10.0, 20.0), (15.0, 30.0), (20.0, 40.0)]
    cmd = TeleopCommand(
        mode=TeleopMode.WAYPOINT_GUIDANCE,
        operator_id="OP-01",
        timestamp=time.time(),
        guidance_waypoints=waypoints
    )
    steer, throttle, brake, msg = bridge.process_command(cmd, current_speed_mps=4.0, closest_obstacle_dist_m=10.0)
    assert len(bridge.guidance_path) == 3
    assert "FOLLOWING_GUIDANCE_PATH_3_POINTS" in msg


# ============================================================================
# 4. ADVERSE WEATHER & SENSOR DEGRADATION TESTS
# ============================================================================

def test_weather_clear_nominal():
    filter_engine = AdverseWeatherFilter(base_speed_limit_mps=13.88)
    advisory, weights = filter_engine.assess_weather(
        visibility_distance_m=150.0,
        ambient_rain_rate_mm_hr=0.0,
        camera_lens_clarity_pct=98.0,
        lidar_point_attenuation_pct=5.0
    )
    assert advisory.condition == WeatherCondition.CLEAR
    assert weights.camera_weight == 0.40
    assert weights.confidence_score >= 0.95
    assert advisory.following_distance_multiplier == 1.0


def test_weather_dense_fog_radar_primary():
    filter_engine = AdverseWeatherFilter()
    advisory, weights = filter_engine.assess_weather(
        visibility_distance_m=20.0,  # Thick Istanbul fog
        ambient_rain_rate_mm_hr=0.0,
        camera_lens_clarity_pct=90.0,
        lidar_point_attenuation_pct=75.0
    )
    assert advisory.condition == WeatherCondition.DENSE_FOG
    assert weights.radar_weight > weights.camera_weight
    assert advisory.following_distance_multiplier == 2.0
    assert advisory.recommended_max_speed_mps <= 7.0


def test_weather_heavy_rain_hydroplaning_prevention():
    filter_engine = AdverseWeatherFilter()
    advisory, weights = filter_engine.assess_weather(
        visibility_distance_m=60.0,
        ambient_rain_rate_mm_hr=35.0,  # Torrential downpour
        camera_lens_clarity_pct=85.0,
        lidar_point_attenuation_pct=20.0
    )
    assert advisory.condition == WeatherCondition.HEAVY_RAIN
    assert "HYDROPLANING_PREVENTION" in advisory.active_warning
    assert advisory.following_distance_multiplier == 1.7


def test_weather_mud_occluded_lens():
    filter_engine = AdverseWeatherFilter()
    advisory, weights = filter_engine.assess_weather(
        visibility_distance_m=100.0,
        ambient_rain_rate_mm_hr=0.0,
        camera_lens_clarity_pct=25.0,  # Mud splash on camera
        lidar_point_attenuation_pct=10.0
    )
    assert advisory.condition == WeatherCondition.MUD_OCCLUDED
    assert weights.camera_weight == 0.10
    assert weights.radar_weight == 0.40
    assert "CAMERA_LENS_OCCLUDED" in advisory.active_warning


def test_v2x_accelerate_for_green():
    engine = V2XEngine()
    phase = SignalPhase("INT-02", 1, TrafficLightState.GREEN, 4.0)
    # 40m away, at current 8 m/s takes 5s -> will miss green. Need 10 m/s to arrive in 4s.
    speed, action = engine.calculate_glosa_speed(distance_to_light_m=40.0, phase=phase, current_speed_mps=8.0, speed_limit_mps=13.88)
    assert action == "ACCELERATE_FOR_GREEN"
    assert math.isclose(speed, 10.0, rel_tol=1e-2)


def test_cyclist_prediction_envelope():
    predictor = TrajectoryPredictionEngine(horizon_sec=5.0, dt=0.5)
    trajs = predictor.predict_agent_trajectory(
        agent_id="BIKE-01",
        agent_type_str="BICYCLE",
        x=2.0,
        y=10.0,
        vx=0.0,
        vy=4.0,
        heading_rad=0.0
    )
    assert len(trajs) >= 1
    assert trajs[0].waypoints[-1].y == 30.0  # 10 + 4*5

    # CARLA Bridge, Curb Detection, ODD, SOTIF & DSSAD Entegrasyon Doğrulaması
    from integration.carla_bridge import TrustiaCarlaBridge
    from perception.ground import CurbAndRoadBoundaryDetector
    from perception.types import PointCloud, Point3D
    from security.odd_sotif_dssad import (
        OddDomainMonitor,
        Iso21448SotifSupervisor,
        UnR157DssadBlackbox,
        SimulationVsFieldProfile,
    )

    carla_br = TrustiaCarlaBridge()
    assert carla_br.connect() is True
    ctrl = carla_br.convert_to_carla_control(target_steer_deg=7.0, target_accel_mps2=1.5)
    snap = carla_br.step_simulation(ctrl)
    assert snap.lidar_points_per_sec == 2_600_000
    override, lat_ms = carla_br.check_human_override(driver_steering_torque_nm=2.2, driver_brake_pedal_pressed=False)
    assert override is True and lat_ms <= 5.0

    # Kaldırım taşı ve yol sınırı algılama
    import numpy as np
    curb_det = CurbAndRoadBoundaryDetector()
    pts = np.array([
        [5.0, 0.0, 0.0, 1.0],
        [5.0, 2.8, 0.15, 1.0],
        [8.0, 2.8, 0.16, 1.0],
        [5.0, -2.8, 0.15, 1.0],
        [8.0, -2.8, 0.14, 1.0],
    ], dtype=float)
    curb_res = curb_det.detect_road_boundaries(PointCloud(pts))
    assert curb_res.valid_corridor is True
    assert abs(curb_res.corridor_width_m - 5.6) < 0.2

    # ODD, SOTIF, DSSAD ve Simülasyon-Saha Tolerans Profili
    odd = OddDomainMonitor()
    assert odd.evaluate(100.0, 100.0, 40.0).within_odd is True
    assert odd.evaluate(9999.0, 9999.0, 40.0).target_decel_mps2 == -1.5

    sotif = Iso21448SotifSupervisor()
    assert sotif.evaluate_sotif(0.45, False).phantom_brake_prevented is True

    dssad = UnR157DssadBlackbox()
    dssad.log_event("L4_ENGAGE", "AUTONOMOUS_L4", 40.0, 1.2, 0.0)
    dssad.log_event("MRM_PULLOVER", "AUTONOMOUS_L4", 35.0, 3.0, -1.5)
    assert dssad.verify_chain_integrity() is True

    prof = SimulationVsFieldProfile()
    tol = prof.compute_field_tolerances(road_friction_mu=0.85, can_bus_load_pct=35.0)
    assert tol["nominal_mrm_pullover_decel_mps2"] == 1.5
    assert tol["nominal_self_check_ms"] == 20.0
    assert tol["nominal_watchdog_timeout_ms"] == 50.0
    assert tol["nominal_human_override_ms"] == 5.0

    # UN R155 CAN-FD IDPS, IEEE 1588 PTP Deskewing, Lanelet2 Rules & Robotaxi Cabin/BMS Safety
    from security.can_ids_r155 import UnR155CanBusIds
    from perception.lidar_deskew_ptp import LidarMotionDeskewer, RawTimedPoint3D
    from planning.lanelet2_rules import Lanelet2TrafficRuleEngine, LaneletSegment
    from command.cabin_bms_safety import (
        RobotaxiCabinAndBmsSupervisor,
        CabinDoorSeatStatus,
        BatteryThermalState,
    )

    can_ids = UnR155CanBusIds()
    ev_ok = can_ids.inspect_frame(0x120, b"\x00" * 8, timestamp_ms=10.0, rolling_counter=1)
    assert ev_ok.accepted is True
    ev_spoof = can_ids.inspect_frame(0x666, b"\x00" * 8, timestamp_ms=12.0, rolling_counter=1)
    assert ev_spoof.accepted is False and ev_spoof.threat_type == "UNAUTHORIZED_ID"
    ev_dos = can_ids.inspect_frame(0x120, b"\x00" * 8, timestamp_ms=11.0, rolling_counter=2)
    assert ev_dos.accepted is False and ev_dos.threat_type == "DOS_FLOODING"

    deskew = LidarMotionDeskewer()
    ptp_st = deskew.evaluate_ptp_sync("GM-CLOCK-01", offset_us=35.0, jitter_us=12.0)
    assert ptp_st.synchronized is True and ptp_st.sotif_degraded is False
    corrected_pts = deskew.deskew_scan(
        [RawTimedPoint3D(10.0, 0.0, 0.5, relative_time_s=0.0)],
        vx_mps=10.0,
        vy_mps=0.0,
        yaw_rate_rad_s=0.0,
        sweep_duration_s=0.050,
    )
    assert math.isclose(corrected_pts[0][0], 9.5, rel_tol=1e-3)

    l2 = Lanelet2TrafficRuleEngine()
    l2.register_lanelet(LaneletSegment("LL-101", 50.0, True, False, has_crosswalk=True, is_intersection=True))
    row_ped = l2.evaluate_rules("LL-101", ego_speed_mps=8.0, pedestrian_on_crosswalk=True, crosswalk_distance_m=15.0)
    assert row_ped.behavior_command == "STOP_FOR_PEDESTRIAN" and row_ped.target_speed_mps == 0.0

    cabin_sup = RobotaxiCabinAndBmsSupervisor()
    c_open = cabin_sup.evaluate(
        CabinDoorSeatStatus(all_doors_closed=False, trunk_closed=True, passenger_seated=True, seatbelt_fastened=True),
        BatteryThermalState(soc_percent=82.0, pack_temp_c=31.0, estimated_range_km=340.0),
        vehicle_speed_mps=0.0,
    )
    assert c_open.dispatch_allowed is False and c_open.motion_inhibit_brake_hold is True
    c_ready = cabin_sup.evaluate(
        CabinDoorSeatStatus(all_doors_closed=True, trunk_closed=True, passenger_seated=True, seatbelt_fastened=True),
        BatteryThermalState(soc_percent=82.0, pack_temp_c=31.0, estimated_range_km=340.0),
        vehicle_speed_mps=5.0,
    )
    assert c_ready.dispatch_allowed is True and c_ready.fleet_state_recommendation == "IN_RIDE"

    # IEEE 2846 RSS, Frenet Lattice, MPC & Redundant Actuator, UN R156 SUMS, eHMI & Siren
    from security.rss_ieee2846 import ResponsibilitySensitiveSafety
    from planning.frenet_lattice_planner import FrenetLatticePlanner, FrenetState
    from control.mpc_redundant_control import RecedingHorizonMPC, RedundantActuatorAllocator
    from security.sums_un_r156 import UnR156SumsManager
    from v2x.ehmi_siren_detector import ExternalHmiAndSirenSupervisor

    rss = ResponsibilitySensitiveSafety()
    verdict_unsafe = rss.evaluate_pair(ego_vel_mps=15.0, front_vel_mps=5.0, actual_longitudinal_gap_m=4.0, actual_lateral_gap_m=0.1)
    assert verdict_unsafe.longitudinal_safe is False and verdict_unsafe.proper_response == "RSS_LONGITUDINAL_BRAKE"

    frenet = FrenetLatticePlanner()
    f_traj = frenet.plan_optimal_trajectory(
        FrenetState(s=0.0, ds=10.0, dds=0.0, d=0.0, dd=0.0, ddd=0.0),
        target_speed_mps=10.0,
        obstacles_sd=[(15.0, 0.0)],
        horizon_s=3.0,
    )
    assert f_traj.collision_free is True and abs(f_traj.target_lateral_d_m) >= 0.8

    mpc = RecedingHorizonMPC()
    sol = mpc.solve(cross_track_error_m=0.6, heading_error_rad=0.05, velocity_mps=8.0, target_velocity_mps=10.0)
    assert sol.optimal_steer_rad < 0.0 and sol.optimal_accel_mps2 > 0.0

    alloc = RedundantActuatorAllocator()
    red = alloc.allocate(requested_decel_mps2=3.5, ibooster_primary_healthy=False, esc_secondary_healthy=True)
    assert red.fail_operational_mode == "DEGRADED_SECONDARY_ACTIVE" and red.secondary_esc_pump_decel_mps2 == 3.5

    sums = UnR156SumsManager()
    pkg = sums.sign_package("v4.3.0-verified", "RXSWIN-R157-TR-2026-002", b"OTA_BINARY_PAYLOAD")
    rej_moving = sums.apply_update(pkg, vehicle_speed_mps=5.0, park_brake_engaged=False)
    assert rej_moving.success is False and rej_moving.status == "REJECTED_VEHICLE_MOVING"
    ok_upd = sums.apply_update(pkg, vehicle_speed_mps=0.0, park_brake_engaged=True, post_update_self_check_ok=True)
    assert ok_upd.success is True and sums.active_rxswin == "RXSWIN-R157-TR-2026-002"

    ehmi = ExternalHmiAndSirenSupervisor()
    siren_dec = ehmi.evaluate(yielding_to_pedestrian=False, mrm_active=False, dominant_audio_freq_hz=950.0, audio_spl_db=85.0, freq_modulation_detected=True)
    assert siren_dec.emergency_siren_detected is True and siren_dec.recommended_vehicle_action == "PULL_OVER_RIGHT_EMERGENCY"



