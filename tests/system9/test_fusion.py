"""Sistem 9 — Sensör füzyonu testleri."""

import pytest

from ai.fusion import fuse, nearest_fused_hazard
from ai.object_detector import ObjectDetector

DETECTOR = ObjectDetector(confidence_threshold=0.0)


def _person_cluster():
    return [(0.0, 0.0, z) for z in [0.0, 0.3, 0.6, 0.9]] + [
        (0.1, 0.0, z) for z in [0.2, 0.5, 0.8]
    ]


def _vehicle_cluster():
    return [(x / 2.0 - 1.8, y / 2.0 - 1.8, 0.4) for x in range(8) for y in range(8)]


class TestFusionBasics:
    def test_daylight_bright_scene(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 2.0, 0.0)],
            thermal_clusters=[],
            rgb_brightness=[200, 220, 240],
            thermal_signal=[5.0, 6.0],
        )
        assert result.daylight_level > 0.5

    def test_night_dark_scene(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 2.0, 0.0)],
            thermal_clusters=[],
            rgb_brightness=[10, 15, 8],
            thermal_signal=[25.0],
        )
        assert result.daylight_level < 0.5

    def test_empty_everything(self):
        result = fuse(DETECTOR, [], [], [], [])
        assert result.fused == []
        assert result.daylight_level == 1.0

    def test_thermal_only_detection_kept(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[],
            thermal_clusters=[(_person_cluster(), 3.0, 0.0)],
            rgb_brightness=[20, 20],
            thermal_signal=[20.0],
        )
        assert len(result.thermal_detections) == 1
        assert result.fused and result.fused[0].kind == "insan"


class TestMerge:
    def test_matching_detection_merged(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 3.0, 0.0)],
            thermal_clusters=[(_person_cluster(), 3.2, 0.0)],
            rgb_brightness=[200],
            thermal_signal=[22.0],
        )
        assert len(result.fused) == 1
        merged = result.fused[0]
        assert merged.kind == "insan"
        assert merged.range_m == pytest.approx(3.1)

    def test_far_apart_detections_kept_separate(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 2.0, 0.0)],
            thermal_clusters=[(_vehicle_cluster(), 15.0, 0.0)],
            rgb_brightness=[200],
            thermal_signal=[10.0],
        )
        assert len(result.fused) == 2

    def test_fused_sorted_by_range(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[
                (_person_cluster(), 8.0, 0.0),
                (_person_cluster(), 1.5, 0.0),
            ],
            thermal_clusters=[(_person_cluster(), 20.0, 0.0)],
            rgb_brightness=[200],
            thermal_signal=[10.0],
        )
        ranges = [d.range_m for d in result.fused]
        assert ranges == sorted(ranges)

    def test_nearest_fused(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 2.0, 0.0)],
            thermal_clusters=[],
            rgb_brightness=[200],
            thermal_signal=[10.0],
        )
        nearest = nearest_fused_hazard(result)
        assert nearest is not None and nearest.kind == "insan"

    def test_summary_string(self):
        result = fuse(
            DETECTOR,
            rgb_clusters=[(_person_cluster(), 2.0, 0.0)],
            thermal_clusters=[],
            rgb_brightness=[200],
            thermal_signal=[10.0],
        )
        text = result.summary()
        assert "insan" in text and "m" in text

    def test_summary_empty(self):
        result = fuse(DETECTOR, [], [], [], [])
        assert result.summary() == "algı yok"

    @pytest.mark.parametrize("brightness", [0, 60, 130, 200, 255])
    def test_daylight_level_monotonic(self, brightness):
        result = fuse(
            DETECTOR,
            rgb_clusters=[],
            thermal_clusters=[],
            rgb_brightness=[brightness],
            thermal_signal=[10.0],
        )
        expected = brightness / 255.0
        assert result.daylight_level == pytest.approx(expected, abs=0.02)