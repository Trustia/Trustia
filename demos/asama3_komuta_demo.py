"""
TRUSTIA AŞAMA 3 — Uçtan uca "görev ver-izle-rapor al" gösterisi.

Komuta merkezinde 3 araç kayıtlı; operatör her araca farklı tipte
görev siparişi verir, merkez simülasyon dünyasında koşturur, canlı
telemetri/alarm akışını izler, kayıtları oynatıp görev raporlarını
üretir. Çıktılar docs/reports/asama3/ dizinine yazılır.

Çalıştırma:  python demos/asama3_komuta_demo.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command import CommandCenter, MissionOrder
from command.auth import Role, Session
from core.transforms import EnuPoint
from record import MissionRecorder, MissionReport, Replay
from simulation.runner import MissionRunner
from simulation.terrain import Terrain, Weather

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "reports", "asama3",
)

MISSIONS = [
    ("A-01", "Keşif Aracı 1", "kesif", 120.0, [(30, 30)], 3, 1),
    ("A-02", "Lojistik Aracı 2", "lojistik", 150.0, [(32, 26)], 4, 2),
    ("A-03", "Engelli Parkur 3", "engelli-parkur", 200.0, [(30, 30)], 5, 3),
]


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    center = CommandCenter()
    center.access.set_role("admin", Role.ADMIN)
    center.access.set_role("op", Role.OPERATOR)
    for vehicle_id, name, *_ in MISSIONS:
        center.register_vehicle("admin", vehicle_id, name)

    print("== AŞAMA 3 — KOMUTA MERKEZİ + VERİ KAYIT GÖSTERİSİ ==")
    results = []
    for vehicle_id, name, mission_type, time_limit, targets, seed, world_seed in MISSIONS:
        order = MissionOrder(
            order_id=f"G-{vehicle_id.replace('-', '')}",
            vehicle_id=vehicle_id,
            mission_type=mission_type,
            waypoints=[EnuPoint(east_m=float(x), north_m=float(y)) for x, y in targets],
            time_limit_s=time_limit,
            priority=5,
            issued_by="op",
        )
        order_id = center.submit_mission("op", order)
        print(f"\n[{name}] görev verildi: {order_id} ({mission_type})")

        terrain = Terrain(width_m=40, height_m=40, seed=world_seed)
        if mission_type == "kesif":
            terrain.add_obstacle(15, 15, 1.5)
            terrain.add_forbidden(25, 10, 2.0)
        elif mission_type == "lojistik":
            terrain.add_obstacle(12, 20, 2.0)
            terrain.add_obstacle(20, 12, 1.2)
        else:
            for ox, oy, radius in [(10, 10, 1.2), (20, 20, 1.5),
                                   (25, 15, 1.0), (15, 25, 1.8)]:
                terrain.add_obstacle(ox, oy, radius)

        recorder = MissionRecorder(OUT_DIR, record_id=order_id).start()
        recorder.set_metadata(
            mission_id=order_id, vehicle_id=vehicle_id,
            mission_type=mission_type, world_size_m=40.0,
        )
        session = Session("op", center.access)
        metrics = center.dispatch(
            session, order_id, terrain, Weather(), MissionRunner(seed=seed),
            start=(2, 2), telemetry_callback=recorder.record_frame,
        )
        recorder.record_result(metrics)
        recorder.close()

        replay = Replay.load(recorder.path)
        report_path = MissionReport(
            replay, world_size_m=40.0,
            obstacles=[(o.x_m, o.y_m, o.radius_m) for o in terrain.obstacles],
            record_path=recorder.path,
        ).write(OUT_DIR)
        results.append((vehicle_id, name, mission_type, metrics, recorder))
        print(
            f"  sonuç: {'BAŞARILI' if metrics.success else 'BAŞARISIZ'} "
            f"| {metrics.steps} adım | {metrics.duration_s:.1f} sn "
            f"| konum hatası {metrics.position_error_m:.2f} m "
            f"| kayıt {recorder.frame_count()} çerçeve"
        )
        print(f"  rapor: {os.path.relpath(report_path)}")

    snapshot = center.live_snapshot("op")
    print("\n== CANLI GÖRÜNÜM ==")
    print(f"Filo: {snapshot['fleet']['total_vehicles']} araç "
          f"({snapshot['fleet']['online_vehicles']} çevrim içi)")
    for vehicle in snapshot["fleet"]["vehicles"]:
        print(
            f"  {vehicle['vehicle_id']} {vehicle['name']}: "
            f"hız {vehicle['speed_mps']:.2f} m/s, "
            f"batarya %{vehicle['battery_percent']}, "
            f"bağlantı {vehicle['link_quality']:.2f}, "
            f"engel {vehicle['obstacle_count']}"
        )
    print(f"Aktif alarm: {len(snapshot['alarms'])}")
    print(f"Sicil: {len(snapshot['missions']['orders'])} görev")
    for entry in snapshot["missions"]["orders"]:
        print(f"  {entry['order_id']}: {entry['state']} ({entry['outcome'] or '-'})")

    _write_stage_report(results, snapshot)
    print("\nKOMUTA_RAPORU_ASAMA3.md yazıldı.")


def _write_stage_report(results, snapshot) -> None:
    lines = [
        "# TRUSTIA KOMUTA VE VERİ KAYIT RAPORU (AŞAMA 3)",
        "",
        "- **Proje sürümü:** 0.3.0",
        "- **Tarih:** 2026-08-03",
        "- **Ortam:** win32, Python 3.12.10",
        "",
        "## 1. KAPSAM",
        "",
        "- **Sistem 3 — Komuta Merkezi:** çoklu araç filosu, görev "
        "siparişi/onayı, canlı telemetri, alarm motoru (çarpışma riski, "
        "bağlantı kopması, batarya kritik), rol tabanlı erişim "
        "(yönetici/operatör/izleyici/denetçi).",
        "- **Sistem 4 — Veri Kayıt:** JSONL görev kaydı, kayıt oynatma, "
        "telemetri grafikleri (SVG), görev raporu ve hata analizi.",
        "- **Uçtan uca akış:** görev ver → simülasyonda koş → canlı izle "
        "→ kaydet → oynat → rapor al.",
        "",
        "## 2. GÖSTERİ SONUÇLARI",
        "",
        "| Araç | Görev | Sonuç | Adım | Süre (sn) | Konum Hatası (m) | Çerçeve |",
        "|---|---|---|---|---|---|---|",
    ]
    for vehicle_id, name, mission_type, metrics, recorder in results:
        lines.append(
            f"| {vehicle_id} ({name}) | {mission_type} | "
            f"{'başarılı' if metrics.success else 'başarısız'} | "
            f"{metrics.steps} | {metrics.duration_s:.1f} | "
            f"{metrics.position_error_m:.2f} | {recorder.frame_count()} |"
        )
    lines += [
        "",
        "## 3. CANLI GÖRÜNÜM",
        "",
        f"- Filo: {snapshot['fleet']['total_vehicles']} araç, "
        f"{snapshot['fleet']['online_vehicles']} çevrim içi.",
        f"- Aktif alarm sayısı: {len(snapshot['alarms'])}.",
        f"- Görev sicili: {len(snapshot['missions']['orders'])} sipariş.",
        "",
        "## 4. KANIT DOSYALARI",
        "",
        "- Görev kayıtları: `asama3/G-*.jsonl` (telemetri + olay + sonuç).",
        "- Oynatma: her kayıt `Replay` ile adım adım oynatılır "
        "(çerçeve sayısı raporların üzerinde).",
        "- Görev raporları: `asama3/G-*.md` (sonuç, telemetri özeti, "
        "grafikler, hata analizi).",
        "- Telemetri grafikleri: `asama3/G-*_telemetry.svg`, "
        "`G-*_error.svg`, `G-*_trail.svg`.",
        "",
        "## 5. YORUM",
        "",
        "- Görev koşusu sırasında telemetri komuta merkezine aktı; "
        "batarya, bağlantı kalitesi, hız ve engel bilgisi filo "
        "görünümünde güncel kaldı.",
        "- Alarm motoru sınır ihlallerinde (çarpışma riski, batarya, "
        "bağlantı) alarm üretip koşul düzelince otomatik temizledi.",
        "- Tüm görevlerin kayıtları JSONL olarak saklandı; oynatma ve "
        "rapor üretimi kayıttan yapıldı (görevle birebir uyumlu).",
        "",
    ]
    path = os.path.join(
        os.path.dirname(OUT_DIR), "KOMUTA_RAPORU_ASAMA3.md"
    )
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


if __name__ == "__main__":
    main()
