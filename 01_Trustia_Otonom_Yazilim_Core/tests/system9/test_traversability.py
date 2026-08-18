"""Sistem 9 — Arazi sınıflandırma ve geçilebilirlik testleri."""

import pytest

from ai.features import Features
from ai.traversability import (
    TERRAIN_CLASSES,
    TRAVERSABILITY,
    TraversabilityCell,
    TraversabilityMap,
    cell_traversability,
    classify_cell,
    class_accuracy,
    cost_for,
)

CENTERS = {
    "asfalt": (0.05, 0.03, 0.85, 0.02),
    "cimen": (0.20, 0.12, 0.45, 0.15),
    "camur": (0.30, 0.25, 0.20, 0.30),
    "kaya": (0.55, 0.45, 0.35, 0.75),
    "cukur": (0.45, 0.35, 0.25, 0.60),
    "su": (0.10, 0.08, 0.05, 0.05),
}


@pytest.mark.parametrize("name", TERRAIN_CLASSES)
def test_center_classified_correctly(name):
    terrain, _ = classify_cell(Features(CENTERS[name]))
    assert terrain == name


@pytest.mark.parametrize("name", TERRAIN_CLASSES)
@pytest.mark.parametrize("sigma", [0.4, 0.8, 1.2])
def test_noise_robust_classification(name, sigma):
    center = CENTERS[name]
    noisy = tuple(c * sigma for c in center)
    terrain, _ = classify_cell(Features(noisy))
    assert terrain in TERRAIN_CLASSES


@pytest.mark.parametrize("name", ("asfalt", "cimen", "camur", "kaya", "cukur", "su"))
def test_class_accuracy_perfect_on_centers(name):
    assert class_accuracy([Features(CENTERS[name])], [name]) == 1.0


class TestTraversabilityScore:
    def test_scores_bounded(self):
        for name, score in TRAVERSABILITY.items():
            assert 0.0 <= score <= 1.0

    def test_ordering(self):
        order = ["asfalt", "cimen", "camur", "kaya", "cukur", "su"]
        values = [TRAVERSABILITY[name] for name in order]
        assert values == sorted(values, reverse=True)

    @pytest.mark.parametrize("name", TERRAIN_CLASSES)
    def test_cell_score_matches_table(self, name):
        assert cell_traversability(Features(CENTERS[name])) == pytest.approx(
            TRAVERSABILITY[name]
        )

    def test_su_impassable(self):
        assert TRAVERSABILITY["su"] == 0.0

    @pytest.mark.parametrize("name", ["asfalt", "cimen", "kaya"])
    def test_cost_inverse(self, name):
        expected = 1.0 / max(TRAVERSABILITY[name], 0.05)
        assert cost_for(Features(CENTERS[name])) == pytest.approx(min(50.0, expected))


class TestMap:
    def test_set_and_get(self):
        m = TraversabilityMap(4, 4)
        m.set_cell(1, 2, Features(CENTERS["cimen"]))
        cell = m.get(1, 2)
        assert cell.terrain == "cimen"
        assert cell.score == pytest.approx(0.8)

    def test_out_of_bounds_raises(self):
        m = TraversabilityMap(3, 3)
        with pytest.raises(IndexError):
            m.set_cell(5, 5, Features(CENTERS["cimen"]))

    def test_missing_cell_defaults_su(self):
        m = TraversabilityMap(4, 4)
        assert m.get(0, 0).terrain == "su"

    def test_neighbors_found(self):
        m = TraversabilityMap(5, 5)
        for dx, dy in [(1, 2), (2, 1), (3, 2), (2, 3)]:
            m.set_cell(dx, dy, Features(CENTERS["asfalt"]))
        neighbors = m.neighbors(2, 2)
        assert len(neighbors) == 4

    def test_corner_neighbors_bounded(self):
        m = TraversabilityMap(3, 3)
        assert len(m.neighbors(0, 0)) == 2

    @pytest.mark.parametrize("threshold", [0.0, 0.3, 0.5, 0.8, 1.0])
    def test_passable_threshold(self, threshold):
        assert TraversabilityCell(0, 0, 0.5, "cimen").passable(threshold) == (0.5 >= threshold)

    def test_profile_correct(self):
        cell = TraversabilityCell(1, 1, 0.8, "cimen")
        assert cell.cost == pytest.approx(1.0 / 0.8)

    def test_impassable_high_cost(self):
        assert TraversabilityCell(0, 0, 0.0, "su").cost == 50.0
    def test_scores_propagate_to_map(self):
        m = TraversabilityMap(3, 3)
        for x in range(3):
            for y in range(3):
                m.set_cell(x, y, Features(CENTERS["kaya"]))
        assert m.count_passable(0.3) == 0
        assert m.count_passable(0.2) == 9

    def test_cost_range(self):
        m = TraversabilityMap(4, 4)
        for name in TERRAIN_CLASSES:
            m.set_cell(0, 0, Features(CENTERS[name]))
            assert 1.0 <= m.get(0, 0).cost <= 50.0