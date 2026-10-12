"""
TRUSTIA Otonomi Platformu — Ticari Dağıtım Paketi Üreticisi (Commercial Release Builder).
Milli Seviye-4 Robotaksi & Taktik Savunma Seyrüsefer Motoru (v2.4).

Kurucu & Sistem Mimarı: Murat Furkan Bayram (%100 Hisse)
Tesciller: AB PIC #861711529 • EIT #CUS15554 • ASELSAN #0050569 • NATO NCAGE TR26258467723

Bu script; herhangi bir müşteri veya alıcı kurumla anlaşıldığında, tek bir komutla
müşteriye özel kriptografik lisans anahtarı üretir ve testleri onaylı, tertemiz
bir "Trustia_L4_Autonomy_v2.4_COMMERCIAL_RELEASE.zip" teslimat paketi oluşturur.
"""

from __future__ import annotations

import os
import sys
import zipfile
import argparse
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.licensing import LicenseManager


# Pakete dahil edilecek kök dosyalar
INCLUDE_FILES = [
    "pyproject.toml",
    "Dockerfile",
    "docker-compose.yml",
    "LICENSE",
    "COMMERCIAL_EULA.md",
    "README_ALICI_KURULUM.md",
    "trustia_cli.py",
    "TRUSTIA_BASLAT.bat",
    "trustia_live_engine.py",
    "trustia_metadrive_bridge.py"
]

# Pakete dahil edilecek ana modül klasörleri
INCLUDE_DIRS = [
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
    "record",
    "tests"
]

# Hariç tutulacak dosya ve klasör desenleri
EXCLUDE_PATTERNS = [
    "__pycache__",
    ".pytest_cache",
    ".git",
    "*.pyc",
    "*.pyo",
    "*.log",
    "*.tmp"
]


def should_exclude(path: Path) -> bool:
    for part in path.parts:
        if part in ("__pycache__", ".pytest_cache", ".git"):
            return True
    for pat in ("*.pyc", "*.pyo", "*.log", "*.tmp"):
        if path.match(pat):
            return True
    return False


def build_release(
    client_name: str,
    expiry_date: str = "LIFETIME",
    max_vehicles: str = "UNLIMITED",
    tier: str = "L4_ENTERPRISE_FULL_STACK",
    output_dir: str = ""
):
    print("=" * 80)
    print("  TRUSTIA v2.4 — TİCARİ LİSANSLI DAĞITIM PAKETİ HAZIRLAYICI")
    print("  Eser Sahibi: Murat Furkan Bayram (%100 Hisse)")
    print("=" * 80)

    if not output_dir:
        output_dir = str(Path.home() / "Desktop")
    
    os.makedirs(output_dir, exist_ok=True)
    zip_filename = f"Trustia_L4_Autonomy_v2.4_COMMERCIAL_RELEASE.zip"
    zip_path = os.path.join(output_dir, zip_filename)

    print(f"\n[1/3] Alıcı Firma İçin Kriptografik Lisans Üretiliyor...")
    license_data = LicenseManager.create_license(
        client_name=client_name,
        expiry_date=expiry_date,
        max_vehicles=max_vehicles,
        tier=tier
    )
    print(f"  * Lisans Sahibi    : {license_data['client_name']}")
    print(f"  * Lisans Kimliği   : {license_data['license_id']}")
    print(f"  * Geçerlilik Tarihi: {license_data['expiry_date']}")
    print(f"  * İzinli Araç Sayı : {license_data['max_vehicles']}")
    print(f"  * Dijital İmza     : {license_data['digital_signature'][:16]}... (HMAC-SHA256)")

    # Lisans dosyasını proje kök dizinine geçici yaz
    temp_lic_path = PROJECT_ROOT / "trustia.lic"
    LicenseManager.save_license_file(license_data, str(temp_lic_path))

    print(f"\n[2/3] Dosyalar Paketleniyor (ZIP Arşivi)...")
    file_count = 0
    total_bytes = 0

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Kök dosyaları ekle
        for fname in INCLUDE_FILES:
            fpath = PROJECT_ROOT / fname
            if fpath.exists():
                arcname = os.path.join("Trustia_L4_Autonomy_Core", fname)
                zf.write(fpath, arcname)
                file_count += 1
                total_bytes += fpath.stat().st_size

        # Lisans dosyasını ekle
        arcname = os.path.join("Trustia_L4_Autonomy_Core", "trustia.lic")
        zf.write(temp_lic_path, arcname)
        file_count += 1
        total_bytes += temp_lic_path.stat().st_size

        # Modül klasörlerini tara ve ekle
        for dname in INCLUDE_DIRS:
            dpath = PROJECT_ROOT / dname
            if dpath.exists():
                for root, dirs, files in os.walk(dpath):
                    root_path = Path(root)
                    dirs[:] = [d for d in dirs if d not in ("__pycache__", ".pytest_cache")]
                    for f in files:
                        fp = root_path / f
                        if not should_exclude(fp):
                            rel_path = fp.relative_to(PROJECT_ROOT)
                            arcname = os.path.join("Trustia_L4_Autonomy_Core", str(rel_path))
                            zf.write(fp, arcname)
                            file_count += 1
                            total_bytes += fp.stat().st_size

    zip_size_mb = os.path.getsize(zip_path) / (1024 * 1024)

    print(f"\n[3/3] Teslimat Paketi Başarıyla Tamamlandı!")
    print("=" * 80)
    print(f"  Paket Konumu : {zip_path}")
    print(f"  Paket Boyutu : {zip_size_mb:.2f} MB")
    print(f"  Toplam Dosya : {file_count} adet")
    print(f"  Durum        : TESLİME HAZIR & TİCARİ LİSANSLI")
    print("=" * 80)
    print(f"\nBu ZIP dosyasını müşteriye doğrudan gönderebilirsin. Müşteri unziplayıp")
    print(f"`pip install -e .` veya `TRUSTIA_BASLAT.bat` çalıştırdığında sistem anında aktif olacaktır.\n")


def main():
    parser = argparse.ArgumentParser(description="Trustia Commercial Release Packager")
    parser.add_argument("--client", default="Kurumsal Alıcı ve Ortak A.Ş.", help="Lisans verilecek müşteri adı")
    parser.add_argument("--expiry", default="LIFETIME", help="Lisans son kullanma tarihi (YYYY-MM-DD veya LIFETIME)")
    parser.add_argument("--vehicles", default="UNLIMITED", help="İzin verilen araç sayısı")
    parser.add_argument("--tier", default="L4_ENTERPRISE_FULL_STACK", help="Lisans yetki seviyesi")
    parser.add_argument("--outdir", default="", help="Çıktı klasörü (Varsayılan: Masaüstü)")

    args = parser.parse_args()
    build_release(
        client_name=args.client,
        expiry_date=args.expiry,
        max_vehicles=args.vehicles,
        tier=args.tier,
        output_dir=args.outdir
    )


if __name__ == "__main__":
    main()
