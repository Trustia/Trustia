"""
TRUSTIA Sistem 4 - Görev Sonu Rapor Üreticisi Birim Testi.
"""

import os
import pytest
from record.report_generator import MissionReportGenerator


def test_mission_report_generator(tmp_path):
    out_file = str(tmp_path / "test_report.md")
    res = MissionReportGenerator.generate_markdown_report(
        mission_id="G-TEST-001",
        mission_type="devriye",
        duration_s=120.0,
        distance_m=150.5,
        avg_speed_mps=1.25,
        threats_count=2,
        output_path=out_file,
    )
    assert os.path.exists(res)
    with open(res, "r", encoding="utf-8") as f:
        text = f.read()
    assert "G-TEST-001" in text
    assert "150.50 Metre" in text
