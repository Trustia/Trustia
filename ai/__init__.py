"""
TRUSTIA Yapay Zeka Algı (Sistem 9) — toplayıcı.

Paket yüzeyi: öznitelik çıkarma, mini MLP eğitimi, arazi
sınıflandırma/geçilebilirlik, nesne tanıma ve sensör füzyonu.
PLAN 3.2: "derin öğrenme modelleri, eğitim altyapısı, arazi
sınıflandırma, nesne tanıma".
"""

from ai.features import (
    Features,
    cluster_shape,
    lidar_features,
    pixel_darkness,
    terrain_cell,
    thermal_signal,
)
from ai.fusion import FusionResult, fuse, nearest_fused_hazard
from ai.mlp import MiniMlp
from ai.object_detector import (
    Detection,
    ObjectDetector,
    cluster_accuracy,
    classify_object,
)
from ai.training import (
    TrainingResult,
    gaussian_blob,
    load_model,
    make_terrain_dataset,
    save_model,
    split_samples,
    train_classifier,
)
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

from ai.bomb_detector import (
    BombDetector,
    ExplosiveType,
    SensorReading,
    ThreatReport,
)
from ai.cbrn_detector import (
    CbrnDetector,
    CbrnReading,
    CbrnThreatReport,
    CbrnThreatType,
)

__all__ = [
    "Features",
    "cluster_shape",
    "lidar_features",
    "pixel_darkness",
    "terrain_cell",
    "thermal_signal",
    "FusionResult",
    "fuse",
    "nearest_fused_hazard",
    "MiniMlp",
    "Detection",
    "ObjectDetector",
    "cluster_accuracy",
    "classify_object",
    "TrainingResult",
    "gaussian_blob",
    "load_model",
    "make_terrain_dataset",
    "save_model",
    "split_samples",
    "train_classifier",
    "TERRAIN_CLASSES",
    "TRAVERSABILITY",
    "TraversabilityCell",
    "TraversabilityMap",
    "cell_traversability",
    "classify_cell",
    "class_accuracy",
    "cost_for",
    "BombDetector",
    "ExplosiveType",
    "SensorReading",
    "ThreatReport",
    "FormationType",
    "SwarmAgentState",
    "SwarmCoordinator",
    "CbrnDetector",
    "CbrnReading",
    "CbrnThreatReport",
    "CbrnThreatType",
]