"""
TRUSTIA SLAM - Odometry entegrasyonu.

Odometry (ölü hesaplama) ölçümlerini birleştirerek robot
pozisyonunu tahmin eder. Wheel odometry, visual odometry, IMU.

Hata birikir → ICP/loop closure ile düzeltilmeli!
"""

from __future__ import annotations

from typing import List, Optional

import numpy as np

from slam.types import Pose2D, OdometryMeasurement


class OdometryIntegrator:
    """Odometry ölçümlerini birleştirip pose tahmini yapar.
    
    Basit forward kinematics: Her ölçüm göreli hareket verir,
    global pose'a eklenir. Hata zamanla birikir (drift).
    
    Kullanım:
        integrator = OdometryIntegrator(initial_pose)
        integrator.update(measurement)
        current_pose = integrator.pose
    """

    def __init__(self, initial_pose: Optional[Pose2D] = None) -> None:
        if initial_pose is None:
            initial_pose = Pose2D(0.0, 0.0, 0.0)
        self._pose = initial_pose
        self._measurements: List[OdometryMeasurement] = []
        self._poses: List[Pose2D] = [initial_pose]
        self._total_distance = 0.0

    @property
    def pose(self) -> Pose2D:
        """Güncel pose tahmini."""
        return self._pose

    @property
    def total_distance(self) -> float:
        """Toplam kat edilen mesafe."""
        return self._total_distance

    @property
    def total_distance_m(self) -> float:
        """Toplam kat edilen mesafe (metre)."""
        return self._total_distance

    @property
    def trajectory(self) -> List[Pose2D]:
        """Tüm pose geçmişi."""
        return list(self._poses)

    def update(self, measurement: OdometryMeasurement) -> Pose2D:
        """Yeni ölçümle pose'u güncelle.
        
        Kinematik model:
            x' = x + d * cos(θ + dθ/2)
            y' = y + d * sin(θ + dθ/2)
            θ' = θ + dθ
        
        Mid-point integration: dönüş ortasındaki açıyı kullan.
        """
        d = measurement.delta_distance_m
        if d < 0:
            from core.errors import SensorError
            raise SensorError("Negative odometry distance is rejected.")
        dtheta = measurement.delta_heading_rad
        
        # Mid-point heading
        mid_heading = self._pose.heading_rad + dtheta / 2.0
        
        # Position update
        dx = d * np.cos(mid_heading)
        dy = d * np.sin(mid_heading)
        
        new_pose = Pose2D(
            x_m=self._pose.x_m + dx,
            y_m=self._pose.y_m + dy,
            heading_rad=self._pose.heading_rad + dtheta,
        )
        
        # Normalize heading [-π, π]
        while new_pose.heading_rad > np.pi:
            new_pose = Pose2D(
                new_pose.x_m,
                new_pose.y_m,
                new_pose.heading_rad - 2 * np.pi,
            )
        while new_pose.heading_rad < -np.pi:
            new_pose = Pose2D(
                new_pose.x_m,
                new_pose.y_m,
                new_pose.heading_rad + 2 * np.pi,
            )
        
        self._pose = new_pose
        self._measurements.append(measurement)
        self._poses.append(new_pose)
        self._total_distance += abs(d)
        
        return new_pose

    def reset(self, pose: Optional[Pose2D] = None) -> None:
        """Pose'u sıfırla (örn. loop closure sonrası veya orijine dön)."""
        if pose is None:
            pose = Pose2D(0.0, 0.0, 0.0)
        self._pose = pose
        self._poses = [pose]
        self._total_distance = 0.0

    def set_pose(self, pose: Pose2D) -> None:
        """Pose'u ayarla."""
        self._pose = pose
        self._poses.append(pose)

    def correction(self, corrected_pose: Pose2D) -> None:
        """Manuel düzeltme (ICP/GPS/loop closure)."""
        self._pose = corrected_pose
        self._poses.append(corrected_pose)


class WheelOdometry:
    """Wheel encoder bazlı odometry.
    
    İki teker encoder'ından diferansiyel drive kinematiği.
    
    Parametreler:
        wheel_base: Tekerler arası mesafe (metre)
        wheel_radius: Teker yarıçapı (metre)
    """

    def __init__(self, wheel_base: float, wheel_radius: float) -> None:
        if wheel_base <= 0.0 or wheel_radius <= 0.0:
            raise ValueError("wheel_base ve wheel_radius pozitif olmalı")
        
        self.wheel_base = wheel_base
        self.wheel_radius = wheel_radius
        self._prev_left_ticks: Optional[int] = None
        self._prev_right_ticks: Optional[int] = None

    def compute_measurement(
        self,
        left_ticks: int,
        right_ticks: int,
        ticks_per_revolution: int,
    ) -> Optional[OdometryMeasurement]:
        """Encoder tick'lerinden odometry ölçümü.
        
        Args:
            left_ticks: Sol teker encoder sayacı
            right_ticks: Sağ teker encoder sayacı
            ticks_per_revolution: Devir başına tick
        
        Returns:
            OdometryMeasurement (ilk çağrıda None)
        """
        if self._prev_left_ticks is None:
            self._prev_left_ticks = left_ticks
            self._prev_right_ticks = right_ticks
            return None
        
        # Tick farkları
        d_left_ticks = left_ticks - self._prev_left_ticks
        d_right_ticks = right_ticks - self._prev_right_ticks
        
        self._prev_left_ticks = left_ticks
        self._prev_right_ticks = right_ticks
        
        # Tick → mesafe
        meters_per_tick = (2.0 * np.pi * self.wheel_radius) / ticks_per_revolution
        d_left = d_left_ticks * meters_per_tick
        d_right = d_right_ticks * meters_per_tick
        
        # Diferansiyel kinematik
        d_center = (d_left + d_right) / 2.0
        d_heading = (d_right - d_left) / self.wheel_base
        
        return OdometryMeasurement(
            delta_distance_m=d_center,
            delta_heading_rad=d_heading,
        )


class VisualOdometry:
    """Visual odometry (kamera bazlı).
    
    Bu basitleştirilmiş placeholder - gerçek implementasyon
    OpenCV opticalFlow veya feature matching gerektirir.
    """

    def __init__(self) -> None:
        self._prev_features: Optional[np.ndarray] = None

    def compute_measurement(
        self,
        image: np.ndarray,
        camera_matrix: np.ndarray,
    ) -> Optional[OdometryMeasurement]:
        """Ardışık görüntülerden hareket tahmini.
        
        Basitleştirilmiş - gerçek implementasyon:
          1. Feature detection (ORB/SIFT)
          2. Feature matching
          3. Essential matrix estimation
          4. Pose recovery
        """
        # Placeholder
        return OdometryMeasurement(
            delta_distance_m=0.0,
            delta_heading_rad=0.0,
        )
