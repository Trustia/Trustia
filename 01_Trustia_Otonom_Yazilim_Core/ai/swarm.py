"""
TRUSTIA Yapay Zeka - Sürü Otonomisi ve Çoklu İKA Formasyon Koordinatörü (Swarm Intelligence).

Kabiliyetler:
  * Çoklu İnsansız Kara Aracı (İKA) Sürü Koordinasyonu
  * Dinamik Formasyon Yapıları (Kama / Wedge, Saf / Line, Kolon / Column, Baklava / Diamond)
  * Lider-Takipçi (Leader-Follower) Nispi Konum Hesaplama
  * Gerçek Zamanlı Tehlike ve Harita Paylaşımı (Swarm Map Fusion)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, List, Optional, Tuple, Any

import numpy as np


class FormationType(IntEnum):
    """Sürü Düzen ve Formasyon Tipleri."""
    LINE = 1     # Yan Yana Saf Düzeni (Geniş alan tarama)
    COLUMN = 2   # Peş Peşe Kolon Düzeni (Dar geçit / tünel)
    WEDGE = 3    # Kama Düzeni (Hücum / devriye)
    DIAMOND = 4  # Baklava Düzeni (360 derece çevre emniyeti)


@dataclass
class SwarmAgentState:
    """Sürüdeki Tekil Araç Durumu."""
    agent_id: str
    is_leader: bool
    east_m: float
    north_m: float
    heading_rad: float
    speed_mps: float = 0.0
    battery_pct: float = 100.0


class SwarmCoordinator:
    """Askeri Sınıf Sürü Zekası ve Formasyon Motoru."""

    def __init__(self, leader_id: str, formation: FormationType = FormationType.WEDGE, spacing_m: float = 5.0) -> None:
        self.leader_id = leader_id
        self.formation = formation
        self.spacing_m = spacing_m
        self.agents: Dict[str, SwarmAgentState] = {}

    def register_agent(self, agent: SwarmAgentState) -> None:
        """Sürüye yeni araç kaydeder."""
        self.agents[agent.agent_id] = agent

    def compute_formation_targets(self) -> Dict[str, Tuple[float, float]]:
        """Lider aracın konum ve yönüne göre diğer takipçilerin alması gereken formasyon hedeflerini hesaplar."""
        if self.leader_id not in self.agents:
            return {}

        leader = self.agents[self.leader_id]
        targets: Dict[str, Tuple[float, float]] = {self.leader_id: (leader.east_m, leader.north_m)}

        followers = [aid for aid in self.agents.keys() if aid != self.leader_id]
        followers.sort()

        cos_h = math.cos(leader.heading_rad)
        sin_h = math.sin(leader.heading_rad)

        for idx, fid in enumerate(followers):
            slot = idx + 1
            dx, dy = 0.0, 0.0

            if self.formation == FormationType.LINE:
                offset_x = (slot if slot % 2 != 0 else -slot) * self.spacing_m
                dx = offset_x * cos_h
                dy = offset_x * sin_h

            elif self.formation == FormationType.COLUMN:
                offset_y = -slot * self.spacing_m
                dx = -offset_y * sin_h
                dy = offset_y * cos_h

            elif self.formation == FormationType.WEDGE:
                side = 1 if slot % 2 != 0 else -1
                rank = (slot + 1) // 2
                offset_x = side * rank * self.spacing_m
                offset_y = -rank * self.spacing_m
                # Body frame to ENU frame transformation
                dx = offset_x * cos_h - offset_y * sin_h
                dy = offset_x * sin_h + offset_y * cos_h

            elif self.formation == FormationType.DIAMOND:
                if slot == 1:
                    offset_x, offset_y = -self.spacing_m, -self.spacing_m
                elif slot == 2:
                    offset_x, offset_y = self.spacing_m, -self.spacing_m
                else:
                    offset_x, offset_y = 0.0, -2.0 * self.spacing_m
                dx = offset_x * cos_h - offset_y * sin_h
                dy = offset_x * sin_h + offset_y * cos_h

            target_e = leader.east_m + dx
            target_n = leader.north_m + dy
            targets[fid] = (target_e, target_n)

        return targets
