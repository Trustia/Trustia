"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — Eğitim altyapısı.

Sentetik öznitelik verisi üretimi, veri bölme, eğitim-keşif iş akışı
ve model serileştirme. PLAN 3.2: "derin öğrenme modelleri, eğitim
altyapısı". Deterministik üretim (tohum verilebilir).
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from ai.mlp import MiniMlp

Sample = Tuple[List[float], int]  # (öznitelik vektörü, sınıf indeksi)


def gaussian_blob(
    center: Sequence[float],
    class_index: int,
    sigma: float = 0.15,
    count: int = 30,
    seed: int = 0,
) -> List[Sample]:
    """Sınıf merkezi etrafında Gauss dağılımlı sentetik örnekler."""
    rng = random.Random(seed)
    return [
        (
            [max(0.0, min(1.0, c + rng.gauss(0.0, sigma))) for c in center],
            class_index,
        )
        for _ in range(count)
    ]


def make_terrain_dataset(per_class: int = 24, seed: int = 7) -> List[Sample]:
    """Arazi sınıfları için sentetik eğitim seti.

    Sınıflar ve merkez öznitelikleri (eğim, pürüzlülük, yansıma,
    düşey zenginlik):
      asfalt (düz, yüksek yansıma), çimen, çamur, kaya, çukur, su.
    """
    centers = {
        "asfalt": (0.05, 0.03, 0.85, 0.02),
        "cimen": (0.20, 0.12, 0.45, 0.15),
        "camur": (0.30, 0.25, 0.20, 0.30),
        "kaya": (0.55, 0.45, 0.35, 0.75),
        "cukur": (0.45, 0.35, 0.25, 0.60),
        "su": (0.10, 0.08, 0.05, 0.05),
    }
    samples: List[Sample] = []
    for class_index, center in enumerate(centers.values()):
        samples.extend(
            gaussian_blob(center, class_index, sigma=0.08, count=per_class, seed=seed + class_index)
        )
    return samples


@dataclass
class TrainingResult:
    """Eğitim çıktısı: metrikler + model."""

    model: MiniMlp
    train_accuracy: float
    eval_accuracy: float
    final_loss: float
    class_names: Tuple[str, ...]

    def summary(self) -> str:
        return (
            f"train=%{self.train_accuracy * 100:.1f} "
            f"eval=%{self.eval_accuracy * 100:.1f} loss={self.final_loss:.4f}"
        )


def split_samples(
    samples: Sequence[Sample], fraction: float = 0.75, seed: int = 3
) -> Tuple[List[Sample], List[Sample]]:
    """Örnekleri (eğitim, değerlendirme) olarak böler."""
    rng = random.Random(seed)
    order = list(samples)
    rng.shuffle(order)
    cut = max(1, int(len(order) * fraction))
    return list(order[:cut]), list(order[cut:])


def train_classifier(
    samples: Sequence[Sample],
    hidden: Sequence[int] = (8, 8),
    epochs: int = 60,
    lr: float = 0.15,
    eval_fraction: float = 0.25,
    seed: int = 11,
) -> TrainingResult:
    """Sınıflandırıcı eğitir; eğitim/keşif metrikleriyle döndürür."""
    train_set, eval_set = split_samples(samples, 1.0 - eval_fraction, seed=seed)
    dim = len(samples[0][0])
    class_count = max(sample[1] for sample in samples) + 1
    model = MiniMlp([dim, *hidden, class_count], seed=seed)
    X_train = [s[0] for s in train_set]
    y_train = [s[1] for s in train_set]
    losses = model.train(
        X_train, y_train, epochs=epochs, lr=lr, batch_size=8, seed=seed
    )
    train_acc = model.accuracy(X_train, y_train)
    eval_acc = (
        model.accuracy([s[0] for s in eval_set], [s[1] for s in eval_set])
        if eval_set
        else train_acc
    )
    return TrainingResult(
        model=model,
        train_accuracy=train_acc,
        eval_accuracy=eval_acc,
        final_loss=losses[-1] if losses else 0.0,
        class_names=(),
    )


def confusion_matrix(
    model: MiniMlp,
    samples: Sequence[Sample],
    class_count: int,
) -> List[List[int]]:
    """Gerçek x tahmin kareleme matrisi."""
    matrix = [[0] * class_count for _ in range(class_count)]
    for x, y in samples:
        matrix[y][model.predict(x)] += 1
    return matrix


def save_model(model: MiniMlp, path: str, class_names: Sequence[str]) -> None:
    """Model + sınıf adlarını tek JSON dosyasına yazar."""
    import json
    import os

    payload = {
        "model": json.loads(model.to_json()),
        "class_names": list(class_names),
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh)


def load_model(path: str) -> Tuple[MiniMlp, Tuple[str, ...]]:
    """`save_model` ile yazılan dosyayı okur."""
    import json

    with open(path, encoding="utf-8") as fh:
        payload = json.load(fh)
    return MiniMlp.from_json(json.dumps(payload["model"])), tuple(payload["class_names"])