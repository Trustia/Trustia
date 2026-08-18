"""
TRUSTIA SLAM Engine - Integrated SLAM state estimator and map builder.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional

from slam.types import Pose2D, OdometryMeasurement
from slam.odometry import OdometryIntegrator
from slam.occupancy_grid import OccupancyGrid


@dataclass
class SlamState:
    """SLAM anlık durum özeti."""
    pose: Pose2D
    occupied_cells: int = 0
    total_distance_m: float = 0.0
    correction_count: int = 0


class SlamEngine:
    """SLAM Tümleşik Konum ve İşgal Haritası Motoru."""
    def __init__(
        self,
        grid_resolution_m: float = 0.5,
        grid_width_m: float = 100.0,
        grid_height_m: float = 100.0,
    ) -> None:
        self.odom = OdometryIntegrator()
        self.grid = OccupancyGrid(resolution_m=grid_resolution_m, width_m=grid_width_m, height_m=grid_height_m)
        self.correction_count = 0

    @property
    def pose(self) -> Pose2D:
        return self.odom.pose

    def step(self, measurement: OdometryMeasurement, scan_hits: Optional[List[Tuple[float, float]]] = None) -> SlamState:
        self.odom.update(measurement)
        if scan_hits:
            origin = (self.odom.pose.x_m, self.odom.pose.y_m)
            self.grid.update_scan(origin, scan_hits)

        occ = self.grid.count_state(OccupancyGrid.OCCUPIED)
        return SlamState(
            pose=self.odom.pose,
            occupied_cells=occ,
            total_distance_m=self.odom.total_distance_m,
            correction_count=self.correction_count,
        )

    def apply_correction(self, corrected_pose: Pose2D) -> None:
        self.odom.set_pose(corrected_pose)
        self.correction_count += 1

    def reset(self) -> None:
        self.odom.reset()
        self.grid.reset()
        self.correction_count = 0
