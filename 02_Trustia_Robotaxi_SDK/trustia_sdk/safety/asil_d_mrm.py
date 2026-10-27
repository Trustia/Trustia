"""
TRUSTIA Otonomi Platformu — ISO 26262 ASIL-D Emniyet Denetleyicisi & MRM Durum Makinesi.
Minimal Risk Maneuver (MRM) Güvenli Durma ve Emniyetli Şeride Çekilme Motoru.

Standart: ISO 26262:2018 ASIL-D • UN/ECE R157 ALKS • 1 Aralık 2024 Resmî Gazete Otonom Tebliği.
"""

from __future__ import annotations

import enum
import time
from dataclasses import dataclass
from typing import Tuple, Optional


class SafetyState(enum.Enum):
    """ASIL-D Otonomi Emniyet Durumları."""
    MANUAL_OVERRIDE     = 0   # Sürücü/Teknisyen müdahalesi (Direksiyon/pedal dokunuldu)
    NOMINAL_AUTONOMOUS  = 1   # Seviye-4 Tam Otonom Sürüş Nominal
    DEGRADED_CAUTION    = 2   # Performans Düşüşü (Sensör kirli/sis, hız 20 km/s'ye çekildi)
    MRM_SAFE_PULLOVER   = 3   # Güvenli Şerit Kenarına Çekilme (Safe Stop Maneuver)
    MRM_EMERGENCY_STOP  = 4   # Kritik Acil Frenleme (Maksimum 6.5 m/s2 ile tam duruş)


@dataclass
class SafetyDiagnostics:
    """Anlık Güvenlik Teşhis Özeti."""
    state: SafetyState
    last_heartbeat_age_ms: float
    cross_track_error_m: float
    active_fault_code: str
    can_bus_healthy: bool
    perception_healthy: bool
    safe_to_drive: bool


class AsilDSafetySupervisor:
    """
    ISO 26262 ASIL-D Güvenlik Gözetmeni (Safety Supervisor).
    50 milisaniye periyotlu donanımsal gözetim köpeği (Watchdog) ve MRM yöneticisi.
    """

    def __init__(
        self,
        watchdog_timeout_ms: float = 50.0,
        self_check_interval_ms: float = 20.0,
        human_override_response_ms: float = 5.0,
        max_cross_track_m: float = 0.50,
        safe_pullover_decel_mps2: float = 1.5,
        emergency_stop_decel_mps2: float = 6.5
    ) -> None:
        self.watchdog_timeout_ms = watchdog_timeout_ms
        self.self_check_interval_ms = self_check_interval_ms
        self.human_override_response_ms = human_override_response_ms
        self.max_cross_track = max_cross_track_m
        self.safe_pullover_decel = safe_pullover_decel_mps2
        self.mrm_decel = emergency_stop_decel_mps2

        self.current_state = SafetyState.NOMINAL_AUTONOMOUS
        self.last_heartbeat_time = time.time()
        self.last_fault_reason = "NONE"
        self.state_enter_time = time.time()

    def feed_watchdog(self) -> None:
        """50 Hz ana otonomi döngüsü tarafından çağrılır (Canlılık kanıtı)."""
        self.last_heartbeat_time = time.time()

    def evaluate_safety(
        self,
        cross_track_error_m: float,
        can_bus_ok: bool,
        calmcar_arbiter_alert: bool,
        driver_takeover_detected: bool = False
    ) -> SafetyDiagnostics:
        """
        Her 10 milisaniyede bir tüm kritik alt sistemlerin emniyet durumunu denetler.
        """
        now = time.time()
        heartbeat_age_ms = (now - self.last_heartbeat_time) * 1000.0

        # 1. Öncelikli Kural: Manuel Müdahale (Driver Takeover)
        if driver_takeover_detected:
            self.current_state = SafetyState.MANUAL_OVERRIDE
            self.last_fault_reason = "DRIVER_MANUAL_TORQUE_OVERRIDE"
            return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, False)

        # 2. Öncelikli Kural: Watchdog Zaman Aşımı (>50ms sessizlik)
        if heartbeat_age_ms > self.watchdog_timeout_ms:
            self.current_state = SafetyState.MRM_EMERGENCY_STOP
            self.last_fault_reason = f"WATCHDOG_TIMEOUT_{heartbeat_age_ms:.1f}MS"
            return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, False)

        # 3. Öncelikli Kural: CAN-FD Veri Yolu Kesintisi
        if not can_bus_ok:
            self.current_state = SafetyState.MRM_EMERGENCY_STOP
            self.last_fault_reason = "CAN_FD_BUS_COMMUNICATION_FAULT"
            return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, False)

        # 4. Öncelikli Kural: Algı / Çarpışma Riski (CalmCar / LiDAR TTC Uyarısı)
        if calmcar_arbiter_alert:
            self.current_state = SafetyState.MRM_EMERGENCY_STOP
            self.last_fault_reason = "CRITICAL_COLLISION_HAZARD_TTC"
            return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, False)

        # 5. Yanal Sapma Toleransı (Şeritten 50 cm'den fazla kayma)
        if abs(cross_track_error_m) > self.max_cross_track:
            self.current_state = SafetyState.DEGRADED_CAUTION
            self.last_fault_reason = f"LANE_DRIFT_EXCESSIVE_{cross_track_error_m:.2f}M"
            return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, True)

        # Her şey normalse
        self.current_state = SafetyState.NOMINAL_AUTONOMOUS
        self.last_fault_reason = "NONE"
        return self._build_diagnostics(heartbeat_age_ms, cross_track_error_m, can_bus_ok, True)

    def _build_diagnostics(
        self,
        hb_age_ms: float,
        cte_m: float,
        can_ok: bool,
        perception_ok: bool
    ) -> SafetyDiagnostics:
        safe = (self.current_state == SafetyState.NOMINAL_AUTONOMOUS)
        return SafetyDiagnostics(
            state=self.current_state,
            last_heartbeat_age_ms=hb_age_ms,
            cross_track_error_m=cte_m,
            active_fault_code=self.last_fault_reason,
            can_bus_healthy=can_ok,
            perception_healthy=perception_ok,
            safe_to_drive=safe
        )

    def get_mrm_deceleration(self) -> float:
        """MRM durumuna göre uygulanması gereken güvenli frenleme ivmesini (m/s2) verir."""
        if self.current_state == SafetyState.MRM_EMERGENCY_STOP:
            return -self.mrm_decel # Sert ve acil duruş (-6.5 m/s2)
        elif self.current_state == SafetyState.MRM_SAFE_PULLOVER:
            return -self.safe_pullover_decel # Kontrollü yavaşlama ve sağa çekilme (-1.5 m/s2)
        elif self.current_state == SafetyState.DEGRADED_CAUTION:
            return -1.0 # Hızı güvenli seviyeye çekme (-1.0 m/s2)
        return 0.0
