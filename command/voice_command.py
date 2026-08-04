"""
TRUSTIA Komuta Katmanı - Taktik Sesli Komut ve İrade Çözümleyici (Voice Command & Intent Parser).

Örnek Komutlar:
  * "IKA-ALPHA, B1 bölgesine git ve devriye at"
  * "Acil durma yap"
  * "Eve dön"
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Optional, Any


@dataclass
class TacticalIntent:
    """Çözümlenmiş Taktik Komut Amacı."""
    command_type: str                   # 'NAVIGATE', 'ESTOP', 'RTH', 'PATROL'
    target_vehicle: str
    target_location: Optional[str] = None


class VoiceCommandParser:
    """Taktik Sesli ve Metinsel Komut Çözümleyici."""

    @staticmethod
    def parse_intent(text: str) -> TacticalIntent:
        """Metin komutunu okuyup taktik komut nesnesine çevirir."""
        clean = text.upper().replace("i", "İ").replace("ı", "I").strip()

        if "ACİL DUR" in clean or "ESTOP" in clean:
            return TacticalIntent(command_type="ESTOP", target_vehicle="ALL")

        if "EVE DÖN" in clean or "RTH" in clean:
            return TacticalIntent(command_type="RTH", target_vehicle="ALL")

        # Vehicle extraction
        match_veh = re.search(r"(IKA-[A-Z0-9]+)", clean)
        veh = match_veh.group(1) if match_veh else "IKA-ALPHA"

        if "DEVRİYE" in clean or "DEVRIYE" in clean or "PATROL" in clean:
            return TacticalIntent(command_type="PATROL", target_vehicle=veh, target_location="ZONE_ALPHA")

        return TacticalIntent(command_type="NAVIGATE", target_vehicle=veh, target_location="DEFAULT")
