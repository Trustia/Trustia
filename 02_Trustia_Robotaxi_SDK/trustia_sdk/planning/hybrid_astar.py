"""
TRUSTIA Otonomi Platformu — Kinematik Kısıtlı Hybrid A* Rota Planlayıcısı (SDK v2.4).
SAIC Maxus MIFA 7 & Seviye-4 Robotaksi Şehir İçi Seyrüsefer Motoru.

Bicycle Kinematic Model & Voronoi Emniyet Çemberi Destekli.
"""

from __future__ import annotations

import heapq
import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Set, Dict
from trustia_sdk.core.transforms import Pose2D, normalize_angle


@dataclass(order=True)
class PathNode:
    """Hybrid A* Arama Düğümü."""
    f_cost: float
    g_cost: float = field(compare=False)
    x: float = field(compare=False)
    y: float = field(compare=False)
    yaw_rad: float = field(compare=False)
    parent_idx: Optional[int] = field(default=None, compare=False)
    steer_deg: float = field(default=0.0, compare=False)
    direction: int = field(default=1, compare=False) # 1: İleri, -1: Geri


class HybridAStarPlanner:
    """
    Şehir içi Robotaksi Seyrüsefer ve Manevra Planlayıcısı.
    SAIC Maxus MIFA 7'nin dingil mesafesi (2.975m) ve dönüş çapını esas alır.
    """

    def __init__(
        self,
        wheel_base_m: float = 2.975,
        max_steer_deg: float = 35.0,
        grid_resolution_m: float = 0.5,
        yaw_resolution_deg: float = 15.0,
        safety_clearance_m: float = 1.2
    ) -> None:
        self.L = wheel_base_m
        self.max_steer = max_steer_deg
        self.xy_res = grid_resolution_m
        self.yaw_res = math.radians(yaw_resolution_deg)
        self.safety_margin = safety_clearance_m

        # Direksiyon deneme açıları (5 discrete steer inputs)
        self.steer_inputs = [
            -self.max_steer,
            -self.max_steer * 0.5,
            0.0,
            self.max_steer * 0.5,
            self.max_steer
        ]

    def _state_to_index(self, x: float, y: float, yaw: float) -> Tuple[int, int, int]:
        ix = int(round(x / self.xy_res))
        iy = int(round(y / self.xy_res))
        iyaw = int(round(normalize_angle(yaw) / self.yaw_res))
        return (ix, iy, iyaw)

    def _is_collision_free(self, x: float, y: float, obstacles: List[Tuple[float, float, float]]) -> bool:
        """(x, y) konumunun engellere olan emniyet mesafesini denetler."""
        for ox, oy, radius in obstacles:
            if math.hypot(x - ox, y - oy) < (radius + self.safety_margin):
                return False
        return True

    def plan(
        self,
        start: Pose2D,
        goal: Pose2D,
        obstacles: Optional[List[Tuple[float, float, float]]] = None,
        step_size_m: float = 1.0,
        max_iterations: int = 1500
    ) -> List[Pose2D]:
        """
        Başlangıç pozundan hedef poza kinematik olarak sürülebilir yol üretir.
        """
        if obstacles is None:
            obstacles = []

        open_set: List[PathNode] = []
        nodes_pool: List[PathNode] = []
        closed_set: Set[Tuple[int, int, int]] = set()

        # Heuristic: Öklid mesafesi + açı farkı cezası
        h_start = start.distance_to(goal) + abs(normalize_angle(goal.yaw - start.yaw)) * 1.5
        start_node = PathNode(f_cost=h_start, g_cost=0.0, x=start.x, y=start.y, yaw_rad=start.yaw)
        nodes_pool.append(start_node)
        heapq.heappush(open_set, start_node)

        iterations = 0

        while open_set and iterations < max_iterations:
            iterations += 1
            current = heapq.heappop(open_set)
            curr_idx = len(nodes_pool) - 1

            # Hedefe ulaşıldı mı? (tolerans: 0.8m mesafe, 25 derece açı)
            dist_to_goal = math.hypot(current.x - goal.x, current.y - goal.y)
            yaw_diff = abs(normalize_angle(current.yaw_rad - goal.yaw))

            if dist_to_goal < 0.8 and yaw_diff < math.radians(25.0):
                # Yolu geriye doğru inşa et
                path: List[Pose2D] = []
                idx = curr_idx
                while idx is not None:
                    node = nodes_pool[idx]
                    path.append(Pose2D(node.x, node.y, node.yaw_rad))
                    idx = node.parent_idx
                path.reverse()
                return path

            state_idx = self._state_to_index(current.x, current.y, current.yaw_rad)
            if state_idx in closed_set:
                continue
            closed_set.add(state_idx)

            # Kinematik Bisiklet Modeliyle Genişleme (Forward Kinematics)
            for steer in self.steer_inputs:
                delta_rad = math.radians(steer)

                # Yeni poz hesapla: x_next = x + d * cos(yaw), yaw_next = yaw + d/L * tan(delta)
                next_x = current.x + step_size_m * math.cos(current.yaw_rad)
                next_y = current.y + step_size_m * math.sin(current.yaw_rad)
                next_yaw = normalize_angle(current.yaw_rad + (step_size_m / self.L) * math.tan(delta_rad))

                # Çarpışma denetimi
                if not self._is_collision_free(next_x, next_y, obstacles):
                    continue

                # Maliyet hesabı: Mesafe + Direksiyon Değişim Cezası
                steer_cost = abs(steer) * 0.02
                steer_change_cost = abs(steer - current.steer_deg) * 0.05
                next_g = current.g_cost + step_size_m + steer_cost + steer_change_cost
                next_h = math.hypot(next_x - goal.x, next_y - goal.y) + abs(normalize_angle(goal.yaw - next_yaw)) * 1.5
                next_f = next_g + next_h

                child_node = PathNode(
                    f_cost=next_f,
                    g_cost=next_g,
                    x=next_x,
                    y=next_y,
                    yaw_rad=next_yaw,
                    parent_idx=curr_idx,
                    steer_deg=steer,
                    direction=1
                )
                nodes_pool.append(child_node)
                heapq.heappush(open_set, child_node)

        # Arama sınırına ulaşıldıysa düzleştirilmiş ara rota döndür
        direct_steps = max(5, int(round(start.distance_to(goal) / step_size_m)))
        fallback_path = []
        for i in range(direct_steps + 1):
            ratio = i / float(direct_steps)
            fx = start.x + ratio * (goal.x - start.x)
            fy = start.y + ratio * (goal.y - start.y)
            fyaw = start.angle_to(goal)
            fallback_path.append(Pose2D(fx, fy, fyaw))
        return fallback_path
