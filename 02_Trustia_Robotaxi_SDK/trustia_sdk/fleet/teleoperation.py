"""
TRUSTIA Robotaksi SDK — Uzaktan Operasyon (Teleoperation) & Çağrı Merkezi Müdahale Köprüsü.
Tripy Mobility Filo Kontrol Merkezi ile Seviye-4 Robotaksi arasındaki düşük gecikmeli,
hız sınırlandırmalı (maksimum 15 km/s) ve ASIL-D korumalı uzaktan kumanda/rehberlik modülü.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class RemoteOperatorCommand:
    operator_id: str
    session_token: str
    target_steer_deg: float
    target_speed_kmh: float
    emergency_stop: bool = False
    network_rtt_ms: float = 25.0
    timestamp: float = 0.0


class TeleoperationSupervisor:
    """
    Uzaktan Operatör Müdahale Denetleyicisi.
    Ağ gecikmesi 150 ms'yi aşarsa veya hız 15 km/s üstüne çıkarsa komutu otomatik sınırlar.
    """

    def __init__(
        self,
        max_remote_speed_kmh: float = 15.0,
        max_network_rtt_ms: float = 150.0,
        max_steer_deg: float = 25.0,
    ) -> None:
        self.max_speed_kmh = max_remote_speed_kmh
        self.max_rtt_ms = max_network_rtt_ms
        self.max_steer_deg = max_steer_deg
        self.active_session: bool = False
        self.current_operator: Optional[str] = None

    def authorize_and_filter(
        self, cmd: RemoteOperatorCommand
    ) -> Tuple[bool, float, float, str]:
        """
        Dönüş: (Komut Geçerli mi, Güvenli Direksiyon Derecesi, Güvenli Hız m/s, Durum)
        """
        if cmd.emergency_stop:
            return False, 0.0, 0.0, "REMOTE_OPERATOR_ESTOP_TRIGGERED"

        if cmd.network_rtt_ms > self.max_rtt_ms:
            return False, 0.0, 0.0, f"TELEOP_RTT_TOO_HIGH_{cmd.network_rtt_ms:.0f}MS_MRM_PULLOVER"

        if not cmd.session_token or len(cmd.session_token) < 8:
            return False, 0.0, 0.0, "UNAUTHORIZED_TELEOP_SESSION"

        self.active_session = True
        self.current_operator = cmd.operator_id

        safe_steer = max(-self.max_steer_deg, min(self.max_steer_deg, cmd.target_steer_deg))
        safe_speed_kmh = max(0.0, min(self.max_speed_kmh, cmd.target_speed_kmh))
        return True, safe_steer, round(safe_speed_kmh / 3.6, 3), "TELEOP_ACTIVE_SAFE"
