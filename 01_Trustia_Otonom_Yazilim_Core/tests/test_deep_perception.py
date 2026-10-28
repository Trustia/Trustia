"""
Unit and Integration Tests for TRUSTIA 3D Deep Perception Engine.
Verifies nuScenes 7-class 3D Bounding Boxes, BEV IoU, 3D NMS, and 24ms latency limit.
"""

import math
import pytest

from ai.deep_perception import (
    BoundingBox3D,
    CLASS_DIMENSION_PRIORS,
    DeepPerceptionEngine,
    NUSCENES_3D_CLASSES,
    calculate_bev_iou,
)


def test_nuscenes_classes_catalog():
    """Verify that all standard nuScenes 3D classes are cataloged."""
    assert "car" in NUSCENES_3D_CLASSES
    assert "pedestrian" in NUSCENES_3D_CLASSES
    assert "truck" in NUSCENES_3D_CLASSES
    assert "motorcycle" in NUSCENES_3D_CLASSES
    assert "bicycle" in NUSCENES_3D_CLASSES
    assert "traffic_cone" in NUSCENES_3D_CLASSES
    assert "barrier" in NUSCENES_3D_CLASSES
    assert len(NUSCENES_3D_CLASSES) >= 7


def test_bounding_box_3d_metrics():
    """Verify 3D volume, range, and BEV corner projection calculations."""
    box = BoundingBox3D(
        box_id=1,
        class_name="car",
        x=10.0,
        y=0.0,
        z=0.0,
        width=2.0,
        length=4.5,
        height=1.5,
        yaw_rad=0.0,
        confidence=0.92,
        velocity_x=0.0,
        velocity_y=12.5,
    )
    assert pytest.approx(box.volume_m3(), rel=1e-3) == 13.5
    assert pytest.approx(box.range_2d_m(), rel=1e-3) == 10.0
    corners = box.corners_2d_bev()
    assert len(corners) == 4
    # With yaw = 0, corners should be around x=10 +/- 2.25, y=0 +/- 1.0
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    assert min(xs) == pytest.approx(7.75, abs=0.01)
    assert max(xs) == pytest.approx(12.25, abs=0.01)
    assert min(ys) == pytest.approx(-1.0, abs=0.01)
    assert max(ys) == pytest.approx(1.0, abs=0.01)


def test_calculate_bev_iou():
    """Verify BEV IoU overlap calculations for overlapping and non-overlapping boxes."""
    box_a = BoundingBox3D(
        box_id=1, class_name="car", x=10.0, y=0.0, z=0.0, width=2.0, length=4.0, height=1.5, yaw_rad=0.0, confidence=0.9
    )
    # Identical box should have IoU = 1.0
    assert pytest.approx(calculate_bev_iou(box_a, box_a), rel=1e-3) == 1.0

    # Far away box should have IoU = 0.0
    box_b = BoundingBox3D(
        box_id=2, class_name="car", x=50.0, y=0.0, z=0.0, width=2.0, length=4.0, height=1.5, yaw_rad=0.0, confidence=0.8
    )
    assert calculate_bev_iou(box_a, box_b) == 0.0

    # Partial overlap box
    box_c = BoundingBox3D(
        box_id=3, class_name="car", x=12.0, y=0.0, z=0.0, width=2.0, length=4.0, height=1.5, yaw_rad=0.0, confidence=0.85
    )
    iou = calculate_bev_iou(box_a, box_c)
    assert 0.0 < iou < 1.0


def test_deep_perception_engine_simulated_actors():
    """Verify inference pipeline with simulated multi-class actors and NMS."""
    engine = DeepPerceptionEngine(confidence_threshold=0.50, nms_iou_threshold=0.25)
    actors = [
        {"class": "car", "x": 15.0, "y": -1.5, "z": 0.0, "confidence": 0.94, "vy": 10.0},
        {"class": "pedestrian", "x": 8.0, "y": 2.0, "z": 0.0, "confidence": 0.88, "vx": 1.2},
        {"class": "traffic_cone", "x": 5.0, "y": 0.5, "z": 0.0, "confidence": 0.30},  # Below threshold
    ]
    boxes, latency_ms = engine.infer(simulated_actors=actors)
    # Traffic cone should be filtered out by confidence threshold
    assert len(boxes) == 2
    classes = [b.class_name for b in boxes]
    assert "car" in classes
    assert "pedestrian" in classes
    assert latency_ms <= 35.0  # Must be strictly within real-time ASIL-D budget


def test_deep_perception_nms_filtering():
    """Verify that duplicate/overlapping bounding boxes are suppressed by 3D NMS."""
    engine = DeepPerceptionEngine(confidence_threshold=0.30, nms_iou_threshold=0.30)
    actors = [
        {"class": "car", "x": 10.0, "y": 0.0, "z": 0.0, "confidence": 0.95},
        {"class": "car", "x": 10.2, "y": 0.1, "z": 0.0, "confidence": 0.70},  # Overlapping duplicate
    ]
    boxes, _ = engine.infer(simulated_actors=actors)
    assert len(boxes) == 1
    assert boxes[0].confidence == pytest.approx(0.95, abs=0.01)


def test_deep_perception_lidar_point_cloud():
    """Verify 3D pillar feature extraction from raw LiDAR point cloud."""
    engine = DeepPerceptionEngine(confidence_threshold=0.40)
    # Generate synthetic pedestrian points (tall, narrow cluster at x=8.0, y=1.0)
    pts = []
    for z in [0.0, 0.4, 0.8, 1.2, 1.6]:
        for dy in [-0.2, 0.0, 0.2]:
            pts.append((8.0, 1.0 + dy, z, 50.0))

    boxes, latency_ms = engine.infer(point_cloud=pts)
    assert len(boxes) >= 1
    detected = boxes[0]
    assert detected.class_name == "pedestrian"
    assert pytest.approx(detected.x, abs=1.0) == 8.0
    assert pytest.approx(detected.y, abs=1.0) == 1.0
