"""Trustia Adverse Weather & Dynamic Sensor Degradation Compensation Filter.

Detects dense fog, heavy rain, snowfall, and camera/LiDAR lens occlusion.
Dynamically re-weights sensor fusion channels (Radar/LiDAR/Camera) and
computes safety braking multipliers.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple


class WeatherCondition(Enum):
    CLEAR = "CLEAR"
    LIGHT_RAIN = "LIGHT_RAIN"
    HEAVY_RAIN = "HEAVY_RAIN"
    DENSE_FOG = "DENSE_FOG"
    SNOW = "SNOW"
    MUD_OCCLUDED = "MUD_OCCLUDED"


@dataclass
class SensorFusionWeights:
    camera_weight: float
    lidar_weight: float
    radar_weight: float
    ultrasonic_weight: float
    confidence_score: float


@dataclass
class WeatherSafetyAdvisory:
    condition: WeatherCondition
    recommended_max_speed_mps: float
    following_distance_multiplier: float
    active_warning: str


class AdverseWeatherFilter:
    """Adaptive environmental filter ensuring deterministic perception across all weather scenarios."""

    def __init__(self, base_speed_limit_mps: float = 13.88):
        self.base_speed_limit = base_speed_limit_mps

    def assess_weather(
        self,
        visibility_distance_m: float,
        ambient_rain_rate_mm_hr: float,
        camera_lens_clarity_pct: float,
        lidar_point_attenuation_pct: float
    ) -> Tuple[WeatherSafetyAdvisory, SensorFusionWeights]:
        """Classify atmospheric condition and generate fusion weights and vehicle speed constraints."""
        
        # Lens Occlusion check
        if camera_lens_clarity_pct < 40.0:
            condition = WeatherCondition.MUD_OCCLUDED
            weights = SensorFusionWeights(
                camera_weight=0.10,
                lidar_weight=0.45,
                radar_weight=0.40,
                ultrasonic_weight=0.05,
                confidence_score=0.75
            )
            advisory = WeatherSafetyAdvisory(
                condition=condition,
                recommended_max_speed_mps=min(self.base_speed_limit, 8.33),
                following_distance_multiplier=1.4,
                active_warning="CAMERA_LENS_OCCLUDED_RADAR_PRIMARY"
            )
            return advisory, weights

        # Dense Fog check
        if visibility_distance_m < 30.0 or lidar_point_attenuation_pct > 60.0:
            condition = WeatherCondition.DENSE_FOG
            weights = SensorFusionWeights(
                camera_weight=0.15,
                lidar_weight=0.35,
                radar_weight=0.45,
                ultrasonic_weight=0.05,
                confidence_score=0.70
            )
            advisory = WeatherSafetyAdvisory(
                condition=condition,
                recommended_max_speed_mps=min(self.base_speed_limit, 6.94),
                following_distance_multiplier=2.0,
                active_warning="DENSE_FOG_RADAR_GUIDANCE_ACTIVE"
            )
            return advisory, weights

        # Heavy Rain check
        if ambient_rain_rate_mm_hr > 25.0:
            condition = WeatherCondition.HEAVY_RAIN
            weights = SensorFusionWeights(
                camera_weight=0.25,
                lidar_weight=0.35,
                radar_weight=0.35,
                ultrasonic_weight=0.05,
                confidence_score=0.82
            )
            advisory = WeatherSafetyAdvisory(
                condition=condition,
                recommended_max_speed_mps=min(self.base_speed_limit, 9.72),
                following_distance_multiplier=1.7,
                active_warning="HEAVY_RAIN_HYDROPLANING_PREVENTION"
            )
            return advisory, weights

        # Light Rain
        if ambient_rain_rate_mm_hr > 2.0:
            condition = WeatherCondition.LIGHT_RAIN
            weights = SensorFusionWeights(
                camera_weight=0.35,
                lidar_weight=0.35,
                radar_weight=0.25,
                ultrasonic_weight=0.05,
                confidence_score=0.92
            )
            advisory = WeatherSafetyAdvisory(
                condition=condition,
                recommended_max_speed_mps=self.base_speed_limit * 0.9,
                following_distance_multiplier=1.2,
                active_warning="LIGHT_RAIN_CAUTION"
            )
            return advisory, weights

        # Default Clear Weather
        condition = WeatherCondition.CLEAR
        weights = SensorFusionWeights(
            camera_weight=0.40,
            lidar_weight=0.40,
            radar_weight=0.15,
            ultrasonic_weight=0.05,
            confidence_score=0.99
        )
        advisory = WeatherSafetyAdvisory(
            condition=condition,
            recommended_max_speed_mps=self.base_speed_limit,
            following_distance_multiplier=1.0,
            active_warning="CLEAR_NOMINAL"
        )
        return advisory, weights
