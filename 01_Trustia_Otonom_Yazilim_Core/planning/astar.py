"""
TRUSTIA Planning - A* Global Path Planning.

Klasik A* algoritması - optimal path bulma.
Multiple heuristic functions, configurable cost.
"""

from __future__ import annotations

import heapq
import math
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple

from core.errors import PlanningError
from planning.grid_map import GridMap
from planning.types import Path, PlanningRequest, PlanningResult, PlanningStatus, Waypoint


class HeuristicType(Enum):
    """A* heuristik fonksiyonları."""
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhattan" 
    DIAGONAL = "diagonal"
    ZERO = "zero"  # Dijkstra's algorithm


@dataclass
class AStarConfig:
    """A* konfigürasyonu."""
    heuristic: HeuristicType = HeuristicType.EUCLIDEAN
    weight: float = 1.0  # Heuristik ağırlığı (>1 = faster, suboptimal)
    diagonal_cost: float = math.sqrt(2)  # Diagonal hareket maliyeti
    allow_diagonal: bool = True
    tie_breaking: bool = True  # Heuristik tie-breaking


@dataclass
class AStarNode:
    """A* node bilgisi."""
    x: int
    y: int
    g_cost: float  # Start'tan maliyet
    h_cost: float  # Goal'e heuristik
    parent: Optional[Tuple[int, int]] = None
    
    @property
    def f_cost(self) -> float:
        return self.g_cost + self.h_cost
    
    def __lt__(self, other: "AStarNode") -> bool:
        if abs(self.f_cost - other.f_cost) < 1e-6:
            return self.h_cost < other.h_cost  # Tie breaking
        return self.f_cost < other.f_cost


class AStarPlanner:
    """A* global path planner."""

    def __init__(self, grid_map: Optional[GridMap] = None, config: AStarConfig = AStarConfig()) -> None:
        if isinstance(grid_map, AStarConfig):
            self.config = grid_map
            self.grid_map = None
        else:
            self.grid_map = grid_map
            self.config = config

    def plan(self, grid_map_or_start: Any, request_or_goal: Any = None) -> Any:
        """A* path planning."""
        if isinstance(grid_map_or_start, tuple) and isinstance(request_or_goal, tuple):
            grid_map = self.grid_map
            start_x, start_y = grid_map_or_start
            goal_x, goal_y = request_or_goal
            if not grid_map.is_traversable(start_x, start_y) or not grid_map.is_traversable(goal_x, goal_y):
                raise PlanningError("Start or goal is in collision.")
            req = PlanningRequest(start=Waypoint(start_x, start_y), goal=Waypoint(goal_x, goal_y))
            res = self._plan_internal(grid_map, req)
            if res.status != PlanningStatus.SUCCESS or res.path is None:
                raise PlanningError("A* planning failed to find path.")
            return res.path

        return self._plan_internal(grid_map_or_start, request_or_goal)

    def _plan_internal(self, grid_map: GridMap, request: PlanningRequest) -> PlanningResult:
        """A* path planning."""
        start_time = time.time()
        
        # Convert world coordinates to grid
        start_gx, start_gy = grid_map.world_to_grid(request.start.x_m, request.start.y_m)
        goal_gx, goal_gy = grid_map.world_to_grid(request.goal.x_m, request.goal.y_m)
        
        # Validate start and goal
        if not grid_map.is_valid_cell(start_gx, start_gy):
            return PlanningResult(PlanningStatus.START_OCCUPIED, message="Start outside grid")
        if not grid_map.is_valid_cell(goal_gx, goal_gy):
            return PlanningResult(PlanningStatus.GOAL_OCCUPIED, message="Goal outside grid")
        
        if grid_map.is_occupied(start_gx, start_gy):
            return PlanningResult(PlanningStatus.START_OCCUPIED, message="Start occupied")
        if grid_map.is_occupied(goal_gx, goal_gy):
            return PlanningResult(PlanningStatus.GOAL_OCCUPIED, message="Goal occupied")
        
        # A* search
        open_set: List[AStarNode] = []
        open_dict: Dict[Tuple[int, int], AStarNode] = {}
        all_nodes: Dict[Tuple[int, int], AStarNode] = {}
        closed_set: Set[Tuple[int, int]] = set()
        
        # Initialize start node
        start_node = AStarNode(
            x=start_gx,
            y=start_gy,
            g_cost=0.0,
            h_cost=self._heuristic(start_gx, start_gy, goal_gx, goal_gy),
        )
        
        heapq.heappush(open_set, start_node)
        open_dict[(start_gx, start_gy)] = start_node
        all_nodes[(start_gx, start_gy)] = start_node
        
        iterations = 0
        max_iterations = grid_map.width * grid_map.height * 4
        
        while open_set and iterations < max_iterations:
            iterations += 1
            
            # Check timeout
            if time.time() - start_time > request.max_planning_time_s:
                return PlanningResult(
                    PlanningStatus.TIMEOUT,
                    planning_time_s=time.time() - start_time,
                    iterations=iterations,
                    message="Planning timeout"
                )
            
            # Get node with lowest f_cost
            current = heapq.heappop(open_set)
            current_pos = (current.x, current.y)
            
            if current_pos in open_dict:
                del open_dict[current_pos]
            
            # Check if reached goal
            if current.x == goal_gx and current.y == goal_gy:
                path = self._reconstruct_path(current, grid_map, all_nodes)
                return PlanningResult(
                    PlanningStatus.SUCCESS,
                    path=path,
                    planning_time_s=time.time() - start_time,
                    iterations=iterations,
                    message="Path found"
                )
            
            closed_set.add(current_pos)
            
            # Explore neighbors
            for nx, ny, move_cost in self._get_neighbors(current.x, current.y, grid_map):
                neighbor_pos = (nx, ny)
                
                if neighbor_pos in closed_set:
                    continue
                
                if not grid_map.is_traversable(grid_map.grid_to_world(nx, ny)[0], grid_map.grid_to_world(nx, ny)[1]):
                    continue
                
                # Calculate costs
                tentative_g = current.g_cost + move_cost + grid_map.get_cost(nx, ny)
                h_cost = self._heuristic(nx, ny, goal_gx, goal_gy)
                
                # Check if this path is better
                if neighbor_pos in open_dict:
                    existing = open_dict[neighbor_pos]
                    if tentative_g >= existing.g_cost:
                        continue
                
                # Create new neighbor node
                neighbor = AStarNode(
                    x=nx,
                    y=ny,
                    g_cost=tentative_g,
                    h_cost=h_cost,
                    parent=current_pos,
                )
                
                heapq.heappush(open_set, neighbor)
                open_dict[neighbor_pos] = neighbor
                all_nodes[neighbor_pos] = neighbor
        
        # No path found
        return PlanningResult(
            PlanningStatus.NO_PATH,
            planning_time_s=time.time() - start_time,
            iterations=iterations,
            message="No path to goal"
        )
    
    def _get_neighbors(self, x: int, y: int, grid_map: GridMap) -> List[Tuple[int, int, float]]:
        """Komşu hücreler ve hareket maliyetleri."""
        neighbors = []
        
        # 4-connectivity (cardinal directions)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if grid_map.is_valid_cell(nx, ny):
                neighbors.append((nx, ny, 1.0))
        
        # 8-connectivity (diagonals)
        if self.config.allow_diagonal:
            diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dx, dy in diagonal_dirs:
                nx, ny = x + dx, y + dy
                if grid_map.is_valid_cell(nx, ny):
                    neighbors.append((nx, ny, self.config.diagonal_cost))
        
        return neighbors
    
    def _heuristic(self, x1: int, y1: int, x2: int, y2: int) -> float:
        """Heuristik fonksiyonu."""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        if self.config.heuristic == HeuristicType.EUCLIDEAN:
            h = math.sqrt(dx * dx + dy * dy)
        elif self.config.heuristic == HeuristicType.MANHATTAN:
            h = dx + dy
        elif self.config.heuristic == HeuristicType.DIAGONAL:
            h = max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)
        else:  # ZERO (Dijkstra)
            h = 0.0
        
        # Tie breaking
        if self.config.tie_breaking and self.config.heuristic != HeuristicType.ZERO:
            h += (dx + dy) * 0.001
        
        return h * self.config.weight
    
    def _reconstruct_path(self, goal_node: AStarNode, grid_map: GridMap, all_nodes: Dict[Tuple[int, int], AStarNode]) -> Path:
        """Goal'den start'a path reconstruct et."""
        waypoints = []
        curr: Optional[AStarNode] = goal_node
        node_chain = []
        
        while curr is not None:
            node_chain.append(curr)
            if curr.parent is not None:
                curr = all_nodes.get(curr.parent)
            else:
                curr = None
        
        node_chain.reverse()
        
        # Convert grid coordinates to waypoints
        for node in node_chain:
            wx, wy = grid_map.grid_to_world(node.x, node.y)
            waypoints.append(Waypoint(x_m=wx, y_m=wy))
        
        return Path(waypoints=waypoints)