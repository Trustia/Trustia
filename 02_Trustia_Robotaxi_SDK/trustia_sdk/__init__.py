"""
TRUSTIA Otonomi Teknolojileri — Seviye-4 Robotaksi Kurumsal SDK (v2.4-Enterprise).
Milli Otonom Sürüş Güvenlik Hakemi, CAN-FD Denetleyici ve Seyrüsefer Motoru.

Fikri Mülkiyet Sahibi: Murat Furkan Bayram (%100 Hisse)
Müşteri / Hedef Platform: Tripy Mobility & MİA Teknoloji (SAIC Maxus MIFA 7)
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
]
