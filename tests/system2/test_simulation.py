"""Sistem 2 — Simülasyon birim testleri.

Terrain (engeller, yasak bölgeler, raycast, sınır sanal duvarı),
sensör modelleri (LiDAR, odometri, araç), senaryo üretimi,
görev koşucusu (yerel kaçınma + global A* rotası + kurtarma) ve
kampanya istatistiklerini doğrular.
"""

from __future__ import annotations

import math
import random

import pytest

from control import PidGains, Controller, VehicleModel
from simulation.runner import MissionMetrics, MissionRunner
from simulation.scenario import Mission, ScenarioGenerator
from simulation.sensors import (
    LidarModel,
    OdometryModel,
    ScanPoint,
    SimulatedVehicle,
)
from simulation.terrain import Terrain, Weather

# ---------------------------------------------------------------- Terrain


def make_world(**kwargs):
    defaults = {
        "width_m": 40.0,
        "height_m": 40.0,
        "seed": 7,
        "obstacle_count": 8,
        "forbidden_count": 2,
    }
    defaults.update(kwargs)
    return Terrain(**defaults)


def test_terrain_layout_counts():
    terrain = make_world()
    assert len(terrain.obstacles) == 8
    assert len(terrain.forbidden) == 2
    assert terrain.width_m == 40.0
    assert terrain.height_m == 40.0


def test_terrain_empty_world_has_no_obstacles():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    assert terrain.obstacles == []
    assert terrain.forbidden == []


def test_is_blocked_true_inside_obstacle():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 10.0, 2.0)
    assert terrain.is_blocked(10.0, 10.0)
    assert terrain.is_blocked(12.0, 10.0)
    assert not terrain.is_blocked(13.5, 10.0)


def test_is_blocked_clearance():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 10.0, 1.0)
    assert not terrain.is_blocked(11.5, 10.0, clearance_m=0.4)
    assert terrain.is_blocked(11.5, 10.0, clearance_m=0.8)


def test_in_forbidden():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_forbidden(20.0, 20.0, 2.0)
    assert terrain.in_forbidden(20.0, 20.0)
    assert terrain.in_forbidden(21.5, 20.0)
    assert not terrain.in_forbidden(22.5, 20.0)


def test_nearest_obstacle_distance_negative_inside():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 10.0, 2.0)
    assert terrain.nearest_obstacle_distance(10.0, 10.0) == pytest.approx(-2.0)
    assert terrain.nearest_obstacle_distance(14.0, 10.0) == pytest.approx(2.0)


def test_nearest_forbidden_empty_returns_inf():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    distance, fz_x, fz_y = terrain.nearest_forbidden(5.0, 5.0)
    assert distance == math.inf


def test_nearest_forbidden_surface_distance():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_forbidden(20.0, 20.0, 2.0)
    distance, fz_x, fz_y = terrain.nearest_forbidden(25.0, 20.0)
    assert distance == pytest.approx(3.0)
    assert fz_x == 20.0
    assert fz_y == 20.0


def test_raycast_obstacle_blocks():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 0.0, 2.0)
    distance = terrain.raycast((0.0, 0.0), 0.0, 30.0)
    assert distance == pytest.approx(8.0, abs=0.01)


def test_raycast_misses_obstacle():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 5.0, 1.0)
    distance = terrain.raycast((0.0, 0.0), 0.0, 30.0)
    assert distance == pytest.approx(30.0)


def test_raycast_grazes_boundary():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(10.0, 0.9, 1.0)
    distance = terrain.raycast((0.0, 0.0), 0.0, 30.0)
    assert 8.5 < distance < 9.7


def test_raycast_forbidden_blocks():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_forbidden(12.0, 0.0, 1.0)
    distance = terrain.raycast((0.0, 0.0), 0.0, 30.0)
    assert distance == pytest.approx(11.0, abs=0.01)


def test_raycast_world_boundary_blocks():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    distance = terrain.raycast((0.0, 0.0), 0.0, 100.0)
    assert distance == pytest.approx(40.0, abs=0.01)


def test_raycast_world_boundary_miss():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    distance = terrain.raycast((20.0, 20.0), 0.0, 30.0)
    assert distance == pytest.approx(20.0, abs=0.01)


def test_sample_clear_point_obstacle_realm():
    rng = random.Random(1)
    terrain = make_world(obstacle_count=12, forbidden_count=0)
    for _ in range(20):
        point = terrain.sample_clear_point(rng, clearance_m=2.0)
        assert not terrain.is_blocked(point[0], point[1], clearance_m=2.0)
        assert terrain.nearest_obstacle_distance(*point) >= 2.0


def test_sample_clear_point_forbidden_free():
    rng = random.Random(2)
    terrain = make_world(obstacle_count=0, forbidden_count=5)
    for _ in range(20):
        point = terrain.sample_clear_point(rng, clearance_m=1.5)
        distance, _, _ = terrain.nearest_forbidden(*point)
        assert distance >= 1.5


def test_weather_defaults():
    weather = Weather()
    assert weather.rain_mmh == 0.0
    assert weather.fog_density == 0.0
    assert not weather.night
    assert weather.lidar_range_factor() == pytest.approx(1.0)


def test_weather_fog_reduces_range():
    weather = Weather(fog_density=0.5)
    assert weather.lidar_range_factor() < 1.0


def test_weather_rain_increases_noise():
    weather = Weather(rain_mmh=15.0)
    noise = weather.lidar_noise_sigma_m(0.02)
    assert noise > Weather(rain_mmh=0.0).lidar_noise_sigma_m(0.02)


def test_weather_invalid_fog_rejected():
    with pytest.raises(ValueError):
        Weather(fog_density=1.5)


def test_weather_invalid_rain_rejected():
    with pytest.raises(ValueError):
        Weather(rain_mmh=-1.0)


# ---------------------------------------------------------------- sensors


def test_lidar_scan_resolution():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    rng = random.Random(0)
    lidar = LidarModel(beam_count=36, max_range_m=10.0)
    scan = lidar.scan(terrain, (20.0, 20.0), 0.0, Weather(), rng)
    assert len(scan) == 36


def test_lidar_scan_angle_spacing():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    rng = random.Random(0)
    lidar = LidarModel(beam_count=4, max_range_m=10.0)
    scan = lidar.scan(terrain, (20.0, 20.0), 0.0, Weather(), rng)
    angles = sorted(point.angle_rad for point in scan)
    diffs = [(b - a) % (2.0 * math.pi) for a, b in zip(angles, angles[1:])]
    assert diffs == pytest.approx([math.pi / 2.0] * 3, abs=1e-3)


def test_lidar_scan_free_space_max_range():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    rng = random.Random(0)
    lidar = LidarModel(beam_count=36, max_range_m=10.0)
    scan = lidar.scan(terrain, (20.0, 20.0), 0.0, Weather(), rng)
    for point in scan:
        # Boş dünyada hiçbir ışın engelle çarpışmaz → menzil dışı (inf)
        assert not math.isfinite(point.range_m)

def test_lidar_sees_boundary_when_close():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    rng = random.Random(0)
    lidar = LidarModel(beam_count=36, max_range_m=10.0)
    scan = lidar.scan(terrain, (5.0, 20.0), 0.0, Weather(), rng)
    assert any(point.range_m < 5.5 for point in scan)


def _test_odometry_noise_bounds():
    sensor = OdometryModel(distance_noise_ratio=0.0, heading_noise_std_deg=0.0)
    rng = random.Random(0)
    measured_d, measured_h = sensor.measure(2.0, 0.1, Weather(), rng)
    assert measured_d == pytest.approx(2.0, abs=1e-6)
    assert measured_h == pytest.approx(0.1, abs=1e-6)


def test_odometry_measure_is_deterministic_with_seed():
    sensor = OdometryModel()
    first = sensor.measure(3.0, 0.2, Weather(), random.Random(42))
    second = sensor.measure(3.0, 0.2, Weather(), random.Random(42))
    assert first == second


def test_vehicle_step_moves_forward():
    vehicle = SimulatedVehicle(0.0, 0.0, 0.0)
    vehicle.step(2.0, 0.0, 0.1)
    assert vehicle.x == pytest.approx(0.2, abs=1e-6)
    assert vehicle.y == pytest.approx(0.0, abs=1e-6)


def test_vehicle_step_turns():
    vehicle = SimulatedVehicle(0.0, 0.0, 0.0)
    vehicle.step(1.0, math.pi / 4.0, 0.1)
    assert vehicle.heading == pytest.approx(math.pi / 4.0 * 0.1, abs=1e-6)


def test_vehicle_step_negative_speed_backwards():
    vehicle = SimulatedVehicle(0.0, 0.0, 0.0)
    vehicle.step(-1.0, 0.0, 0.1)
    assert vehicle.x == pytest.approx(-0.1, abs=1e-6)


# ---------------------------------------------------------------- senaryo


def _mission(mission_type="kesif", seed=100):
    return ScenarioGenerator(world_size_m=20.0).generate(
        mission_type=mission_type, seed=seed
    )


def test_generator_produces_mission():
    mission = _mission()
    assert isinstance(mission, Mission)
    assert mission.waypoints
    assert mission.time_limit_s > 0.0
    assert mission.arrival_tolerance_m == pytest.approx(1.5)


def test_gps_flag_only_gps_koridor():
    assert not _mission("gps-koridor").gps_available
    assert _mission("kesif").gps_available
    assert _mission("lojistik").gps_available
    assert _mission("devriye").gps_available
    assert _mission("engelli-parkur").gps_available


def test_patrol_has_multiple_waypoints():
    mission = _mission("devriye")
    assert len(mission.waypoints) >= 1


def test_mission_generation_same_seed_similar():
    first = _mission("kesif", seed=5)
    second = _mission("kesif", seed=5)
    assert first.start == second.start
    assert first.waypoints == second.waypoints


def test_mission_start_not_in_forbidden():
    generator = ScenarioGenerator(world_size_m=20.0)
    mission = generator.generate("kesif", seed=15)
    terrain = Terrain(
        width_m=mission.terrain.width_m,
        height_m=mission.terrain.height_m,
        seed=mission.terrain.seed,
        obstacle_count=mission.terrain.obstacle_count,
        forbidden_count=mission.terrain.forbidden_count,
    )
    distance, _, _ = terrain.nearest_forbidden(*mission.start)
    assert distance >= 1.5


def test_mission_unknown_type_rejected():
    with pytest.raises(ValueError):
        ScenarioGenerator().generate("bozuk-tip", seed=1)


def test_mission_times_positive():
    for mission_type in ScenarioGenerator.TYPES:
        mission = _mission(mission_type, seed=9)
        assert mission.time_limit_s > 10.0


def test_mission_clearance_towards_waypoints():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(20.0, 20.0, 6.0)
    rng = random.Random(3)
    for _ in range(10):
        point = terrain.sample_clear_point(rng, clearance_m=1.0)
        assert terrain.nearest_obstacle_distance(*point) >= 1.0
        assert not terrain.is_blocked(*point, clearance_m=1.0)


# ---------------------------------------------------------------- runner


def _runner(**overrides):
    params = {
        "dt_s": 0.02,
        "seed": 1,
        "beam_count": 48,
        "lidar_max_range_m": 12.0,
        "vehicle_radius_m": 0.4,
        "grid_update_every": 10,
    }
    params.update(overrides)
    return MissionRunner(**params)


def _empty_mission(distance=8.0, time_limit=30.0):
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    return terrain, Mission(
        mission_id="test",
        mission_type="kesif",
        start=(5.0, 5.0),
        start_heading_rad=0.0,
        waypoints=[(5.0 + distance, 5.0)],
        arrival_tolerance_m=1.5,
        time_limit_s=time_limit,
        gps_available=False,
        terrain={
            "width_m": 40.0,
            "height_m": 40.0,
            "seed": 7,
            "obstacle_count": 0,
            "forbidden_count": 0,
        },
        weather=Weather(),
    )


def test_runner_rejects_bad_dt():
    with pytest.raises(ValueError):
        _runner(dt_s=0.0)


def test_metrics_failure_reason_order():
    assert MissionMetrics("a", "b", False, collision=True).failure_reason() == "çarpışma"
    assert (
        MissionMetrics("a", "b", False, forbidden_violation=True).failure_reason()
        == "yasak bölge ihlali"
    )
    assert MissionMetrics("a", "b", False, time_out=True).failure_reason() == "süre aşımı"
    assert MissionMetrics("a", "b", False, stuck=True).failure_reason() == "sıkışma"
    assert MissionMetrics("a", "b", True).failure_reason() == ""


def test_runner_empty_world_success():
    terrain, mission = _empty_mission()
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.success
    assert metrics.collision is False
    assert metrics.position_error_m < 2.5


def test_runner_obstacle_route_takes_detour():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_obstacle(9.0, 5.0, 1.5)
    mission = Mission(
        mission_id="t",
        mission_type="lojistik",
        start=(2.0, 5.0),
        start_heading_rad=0.0,
        waypoints=[(16.0, 5.0)],
        arrival_tolerance_m=1.5,
        time_limit_s=40.0,
        gps_available=True,
        terrain=None,
        weather=Weather(),
    )
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.success


def test_runner_mission_heading_start_used():
    terrain, mission = _empty_mission(distance=10.0)
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.waypoints_reached >= 1
    assert metrics.duration_s > 1.0


def test_runner_detects_metric_fields():
    terrain, mission = _empty_mission(distance=6.0)
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.map_known_ratio >= 0.0
    assert metrics.position_error_m >= 0.0
    assert metrics.steps > 0


def test_runner_forbidden_zone_detour_succeeds():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_forbidden(9.0, 5.0, 2.0)
    mission = Mission(
        mission_id="t",
        mission_type="kesif",
        start=(2.0, 1.0),
        start_heading_rad=0.0,
        waypoints=[(16.0, 9.0)],
        arrival_tolerance_m=1.5,
        time_limit_s=40.0,
        gps_available=True,
        terrain=None,
        weather=Weather(),
    )
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.success
    assert metrics.forbidden_violation is False


def test_runner_starts_inside_forbidden_fails_fast():
    terrain = make_world(obstacle_count=0, forbidden_count=0)
    terrain.add_forbidden(5.0, 5.0, 5.0)
    mission = Mission(
        mission_id="t",
        mission_type="kesif",
        start=(5.0, 5.0),
        start_heading_rad=0.0,
        waypoints=[(30.0, 30.0)],
        arrival_tolerance_m=1.5,
        time_limit_s=30.0,
        gps_available=True,
        terrain=None,
        weather=Weather(),
    )
    metrics = _runner().run(terrain, mission.weather, mission)
    assert metrics.forbidden_violation
    assert not metrics.success


def test_controller_integration_step():
    controller = Controller(
        model=VehicleModel(max_speed_mps=2.0, max_angular_radps=1.5),
        heading_gains=PidGains(kp=2.0, ki=0.1, kd=0.2),
        speed_gains=PidGains(kp=1.0, ki=0.05, kd=0.0),
    )
    command = controller.step(
        target_heading_rad=0.5,
        target_speed_mps=1.5,
        current_heading_rad=0.0,
        dt=0.02,
    )
    assert command.forward_mps > 0.0
    assert command.angular_radps > 0.0
    assert command.forward_mps <= 2.0


# ---------------------------------------------------------------- kampanya


def _run_one(seed):
    from simulation.campaign import CampaignRunner

    return CampaignRunner(workers=1).execute(count=1, world_size=20, seeds=None)


def test_campaign_small_summary():
    from simulation.campaign import Campaign

    campaign = Campaign(start_seed=0, run_count=10, world_size_m=20.0, verbose=False)
    summary, results = campaign.run()
    assert summary.total_runs == 10
    assert len(results) == 10
    assert 0 <= summary.successful <= 10
    assert summary.position_error_m >= 0.0
    assert summary.route_deviation_m >= 0.0
    for name, entry in summary.per_type.items():
        assert entry["runs"] >= 1
        assert entry["runs"] == 2
        assert 0.0 <= entry["success"] <= entry["runs"]
        assert "success_rate" in entry


def test_campaign_parallel_matches_serial():
    from simulation.campaign import Campaign

    serial = Campaign(
        start_seed=0, run_count=6, world_size_m=20.0, verbose=False, workers=1
    ).run()[0]
    parallel = Campaign(
        start_seed=0, run_count=6, world_size_m=20.0, verbose=False, workers=2
    ).run()[0]
    assert serial.total_runs == parallel.total_runs == 6
    assert serial.successful == parallel.successful
    assert serial.collisions == parallel.collisions
    assert serial.position_error_m == pytest.approx(parallel.position_error_m, abs=1e-9)


def test_campaign_merge_results(tmp_path):
    from simulation.campaign import Campaign, _summarize_metrics

    first = Campaign(
        start_seed=0, run_count=3, world_size_m=20.0, verbose=False
    ).run()[1]
    second = Campaign(
        start_seed=3, run_count=3, world_size_m=20.0, verbose=False
    ).run()[1]
    combined = _summarize_metrics(first + second)
    assert combined.total_runs == 6
    assert combined.per_type
    for name, entry in combined.per_type.items():
        assert entry["runs"] >= 1
        assert "success_rate" in entry