"""Trustia Multimodal Trajectory & Intention Prediction Engine.

Predicts future motion trajectories of pedestrians, cyclists, and vehicles
over a 5.0-second planning horizon (10 discrete timesteps @ dt=0.5s).
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Tuple, Optional
import math


class AgentType(Enum):
    PEDESTRIAN = "PEDESTRIAN"
    BICYCLE = "BICYCLE"
    VEHICLE = "VEHICLE"
    UNKNOWN = "UNKNOWN"


class IntentionType(Enum):
    CROSSING = "CROSSING"
    WALKING_PARALLEL = "WALKING_PARALLEL"
    LANE_KEEP = "LANE_KEEP"
    LANE_CHANGE_LEFT = "LANE_CHANGE_LEFT"
    LANE_CHANGE_RIGHT = "LANE_CHANGE_RIGHT"
    STOPPING = "STOPPING"
    TURNING = "TURNING"


@dataclass
class TrajectoryPoint:
    t_offset_sec: float
    x: float
    y: float
    vx: float
    vy: float
    uncertainty_radius_m: float


@dataclass
class PredictedTrajectory:
    agent_id: str
    agent_type: AgentType
    intention: IntentionType
    probability: float
    waypoints: List[TrajectoryPoint]
    collision_risk_score: float = 0.0


class TrajectoryPredictionEngine:
    """Predictive perception layer generating 5-second probabilistic trajectory horizons."""

    def __init__(self, horizon_sec: float = 5.0, dt: float = 0.5):
        self.horizon_sec = horizon_sec
        self.dt = dt
        self.num_steps = int(horizon_sec / dt)

    def predict_agent_trajectory(
        self,
        agent_id: str,
        agent_type_str: str,
        x: float,
        y: float,
        vx: float,
        vy: float,
        heading_rad: float,
        ego_x: float = 0.0,
        ego_y: float = 0.0,
        ego_vx: float = 0.0,
        ego_vy: float = 0.0
    ) -> List[PredictedTrajectory]:
        """Generate multimodal future trajectories for a detected obstacle/actor."""
        try:
            agent_type = AgentType[agent_type_str.upper()]
        except KeyError:
            agent_type = AgentType.UNKNOWN

        speed = math.hypot(vx, vy)
        results = []

        if agent_type == AgentType.PEDESTRIAN:
            # Mode 1: Constant velocity in current direction
            waypoints_main = []
            for step in range(1, self.num_steps + 1):
                t = step * self.dt
                # Add slight deceleration or steady motion
                px = x + vx * t
                py = y + vy * t
                sigma = 0.15 * (t ** 0.75)  # expanding uncertainty cone
                waypoints_main.append(TrajectoryPoint(t, px, py, vx, vy, sigma))

            # Intention classification
            is_crossing = abs(math.sin(heading_rad)) > 0.4
            intention = IntentionType.CROSSING if is_crossing else IntentionType.WALKING_PARALLEL

            risk = self._calculate_collision_risk(waypoints_main, ego_x, ego_y, ego_vx, ego_vy)

            results.append(
                PredictedTrajectory(
                    agent_id=agent_id,
                    agent_type=agent_type,
                    intention=intention,
                    probability=0.75,
                    waypoints=waypoints_main,
                    collision_risk_score=risk
                )
            )

            # Mode 2: Pedestrian stopping / hesitating
            waypoints_stop = []
            for step in range(1, self.num_steps + 1):
                t = step * self.dt
                decay = math.exp(-0.8 * t)
                px = x + vx * (1 - decay) * 1.2
                py = y + vy * (1 - decay) * 1.2
                waypoints_stop.append(TrajectoryPoint(t, px, py, 0.0, 0.0, 0.3 * t))

            results.append(
                PredictedTrajectory(
                    agent_id=agent_id,
                    agent_type=agent_type,
                    intention=IntentionType.STOPPING,
                    probability=0.25,
                    waypoints=waypoints_stop,
                    collision_risk_score=0.1
                )
            )

        elif agent_type == AgentType.VEHICLE:
            # Mode 1: Lane following
            waypoints_lane = []
            for step in range(1, self.num_steps + 1):
                t = step * self.dt
                px = x + vx * t
                py = y + vy * t
                sigma = 0.2 * t
                waypoints_lane.append(TrajectoryPoint(t, px, py, vx, vy, sigma))

            risk = self._calculate_collision_risk(waypoints_lane, ego_x, ego_y, ego_vx, ego_vy)

            results.append(
                PredictedTrajectory(
                    agent_id=agent_id,
                    agent_type=agent_type,
                    intention=IntentionType.LANE_KEEP,
                    probability=0.85,
                    waypoints=waypoints_lane,
                    collision_risk_score=risk
                )
            )

            # Mode 2: Cut-in / Lane change
            waypoints_cutin = []
            lateral_v = 1.0 if vy >= 0 else -1.0
            for step in range(1, self.num_steps + 1):
                t = step * self.dt
                px = x + vx * t
                py = y + (vy + lateral_v * min(1.0, t / 2.0)) * t
                waypoints_cutin.append(TrajectoryPoint(t, px, py, vx, vy + lateral_v, 0.4 * t))

            results.append(
                PredictedTrajectory(
                    agent_id=agent_id,
                    agent_type=agent_type,
                    intention=IntentionType.LANE_CHANGE_LEFT if lateral_v > 0 else IntentionType.LANE_CHANGE_RIGHT,
                    probability=0.15,
                    waypoints=waypoints_cutin,
                    collision_risk_score=risk * 1.2
                )
            )

        else:
            # Default linear model
            waypoints = [
                TrajectoryPoint(step * self.dt, x + vx * step * self.dt, y + vy * step * self.dt, vx, vy, 0.2 * step)
                for step in range(1, self.num_steps + 1)
            ]
            results.append(
                PredictedTrajectory(
                    agent_id=agent_id,
                    agent_type=AgentType.UNKNOWN,
                    intention=IntentionType.LANE_KEEP,
                    probability=1.0,
                    waypoints=waypoints,
                    collision_risk_score=0.0
                )
            )

        return results

    def _calculate_collision_risk(self, waypoints: List[TrajectoryPoint], ego_x: float, ego_y: float, ego_vx: float, ego_vy: float) -> float:
        """Estimate minimum distance and Time-To-Collision (TTC) with ego vehicle."""
        min_dist = float("inf")
        min_t = 0.0

        for pt in waypoints:
            ego_pt_x = ego_x + ego_vx * pt.t_offset_sec
            ego_pt_y = ego_y + ego_vy * pt.t_offset_sec
            dist = math.hypot(pt.x - ego_pt_x, pt.y - ego_pt_y)
            if dist < min_dist:
                min_dist = dist
                min_t = pt.t_offset_sec

        if min_dist < 2.5:
            return 1.0  # Critical immediate collision
        elif min_dist < 6.0:
            return max(0.1, 1.0 - (min_dist / 6.0))
        return 0.0
