"""
TRUSTIA Simülasyon Dünyası — Kampanya koşucusu (10.000 görev koşusu).

Toplu kampanya: deterministik seed sırasıyla görev üretir, koşar,
metrikleri toplar ve AŞAMA 2 raporunu (docs/reports) üretir.

Kullanım:
    python -m simulation.campaign --count 10000
"""

from __future__ import annotations

import argparse
import datetime
import os
import pickle
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from simulation.runner import MissionMetrics, MissionRunner
from simulation.scenario import ScenarioGenerator
from simulation.terrain import Terrain, Weather

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@dataclass
class CampaignSummary:
    """Kampanya özet istatistikleri."""

    total_runs: int = 0
    successful: int = 0
    collisions: int = 0
    forbidden_violations: int = 0
    time_outs: int = 0
    out_of_bounds: int = 0
    total_duration_s: float = 0.0
    avg_duration_s: float = 0.0
    position_error_m: float = 0.0
    route_deviation_m: float = 0.0
    reaction_time_s: float = 0.0
    min_clearance_m: float = 0.0
    per_type: Dict[str, Dict[str, float]] = field(default_factory=dict)


def _run_block(
    start_seed: int,
    run_count: int,
    world_size_m: float,
) -> Tuple[CampaignSummary, List[MissionMetrics]]:
    """Tek process içinde seed bloğunu koşar (paralel kampanya birimi)."""
    generator = ScenarioGenerator(world_size_m=world_size_m)
    runner = MissionRunner(seed=start_seed)
    types = ("devriye", "kesif", "lojistik", "engelli-parkur", "gps-koridor")
    summary = CampaignSummary()
    results: List[MissionMetrics] = []
    for offset in range(run_count):
        seed = start_seed + offset
        mission = generator.generate(types[seed % len(types)], seed)
        terrain = Terrain(
            width_m=mission.terrain.width_m,
            height_m=mission.terrain.height_m,
            seed=mission.terrain.seed,
            obstacle_count=mission.terrain.obstacle_count,
            forbidden_count=mission.terrain.forbidden_count,
        )
        metrics = runner.run(terrain, mission.weather, mission)
        results.append(metrics)
        summary.total_runs += 1
        summary.total_duration_s += metrics.duration_s
        if metrics.success:
            summary.successful += 1
        if metrics.collision:
            summary.collisions += 1
        if metrics.forbidden_violation:
            summary.forbidden_violations += 1
        if metrics.time_out:
            summary.time_outs += 1
        if metrics.out_of_bounds:
            summary.out_of_bounds += 1
        summary.position_error_m += metrics.position_error_m
        summary.route_deviation_m += metrics.route_deviation_m
        summary.reaction_time_s += metrics.reaction_time_s
        summary.min_clearance_m += metrics.min_obstacle_clearance_m
        entry = summary.per_type.setdefault(
            metrics.mission_type,
            {"runs": 0, "success": 0, "error": 0.0},
        )
        entry["runs"] += 1
        if metrics.success:
            entry["success"] += 1
        entry["error"] += metrics.position_error_m
    return summary, results


def _merge_summaries(parts: List[Tuple[CampaignSummary, List[MissionMetrics]]]) -> Tuple[CampaignSummary, List[MissionMetrics]]:
    """Paralel blok sonuçlarını tek özet ve metrik listesinde birleştirir."""
    merged = CampaignSummary()
    all_metrics: List[MissionMetrics] = []
    for summary, results in parts:
        all_metrics.extend(results)
        merged.total_runs += summary.total_runs
        merged.successful += summary.successful
        merged.collisions += summary.collisions
        merged.forbidden_violations += summary.forbidden_violations
        merged.time_outs += summary.time_outs
        merged.out_of_bounds += summary.out_of_bounds
        merged.total_duration_s += summary.total_duration_s
        merged.position_error_m += summary.position_error_m
        merged.route_deviation_m += summary.route_deviation_m
        merged.reaction_time_s += summary.reaction_time_s
        merged.min_clearance_m += summary.min_clearance_m
        for name, entry in summary.per_type.items():
            target = merged.per_type.setdefault(
                name, {"runs": 0, "success": 0, "error": 0.0}
            )
            for key in ("runs", "success"):
                target[key] += entry[key]
            target["error"] += entry["error"]
    return merged, all_metrics


def _finalize(summary: CampaignSummary) -> None:
    """Toplamları ortalamalara çevirir ve tip başına oranları ekler."""
    n = summary.total_runs
    if n:
        summary.avg_duration_s = summary.total_duration_s / n
        summary.position_error_m /= n
        summary.route_deviation_m /= n
        summary.reaction_time_s /= n
        summary.min_clearance_m /= n
    for entry in summary.per_type.values():
        if entry["runs"]:
            entry["error"] /= entry["runs"]
            entry["success_rate"] = entry["success"] / entry["runs"] * 100.0


def _summarize_metrics(results: List[MissionMetrics]) -> CampaignSummary:
    """Metrik listesinden tam özet üretir (birleştirme için)."""
    summary = CampaignSummary()
    for metrics in results:
        summary.total_runs += 1
        summary.total_duration_s += metrics.duration_s
        if metrics.success:
            summary.successful += 1
        if metrics.collision:
            summary.collisions += 1
        if metrics.forbidden_violation:
            summary.forbidden_violations += 1
        if metrics.time_out:
            summary.time_outs += 1
        if metrics.out_of_bounds:
            summary.out_of_bounds += 1
        summary.position_error_m += metrics.position_error_m
        summary.route_deviation_m += metrics.route_deviation_m
        summary.reaction_time_s += metrics.reaction_time_s
        summary.min_clearance_m += metrics.min_obstacle_clearance_m
        entry = summary.per_type.setdefault(
            metrics.mission_type,
            {"runs": 0, "success": 0, "error": 0.0},
        )
        entry["runs"] += 1
        if metrics.success:
            entry["success"] += 1
        entry["error"] += metrics.position_error_m
    _finalize(summary)
    return summary


def _worker_run(block: Tuple[int, int, float]) -> Tuple[CampaignSummary, List[MissionMetrics]]:
    """Process havuzu için modül düzeyinde sarıcı (spawn'da lambda yok)."""
    return _run_block(*block)


class Campaign:
    """Seed aralığındaki görevleri sırayla koşan toplu koşucu."""

    def __init__(
        self,
        start_seed: int = 0,
        run_count: int = 1000,
        world_size_m: float = 40.0,
        verbose: bool = True,
        workers: int = 1,
    ) -> None:
        if run_count <= 0:
            raise ValueError("koşu sayısı pozitif olmalı")
        if workers <= 0:
            raise ValueError("işçi sayısı pozitif olmalı")
        self._start_seed = start_seed
        self._run_count = run_count
        self._world_size = world_size_m
        self._verbose = verbose
        self._workers = workers
        self._generator = ScenarioGenerator(world_size_m=world_size_m)
        self._runner = MissionRunner(seed=start_seed)

    def run(self) -> Tuple[CampaignSummary, List[MissionMetrics]]:
        """Kampanyayı koşar; (özet, tüm metrikler) döndürür.

        Workers > 1 ise seed bloğu process havuzuna dağıtılır;
        aksi hâlde tek process içinde seri koşulur.
        """
        started = time.perf_counter()
        block_count = self._workers
        block_size = -(-self._run_count // block_count)
        blocks: List[Tuple[int, int, int]] = []
        for index in range(block_count):
            start = self._start_seed + index * block_size
            count = min(block_size, self._run_count - index * block_size)
            if count > 0:
                blocks.append((start, count, self._world_size))
        if self._workers > 1 and len(blocks) > 1:
            with ProcessPoolExecutor(max_workers=self._workers) as pool:
                parts: List[Tuple[CampaignSummary, List[MissionMetrics]]] = (
                    list(pool.map(_worker_run, blocks))
                )
        else:
            parts = [_run_block(*block) for block in blocks]
        merged, all_metrics = _merge_summaries(parts)
        _finalize(merged)
        if self._verbose:
            elapsed = time.perf_counter() - started
            rate = (merged.successful / merged.total_runs * 100.0
                    if merged.total_runs else 0.0)
            print(
                f"Kampanya: {merged.total_runs} koşu, başarı %{rate:.1f}, "
                f"{elapsed:.1f} sn"
            )
        return merged, all_metrics

    def write_report(self, summary: CampaignSummary) -> str:
        """AŞAMA 2 raporunu Markdown olarak üretir."""
        output_path = os.path.join(
            REPO_ROOT, "docs", "reports", "SIMULASYON_RAPORU_ASAMA2.md"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        success_rate = (summary.successful / summary.total_runs * 100.0
                        if summary.total_runs else 0.0)
        lines = [
            "# TRUSTIA SİMÜLASYON RAPORU (AŞAMA 2)",
            "",
            f"- **Proje sürümü:** 0.2.0",
            f"- **Tarih:** {datetime.date.today().isoformat()}",
            f"- **Ortam:** {sys.platform}, Python {sys.version.split()[0]}",
            f"- **Görev koşusu sayısı:** {summary.total_runs}",
            f"- **Dünya boyutu:** {self._world_size:.0f} x {self._world_size:.0f} m",
            "",
            "## 1. GENEL SONUÇ",
            "",
            "| Metrik | Değer |",
            "|---|---|",
            f"| Görev başarı oranı | %{success_rate:.1f} |",
            f"| Çarpışma sayısı | {summary.collisions} |",
            f"| Yasak bölge ihlali | {summary.forbidden_violations} |",
            f"| Süre aşımı | {summary.time_outs} |",
            f"| Saha dışı | {summary.out_of_bounds} |",
            f"| Ortalama görev süresi | {summary.avg_duration_s:.1f} sn |",
            f"| GPS'siz konum hatası (ort) | {summary.position_error_m:.2f} m |",
            f"| Rota sapması (ort) | {summary.route_deviation_m:.2f} m |",
            f"| Engel tepki süresi (ort) | {summary.reaction_time_s:.3f} sn |",
            f"| Minimum engel payı (ort) | {summary.min_clearance_m:.2f} m |",
            "",
            "## 2. GÖREV TİPİNE GÖRE DAĞILIM",
            "",
            "| Görev tipi | Koşu | Başarı | Başarı Oranı | Konum Hatası (m) |",
            "|---|---|---|---|---|",
        ]
        for name, entry in sorted(summary.per_type.items()):
            lines.append(
                f"| {name} | {entry['runs']} | {entry['success']} "
                f"| %{entry.get('success_rate', 0.0):.1f} "
                f"| {entry['error']:.2f} |"
            )
        lines += [
            "",
            "## 3. YORUM",
            "",
            "- Görev başarı oranı %100 olmayan durumların her biri "
            "çarpışma/ihlal/süre analizine açıktır; tekrar üretim "
            "deterministik seed ile birebir tekrarlanabilir.",
            "- GPS'siz koridor görevlerindeki konum hatası, odometri "
            "birikim hatası + LiDAR engel kaçınmasının etkileşimidir.",
            "- Tüm koşular aynı koşucu (otonomi zinciri) ile üretildi: "
            "algı → SLAM → planlama → kontrol → araç.",
            "",
        ]
        report = "\n".join(lines)
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(report)
        return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="TRUSTIA simülasyon kampanyası")
    parser.add_argument("--count", type=int, default=1000,
                        help="koşu sayısı (varsayılan: 1000)")
    parser.add_argument("--start-seed", type=int, default=0)
    parser.add_argument("--world-size", type=float, default=40.0)
    parser.add_argument("--workers", type=int, default=1,
                        help="paralel process sayısı")
    parser.add_argument("--save-results", type=str, default=None,
                        help="metrik listesini pickle dosyasına yazar")
    parser.add_argument("--merge-results", nargs="+", default=None,
                        help="pickle parçalarını birleştirip rapor yazar")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.merge_results:
        all_metrics: List[MissionMetrics] = []
        for path in args.merge_results:
            with open(path, "rb") as fh:
                all_metrics.extend(pickle.load(fh))
        summary = _summarize_metrics(all_metrics)
        campaign = Campaign(
            start_seed=args.start_seed,
            run_count=len(all_metrics),
            world_size_m=args.world_size,
            verbose=False,
        )
        report_path = campaign.write_report(summary)
        rate = summary.successful / summary.total_runs * 100.0
        print(
            f"Birleştirme tamam: {summary.total_runs} koşu, başarı %{rate:.1f}, "
            f"çarpışma {summary.collisions}"
        )
        print(f"Rapor: {report_path}")
        return 0

    campaign = Campaign(
        start_seed=args.start_seed,
        run_count=args.count,
        world_size_m=args.world_size,
        verbose=not args.quiet,
        workers=args.workers,
    )
    summary, results = campaign.run()
    report_path = campaign.write_report(summary)
    rate = summary.successful / summary.total_runs * 100.0
    print(
        f"Kampanya tamam: {summary.total_runs} koşu, başarı %{rate:.1f}, "
        f"çarpışma {summary.collisions}"
    )
    print(f"Rapor: {report_path}")
    if args.save_results:
        with open(args.save_results, "wb") as fh:
            pickle.dump(results, fh)
        print(f"Parça sonuçları: {args.save_results}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
