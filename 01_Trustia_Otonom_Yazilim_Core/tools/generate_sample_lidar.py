"""
Generates standard binary (.bin) and ASCII (.pcd) point cloud sample files.
Format compatible with KITTI and nuScenes (x, y, z, intensity as float32).
"""

import os
import struct
import numpy as np


def generate_sample_lidar(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(1337)
    
    points = []
    
    # 1. Road surface: z ~ -1.5, x in [2, 60], y in [-15, 15]
    for _ in range(1500):
        x = np.random.uniform(2.0, 50.0)
        y = np.random.uniform(-10.0, 10.0)
        z = -1.6 + np.random.normal(0, 0.03)
        intensity = np.random.uniform(10.0, 40.0)
        points.append([x, y, z, intensity])
        
    # 2. Leading Car: Center at x=18.0, y=0.0, z=-0.6 (dim: 4.5 x 2.0 x 1.6)
    for _ in range(350):
        x = 18.0 + np.random.uniform(-2.2, 2.2)
        y = 0.0 + np.random.uniform(-1.0, 1.0)
        z = -0.6 + np.random.uniform(-0.8, 0.8)
        intensity = np.random.uniform(60.0, 100.0)
        points.append([x, y, z, intensity])
        
    # 3. Pedestrian on sidewalk: Center at x=9.0, y=3.5, z=-0.7 (dim: 0.6 x 0.6 x 1.7)
    for _ in range(80):
        x = 9.0 + np.random.uniform(-0.3, 0.3)
        y = 3.5 + np.random.uniform(-0.3, 0.3)
        z = -0.7 + np.random.uniform(-0.85, 0.85)
        intensity = np.random.uniform(40.0, 80.0)
        points.append([x, y, z, intensity])
        
    # 4. Cyclist: Center at x=14.0, y=-2.5, z=-0.8 (dim: 1.8 x 0.6 x 1.4)
    for _ in range(120):
        x = 14.0 + np.random.uniform(-0.9, 0.9)
        y = -2.5 + np.random.uniform(-0.3, 0.3)
        z = -0.8 + np.random.uniform(-0.7, 0.7)
        intensity = np.random.uniform(50.0, 90.0)
        points.append([x, y, z, intensity])

    pts_arr = np.array(points, dtype=np.float32)
    
    # Save .bin (KITTI / nuScenes raw binary)
    bin_path = os.path.join(output_dir, "sample_drive_001.bin")
    pts_arr.tofile(bin_path)
    
    # Save .pcd (Standard Point Cloud Data format)
    pcd_path = os.path.join(output_dir, "sample_drive_001.pcd")
    with open(pcd_path, "w", encoding="utf-8") as f:
        f.write("# .PCD v0.7 - Point Cloud Data\n")
        f.write("VERSION 0.7\n")
        f.write("FIELDS x y z intensity\n")
        f.write("SIZE 4 4 4 4\n")
        f.write("TYPE F F F F\n")
        f.write("COUNT 1 1 1 1\n")
        f.write(f"WIDTH {len(pts_arr)}\n")
        f.write("HEIGHT 1\n")
        f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
        f.write(f"POINTS {len(pts_arr)}\n")
        f.write("DATA ascii\n")
        for p in pts_arr:
            f.write(f"{p[0]:.4f} {p[1]:.4f} {p[2]:.4f} {p[3]:.1f}\n")

    print(f"Generated {len(pts_arr)} points:")
    print(f" - BIN: {bin_path} ({os.path.getsize(bin_path)} bytes)")
    print(f" - PCD: {pcd_path} ({os.path.getsize(pcd_path)} bytes)")
    return bin_path, pcd_path


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(script_dir, "..", "data", "pointclouds")
    generate_sample_lidar(target_dir)
