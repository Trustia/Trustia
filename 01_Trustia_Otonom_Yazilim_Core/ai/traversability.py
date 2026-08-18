"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Arazi sınıflandırma ve
geçilebilirlik analizi.

Öznitelik vektörlerini arazi sınıfına eşler (kaya, çukur, çamur,
çimen, su, asfalt) ve geçilebilirlik skoru üretir. PLAN 3.3 Katman 1:
"arazi sınıflandırma (kaya, çukur, çamur, çimen, su)" ve Katman 2:
"geçilebilirlik (traversability) analizi".
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

from ai.features import Features

TERRAIN_CLASSES: Tuple[str, ...] = ("asfalt", "cimen", "camur", "kaya", "cukur", "su")

# Sınıf başına geçilebilirlik (0 = geçilmez, 1 = ideal)
TRAVERSABILITY: Dict[str, float] = {
    "asfalt": 1.00,
    "cimen": 0.80,
    "camur": 0.45,
    "kaya": 0.25,
    "cukur": 0.15,
    "su": 0.00,
}

# Sınıf merkezleri (eğim, pürüzlülük, yansıma, düşey zenginlik)
_CENTERS: Dict[str, Tuple[float, float, float, float]] = {
    "asfalt": (0.05, 0.03, 0.85, 0.02),
    "cimen": (0.20, 0.12, 0.45, 0.15),
    "camur": (0.30, 0.25, 0.20, 0.30),
    "kaya": (0.55, 0.45, 0.35, 0.75),
    "cukur": (0.45, 0.35, 0.25, 0.60),
    "su": (0.10, 0.08, 0.05, 0.05),
}


def classify_cell(features: Features) -> Tuple[str, float]:
    """Hücre özniteliklerinden (sınıf, en yakın merkez mesafesi)."""
    if features.dim() < 4:
        raise ValueError("arazi sınıflandırması en az 4 öznitelik ister")
    best_class, best_dist = "asfalt", float("inf")
    for name, center in _CENTERS.items():
        dist = sum((v - c) ** 2 for v, c in zip(features.as_list(), center))
        if dist < best_dist:
            best_class, best_dist = name, dist
    return best_class, best_dist


def cell_traversability(features: Features) -> float:
    """Hücre geçilebilirlik skoru 0-1."""
    terrain_class, _ = classify_cell(features)
    return TRAVERSABILITY[terrain_class]


def cost_for(features: Features) -> float:
    """Planlama maliyeti = 1/geçilebilirlik (aşırı büyük değer yok)."""
    score = cell_traversability(features)
    return min(50.0, 1.0 / max(score, 0.05))


def class_accuracy(
    features_list: Sequence[Features],
    expected: Sequence[str],
) -> float:
    """Sınıflandırma doğruluğu."""
    correct = sum(
        1 for f, e in zip(features_list, expected) if classify_cell(f)[0] == e
    )
    return correct / max(1, len(expected))


@dataclass
class TraversabilityCell:
    """Tek ızgara hücresi."""

    x: int
    y: int
    score: float
    terrain: str

    @property
    def cost(self) -> float:
        return min(50.0, 1.0 / max(self.score, 0.02))

    def passable(self, threshold: float = 0.3) -> bool:
        return self.score >= threshold


class TraversabilityMap:
    """Geçilebilirlik ızgara haritası (planlamaya maliyet sunar)."""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._cells: Dict[Tuple[int, int], TraversabilityCell] = {}

    def set_cell(
        self, x: int, y: int, features: Features
    ) -> TraversabilityCell:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("hücre ızgaranın dışında")
        terrain, _ = classify_cell(features)
        score = TRAVERSABILITY[terrain]
        cell = TraversabilityCell(x, y, score, terrain)
        self._cells[(x, y)] = cell
        return cell

    def get(self, x: int, y: int) -> TraversabilityCell:
        try:
            return self._cells[(x, y)]
        except KeyError:
            return TraversabilityCell(x, y, 0.0, "su")

    def neighbors(self, x: int, y: int) -> List[TraversabilityCell]:
        cells: List[TraversabilityCell] = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                cells.append(self.get(nx, ny))
        return cells

    def count_passable(self, threshold: float = 0.3) -> int:
        return sum(1 for c in self._cells.values() if c.passable(threshold))