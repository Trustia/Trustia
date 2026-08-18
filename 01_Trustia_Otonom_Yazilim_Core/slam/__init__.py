"""
TRUSTIA SLAM Sistemi (Simultaneous Localization and Mapping) - Sistem 1, Katman 2

GPS'siz konum belirleme ve haritalama. Kritik algoritmalar:
  * ICP (Iterative Closest Point) - tarama eşleştirme
  * Odometry Integration - ölü hesaplama entegrasyonu
  * Occupancy Grid Mapping - işgal haritası
  * Loop Closure Detection - döngü kapama
  * Pose Graph Optimization - graf optimizasyonu (g2o benzeri)

PLAN 3.3 Katman 2: "GPS'siz konum: ICP tarama eşleştirme, 
ölü hesaplama, olasılıklı harita çıkarma, IMU + LiDAR + kamera
füzyonu. Hedef: 10 km GPS'siz görevde 2-3 metreden az sapma."
"""

from slam.types import (
    Pose2D,
    Pose3D,
    OdometryMeasurement,
    ScanMatch,
    LoopClosure,
    angular_difference,
)
from slam.icp import (
    ICP2D,
    ICP3D,
    ICPConfig,
)
from slam.odometry import (
    OdometryIntegrator,
    WheelOdometry,
    VisualOdometry,
)
from slam.occupancy_grid import (
    OccupancyGrid,
    OccupancyCell,
    LogOdds,
    bresenham_line,
)
from slam.pose_graph import (
    PoseGraph,
    PoseNode,
    PoseEdge,
    optimize_pose_graph,
)
from slam.loop_closure import (
    LoopClosureDetector,
    PlaceRecognition,
    ScanContext,
)
from slam.engine import (
    SlamEngine,
    SlamState,
)

__all__ = [
    # Types
    "Pose2D",
    "Pose3D",
    "OdometryMeasurement",
    "ScanMatch",
    "LoopClosure",
    "angular_difference",
    # ICP
    "ICP2D",
    "ICP3D",
    "ICPConfig",
    # Odometry
    "OdometryIntegrator",
    "WheelOdometry",
    "VisualOdometry",
    # Occupancy Grid
    "OccupancyGrid",
    "OccupancyCell",
    "LogOdds",
    "bresenham_line",
    # Pose Graph
    "PoseGraph",
    "PoseNode",
    "PoseEdge",
    "optimize_pose_graph",
    # Loop Closure
    "LoopClosureDetector",
    "PlaceRecognition",
    "ScanContext",
    # Engine
    "SlamEngine",
    "SlamState",
]
