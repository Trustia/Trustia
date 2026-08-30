"""Trustia Teleoperation & Remote Intervention Bridge.

Implements remote dispatch, path guidance, and safety-monitored teleoperation
for Level-4 Robotaxis and tactical defense robots.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple, Optional
import time
import math


class TeleopMode(Enum):
    AUTONOMOUS = "AUTONOMOUS"
    WAYPOINT_GUIDANCE = "WAYPOINT_GUIDANCE"
    DIRECT_DRIVE = "DIRECT_DRIVE"
    REMOTE_ESTOP = "REMOTE_ESTOP"


@dataclass
class TeleopCommand:
    mode: TeleopMode
    operator_id: str
    timestamp: float
    steering_deg: float = 0.0  # [-35.0, 35.0]
    throttle_pct: float = 0.0  # [0.0, 100.0]
    brake_pct: float = 0.0     # [0.0, 100.0]
    guidance_waypoints: List[Tuple[float, float]] = field(default_factory=list)
    auth_token: str = ""


@dataclass
class TeleopState:
    active_mode: TeleopMode
    latency_ms: float
    operator_connected: bool
    link_quality_pct: float
    last_heartbeat_timestamp: float
    emergency_override_triggered: bool


class TeleoperationBridge:
    """Enterprise-grade Remote Teleoperation & Dispatch Controller with Hardware Safety Interlock."""

    def __init__(self, heartbeat_timeout_sec: float = 0.300, max_safe_teleop_speed_mps: float = 8.33):
        self.heartbeat_timeout_sec = heartbeat_timeout_sec
        self.max_safe_speed = max_safe_teleop_speed_mps
        self.state = TeleopState(
            active_mode=TeleopMode.AUTONOMOUS,
            latency_ms=0.0,
            operator_connected=False,
            link_quality_pct=100.0,
            last_heartbeat_timestamp=time.time(),
            emergency_override_triggered=False
        )
        self.guidance_path: List[Tuple[float, float]] = []

    def handle_operator_heartbeat(self, operator_id: str, client_time: float) -> TeleopState:
        """Process low-latency WebRTC heartbeat from remote operations center."""
        now = time.time()
        self.state.latency_ms = max(1.0, (now - client_time) * 1000.0)
        self.state.last_heartbeat_timestamp = now
        self.state.operator_connected = True
        self.state.link_quality_pct = max(0.0, 100.0 - (self.state.latency_ms / 5.0))
        return self.state

    def process_command(self, cmd: TeleopCommand, current_speed_mps: float, closest_obstacle_dist_m: float) -> Tuple[float, float, float, str]:
        """Validate and execute remote teleoperation command with active safety envelope.

        Returns: (steering_deg, throttle_pct, brake_pct, status_msg)
        """
        now = time.time()
        time_since_heartbeat = now - self.state.last_heartbeat_timestamp

        # 1. Watchdog Timeout Check
        if time_since_heartbeat > self.heartbeat_timeout_sec:
            self.state.emergency_override_triggered = True
            self.state.active_mode = TeleopMode.REMOTE_ESTOP
            return 0.0, 0.0, 100.0, "TIMEOUT_FAILSAFE_BRAKE"

        # 2. Remote E-STOP Check
        if cmd.mode == TeleopMode.REMOTE_ESTOP:
            self.state.active_mode = TeleopMode.REMOTE_ESTOP
            return 0.0, 0.0, 100.0, "OPERATOR_EMERGENCY_STOP"

        # 3. Obstacle Collision Override (Active Safety Guard)
        if closest_obstacle_dist_m < 2.0 and cmd.throttle_pct > 0.0:
            return cmd.steering_deg, 0.0, 100.0, "OBSTACLE_PROXIMITY_BRAKE_OVERRIDE"

        # 4. Waypoint Guidance Mode
        if cmd.mode == TeleopMode.WAYPOINT_GUIDANCE:
            self.state.active_mode = TeleopMode.WAYPOINT_GUIDANCE
            self.guidance_path = cmd.guidance_waypoints
            return 0.0, 20.0, 0.0, f"FOLLOWING_GUIDANCE_PATH_{len(self.guidance_path)}_POINTS"

        # 5. Direct Drive Mode (Speed-Capped)
        if cmd.mode == TeleopMode.DIRECT_DRIVE:
            self.state.active_mode = TeleopMode.DIRECT_DRIVE
            target_throttle = cmd.throttle_pct
            if current_speed_mps > self.max_safe_speed:
                target_throttle = 0.0  # Speed governor
            clamped_steer = max(-35.0, min(35.0, cmd.steering_deg))
            return clamped_steer, target_throttle, cmd.brake_pct, "DIRECT_DRIVE_ACTIVE"

        return 0.0, 0.0, 0.0, "AUTONOMOUS_DEFAULT"
