"""
TRUSTIA Veri Kayıt (Sistem 4) — Görev raporu üretici.

Kaydedilen görevden okunabilir rapor (markdown) üretir: görev
kimliği, sonuç, telemetri özeti, olaylar, alarm zaman çizelgesi ve
hata analizi. Grafikler (SVG) raporla birlikte yazılır — PLAN:
"kayıt oynatma, telemetri grafikleri, görev raporları, hata analizi".
"""

from __future__ import annotations

import html
import os
from typing import List, Optional, Tuple

from record.graphs import export_mission_charts
from record.replay import Replay


class MissionReport:
    """Bir görev kaydını markdown rapora dönüştürür."""

    def __init__(self, replay: Replay, world_size_m: float = 40.0,
                 obstacles: Optional[List[Tuple[float, float, float]]] = None,
                 record_path: str = "") -> None:
        self.replay = replay
        self.world_size_m = world_size_m
        self.obstacles = obstacles or []
        self.record_path = record_path

    def write(self, directory: str, base_name: str = "") -> str:
        """Raporu (markdown) ve grafikleri yazar; rapor yolunu döndürür."""
        os.makedirs(directory, exist_ok=True)
        base_name = base_name or self._default_base_name()
        charts = export_mission_charts(
            directory,
            base_name,
            steps=self.replay.step_numbers(),
            positions=self.replay.positions(),
            world_size_m=self.world_size_m,
            obstacles=self.obstacles,
            speed=self.replay.speeds(),
            battery=self.replay.battery(),
            link=self.replay.link_quality(),
            error=self.replay.position_error(),
        )
        path = os.path.join(directory, f"{base_name}.md")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(self._to_markdown(base_name, charts))
        return path

    # ---- iç ----

    def _default_base_name(self) -> str:
        result = self.replay.result or {}
        return result.get("mission_id", "gorev")

    def _to_markdown(self, base_name: str, charts: list) -> str:
        replay = self.replay
        result = replay.result or {}
        stats = replay.stats()
        meta = replay.metadata
        lines = [
            "# TRUSTIA GÖREV RAPORU",
            "",
            f"- **Kayıt:** `{self.record_path or '-'}`",
            f"- **Çerçeve sayısı:** {stats['frame_count']}",
            "",
            "## 1. SONUÇ",
            "",
        ]
        success = replay.success()
        lines.append(f"| Alan | Değer |")
        lines.append(f"|---|---|")
        lines.append(f"| Görev kimliği | {result.get('mission_id', '-')} |")
        lines.append(f"| Görev tipi | {result.get('mission_type', '-')} |")
        lines.append(f"| Başarı | {'EVET' if success else 'HAYIR'} |")
        if not success:
            lines.append(f"| Başarısızlık nedeni | {result.get('failure_reason', '-')} |")
        lines.append(f"| Süre | {result.get('duration_s', 0.0)} sn |")
        lines.append(f"| Adım | {result.get('steps', 0)} |")
        lines.append(f"| Çarpışma | {'EVET' if result.get('collision') else 'hayır'} |")
        lines.append(f"| GPS'siz konum hatası (ort) | {result.get('position_error_m', 0.0)} m |")
        lines.append(f"| Rota sapması (ort) | {result.get('route_deviation_m', 0.0)} m |")
        lines.append(f"| Engel tepki süresi (ort) | {result.get('reaction_time_s', 0.0)} sn |")
        lines.append("")
        lines.append("## 2. TELEMETRİ ÖZETİ")
        lines.append("")
        lines.append("| Metrik | Değer |")
        lines.append("|---|---|")
        lines.append(f"| Ortalama hız | {stats['mean_speed_mps']} m/s |")
        lines.append(f"| Maksimum hız | {stats['max_speed_mps']} m/s |")
        lines.append(f"| Ortalama konum hatası | {stats['mean_position_error_m']} m |")
        lines.append(f"| Maksimum konum hatası | {stats['max_position_error_m']} m |")
        lines.append(f"| En düşük bağlantı kalitesi | {stats['min_link_quality']} |")
        lines.append(f"| Ortalama batarya | %{stats['mean_battery_percent']} |")
        lines.append("")
        lines.append("## 3. GRAFİKLER")
        lines.append("")
        for chart in charts:
            lines.append(f"![{os.path.basename(chart)}]({os.path.basename(chart)})")
            lines.append("")
        lines.append("## 4. OLAYLAR")
        lines.append("")
        events = replay.event_summary()
        if events:
            lines.append("| Zaman (ns) | Kategori | Mesaj |")
            lines.append("|---|---|---|")
            for event in events:
                lines.append(
                    f"| {event['at_ns']} | {html.escape(event['category'])} "
                    f"| {html.escape(event['message'])} |"
                )
        else:
            lines.append("_Kayıtlı olay yok._")
        lines.append("")
        lines.append("## 5. HATA ANALİZİ")
        lines.append("")
        if success:
            lines.append("Görev başarıyla tamamlandı; hata analizi gerekmedi.")
        else:
            lines.append(self._failure_analysis(result))
        lines.append("")
        return "\n".join(lines)

    def _failure_analysis(self, result: dict) -> str:
        reason = result.get("failure_reason", "bilinmiyor")
        steps = result.get("steps", 0)
        deviation = result.get("route_deviation_m", 0.0)
        error_m = result.get("final_position_error_m", 0.0)
        if reason == "çarpışma":
            return (
                f"Kök neden: araç bir engelle çarpıştı (adım {steps}). "
                f"Kaçınma penceresi daraldı veya sensör gürültüsü "
                f"engeli gizledi."
            )
        if reason == "yasak bölge ihlali":
            return (
                f"Kök neden: yasak bölgeye giriş (adım {steps}). "
                f"Yasak bölge itmesi sınırda yetersiz kaldı."
            )
        if reason == "süre aşımı":
            return (
                f"Kök neden: süre limiti doldu (adım {steps}). "
                f"Görev ortamı tahmin edilenden yoğundu; "
                f"rota sapması {deviation:.2f} m."
            )
        if reason == "saha dışı":
            return (
                f"Kök nedeni: araç dünya sınırından çıktı (adım {steps}). "
                f"Sınır itmesi yetersizdi; son konum hatası {error_m:.2f} m."
            )
        if reason == "sıkışma":
            return (
                f"Kök neden: araç sıkıştı (adım {steps}); "
                f"kurtarma manevraları başarısız oldu."
            )
        return f"Başarısızlık nedeni: {reason} (adım {steps})."
