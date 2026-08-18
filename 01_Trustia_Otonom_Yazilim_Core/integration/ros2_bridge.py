"""
TRUSTIA Entegrasyon Katmanı - ROS 2 (Robot Operating System 2) Köprüsü.

Sıfır Dış Bağımlılıklı ROS 2 Mesaj Dönüştürücü:
  * `geometry_msgs/Twist` -> TRUSTIA `DriveCommand`
  * TRUSTIA `Pose2D` -> `nav_msgs/Odometry`
  * TRUSTIA `LaserPoint` listesi -> `sensor_msgs/LaserScan`
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Any


@dataclass
class Ros2Twist:
    """ROS 2 geometry_msgs/Twist standart mesajı."""
    linear_x: float = 0.0
    linear_y: float = 0.0
    angular_z: float = 0.0


@dataclass
class Ros2LaserScan:
    """ROS 2 sensor_msgs/LaserScan standart mesajı."""
    angle_min: float
    angle_max: float
    angle_increment: float
    ranges: List[float]


class Ros2Bridge:
    """TRUSTIA ve ROS 2 Mesaj Dönüştürücü Köprüsü."""

    @staticmethod
    def twist_to_drive_command(twist: Ros2Twist) -> Dict[str, float]:
        """ROS 2 Twist mesajını TRUSTIA sürüş komutuna çevirir."""
        return {
            "speed_mps": twist.linear_x,
            "steer_rad": twist.angular_z,
        }

    @staticmethod
    def laser_points_to_ros2_scan(points: List[Any], min_angle: float = -math.pi, max_angle: float = math.pi) -> Ros2LaserScan:
        """TRUSTIA Lazer noktalarını ROS 2 LaserScan formatına çevirir."""
        ranges = [getattr(p, "range_m", 0.0) for p in points]
        return Ros2LaserScan(
            angle_min=min_angle,
            angle_max=max_angle,
            angle_increment=(max_angle - min_angle) / max(1, len(points)),
            ranges=ranges,
        )
