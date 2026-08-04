"""
TRUSTIA Planning - RRT and RRT* Sampling-Based Planning.

Rapidly-exploring Random Tree for complex environments.
RRT*: asymptotically optimal version.
"""

from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple

import numpy as np

from planning.grid_map import GridMap
from planning.types import Path, PlanningRequest, PlanningResult, PlanningStatus, Waypoint


@dataclass
class RRTConfig:
    """RRT konfigürasyonu."""
    max_iterations: int = 5000
    step_size_m: float = 1.0  # Maximum extension distance
    goal_bias: float = 0.1    # Probability of sampling goal
    goal_tolerance_m: float = 0.5
    # RRT* specific
    search_radius_m: float = 2.0  # Rewiring radius for RRT*
    max_neighbors: int = 10       # Max neighbors to consider


@dataclass
class RRTNode:
    """RRT tree node."""
    x: float
    y: float
    parent: Optional["RRTNode"] = None
    cost: float = 0.0  # Cost from root (for RRT*)
    
    def distance_to(self, other: "RRTNode") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def distance_to_point(self, x: float, y: float) -> float:
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)


class RRTPlanner:
    """Basic RRT planner."""
    
    def __init__(self, config: RRTConfig = RRTConfig()) -> None:
        self.config = config
        self.tree: List[RRTNode] = []
    
    def plan(self, grid_map: GridMap, request: PlanningRequest) -> PlanningResult:
        """RRT path planning."""
        start_time = time.time()
        
        # Validate start and goal
        if not grid_map.is_collision_free(request.start.x_m, request.start.y_m):
            return PlanningResult(PlanningStatus.START_OCCUPIED, message="Start in collision")
        if not grid_map.is_collision_free(request.goal.x_m, request.goal.y_m):
            return PlanningResult(PlanningStatus.GOAL_OCCUPIED, message="Goal in collision")
        
        # Initialize tree with start node
        self.tree = []
        start_node = RRTNode(x=request.start.x_m, y=request.start.y_m, cost=0.0)
        self.tree.append(start_node)
        
        # Define sampling bounds from grid map
        map_bounds = self._get_map_bounds(grid_map)
        
        for iteration in range(self.config.max_iterations):
            # Check timeout
            if time.time() - start_time > request.max_planning_time_s:
                return PlanningResult(
                    PlanningStatus.TIMEOUT,
                    planning_time_s=time.time() - start_time,
                    iterations=iteration,
                    message="RRT timeout"
                )
            
            # Sample random point
            sample_x, sample_y = self._sample_point(request.goal, map_bounds)
            
            # Find nearest node in tree
            nearest_node = self._find_nearest_node(sample_x, sample_y)
            
            # Extend tree towards sample
            new_node = self._extend_tree(nearest_node, sample_x, sample_y, grid_map)
            
            if new_node is not None:
                self.tree.append(new_node)
                
                # Check if reached goal
                goal_dist = new_node.distance_to_point(request.goal.x_m, request.goal.y_m)
                if goal_dist <= self.config.goal_tolerance_m:
                    path = self._extract_path(new_node, grid_map)
                    return PlanningResult(
                        PlanningStatus.SUCCESS,
                        path=path,
                        planning_time_s=time.time() - start_time,
                        iterations=iteration + 1,
                        message="RRT path found"
                    )
        
        # No path found within max iterations
        return PlanningResult(
            PlanningStatus.NO_PATH,
            planning_time_s=time.time() - start_time,
            iterations=self.config.max_iterations,
            message="RRT max iterations reached"
        )
    
    def _get_map_bounds(self, grid_map: GridMap) -> Tuple[float, float, float, float]:
        """Get map bounds in world coordinates."""
        min_x = grid_map.origin_x_m
        min_y = grid_map.origin_y_m
        max_x = grid_map.origin_x_m + grid_map.width * grid_map.resolution_m
        max_y = grid_map.origin_y_m + grid_map.height * grid_map.resolution_m
        return min_x, min_y, max_x, max_y
    
    def _sample_point(self, goal: Waypoint, map_bounds: Tuple[float, float, float, float]) -> Tuple[float, float]:
        """Sample random point in configuration space."""
        min_x, min_y, max_x, max_y = map_bounds
        
        # Goal biased sampling
        if random.random() < self.config.goal_bias:
            return goal.x_m, goal.y_m
        
        # Uniform random sampling
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        return x, y
    
    def _find_nearest_node(self, x: float, y: float) -> RRTNode:
        """Find nearest node in tree."""
        nearest_node = self.tree[0]
        nearest_dist = nearest_node.distance_to_point(x, y)
        
        for node in self.tree[1:]:
            dist = node.distance_to_point(x, y)
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_node = node
        
        return nearest_node
    
    def _extend_tree(self, nearest: RRTNode, sample_x: float, sample_y: float, grid_map: GridMap) -> Optional[RRTNode]:
        """Extend tree from nearest node towards sample."""
        # Direction from nearest to sample
        dx = sample_x - nearest.x
        dy = sample_y - nearest.y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance < 1e-6:
            return None
        
        # Normalize and scale by step size
        step_x = nearest.x + (dx / distance) * min(self.config.step_size_m, distance)
        step_y = nearest.y + (dy / distance) * min(self.config.step_size_m, distance)
        
        # Check collision along path
        if self._is_path_collision_free(nearest.x, nearest.y, step_x, step_y, grid_map):
            new_node = RRTNode(
                x=step_x,
                y=step_y,
                parent=nearest,
                cost=nearest.cost + nearest.distance_to_point(step_x, step_y)
            )
            return new_node
        
        return None
    
    def _is_path_collision_free(self, x1: float, y1: float, x2: float, y2: float, grid_map: GridMap) -> bool:
        """Check if straight line path is collision free."""
        # Discretize path and check each point
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        num_checks = max(2, int(distance / (grid_map.resolution_m * 0.5)))
        
        for i in range(num_checks + 1):
            t = i / num_checks if num_checks > 0 else 0
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            
            if not grid_map.is_collision_free(x, y):
                return False
        
        return True
    
    def _extract_path(self, goal_node: RRTNode, grid_map: GridMap) -> Path:
        """Extract path from tree."""
        path = Path()
        waypoints = []
        
        # Trace back from goal to start
        current = goal_node
        while current is not None:
            waypoints.append(Waypoint(x_m=current.x, y_m=current.y))
            current = current.parent
        
        # Reverse to get start->goal order
        waypoints.reverse()
        
        path.waypoints = waypoints
        
        # Calculate total path length
        total_length = 0.0
        for i in range(1, len(waypoints)):
            total_length += waypoints[i-1].distance_to(waypoints[i])
        path.total_length = total_length
        
        return path


class RRTStarPlanner(RRTPlanner):
    """RRT* - asymptotically optimal RRT."""
    
    def plan(self, grid_map: GridMap, request: PlanningRequest) -> PlanningResult:
        """RRT* path planning with rewiring."""
        start_time = time.time()
        
        # Validate start and goal
        if not grid_map.is_collision_free(request.start.x_m, request.start.y_m):
            return PlanningResult(PlanningStatus.START_OCCUPIED, message="Start in collision")
        if not grid_map.is_collision_free(request.goal.x_m, request.goal.y_m):
            return PlanningResult(PlanningStatus.GOAL_OCCUPIED, message="Goal in collision")
        
        # Initialize tree
        self.tree = []
        start_node = RRTNode(x=request.start.x_m, y=request.start.y_m, cost=0.0)
        self.tree.append(start_node)
        
        map_bounds = self._get_map_bounds(grid_map)
        best_goal_node = None
        
        for iteration in range(self.config.max_iterations):
            # Check timeout
            if time.time() - start_time > request.max_planning_time_s:
                if best_goal_node:
                    path = self._extract_path(best_goal_node, grid_map)
                    return PlanningResult(
                        PlanningStatus.SUCCESS,
                        path=path,
                        planning_time_s=time.time() - start_time,
                        iterations=iteration,
                        message="RRT* timeout with solution"
                    )
                return PlanningResult(
                    PlanningStatus.TIMEOUT,
                    planning_time_s=time.time() - start_time,
                    iterations=iteration,
                    message="RRT* timeout"
                )
            
            # Sample random point
            sample_x, sample_y = self._sample_point(request.goal, map_bounds)
            
            # Find nearest node
            nearest_node = self._find_nearest_node(sample_x, sample_y)
            
            # Extend tree (same as RRT)
            new_node = self._extend_tree(nearest_node, sample_x, sample_y, grid_map)
            
            if new_node is not None:
                # RRT* improvement: find neighbors and choose best parent
                neighbors = self._find_neighbors(new_node, grid_map)
                
                # Choose best parent (lowest cost path)
                best_parent = nearest_node
                best_cost = nearest_node.cost + nearest_node.distance_to(new_node)
                
                for neighbor in neighbors:
                    if self._is_path_collision_free(neighbor.x, neighbor.y, new_node.x, new_node.y, grid_map):
                        potential_cost = neighbor.cost + neighbor.distance_to(new_node)
                        if potential_cost < best_cost:
                            best_cost = potential_cost
                            best_parent = neighbor
                
                new_node.parent = best_parent
                new_node.cost = best_cost
                self.tree.append(new_node)
                
                # RRT* improvement: rewire tree
                self._rewire_tree(new_node, neighbors, grid_map)
                
                # Check if reached goal
                goal_dist = new_node.distance_to_point(request.goal.x_m, request.goal.y_m)
                if goal_dist <= self.config.goal_tolerance_m:
                    if best_goal_node is None or new_node.cost < best_goal_node.cost:
                        best_goal_node = new_node
        
        # Return best solution found
        if best_goal_node:
            path = self._extract_path(best_goal_node, grid_map)
            return PlanningResult(
                PlanningStatus.SUCCESS,
                path=path,
                planning_time_s=time.time() - start_time,
                iterations=self.config.max_iterations,
                message="RRT* path found"
            )
        
        return PlanningResult(
            PlanningStatus.NO_PATH,
            planning_time_s=time.time() - start_time,
            iterations=self.config.max_iterations,
            message="RRT* no path found"
        )
    
    def _find_neighbors(self, node: RRTNode, grid_map: GridMap) -> List[RRTNode]:
        """Find neighbors within search radius."""
        neighbors = []
        
        for other_node in self.tree:
            if other_node == node:
                continue
            
            distance = node.distance_to(other_node)
            if distance <= self.config.search_radius_m:
                neighbors.append(other_node)
                
                if len(neighbors) >= self.config.max_neighbors:
                    break
        
        return neighbors
    
    def _rewire_tree(self, new_node: RRTNode, neighbors: List[RRTNode], grid_map: GridMap) -> None:
        """Rewire tree to improve costs."""
        for neighbor in neighbors:
            # Check if routing through new_node improves neighbor's cost
            potential_cost = new_node.cost + new_node.distance_to(neighbor)
            
            if (potential_cost < neighbor.cost and 
                self._is_path_collision_free(new_node.x, new_node.y, neighbor.x, neighbor.y, grid_map)):
                
                # Rewire: make new_node the parent of neighbor
                neighbor.parent = new_node
                neighbor.cost = potential_cost
                
                # Propagate cost changes to descendants
                self._update_descendants_cost(neighbor)
    
    def _update_descendants_cost(self, node: RRTNode) -> None:
        """Update cost of all descendants recursively."""
        for child in self.tree:
            if child.parent == node:
                old_cost = child.cost
                new_cost = node.cost + node.distance_to(child)
                
                if new_cost != old_cost:
                    child.cost = new_cost
                    self._update_descendants_cost(child)


from core.errors import PlanningError

class RrtPlanner:
    """Convenience / Legacy RRT planner wrapper for simplified tuple interface."""

    def __init__(
        self,
        is_traversable=None,
        step_size_m: float = 1.0,
        max_iterations: int = 3000,
        goal_bias: float = 0.1,
        seed: Optional[int] = None,
    ) -> None:
        if step_size_m <= 0:
            raise PlanningError("step_size_m must be > 0")
        self.is_traversable = is_traversable or (lambda x, y: True)
        self.step_size_m = step_size_m
        self.max_iterations = max_iterations
        self.goal_bias = goal_bias
        self.seed = seed

    def plan(
        self,
        start: Tuple[float, float],
        goal: Tuple[float, float],
        bounds: Tuple[float, float, float, float] = (0.0, 100.0, 0.0, 100.0),
    ) -> Path:
        if self.seed is not None:
            random.seed(self.seed)

        start_x, start_y = start
        goal_x, goal_y = goal
        min_x, max_x, min_y, max_y = bounds

        if not self.is_traversable(start_x, start_y) or not self.is_traversable(goal_x, goal_y):
            raise PlanningError("Start or goal is in collision.")

        tree = [RRTNode(start_x, start_y)]

        for _ in range(self.max_iterations):
            if random.random() < self.goal_bias:
                sx, sy = goal_x, goal_y
            else:
                sx = random.uniform(min_x, max_x)
                sy = random.uniform(min_y, max_y)

            nearest = min(tree, key=lambda n: n.distance_to_point(sx, sy))
            dist = nearest.distance_to_point(sx, sy)
            if dist < 1e-6:
                continue

            step = min(dist, self.step_size_m)
            nx = nearest.x + (sx - nearest.x) / dist * step
            ny = nearest.y + (sy - nearest.y) / dist * step

            if self.is_traversable(nx, ny):
                new_node = RRTNode(nx, ny, parent=nearest)
                tree.append(new_node)
                if math.hypot(nx - goal_x, ny - goal_y) <= self.step_size_m:
                    curr: Optional[RRTNode] = new_node
                    pts = []
                    while curr:
                        pts.append(Waypoint(curr.x, curr.y))
                        curr = curr.parent
                    pts.reverse()
                    pts.append(Waypoint(goal_x, goal_y))
                    return Path(pts)

        raise PlanningError("RRT path planning failed: Max iterations reached.")