"""
TRUSTIA UN R155 & ISO/SAE 21434 Otomotiv Siber Güvenlik ve CAN-FD Saldırı Tespit Sistemi (CAN-IDPS)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CanIdProfile:
    arbitration_id: int
    name: str
    nominal_interval_ms: float
    min_allowed_interval_ms: float
    expected_dlc: int
    has_rolling_counter: bool = True


@dataclass(frozen=True)
class CanFrameSecurityEvent:
    timestamp_ms: float
    arbitration_id: int
    accepted: bool
    threat_type: str
    severity: str
    recommended_action: str
    detail: str


class UnR155CanBusIds:
    """UN/ECE R155 ve ISO/SAE 21434 uyumlu CAN-FD Saldırı Tespit ve Önleme Sistemi."""

    def __init__(self, profiles: Optional[Dict[int, CanIdProfile]] = None) -> None:
        if profiles is None:
            profiles = {
                0x120: CanIdProfile(0x120, "ADCU_Steering_Cmd", 10.0, 4.0, 8, True),
                0x122: CanIdProfile(0x122, "ADCU_Longitudinal_Cmd", 10.0, 4.0, 8, True),
                0x101: CanIdProfile(0x101, "ADCU_Emergency_MRM", 10.0, 2.0, 8, True),
                0x130: CanIdProfile(0x130, "ADCU_Safety_Heartbeat", 20.0, 8.0, 8, True),
            }
        self.profiles: Dict[int, CanIdProfile] = dict(profiles)
        self._last_rx_time_ms: Dict[int, float] = {}
        self._last_counter: Dict[int, int] = {}
        self.security_log: List[CanFrameSecurityEvent] = []

    def inspect_frame(
        self,
        arbitration_id: int,
        payload: bytes,
        timestamp_ms: float,
        rolling_counter: Optional[int] = None,
    ) -> CanFrameSecurityEvent:
        if arbitration_id not in self.profiles:
            ev = CanFrameSecurityEvent(
                timestamp_ms=timestamp_ms,
                arbitration_id=arbitration_id,
                accepted=False,
                threat_type="UNAUTHORIZED_ID",
                severity="CRITICAL",
                recommended_action="TRIGGER_MRM_ISOLATION",
                detail=f"Yetkisiz CAN ID: 0x{arbitration_id:03X}",
            )
            self.security_log.append(ev)
            return ev

        profile = self.profiles[arbitration_id]
        if len(payload) != profile.expected_dlc:
            ev = CanFrameSecurityEvent(
                timestamp_ms=timestamp_ms,
                arbitration_id=arbitration_id,
                accepted=False,
                threat_type="DLC_MISMATCH",
                severity="WARNING",
                recommended_action="DROP_FRAME",
                detail=f"{profile.name} DLC uyuşmazlığı.",
            )
            self.security_log.append(ev)
            return ev

        if arbitration_id in self._last_rx_time_ms:
            dt_ms = timestamp_ms - self._last_rx_time_ms[arbitration_id]
            if 0.0 <= dt_ms < profile.min_allowed_interval_ms:
                ev = CanFrameSecurityEvent(
                    timestamp_ms=timestamp_ms,
                    arbitration_id=arbitration_id,
                    accepted=False,
                    threat_type="DOS_FLOODING",
                    severity="CRITICAL",
                    recommended_action="TRIGGER_MRM_ISOLATION",
                    detail=f"{profile.name} DoS saldırısı: dt={dt_ms:.2f} ms",
                )
                self.security_log.append(ev)
                return ev

        if profile.has_rolling_counter and rolling_counter is not None:
            rc = rolling_counter & 0x0F
            if arbitration_id in self._last_counter:
                prev_rc = self._last_counter[arbitration_id]
                expected_rc = (prev_rc + 1) & 0x0F
                if rc != expected_rc:
                    ev = CanFrameSecurityEvent(
                        timestamp_ms=timestamp_ms,
                        arbitration_id=arbitration_id,
                        accepted=False,
                        threat_type="REPLAY_COUNTER_ERROR",
                        severity="CRITICAL" if rc == prev_rc else "WARNING",
                        recommended_action="TRIGGER_MRM_ISOLATION" if rc == prev_rc else "DROP_FRAME",
                        detail=f"{profile.name} sayaç hatası: beklenen {expected_rc}, gelen {rc}",
                    )
                    self.security_log.append(ev)
                    return ev
            self._last_counter[arbitration_id] = rc

        self._last_rx_time_ms[arbitration_id] = timestamp_ms
        return CanFrameSecurityEvent(
            timestamp_ms=timestamp_ms,
            arbitration_id=arbitration_id,
            accepted=True,
            threat_type="NONE",
            severity="INFO",
            recommended_action="ALLOW",
            detail="OK",
        )
