"""Sistem 9 — MiniMLP birim testleri."""

import pytest

from ai.mlp import MiniMlp

XOR_X = [[0, 0], [0, 1], [1, 0], [1, 1]]
XOR_Y = [0, 1, 1, 0]


class TestConstruction:
    @pytest.mark.parametrize("sizes", [
        [2, 1], [2, 4, 2], [3, 5, 5, 2], [1, 16, 8, 4, 2],
    ])
    def test_shape_recorded(self, sizes):
        assert MiniMlp(sizes).sizes == list(sizes)

    def test_invalid_single_layer(self):
        with pytest.raises(ValueError):
            MiniMlp([3])

    def test_layer_count(self):
        assert len(MiniMlp([2, 3, 3, 2]).layers) == 3

    def test_weights_include_bias(self):
        model = MiniMlp([2, 3, 2])
        assert all(len(n) == 3 for n in model.layers[0])
        assert all(len(n) == 4 for n in model.layers[1])

    def test_seed_determinism(self):
        a = MiniMlp([2, 4, 2], seed=42).to_json()
        b = MiniMlp([2, 4, 2], seed=42).to_json()
        assert a == b

    def test_different_seed_differs(self):
        a = MiniMlp([2, 4, 2], seed=1).to_json()
        b = MiniMlp([2, 4, 2], seed=2).to_json()
        assert a != b


class TestForward:
    @pytest.mark.parametrize("x", [
        [0.0, 0.0], [1.0, 1.0], [0.5, 0.5], [0.1, 0.9],
    ])
    def test_logits_output_size(self, x):
        logits, acts = MiniMlp([2, 4, 3]).forward(x)
        assert len(logits) == 3
        assert len(acts) == 2

    def test_softmax_sums_to_one(self):
        model = MiniMlp([2, 4, 3])
        probs = model.probabilities([0.3, 0.7])
        assert sum(probs) == pytest.approx(1.0)

    @pytest.mark.parametrize("i", range(3))
    def test_probabilities_non_negative(self, i):
        model = MiniMlp([2, 4, 3], seed=5)
        assert model.probabilities([0.2, 0.8])[i] >= 0.0

    def test_predict_returns_valid_index(self):
        model = MiniMlp([2, 4, 5])
        assert 0 <= model.predict([0.4, 0.6]) < 5

    def test_deterministic_forward(self):
        model = MiniMlp([2, 3, 2], seed=9)
        assert model.probabilities([0.1, 0.2]) == model.probabilities([0.1, 0.2])


class TestTraining:
    @pytest.mark.parametrize("epochs", [100, 200, 300])
    def test_xor_learns(self, epochs):
        model = MiniMlp([2, 8, 2])
        model.train(XOR_X, XOR_Y, epochs=epochs, lr=0.3)
        assert model.accuracy(XOR_X, XOR_Y) == 1.0

    def test_loss_decreases(self):
        model = MiniMlp([2, 8, 2])
        losses = model.train(XOR_X, XOR_Y, epochs=40, lr=0.3, batch_size=2)
        assert losses[-1] < losses[0]

    @pytest.mark.parametrize("seed", range(5))
    def test_xor_repeatable_across_seeds(self, seed):
        model = MiniMlp([2, 8, 2], seed=seed)
        model.train(XOR_X, XOR_Y, epochs=150, lr=0.3, seed=seed)
        assert model.accuracy(XOR_X, XOR_Y) == 1.0

    def test_single_sample_batch(self):
        model = MiniMlp([2, 8, 2])
        losses = model.train(XOR_X, XOR_Y, epochs=10, batch_size=1)
        assert len(losses) == 10

    def test_large_batch_clamped(self):
        model = MiniMlp([2, 8, 2])
        losses = model.train(XOR_X, XOR_Y, epochs=5, batch_size=100)
        assert len(losses) == 5

    def test_constant_label_set(self):
        model = MiniMlp([2, 3, 2])
        X = [[0.1, 0.1], [0.9, 0.9], [0.5, 0.5]]
        model.train(X, [1, 1, 1], epochs=30)
        assert all(model.predict(x) == 1 for x in X)

    def test_accuracy_empty_dataset(self):
        model = MiniMlp([2, 2])
        assert model.accuracy([], []) == 0.0

    def test_training_returns_epoch_losses(self):
        model = MiniMlp([2, 8, 2])
        losses = model.train(XOR_X, XOR_Y, epochs=7)
        assert len(losses) == 7
        assert all(l > 0 for l in losses)


class TestPersistence:
    def test_json_roundtrip_predictions(self):
        model = MiniMlp([2, 4, 2])
        model.train(XOR_X, XOR_Y, epochs=80, lr=0.3)
        clone = MiniMlp.from_json(model.to_json())
        for x in XOR_X:
            assert clone.predict(x) == model.predict(x)

    def test_json_roundtrip_probabilities(self):
        model = MiniMlp([2, 3, 2], seed=3)
        clone = MiniMlp.from_json(model.to_json())
        assert clone.probabilities([0.2, 0.7]) == pytest.approx(
            model.probabilities([0.2, 0.7])
        )

    def test_from_json_preserves_sizes(self):
        model = MiniMlp([2, 6, 4, 3])
        clone = MiniMlp.from_json(model.to_json())
        assert clone.sizes == [2, 6, 4, 3]

    def test_malformed_json_raises(self):
        with pytest.raises(Exception):
            MiniMlp.from_json("{not valid")