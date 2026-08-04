"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Nesne tanıma.

LiDAR küme şekli ve kamera termal/renk sinyallerinden nesne sınıfı
tahmini: araç, insan, bilinmeyen engel. PLAN 3.3 Katman 1:
"nesne tanıma (insan, araç)".
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from ai.features import Features, cluster_shape

OBJECT_CLASSES: Tuple[str, ...] = ("araç", "insan", "bilinmeyen engel")

# Küme şekli öznitelik merkezleri: (boyut, yoğunluk, düşey oran, maks z)
# Ölçümlü küme örnekleriyle hizalanmıştır: araç geniş-yassı, insan
# dar-dik, bilinmeyen orta.
_VEHICLE_CENTER = (0.62, 0.07, 0.05, 0.40)
_PERSON_CENTER = (0.12, 0.20, 0.45, 0.90)
_UNKNOWN_CENTER = (0.35, 0.15, 0.30, 0.60)


def classify_object(shape: Features) -> Tuple[str, float]:
    """Küme şeklinden (sınıf, en yakın merkez mesafesi)."""
    if shape.dim() < 4:
        raise ValueError("nesne tanıma en az 4 öznitelik ister")
    candidates = (
        ("araç", _VEHICLE_CENTER),
        ("insan", _PERSON_CENTER),
        ("bilinmeyen engel", _UNKNOWN_CENTER),
    )
    best, best_dist = candidates[0], float("inf")
    for name, center in candidates:
        dist = sum((v - c) ** 2 for v, c in zip(shape.as_list(), center))
        if dist < best_dist:
            best, best_dist = name, dist
    return best, best_dist


@dataclass
class Detection:
    """Tek nesne tespiti."""

    kind: str
    confidence: float
    range_m: float
    bearing_deg: float
    size_m: float

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "confidence": round(self.confidence, 3),
            "range_m": round(self.range_m, 2),
            "bearing_deg": round(self.bearing_deg, 1),
            "size_m": round(self.size_m, 2),
        }


class ObjectDetector:
    """Küme listesinden nesne tespiti (eşik + merkez mesafesi)."""

    def __init__(self, confidence_threshold: float = 0.35) -> None:
        self.confidence_threshold = confidence_threshold

    @staticmethod
    def _confidence(dist: float) -> float:
        return max(0.0, min(1.0, 1.0 - dist / 1.2))

    def detect(
        self,
        clusters: Sequence[Tuple[List[Tuple[float, float, float]], float, float]],
    ) -> List[Detection]:
        """`clusters`: (noktalar, menzil_m, kerteriz_derece) demetleri."""
        detections: List[Detection] = []
        for points, range_m, bearing_deg in clusters:
            shape = cluster_shape(points)
            kind, dist = classify_object(shape)
            confidence = self._confidence(dist)
            if confidence >= self.confidence_threshold:
                detections.append(
                    Detection(
                        kind=kind,
                        confidence=confidence,
                        range_m=range_m,
                        bearing_deg=bearing_deg,
                        size_m=math.sqrt(sum((v - 0.0) ** 2 for v in shape.as_list()[:2])),
                    )
                )
        return detections

    def nearest_hazard(self, clusters: Sequence) -> Optional[Detection]:
        detections = self.detect(clusters)
        if not detections:
            return None
        return min(detections, key=lambda d: d.range_m)


def cluster_accuracy(
    shape_features: Sequence[Features],
    expected: Sequence[str],
) -> float:
    correct = sum(
        1 for f, e in zip(shape_features, expected) if classify_object(f)[0] == e
    )
    return correct / max(1, len(expected))