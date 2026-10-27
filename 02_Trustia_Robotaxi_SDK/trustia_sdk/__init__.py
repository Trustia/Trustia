"""
TRUSTIA Otonomi Teknolojileri — Seviye-4 Robotaksi Kurumsal SDK (v2.4-Enterprise).
Milli Otonom Sürüş Güvenlik Hakemi, CAN-FD Denetleyici ve Seyrüsefer Motoru.

Fikri Mülkiyet Sahibi: Murat Furkan Bayram (%100 Hisse)
Referans Platform: SAIC Maxus MIFA 7 Elektrikli MPV
Standartlar: ISO 26262 ASIL-D • ISO 11898-1 CAN-FD • UN/ECE R157 • KVKK m.9 Uyumlu
"""

from __future__ import annotations

__version__ = "2.4.0-enterprise"
__author__ = "Murat Furkan Bayram (Trustia AI)"
__license__ = "Proprietary Commercial Enterprise License"

from trustia_sdk.core.licensing import LicenseManager
from trustia_sdk.core.transforms import Pose2D, KinematicState
from trustia_sdk.canbus.mifa7_canfd import Mifa7CanFdBridge, CanFdFrame
from trustia_sdk.safety.asil_d_mrm import AsilDSafetySupervisor, SafetyState
from trustia_sdk.planning.hybrid_astar import HybridAStarPlanner
from trustia_sdk.control.stanley_controller import StanleyController
from trustia_sdk.perception.calmcar_bridge import CalmCarSafetyArbiter
from trustia_sdk.perception.curb_detector import CurbBoundaryDetector, RoadCorridorResult
from trustia_sdk.safety.odd_sotif_dssad import (
    OddBoundaryConfig,
    OddDomainMonitor,
    Iso21448SotifSupervisor,
    UnR157DssadBlackbox,
    DssadRecord,
)
from trustia_sdk.fleet.teleoperation import TeleoperationSupervisor, RemoteOperatorCommand
from trustia_sdk.core.carla_bridge import RobotaxiCarlaBridge, CarlaStepState
from trustia_sdk.safety.can_ids_r155 import UnR155CanBusIds, CanFrameSecurityEvent
from trustia_sdk.perception.lidar_deskew_ptp import LidarMotionDeskewer, RawTimedPoint3D, PtpSyncStatus
from trustia_sdk.planning.lanelet2_rules import Lanelet2TrafficRuleEngine, LaneletSegment, RightOfWayDecision
from trustia_sdk.fleet.cabin_bms_safety import (
    RobotaxiCabinAndBmsSupervisor,
    CabinDoorSeatStatus,
    BatteryThermalState,
    CabinSafetyDecision,
)
from trustia_sdk.safety.rss_ieee2846 import ResponsibilitySensitiveSafety, RssParameters, RssSafetyVerdict
from trustia_sdk.planning.frenet_lattice_planner import FrenetLatticePlanner, FrenetState, FrenetCandidateTrajectory
from trustia_sdk.control.mpc_redundant_control import (
    RecedingHorizonMPC,
    MpcControlSolution,
    RedundantActuatorAllocator,
    RedundantActuatorAllocation,
)
from trustia_sdk.safety.sums_un_r156 import UnR156SumsManager, SoftwareUpdatePackage, SumsUpdateResult
from trustia_sdk.perception.ehmi_siren_detector import ExternalHmiAndSirenSupervisor, EhmiAndSirenDecision

__all__ = [
    "__version__",
    "LicenseManager",
    "Pose2D",
    "KinematicState",
    "Mifa7CanFdBridge",
    "CanFdFrame",
    "AsilDSafetySupervisor",
    "SafetyState",
    "HybridAStarPlanner",
    "StanleyController",
    "CalmCarSafetyArbiter",
    "CurbBoundaryDetector",
    "RoadCorridorResult",
    "OddBoundaryConfig",
    "OddDomainMonitor",
    "Iso21448SotifSupervisor",
    "UnR157DssadBlackbox",
    "DssadRecord",
    "TeleoperationSupervisor",
    "RemoteOperatorCommand",
    "RobotaxiCarlaBridge",
    "CarlaStepState",
    "UnR155CanBusIds",
    "CanFrameSecurityEvent",
    "LidarMotionDeskewer",
    "RawTimedPoint3D",
    "PtpSyncStatus",
    "Lanelet2TrafficRuleEngine",
    "LaneletSegment",
    "RightOfWayDecision",
    "RobotaxiCabinAndBmsSupervisor",
    "CabinDoorSeatStatus",
    "BatteryThermalState",
    "CabinSafetyDecision",
    "ResponsibilitySensitiveSafety",
    "RssParameters",
    "RssSafetyVerdict",
    "FrenetLatticePlanner",
    "FrenetState",
    "FrenetCandidateTrajectory",
    "RecedingHorizonMPC",
    "MpcControlSolution",
    "RedundantActuatorAllocator",
    "RedundantActuatorAllocation",
    "UnR156SumsManager",
    "SoftwareUpdatePackage",
    "SumsUpdateResult",
    "ExternalHmiAndSirenSupervisor",
    "EhmiAndSirenDecision",
]
