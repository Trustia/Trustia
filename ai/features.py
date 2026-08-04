"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Öznitelik çıkarma.

LiDAR nokta bulutları ve arazi hücrelerinden sınıflandırıcıya girdi
olan öznitelik vektörleri üretilir (arazi sınıflandırma + nesne
tanıma için ortak çatı). PLAN 3.2: "arazi sınıflandırma, nesne tanıma".
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from statistics import mean, pstdev
from typing import Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class Features:
    """Sınıflandırıcı girdisi — normalize edilmiş öznitelik vektörü."""

    values: Tuple[float, ...]

    def as_list(self) -> List[float]:
        return list(self.values)

    def dim(self) -> int:
        return len(self.values)


def _safe_mean(values: Sequence[float]) -> float:
    return mean(values) if values else 0.0


def _safe_std(values: Sequence[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def lidar_features(
    ranges: Sequence[float],
    intensities: Sequence[float] = (),
) -> Features:
    """Döner LiDAR taramasından öznitelik vektörü.

    Boyutlar: [ortalama menzil, menzil varyansı, dikey örtü, ortalama
    yansıma, minimum menzil, komşuluk sıçraması (türbülans)]. Değerler
    0-1 aralığına kaba ölçeklenir.
    """
    finite = [r for r in ranges if math.isfinite(r)]
    coverage = len(finite) / max(1, len(ranges))
    mean_range = _safe_mean(finite) if finite else 0.0
    std_range = _safe_std(finite)
    inten = list(intensities)
    mean_intensity = (_safe_mean(inten) if inten else 0.0) / 255.0
    min_range = min(finite) if finite else 0.0
    jumps = 0.0
    if len(finite) > 1:
        deltas = [abs(finite[i] - finite[i - 1]) for i in range(1, len(finite))]
        jumps = min(1.0, _safe_mean(deltas) / 10.0)
    return Features((
        min(1.0, mean_range / 30.0),
        min(1.0, std_range / 10.0),
        coverage,
        mean_intensity,
        min(1.0, min_range / 5.0),
        jumps,
    ))


def terrain_cell(
    elevation_samples: Sequence[float],
    width_m: float = 1.0,
) -> Features:
    """Arazi hücresi yükselti örneklerinden eğim/pürüzlülük öznitelikleri.

    Arşlar: [eğim (dikey aralık genişliğe bölünür), yükselti standart
    sapması, normalize ortalama yükselti, normalize yükselti zenginliği].
    """
    if not elevation_samples:
        return Features((0.0, 0.0, 0.0, 0.0))
    max_e = max(elevation_samples)
    min_e = min(elevation_samples)
    slope = (max_e - min_e) / max(0.1, width_m)
    return Features((
        min(1.0, slope / 2.0),
        min(1.0, _safe_std(elevation_samples) / 1.5),
        min(1.0, _safe_mean(elevation_samples) / 5.0),
        max(0.0, min(1.0, (max_e - min_e) / 2.0)),
    ))


def cluster_shape(
    points: Sequence[Tuple[float, float, float]],
) -> Features:
    """Nokta kümesi varlık şeklinden boyut/yoğunluk öznitelikleri.

    Küme merkezine göre yayılım (genişlik) ve nokta/alan yoğunluğu
    nesne tanıma için kullanılır."""
    if not points:
        return Features((0.0, 0.0, 0.0, 0.0))
    n = len(points)
    cx = mean(p[0] for p in points)
    cy = mean(p[1] for p in points)
    cz = mean(p[2] for p in points)
    radius = max(
        math.dist((p[0], p[1], p[2]), (cx, cy, cz)) for p in points
    )
    area = math.pi * radius * radius if radius > 0 else 1.0
    density = n / area if area > 0 else 0.0
    size = radius
    vertical_ratio = _vertical_ratio(points)
    return Features((
        min(1.0, size / 4.0),
        min(1.0, density / 50.0),
        vertical_ratio,
        min(1.0, max(p[2] for p in points) if points else 0.0),
    ))


def _vertical_ratio(points: Sequence[Tuple[float, float, float]]) -> float:
    if len(points) < 2:
        return 0.0
    z_std = pstdev(p[2] for p in points)
    return min(1.0, z_std / 2.0)


def thermal_signal(values: Sequence[float]) -> float:
    """Termal kamera ortalama sıcaklık sinyali 0-1."""
    if not values:
        return 0.0
    return min(1.0, max(0.0, (_safe_mean(values)) / 30.0))


def pixel_darkness(values: Sequence[float]) -> float:
    """Gece/Gündüz belirtisi: ortalama parlaklık düşükse gece."""
    if not values:
        return 0.0
    return 1.0 - min(1.0, _safe_mean(values) / 255.0)