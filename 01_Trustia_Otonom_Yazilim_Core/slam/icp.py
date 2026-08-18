"""
TRUSTIA SLAM - ICP (Iterative Closest Point) Scan Matching.

İki nokta bulutunu/taramayı hizalar. GPS olmadan konum belirlemenin
temel yöntemi: önceki tarama ile yeni tarama eşleştirilir, araç
hareketi bulunur.

Algoritma:
  1. En yakın nokta eşleştirmeleri bul
  2. Optimal dönüşümü hesapla (SVD)
  3. Dönüşümü uygula
  4. Yakınsayana kadar tekrarla

2D ve 3D versiyonları.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from slam.types import Pose2D, Pose3D, ScanMatch


@dataclass
class ICPConfig:
    """ICP algoritması parametreleri."""
    max_iterations: int = 50
    convergence_threshold: float = 1e-6  # Değişim eşiği (metre)
    max_correspondence_distance: float = 1.0  # Maksimum eşleştirme mesafesi
    outlier_ratio: float = 0.8  # En iyi % kaç eşleştirme kullanılır
    min_inliers: int = 10  # Minimum eşleştirme sayısı


class ICP2D:
    """2D ICP - lazer tarama eşleştirme.
    
    İki 2D nokta kümesini hizalar (x, y düzleminde).
    GPS'siz odometry düzeltmesi için kritik.
    
    Kullanım:
        icp = ICP2D()
        match = icp.align(source_points, target_points)
        corrected_pose = current_pose.compose(match.transform)
    """

    def __init__(self, config: Optional[ICPConfig] = None) -> None:
        self.config = config or ICPConfig()

    def align(
        self,
        source: np.ndarray,
        target: np.ndarray,
        initial_guess: Optional[Pose2D] = None,
    ) -> ScanMatch:
        """İki nokta kümesini hizala.
        
        Args:
            source: (N, 2) kaynak noktalar
            target: (M, 2) hedef noktalar
            initial_guess: Başlangıç tahmini (opsiyonel)
        
        Returns:
            ScanMatch sonucu (source → target dönüşümü)
        """
        if source.shape[0] < 3 or target.shape[0] < 3:
            return ScanMatch(
                transform=Pose2D(0, 0, 0),
                fitness_score=float('inf'),
                inlier_rmse=float('inf'),
                converged=False,
                iterations=0,
            )
        
        # Initial transform
        if initial_guess is not None:
            current_source = self._apply_transform_2d(source, initial_guess)
            cumulative_transform = initial_guess
        else:
            current_source = source.copy()
            cumulative_transform = Pose2D(0, 0, 0)
        
        prev_error = float('inf')
        
        for iteration in range(self.config.max_iterations):
            # 1. Find correspondences (nearest neighbors)
            correspondences, distances = self._find_correspondences(
                current_source, target
            )
            
            # 2. Reject outliers
            valid_mask = distances < self.config.max_correspondence_distance
            if valid_mask.sum() < self.config.min_inliers:
                break
            
            # Keep best correspondences
            n_keep = int(valid_mask.sum() * self.config.outlier_ratio)
            if n_keep < self.config.min_inliers:
                n_keep = self.config.min_inliers
            
            sorted_indices = np.argsort(distances[valid_mask])[:n_keep]
            valid_indices = np.where(valid_mask)[0][sorted_indices]
            
            src_matched = current_source[valid_indices]
            tgt_matched = target[correspondences[valid_indices]]
            
            # 3. Compute optimal transform (SVD)
            delta_transform = self._compute_transform_2d(src_matched, tgt_matched)
            
            # 4. Apply transform
            current_source = self._apply_transform_2d(current_source, delta_transform)
            cumulative_transform = cumulative_transform.compose(delta_transform)
            
            # 5. Check convergence
            mean_error = distances[valid_indices].mean()
            error_change = abs(prev_error - mean_error)
            
            if error_change < self.config.convergence_threshold:
                fitness = float(mean_error)
                rmse = float(np.sqrt((distances[valid_indices] ** 2).mean()))
                return ScanMatch(
                    transform=cumulative_transform,
                    fitness_score=fitness,
                    inlier_rmse=rmse,
                    converged=True,
                    iterations=iteration + 1,
                )
            
            prev_error = mean_error
        
        # Did not converge
        correspondences, distances = self._find_correspondences(current_source, target)
        valid_mask = distances < self.config.max_correspondence_distance
        
        if valid_mask.sum() > 0:
            fitness = float(distances[valid_mask].mean())
            rmse = float(np.sqrt((distances[valid_mask] ** 2).mean()))
        else:
            fitness = float('inf')
            rmse = float('inf')
        
        return ScanMatch(
            transform=cumulative_transform,
            fitness_score=fitness,
            inlier_rmse=rmse,
            converged=False,
            iterations=self.config.max_iterations,
        )

    def _find_correspondences(
        self, source: np.ndarray, target: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Her kaynak nokta için en yakın hedef noktayı bul.
        
        Returns:
            correspondences: (N,) hedef indisleri
            distances: (N,) mesafeler
        """
        # Brute force (optimize edilebilir KD-tree ile)
        n_source = source.shape[0]
        correspondences = np.zeros(n_source, dtype=int)
        distances = np.zeros(n_source)
        
        for i in range(n_source):
            dists = np.linalg.norm(target - source[i], axis=1)
            correspondences[i] = np.argmin(dists)
            distances[i] = dists[correspondences[i]]
        
        return correspondences, distances

    def _compute_transform_2d(
        self, source: np.ndarray, target: np.ndarray
    ) -> Pose2D:
        """Optimal 2D rigid transform (rotation + translation).
        
        SVD yöntemi: https://igl.ethz.ch/projects/ARAP/svd_rot.pdf
        """
        # Merkezleri bul
        src_center = source.mean(axis=0)
        tgt_center = target.mean(axis=0)
        
        # Merkezden uzaklıkları
        src_centered = source - src_center
        tgt_centered = target - tgt_center
        
        # Covariance matrix
        H = src_centered.T @ tgt_centered
        
        # SVD
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T
        
        # Determinant kontrolü (reflection'u düzelt)
        if np.linalg.det(R) < 0:
            Vt[-1, :] *= -1
            R = Vt.T @ U.T
        
        # Translation
        t = tgt_center - R @ src_center
        
        # Pose2D'ye çevir
        theta = np.arctan2(R[1, 0], R[0, 0])
        return Pose2D(x_m=float(t[0]), y_m=float(t[1]), heading_rad=float(theta))

    def _apply_transform_2d(self, points: np.ndarray, transform: Pose2D) -> np.ndarray:
        """2D noktaları dönüştür."""
        c = np.cos(transform.heading_rad)
        s = np.sin(transform.heading_rad)
        R = np.array([[c, -s], [s, c]])
        t = np.array([transform.x_m, transform.y_m])
        return (R @ points.T).T + t


class ICP3D:
    """3D ICP - 3D nokta bulutu hizalama.
    
    3D LiDAR, depth kamera için. Kuaterniyon bazlı rotasyon.
    """

    def __init__(self, config: Optional[ICPConfig] = None) -> None:
        self.config = config or ICPConfig()

    def align(
        self,
        source: np.ndarray,
        target: np.ndarray,
        initial_guess: Optional[Pose3D] = None,
    ) -> Tuple[Pose3D, float, bool]:
        """3D nokta bulutu hizalama.
        
        Returns:
            transform: Bulunan dönüşüm
            fitness: Eşleşme kalitesi
            converged: Yakınsadı mı
        """
        if source.shape[0] < 3 or target.shape[0] < 3:
            return (
                Pose3D(position=np.zeros(3), quaternion=np.array([0, 0, 0, 1])),
                float('inf'),
                False,
            )
        
        # Initial transform
        if initial_guess is not None:
            T_init = initial_guess.to_matrix()
            ones = np.ones((source.shape[0], 1))
            homogeneous = np.hstack([source, ones])
            current_source = (T_init @ homogeneous.T).T[:, :3]
            cumulative_T = T_init
        else:
            current_source = source.copy()
            cumulative_T = np.eye(4)
        
        prev_error = float('inf')
        
        for iteration in range(self.config.max_iterations):
            # Find correspondences
            correspondences, distances = self._find_correspondences_3d(
                current_source, target
            )
            
            # Reject outliers
            valid_mask = distances < self.config.max_correspondence_distance
            if valid_mask.sum() < self.config.min_inliers:
                break
            
            n_keep = int(valid_mask.sum() * self.config.outlier_ratio)
            n_keep = max(n_keep, self.config.min_inliers)
            
            sorted_indices = np.argsort(distances[valid_mask])[:n_keep]
            valid_indices = np.where(valid_mask)[0][sorted_indices]
            
            src_matched = current_source[valid_indices]
            tgt_matched = target[correspondences[valid_indices]]
            
            # Compute transform
            delta_T = self._compute_transform_3d(src_matched, tgt_matched)
            
            # Apply transform
            ones = np.ones((current_source.shape[0], 1))
            homogeneous = np.hstack([current_source, ones])
            current_source = (delta_T @ homogeneous.T).T[:, :3]
            cumulative_T = delta_T @ cumulative_T
            
            # Check convergence
            mean_error = distances[valid_indices].mean()
            error_change = abs(prev_error - mean_error)
            
            if error_change < self.config.convergence_threshold:
                return Pose3D.from_matrix(cumulative_T), float(mean_error), True
            
            prev_error = mean_error
        
        # Did not converge
        correspondences, distances = self._find_correspondences_3d(current_source, target)
        valid_mask = distances < self.config.max_correspondence_distance
        fitness = float(distances[valid_mask].mean()) if valid_mask.sum() > 0 else float('inf')
        
        return Pose3D.from_matrix(cumulative_T), fitness, False

    def _find_correspondences_3d(
        self, source: np.ndarray, target: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """3D en yakın nokta eşleştirme."""
        n_source = source.shape[0]
        correspondences = np.zeros(n_source, dtype=int)
        distances = np.zeros(n_source)
        
        for i in range(n_source):
            dists = np.linalg.norm(target - source[i], axis=1)
            correspondences[i] = np.argmin(dists)
            distances[i] = dists[correspondences[i]]
        
        return correspondences, distances

    def _compute_transform_3d(
        self, source: np.ndarray, target: np.ndarray
    ) -> np.ndarray:
        """Optimal 3D rigid transform (4x4 matrix)."""
        # Merkezle
        src_center = source.mean(axis=0)
        tgt_center = target.mean(axis=0)
        
        src_centered = source - src_center
        tgt_centered = target - tgt_center
        
        # Covariance
        H = src_centered.T @ tgt_centered
        
        # SVD
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T
        
        # Reflection düzeltmesi
        if np.linalg.det(R) < 0:
            Vt[2, :] *= -1
            R = Vt.T @ U.T
        
        # Translation
        t = tgt_center - R @ src_center
        
        # 4x4 matrix
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = t
        return T
