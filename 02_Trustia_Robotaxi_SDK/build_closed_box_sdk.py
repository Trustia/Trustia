"""
TRUSTIA Robotaksi SDK — Kapalı Kutu (Closed-Box .pyc Bytecode) Dağıtım Paketleyicisi.

Müşteriye veya iş ortaklarına (Tripy Mobility / MİA Teknoloji vb.) Gizlilik Sözleşmesi (NDA)
kapsamında gönderilecek deneme paketini üretir.
Açık kaynak (.py) dosyalarını pakete KESİNLİKLE dahil etmez; yalnızca derlenmiş (.pyc)
ikili modülleri, yapılandırma dosyalarını (.yaml, .dbc) ve doğrulama araçlarını paketler.
"""

from __future__ import annotations

import os
import py_compile
import shutil
import zipfile
from pathlib import Path


def build_closed_box_robotaxi_sdk() -> Path:
    sdk_root = Path(__file__).resolve().parent
    dist_dir = sdk_root / "dist"
    staging_dir = dist_dir / "Trustia_Robotaxi_SDK_ClosedBox"

    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True, exist_ok=True)

    # 1. trustia_sdk içindeki tüm .py dosyalarını .pyc olarak derle (kaynak kodu kopyalama!)
    src_pkg = sdk_root / "trustia_sdk"
    dst_pkg = staging_dir / "trustia_sdk"

    for py_file in src_pkg.rglob("*.py"):
        rel = py_file.relative_to(src_pkg)
        target_pyc = (dst_pkg / rel).with_suffix(".pyc")
        target_pyc.parent.mkdir(parents=True, exist_ok=True)
        py_compile.compile(str(py_file), cfile=str(target_pyc), doraise=True)

    # 2. Config, CAN-FD DBC, Docs, GUI ve Test/Çalıştırma betiklerini kopyala
    for folder in ["canbus", "config", "docs", "gui", "tests"]:
        s_folder = sdk_root / folder
        if s_folder.exists():
            shutil.copytree(s_folder, staging_dir / folder, dirs_exist_ok=True)

    for file_name in [
        "README.md",
        "CALISTIR_TESTLER.bat",
        "CALISTIR_KOKPIT.bat",
        "CALISTIR_DRIVE_LOOP.bat",
    ]:
        s_file = sdk_root / file_name
        if s_file.exists():
            shutil.copy2(s_file, staging_dir / file_name)

    # 3. Zip arşivi oluştur
    zip_path = dist_dir / "Trustia_Robotaxi_Evaluation_SDK_ClosedBox.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in staging_dir.rglob("*"):
            if file_path.is_file():
                zf.write(file_path, file_path.relative_to(staging_dir))

    return zip_path


if __name__ == "__main__":
    out = build_closed_box_robotaxi_sdk()
    print(f"[TAMAMLANDI] Kapalı Kutu Robotaksi SDK Paketi Üretildi: {out}")
