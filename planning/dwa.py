"""
TRUSTIA Planning - Dynamic Window Approach (DWA) for local obstacle avoidance and velocity sampling.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional


@dataclass
class DWAConfig:
    """DWA konfigürasyonu."""
    max_speed_mps: float = 2.0
    min_speed_mps: float = 0.0
    max_yaw_rate_rads: float = math.radians(40.0)
    max_accel_mps2: float = 0.5
    max_delta_yaw_rate_rads2: float = math.radians(40.0)
    v_resolution_mps: float = 0.1
    yaw_rate_resolution_rads: float = math.radians(2.0)
    dt_s: float = 0.1
    predict_time_s: float = 3.0
    to_goal_cost_gain: float = 0.15
    speed_cost_gain: float = 1.0
    obstacle_cost_gain: float = 1.0
    robot_radius_m: float = 0.5


@dataclass
class VelocitySpace:
    """Dinamik pencere hız uzayı."""
    min_v: float
    max_v: float
    min_w: float
    max_w: float


@dataclass
class DynamicWindow:
    """Robot dinamik kısıtlarına göre hız aralıklarını hesaplayan pencere."""
    config: DWAConfig = field(default_factory=DWAConfig)

    def compute_window(self, current_v: float, current_w: float) -> VelocitySpace:
        min_v = max(self.config.min_speed_mps, current_v - self.config.max_accel_mps2 * self.config.dt_s)
        max_v = min(self.config.max_speed_mps, current_v + self.config.max_accel_mps2 * self.config.dt_s)
        min_w = max(-self.config.max_yaw_rate_rads, current_w - self.config.max_delta_yaw_rate_rads2 * self.config.dt_s)
        max_w = min(self.config.max_yaw_rate_rads, current_w + self.config.max_delta_yaw_rate_rads2 * self.config.dt_s)
        return VelocitySpace(min_v, max_v, min_w, max_w)


class DWAPlanner:
    """Dynamic Window Approach yerel planlayıcı."""
    def __init__(self, config: DWAConfig = DWAConfig()) -> None:
        self.config = config
        self.window = DynamicWindow(config)

    def plan(
        self,
        x: float,
        y: float,
        yaw: float,
        v: float,
        w: float,
        goal: Tuple[float, float],
        obstacles: List[Tuple[float, float]],
    ) -> Tuple[float, float]:
        vs = self.window.compute_window(v, w)
        best_v = 0.0
        best_w = 0.0
        min_cost = float('inf')

        v_steps = max(1, int((vs.max_v - vs.min_v) / max(0.01, self.config.v_resolution_mps)))
        w_steps = max(1, int((vs.max_w - vs.min_w) / max(0.01, self.config.yaw_rate_resolution_rads)))

        for i in range(v_steps + 1):
            sample_v = vs.min_v + i * self.config.v_resolution_mps
            if sample_v > vs.max_v:
                sample_v = vs.max_v
            for j in range(w_steps + 1):
                sample_w = vs.min_w + j * self.config.yaw_rate_resolution_rads
                if sample_w > vs.max_w:
                    sample_w = vs.max_w

                cost = self._calc_cost(x, y, yaw, sample_v, sample_w, goal, obstacles)
                if cost < min_cost:
                    min_cost = cost
                    best_v = sample_v
                    best_w = sample_w

        return best_v, best_w

    def _calc_cost(
        self,
        x: float,
        y: float,
        yaw: float,
        v: float,
        w: float,
        goal: Tuple[float, float],
        obstacles: List[Tuple[float, float]],
    ) -> float:
        predict_steps = int(self.config.predict_time_s / self.config.dt_s)
        curr_x, curr_y, curr_yaw = x, y, yaw

        for _ in range(predict_steps):
            curr_x += v * math.cos(curr_yaw) * self.config.dt_s
            curr_y += v * math.sin(curr_yaw) * self.config.dt_s
            curr_yaw += w * self.config.dt_s

        dist_to_goal = math.hypot(goal[0] - curr_x, goal[1] - curr_y)
        goal_cost = self.config.to_goal_cost_gain * dist_to_goal
        speed_cost = self.config.speed_cost_gain * (self.config.max_speed_mps - v)

        min_obs_dist = float('inf')
        for ox, oy in obstacles:
            d = math.hypot(ox - curr_x, oy - curr_y)
            if d < min_obs_dist:
                min_obs_dist = d

        if min_obs_dist <= self.config.robot_radius_m:
            return float('inf')

        obs_cost = self.config.obstacle_cost_gain / min_obs_dist if min_obs_dist > 0 else float('inf')
        return goal_cost + speed_cost + obs_cost


class LocalAvoidance:
    """Yerel engel kaçınma vektör alanı denetleyicisi."""
    def __init__(self, avoidance_radius_m: float = 5.0, max_turn_deg: float = 60.0) -> None:
        self.avoidance_radius_m = avoidance_radius_m
        self.max_turn_deg = max_turn_deg

    def avoid(self, desired_heading_rad: float, obstacles: List[Tuple]) -> float:
        if not obstacles:
            return desired_heading_rad

        repulsion_x = 0.0
        repulsion_y = 0.0
        has_close_obs = False

        for item in obstacles:
            dx = item[0]
            dy = item[1]
            dist = math.hypot(dx, dy)
            if dist < self.avoidance_radius_m and dist > 0.001:
                has_close_obs = True
                force = (self.avoidance_radius_m - dist) / dist
                repulsion_x -= (dx / dist) * force
                repulsion_y -= (dy / dist) * force

        if not has_close_obs:
            return desired_heading_rad

        heading_x = math.cos(desired_heading_rad) + repulsion_x
        heading_y = math.sin(desired_heading_rad) + repulsion_y
        return math.atan2(heading_y, heading_x)
