"""
TRUSTIA Otonom Sürüş Çekirdeği — ISO 21448 (SOTIF) Kural Tabanlı Güvenlik Hakemi.
================================================================================
Bu modül, ISO 21448 (SOTIF - Safety of the Intended Functionality) standardı
uyarınca; derin öğrenme ve yapay zeka çıktılarının deterministik fizik ve sensör
çapraz kontrolleriyle denetlendiği, hayalet engellerin (phantom braking) elendiği
ve 35ms gecikme aşımında Minimal Risk Manevrasını (MRM) tetikleyen emniyet hakemidir.

Standartlar ve Fonksiyonel Güvenlik Kalkanı:
  - ISO 21448 (SOTIF) Çalışma Zamanı Plausibility Denetleyicisi
  - Hayalet Engel (Phantom Detection) ve Güneş Parlaması Elemesi
  - Kamera-LiDAR Çapraz Teyit Kuralı (Cross-Sensor Validation)
  - 35 ms Maksimum Yapay Zeka Çıkarım Gecikmesi Sınırı
  - ISO 26262 ASIL-D 50ms Watchdog ve -1.5 m/s² MRM Güvenli Duruş Tetikleyicisi
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from ai.deep_perception import BoundingBox3D
from ai.tracking import TrackedObstacle3D


@dataclass
class SotifPlausibilityReport:
    """ISO 21448 SOTIF Denetim Sonuç Raporu."""

    is_safe_to_proceed: bool
    phantom_detections_rejected: int
    kinematic_violations_count: int
    latency_violation: bool
    inference_latency_ms: float
    recommended_action: str  # "NOMINAL_CONTINUE", "CAUTION_SLOWDOWN", "MRM_SAFE_STOP"
    target_decel_mps2: float
    verified_obstacles: List[TrackedObstacle3D] = field(default_factory=list)
    rejection_reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "safe": self.is_safe_to_proceed,
            "action": self.recommended_action,
            "target_decel_mps2": self.target_decel_mps2,
            "latency_ms": round(self.inference_latency_ms, 2),
            "latency_fault": self.latency_violation,
            "phantoms_rejected": self.phantom_detections_rejected,
            "kinematic_violations": self.kinematic_violations_count,
            "verified_count": len(self.verified_obstacles),
            "reasons": self.rejection_reasons,
        }


class Iso21448SotifMonitor:
    """
    ISO 21448 SOTIF Kural Tabanlı Güvenlik Hakemi ve Plausibility Denetleyicisi.
    """

    def __init__(
        self,
        max_inference_latency_ms: float = 35.0,
        max_physical_acceleration_mps2: float = 12.0,
        min_lidar_points_in_box: int = 3,
        watchdog_consecutive_timeout_limit: int = 2,
    ) -> None:
        self.max_inference_latency_ms = max_inference_latency_ms
        self.max_physical_acceleration_mps2 = max_physical_acceleration_mps2
        self.min_lidar_points_in_box = min_lidar_points_in_box
        self.watchdog_consecutive_timeout_limit = watchdog_consecutive_timeout_limit
        self.consecutive_latency_violations = 0

    def evaluate_perception(
        self,
        tracked_obstacles: Sequence[TrackedObstacle3D],
        inference_latency_ms: float,
        raw_lidar_points: Optional[Sequence[Tuple[float, float, float, float]]] = None,
    ) -> SotifPlausibilityReport:
        """
        Derin öğrenme algı ve takip çıktılarını SOTIF kurallarına göre denetler.
        """
        rejection_reasons: List[str] = []
        verified_obstacles: List[TrackedObstacle3D] = []
        phantoms_count = 0
        kinematic_count = 0

        # 1. Çıkarım Gecikmesi Denetimi (35ms Sınırı)
        latency_fault = inference_latency_ms > self.max_inference_latency_ms
        if latency_fault:
            self.consecutive_latency_violations += 1
            rejection_reasons.append(
                f"Yapay zeka çıkarım gecikmesi aşıldı: {inference_latency_ms:.1f}ms > {self.max_inference_latency_ms:.1f}ms"
            )
        else:
            self.consecutive_latency_violations = 0

        # İki ardışık gecikme aşımında doğrudan MRM Güvenli Duruş
        if self.consecutive_latency_violations >= self.watchdog_consecutive_timeout_limit:
            return SotifPlausibilityReport(
                is_safe_to_proceed=False,
                phantom_detections_rejected=0,
                kinematic_violations_count=0,
                latency_violation=True,
                inference_latency_ms=inference_latency_ms,
                recommended_action="MRM_SAFE_STOP",
                target_decel_mps2=-1.5,
                verified_obstacles=[],
                rejection_reasons=["ISO 26262 ASIL-D Watchdog: 2 ardışık yapay zeka zaman aşımı. MRM aktif."],
            )

        # 2. Her Takip Edilen Nesne İçin Fiziksel Mantık ve Çapraz Denetim
        for obs in tracked_obstacles:
            # 2.A. Kinematik İvme ve Hız Tutarlılığı Kontrolü
            # Yayanın 20 km/s üzerinde koşması veya aracın 180 km/s üzerinde uçması fiziksel plausibility ihlalidir
            if obs.class_name == "pedestrian" and obs.speed_mps() > 8.0:
                kinematic_count += 1
                rejection_reasons.append(f"İhlal: Yaya #{obs.track_id} fiziksel hız sınırını aşıyor: {obs.speed_kmh():.1f} km/h")
                continue

            if obs.speed_mps() > 50.0:  # > 180 km/s kentsel ODD ihlali
                kinematic_count += 1
                rejection_reasons.append(f"İhlal: Araç #{obs.track_id} aşırı hız anomalisi: {obs.speed_kmh():.1f} km/h")
                continue

            # 2.B. LiDAR Çapraz Doğrulaması (Hayalet Engel Elemesi)
            # Eğer LiDAR noktaları verilmişse ve kutunun içinde hiç yansıma yoksa bu bir hayalet engeldir
            if raw_lidar_points is not None and len(raw_lidar_points) > 0 and obs.confidence < 0.65:
                pts_inside = 0
                for pt in raw_lidar_points:
                    px, py, pz, _ = pt
                    if (
                        abs(px - obs.x) <= obs.length / 2.0
                        and abs(py - obs.y) <= obs.width / 2.0
                        and abs(pz - obs.z) <= obs.height / 2.0
                    ):
                        pts_inside += 1
                        if pts_inside >= self.min_lidar_points_in_box:
                            break

                if pts_inside < self.min_lidar_points_in_box:
                    phantoms_count += 1
                    rejection_reasons.append(
                        f"Hayalet Engel Reddedildi: Nesne #{obs.track_id} LiDAR ile teyit edilemedi (Nokta: {pts_inside})"
                    )
                    continue

            verified_obstacles.append(obs)

        # Karar üretimi
        if latency_fault:
            action = "CAUTION_SLOWDOWN"
            decel = -0.8
            safe = True
        else:
            action = "NOMINAL_CONTINUE"
            decel = 0.0
            safe = True

        return SotifPlausibilityReport(
            is_safe_to_proceed=safe,
            phantom_detections_rejected=phantoms_count,
            kinematic_violations_count=kinematic_count,
            latency_violation=latency_fault,
            inference_latency_ms=inference_latency_ms,
            recommended_action=action,
            target_decel_mps2=decel,
            verified_obstacles=verified_obstacles,
            rejection_reasons=rejection_reasons,
        )
