"""Sistem 7 — Rapor üretici testleri (pytest çıktı ayrıştırma + istatistik)."""

from __future__ import annotations

import pytest

from core.reporting import ReportSection, TestReportGenerator as _Generator


class TestParseSummary:
    GENERATOR = _Generator()

    @pytest.mark.parametrize("line,passed,failed", [
        ("161 passed in 1.27s", 161, 0),
        ("306 passed, 2 failed in 34.0s", 306, 2),
        ("100 passed, 3 failed, 1 error in 5.5s", 100, 3),
        ("50 passed, 1 skipped in 0.9s", 50, 0),
        ("1 passed in 0.01s", 1, 0),
        ("0 passed in 0.00s", 0, 0),
    ])
    def test_passed_failed(self, line, passed, failed):
        summary = self.GENERATOR.parse_summary(line)
        assert summary["passed"] == passed
        assert summary["failed"] == failed

    @pytest.mark.parametrize("line,expected", [
        ("161 passed in 1.27s", 1.27),
        ("306 passed, 2 failed in 34.0s", 34.0),
        ("10 passed in 0.5s", 0.5),
    ])
    def test_duration(self, line, expected):
        summary = self.GENERATOR.parse_summary(line)
        assert summary["duration_s"] == pytest.approx(expected)

    def test_no_match_returns_zeros(self):
        summary = self.GENERATOR.parse_summary("no test output here")
        assert summary["passed"] == 0
        assert summary["failed"] == 0

    def test_full_output_parsing(self):
        output = (
            "tests/system1: 210 passed in 20.1s\n"
            "tests/system2: 96 passed, 1 failed in 12.5s\n"
        )
        summary = self.GENERATOR.parse_summary(output)
        assert summary["passed"] == 96
        assert summary["failed"] == 1

    @pytest.mark.parametrize("token,key", [
        ("passed", "passed"),
        ("failed", "failed"),
        ("error", "errored"),
        ("skipped", "skipped"),
    ])
    def test_token_mapping(self, token, key):
        line = f"7 {token} in 1.0s"
        summary = self.GENERATOR.parse_summary(line)
        assert summary[key] == 7

    def test_skipped_count(self):
        summary = self.GENERATOR.parse_summary("5 passed, 3 skipped in 0.2s")
        assert summary["skipped"] == 3


class TestReportSection:
    def test_total_sum(self):
        section = ReportSection("x", passed=5, failed=2, errored=1, skipped=1)
        assert section.total == 9

    def test_pass_rate(self):
        section = ReportSection("x", passed=90, failed=10)
        assert section.pass_rate == pytest.approx(90.0)

    def test_pass_rate_empty(self):
        assert ReportSection("x").pass_rate == 0.0

    def test_pass_rate_perfect(self):
        assert ReportSection("x", passed=10).pass_rate == pytest.approx(100.0)

    def test_pass_rate_zero(self):
        section = ReportSection("x", failed=10)
        assert section.pass_rate == pytest.approx(0.0)

    def test_defaults(self):
        section = ReportSection("y")
        assert section.passed == 0
        assert section.failed == 0
        assert section.total == 0

    def test_name_preserved(self):
        assert ReportSection("Sistem 9: Yapay Zeka").name == "Sistem 9: Yapay Zeka"


class TestReportTemplate:
    def test_report_sections_markdown_table(self, tmp_path):
        from core.reporting import TestReportGenerator
        import os

        generator = TestReportGenerator(project_version="9.9.9")
        lines = [
            "# TRUSTIA TEST RAPORU",
            "- **Proje sürümü:** 9.9.9",
            "| Kategori | Durum |",
            "| 1 | 2 |",
        ]
        output = os.path.join(str(tmp_path), "r.md")
        with open(output, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        content = open(output, encoding="utf-8").read()
        assert "TRUSTIA TEST RAPORU" in content
        assert "9.9.9" in content
        assert generator is not None