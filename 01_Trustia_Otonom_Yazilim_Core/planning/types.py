"""
TRUSTIA Planlama - Temel veri yapıları.

Path, waypoint, trajectory ve planlama sonuçları.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional, Tuple

import numpy as np


@dataclass(frozen=True)
class Waypoint:
    """Tek rota noktası - konum + kısıtlar."""
    x_m: float
    y_m: float
    heading_rad: Optional[float] = None  # Zorunlu heading (opsiyonel)
    speed_mps: float = 1.0
    tolerance_m: float = 1.0  # Varış toleransı
    
    def distance_to(self, other: "Waypoint") -> float:
        dx = self.x_m - other.x_m
        dy = self.y_m - other.y_m
        return math.sqrt(dx * dx + dy * dy)
    
    def to_tuple(self) -> Tuple[float, float]:
        return (self.x_m, self.y_m)


@dataclass
class Path:
    """Waypoint dizisi - global path."""
    waypoints: List[Waypoint] = field(default_factory=list)
    total_length: float = 0.0
    planning_time_s: float = 0.0
    
    def __len__(self) -> int:
        return len(self.waypoints)
    
    def __getitem__(self, index: int) -> Waypoint:
        return self.waypoints[index]
    
    def append(self, waypoint: Waypoint) -> None:
        if self.waypoints:
            self.total_length += self.waypoints[-1].distance_to(waypoint)
        self.waypoints.append(waypoint)
    
    def extend(self, waypoints: List[Waypoint]) -> None:
        for wp in waypoints:
            self.append(wp)
    
    def closest_waypoint(self, x: float, y: float) -> Tuple[int, float]:
        """En yakın waypoint (indis, mesafe)."""
        if not self.waypoints:
            return -1, float('inf')
        
        best_idx = 0
        best_dist = float('inf')
        
        for i, wp in enumerate(self.waypoints):
            dist = math.sqrt((wp.x_m - x)**2 + (wp.y_m - y)**2)
            if dist < best_dist:
                best_dist = dist
                best_idx = i
        
        return best_idx, best_dist
    
    def to_xy_lists(self) -> Tuple[List[float], List[float]]:
        """(x_list, y_list) plotting için."""
        x_list = [wp.x_m for wp in self.waypoints]
        y_list = [wp.y_m for wp in self.waypoints]
        return x_list, y_list

    @property
    def length_m(self) -> float:
        if not self.waypoints or len(self.waypoints) < 2:
            return 0.0
        total = 0.0
        for i in range(len(self.waypoints) - 1):
            total += self.waypoints[i].distance_to(self.waypoints[i + 1])
        return total

    def smooth(self) -> Path:
        if len(self.waypoints) < 3:
            return Path(list(self.waypoints))
        res = [self.waypoints[0]]
        for i in range(1, len(self.waypoints) - 1):
            prev_wp = res[-1]
            curr_wp = self.waypoints[i]
            next_wp = self.waypoints[i + 1]
            dx1 = curr_wp.x_m - prev_wp.x_m
            dy1 = curr_wp.y_m - prev_wp.y_m
            dx2 = next_wp.x_m - curr_wp.x_m
            dy2 = next_wp.y_m - curr_wp.y_m
            cross = abs(dx1 * dy2 - dy1 * dx2)
            if cross > 1e-6:
                res.append(curr_wp)
        res.append(self.waypoints[-1])
        return Path(res)


class PlanningStatus(IntEnum):
    """Planlama sonucu durumu."""
    SUCCESS = 0
    NO_PATH = 1
    START_OCCUPIED = 2
    GOAL_OCCUPIED = 3
    TIMEOUT = 4
    ERROR = 5


@dataclass
class PlanningRequest:
    """Planlama talebi."""
    start: Waypoint
    goal: Waypoint
    max_planning_time_s: float = 5.0
    use_start_heading: bool = True
    use_goal_heading: bool = True


@dataclass 
class PlanningResult:
    """Planlama sonucu."""
    status: PlanningStatus
    path: Optional[Path] = None
    planning_time_s: float = 0.0
    iterations: int = 0
    message: str = ""
    
    @property
    def success(self) -> bool:
        return self.status == PlanningStatus.SUCCESS


@dataclass(frozen=True)
class TrajectoryPoint:
    """Trajectory üzerinde tek nokta - kinematik/dinamik bilgi."""
    x_m: float
    y_m: float
    heading_rad: float
    velocity_mps: float = 0.0
    acceleration_mps2: float = 0.0
    curvature: float = 0.0  # 1/radius_m
    time_s: float = 0.0
    
    def to_waypoint(self) -> Waypoint:
        return Waypoint(
            x_m=self.x_m,
            y_m=self.y_m, 
            heading_rad=self.heading_rad,
            speed_mps=self.velocity_mps,
        )


@dataclass
class Trajectory:
    """Kinematik/dinamik trajectory - zamanla parametreli."""
    points: List[TrajectoryPoint] = field(default_factory=list)
    duration_s: float = 0.0
    
    def __len__(self) -> int:
        return len(self.points)
    
    def __getitem__(self, index: int) -> TrajectoryPoint:
        return self.points[index]
    
    def append(self, point: TrajectoryPoint) -> None:
        self.points.append(point)
        if self.points:
            self.duration_s = max(self.duration_s, point.time_s)
    
    def sample_at_time(self, t: float) -> Optional[TrajectoryPoint]:
        """Belirli zamandaki trajectory noktasını interpolate et."""
        if not self.points or t < 0:
            return None
        
        if t >= self.duration_s:
            return self.points[-1]
        
        # Linear interpolation between adjacent points
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            
            if p1.time_s <= t <= p2.time_s:
                if p2.time_s == p1.time_s:
                    return p1
                
                alpha = (t - p1.time_s) / (p2.time_s - p1.time_s)
                
                return TrajectoryPoint(
                    x_m=p1.x_m + alpha * (p2.x_m - p1.x_m),
                    y_m=p1.y_m + alpha * (p2.y_m - p1.y_m),
                    heading_rad=p1.heading_rad + alpha * (p2.heading_rad - p1.heading_rad),
                    velocity_mps=p1.velocity_mps + alpha * (p2.velocity_mps - p1.velocity_mps),
                    acceleration_mps2=p1.acceleration_mps2 + alpha * (p2.acceleration_mps2 - p1.acceleration_mps2),
                    curvature=p1.curvature + alpha * (p2.curvature - p1.curvature),
                    time_s=t,
                )
        
        return self.points[0]
    
    def to_path(self) -> Path:
        """Trajectory → Path (kinematik bilgi kaybı)."""
        path = Path()
        for point in self.points:
            path.append(point.to_waypoint())
        return path
    
    def max_velocity(self) -> float:
        """Maksimum hız."""
        if not self.points:
            return 0.0
        return max(p.velocity_mps for p in self.points)
    
    def max_acceleration(self) -> float:
        """Maksimum ivme."""
        if not self.points:
            return 0.0
        return max(abs(p.acceleration_mps2) for p in self.points)