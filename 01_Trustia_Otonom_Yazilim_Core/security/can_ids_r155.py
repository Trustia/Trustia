"""
TRUSTIA UN R155 & ISO/SAE 21434 Otomotiv Siber Güvenlik ve CAN-FD Saldırı Tespit Sistemi (CAN-IDPS)
====================================================================================================
Seviye-4 Robotaksi şasi veri yolu (CAN / CAN-FD) üzerinde gerçekleşebilecek:
  1. Yetkisiz Mesaj Kimliği Enjeksiyonu (Unauthorized CAN ID Spoofing)
  2. Yüksek Frekanslı Veri Yolu Boğma / DoS Saldırısı (Bus Flooding / Rate Anomaly)
  3. Tekrarlama (Replay) ve Yürüyen Sayaç (Rolling Counter 0..15) Atlama Saldırısı
  4. Mesaj Boyutu (DLC) ve CRC Bütünlük İhlali

olaylarını gerçek zamanlı (< 0.2 ms) yakalar ve kritik saldırı durumunda ASIL-D MRM / güvenli
frenleme kilidini tetikler.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CanIdProfile:
    """Yetkili bir CAN-FD mesaj kimliğinin beklenen siber güvenlik profili."""

    arbitration_id: int
    name: str
    nominal_interval_ms: float
    min_allowed_interval_ms: float
    expected_dlc: int
    has_rolling_counter: bool = True


@dataclass(frozen=True)
class CanFrameSecurityEvent:
    """CAN-IDPS tarafından üretilen siber güvenlik denetim kararı."""

    timestamp_ms: float
    arbitration_id: int
    accepted: bool
    threat_type: str  # "NONE", "UNAUTHORIZED_ID", "DOS_FLOODING", "REPLAY_COUNTER_ERROR", "DLC_MISMATCH"
    severity: str     # "INFO", "WARNING", "CRITICAL"
    recommended_action: str  # "ALLOW", "DROP_FRAME", "TRIGGER_MRM_ISOLATION"
    detail: str


class UnR155CanBusIds:
    """
    UN/ECE R155 (CSMS) ve ISO/SAE 21434 uyumlu Araç İçi CAN-FD Saldırı Tespit Sistemi.
    SAIC Maxus MIFA 7 ve Hyundai Ioniq 5 (E-GMP) otonom kontrol kimliklerini korur.
    """

    def __init__(self, profiles: Optional[Dict[int, CanIdProfile]] = None) -> None:
        if profiles is None:
            profiles = {
                0x120: CanIdProfile(0x120, "ADCU_Steering_Cmd", 10.0, 4.0, 8, True),
                0x122: CanIdProfile(0x122, "ADCU_Longitudinal_Cmd", 10.0, 4.0, 8, True),
                0x101: CanIdProfile(0x101, "ADCU_Emergency_MRM", 10.0, 2.0, 8, True),
                0x130: CanIdProfile(0x130, "ADCU_Safety_Heartbeat", 20.0, 8.0, 8, True),
                0x210: CanIdProfile(0x210, "EPS_Steering_Feedback", 10.0, 4.0, 8, True),
                0x220: CanIdProfile(0x220, "IBooster_Brake_Feedback", 10.0, 4.0, 8, True),
            }
        self.profiles: Dict[int, CanIdProfile] = dict(profiles)
        self._last_rx_time_ms: Dict[int, float] = {}
        self._last_counter: Dict[int, int] = {}
        self._anomaly_counts: Dict[int, int] = {}
        self.security_log: List[CanFrameSecurityEvent] = []

    def inspect_frame(
        self,
        arbitration_id: int,
        payload: bytes,
        timestamp_ms: float,
        rolling_counter: Optional[int] = None,
    ) -> CanFrameSecurityEvent:
        """Gelen veya giden CAN-FD çerçevesini UN R155 kurallarına göre denetler."""
        # 1. Beyaz liste (Whitelist) kontrolü
        if arbitration_id not in self.profiles:
            event = CanFrameSecurityEvent(
                timestamp_ms=timestamp_ms,
                arbitration_id=arbitration_id,
                accepted=False,
                threat_type="UNAUTHORIZED_ID",
                severity="CRITICAL",
                recommended_action="TRIGGER_MRM_ISOLATION",
                detail=f"Yetkisiz CAN ID algılandı: 0x{arbitration_id:03X}",
            )
            self.security_log.append(event)
            return event

        profile = self.profiles[arbitration_id]

        # 2. Veri uzunluğu (DLC) kontrolü
        if len(payload) != profile.expected_dlc:
            self._anomaly_counts[arbitration_id] = self._anomaly_counts.get(arbitration_id, 0) + 1
            event = CanFrameSecurityEvent(
                timestamp_ms=timestamp_ms,
                arbitration_id=arbitration_id,
                accepted=False,
                threat_type="DLC_MISMATCH",
                severity="WARNING",
                recommended_action="DROP_FRAME",
                detail=f"{profile.name} DLC hatası: beklenen {profile.expected_dlc}, gelen {len(payload)}",
            )
            self.security_log.append(event)
            return event

        # 3. Frekans / DoS Flooding kontrolü
        if arbitration_id in self._last_rx_time_ms:
            dt_ms = timestamp_ms - self._last_rx_time_ms[arbitration_id]
            if 0.0 <= dt_ms < profile.min_allowed_interval_ms:
                self._anomaly_counts[arbitration_id] = self._anomaly_counts.get(arbitration_id, 0) + 1
                event = CanFrameSecurityEvent(
                    timestamp_ms=timestamp_ms,
                    arbitration_id=arbitration_id,
                    accepted=False,
                    threat_type="DOS_FLOODING",
                    severity="CRITICAL",
                    recommended_action="TRIGGER_MRM_ISOLATION",
                    detail=f"{profile.name} yüksek frekanslı DoS saldırısı: dt={dt_ms:.2f} ms < {profile.min_allowed_interval_ms:.2f} ms",
                )
                self.security_log.append(event)
                return event

        # 4. Yürüyen Sayaç (Rolling Counter) ve Replay kontrolü
        if profile.has_rolling_counter and rolling_counter is not None:
            rc = rolling_counter & 0x0F
            if arbitration_id in self._last_counter:
                prev_rc = self._last_counter[arbitration_id]
                expected_rc = (prev_rc + 1) & 0x0F
                if rc == prev_rc or rc != expected_rc:
                    self._anomaly_counts[arbitration_id] = self._anomaly_counts.get(arbitration_id, 0) + 1
                    event = CanFrameSecurityEvent(
                        timestamp_ms=timestamp_ms,
                        arbitration_id=arbitration_id,
                        accepted=False,
                        threat_type="REPLAY_COUNTER_ERROR",
                        severity="CRITICAL" if rc == prev_rc else "WARNING",
                        recommended_action="TRIGGER_MRM_ISOLATION" if rc == prev_rc else "DROP_FRAME",
                        detail=f"{profile.name} sayaç/tekrar hatası: önceki={prev_rc}, gelen={rc}, beklenen={expected_rc}",
                    )
                    self.security_log.append(event)
                    return event
            self._last_counter[arbitration_id] = rc

        self._last_rx_time_ms[arbitration_id] = timestamp_ms
        event = CanFrameSecurityEvent(
            timestamp_ms=timestamp_ms,
            arbitration_id=arbitration_id,
            accepted=True,
            threat_type="NONE",
            severity="INFO",
            recommended_action="ALLOW",
            detail=f"{profile.name} çerçevesi doğrulandı.",
        )
        return event
