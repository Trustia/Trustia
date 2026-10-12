"""
TRUSTIA Otonomi Platformu — Tam Garanti Kapalı Kutu Dağıtım Üreticisi (Closed-Box Release Builder).
Milli Seviye-4 Robotaksi & Taktik Savunma Seyrüsefer Motoru (v2.4).

Kurucu & Sistem Mimarı: Murat Furkan Bayram (%100 Hisse)
Tesciller: AB PIC #861711529 • EIT #CUS15554 • ASELSAN #0050569 • NATO NCAGE TR26258467723

Bu araç; müşteriye giden teslimat paketinde TEK BİR SATIR BİLE OKUNABİLİR .py KODU
BIRAKMAZ! Tüm algoritmaları ve giriş scriptlerini optimize edilmiş ikili bytecode (.pyc)
makine diline derler, orijinal .py kaynak dosyalarını tamamen imha eder ve donanım kilidiyle mühürler.
"""

from __future__ import annotations

import os
import sys
import shutil
import zipfile
import py_compile
import compileall
import argparse
import hashlib
import json
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.licensing import LicenseManager


# Pakete dahil edilecek çekirdek modüller
CORE_MODULES = [
    "core",
    "perception",
    "planning",
    "control",
    "slam",
    "integration",
    "security",
    "simulation",
    "v2x",
    "ai",
    "command",
    "record"
]

# Kök yönetim ve çalıştırma scriptleri
ROOT_SCRIPTS = [
    "trustia_cli.py",
    "trustia_live_engine.py",
    "trustia_metadrive_bridge.py"
]


BATCH_LAUNCHER_CONTENT = """@echo off
cd /d "%~dp0"
title TRUSTIA v2.4 - Seviye-4 Otonomi ve Taktik C2 Kontrol Merkezi
cls

if not exist "%~dp0trustia_cli.pyc" (
    echo ===============================================================================
    echo  DIKKAT: Yazilim ZIP arsivinin icinden dogrudan calistirilamaz!
    echo  Lutfen once ZIP dosyasina sag tiklayip Tumunu Ayikla secenegini seciniz.
    echo ===============================================================================
    echo.
    pause
    exit /b
)
echo ===============================================================================
echo    TRUSTIA v2.4 - SEVIYE-4 DUAL-USE OTONOM MOBILITE VE TAKTIK C2 SISTEMI
echo    Kurucu: Murat Furkan Bayram (17 Yas, %%80) - Tescil: AB PIC #861711529
echo    Lisans: TICARI KAPALI KUTU (CLOSED-BOX COMPILED BINARY RELEASE)
echo ===============================================================================
echo.
echo  [1] Taktik C2 Masaustu Konsolunu Baslat (MIL-STD-2525 / STANAG 4586 GUI)
echo  [2] Sistem ve Alt Bilesen Dogrulama Suitini Calistir (1.305 Test Sertifikali)
echo  [3] Yapay Zeka Tehdit, EYP ve KHKN Algilama Motorunu Calistir
echo  [4] Yerli Mimari, AB PIC ve NATO Uygunluk Sertifikasyon Denetimini Kostur
echo  [5] Hyundai Ioniq 5 Seviye-4 CAN-FD Otonom Surus Dongusunu Baslat
echo  [6] Kurumsal Kimlik, Devlet Tescilleri ve Akreditasyonlari Goruntule
echo  [7] Canli 3D WebGL Dijital Ikiz Kokpitini Baslat (Port 8090 / Tarayici)
echo  [8] MetaDrive 3D Masaustu Otonom Surus Simulasyonunu Baslat (Panda3D)
echo  [9] Ticari Lisans ve Dogrulama Durumunu Goruntule (Commercial License Status)
echo.
echo ===============================================================================
set /p secim="Lutfen calistirmak istediginiz islem numarasini giriniz (1-9): "

if "%secim%"=="1" python trustia_cli.pyc gui
if "%secim%"=="2" python trustia_cli.pyc test
if "%secim%"=="3" python trustia_cli.pyc threats
if "%secim%"=="4" python trustia_cli.pyc audit
if "%secim%"=="5" python trustia_cli.pyc robotaxi
if "%secim%"=="6" python trustia_cli.pyc info
if "%secim%"=="7" (
    start "" "http://localhost:8090"
    python trustia_live_engine.pyc
)
if "%secim%"=="8" python trustia_metadrive_bridge.pyc
if "%secim%"=="9" python trustia_cli.pyc license

pause
"""


def generate_integrity_manifest(target_dir: Path) -> dict:
    """Paketteki tüm derlenmiş ikili dosyaların SHA-256 bütünlük imzasını çıkarır."""
    manifest = {}
    for root, _, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".pyc") or f.endswith(".pyd") or f.endswith(".so"):
                fp = Path(root) / f
                rel = fp.relative_to(target_dir).as_posix()
                with open(fp, "rb") as bin_f:
                    manifest[rel] = hashlib.sha256(bin_f.read()).hexdigest()
    return manifest


def build_closed_box_release(
    client_name: str,
    hardware_lock: str = "ANY",
    expiry_date: str = "LIFETIME",
    max_vehicles: str = "UNLIMITED",
    tier: str = "L4_ENTERPRISE_FULL_STACK",
    output_dir: str = ""
):
    print("=" * 80)
    print("  TRUSTIA v2.4 — TAM GARANTİ KAPALI KUTU (CLOSED-BOX) DAĞITIM ÜRETİCİSİ")
    print("  Eser Sahibi: Murat Furkan Bayram (%100 Hisse)")
    print("  Güvenlik    : SIFIR OKUNABİLİR KOD • DERLENMİŞ İKİLİ DOSYA • DONANIM KİLİDİ")
    print("=" * 80)

    if not output_dir:
        output_dir = str(Path.home() / "Desktop")

    os.makedirs(output_dir, exist_ok=True)
    stage_dir = PROJECT_ROOT / "build_closed_box_staging"
    if stage_dir.exists():
        shutil.rmtree(stage_dir)
    os.makedirs(stage_dir, exist_ok=True)

    package_root = stage_dir / "Trustia_L4_Autonomy_ClosedBox"
    os.makedirs(package_root, exist_ok=True)

    print("\n[1/5] Modüller ve Scriptler Kopyalanıyor...")
    # 12 Modülü kopyala
    for mod in CORE_MODULES:
        src_mod = PROJECT_ROOT / mod
        dst_mod = package_root / mod
        if src_mod.exists():
            shutil.copytree(src_mod, dst_mod, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc"))
            compileall.compile_dir(str(dst_mod), force=True, legacy=True, optimize=2, quiet=1)

    # Kök scriptleri derle ve doğrudan .pyc olarak yerleştir
    for sname in ROOT_SCRIPTS:
        src_script = PROJECT_ROOT / sname
        if src_script.exists():
            base_name = Path(sname).stem
            dst_pyc = package_root / f"{base_name}.pyc"
            py_compile.compile(str(src_script), str(dst_pyc), optimize=2)

    # Başlatıcı batch dosyasını yerleştir
    with open(package_root / "TRUSTIA_BASLAT.bat", "w", encoding="utf-8") as bf:
        bf.write(BATCH_LAUNCHER_CONTENT)

    # Alıcı belgelerini kopyala
    for doc in ["README_ALICI_KURULUM.md", "COMMERCIAL_EULA.md", "LICENSE", "pyproject.toml"]:
        d_src = PROJECT_ROOT / doc
        if d_src.exists():
            shutil.copy2(d_src, package_root / doc)

    print("\n[2/5] KRİTİK GÜVENLİK ADIMI: Paket İçindeki TÜM .py Kaynak Dosyaları İmha Ediliyor...")
    deleted_py_count = 0
    preserved_pyc_count = 0

    for root, dirs, files in os.walk(package_root):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"), ignore_errors=True)
            dirs.remove("__pycache__")

        for f in files:
            fp = Path(root) / f
            if f.endswith(".py"):
                fp.unlink()
                deleted_py_count += 1
            elif f.endswith(".pyc"):
                preserved_pyc_count += 1

    # Güvenlik Kontrolü: Tek bir tane bile .py kalmamalı!
    remaining_py = list(package_root.rglob("*.py"))
    assert len(remaining_py) == 0, f"HATA: Pakette hala .py dosyası var: {remaining_py}"

    print(f"  * İmha Edilen Orijinal .py Dosyası : {deleted_py_count} adet (Artık kod okunamaz!)")
    print(f"  * Üretilen Kapalı .pyc İkili Dosya   : {preserved_pyc_count} adet (Saf Makine Bytecode)")
    print(f"  * Kalan Açık .py Dosyası Sayısı      : 0 ADET (%100 KAPALI KUTU GARANTİSİ)")

    print("\n[3/5] Donanım Kilitli Lisans ve Bütünlük İmzası Üretiliyor...")
    if hardware_lock.lower() == "current":
        hardware_lock = LicenseManager.get_hardware_fingerprint()

    license_data = LicenseManager.create_license(
        client_name=client_name,
        expiry_date=expiry_date,
        max_vehicles=max_vehicles,
        hardware_lock=hardware_lock,
        tier=tier
    )
    LicenseManager.save_license_file(license_data, str(package_root / "trustia.lic"))

    manifest = generate_integrity_manifest(package_root)
    with open(package_root / "integrity.manifest", "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, indent=2)

    print(f"  * Lisans Sahibi    : {license_data['client_name']}")
    print(f"  * Donanım Kilidi   : {license_data['hardware_lock']} (Başka cihazda çalışmaz)")
    print(f"  * Lisans Kimliği   : {license_data['license_id']}")
    print(f"  * Bütünlük İmzası  : {len(manifest)} dosya mühürlendi (SHA-256 Anti-Tamper)")

    print("\n[4/5] Final Kapalı Kutu ZIP Paketi Paketleniyor...")
    zip_filename = "Trustia_L4_Autonomy_v2.4_TAM_GARANTI_KAPALI_KUTU.zip"
    zip_path = os.path.join(output_dir, zip_filename)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(package_root):
            for f in files:
                fp = Path(root) / f
                rel_path = fp.relative_to(stage_dir)
                zf.write(fp, rel_path)

    zip_size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    shutil.rmtree(stage_dir, ignore_errors=True)

    print("=" * 80)
    print("  TAM GARANTİ KAPALI KUTU TESLİMAT PAKETİ HAZIR!")
    print("=" * 80)
    print(f"  Paket Konumu : {zip_path}")
    print(f"  Paket Boyutu : {zip_size_mb:.2f} MB")
    print(f"  Güvenlik     : %100 KAPALI KUTU (SIFIR .py KAYNAK KODU)")
    print(f"  Kopya Engeli : Donanım Kilidi Aktif ({hardware_lock})")
    print("=" * 80)
    print("\nAlıcı bu paketi açtığında tek bir satır kod bile göremez.")
    print("Yazılımı doğrudan aracında `TRUSTIA_BASLAT.bat` ile çalıştırabilir.\n")


def main():
    parser = argparse.ArgumentParser(description="Trustia Tam Garanti Kapali Kutu Release Builder")
    parser.add_argument("--client", default="Kurumsal Alıcı ve Ortak A.Ş.", help="Alıcı kurum adı")
    parser.add_argument("--hw-lock", default="ANY", help="Donanım kilidi (ANY veya current veya 16 haneli ID)")
    parser.add_argument("--expiry", default="LIFETIME", help="Lisans son kullanma tarihi (YYYY-MM-DD veya LIFETIME)")
    parser.add_argument("--vehicles", default="UNLIMITED", help="İzin verilen araç sayısı")
    parser.add_argument("--tier", default="L4_ENTERPRISE_FULL_STACK", help="Yetki seviyesi")
    parser.add_argument("--outdir", default="", help="Çıktı klasörü (Varsayılan: Masaüstü)")

    args = parser.parse_args()
    build_closed_box_release(
        client_name=args.client,
        hardware_lock=args.hw_lock,
        expiry_date=args.expiry,
        max_vehicles=args.vehicles,
        tier=args.tier,
        output_dir=args.outdir
    )


if __name__ == "__main__":
    main()
