"""Sistem 1 — Algı (LiDAR/engel tespiti) birim testleri."""

import math

import pytest

from core.errors import SensorError
from core.transforms import EnuPoint
from perception import (
    LaserPoint,
    Obstacle,
    ObstacleDetector,
    PointCloudFilter,
    Clusterer,
    FieldOfView,
)


def ring(center_range, count=36, start_angle=0.0):
    """Belirli menzildeki noktaları 10° aralıklarla üretir."""
    points = []
    for i in range(count):
        angle = start_angle + 2.0 * math.pi * i / count
        points.append(LaserPoint(
            range_m=center_range,
            angle_rad=angle,
        ))
    return points


def test_filter_rejects_near_points():
    filt = PointCloudFilter(min_range_m=0.5, max_range_m=10.0)
    points = [LaserPoint(0.1, 0.0), LaserPoint(5.0, 0.0)]
    result = filt.apply(points)
    assert len(result) == 1
    assert result[0].range_m == 5.0


def test_filter_rejects_far_points():
    filt = PointCloudFilter(min_range_m=0.5, max_range_m=10.0)
    points = [LaserPoint(11.0, 0.0), LaserPoint(9.0, 0.0)]
    result = filt.apply(points)
    assert len(result) == 1


def test_filter_rejects_invalid_range_config():
    with pytest.raises(SensorError):
        PointCloudFilter(min_range_m=5.0, max_range_m=5.0)


def test_filter_ground_removal():
    filt = PointCloudFilter(
        min_range_m=0.1, max_range_m=10.0, ground_clearance_m=0.2
    )
    ground = LaserPoint(5.0, 0.0, elevation_rad=0.01)  # 5cm yükseklik
    above = LaserPoint(5.0, 0.0, elevation_rad=0.2)    # ~1m yükseklik
    result = filt.apply([ground, above])
    assert len(result) == 1


def test_clusterer_splits_gaps():
    clusterer = Clusterer(
        angular_resolution_rad=math.radians(1.0),
        gap_scale=2.0,
        min_cluster_points=1,
    )
    # 5 m'de iki nokta arası açı 20° → çizgisel mesafe ~1.74 m
    # 5 m'de iki nokta arası açı 1° → çizgisel mesafe ~0.087 m
    near = [
        LaserPoint(5.0, math.radians(0)),
        LaserPoint(5.0, math.radians(1)),
    ]
    far = [LaserPoint(5.0, math.radians(30))]
    clusters = clusterer.cluster(near + far)
    assert len(clusters) == 2


def test_clusterer_merges_close():
    clusterer = Clusterer(angular_resolution_rad=math.radians(1.0), gap_scale=2.0)
    points = [
        LaserPoint(5.0, math.radians(0)),
        LaserPoint(5.0, math.radians(1)),
        LaserPoint(5.0, math.radians(2)),
    ]
    clusters = clusterer.cluster(points)
    assert len(clusters) == 1


def test_clusterer_min_points_filter():
    clusterer = Clusterer(min_cluster_points=3)
    points = [LaserPoint(5.0, 0.0), LaserPoint(5.0, 0.01)]
    assert clusterer.cluster(points) == []


def test_detector_finds_obstacle():
    detector = ObstacleDetector(
        safety_radius_m=0.0,
        clusterer=Clusterer(
            angular_resolution_rad=math.radians(2.0),
            gap_scale=2.0,
        ),
    )
    # 0° çevresinde yoğun nokta kümesi → tek engel (2° aralıklı sık tarama)
    points = [
        LaserPoint(5.0, math.radians(-10.0 + 2.0 * i))
        for i in range(11)
    ]
    vehicle = EnuPoint(0.0, 0.0)
    obstacles = detector.detect(points, vehicle)
    assert len(obstacles) == 1
    obstacle = obstacles[0]
    # engel ~5 m ileride (0° yönü) → merkez (5,0) civarı
    assert math.hypot(obstacle.center.east_m - 5.0,
                      obstacle.center.north_m) < 0.3
    assert obstacle.point_count == 11


def test_detector_empty_scan():
    detector = ObstacleDetector()
    assert detector.detect([], EnuPoint(0.0, 0.0)) == []


def test_danger_level_zero_at_distance():
    obstacle = Obstacle(
        id=1,
        center=EnuPoint(12.0, 0.0),
        radius_m=0.5,
        point_count=3,
        max_range_m=13.0,
    )
    assessed = ObstacleDetector._assess_danger(obstacle, EnuPoint(0.0, 0.0))
    assert assessed.danger_level == 0.0


def test_danger_level_max_at_collision():
    obstacle = Obstacle(
        id=1,
        center=EnuPoint(0.3, 0.0),
        radius_m=0.5,
        point_count=3,
        max_range_m=1.0,
    )
    assessed = ObstacleDetector._assess_danger(obstacle, EnuPoint(0.0, 0.0))
    assert assessed.danger_level == 1.0


def test_danger_scales_between():
    obstacle = Obstacle(
        id=1,
        center=EnuPoint(5.0, 0.0),
        radius_m=0.5,
        point_count=3,
        max_range_m=6.0,
    )
    assessed = ObstacleDetector._assess_danger(obstacle, EnuPoint(0.0, 0.0))
    assert 0.0 < assessed.danger_level < 1.0


def test_obstacle_distance():
    obstacle = Obstacle(
        id=1,
        center=EnuPoint(5.0, 0.0),
        radius_m=0.5,
        point_count=3,
        max_range_m=6.0,
    )
    assert abs(obstacle.distance_to(EnuPoint(0.0, 0.0)) - 4.5) < 1e-9


def test_fov_angular_width():
    fov = FieldOfView(-math.pi / 4, math.pi / 4, 30.0)
    assert abs(fov.angular_width_deg - 90.0) < 1e-9


def test_fov_invalid_angles():
    with pytest.raises(SensorError):
        FieldOfView(math.pi / 4, -math.pi / 4, 30.0)


def test_fov_contains():
    fov = FieldOfView(-math.pi / 4, math.pi / 4, 30.0)
    inside = LaserPoint(10.0, 0.0)
    outside = LaserPoint(10.0, math.pi / 2)
    assert fov.contains(inside) is True
    assert fov.contains(outside) is False


def test_fov_coverage_ratio():
    fov = FieldOfView(-math.pi / 4, math.pi / 4, 30.0)
    points = [LaserPoint(5.0, 0.0), LaserPoint(5.0, math.pi), LaserPoint(5.0, 0.1)]
    assert abs(fov.coverage_ratio(points) - 2 / 3) < 1e-9
    assert fov.coverage_ratio([]) == 0.0
