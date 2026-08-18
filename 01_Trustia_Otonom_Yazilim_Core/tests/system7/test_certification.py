"""AŞAMA 6 — Sertifikasyon denetim aracı testleri."""

from __future__ import annotations

import os

import pytest

from core.certification import (
    CertificationAudit,
    ChecklistItem,
    DependencyReport,
    DEV_TOOLS,
    LOCAL_PACKAGES,
)


def _make_repo(tmp_path):
    """İç içe yerel paket + stdlib importlu sentetik depo üretir."""
    root = tmp_path / "depo"
    root.mkdir()
    (root / "core").mkdir()
    (root / "core" / "__init__.py").write_text("", encoding="utf-8")
    (root / "core" / "modul.py").write_text(
        "import math\nimport os\nfrom core import modul2\n", encoding="utf-8"
    )
    (root / "core" / "modul2.py").write_text(
        "from dataclasses import dataclass\n", encoding="utf-8"
    )
    (root / "tests").mkdir()
    (root / "tests" / "test_x.py").write_text(
        "import pytest\n\ndef test_a():\n    assert True\n",
        encoding="utf-8",
    )
    return root


class TestDependencyScan:
    def test_stdlib_imports_detected(self, tmp_path):
        root = _make_repo(tmp_path)
        report = CertificationAudit(str(root)).scan_dependencies()
        assert "math" in report.stdlib
        assert "os" in report.stdlib
        assert "dataclasses" in report.stdlib

    def test_local_package_excluded(self, tmp_path):
        root = _make_repo(tmp_path)
        report = CertificationAudit(str(root)).scan_dependencies()
        assert "core" not in report.third_party
        assert report.scanned_files == 4

    def test_dev_tool_separated(self, tmp_path):
        root = _make_repo(tmp_path)
        report = CertificationAudit(str(root)).scan_dependencies()
        assert "pytest" in report.dev_tools
        assert "pytest" not in report.product_external
        assert report.fully_local

    def test_fully_local_true_without_third_party(self):
        report = DependencyReport(stdlib={"math", "os"})
        assert report.fully_local
        assert report.product_external == set()

    def test_fully_local_false_with_third_party(self):
        report = DependencyReport(
            stdlib={"math"}, third_party={"numpy"}
        )
        assert not report.fully_local
        assert report.product_external == {"numpy"}

    def test_empty_repo(self, tmp_path):
        root = tmp_path / "bos"
        root.mkdir()
        report = CertificationAudit(str(root)).scan_dependencies()
        assert report.scanned_files == 0
        assert report.fully_local

    def test_generated_dirs_skipped(self, tmp_path):
        root = _make_repo(tmp_path)
        (root / ".venv").mkdir()
        (root / ".venv" / "lib.py").write_text("import numpy\n", encoding="utf-8")
        (root / "__pycache__").mkdir()
        (root / "__pycache__" / "c.py").write_text("import numpy\n", encoding="utf-8")
        report = CertificationAudit(str(root)).scan_dependencies()
        assert "numpy" not in report.third_party
        assert "numpy" not in report.product_external


class TestLineCount:
    def test_count_lines(self, tmp_path):
        root = _make_repo(tmp_path)
        audit = CertificationAudit(str(root))
        assert audit.line_count() >= 6

    def test_comments_and_blanks_excluded(self, tmp_path):
        root = tmp_path / "d"
        root.mkdir()
        (root / "a.py").write_text(
            "# yorum\n\nx = 1\n# baska\n\n", encoding="utf-8"
        )
        assert CertificationAudit(str(root)).line_count() == 1

    def test_empty_dir_zero(self, tmp_path):
        root = tmp_path / "b"
        root.mkdir()
        assert CertificationAudit(str(root)).line_count() == 0


class TestChecklist:
    def test_item_defaults(self):
        item = ChecklistItem("şart", "kanıt", True)
        assert item.requirement == "şart"
        assert item.met

    def test_items_have_evidence_paths(self):
        items = CertificationAudit(".").requirement_checklist()
        assert len(items) >= 8
        for item in items:
            assert item.requirement
            assert item.evidence

    def test_checklist_contains_required_sharts(self):
        items = CertificationAudit(".").requirement_checklist()
        names = " ".join(i.requirement for i in items)
        assert "JAUS" in names
        assert "Denetim" in names
        assert "GPS" in names


class TestConstants:
    def test_local_packages_known(self):
        assert "core" in LOCAL_PACKAGES
        assert "simulation" in LOCAL_PACKAGES

    def test_dev_tools_known(self):
        assert "pytest" in DEV_TOOLS

    def test_stdlib_not_empty(self):
        assert len(LOCAL_PACKAGES) >= 8


class TestReport:
    def test_generate_markdown_structure(self, tmp_path):
        root = _make_repo(tmp_path)
        output = os.path.join(str(tmp_path), "rapor.md")
        path = CertificationAudit(str(root)).generate_markdown(output)
        assert path == output
        content = open(output, encoding="utf-8").read()
        assert "SERTİFİKASYON" in content
        assert "YERLİ KATKI" in content
        assert "KONTROL LİSTESİ" in content

    def test_report_shows_fully_local(self, tmp_path):
        root = _make_repo(tmp_path)
        output = os.path.join(str(tmp_path), "rapor.md")
        CertificationAudit(str(root)).generate_markdown(output)
        content = open(output, encoding="utf-8").read()
        assert "%100" in content