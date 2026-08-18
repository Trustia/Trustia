"""
TRUSTIA SLAM - Loop Closure Detection.

Robot aynı yere geri döndüğünde bunu tespit eder. Büyük drift
birikmiş olabilir - loop closure ile düzeltilir.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

from slam.types import Pose2D, LoopClosure


@dataclass
class ScanContext:
    """LiDAR tarama bağlam imzası."""
    descriptor: np.ndarray
    max_range: float
    
    @classmethod
    def from_scan(cls, points: np.ndarray, n_rings: int = 20, n_sectors: int = 60, max_range: float = 20.0) -> "ScanContext":
        descriptor = np.zeros((n_rings, n_sectors))
        for point in points:
            x, y = point
            r = math.sqrt(x*x + y*y)
            if r > max_range:
                continue
            theta = math.atan2(y, x)
            ring_idx = min(int(r / max_range * n_rings), n_rings - 1)
            sector_idx = min(int((theta + math.pi) / (2 * math.pi) * n_sectors), n_sectors - 1)
            descriptor[ring_idx, sector_idx] = max(descriptor[ring_idx, sector_idx], 1.0)
        return cls(descriptor=descriptor, max_range=max_range)
    
    def distance_to(self, other: "ScanContext") -> float:
        best_dist = float('inf')
        n_sectors = self.descriptor.shape[1]
        for shift in range(n_sectors):
            shifted = np.roll(other.descriptor, shift, axis=1)
            dot = np.sum(self.descriptor * shifted)
            norm1 = np.linalg.norm(self.descriptor)
            norm2 = np.linalg.norm(shifted)
            if norm1 > 0 and norm2 > 0:
                similarity = dot / (norm1 * norm2)
                best_dist = min(best_dist, 1.0 - similarity)
        return best_dist


class PlaceRecognition:
    def __init__(self, similarity_threshold: float = 0.15, min_time_gap_s: float = 30.0) -> None:
        self.similarity_threshold = similarity_threshold
        self.min_time_gap_s = min_time_gap_s
        self._contexts: Dict[int, ScanContext] = {}
        self._timestamps: Dict[int, int] = {}
        self._poses: Dict[int, Pose2D] = {}
    
    def add_node(self, node_id: int, scan_points: np.ndarray, pose: Pose2D, timestamp_ns: int) -> None:
        context = ScanContext.from_scan(scan_points)
        self._contexts[node_id] = context
        self._timestamps[node_id] = timestamp_ns
        self._poses[node_id] = pose
    
    def find_candidates(self, scan_points: np.ndarray, current_node_id: int, current_timestamp_ns: int, top_k: int = 5) -> List[Tuple[int, float]]:
        query_context = ScanContext.from_scan(scan_points)
        candidates = []
        for node_id, context in self._contexts.items():
            if node_id == current_node_id:
                continue
            time_gap_s = abs(current_timestamp_ns - self._timestamps[node_id]) / 1e9
            if time_gap_s < self.min_time_gap_s:
                continue
            distance = query_context.distance_to(context)
            if distance < self.similarity_threshold:
                candidates.append((node_id, distance))
        candidates.sort(key=lambda x: x[1])
        return candidates[:top_k]


class LoopClosureDetector:
    def __init__(self) -> None:
        self.place_recognition = PlaceRecognition()
        self._closures: List[LoopClosure] = []
    
    def detect(self, current_node_id: int, scan_points: np.ndarray, current_pose: Pose2D, timestamp_ns: int) -> Optional[LoopClosure]:
        candidates = self.place_recognition.find_candidates(scan_points, current_node_id, timestamp_ns)
        if not candidates:
            return None
        matched_node_id, score = candidates[0]
        matched_pose = self.place_recognition._poses.get(matched_node_id)
        if matched_pose and matched_pose.distance_to(current_pose) > 10.0:
            confidence = 1.0 - score
            if confidence > 0.7:
                closure = LoopClosure(
                    current_node_id=current_node_id,
                    matched_node_id=matched_node_id,
                    relative_pose=matched_pose.inverse().compose(current_pose),
                    confidence=confidence,
                    distance_m=matched_pose.distance_to(current_pose),
                    timestamp_ns=timestamp_ns,
                )
                self._closures.append(closure)
                return closure
        return None