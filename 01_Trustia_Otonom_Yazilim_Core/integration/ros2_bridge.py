"""
TRUSTIA Entegrasyon Katmanı - ROS 2 (Robot Operating System 2) Köprüsü.

Sıfır Dış Bağımlılıklı ROS 2 Mesaj ve Düğüm Dönüştürücü:
  * `geometry_msgs/Twist` <-> TRUSTIA Sürüş Komutu
  * `nav_msgs/Odometry` <-> TRUSTIA Poz ve Odometri
  * `sensor_msgs/LaserScan` <-> TRUSTIA Lazer Noktaları
  * ROS 2 QoS Profilleri (SensorData / Reliable Command)
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class Ros2QosPolicy(Enum):
    """ROS 2 Servis Kalitesi (QoS) Politikaları."""
    RELIABLE = "RELIABLE"
    BEST_EFFORT = "BEST_EFFORT"


@dataclass
class Ros2QosProfile:
    """ROS 2 Konu Abonelik/Yayın QoS Profili."""
    reliability: Ros2QosPolicy = Ros2QosPolicy.RELIABLE
    depth: int = 10

    @classmethod
    def sensor_data(cls) -> "Ros2QosProfile":
        return cls(reliability=Ros2QosPolicy.BEST_EFFORT, depth=5)

    @classmethod
    def command_control(cls) -> "Ros2QosProfile":
        return cls(reliability=Ros2QosPolicy.RELIABLE, depth=1)


@dataclass
class Ros2Header:
    """ROS 2 std_msgs/Header standart başlığı."""
    stamp_sec: int = 0
    stamp_nanosec: int = 0
    frame_id: str = "base_link"

    @classmethod
    def now(cls, frame_id: str = "base_link") -> "Ros2Header":
        now_f = time.time()
        sec = int(now_f)
        nsec = int((now_f - sec) * 1e9)
        return cls(stamp_sec=sec, stamp_nanosec=nsec, frame_id=frame_id)


@dataclass
class Ros2Twist:
    """ROS 2 geometry_msgs/Twist standart mesajı."""
    linear_x: float = 0.0
    linear_y: float = 0.0
    angular_z: float = 0.0


@dataclass
class Ros2LaserScan:
    """ROS 2 sensor_msgs/LaserScan standart mesajı."""
    header: Ros2Header = field(default_factory=Ros2Header.now)
    angle_min: float = -math.pi
    angle_max: float = math.pi
    angle_increment: float = 0.01
    ranges: List[float] = field(default_factory=list)


@dataclass
class Ros2Odometry:
    """ROS 2 nav_msgs/Odometry standart mesajı."""
    header: Ros2Header = field(default_factory=lambda: Ros2Header.now("odom"))
    child_frame_id: str = "base_link"
    pos_x: float = 0.0
    pos_y: float = 0.0
    pos_z: float = 0.0
    yaw_rad: float = 0.0
    speed_mps: float = 0.0


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
    def drive_command_to_twist(speed_mps: float, steer_rad: float) -> Ros2Twist:
        """TRUSTIA sürüş komutunu ROS 2 Twist formatına çevirir."""
        return Ros2Twist(linear_x=speed_mps, angular_z=steer_rad)

    @staticmethod
    def laser_points_to_ros2_scan(points: List[Any], min_angle: float = -math.pi, max_angle: float = math.pi) -> Ros2LaserScan:
        """TRUSTIA Lazer noktalarını ROS 2 LaserScan formatına çevirir."""
        ranges = [getattr(p, "range_m", 0.0) for p in points]
        inc = (max_angle - min_angle) / max(1, len(points))
        return Ros2LaserScan(
            header=Ros2Header.now("lidar_frame"),
            angle_min=min_angle,
            angle_max=max_angle,
            angle_increment=inc,
            ranges=ranges,
        )

    @staticmethod
    def pose_to_ros2_odometry(east_m: float, north_m: float, yaw_rad: float, speed_mps: float = 0.0) -> Ros2Odometry:
        """TRUSTIA Pozunu ROS 2 Odometry mesajına dönüştürür."""
        return Ros2Odometry(
            header=Ros2Header.now("odom"),
            pos_x=east_m,
            pos_y=north_m,
            yaw_rad=yaw_rad,
            speed_mps=speed_mps,
        )
