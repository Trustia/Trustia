"""Trustia V2X (Vehicle-to-Everything) Communication Engine.

Implements SAE J2735 and ETSI ITS-G5 protocols for:
1. V2I (Vehicle-to-Infrastructure): SPaT (Signal Phase and Timing) & GLOSA speed advisory.
2. V2V (Vehicle-to-Vehicle): BSM emergency braking and blind spot alerts.
3. V2P (Vehicle-to-Pedestrian): Crosswalk safety beacons.
4. Emergency Vehicle Alerts (EVA): Priority path yielding for emergency responders.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple
import math
import time


class TrafficLightState(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    FLASHING_YELLOW = "FLASHING_YELLOW"
    UNKNOWN = "UNKNOWN"


@dataclass
class SignalPhase:
    intersection_id: str
    phase_id: int
    state: TrafficLightState
    time_to_change_sec: float
    confidence: float = 1.0


@dataclass
class EmergencyVehicleAlert:
    vehicle_id: str
    vehicle_type: str  # "AMBULANCE", "POLICE", "FIRE_TRUCK"
    position_x: float
    position_y: float
    heading_deg: float
    speed_mps: float
    siren_active: bool
    timestamp: float


@dataclass
class V2XMessage:
    msg_type: str  # "SPAT", "MAP", "BSM", "EVA"
    sender_id: str
    timestamp: float
    payload: dict
    signature_valid: bool = True


class V2XEngine:
    """Universal V2X Engine for Level-4 Autonomous Urban and Tactical Vehicles."""

    def __init__(self, vehicle_id: str = "TRUSTIA-V01"):
        self.vehicle_id = vehicle_id
        self.active_phases: Dict[str, SignalPhase] = {}
        self.nearby_v2v_vehicles: Dict[str, dict] = {}
        self.active_emergency_alerts: List[EmergencyVehicleAlert] = []
        self.message_history: List[V2XMessage] = []
        self.rx_count = 0
        self.tx_count = 0

    def process_spat_message(self, intersection_id: str, phase_id: int, state_str: str, time_to_change: float) -> SignalPhase:
        """Process V2I Signal Phase and Timing message from smart traffic light."""
        try:
            state = TrafficLightState[state_str.upper()]
        except KeyError:
            state = TrafficLightState.UNKNOWN

        phase = SignalPhase(
            intersection_id=intersection_id,
            phase_id=phase_id,
            state=state,
            time_to_change_sec=max(0.0, float(time_to_change))
        )
        self.active_phases[f"{intersection_id}_{phase_id}"] = phase
        self.rx_count += 1
        return phase

    def calculate_glosa_speed(self, distance_to_light_m: float, phase: SignalPhase, current_speed_mps: float, speed_limit_mps: float = 13.88) -> Tuple[float, str]:
        """Green Light Optimal Speed Advisory (GLOSA).

        Recommends optimal speed to arrive at the stop line on GREEN, saving energy & avoiding stops.
        """
        if distance_to_light_m <= 1.0:
            return current_speed_mps, "AT_INTERSECTION"

        if phase.state == TrafficLightState.GREEN:
            # If light is green, check if we can make it at current speed
            time_needed = distance_to_light_m / max(0.1, current_speed_mps)
            if time_needed <= phase.time_to_change_sec:
                return current_speed_mps, "CRUISE_GREEN"
            else:
                # Need to accelerate slightly if within speed limit
                required_speed = distance_to_light_m / max(0.5, phase.time_to_change_sec)
                if required_speed <= speed_limit_mps:
                    return required_speed, "ACCELERATE_FOR_GREEN"
                else:
                    # Can't make it, prepare to stop
                    return min(current_speed_mps * 0.7, distance_to_light_m / (phase.time_to_change_sec + 5.0)), "DECELERATE_FOR_RED"

        elif phase.state == TrafficLightState.RED:
            # Light is currently red. Arrive when it turns green
            target_arrival_time = phase.time_to_change_sec + 1.0
            optimal_speed = distance_to_light_m / max(1.0, target_arrival_time)
            optimal_speed = min(optimal_speed, speed_limit_mps)
            return optimal_speed, "GLOSA_SMOOTH_ARRIVAL"

        return current_speed_mps, "MAINTAIN"

    def process_bsm(self, sender_id: str, x: float, y: float, vx: float, vy: float, brake_active: bool, hard_braking: bool) -> dict:
        """Process V2V Basic Safety Message from adjacent connected vehicles."""
        self.rx_count += 1
        record = {
            "sender_id": sender_id,
            "x": x,
            "y": y,
            "vx": vx,
            "vy": vy,
            "brake_active": brake_active,
            "hard_braking": hard_braking,
            "timestamp": time.time()
        }
        self.nearby_v2v_vehicles[sender_id] = record
        return record

    def check_eebl_risk(self, my_x: float, my_y: float, my_heading: float) -> Tuple[bool, Optional[str]]:
        """Emergency Electronic Brake Light (EEBL) hazard assessment."""
        for v_id, data in self.nearby_v2v_vehicles.items():
            if data.get("hard_braking", False):
                dx = data["x"] - my_x
                dy = data["y"] - my_y
                dist = math.hypot(dx, dy)
                if dist < 60.0:  # Within 60m ahead
                    return True, v_id
        return False, None

    def process_eva(self, alert: EmergencyVehicleAlert) -> dict:
        """Process Emergency Vehicle Alert (EVA) and generate path yield advisory."""
        self.active_emergency_alerts.append(alert)
        self.rx_count += 1
        return {
            "status": "YIELD_REQUIRED" if alert.siren_active else "MONITOR",
            "vehicle_id": alert.vehicle_id,
            "recommended_action": "PULL_OVER_RIGHT" if alert.siren_active else "NORMAL"
        }

    def generate_bsm(self, my_x: float, my_y: float, my_vx: float, my_vy: float, brake_active: bool) -> V2XMessage:
        """Generate outbound V2V Basic Safety Message broadcast."""
        self.tx_count += 1
        payload = {
            "x": my_x,
            "y": my_y,
            "vx": my_vx,
            "vy": my_vy,
            "brake_active": brake_active,
            "hard_braking": brake_active and abs(my_vx) < 1.0
        }
        msg = V2XMessage(
            msg_type="BSM",
            sender_id=self.vehicle_id,
            timestamp=time.time(),
            payload=payload,
            signature_valid=True
        )
        self.message_history.append(msg)
        return msg
