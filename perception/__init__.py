"""
TRUSTIA Algı Sistemi (Perception) - Sistem 1, Katman 1

LiDAR nokta bulutu işleme, engel tespiti, zemin segmentasyonu ve
3D ortam algısı. Endüstri standardı algoritmalarla gerçek zamanlı
nokta bulutu işleme.

Modüller:
  * filters      : Voxel grid, statistical outlier removal, radius filter
  * ground       : RANSAC zemin segmentasyonu, multi-plane fitting
  * clustering   : Euclidean clustering, DBSCAN, region growing
  * obstacle     : Engel tespiti, sınıflandırma, tracking
  * types        : Veri yapıları (LaserScan, PointCloud, Obstacle)

PLAN 3.3 Katman 1: "LiDAR nokta bulutu alımı, filtreleme,
engel tespiti ve sınıflandırma, arazi geçilebilirlik haritası."
"""

from perception.types import (
    LaserScan,
    PointCloud,
    Point3D,
    Obstacle,
    ObstacleClass,
    BoundingBox,
    LaserPoint,
    FieldOfView,
)
from perception.filters import (
    PointCloudFilter,
    VoxelGridFilter,
    StatisticalOutlierFilter,
    RadiusOutlierFilter,
    PassThroughFilter,
)
from perception.ground import (
    GroundSegmenter,
    RANSACGroundSegmenter,
    MultiPlaneSegmenter,
    GroundPlane,
)
from perception.clustering import (
    Clusterer,
    EuclideanClusterer,
    DBSCANClusterer,
    RegionGrowingClusterer,
    Cluster,
)
from perception.obstacle import (
    ObstacleDetector,
    ObstacleTracker,
    KalmanTracker,
    DetectionResult,
)

__all__ = [
    # Types
    "LaserScan",
    "PointCloud",
    "Point3D",
    "Obstacle",
    "ObstacleClass",
    "BoundingBox",
    "LaserPoint",
    "FieldOfView",
    # Filters
    "PointCloudFilter",
    "VoxelGridFilter",
    "StatisticalOutlierFilter",
    "RadiusOutlierFilter",
    "PassThroughFilter",
    # Ground Segmentation
    "GroundSegmenter",
    "RANSACGroundSegmenter",
    "MultiPlaneSegmenter",
    "GroundPlane",
    # Clustering
    "Clusterer",
    "EuclideanClusterer",
    "DBSCANClusterer",
    "RegionGrowingClusterer",
    "Cluster",
    # Obstacle Detection
    "ObstacleDetector",
    "ObstacleTracker",
    "KalmanTracker",
    "DetectionResult",
]
