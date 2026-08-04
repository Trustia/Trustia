"""Sistem 9 — Geri yayılım sayısal doğrulaması.

Analitik gradyanlar sonlu fark (finite-difference) ile karşılaştırılır.
Bu, ağın türevlerinin doğru olduğunu kanıtlayan geleneksel testtir.
"""

from __future__ import annotations

import math

import pytest

from ai.mlp import MiniMlp


def _loss(model, x, target):
    probs = model.probabilities(x)
    return -math.log(max(probs[target], 1e-12))


def _restore_layers(model, items):
    model.layers = [tuple(tuple(n) for n in layer) for layer in items]


def _numerical_grad(model, x, target, eps=1e-4):
    """Her ağırlık için merkezlenmiş sonlu fark gradyanı."""
    items = [[list(n) for n in layer] for layer in model.layers]
    base = _loss(model, x, target)
    grads = []
    for li, layer in enumerate(items):
        layer_grads = []
        for n in range(len(layer)):
            neuron_grads = []
            for i in range(len(layer[n])):
                old = items[li][n][i]
                items[li][n][i] = old + eps
                _restore_layers(model, items)
                up = _loss(model, x, target)
                items[li][n][i] = old - eps
                _restore_layers(model, items)
                dn = _loss(model, x, target)
                items[li][n][i] = old
                neuron_grads.append((up - dn) / (2 * eps))
            layer_grads.append(tuple(neuron_grads))
        grads.append(tuple(layer_grads))
    _restore_layers(model, items)
    assert base == pytest.approx(_loss(model, x, target))
    return grads


@pytest.mark.parametrize("hidden", [[3], [4, 3], [5]])
@pytest.mark.parametrize("seed", [0, 5, 11])
def test_analytical_matches_numerical(hidden, seed):
    model = MiniMlp([2, *hidden, 2], seed=seed)
    x = [0.3, 0.7]
    loss, analytic = model._backward(x, 1)
    numeric = _numerical_grad(model, x, 1)
    assert loss == pytest.approx(_loss(model, x, 1))
    for li in range(len(model.layers)):
        for n in range(len(model.layers[li])):
            for i in range(len(model.layers[li][n])):
                assert abs(analytic[li][n][i] - numeric[li][n][i]) < 1e-4


@pytest.mark.parametrize("hidden", [[2], [3, 3]])
def test_gradient_of_second_class(hidden):
    model = MiniMlp([2, *hidden, 3], seed=7)
    numeric = _numerical_grad(model, [0.8, 0.2], 2)
    _, analytic = model._backward([0.8, 0.2], 2)
    for li in range(len(model.layers)):
        for n in range(len(model.layers[li])):
            for i in range(len(model.layers[li][n])):
                assert abs(analytic[li][n][i] - numeric[li][n][i]) < 1e-4


def test_loss_finite():
    model = MiniMlp([2, 3, 2], seed=1)
    loss, _ = model._backward([0.5, 0.5], 0)
    assert math.isfinite(loss)


@pytest.mark.parametrize("seed", range(4))
def test_backward_does_not_mutate_weights(seed):
    model = MiniMlp([2, 4, 2], seed=seed)
    before = model.to_json()
    model._backward([0.2, 0.8], 1)
    assert model.to_json() == before


@pytest.mark.parametrize("target", [0, 1])
def test_target_gradients_valid(target):
    model = MiniMlp([2, 3, 2], seed=3)
    _, grads = model._backward([0.4, 0.6], target)
    for layer_grad in grads:
        for neuron_grad in layer_grad:
            assert len(neuron_grad) >= 2
            assert all(math.isfinite(g) for g in neuron_grad)