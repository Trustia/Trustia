"""
TRUSTIA Lanelet2 Yüksek Çözünürlüklü (HD) Şerit Ağı ve Kavşak/Yaya Geçiş Üstünlüğü Motoru
=========================================================================================
Seviye-4 Robotaksinin şehir içi ve kampüs yollarında:
  1. Lanelet2 topolojik şerit sınırlarını (kesikli şerit / düz çizgi şerit değiştirme yasağı)
  2. Yaya geçidi (Crosswalk) yaklaşımında yaya varlığı ve duruş mesafesi hesabını
  3. Kavşaklarda geçiş üstünlüğü (Right-of-Way), trafik ışığı durumu ve hız sınırı kurallarını

deterministik olarak işleten karar motorudur.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class LaneletSegment:
    """Lanelet2 yüksek çözünürlüklü harita şerit dilimi."""

    lanelet_id: str
    speed_limit_kmh: float
    left_bound_solid: bool
    right_bound_solid: bool
    has_crosswalk: bool = False
    is_intersection: bool = False


@dataclass(frozen=True)
class RightOfWayDecision:
    """Trafik kuralları ve geçiş üstünlüğü değerlendirme sonucu."""

    lanelet_id: str
    behavior_command: str  # "CRUISE", "STOP_FOR_PEDESTRIAN", "STOP_RED_LIGHT", "YIELD_INTERSECTION"
    target_speed_mps: float
    lane_change_left_allowed: bool
    lane_change_right_allowed: bool
    stopping_distance_m: Optional[float]
    reason: str


class Lanelet2TrafficRuleEngine:
    """
    Lanelet2 HD harita katmanı üzerinde hız sınırı, şerit değiştirme izni,
    yaya geçidi önceliği ve kavşak geçiş üstünlüğü kararlarını üretir.
    """

    def __init__(self, comfortable_decel_mps2: float = 2.0) -> None:
        self.comfortable_decel_mps2 = comfortable_decel_mps2
        self.lanelets: Dict[str, LaneletSegment] = {}

    def register_lanelet(self, segment: LaneletSegment) -> None:
        self.lanelets[segment.lanelet_id] = segment

    def evaluate_rules(
        self,
        lanelet_id: str,
        ego_speed_mps: float,
        pedestrian_on_crosswalk: bool = False,
        crosswalk_distance_m: float = 999.0,
        traffic_light_state: str = "GREEN",  # "GREEN", "YELLOW", "RED"
        conflicting_vehicle_ttc_s: float = 99.0,
    ) -> RightOfWayDecision:
        """Aktif Lanelet şeridindeki trafik kurallarını değerlendirir."""
        segment = self.lanelets.get(
            lanelet_id,
            LaneletSegment(
                lanelet_id=lanelet_id,
                speed_limit_kmh=50.0,
                left_bound_solid=True,
                right_bound_solid=True,
            ),
        )
        max_speed_mps = segment.speed_limit_kmh / 3.6
        left_ok = not segment.left_bound_solid
        right_ok = not segment.right_bound_solid

        # 1. Yaya geçidinde yaya varsa mutlak geçiş üstünlüğü yayadadır (2918 s. KTK m.74)
        if segment.has_crosswalk and pedestrian_on_crosswalk and crosswalk_distance_m <= 45.0:
            stop_dist = max(0.0, crosswalk_distance_m - 3.0)
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="STOP_FOR_PEDESTRIAN",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=stop_dist,
                reason=f"KTK m.74 Yaya Geçidi Önceliği: {crosswalk_distance_m:.1f} m ileride yaya algılandı.",
            )

        # 2. Kırmızı veya sarı trafik ışığı
        if traffic_light_state in ("RED", "YELLOW"):
            stop_dist = max(0.0, crosswalk_distance_m - 2.0)
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="STOP_RED_LIGHT",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=stop_dist,
                reason=f"Trafik ışığı {traffic_light_state} durumunda, duruş çizgisi korunuyor.",
            )

        # 3. Kavşak içinde yaklaşan öncelikli araç kontrolü
        if segment.is_intersection and conflicting_vehicle_ttc_s < 4.5:
            return RightOfWayDecision(
                lanelet_id=lanelet_id,
                behavior_command="YIELD_INTERSECTION",
                target_speed_mps=0.0,
                lane_change_left_allowed=False,
                lane_change_right_allowed=False,
                stopping_distance_m=5.0,
                reason=f"Kavşak geçiş üstünlüğü koruması (çakışan araç TTC={conflicting_vehicle_ttc_s:.1f} sn).",
            )

        return RightOfWayDecision(
            lanelet_id=lanelet_id,
            behavior_command="CRUISE",
            target_speed_mps=max_speed_mps,
            lane_change_left_allowed=left_ok,
            lane_change_right_allowed=right_ok,
            stopping_distance_m=None,
            reason=f"Normal seyir ({segment.speed_limit_kmh:.0f} km/s hız sınırı).",
        )
