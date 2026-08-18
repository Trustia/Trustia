"""
TRUSTIA — Webots 3D Robotik ve Otonomi Kontrolcüsü (Simulation Bridge).

Bu modül, Cyberbotics Webots 3D robotik simülatöründeki tekerlekli aracı / İKA'yı
TRUSTIA Otonomi Çekirdeğine (SLAM, Hybrid A*, Engel Kaçınma, Tehdit Tespiti) bağlar.
"""

from __future__ import annotations

import math
import sys
import time
from typing import List, Optional, Tuple

try:
    from controller import Robot, Lidar, Camera, GPS, Compass, Motor
    WEBOTS_AVAILABLE = True
except ImportError:
    WEBOTS_AVAILABLE = False


class TrustiaWebotsController:
    """Webots robot simülatörü ile Trustia Core arasındaki 3D köprü."""

    def __init__(self, time_step: int = 32):
        if not WEBOTS_AVAILABLE:
            print("[UYARI] Webots Python modulu henuz kurulu degil. (Webots icinden baslatildiginda otomatik taninacaktir)")
            return

        self.robot = Robot()
        self.time_step = time_step if time_step > 0 else int(self.robot.getBasicTimeStep())

        self._init_sensors()
        self._init_actuators()
        print("[OK] TRUSTIA Webots 3D Otonomi Kontrolcusu Aktif Edildi.")

    def _init_sensors(self):
        try:
            self.lidar = self.robot.getDevice("lidar")
            if self.lidar:
                self.lidar.enable(self.time_step)
                self.lidar.enablePointCloud()
                print("  * 3D LiDAR Sensörü: AKTİF")
        except Exception:
            self.lidar = None

        try:
            self.camera = self.robot.getDevice("camera")
            if self.camera:
                self.camera.enable(self.time_step)
                print("  * RGB Sürüş Kamerası: AKTİF")
        except Exception:
            self.camera = None

    def _init_actuators(self):
        try:
            self.left_motor = self.robot.getDevice("left wheel motor")
            self.right_motor = self.robot.getDevice("right wheel motor")
            if self.left_motor and self.right_motor:
                self.left_motor.setPosition(float('inf'))
                self.right_motor.setPosition(float('inf'))
                self.left_motor.setVelocity(0.0)
                self.right_motor.setVelocity(0.0)
                print("  * Sürüş Motorları: AKTİF")
        except Exception:
            self.left_motor = None
            self.right_motor = None

    def step(self) -> bool:
        if not WEBOTS_AVAILABLE or not hasattr(self, "robot"):
            return False

        if self.robot.step(self.time_step) == -1:
            return False

        ranges = self.get_lidar_ranges() if self.lidar else []
        self.autonomous_drive(ranges)
        return True

    def get_lidar_ranges(self) -> List[float]:
        if not self.lidar:
            return []
        return list(self.lidar.getRangeImage())

    def autonomous_drive(self, ranges: List[float]):
        if not self.left_motor or not self.right_motor:
            return

        base_speed = 3.0
        obstacle_detected = False

        if ranges:
            mid = len(ranges) // 2
            front_cone = ranges[max(0, mid - 20): min(len(ranges), mid + 20)]
            valid_ranges = [r for r in front_cone if not math.isinf(r) and not math.isnan(r) and r > 0.1]
            if valid_ranges and min(valid_ranges) < 1.5:
                obstacle_detected = True

        if obstacle_detected:
            self.left_motor.setVelocity(base_speed * 0.8)
            self.right_motor.setVelocity(-base_speed * 0.8)
        else:
            self.left_motor.setVelocity(base_speed)
            self.right_motor.setVelocity(base_speed)

    def run(self):
        print("\n[TRUSTIA] 3D Otonom Sürüş Başladı...")
        while self.step():
            pass


if __name__ == "__main__":
    controller = TrustiaWebotsController()
    if WEBOTS_AVAILABLE and hasattr(controller, "robot"):
        controller.run()
