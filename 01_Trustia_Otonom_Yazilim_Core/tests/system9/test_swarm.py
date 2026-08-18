"""
TRUSTIA Sistem 9 - Sürü Otonomisi ve Formasyon Koordinatörü Birim Testleri.
"""

import math
import pytest
from ai.swarm import SwarmCoordinator, SwarmAgentState, FormationType


def test_swarm_wedge_formation():
    coordinator = SwarmCoordinator(leader_id="IKA-01", formation=FormationType.WEDGE, spacing_m=5.0)
    leader = SwarmAgentState("IKA-01", is_leader=True, east_m=100.0, north_m=100.0, heading_rad=0.0)
    follower1 = SwarmAgentState("IKA-02", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=0.0)
    follower2 = SwarmAgentState("IKA-03", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=0.0)

    coordinator.register_agent(leader)
    coordinator.register_agent(follower1)
    coordinator.register_agent(follower2)

    targets = coordinator.compute_formation_targets()
    assert len(targets) == 3
    assert targets["IKA-01"] == (100.0, 100.0)
    # Target positions around leader
    assert "IKA-02" in targets
    assert "IKA-03" in targets
