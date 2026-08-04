"""
TRUSTIA Sistem 8 - ROS 2 Köprü Modülü Birim Testleri.
"""

import math
import pytest
from integration.ros2_bridge import Ros2Bridge, Ros2Twist
from perception.types import LaserPoint


def test_ros2_twist_conversion():
    twist = Ros2Twist(linear_x=2.5, angular_z=0.15)
    cmd = Ros2Bridge.twist_to_drive_command(twist)
    assert cmd["speed_mps"] == 2.5
    assert cmd["steer_rad"] == 0.15


def test_ros2_laserscan_conversion():
    pts = [LaserPoint(5.0, 0.0), LaserPoint(8.0, 0.1)]
    scan = Ros2Bridge.laser_points_to_ros2_scan(pts)
    assert len(scan.ranges) == 2
    assert scan.ranges[0] == 5.0
