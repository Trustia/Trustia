"""
Unit and Integration Tests for TRUSTIA ONNX-Driven 3D Deep Perception.
Verifies ONNX model loading, .bin/.pcd LiDAR parsing, pseudo-image pillarization,
and real-time inference latency under ISO 26262 ASIL-D constraints.
"""

import os
import pytest
import numpy as np

from ai.deep_perception import DeepPerceptionEngine, BoundingBox3D, calculate_bev_iou


@pytest.fixture
def core_paths():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    onnx_path = os.path.join(base_dir, "..", "models", "trustia_centerpoint_backbone.onnx")
    bin_path = os.path.join(base_dir, "..", "data", "pointclouds", "sample_drive_001.bin")
    pcd_path = os.path.join(base_dir, "..", "data", "pointclouds", "sample_drive_001.pcd")
    return {
        "onnx": os.path.abspath(onnx_path),
        "bin": os.path.abspath(bin_path),
        "pcd": os.path.abspath(pcd_path),
    }


def test_lidar_file_loaders(core_paths):
    """Verify loading binary (.bin) and ASCII (.pcd) point clouds."""
    # 1. Load BIN
    pts_bin = DeepPerceptionEngine.load_point_cloud_bin(core_paths["bin"])
    assert len(pts_bin) > 500
    p0 = pts_bin[0]
    assert len(p0) == 4  # (x, y, z, intensity)
    assert isinstance(p0[0], float)

    # 2. Load PCD
    pts_pcd = DeepPerceptionEngine.load_point_cloud_pcd(core_paths["pcd"])
    assert len(pts_pcd) == len(pts_bin)
    assert pytest.approx(pts_pcd[0][0], abs=0.01) == pts_bin[0][0]


def test_onnx_model_loading_and_session(core_paths):
    """Verify ONNX Runtime inference session initialization."""
    engine = DeepPerceptionEngine(onnx_model_path=core_paths["onnx"])
    assert engine.onnx_session is not None
    assert engine.onnx_model_path == core_paths["onnx"]


def test_pillar_pseudo_image_preprocessing(core_paths):
    """Verify point cloud voxelization into 64-channel BEV pseudo-image."""
    engine = DeepPerceptionEngine()
    pts = DeepPerceptionEngine.load_point_cloud_bin(core_paths["bin"])
    pseudo_img = engine.preprocess_point_cloud_to_pillars(pts, grid_size=(128, 128))
    
    assert pseudo_img is not None
    assert pseudo_img.shape == (1, 64, 128, 128)
    assert pseudo_img.dtype == np.float32
    # Ensure points actually contributed to channels
    assert np.max(pseudo_img[0, 0, :, :]) > 0.0


def test_onnx_live_inference_with_bin_file(core_paths):
    """Verify end-to-end ONNX model inference from raw .bin LiDAR file."""
    engine = DeepPerceptionEngine(
        confidence_threshold=0.30,
        onnx_model_path=core_paths["onnx"]
    )
    # Preload points (simulating LiDAR UDP frame buffer)
    pts = DeepPerceptionEngine.load_point_cloud_bin(core_paths["bin"])
    boxes, latency_ms = engine.infer(point_cloud=pts)
    
    # Must run deterministically within ASIL-D 35ms budget
    assert latency_ms <= 35.0
    assert engine.last_inference_latency_ms == latency_ms
    assert isinstance(boxes, list)


def test_onnx_output_decoding_and_nms():
    """Verify tensor decoding from mock ONNX outputs to BoundingBox3D."""
    engine = DeepPerceptionEngine(confidence_threshold=0.50, nms_iou_threshold=0.20)
    
    # Create synthetic heatmap with 2 peaks for 'car' (index 0) and 'pedestrian' (index 1)
    heatmap = np.zeros((1, 7, 128, 128), dtype=np.float32)
    heatmap[0, 0, 32, 64] = 0.92  # Car at grid (32, 64)
    heatmap[0, 1, 16, 80] = 0.85  # Pedestrian at grid (16, 80)
    
    box_reg = np.zeros((1, 8, 128, 128), dtype=np.float32)
    # Box dimensions: dx, dy, dz, w_offset, l_offset, h_offset, sin_yaw, cos_yaw
    box_reg[0, 3, 32, 64] = 0.05  # slight width offset
    box_reg[0, 7, 32, 64] = 1.0   # cos(yaw) = 1 -> yaw = 0
    
    velocity = np.zeros((1, 2, 128, 128), dtype=np.float32)
    velocity[0, 0, 32, 64] = 8.5   # vx = 8.5 m/s
    
    boxes = engine.decode_onnx_outputs(heatmap, box_reg, velocity)
    assert len(boxes) == 2
    
    car_box = next(b for b in boxes if b.class_name == "car")
    ped_box = next(b for b in boxes if b.class_name == "pedestrian")
    
    assert car_box.confidence == pytest.approx(0.92, abs=0.01)
    assert car_box.velocity_x == pytest.approx(8.5, abs=0.01)
    assert ped_box.confidence == pytest.approx(0.85, abs=0.01)
