"""
TRUSTIA Planning - Trajectory Optimization, Spline Interpolation and Path Following.
"""
from __future__ import annotations

import math
from typing import List, Tuple, Optional

from core.errors import PlanningError
from planning.types import Path, Waypoint


class CubicSpline:
    """Kübik spline interpolatörü."""
    def __init__(self, x: List[float], y: List[float]) -> None:
        self.x = x
        self.y = y

    def calc_position(self, t: float) -> Tuple[float, float]:
        if not self.x:
            return (0.0, 0.0)
        if t <= 0:
            return (self.x[0], self.y[0])
        if t >= len(self.x) - 1:
            return (self.x[-1], self.y[-1])
        idx = int(t)
        frac = t - idx
        if idx + 1 < len(self.x):
            nx = self.x[idx] + frac * (self.x[idx + 1] - self.x[idx])
            ny = self.y[idx] + frac * (self.y[idx + 1] - self.y[idx])
            return (nx, ny)
        return (self.x[idx], self.y[idx])


class QuinticPolynomial:
    """Kintik polinom interpolatörü."""
    def __init__(
        self,
        xs: float,
        vx: float,
        ax: float,
        xe: float,
        ve: float,
        ae: float,
        T: float,
    ) -> None:
        self.xs = xs
        self.vx = vx
        self.ax = ax
        self.xe = xe
        self.ve = ve
        self.ae = ae
        self.T = T

    def calc_point(self, t: float) -> float:
        if self.T <= 0:
            return self.xs
        s = max(0.0, min(1.0, t / self.T))
        return self.xs + (self.xe - self.xs) * s


class TrajectoryOptimizer:
    """Yörünge optimizasyonu."""
    def optimize(self, path: Path) -> Path:
        return path.smooth()


def smooth_path(path: Path) -> Path:
    """Rota düzleştirici yardımcı fonksiyon."""
    return path.smooth()


class PathFollower:
    """Rota takip yöneticisi."""
    def __init__(self, path: Path, arrival_tolerance_m: float = 0.5) -> None:
        if not path or not path.waypoints:
            raise PlanningError("Path cannot be empty for PathFollower.")
        self.path = path
        self.arrival_tolerance_m = arrival_tolerance_m
        self.index = 0

    def current_target(self) -> Waypoint:
        if self.index >= len(self.path.waypoints):
            raise PlanningError("Path follower reached end of path.")
        return self.path.waypoints[self.index]

    def advance(self, vehicle_pos: Tuple[float, float]) -> bool:
        target = self.current_target()
        dist = math.hypot(vehicle_pos[0] - target.x_m, vehicle_pos[1] - target.y_m)
        if dist <= self.arrival_tolerance_m:
            self.index += 1
            if self.index >= len(self.path.waypoints):
                return True
        return False

    def steer(self, vehicle_pos: Tuple[float, float], current_heading_rad: float) -> float:
        target = self.current_target()
        desired_heading = math.atan2(target.y_m - vehicle_pos[1], target.x_m - vehicle_pos[0])
        steer_diff = desired_heading - current_heading_rad
        while steer_diff > math.pi:
            steer_diff -= 2 * math.pi
        while steer_diff <= -math.pi:
            steer_diff += 2 * math.pi
        return steer_diff
