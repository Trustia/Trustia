"""
TRUSTIA Planning - Hybrid A* Path Planning.

Araç kinematik kısıtları ile A*. Gerçekçi araç hareketleri.
Bicycle model based planning.
"""

from __future__ import annotations

import heapq
import math
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

import numpy as np

from planning.grid_map import GridMap
from planning.types import Path, PlanningRequest, PlanningResult, PlanningStatus, Waypoint


@dataclass
class VehicleModel:
    """Araç kinematik modeli."""
    wheelbase_m: float = 2.5      # Aks arası mesafe
    max_steer_rad: float = 0.6    # Maksimum direksiyon açısı
    min_turn_radius_m: float = 4.0  # Minimum dönüş yarıçapı
    length_m: float = 4.0         # Araç boyu
    width_m: float = 2.0          # Araç genişliği


@dataclass  
class HybridAStarConfig:
    """Hybrid A* konfigürasyonu."""
    # Grid discretization
    xy_resolution_m: float = 0.5
    yaw_resolution_rad: float = math.radians(15)  # 15 derece
    
    # Motion primitives
    motion_step_size_m: float = 1.0
    num_steer_angles: int = 5  # Symmetric steering angles
    
    # Costs
    reverse_penalty: float = 2.0
    steer_penalty: float = 1.5
    steer_change_penalty: float = 2.0
    
    # Heuristics
    holonomic_heuristic_weight: float = 2.0
    
    # Search limits
    max_iterations: int = 10000


@dataclass
class HybridAStarNode:
    """Hybrid A* node - (x, y, yaw) configuration."""
    x: float
    y: float 
    yaw: float
    g_cost: float
    h_cost: float
    steer_angle: float = 0.0
    direction: int = 1  # 1: forward, -1: reverse
    parent: Optional[Tuple[int, int, int]] = None
    
    @property
    def f_cost(self) -> float:
        return self.g_cost + self.h_cost
    
    def __lt__(self, other: "HybridAStarNode") -> bool:
        return self.f_cost < other.f_cost


class HybridAStarPlanner:
    """Hybrid A* planner with vehicle kinematics."""
    
    def __init__(self, vehicle: VehicleModel, config: HybridAStarConfig = HybridAStarConfig()) -> None:
        self.vehicle = vehicle
        self.config = config
        
        # Pre-compute steering angles
        self._compute_steering_angles()
        
        # Holonomic heuristic (precomputed A*)
        self._holonomic_heuristic: Optional[np.ndarray] = None
    
    def _compute_steering_angles(self) -> None:
        """Pre-compute symmetric steering angles."""
        self.steering_angles = []
        
        # Add straight motion
        self.steering_angles.append(0.0)
        
        # Add symmetric left/right steering
        for i in range(1, (self.config.num_steer_angles + 1) // 2):
            angle = (i / ((self.config.num_steer_angles - 1) // 2)) * self.vehicle.max_steer_rad
            self.steering_angles.append(angle)   # Right
            self.steering_angles.append(-angle)  # Left
    
    def plan(self, grid_map: GridMap, request: PlanningRequest) -> PlanningResult:
        """Hybrid A* planning."""
        start_time = time.time()
        
        # Validate start and goal
        if not self._is_valid_configuration(request.start.x_m, request.start.y_m, 
                                          request.start.heading_rad or 0.0, grid_map):
            return PlanningResult(PlanningStatus.START_OCCUPIED, message="Start configuration invalid")
        
        if not self._is_valid_configuration(request.goal.x_m, request.goal.y_m,
                                          request.goal.heading_rad or 0.0, grid_map):
            return PlanningResult(PlanningStatus.GOAL_OCCUPIED, message="Goal configuration invalid")
        
        # Precompute holonomic heuristic from goal
        self._precompute_holonomic_heuristic(grid_map, request.goal)
        
        # Initialize search
        open_set: List[HybridAStarNode] = []
        open_dict: Dict[Tuple[int, int, int], HybridAStarNode] = {}
        closed_set: Set[Tuple[int, int, int]] = set()
        
        # Discretize start configuration
        start_indices = self._discretize_configuration(
            request.start.x_m, request.start.y_m, request.start.heading_rad or 0.0
        )
        
        start_node = HybridAStarNode(
            x=request.start.x_m,
            y=request.start.y_m,
            yaw=request.start.heading_rad or 0.0,
            g_cost=0.0,
            h_cost=self._compute_heuristic(request.start.x_m, request.start.y_m, request.goal),
        )
        
        heapq.heappush(open_set, start_node)
        open_dict[start_indices] = start_node
        
        iterations = 0
        
        while open_set and iterations < self.config.max_iterations:
            iterations += 1
            
            # Check timeout
            if time.time() - start_time > request.max_planning_time_s:
                return PlanningResult(
                    PlanningStatus.TIMEOUT,
                    planning_time_s=time.time() - start_time,
                    iterations=iterations,
                    message="Hybrid A* timeout"
                )
            
            # Get best node
            current = heapq.heappop(open_set)
            current_indices = self._discretize_configuration(current.x, current.y, current.yaw)
            
            if current_indices in open_dict:
                del open_dict[current_indices]
            
            # Check goal reach
            if self._is_goal_reached(current, request.goal):
                path = self._reconstruct_path(current, open_dict, closed_set)
                return PlanningResult(
                    PlanningStatus.SUCCESS,
                    path=path,
                    planning_time_s=time.time() - start_time,
                    iterations=iterations,
                    message="Hybrid A* path found"
                )
            
            closed_set.add(current_indices)
            
            # Expand motion primitives
            successors = self._generate_successors(current, grid_map)
            
            for successor in successors:
                successor_indices = self._discretize_configuration(
                    successor.x, successor.y, successor.yaw
                )
                
                if successor_indices in closed_set:
                    continue
                
                if not self._is_valid_configuration(successor.x, successor.y, successor.yaw, grid_map):
                    continue
                
                # Check if better path
                if successor_indices in open_dict:
                    existing = open_dict[successor_indices]
                    if successor.g_cost >= existing.g_cost:
                        continue
                
                # Add to open set
                successor.parent = current_indices
                heapq.heappush(open_set, successor)
                open_dict[successor_indices] = successor
        
        return PlanningResult(
            PlanningStatus.NO_PATH,
            planning_time_s=time.time() - start_time,
            iterations=iterations,
            message="Hybrid A* no path found"
        )
    
    def _discretize_configuration(self, x: float, y: float, yaw: float) -> Tuple[int, int, int]:
        """Discretize configuration to grid indices."""
        grid_x = int(round(x / self.config.xy_resolution_m))
        grid_y = int(round(y / self.config.xy_resolution_m))
        grid_yaw = int(round(yaw / self.config.yaw_resolution_rad))
        return grid_x, grid_y, grid_yaw
    
    def _generate_successors(self, node: HybridAStarNode, grid_map: GridMap) -> List[HybridAStarNode]:
        """Generate successor configurations using motion primitives."""
        successors = []
        
        for direction in [1, -1]:  # Forward, backward
            for steer_angle in self.steering_angles:
                # Compute next configuration using bicycle model
                next_x, next_y, next_yaw = self._bicycle_model(
                    node.x, node.y, node.yaw, steer_angle, 
                    direction * self.config.motion_step_size_m
                )
                
                # Compute cost
                motion_cost = self.config.motion_step_size_m
                if direction == -1:
                    motion_cost *= self.config.reverse_penalty
                
                if abs(steer_angle) > 1e-6:
                    motion_cost *= self.config.steer_penalty
                
                # Steering change penalty
                steer_change_cost = 0.0
                if abs(steer_angle - node.steer_angle) > 1e-6:
                    steer_change_cost = self.config.steer_change_penalty
                
                g_cost = node.g_cost + motion_cost + steer_change_cost
                h_cost = self._compute_heuristic(next_x, next_y, None)  # Goal set in precompute
                
                successor = HybridAStarNode(
                    x=next_x,
                    y=next_y,
                    yaw=next_yaw,
                    g_cost=g_cost,
                    h_cost=h_cost,
                    steer_angle=steer_angle,
                    direction=direction,
                )
                
                successors.append(successor)
        
        return successors
    
    def _bicycle_model(self, x: float, y: float, yaw: float, steer: float, distance: float) -> Tuple[float, float, float]:
        """Bicycle model kinematics."""
        if abs(steer) < 1e-6:
            # Straight line motion
            next_x = x + distance * math.cos(yaw)
            next_y = y + distance * math.sin(yaw)
            next_yaw = yaw
        else:
            # Arc motion
            turn_radius = self.vehicle.wheelbase_m / math.tan(steer)
            angular_distance = distance / turn_radius
            
            next_x = x + turn_radius * (math.sin(yaw + angular_distance) - math.sin(yaw))
            next_y = y - turn_radius * (math.cos(yaw + angular_distance) - math.cos(yaw))
            next_yaw = yaw + angular_distance
        
        # Normalize yaw
        next_yaw = math.atan2(math.sin(next_yaw), math.cos(next_yaw))
        
        return next_x, next_y, next_yaw
    
    def _is_valid_configuration(self, x: float, y: float, yaw: float, grid_map: GridMap) -> bool:
        """Check if configuration is collision-free."""
        # Simple check: vehicle as oriented rectangle
        half_length = self.vehicle.length_m * 0.5
        half_width = self.vehicle.width_m * 0.5
        
        # Vehicle corners relative to center
        corners = [
            (-half_length, -half_width),
            (-half_length, half_width),
            (half_length, -half_width),
            (half_length, half_width),
        ]
        
        # Transform corners to world coordinates
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)
        
        for dx, dy in corners:
            world_x = x + dx * cos_yaw - dy * sin_yaw
            world_y = y + dx * sin_yaw + dy * cos_yaw
            
            if not grid_map.is_collision_free(world_x, world_y):
                return False
        
        return True
    
    def _is_goal_reached(self, node: HybridAStarNode, goal: Waypoint) -> bool:
        """Check if node is close enough to goal."""
        pos_dist = math.sqrt((node.x - goal.x_m)**2 + (node.y - goal.y_m)**2)
        
        if pos_dist > goal.tolerance_m:
            return False
        
        # Check heading if specified
        if goal.heading_rad is not None:
            yaw_diff = abs(node.yaw - goal.heading_rad)
            yaw_diff = min(yaw_diff, 2 * math.pi - yaw_diff)  # Wrap around
            if yaw_diff > math.radians(15):  # 15 degree tolerance
                return False
        
        return True
    
    def _precompute_holonomic_heuristic(self, grid_map: GridMap, goal: Waypoint) -> None:
        """Precompute holonomic heuristic using Dijkstra from goal."""
        # Simplified: use Euclidean distance for now
        # In practice, you'd run Dijkstra from goal backwards
        self._goal_for_heuristic = goal
    
    def _compute_heuristic(self, x: float, y: float, goal: Optional[Waypoint]) -> float:
        """Compute heuristic cost to goal."""
        if hasattr(self, '_goal_for_heuristic'):
            goal = self._goal_for_heuristic
        
        if goal is None:
            return 0.0
        
        # Euclidean distance * weight
        euclidean = math.sqrt((x - goal.x_m)**2 + (y - goal.y_m)**2)
        return euclidean * self.config.holonomic_heuristic_weight
    
    def _reconstruct_path(self, goal_node: HybridAStarNode, open_dict: Dict, closed_dict: Set) -> Path:
        """Reconstruct path from goal to start."""
        path = Path()
        waypoints = []
        
        # Collect nodes (this is simplified - in practice you'd store the full tree)
        current = goal_node
        waypoints.append(Waypoint(
            x_m=current.x,
            y_m=current.y,
            heading_rad=current.yaw,
            speed_mps=1.0 if current.direction > 0 else -1.0
        ))
        
        # For simplicity, just return the goal waypoint
        # In practice, you'd traverse the parent chain
        
        waypoints.reverse()
        path.waypoints = waypoints
        
        return path