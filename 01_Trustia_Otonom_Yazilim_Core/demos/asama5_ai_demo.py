"""
TRUSTIA AŞAMA 5 - Yapay Zeka Algı (Sistem 9) + Test Tamamlama (Sistem 7)

Akış:
  1) Sentetik arazi verisi uret, MLP ile egit (egitim altyapisi)
  2) Arazi siniflandirma + gecilebilirlik haritasi (traversability)
  3) LiDAR kumeleme ile nesne tanima (insan/arac)
  4) Gunduz/gece sensor fuzyonu (termal agirlik)
  5) Egitilen modeli kaydet/yukle + simulasyon gorev kosusu
  Ciktilari: docs/reports/asama5/ (model.json, harita SVG, METRIKLER)
"""

from __future__ import annotations

import json
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)

from ai.features import Features, lidar_features, terrain_cell
from ai.fusion import fuse
from ai.object_detector import ObjectDetector
from ai.training import make_terrain_dataset, save_model, train_classifier
from ai.traversability import (
    TERRAIN_CLASSES,
    TRAVERSABILITY,
    TraversabilityMap,
    classify_cell,
    cost_for,
)

OUT_DIR = os.path.join(REPO, "docs", "reports", "asama5")
os.makedirs(OUT_DIR, exist_ok=True)


def banner(title: str) -> None:
    print("=" * 62)
    print(" " + title)
    print("=" * 62)


def main() -> int:
    banner("1) Egitim Altyapisi: sentetik veri + MLP")
    samples = make_terrain_dataset(per_class=40, seed=7)
    result = train_classifier(samples, epochs=60, lr=0.15)
    print(f"veri seti: {len(samples)} ornek, 6 sinif")
    print(f"egitim dogrulu:  %{result.train_accuracy * 100:.1f}")
    print(f"kesif dogrulu:   %{result.eval_accuracy * 100:.1f}")
    print(f"son kayip:       {result.final_loss:.4f}")

    banner("2) Model kaydet / yukle (serilestirme)")
    model_path = os.path.join(OUT_DIR, "arazi_model.json")
    save_model(result.model, model_path, TERRAIN_CLASSES)
    from ai.training import load_model

    loaded, names = load_model(model_path)
    probe = samples[0][0]
    print(f"kayit: {os.path.relpath(model_path, REPO)}")
    print(f"yuklendi: {len(names)} sinif, tahmin tutarli: "
          f"{loaded.predict(probe) == result.model.predict(probe)}")

    banner("3) Arazi siniflandirma + gecilebilirlik")
    print(f"sinif gecilebilirlik: "
          f"{' '.join(f'{k}={v:.2f}' for k, v in TRAVERSABILITY.items())}")
    correct = sum(
        1 for i in range(0, len(samples), 40)
        for k in range(40)
        if classify_cell(Features(samples[i + k][0]))[0] == TERRAIN_CLASSES[samples[i + k][1]]
    )
    print(f"kural tabanli siniflandirma dogrulugu: "
          f"%{correct / len(samples) * 100:.1f}")

    tmap = TraversabilityMap(8, 8)
    import random

    rng = random.Random(5)
    for x in range(8):
        for y in range(8):
            slope = rng.uniform(0.0, 0.8)
            rough = rng.uniform(0.0, 0.6)
            reflect = rng.uniform(0.05, 0.9)
            vert = rng.uniform(0.0, 0.8)
            tmap.set_cell(x, y, Features((slope, rough, reflect, vert)))
    passable = tmap.count_passable(0.3)
    print(f"gecilebilirlik haritasi: 64 hucre, "
          f"gecilebilir {passable} (%{passable / 64 * 100:.0f})")

    banner("4) Nesne tanima (LiDAR kumeleme)")
    detector = ObjectDetector()
    vehicle_points = [(x / 2.0 - 1.8, y / 2.0 - 1.8, 0.4) for x in range(8) for y in range(8)]
    person_points = [(0.0, 0.0, z) for z in [0.0, 0.3, 0.6, 0.9]] + [
        (0.1, 0.0, z) for z in [0.2, 0.5, 0.8]
    ]
    hits = detector.detect([
        (vehicle_points, 6.5, 12.0),
        (person_points, 2.8, -8.0),
    ])
    for hit in hits:
        print(f"tespit: {hit.kind:>16} menzil={hit.range_m:.1f} m "
              f"kerteriz={hit.bearing_deg:+.0f} gaven=%{hit.confidence * 100:.0f}")

    banner("5) Gunduz/gece sensor fuzyonu")
    vehicle_cluster = [(vehicle_points, 6.5, 12.0)]
    person_cluster = [(person_points, 2.8, -8.0)]
    day = fuse(detector, vehicle_cluster, vehicle_cluster,
               [200, 210], [8.0])
    night = fuse(detector, vehicle_cluster, person_cluster,
                 [12, 9], [22.0])
    print(f"gunduz (RGB agir): {day.summary()}")
    print(f"gece  (termal agir): {night.summary()}")

    banner("6) Simulasyon gorev kosusu + kayit")
    from record.recorder import MissionRecorder
    from simulation.runner import MissionRunner
    from simulation.scenario import ScenarioGenerator
    from simulation.terrain import Terrain

    mission = ScenarioGenerator(world_size_m=20.0).generate("kesif", seed=11)
    spec = mission.terrain
    terrain = Terrain(
        width_m=spec.width_m, height_m=spec.height_m, seed=spec.seed,
        obstacle_count=spec.obstacle_count, forbidden_count=spec.forbidden_count,
    )
    recorder = MissionRecorder(OUT_DIR, record_id="ai-gorev")
    recorder.set_metadata(model="arazi_model.json", seed=11, gorev="kesif")
    runner = MissionRunner(dt_s=0.1, beam_count=24, lidar_max_range_m=8.0)
    frames = []

    def _cb(frame):
        frames.append(frame.to_dict())
        recorder.record_frame(frame)

    metrics = runner.run(terrain, mission.weather, mission,
                         telemetry_callback=_cb)
    recorder.record_result(metrics)
    recorder.record_event("sonuc", "basarili" if metrics.success else "basarisiz")
    recorder.close()
    print(f"gorev: kesif seed=11 -> basari={metrics.success} "
          f"adim={metrics.steps} sure={metrics.duration_s:.1f} s")
    print(f"konum hatasi={metrics.position_error_m:.2f} m, "
          f"rota sapmasi={metrics.route_deviation_m:.2f} m")
    print(f"kayit dosyasi: {os.path.relpath(recorder.path, REPO)} "
          f"({len(frames)} telemetri cercevesi)")

    banner("7) Metrik ozeti (Sistem 7)")
    summary = {
        "egitim_verisi": len(samples),
        "train_accuracy": round(result.train_accuracy, 4),
        "eval_accuracy": round(result.eval_accuracy, 4),
        "final_loss": round(result.final_loss, 4),
        "kural_siniflandirma_accuracy": round(correct / len(samples), 4),
        "harita_gecilebilir_hucre": passable,
        "nesne_tespitleri": [h.to_dict() for h in hits],
        "gorev": {
            "success": metrics.success,
            "steps": metrics.steps,
            "duration_s": round(metrics.duration_s, 2),
            "position_error_m": round(metrics.position_error_m, 3),
            "route_deviation_m": round(metrics.route_deviation_m, 3),
        },
    }
    meta_path = os.path.join(OUT_DIR, "METRIKLER.json")
    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)
    print(f"metrikler: {os.path.relpath(meta_path, REPO)}")
    print()
    print("AŞAMA 5 tamamlandi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
