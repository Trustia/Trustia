"""
TRUSTIA Robotaksi Yolcu Kabin Güvenliği, Kapı Kilidi (Door Interlock) ve EV Batarya/Termal Yöneticisi
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CabinDoorSeatStatus:
    all_doors_closed: bool
    trunk_closed: bool
    passenger_seated: bool
    seatbelt_fastened: bool
    passenger_sos_pressed: bool = False


@dataclass(frozen=True)
class BatteryThermalState:
    soc_percent: float
    pack_temp_c: float
    estimated_range_km: float


@dataclass(frozen=True)
class CabinSafetyDecision:
    dispatch_allowed: bool
    motion_inhibit_brake_hold: bool
    trigger_passenger_mrm: bool
    intercom_call_center_active: bool
    fleet_state_recommendation: str
    max_power_derating_ratio: float
    reason: str


class RobotaxiCabinAndBmsSupervisor:
    """Ticari Robotaksi yolcu kabin emniyeti ve EV batarya/termal koruma yöneticisi."""

    def __init__(
        self,
        min_dispatch_soc_percent: float = 18.0,
        thermal_derate_temp_c: float = 48.0,
    ) -> None:
        self.min_dispatch_soc_percent = min_dispatch_soc_percent
        self.thermal_derate_temp_c = thermal_derate_temp_c

    def evaluate(
        self,
        cabin: CabinDoorSeatStatus,
        bms: BatteryThermalState,
        vehicle_speed_mps: float,
    ) -> CabinSafetyDecision:
        if cabin.passenger_sos_pressed:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=(vehicle_speed_mps < 0.2),
                trigger_passenger_mrm=True,
                intercom_call_center_active=True,
                fleet_state_recommendation="PASSENGER_SOS_MRM",
                max_power_derating_ratio=0.5,
                reason="Yolcu SOS sağa çekme talebi aktif.",
            )
        if not cabin.all_doors_closed or not cabin.trunk_closed:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=True,
                trigger_passenger_mrm=(vehicle_speed_mps > 0.5),
                intercom_call_center_active=False,
                fleet_state_recommendation="HOLD_DOOR_OR_BELT",
                max_power_derating_ratio=0.0,
                reason="Kapı/bagaj emniyet kilidi aktif.",
            )
        if cabin.passenger_seated and not cabin.seatbelt_fastened and vehicle_speed_mps < 0.5:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=True,
                trigger_passenger_mrm=False,
                intercom_call_center_active=False,
                fleet_state_recommendation="HOLD_DOOR_OR_BELT",
                max_power_derating_ratio=0.0,
                reason="Yolcu emniyet kemeri takılı değil.",
            )
        power_ratio = 0.65 if bms.pack_temp_c >= self.thermal_derate_temp_c else 1.0
        if bms.soc_percent < self.min_dispatch_soc_percent and not cabin.passenger_seated:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=False,
                trigger_passenger_mrm=False,
                intercom_call_center_active=False,
                fleet_state_recommendation="RETURN_TO_CHARGER",
                max_power_derating_ratio=power_ratio,
                reason="Düşük batarya SoC — şarj istasyonuna dönüş.",
            )
        return CabinSafetyDecision(
            dispatch_allowed=True,
            motion_inhibit_brake_hold=False,
            trigger_passenger_mrm=False,
            intercom_call_center_active=False,
            fleet_state_recommendation="IN_RIDE" if cabin.passenger_seated else "READY_FOR_PASSENGER",
            max_power_derating_ratio=power_ratio,
            reason="Kabin ve batarya durumu uygun.",
        )
