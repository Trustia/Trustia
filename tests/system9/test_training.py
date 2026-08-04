"""Sistem 9 — Eğitim altyapısı testleri."""

import os

import pytest

from ai.mlp import MiniMlp
from ai.training import (
    gaussian_blob,
    load_model,
    make_terrain_dataset,
    save_model,
    split_samples,
    train_classifier,
    confusion_matrix,
)


class TestGaussianBlob:
    @pytest.mark.parametrize("count", [1, 5, 30])
    def test_count(self, count):
        assert len(gaussian_blob([0.5, 0.5], 1, count=count)) == count

    def test_labels(self):
        samples = gaussian_blob([0.5, 0.5], 2, count=10)
        assert all(s[1] == 2 for s in samples)

    def test_values_bounded(self):
        samples = gaussian_blob([1.0, 1.0], 0, sigma=5.0, count=200)
        for x, _ in samples:
            assert 0.0 <= x[0] <= 1.0
            assert 0.0 <= x[1] <= 1.0

    @pytest.mark.parametrize("seed", [0, 3, 9])
    def test_deterministic(self, seed):
        a = gaussian_blob([0.3, 0.6], 0, count=10, seed=seed)
        b = gaussian_blob([0.3, 0.6], 0, count=10, seed=seed)
        assert a == b


class TestDataset:
    def test_terrain_dataset_size(self):
        assert len(make_terrain_dataset(per_class=10)) == 60

    def test_terrain_dataset_classes(self):
        samples = make_terrain_dataset(per_class=5)
        labels = sorted(set(s[1] for s in samples))
        assert labels == [0, 1, 2, 3, 4, 5]

    @pytest.mark.parametrize("per_class", [4, 12])
    def test_balanced_classes(self, per_class):
        samples = make_terrain_dataset(per_class=per_class)
        from collections import Counter
        counts = Counter(s[1] for s in samples)
        assert all(c == per_class for c in counts.values())

    def test_terrain_features_dim(self):
        samples = make_terrain_dataset(per_class=3)
        assert all(len(s[0]) == 4 for s in samples)


class TestSplit:
    @pytest.mark.parametrize("fraction", [0.5, 0.75, 0.9])
    def test_split_ratio(self, fraction):
        samples = [( [0.5] * 2, i % 2) for i in range(100)]
        train_set, eval_set = split_samples(samples, fraction, seed=1)
        expected_eval = int(round(100 * (1 - fraction)))
        assert len(eval_set) == expected_eval
        assert len(train_set) == 100 - expected_eval

    def test_combined_length(self):
        samples = [( [0.5] * 2, 0)] * 40
        train_set, eval_set = split_samples(samples, 0.7, seed=2)
        assert len(train_set) + len(eval_set) == 40

    def test_no_empty_eval(self):
        samples = [( [0.5] * 2, 0)] * 10
        train_set, eval_set = split_samples(samples, 0.99, seed=0)
        assert len(eval_set) >= 1

    @pytest.mark.parametrize("seed", [0, 5])
    def test_split_deterministic(self, seed):
        samples = [( [0.5] * 2, i % 2) for i in range(50)]
        a = split_samples(samples, 0.7, seed=seed)
        b = split_samples(samples, 0.7, seed=seed)
        assert a == b


class TestClassifier:
    def test_training_improves_accuracy(self):
        samples = make_terrain_dataset(per_class=15, seed=7)
        result = train_classifier(samples, epochs=80, lr=0.2)
        assert result.train_accuracy > 0.75
        assert result.eval_accuracy > 0.60

    def test_result_fields(self):
        samples = make_terrain_dataset(per_class=8)
        result = train_classifier(samples, epochs=10)
        assert 0.0 <= result.train_accuracy <= 1.0
        assert 0.0 <= result.eval_accuracy <= 1.0
        assert result.final_loss > 0.0

    @pytest.mark.parametrize("epochs", [5, 20])
    def test_epochs_parameter(self, epochs):
        samples = make_terrain_dataset(per_class=8)
        result = train_classifier(samples, epochs=epochs)
        assert result.model.sizes == [4, 8, 8, 6]

    def test_deterministic_training(self):
        samples = make_terrain_dataset(per_class=8)
        a = train_classifier(samples, seed=11)
        b = train_classifier(samples, seed=11)
        assert a.final_loss == b.final_loss

    def test_summary_string(self):
        samples = make_terrain_dataset(per_class=4)
        result = train_classifier(samples, epochs=5)
        text = result.summary()
        assert "train=" in text and "eval=" in text

    def test_confusion_matrix_shape(self):
        samples = make_terrain_dataset(per_class=6)
        model = MiniMlp([4, 8, 8, 6])
        matrix = confusion_matrix(model, samples, 6)
        assert len(matrix) == 6
        assert all(len(row) == 6 for row in matrix)
        assert sum(sum(row) for row in matrix) == len(samples)


class TestPersistence:
    def test_save_load_roundtrip(self, tmp_path):
        samples = make_terrain_dataset(per_class=6)
        result = train_classifier(samples, epochs=30)
        path = os.path.join(str(tmp_path), "model.json")
        save_model(result.model, path, ("a", "b", "c", "d", "e", "f"))
        model, names = load_model(path)
        assert names == ("a", "b", "c", "d", "e", "f")
        assert model.predict(samples[0][0]) == result.model.predict(samples[0][0])

    def test_save_creates_directory(self, tmp_path):
        path = os.path.join(str(tmp_path), "nested", "dir", "model.json")
        save_model(MiniMlp([4, 2]), path, ("x", "y"))
        assert os.path.exists(path)

    def test_load_missing_file_raises(self, tmp_path):
        with pytest.raises(Exception):
            load_model(os.path.join(str(tmp_path), "yok.json"))