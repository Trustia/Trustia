"""
TRUSTIA Otonomi Platformu — Coklu IKA Suru Otonomisi ve Formasyon Demosu.
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.swarm import SwarmCoordinator, SwarmAgentState, FormationType


def main():
    print("=========================================================================")
    print("  TRUSTIA COKLU IKA SURU OTONOMISI VE FORMASYON KONTROL DEMOSU ")
    print("=========================================================================\n")

    # Sürü Koordinatörünü Başlat (Lider: IKA-ALPHA, Formasyon: KAMA / WEDGE)
    coordinator = SwarmCoordinator(leader_id="IKA-ALPHA", formation=FormationType.WEDGE, spacing_m=8.0)

    # 4 Adet İKA Sürüye Kaydediliyor
    leader = SwarmAgentState("IKA-ALPHA", is_leader=True, east_m=50.0, north_m=50.0, heading_rad=0.0, speed_mps=1.5)
    f1 = SwarmAgentState("IKA-BRAVO", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=0.0)
    f2 = SwarmAgentState("IKA-CHARLIE", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=0.0)
    f3 = SwarmAgentState("IKA-DELTA", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=0.0)

    for agent in [leader, f1, f2, f3]:
        coordinator.register_agent(agent)

    print("[1/2] Lider IKA-ALPHA Konumu: ENU(50.0m, 50.0m) | Yonis: 0 derece | Formasyon: KAMA (WEDGE)")

    targets = coordinator.compute_formation_targets()

    print("\n[2/2] Surudeki Takipci IKAlarin Otonom Formasyon Hedef Konumlari:\n")
    for aid, (e, n) in targets.items():
        role = "LIDER" if aid == "IKA-ALPHA" else "TAKIPCI"
        print(f"  * [{aid}] ({role:<7}): Hedef ENU Konumu -> East: {e:6.1f}m | North: {n:6.1f}m")

    print("\n[SONUC] SURU OTONOMISI TAMAMLANDI: Tum araçlar lideri otonom takip formasyonuna alindi!")
    print("=========================================================================\n")


if __name__ == "__main__":
    main()
