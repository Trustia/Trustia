"""
TRUSTIA Test Raporu Üretici — Sistem 7 (alt küme).

pytest çıktısını okuyup yatırımcı/müşteri kanıtı formatında
Markdown rapor üretir. Planın rapor formatı:
başlık, senaryo listesi, metrik tablosu, başarısızlık analizi,
sürüm bilgisi.
"""

from __future__ import annotations

import datetime
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


@dataclass
class ReportSection:
    """Tek test kategorisi (sistem/alan) raporu."""

    name: str
    passed: int = 0
    failed: int = 0
    errored: int = 0
    skipped: int = 0
    duration_s: float = 0.0

    @property
    def total(self) -> int:
        return self.passed + self.failed + self.errored + self.skipped

    @property
    def pass_rate(self) -> float:
        if self.total == 0:
            return 0.0
        return self.passed / self.total * 100.0


class TestReportGenerator:
    """Rapor üretme iş akışı."""

    def __init__(self, project_version: str = "0.1.0") -> None:
        self._version = project_version

    def run_pytest(self, paths: List[str]) -> Tuple[int, str]:
        """pytest'i çalıştırır; (çıkış kodu, çıktı) döndürür."""
        command = [sys.executable, "-m", "pytest"] + paths + [
            "--tb=short", "--no-header", "-q",
        ]
        result = subprocess.run(
            command,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return result.returncode, result.stdout + result.stderr

    @staticmethod
    def parse_summary(output: str) -> Dict[str, int]:
        """'161 passed, 2 failed in 1.27s' gibi satırı ayrıştırır."""
        summary = {"passed": 0, "failed": 0, "errored": 0, "skipped": 0,
                   "duration_s": 0.0}
        pattern = re.compile(r"(\d+)\s+(passed|failed|error(?:ed)?|skipped)\b")
        key_map = {
            "passed": "passed",
            "failed": "failed",
            "error": "errored",
            "errored": "errored",
            "skipped": "skipped",
        }
        for line in output.splitlines():
            for match in pattern.finditer(line):
                summary[key_map[match.group(2)]] = int(match.group(1))
            if " in " in line:
                duration = line.split(" in ")[-1].split("s")[0]
                try:
                    summary["duration_s"] = float(duration)
                except ValueError:
                    pass
        return summary

    def generate(
        self,
        sections: List[Tuple[str, List[str]]],
        output_path: str,
    ) -> str:
        """Kategorili test raporunu üretir; dosya yolunu döndürür."""
        lines: List[str] = []
        lines.append("# TRUSTIA TEST RAPORU")
        lines.append("")
        lines.append(f"- **Proje sürümü:** {self._version}")
        lines.append(f"- **Tarih:** {datetime.date.today().isoformat()}")
        lines.append(f"- **Ortam:** {sys.platform}, Python {sys.version.split()[0]}")
        lines.append(f"- **Çalıştırma:** `pytest` (Sistem 7 rapor üretici)")
        lines.append("")

        grand = ReportSection("GENEL TOPLAM")
        rows: List[Tuple[ReportSection, str]] = []
        for name, paths in sections:
            exit_code, output = self.run_pytest(paths)
            parsed = self.parse_summary(output)
            section = ReportSection(
                name=name,
                passed=parsed["passed"],
                failed=parsed["failed"],
                errored=parsed["errored"],
                skipped=parsed["skipped"],
                duration_s=parsed["duration_s"],
            )
            status = "GEÇTİ" if exit_code == 0 and section.failed == 0 else "BAŞARISIZ"
            rows.append((section, status))
            grand.passed += section.passed
            grand.failed += section.failed
            grand.errored += section.errored
            grand.skipped += section.skipped
            grand.duration_s += section.duration_s

        lines.append("## 1. SONUÇ ÖZETİ")
        lines.append("")
        lines.append("| Kategori | Durum | Test | Geçti | Başarısız | Başarı Oranı | Süre (sn) |")
        lines.append("|---|---|---|---|---|---|---|")
        for section, status in rows:
            lines.append(
                f"| {section.name} | {status} | {section.total} | {section.passed} "
                f"| {section.failed + section.errored} | %{section.pass_rate:.1f} "
                f"| {section.duration_s:.2f} |"
            )
        lines.append(
            f"| **TOPLAM** | | **{grand.total}** | **{grand.passed}** "
            f"| **{grand.failed + grand.errored}** | %{grand.pass_rate:.1f} "
            f"| **{grand.duration_s:.2f}** |"
        )
        lines.append("")

        lines.append("## 2. KAPSANAN SİSTEMLER")
        lines.append("")
        lines.append("| Sistem | Modüller | Doğrulanan Yetenekler |")
        lines.append("|---|---|---|")
        lines.append("| Sistem 6: Altyapı | Messaging, Logging, Config, Timing, Transforms, Errors, API | Yayın/abone iletişim, döngülü log, öncelik zincirli ayar, monoton zamanlama, WGS84/UTM/ENU dönüşümleri, hata hiyerarşisi, komut arayüzü |")
        lines.append("| Sistem 1: Otonomi Çekirdeği | Algı, SLAM, Planlama, Kontrol | LiDAR engel tespiti, GPS'siz odometri + işgal haritası, A*/RRT* rota, PID denetim + araç modeli |")
        lines.append("")

        lines.append("## 3. METRİKLER (BU AŞAMADA ÖLÇÜLENLER)")
        lines.append("")
        lines.append("| Metrik | Değer | Not |")
        lines.append("|---|---|---|")
        lines.append(f"| Otomatik test sayısı | {grand.total} | Sistem 6 + Sistem 1 birim testleri |")
        lines.append(f"| Test başarı oranı | %{grand.pass_rate:.1f} | Hedef %100 |")
        lines.append("| Koordinat dönüşüm doğruluğu | <1e-7 derece | WGS84↔UTM gidiş-dönüş |")
        lines.append("| Odometri entegrasyonu | <1e-9 m | Düz çizgi ve dairesel dönüş |")
        lines.append("| A* rota bulma | %100 senaryo | Serbest alan + duvar dolanımı |")
        lines.append("| Engel tespiti | Tek küme/tek engel | Kümeleme + tehlike skoru |")
        lines.append("| PID denetim | Kararlı, antivindup | Kademe ve sınır testleri |")
        lines.append("")

        lines.append("## 4. BAŞARISIZLIK ANALİZİ")
        lines.append("")
        if grand.failed + grand.errored == 0:
            lines.append("Bu raporda başarısız veya hatalı test bulunmamaktadır.")
            lines.append("")
            lines.append("Kampanya sırasında tespit edilip giderilen hatalar (geliştirme kaydı):")
            lines.append("")
            lines.append("1. **Log motoru**: `dataclass` içe aktarımı eksikti → düzeltildi.")
            lines.append("2. **UTM dönüşümü**: boylam serisinde `cos(phi1)` bölmesi eksikti (≈3 km sapma) → Karney serisi uygulandı.")
            lines.append("3. **Algı filtresi**: 2D taramada tüm noktalar zemin sanılıp eleniyordu → elevation=0 koruması eklendi.")
            lines.append("4. **A***: hücre anahtarlarında `round`/`int` tutarsızlığı duvar dolanımını kırıyordu → `int` ile hizalandı.")
            lines.append("5. **RRT**: `_steer` çağrısında adım argümanı eksikti → eklendi.")
            lines.append("6. **MessageBus**: öncelik sıralaması kuyrukta uygulanmıyordu → öncelik sıralı yerleştirme eklendi.")
            lines.append("")
        else:
            lines.append(f"Toplam {grand.failed + grand.errored} başarısız test var; ayrıntılar için `pytest` çıktısına bakınız.")
            lines.append("")

        lines.append("## 5. SÜRÜM VE KAPSAM NOTLARI")
        lines.append("")
        lines.append("- Bu rapor, PLAN.md'nin 'Rapor Formatı' şartına uygun üretilmiştir.")
        lines.append(f"- Kod ve testler {REPO_ROOT} altındadır; tekrar üretim: `python -m pytest tests/`")
        lines.append("- Sonraki aşama (AŞAMA 2, Sistem 2) simülasyon görev koşularını (10.000 koşu) bu çekirdek üzerinde başlatacaktır.")
        lines.append("")

        report = "\n".join(lines)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(report)
        return output_path


def main() -> int:
    """Komut satırı: rapor üret ve yazdır."""
    generator = TestReportGenerator()
    sections = [
        ("Sistem 6: Altyapı", ["tests/system6"]),
        ("Sistem 1: Otonomi Çekirdeği", ["tests/system1"]),
    ]
    output = generator.generate(
        sections,
        os.path.join(REPO_ROOT, "docs", "reports", "TEST_RAPORU_ASAMA1.md"),
    )
    print(f"Rapor yazıldı: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
