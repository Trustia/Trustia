"""Sistem 9 — Nesne tanıma testleri."""

import pytest

from ai.features import Features
from ai.object_detector import (
    Detection,
    ObjectDetector,
    classify_object,
    cluster_accuracy,
)

VEHICLE = (0.62, 0.07, 0.05, 0.40)
PERSON = (0.12, 0.20, 0.45, 0.90)
UNKNOWN = (0.35, 0.15, 0.30, 0.60)


class TestClassify:
    @pytest.mark.parametrize("center,expected", [
        (VEHICLE, "araç"),
        (PERSON, "insan"),
        (UNKNOWN, "bilinmeyen engel"),
    ])
    def test_center_objects(self, center, expected):
        klass, dist = classify_object(Features(center))
        assert klass == expected
        assert dist >= 0.0

    @pytest.mark.parametrize("center,expected", [
        ((1, 1, 1, 1), "insan"),
        ((0, 0, 0, 0), "araç"),
    ])
    def test_extreme_features(self, center, expected):
        assert classify_object(Features(center))[0] == expected

    def test_short_vector_raises(self):
        with pytest.raises(ValueError):
            classify_object(Features((0, 0, 0)))

    @pytest.mark.parametrize("sigma", [0.3, 0.6, 0.9])
    def test_noise_keeps_valid_class(self, sigma):
        klass, _ = classify_object(Features(tuple(v * sigma for v in VEHICLE)))
        assert klass in ("araç", "bilinmeyen engel", "insan")

    @pytest.mark.parametrize("case", [
        ([VEHICLE, PERSON, UNKNOWN], ["araç", "insan", "bilinmeyen engel"]),
        ([PERSON, PERSON], ["insan", "insan"]),
    ])
    def test_cluster_accuracy(self, case):
        feats, expected = case
        wrapped = [Features(f) for f in feats]
        assert cluster_accuracy(wrapped, expected) == 1.0

    def test_cluster_accuracy_mismatch(self):
        assert cluster_accuracy([Features(VEHICLE)], ["insan"]) == 0.0


class TestDetector:
    def _vehicle_cluster(self):
        points = [(x / 2.0 - 1.8, y / 2.0 - 1.8, 0.4) for x in range(8) for y in range(8)]
        return points

    def _person_cluster(self):
        points = [(0.0, 0.0, z) for z in [0.0, 0.3, 0.6, 0.9]] + [
            (0.1, 0.0, z) for z in [0.2, 0.5, 0.8]
        ]
        return points

    def test_detect_vehicle(self):
        clusters = [(self._vehicle_cluster(), 4.0, 10.0)]
        detections = ObjectDetector().detect(clusters)
        assert detections and detections[0].kind == "araç"

    def test_detect_person(self):
        clusters = [(self._person_cluster(), 2.0, -15.0)]
        detections = ObjectDetector().detect(clusters)
        assert detections and detections[0].kind == "insan"

    def test_range_bearing_carried(self):
        clusters = [(self._person_cluster(), 3.5, 22.0)]
        det = ObjectDetector().detect(clusters)[0]
        assert det.range_m == 3.5
        assert det.bearing_deg == 22.0

    @pytest.mark.parametrize("threshold", [0.0, 0.4, 0.95])
    def test_threshold_filters(self, threshold):
        detector = ObjectDetector(confidence_threshold=threshold)
        hits = detector.detect([(self._person_cluster(), 2.0, 0.0)])
        if threshold >= 0.95:
            assert hits == []
        else:
            assert all(d.confidence >= threshold for d in hits)

    def test_empty_clusters(self):
        assert ObjectDetector().detect([]) == []

    def test_confidence_bounded(self):
        det = ObjectDetector(confidence_threshold=0.0).detect(
            [(self._vehicle_cluster(), 3.0, 0.0)]
        )
        assert all(0.0 <= d.confidence <= 1.0 for d in det)

    def test_nearest_hazard(self):
        detector = ObjectDetector()
        clusters = [
            (self._person_cluster(), 8.0, 0.0),
            (self._person_cluster(), 2.0, 0.0),
        ]
        nearest = detector.nearest_hazard(clusters)
        assert nearest is not None and nearest.range_m == 2.0

    def test_nearest_hazard_none(self):
        assert ObjectDetector().nearest_hazard([]) is None

    def test_detection_to_dict(self):
        det = Detection("insan", 0.9, 2.34, 12.5, 0.4)
        data = det.to_dict()
        assert data["kind"] == "insan"
        assert data["confidence"] == 0.9
        assert data["range_m"] == 2.34
        assert data["bearing_deg"] == 12.5