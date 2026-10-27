"""
TRUSTIA Lanelet2 Yüksek Çözünürlüklü (HD) Şerit Ağı ve Kavşak/Yaya Geçiş Üstünlüğü Motoru
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class LaneletSegment:
    lanelet_id: str
    speed_limit_kmh: float
    left_bound_solid: bool
    right_bound_solid: bool
    has_crosswalk: bool = False
    is_intersection: bool = False


@dataclass(frozen=True)
class RightOfWayDecision:
    lanelet_id: str
    behavior_command: str
    target_speed_mps: float
    lane_change_left_allowed: bool
    lane_change_right_allowed: bool
    stopping_distance_m: Optional[float]
    reason: str


class Lanelet2TrafficRuleEngine:
    """Lanelet2 HD harita trafik kuralları ve yaya/kavşak geçiş üstünlüğü motoru."""

    def __init__(self) -> None:
        self.lanelets: Dict[str, LaneletSegment] = {}

    def register_lanelet(self, segment: LaneletSegment) -> None:
        self.lanelets[segment.lanelet_id] = segment

    def evaluate_rules(
        self,
        lanelet_id: str,
        ego_speed_mps: float,
        pedestrian_on_crosswalk: bool = False,
        crosswalk_distance_m: float = 999.0,
        traffic_light_state: str = "GREEN",
        conflicting_vehicle_ttc_s: float = 99.0,
    ) -> RightOfWayDecision:
        segment = self.lanelets.get(
            lanelet_id,
            LaneletSegment(lanelet_id, 50.0, True, True),
        )
        max_speed_mps = segment.speed_limit_kmh / 3.6
        if segment.has_crosswalk and pedestrian_on_crosswalk and crosswalk_distance_m <= 45.0:
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="STOP_FOR_PEDESTRIAN",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=max(0.0, crosswalk_distance_m - 3.0),
                reason="Yaya geçidi önceliği",
            )
        if traffic_light_state in ("RED", "YELLOW"):
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="STOP_RED_LIGHT",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=max(0.0, crosswalk_distance_m - 2.0),
                reason="Kırmızı/Sarı ışık duruşu",
            )
        if segment.is_intersection and conflicting_vehicle_ttc_s < 4.5:
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="YIELD_INTERSECTION",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=5.0,
                reason="Kavşak geçiş üstünlüğü beklemesi",
            )
        return RightOfWayDecision(
            lanelet_id=lanelet_id,
            behavior_command="CRUISE",
            target_speed_mps=max_speed_mps,
            lane_change_left_allowed=not segment.left_bound_solid,
            lane_change_right_allowed=not segment.right_bound_solid,
            stopping_distance_m=None,
            reason="Normal seyir",
        )
