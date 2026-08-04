"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Mini MLP (saf Python).

Bağımlılıksız çok katmanlı algılayıcı: ileri yayılım, geri yayılım,
SGD + minibatch, cross-entropy + softmax. Küçük boyutlarda gerçek
eğitim yapılabilir (XOR, sentetik sınıflandırma). PLAN 3.2:
"derin öğrenme modelleri, eğitim altyapısı".
"""

from __future__ import annotations

import json
import math
import random
from typing import List, Sequence, Tuple

Neuron = Tuple[float, ...]          # ağırlıklar + bias (son eleman)
Layer = Tuple[Neuron, ...]


def _xavier(size_in: int, size_out: int, rng: random.Random) -> Layer:
    limit = math.sqrt(6.0 / max(1, size_in + size_out))
    return tuple(
        tuple(rng.uniform(-limit, limit) for _ in range(size_in + 1))
        for _ in range(size_out)
    )


class MiniMlp:
    """Tam bağlı çok katmanlı ağ (0-1 giriş, softmax çıkış).

    `sizes` katman büyüklüklerini verir; son katman sınıf sayısıdır.
    Ağırlıklar `to_json`/`from_json` ile kaydedilip yüklenebilir.
    """

    def __init__(self, sizes: Sequence[int], seed: int = 0) -> None:
        if len(sizes) < 2:
            raise ValueError("en az iki katman gerekli")
        self.sizes = list(sizes)
        rng = random.Random(seed)
        self.layers: List[Layer] = [
            _xavier(sizes[i], sizes[i + 1], rng)
            for i in range(len(sizes) - 1)
        ]

    # ------------------------------------------------------------------
    @staticmethod
    def _neuron_dot(neuron: Neuron, inputs: Sequence[float]) -> float:
        result = neuron[-1]
        for i in range(len(neuron) - 1):
            result += neuron[i] * inputs[i]
        return result

    def forward(self, x: Sequence[float]) -> Tuple[List[float], List[List[float]]]:
        """İleri yayılım; (logits, katman aktivasyonları) döndürür."""
        activations: List[List[float]] = []
        current = list(x)
        for layer in self.layers[:-1]:
            current = [math.tanh(self._neuron_dot(n, current)) for n in layer]
            activations.append(list(current))
        logits = [self._neuron_dot(n, current) for n in self.layers[-1]]
        activations.append(list(current))
        return logits, activations

    def predict(self, x: Sequence[float]) -> int:
        """En yüksek olasılıklı sınıf indeksi."""
        logits, _ = self.forward(x)
        return max(range(len(logits)), key=lambda i: logits[i])

    def probabilities(self, x: Sequence[float]) -> List[float]:
        """Softmax olasılık dağılımı."""
        logits, _ = self.forward(x)
        return self._softmax(logits)

    @staticmethod
    def _softmax(logits: Sequence[float]) -> List[float]:
        mx = max(logits)
        exp = [math.exp(v - mx) for v in logits]
        total = sum(exp)
        return [e / total for e in exp]

    # ------------------------------------------------------------------
    def train(
        self,
        X: Sequence[Sequence[float]],
        y: Sequence[int],
        epochs: int = 30,
        lr: float = 0.1,
        batch_size: int = 8,
        seed: int = 1,
    ) -> List[float]:
        """Minibatch SGD; her epoch sonunda ortalama kayıp listesi."""
        rng = random.Random(seed)
        samples = list(range(len(X)))
        losses: List[float] = []
        for _ in range(epochs):
            rng.shuffle(samples)
            epoch_loss = 0.0
            for start in range(0, len(samples), batch_size):
                batch = samples[start:start + batch_size]
                grads = self._zero_grads()
                for idx in batch:
                    sample_loss, sample_grads = self._backward(X[idx], y[idx])
                    epoch_loss += sample_loss
                    for l in range(len(self.layers)):
                        for n in range(len(grads[l])):
                            for w in range(len(grads[l][n])):
                                grads[l][n][w] += sample_grads[l][n][w]
                self._apply_grads(grads, lr / len(batch))
            losses.append(epoch_loss / len(samples))
        return losses

    def accuracy(self, X: Sequence[Sequence[float]], y: Sequence[int]) -> float:
        correct = sum(1 for x, t in zip(X, y) if self.predict(x) == t)
        return correct / max(1, len(y))

    # ------------------------------------------------------------------
    def _zero_grads(self) -> List[Layer]:
        return [
            [[0.0 for _ in range(len(neuron))] for neuron in layer]
            for layer in self.layers
        ]

    def _backward(self, x: Sequence[float], target: int) -> Tuple[float, List[Layer]]:
        """Tek örnek geri yayılım; (kayıp, katman gradyanları)."""
        logits, activations = self.forward(x)
        probs = self._softmax(logits)
        loss = -math.log(max(probs[target], 1e-12))
        delta = [p - (1.0 if i == target else 0.0) for i, p in enumerate(probs)]
        grads: List[Layer] = [() for _ in range(len(self.layers))]
        for l in range(len(self.layers) - 1, -1, -1):
            layer = self.layers[l]
            inputs = list(x) if l == 0 else activations[l - 1]
            layer_grad = []
            for n, neuron in enumerate(layer):
                neuron_grad = [delta[n] * inputs[i] for i in range(len(neuron) - 1)]
                neuron_grad.append(delta[n])
                layer_grad.append(tuple(neuron_grad))
            grads[l] = tuple(layer_grad)
            if l > 0:
                new_delta = [0.0] * len(self.layers[l - 1])
                for prev in range(len(inputs)):
                    total = sum(delta[n] * neuron[prev] for n, neuron in enumerate(layer))
                    new_delta[prev] = total * (1.0 - inputs[prev] ** 2)
                delta = new_delta
        return loss, grads

    def _apply_grads(self, grads: List[Layer], step: float) -> None:
        self.layers = [
            tuple(
                tuple(w - step * grads[l][n][i] for i, w in enumerate(neuron))
                for n, neuron in enumerate(layer)
            )
            for l, layer in enumerate(self.layers)
        ]

    # ------------------------------------------------------------------
    def to_json(self) -> str:
        return json.dumps({
            "sizes": self.sizes,
            "layers": [[list(neuron) for neuron in layer] for layer in self.layers],
        })

    @classmethod
    def from_json(cls, text: str) -> "MiniMlp":
        payload = json.loads(text)
        model = cls(payload["sizes"])
        model.layers = [
            tuple(tuple(neuron) for neuron in layer)
            for layer in payload["layers"]
        ]
        return model