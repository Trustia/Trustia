"""Sistem 9 — Öznitelik çıkarma birim testleri."""

import pytest

from ai.features import (
    Features,
    cluster_shape,
    lidar_features,
    pixel_darkness,
    terrain_cell,
    thermal_signal,
)


class TestLidarFeatures:
    def test_empty_scan(self):
        f = lidar_features([])
        assert f.dim() == 6
        assert f.as_list() == [0.0] * 6

    def test_single_beam(self):
        f = lidar_features([10.0])
        assert f.as_list()[0] == pytest.approx(10.0 / 30.0)

    def test_uniform_range_std_zero(self):
        f = lidar_features([5.0] * 10)
        assert f.as_list()[1] == 0.0

    @pytest.mark.parametrize("range_m", [1.0, 5.0, 15.0, 29.0])
    def test_mean_scale(self, range_m):
        f = lidar_features([range_m] * 8)
        assert f.as_list()[0] == pytest.approx(min(1.0, range_m / 30.0), abs=1e-6)

    def test_infinite_values_dropped(self):
        f = lidar_features([float("inf"), float("nan"), 6.0])
        assert f.as_list()[0] == pytest.approx(6.0 / 30.0)

    @pytest.mark.parametrize("frac", [0.0, 0.25, 0.5, 1.0])
    def test_coverage_fraction(self, frac):
        ranges = [5.0] * 8 + [float("inf")] * 4
        keep = int(frac * len(ranges))
        f = lidar_features(ranges[:keep] + [float("inf")] * (len(ranges) - keep))
        assert 0.0 <= f.as_list()[2] <= 1.0

    def test_intensity_scaled_to_unit(self):
        f = lidar_features([5.0] * 3, [200, 200, 200])
        assert f.as_list()[3] == pytest.approx(200 / 255)

    def test_rough_scan_has_jumps(self):
        smooth = lidar_features([5.0] * 20)
        rough = lidar_features([5.0 if i % 2 == 0 else 9.0 for i in range(20)])
        assert rough.as_list()[5] > smooth.as_list()[5]


class TestTerrainCell:
    def test_empty_cell(self):
        assert terrain_cell([]).as_list() == [0.0] * 4

    def test_flat_cell_zero_slope(self):
        f = terrain_cell([2.0] * 10)
        assert f.as_list()[0] == 0.0
        assert f.as_list()[1] == 0.0

    @pytest.mark.parametrize("height_range", [0.5, 1.0, 2.0])
    def test_slope_grows_with_height_range(self, height_range):
        f = terrain_cell([0.0, height_range])
        assert f.as_list()[0] == pytest.approx(min(1.0, height_range / 2.0))

    def test_rough_cell_has_variance(self):
        f = terrain_cell([1.0, 1.1, 1.05, 0.9, 1.2])
        assert f.as_list()[1] > 0.0

    def test_mean_normalized(self):
        f = terrain_cell([4.0] * 5)
        assert f.as_list()[2] == pytest.approx(4.0 / 5.0)

    @pytest.mark.parametrize("width", [0.5, 1.0, 2.0])
    def test_width_scales_slope(self, width):
        f = terrain_cell([0.0, 1.0], width_m=width)
        assert f.as_list()[0] == pytest.approx(min(1.0, 1.0 / width / 2.0))


class TestClusterShape:
    def test_empty_cluster(self):
        assert cluster_shape([]).as_list() == [0.0] * 4

    def test_single_point(self):
        f = cluster_shape([(1.0, 0.0, 0.0)])
        assert f.as_list()[0] == 0.0

    def test_wide_flat_cluster_small_vertical_ratio(self):
        points = [(x, y, 0.1) for x in range(4) for y in range(4)]
        f = cluster_shape(points)
        assert f.as_list()[2] < 0.3

    def test_tall_cluster_large_vertical_ratio(self):
        points = [(0.0, 0.0, z) for z in [0.0, 0.5, 1.0, 1.5]]
        f = cluster_shape(points)
        assert f.as_list()[2] > 0.2

    def test_bigger_radius_bigger_size_feature(self):
        small = cluster_shape([(0.0, 0.0, 0.0), (0.2, 0.0, 0.0)])
        big = cluster_shape([(0.0, 0.0, 0.0), (2.0, 0.0, 0.0)])
        assert big.as_list()[0] > small.as_list()[0]

    def test_dense_cluster_high_density(self):
        dense = cluster_shape([(0.0, 0.0, 0.0)] * 50)
        assert dense.as_list()[1] > 0.0


class TestThermalAndDarkness:
    @pytest.mark.parametrize("mean_c", [0, 5, 15, 29])
    def test_thermal_scaled(self, mean_c):
        assert thermal_signal([mean_c]) == pytest.approx(mean_c / 30.0)

    def test_thermal_empty(self):
        assert thermal_signal([]) == 0.0

    @pytest.mark.parametrize("brightness", [0, 50, 200, 255])
    def test_darkness_inverse(self, brightness):
        assert pixel_darkness([brightness]) == pytest.approx(1.0 - brightness / 255.0)

    def test_darkness_empty(self):
        assert pixel_darkness([]) == 0.0

    def test_darkness_bounded(self):
        assert 0.0 <= pixel_darkness([10, 20, 30]) <= 1.0


class TestFeaturesDataclass:
    def test_values_stored(self):
        f = Features((0.1, 0.2, 0.3))
        assert f.as_list() == [0.1, 0.2, 0.3]

    def test_dim(self):
        assert Features((1, 2, 3, 4, 5)).dim() == 5

    def test_immutable(self):
        f = Features((1, 2))
        with pytest.raises(Exception):
            f.values[0] = 9