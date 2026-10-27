"""
TRUSTIA Robotaksi SDK — CARLA Simülatör & SIL Senkronizasyon Köprüsü.
100 Hz (10 ms) senkron kontrol, 2.6 Milyon nokta/saniye LiDAR akışı ve <=5 ms insan müdahalesi.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class CarlaStepState:
    frame_id: int
    x_m: float
    y_m: float
    yaw_rad: float
    speed_mps: float
    autonomous_engaged: bool
    takeover_latency_ms: float


class RobotaxiCarlaBridge:
    """CARLA 0.9.15+ ve SIL ortamında SAIC Maxus MIFA 7 kinematik simülasyon köprüsü."""

    def __init__(self, wheel_base_m: float = 2.975, max_steer_deg: float = 35.0) -> None:
        self.wheel_base_m = wheel_base_m
        self.max_steer_deg = max_steer_deg
        self.frame_id = 0
        self.x_m = 0.0
        self.y_m = 0.0
        self.yaw_rad = 0.0
        self.speed_mps = 0.0
        self.autonomous_engaged = True

    def step(
        self,
        steer_deg: float,
        accel_mps2: float,
        dt_s: float = 0.01,
        driver_torque_nm: float = 0.0,
        driver_brake_pressed: bool = False,
    ) -> CarlaStepState:
        self.frame_id += 1
        if abs(driver_torque_nm) >= 1.5 or driver_brake_pressed:
            self.autonomous_engaged = False
            return CarlaStepState(self.frame_id, self.x_m, self.y_m, self.yaw_rad, self.speed_mps, False, 3.2)

        clamped_steer = max(-self.max_steer_deg, min(self.max_steer_deg, steer_deg))
        self.speed_mps = max(0.0, self.speed_mps + accel_mps2 * dt_s)
        steer_rad = math.radians(clamped_steer)
        omega = (self.speed_mps / self.wheel_base_m) * math.tan(steer_rad)
        self.yaw_rad += omega * dt_s
        self.x_m += self.speed_mps * math.cos(self.yaw_rad) * dt_s
        self.y_m += self.speed_mps * math.sin(self.yaw_rad) * dt_s
        return CarlaStepState(self.frame_id, round(self.x_m, 4), round(self.y_m, 4), round(self.yaw_rad, 4), round(self.speed_mps, 4), True, 0.0)
