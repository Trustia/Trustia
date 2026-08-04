"""
TRUSTIA Planning - Grid Map.

Occupancy grid'i planlama için discretized harita.
Obstacle inflation, cost computation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional, Tuple

import numpy as np


class CellType(IntEnum):
    """Grid hücre tipleri."""
    FREE = 0        # Serbest alan
    OCCUPIED = 100  # Engel
    UNKNOWN = -1    # Bilinmeyen


@dataclass
class GridCell:
    """Tek grid hücresi."""
    x: int
    y: int
    cost: float = 0.0
    cell_type: CellType = CellType.FREE
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))


class GridMap:
    """2D occupancy grid - planlama için."""
    
    def __init__(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        resolution_m: float = 1.0,
        width_m: float = 50.0,
        height_m: float = 50.0,
        origin_x_m: float = 0.0,
        origin_y_m: float = 0.0,
    ) -> None:
        if width is None:
            width = max(1, int(width_m / resolution_m))
        if height is None:
            height = max(1, int(height_m / resolution_m))
        self.width = width
        self.height = height
        self.width_m = width * resolution_m
        self.height_m = height * resolution_m
        self.resolution_m = resolution_m
        self.origin_x_m = origin_x_m
        self.origin_y_m = origin_y_m

        self.data = np.full((height, width), CellType.FREE, dtype=np.int8)
        self.cost_map = np.zeros((height, width), dtype=np.float32)

    def mark_obstacle(self, x_m: float, y_m: float, radius_m: float = 0.0) -> None:
        gx, gy = self.world_to_grid(x_m, y_m)
        r_cells = int(math.ceil(radius_m / self.resolution_m))
        if r_cells <= 0:
            if self.is_valid_cell(gx, gy):
                self.data[gy, gx] = CellType.OCCUPIED.value
                self.cost_map[gy, gx] = float('inf')
        else:
            for dx in range(-r_cells, r_cells + 1):
                for dy in range(-r_cells, r_cells + 1):
                    if dx * dx + dy * dy <= r_cells * r_cells:
                        nx, ny = gx + dx, gy + dy
                        if self.is_valid_cell(nx, ny):
                            self.data[ny, nx] = CellType.OCCUPIED.value
                            self.cost_map[ny, nx] = float('inf')

    def is_traversable(self, x_m: float, y_m: float) -> bool:
        gx, gy = self.world_to_grid(x_m, y_m)
        if not self.is_valid_cell(gx, gy):
            return False
        return bool(self.data[gy, gx] != CellType.OCCUPIED.value)
    
    def world_to_grid(self, x_m: float, y_m: float) -> Tuple[int, int]:
        """World coordinates → grid indices."""
        grid_x = int((x_m - self.origin_x_m) / self.resolution_m)
        grid_y = int((y_m - self.origin_y_m) / self.resolution_m)
        return grid_x, grid_y
    
    def grid_to_world(self, grid_x: int, grid_y: int) -> Tuple[float, float]:
        """Grid indices → world coordinates (cell center)."""
        world_x = self.origin_x_m + (grid_x + 0.5) * self.resolution_m
        world_y = self.origin_y_m + (grid_y + 0.5) * self.resolution_m
        return world_x, world_y
    
    def is_valid_cell(self, grid_x: int, grid_y: int) -> bool:
        """Grid koordinatları geçerli mi?"""
        return 0 <= grid_x < self.width and 0 <= grid_y < self.height
    
    def get_cell_type(self, grid_x: int, grid_y: int) -> CellType:
        """Hücre tipini al."""
        if not self.is_valid_cell(grid_x, grid_y):
            return CellType.OCCUPIED  # Grid dışı = engel
        return CellType(self.data[grid_y, grid_x])
    
    def set_cell_type(self, grid_x: int, grid_y: int, cell_type: CellType) -> None:
        """Hücre tipini ayarla."""
        if self.is_valid_cell(grid_x, grid_y):
            self.data[grid_y, grid_x] = cell_type.value
    
    def get_cost(self, grid_x: int, grid_y: int) -> float:
        """Planlama maliyeti al."""
        if not self.is_valid_cell(grid_x, grid_y):
            return float('inf')
        return self.cost_map[grid_y, grid_x]
    
    def set_cost(self, grid_x: int, grid_y: int, cost: float) -> None:
        """Planlama maliyeti ayarla."""
        if self.is_valid_cell(grid_x, grid_y):
            self.cost_map[grid_y, grid_x] = cost
    
    def is_free(self, grid_x: int, grid_y: int) -> bool:
        """Hücre serbest mi?"""
        return self.get_cell_type(grid_x, grid_y) == CellType.FREE
    
    def is_occupied(self, grid_x: int, grid_y: int) -> bool:
        """Hücre engellenmiş mi?"""
        cell_type = self.get_cell_type(grid_x, grid_y)
        return cell_type == CellType.OCCUPIED
    
    def is_collision_free(self, x_m: float, y_m: float) -> bool:
        """World koordinatlarında çarpışma var mı?"""
        grid_x, grid_y = self.world_to_grid(x_m, y_m)
        return self.is_free(grid_x, grid_y)
    
    def get_neighbors(self, grid_x: int, grid_y: int, connectivity: int = 8) -> List[Tuple[int, int]]:
        """Komşu hücreleri al (4 veya 8 bağlantı)."""
        neighbors = []
        
        if connectivity == 4:
            # 4-connectivity (cardinal directions)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            # 8-connectivity (including diagonals)
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)
            ]
        
        for dx, dy in directions:
            nx, ny = grid_x + dx, grid_y + dy
            if self.is_valid_cell(nx, ny):
                neighbors.append((nx, ny))
        
        return neighbors
    
    def update_from_occupancy_grid(self, occupancy_data: np.ndarray, occupied_threshold: float = 0.65, free_threshold: float = 0.25) -> None:
        """Occupancy grid'den güncelle."""
        # Normalize occupancy probabilities to [0, 1]
        normalized = occupancy_data.astype(np.float32)
        if normalized.max() > 1.0:
            normalized = normalized / 100.0
        
        # Classify cells
        self.data[normalized >= occupied_threshold] = CellType.OCCUPIED
        self.data[normalized <= free_threshold] = CellType.FREE
        # Cells between thresholds remain UNKNOWN
    
    def add_obstacle_circle(self, center_x_m: float, center_y_m: float, radius_m: float) -> None:
        """Dairesel engel ekle."""
        center_gx, center_gy = self.world_to_grid(center_x_m, center_y_m)
        radius_cells = int(radius_m / self.resolution_m) + 1
        
        for dy in range(-radius_cells, radius_cells + 1):
            for dx in range(-radius_cells, radius_cells + 1):
                gx, gy = center_gx + dx, center_gy + dy
                if not self.is_valid_cell(gx, gy):
                    continue
                
                # Check if cell is within circle
                wx, wy = self.grid_to_world(gx, gy)
                dist = math.sqrt((wx - center_x_m)**2 + (wy - center_y_m)**2)
                if dist <= radius_m:
                    self.set_cell_type(gx, gy, CellType.OCCUPIED)
    
    def add_obstacle_rectangle(self, min_x_m: float, min_y_m: float, max_x_m: float, max_y_m: float) -> None:
        """Dikdörtgen engel ekle."""
        min_gx, min_gy = self.world_to_grid(min_x_m, min_y_m)
        max_gx, max_gy = self.world_to_grid(max_x_m, max_y_m)
        
        for gy in range(min_gy, max_gy + 1):
            for gx in range(min_gx, max_gx + 1):
                if self.is_valid_cell(gx, gy):
                    self.set_cell_type(gx, gy, CellType.OCCUPIED)
    
    def clear_area_circle(self, center_x_m: float, center_y_m: float, radius_m: float) -> None:
        """Dairesel alanı temizle."""
        center_gx, center_gy = self.world_to_grid(center_x_m, center_y_m)
        radius_cells = int(radius_m / self.resolution_m) + 1
        
        for dy in range(-radius_cells, radius_cells + 1):
            for dx in range(-radius_cells, radius_cells + 1):
                gx, gy = center_gx + dx, center_gy + dy
                if not self.is_valid_cell(gx, gy):
                    continue
                
                wx, wy = self.grid_to_world(gx, gy)
                dist = math.sqrt((wx - center_x_m)**2 + (wy - center_y_m)**2)
                if dist <= radius_m:
                    self.set_cell_type(gx, gy, CellType.FREE)


def inflate_obstacles(grid_map: GridMap, inflation_radius_m: float) -> None:
    """Engelleri şişir - güvenli mesafe için."""
    if inflation_radius_m <= 0:
        return
    
    # Create distance transform
    occupied_mask = (grid_map.data == CellType.OCCUPIED)
    
    # Simple inflation: mark cells within radius of any occupied cell
    inflation_cells = int(inflation_radius_m / grid_map.resolution_m)
    
    # Reset cost map
    grid_map.cost_map.fill(0.0)
    
    # For each occupied cell, inflate around it
    occupied_coords = np.where(occupied_mask)
    for occ_y, occ_x in zip(occupied_coords[0], occupied_coords[1]):
        for dy in range(-inflation_cells, inflation_cells + 1):
            for dx in range(-inflation_cells, inflation_cells + 1):
                gx, gy = occ_x + dx, occ_y + dy
                if not grid_map.is_valid_cell(gx, gy):
                    continue
                
                # Distance from occupied cell
                dist_cells = math.sqrt(dx*dx + dy*dy)
                dist_m = dist_cells * grid_map.resolution_m
                
                if dist_m <= inflation_radius_m:
                    # Set high cost for inflated area
                    if grid_map.get_cell_type(gx, gy) == CellType.FREE:
                        # Cost decreases with distance from obstacle
                        cost = 100.0 * (1.0 - dist_m / inflation_radius_m)
                        grid_map.set_cost(gx, gy, max(grid_map.get_cost(gx, gy), cost))
                    else:
                        # Occupied cells have infinite cost
                        grid_map.set_cost(gx, gy, float('inf'))