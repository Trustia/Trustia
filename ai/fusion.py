"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Sensör füzyonu.

Gündüz/gece kamera + termal + LiDAR bilgisini birleştirip tek
güvenilir algı çıktısı üretir. PLAN 3.3 Katman 2:
"sensör füzyonu: gündüz/gece kamera birleştirme".
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence

from ai.object_detector import Detection, ObjectDetector


@dataclass
class FusionResult:
    """Birleştirilmiş algı çıktısı."""

    daylight_level: float          # 1 = gündüz, 0 = gece
    rgb_detections: List[Detection]
    thermal_detections: List[Detection]
    fused: List[Detection]

    def summary(self) -> str:
        if not self.fused:
            return "algı yok"
        primary = self.fused[0]
        return (
            f"{primary.kind} @ {primary.range_m:.1f} m "
            f"(güven %{primary.confidence * 100:.0f}) +{len(self.fused) - 1} hedef"
        )


def _merge_by_range(
    rgb: Sequence[Detection], thermal: Sequence[Detection], rgb_weight: float
) -> List[Detection]:
    merged: List[Detection] = []
    used_thermal: set = set()
    for d in rgb:
        best_i, best_delta = None, float("inf")
        for i, t in enumerate(thermal):
            delta = abs(t.range_m - d.range_m)
            if delta < best_delta:
                best_i, best_delta = i, delta
        if best_i is not None and best_delta <= 2.0:
            t = thermal[best_i]
            used_thermal.add(best_i)
            if t.kind == d.kind:
                confidence = max(d.confidence, t.confidence)
            else:
                confidence = (
                    d.confidence * rgb_weight + t.confidence * (1.0 - rgb_weight)
                )
            merged.append(
                Detection(
                    kind=d.kind,
                    confidence=confidence,
                    range_m=(d.range_m + t.range_m) / 2.0,
                    bearing_deg=d.bearing_deg,
                    size_m=max(d.size_m, t.size_m),
                )
            )
        else:
            merged.append(d)
    for i, t in enumerate(thermal):
        if i not in used_thermal:
            merged.append(t)
    merged.sort(key=lambda d: d.range_m)
    return merged


def fuse(
    detector: ObjectDetector,
    rgb_clusters: Sequence,
    thermal_clusters: Sequence,
    rgb_brightness: Sequence[float],
    thermal_signal: Sequence[float],
) -> FusionResult:
    """RGB + termal tespitleri tek listede birleştirir.

    Gece (parlaklık düşük) ise termal tespit ağırlık kazanır.
    """
    if not rgb_brightness and not thermal_signal:
        daylight_ratio = 1.0
    else:
        mean_bright = sum(rgb_brightness) / max(1, len(rgb_brightness))
        daylight_ratio = min(1.0, max(0.0, mean_bright / 255.0))
    rgb_detections = detector.detect(rgb_clusters)
    thermal_detections = detector.detect(thermal_clusters)
    rgb_weight = 0.85 * daylight_ratio + 0.10
    fused = _merge_by_range(rgb_detections, thermal_detections, rgb_weight)
    return FusionResult(
        daylight_level=daylight_ratio,
        rgb_detections=rgb_detections,
        thermal_detections=thermal_detections,
        fused=fused,
    )


def nearest_fused_hazard(result: FusionResult) -> Optional[Detection]:
    return result.fused[0] if result.fused else None