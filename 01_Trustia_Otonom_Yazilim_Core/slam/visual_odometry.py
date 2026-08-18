"""
TRUSTIA SLAM Katmanı - Görsel Odometri (Visual Odometry - Mono/Stereo Camera Odometry).

Kabiliyetler:
  * Kamera Kareleri Arasındaki Hareketi Tahmin Etme (Optical Flow / Feature Motion)
  * Görsel İlerleme Mesafesi ve Yön Hesaplama (Visual Dead Reckoning)
"""

from __future__ import annotations

import math
from typing import List, Tuple, Optional
import numpy as np


class VisualOdometryEstimator:
    """Saf NumPy Tabanlı Görsel Odometri Hesaplayıcısı."""

    def __init__(self, focal_length_px: float = 800.0) -> None:
        self.focal_length_px = focal_length_px
        self.prev_features: Optional[np.ndarray] = None

    def estimate_motion(self, current_features: np.ndarray) -> Tuple[float, float]:
        """İki kamera karesi arasındaki piksel hareketinden (delta_x, delta_yaw) mesafe hesaplar."""
        if self.prev_features is None or len(current_features) == 0:
            self.prev_features = current_features
            return (0.0, 0.0)

        # Average feature shift
        shift = np.mean(current_features - self.prev_features, axis=0)
        self.prev_features = current_features

        delta_dist = float(np.linalg.norm(shift)) * 0.01  # scale factor
        delta_yaw = math.atan2(float(shift[0]), self.focal_length_px)
        return (delta_dist, delta_yaw)
