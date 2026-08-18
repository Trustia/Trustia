"""
TRUSTIA Simülasyon Dünyası — Görev koşucusu ve metrik toplama.

Otonomi zinciri entegrasyonu (Sistem 1 modülleri gerçek kullanımda):
  * Algı      : LiDAR taraması → engel tespiti (perception)
  * SLAM      : odometri entegrasyonu + işgal haritası (slam)
  * Planlama  : yerel kaçınma + rota takibi (planning)
  * Kontrol   : hız/açısal hız komutları (control)

Metrikler (PLAN 5.2): görev başarı oranı, çarpışma sayısı,
GPS'siz konum hatası, rota sapması, engel tepki süresi.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from control import Controller, DriveCommand, PidGains, VehicleModel
from core.api import TelemetryFrame
from core.errors import PlanningError
from perception import Clusterer, ObstacleDetector, PointCloudFilter
from planning import AStarPlanner, GridMap, LocalAvoidance
from slam import OdometryIntegrator, OdometryMeasurement, Pose2D
from simulation.scenario import Mission
from simulation.sensors import LidarModel, OdometryModel, SimulatedVehicle, ScanPoint
from simulation.terrain import Terrain, Weather


@dataclass
class MissionMetrics:
    """Tek görev koşusunun ölçülen metrikleri."""

    mission_id: str
    mission_type: str
    success: bool
    collision: bool = False
    forbidden_violation: bool = False
    time_out: bool = False
    out_of_bounds: bool = False
    stuck: bool = False
    stuck_recoveries: int = 0
    steps: int = 0
    duration_s: float = 0.0
    waypoints_reached: int = 0
    position_error_m: float = 0.0        # GPS'siz: odometri/gerçek sapma (ort)
    final_position_error_m: float = 0.0  # görev sonundaki sapma
    route_deviation_m: float = 0.0       # rota çizgisine dikey sapma (ort)
    reaction_time_s: float = 0.0         # engel görme → kaçınma (ort)
    max_reaction_time_s: float = 0.0
    min_obstacle_clearance_m: float = math.inf
    map_known_ratio: float = 0.0

    def failure_reason(self) -> str:
        if self.success:
            return ""
        if self.collision:
            return "çarpışma"
        if self.forbidden_violation:
            return "yasak bölge ihlali"
        if self.time_out:
            return "süre aşımı"
        if self.out_of_bounds:
            return "saha dışı"
        if self.stuck:
            return "sıkışma"
        return "adım limiti"


class MissionRunner:
    """Bir görevi simülasyon dünyasında uçtan uca koşar."""

    def __init__(
        self,
        dt_s: float = 0.1,
        seed: int = 0,
        beam_count: int = 48,
        lidar_max_range_m: float = 12.0,
        vehicle_radius_m: float = 0.4,
        grid_update_every: int = 20,
    ) -> None:
        if dt_s <= 0.0:
            raise ValueError(f"zaman adımı pozitif olmalı: {dt_s}")
        self._dt = dt_s
        self._seed = seed
        self._beam_count = beam_count
        self._lidar_max_range = lidar_max_range_m
        self._vehicle_radius = vehicle_radius_m
        self._grid_update_every = max(1, grid_update_every)
        self._rng = random.Random(seed)
        self._lidar = LidarModel(
            beam_count=beam_count,
            max_range_m=lidar_max_range_m,
        )
        self._odometry_sensor = OdometryModel(
            distance_noise_ratio=0.015,
            heading_noise_std_deg=0.6,
        )
        self._detector = ObstacleDetector(
            filter=PointCloudFilter(
                min_range_m=0.3,
                max_range_m=lidar_max_range_m,
            ),
            clusterer=Clusterer(
                angular_resolution_rad=math.radians(360.0 / beam_count),
                gap_scale=1.2,
                min_cluster_points=2,
            ),
            safety_radius_m=0.4,
        )
        self._avoidance = LocalAvoidance(
            avoidance_radius_m=4.0,
            max_turn_deg=60.0,
        )
        self._controller = Controller(
            model=VehicleModel(
                max_speed_mps=2.0,
                max_angular_radps=1.5,
                max_accel_mps2=2.5,
            ),
            heading_gains=PidGains(kp=2.0, ki=0.1, kd=0.2),
            speed_gains=PidGains(kp=1.0, ki=0.05, kd=0.0),
        )

    def run(self, terrain: Terrain, weather: Weather, mission: Mission,
            telemetry_callback=None) -> MissionMetrics:
        """Görevi koşar ve ölçülen metrikleri döndürür.

        telemetry_callback: isteğe bağlı; her adımda bir TelemetryFrame
        alır (komuta merkezi/kaydedici). Yalnızca okur, simülasyon
        durumunu değiştiremez — determinizm korunur.
        """
        # Determinizm: her görev, görev seed'ine bağlı bağımsız gürültü zinciri
        # üretir (koşu sırasından ve kampanya işçisinden bağımsız).
        mission_seed = getattr(mission.terrain, "seed", None)
        self._rng = random.Random(mission_seed if mission_seed is not None else self._seed)
        self._controller.reset()  # PID durumu koşular arası taşınmaz (determinizm)
        vehicle = SimulatedVehicle(
            x_m=mission.start[0],
            y_m=mission.start[1],
            heading_rad=mission.start_heading_rad,
        )
        odometry = OdometryIntegrator(
            Pose2D(x_m=mission.start[0], y_m=mission.start[1],
                   heading_rad=mission.start_heading_rad)
        )
        grid = _make_grid(terrain)
        plan_grid = _make_plan_grid(terrain, self._vehicle_radius)
        planner = AStarPlanner(plan_grid)
        route: List[Tuple[float, float]] = []
        route_index = 0
        planned_waypoint = -1
        replan_every = 100
        next_replan = 0
        steps_limit = int(mission.time_limit_s / self._dt) + 1

        metrics = MissionMetrics(
            mission_id=mission.mission_id,
            mission_type=mission.mission_type,
            success=False,
        )
        waypoint_index = 0
        speed_mps = 1.0
        first_detection_step: Optional[int] = None
        first_avoidance_step: Optional[int] = None
        reaction_samples = 0
        reaction_total = 0.0
        deviation_total = 0.0
        deviation_samples = 0
        error_total = 0.0
        error_samples = 0
        detected_obstacles_prev = 0
        stuck_check_every = 150
        stuck_min_distance = 2.0
        last_progress_check = 0
        last_check_position = (vehicle.x, vehicle.y)
        recovery_until = 0
        recovery_heading = 0.0
        prev_avoid = 0.0
        telemetry_rng = random.Random(
            (mission_seed if mission_seed is not None else self._seed) ^ 0x5DEECE66D
        )

        for step in range(1, steps_limit + 1):
            x, y, heading = vehicle.x, vehicle.y, vehicle.heading

            if terrain.is_blocked(x, y, clearance_m=self._vehicle_radius):
                metrics.collision = True
                break
            if terrain.in_forbidden(x, y):
                metrics.forbidden_violation = True
                break
            if not (0.0 <= x <= terrain.width_m and 0.0 <= y <= terrain.height_m):
                metrics.out_of_bounds = True
                break

            if step - last_progress_check >= stuck_check_every:
                moved = math.hypot(x - last_check_position[0],
                                   y - last_check_position[1])
                if moved < stuck_min_distance:
                    recovery_until = step + 100
                    recovery_heading = prev_avoid
                    metrics.stuck_recoveries += 1
                last_progress_check = step
                last_check_position = (x, y)

            scan = self._lidar.scan(
                terrain, (x, y), heading, weather, self._rng
            )
            obstacles = self._detector.detect(scan, _enu(x, y))
            # Dünya sınırına yapışık kümeler sanal duvardır; yerel
            # kaçınma ve pay (clearance) hesabından çıkarılır. Gerçek
            # engellerin enge girişimi metrikte korunur.
            real_obstacles = []
            for obstacle in obstacles:
                center_x = obstacle.center.east_m
                center_y = obstacle.center.north_m
                edge = min(center_x, center_y,
                           terrain.width_m - center_x, terrain.height_m - center_y)
                if edge < 1.2:
                    continue
                real_obstacles.append(obstacle)
            detected = len(real_obstacles)
            if detected > 0 and first_detection_step is None:
                first_detection_step = step
            if detected > 0 and detected_obstacles_prev == 0:
                first_detection_step = first_detection_step or step

            obstacle_tuples = [
                (o.center.east_m - x, o.center.north_m - y, o.radius_m)
                for o in real_obstacles
            ]
            if real_obstacles:
                clearance = min(o.distance_to(_enu(x, y)) for o in real_obstacles)
                metrics.min_obstacle_clearance_m = min(
                    metrics.min_obstacle_clearance_m, clearance
                )
            else:
                clearance = math.inf

            target = mission.waypoints[waypoint_index]
            if step < recovery_until:
                tx = x + 2.5 * math.cos(recovery_heading)
                ty = y + 2.5 * math.sin(recovery_heading)
                local_target = (
                    max(0.5, min(terrain.width_m - 0.5, tx)),
                    max(0.5, min(terrain.height_m - 0.5, ty)),
                )
            elif (step >= next_replan or planned_waypoint != waypoint_index
                    or (route and route_index >= len(route))):
                try:
                    path = planner.plan((x, y), target)
                    route = [(w.x_m, w.y_m) for w in path.waypoints]
                    route_index = 1 if len(route) > 1 else 0
                    planned_waypoint = waypoint_index
                except PlanningError:
                    route = []
                    planned_waypoint = waypoint_index
                next_replan = step + replan_every
            if step < recovery_until:
                local_target = (
                    max(0.5, min(terrain.width_m - 0.5, x + 2.5 * math.cos(recovery_heading))),
                    max(0.5, min(terrain.height_m - 0.5, y + 2.5 * math.sin(recovery_heading))),
                )
            elif route and route_index < len(route):
                local_target = route[route_index]
                if math.hypot(local_target[0] - x, local_target[1] - y) < 0.6:
                    route_index += 1
                    if route_index < len(route):
                        local_target = route[route_index]
            else:
                local_target = target
            desired_heading = math.atan2(local_target[1] - y, local_target[0] - x)
            # Rota varken kaçınma yalnızca acil tehditte; rotasızken keşif kaçınması
            if real_obstacles and (not route or clearance < 1.5):
                avoid_heading = self._avoidance.avoid(desired_heading, obstacle_tuples)
            else:
                avoid_heading = desired_heading
            # Yasak bölge itmesi: bölge yakınında yönü dışarı doğru bük
            forbidden_dist, fz_x, fz_y = terrain.nearest_forbidden(x, y)
            if forbidden_dist < 3.0:
                away_angle = math.atan2(y - fz_y, x - fz_x)
                weight = (1.0 - forbidden_dist / 3.0) * 1.0
                hx = math.cos(avoid_heading)
                hy = math.sin(avoid_heading)
                avoid_heading = math.atan2(
                    hy + weight * math.sin(away_angle),
                    hx + weight * math.cos(away_angle),
                )
            # Dünya sınırı itmesi: kenara yaklaştıkça yönü içeri çevir
            edge_dist = min(x, y, terrain.width_m - x, terrain.height_m - y)
            if edge_dist < 2.5:
                if x <= y and x <= terrain.width_m - x:
                    ex, ey = 1.0, 0.0
                elif terrain.width_m - x <= y:
                    ex, ey = -1.0, 0.0
                elif y <= terrain.height_m - y:
                    ex, ey = 0.0, 1.0
                else:
                    ex, ey = 0.0, -1.0
                weight = 1.0 - edge_dist / 2.5
                hx = math.cos(avoid_heading)
                hy = math.sin(avoid_heading)
                avoid_heading = math.atan2(
                    hy + weight * ey,
                    hx + weight * ex,
                )
            prev_avoid = avoid_heading
            if abs(_wrap(avoid_heading - desired_heading)) > 1e-6 and detected > 0:
                if first_avoidance_step is None:
                    first_avoidance_step = step

            heading_err_estimate = _wrap(avoid_heading - heading)
            speed_setpoint = self._speed_for(
                step, speed_mps, heading_err_estimate, clearance,
                local_target, x, y
            )
            # Yakın engel: yavaşla; çarpışma anında dur (kaçış yönü hazır)
            if clearance < 1.2:
                speed_setpoint = min(speed_setpoint, 0.5)
            if clearance < 0.4:
                speed_setpoint = 0.0
            if forbidden_dist < 0.8:
                speed_setpoint = min(speed_setpoint, 0.2)
            if edge_dist < 0.5:
                speed_setpoint = min(speed_setpoint, 0.2)
            command = self._controller.step(
                target_heading_rad=avoid_heading,
                target_speed_mps=speed_setpoint,
                current_heading_rad=heading,
                dt=self._dt,
            )
            speed = command.forward_mps
            angular = command.angular_radps
            speed_mps = speed

            vehicle.step(speed, angular, self._dt)

            true_dx = vehicle.x - x
            true_dy = vehicle.y - y
            true_delta = math.hypot(true_dx, true_dy)
            true_delta_heading = _wrap(vehicle.heading - heading)
            measured_d, measured_h = self._odometry_sensor.measure(
                true_delta, true_delta_heading, weather, self._rng
            )
            odometry.update(OdometryMeasurement(
                delta_distance_m=measured_d,
                delta_heading_rad=measured_h,
            ))

            estimated_hits = []
            if step % self._grid_update_every == 0 and not mission.gps_available:
                pose = odometry.pose
                estimated_hits = [
                    (pose.x_m + p.range_m * math.cos(p.angle_rad),
                     pose.y_m + p.range_m * math.sin(p.angle_rad))
                    for p in scan
                    if math.isfinite(p.range_m)
                ]
                grid.update_scan((pose.x_m, pose.y_m), estimated_hits)

            est = odometry.pose
            error = math.hypot(est.x_m - vehicle.x, est.y_m - vehicle.y)
            error_total += error
            error_samples += 1
            metrics.final_position_error_m = error

            deviation = _line_deviation(
                (x, y), mission.start, target
            )
            deviation_total += deviation
            deviation_samples += 1

            reached = math.hypot(
                x - target[0], y - target[1]
            ) <= mission.arrival_tolerance_m
            if reached:
                waypoint_index += 1
                if waypoint_index >= len(mission.waypoints):
                    metrics.success = True
                    metrics.steps = step
                    metrics.duration_s = step * self._dt
                    break

            if first_detection_step is not None and first_avoidance_step is not None:
                reaction_total += (first_avoidance_step - first_detection_step) * self._dt
                reaction_samples += 1
                metrics.max_reaction_time_s = max(
                    metrics.max_reaction_time_s,
                    (first_avoidance_step - first_detection_step) * self._dt,
                )
                first_detection_step = None
                first_avoidance_step = None
            detected_obstacles_prev = detected

            if telemetry_callback is not None:
                phase = "ACTIVE"
                try:
                    telemetry_callback(TelemetryFrame(
                        vehicle_id=mission.mission_id,
                        sim_time_s=step * self._dt,
                        step=step,
                        position_m=(vehicle.x, vehicle.y),
                        heading_deg=math.degrees(vehicle.heading) % 360.0,
                        speed_mps=speed_mps,
                        target_m=target,
                        clearance_m=clearance,
                        obstacle_count=detected,
                        waypoint_index=waypoint_index,
                        waypoint_count=len(mission.waypoints),
                        mission_phase=phase,
                        gps_available=mission.gps_available,
                        position_error_m=error,
                        battery_percent=max(5.0, 100.0 - 0.05 * step),
                        link_quality=max(0.3, min(
                            1.0, 0.9 + 0.08 * math.sin(step / 20.0)
                            + 0.02 * telemetry_rng.gauss(0.0, 1.0))),
                        engine_ok=True,
                    ))
                except Exception:
                    pass
        else:
            metrics.time_out = True

        metrics.steps = metrics.steps or steps_limit
        metrics.duration_s = metrics.duration_s or steps_limit * self._dt
        if metrics.stuck:
            metrics.duration_s = metrics.steps * self._dt
        if error_samples:
            metrics.position_error_m = error_total / error_samples
        if deviation_samples:
            metrics.route_deviation_m = deviation_total / deviation_samples
        if reaction_samples:
            metrics.reaction_time_s = reaction_total / reaction_samples
        if not math.isfinite(metrics.min_obstacle_clearance_m):
            metrics.min_obstacle_clearance_m = 0.0
        metrics.map_known_ratio = grid.known_ratio() if not mission.gps_available else 0.0
        metrics.waypoints_reached = waypoint_index
        return metrics

    def _speed_for(
        self,
        step: int,
        current: float,
        heading_err: float,
        clearance: float,
        target: Tuple[float, float],
        x: float,
        y: float,
    ) -> float:
        distance_to_target = math.hypot(target[0] - x, target[1] - y)
        speed = 2.0
        if abs(heading_err) > math.radians(45.0):
            speed = 0.6
        if clearance < 2.5:
            speed = min(speed, 0.7)
        if clearance < 1.0:
            speed = min(speed, 0.4)
        if distance_to_target < 2.0:
            speed = min(speed, 0.8)
        return speed


def _make_grid(terrain: Terrain):
    from slam import OccupancyGrid
    return OccupancyGrid(
        width_m=terrain.width_m,
        height_m=terrain.height_m,
        resolution_m=0.5,
        center=(terrain.width_m / 2.0, terrain.height_m / 2.0),
    )


def _make_plan_grid(terrain: Terrain, vehicle_radius_m: float) -> GridMap:
    """Global planlama için engelli+yasak bölgeli, şişirilmiş harita."""
    grid = GridMap(
        resolution_m=0.5,
        width_m=terrain.width_m,
        height_m=terrain.height_m,
    )
    inflation = vehicle_radius_m + 0.6
    for obstacle in terrain.obstacles:
        grid.mark_obstacle(obstacle.x_m, obstacle.y_m,
                           obstacle.radius_m + inflation)
    for zone in terrain.forbidden:
        grid.mark_obstacle(zone.x_m, zone.y_m, zone.radius_m + inflation)
    return grid


def _enu(x: float, y: float):
    from core.transforms import EnuPoint
    return EnuPoint(east_m=x, north_m=y)


def _wrap(angle: float) -> float:
    while angle > math.pi:
        angle -= 2.0 * math.pi
    while angle <= -math.pi:
        angle += 2.0 * math.pi
    return angle


def _line_deviation(
    point: Tuple[float, float],
    start: Tuple[float, float],
    end: Tuple[float, float],
) -> float:
    """Noktanın başlangıç-hedef doğrusuna dikey uzaklığı."""
    sx, sy = start
    ex, ey = end
    px, py = point
    dx, dy = ex - sx, ey - sy
    length_sq = dx * dx + dy * dy
    if length_sq < 1e-9:
        return math.hypot(px - sx, py - sy)
    t = max(0.0, min(1.0, ((px - sx) * dx + (py - sy) * dy) / length_sq))
    proj_x, proj_y = sx + t * dx, sy + t * dy
    return math.hypot(px - proj_x, py - proj_y)
