"""
TRUSTIA SLAM - Occupancy Grid Mapping.

Olasılıklı ızgara haritası - her hücre dolu/boş olasılığını tutar.
Log-odds representation ile verimli güncelleme.

Bresenham ray tracing: Sensörden engele kadar çizgi boyunca
hücreler 'boş' olarak işaretlenir, engel noktası 'dolu'.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np


@dataclass
class LogOdds:
    """Log-odds olasılık temsili."""

    @staticmethod
    def from_probability(p: float) -> float:
        p = max(0.001, min(0.999, p))
        return math.log(p / (1.0 - p))

    @staticmethod
    def to_probability(l: float) -> float:
        return 1.0 / (1.0 + math.exp(-l))

    @staticmethod
    def update(l_old: float, l_new: float) -> float:
        return l_old + l_new


@dataclass
class OccupancyCell:
    """Tek ızgara hücresi."""
    x: int
    y: int
    log_odds: float = 0.0

    @property
    def probability(self) -> float:
        return LogOdds.to_probability(self.log_odds)

    @property
    def occupied(self) -> bool:
        return self.log_odds > 0.0

    @property
    def free(self) -> bool:
        return self.log_odds < 0.0

    @property
    def unknown(self) -> bool:
        return abs(self.log_odds) < 0.01


def bresenham_line(start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Bresenham çizgi algoritması."""
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    line = []
    x, y = x0, y0
    while True:
        line.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return line


class OccupancyGrid:
    """2D olasılıklı ızgara haritası."""
    UNKNOWN = 0
    FREE = 1
    OCCUPIED = 2

    def __init__(
        self,
        resolution_m: float = 0.5,
        width_m: float = 50.0,
        height_m: float = 50.0,
        center: Tuple[float, float] = (0.0, 0.0),
    ) -> None:
        if width_m <= 0 or height_m <= 0 or resolution_m <= 0:
            from core.errors import SensorError
            raise SensorError("Boyutlar pozitif olmalı")

        self.width_m = width_m
        self.height_m = height_m
        self.resolution_m = resolution_m
        self.center = center

        self.width_cells = max(1, int(width_m / resolution_m))
        self.height_cells = max(1, int(height_m / resolution_m))

        self._grid: Dict[Tuple[int, int], int] = {}
        self.l_occ = LogOdds.from_probability(0.7)
        self.l_free = LogOdds.from_probability(0.3)
        self.l_min = LogOdds.from_probability(0.01)
        self.l_max = LogOdds.from_probability(0.99)

    def world_to_grid(self, x_m: float, y_m: float) -> Tuple[int, int]:
        x_rel = x_m - self.center[0] + self.width_m / 2.0
        y_rel = y_m - self.center[1] + self.height_m / 2.0
        return int(x_rel / self.resolution_m), int(y_rel / self.resolution_m)

    def grid_to_world(self, i: int, j: int) -> Tuple[float, float]:
        x_m = i * self.resolution_m - self.width_m / 2.0 + self.center[0]
        y_m = j * self.resolution_m - self.height_m / 2.0 + self.center[1]
        return x_m + self.resolution_m / 2.0, y_m + self.resolution_m / 2.0

    def in_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self.width_cells and 0 <= j < self.height_cells

    def get_cell(self, x_m: float, y_m: float) -> int:
        i, j = self.world_to_grid(x_m, y_m)
        if not self.in_bounds(i, j):
            return self.UNKNOWN
        return self._grid.get((i, j), self.UNKNOWN)

    def mark_free(self, x_m: float, y_m: float) -> None:
        i, j = self.world_to_grid(x_m, y_m)
        if self.in_bounds(i, j):
            self._grid[(i, j)] = self.FREE

    def mark_occupied(self, x_m: float, y_m: float) -> None:
        i, j = self.world_to_grid(x_m, y_m)
        if self.in_bounds(i, j):
            self._grid[(i, j)] = self.OCCUPIED

    def is_free(self, x_m: float, y_m: float) -> bool:
        return self.get_cell(x_m, y_m) == self.FREE

    def is_occupied(self, x_m: float, y_m: float) -> bool:
        return self.get_cell(x_m, y_m) == self.OCCUPIED

    def count_state(self, state: int) -> int:
        return sum(1 for v in self._grid.values() if v == state)

    def known_ratio(self) -> float:
        total = self.width_cells * self.height_cells
        known = sum(1 for v in self._grid.values() if v != self.UNKNOWN)
        return known / total if total > 0 else 0.0

    def raycast(self, start: Tuple[float, float], end: Tuple[float, float]) -> List[Tuple[float, float]]:
        x0, y0 = start
        x1, y1 = end
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(1, int(dist / (self.resolution_m * 0.5)))
        pts = []
        for s in range(steps + 1):
            t = s / steps
            wx = x0 + t * (x1 - x0)
            wy = y0 + t * (y1 - y0)
            i, j = self.world_to_grid(wx, wy)
            cx, cy = self.grid_to_world(i, j)
            if (cx, cy) not in pts:
                pts.append((cx, cy))
        return pts

    def neighbors_4(self, x_m: float, y_m: float) -> List[Tuple[float, float]]:
        r = self.resolution_m
        return [
            (x_m + r, y_m),
            (x_m - r, y_m),
            (x_m, y_m + r),
            (x_m, y_m - r),
        ]

    def update_scan(self, origin: Tuple[float, float], scan_hits: List[Tuple[float, float]]) -> int:
        updated = 0
        for hit in scan_hits:
            pts = self.raycast(origin, hit)
            for px, py in pts[:-1]:
                self.mark_free(px, py)
                updated += 1
            self.mark_occupied(hit[0], hit[1])
            updated += 1
        return updated

    def reset(self) -> None:
        self._grid.clear()
