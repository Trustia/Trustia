"""
TRUSTIA Otonomi Platformu — Tripy Filo Telemetri ve Görev Yönetim Köprüsü (SDK v2.4).
Tripy Bulut Operasyon Merkezi & Mobil Uygulama Entegrasyon Katmanı.

Standart: JSON Telemetri Şeması • WebSocket • REST API Köprüsü.
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional
from trustia_sdk.core.transforms import KinematicState
from trustia_sdk.safety.asil_d_mrm import SafetyDiagnostics, SafetyState


@dataclass
class FleetTelemetryPacket:
    """Tripy Filo Sunucusuna Saniyede 10 Kez Gönderilen Canlı Durum Paketi."""
    vehicle_id: str
    timestamp_unix: float
    latitude: float
    longitude: float
    altitude_m: float
    speed_kmh: float
    heading_deg: float
    steering_angle_deg: float
    battery_percentage: float
    autonomy_mode: str
    safety_state: str
    active_passenger: bool
    odometer_km: float
    diagnostics_code: str

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


@dataclass
class RobotaxiMission:
    """Yolcu Çağrı / Görev Siparişi."""
    mission_id: str
    passenger_name: str
    pickup_coords: tuple[float, float]
    dropoff_coords: tuple[float, float]
    fare_tl: float
    status: str = "PENDING" # PENDING, EN_ROUTE_PICKUP, PASSENGER_ONBOARD, COMPLETED


class TripyFleetBridge:
    """
    Tripy Mobility Merkezi Filo Sunucusu ile Araç Arasındaki Telemetri Köprüsü.
    """

    def __init__(self, vehicle_id: str = "TRIPY-MIFA7-001") -> None:
        self.vehicle_id = vehicle_id
        self.active_mission: Optional[RobotaxiMission] = None
        self.battery_level = 88.5 # % SoC
        self.odometer_km = 12450.0

    def generate_telemetry_packet(
        self,
        state: KinematicState,
        safety_diag: SafetyDiagnostics,
        gnss_lat: float = 39.8688, # Ankara Bilkent Cyberpark
        gnss_lon: float = 32.7483
    ) -> FleetTelemetryPacket:
        """Canlı telemetri paketini üretir."""
        return FleetTelemetryPacket(
            vehicle_id=self.vehicle_id,
            timestamp_unix=time.time(),
            latitude=gnss_lat,
            longitude=gnss_lon,
            altitude_m=920.0,
            speed_kmh=state.velocity_kmh,
            heading_deg=math.degrees(state.yaw_rad),
            steering_angle_deg=state.steering_angle_deg,
            battery_percentage=self.battery_level,
            autonomy_mode="LEVEL_4_AUTONOMOUS" if safety_diag.safe_to_drive else "SAFETY_RESTRICTED",
            safety_state=safety_diag.state.name,
            active_passenger=(self.active_mission is not None and self.active_mission.status == "PASSENGER_ONBOARD"),
            odometer_km=self.odometer_km,
            diagnostics_code=safety_diag.active_fault_code
        )

    def dispatch_mission(self, mission: RobotaxiMission) -> bool:
        """Merkezden yeni yolcu alma görevi atar."""
        self.active_mission = mission
        self.active_mission.status = "EN_ROUTE_PICKUP"
        return True

    def remote_emergency_stop(self) -> Dict[str, Any]:
        """Tripy filo operatörünün uzaktan acil durdurma emri."""
        return {
            "command": "REMOTE_MRM_ESTOP",
            "vehicle_id": self.vehicle_id,
            "timestamp": time.time(),
            "status": "EXECUTED"
        }
