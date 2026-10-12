"""
TRUSTIA AI — Kurumsal B2B Otonomi SDK Paketi Üreticisi (Enterprise SDK Packager).
Seviye-4 Otonom Sürüş Çekirdeği (v2.4).

Bu araç; müşteriye giden teslimat paketini TÜM GEREKSİZ ŞEYLERDEN (menüler, .bat dosyaları,
MetaDrive simülasyonları, kişisel ve askeri modüller) tamamen arındırır.
SADECE VE SADECE aracın beynine kurulacak kapalı, derlenmiş saf otonom sürüş motorunu (SDK) paketler.
"""

from __future__ import annotations

import os
import sys
import shutil
import zipfile
import py_compile
import compileall
import argparse
import json
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.licensing import LicenseManager


SDK_MODULES = [
    "core",
    "slam",
    "planning",
    "control",
    "integration",
    "perception",
    "security",
    "v2x",
    "ai"
]

README_CONTENT = """# TRUSTIA LEVEL-4 AUTONOMOUS DRIVING CORE (ENTERPRISE SDK v2.4)

Trustia Seviye-4 Otonom Sürüş Çekirdeği, elektrikli ve otonom araç platformları
için geliştirilmiş kapalı devre, yüksek emniyetli (ISO 26262 ASIL-D) bir sürüş motorudur.

---

## 1. KURULUM

```bash
# SDK paketinin bulunduğu dizinde çalıştırın:
pip install -e .
```

---

## 2. ARAÇ ENTEGRASYONU (PYTHON KODU)

Araç bilgisayarınızdaki (NVIDIA Drive Orin / Linux x86_64) otonom servisinizde
motoru tek satırla başlatabilirsiniz:

```python
from trustia import AutonomyCore

# 1. Otonom sürüş motorunu başlat
vehicle = AutonomyCore(config_file="config/vehicle_config.yaml")
status = vehicle.start()
print("Otonomi Durumu:", status)

# 2. Araca hedef koordinat ata
vehicle.set_target(x=150.0, y=75.0, heading=0.0)

# 3. Anlık telemetriyi oku
telemetry = vehicle.get_telemetry()
print("Araç Hızı:", telemetry["speed_kmh"])

# 4. Görev bittiğinde emniyetle durdur
vehicle.stop()
```

---

## 3. YAPILANDIRMA

Tüm araç, LiDAR ve CAN-FD parametreleri `config/vehicle_config.yaml` dosyasından
yönetilir. Kod içinde herhangi bir değişiklik yapılmasına gerek yoktur.

---

## 4. DESTEK VE LİSANS
* **Sağlayıcı:** Trustia AI Technologies
* **Eser Sahibi:** Murat Furkan Bayram
* **İletişim:** iletisim@trustia.com.tr
"""


def build_enterprise_sdk(
    client_name: str,
    hardware_lock: str = "ANY",
    expiry_date: str = "LIFETIME",
    max_vehicles: str = "UNLIMITED",
    output_dir: str = ""
):
    print("=" * 80)
    print("  TRUSTIA AI — SAF KURUMSAL B2B OTONOMİ SDK PAKETLEYİCİ")
    print("  Teslimat: SADECE YAZILIM MOTORU (SIFIR MENÜ • SIFIR OYUN • SIFIR .py)")
    print("=" * 80)

    if not output_dir:
        output_dir = str(Path.home() / "Desktop")

    os.makedirs(output_dir, exist_ok=True)
    staging = PROJECT_ROOT / "staging_enterprise_sdk"
    if staging.exists():
        shutil.rmtree(staging)
    os.makedirs(staging, exist_ok=True)

    sdk_root = staging / "Trustia_L4_Autonomy_SDK"
    trustia_pkg = sdk_root / "trustia"
    os.makedirs(trustia_pkg, exist_ok=True)

    print("\n[1/4] Saf Otonomi Modülleri Kopyalanıyor ve Derleniyor...")
    # 1. Kök __init__.py derle
    root_init = PROJECT_ROOT / "__init__.py"
    py_compile.compile(str(root_init), str(trustia_pkg / "__init__.pyc"), optimize=2)

    # 2. Saf otonomi modüllerini derle
    for mod in SDK_MODULES:
        src_mod = PROJECT_ROOT / mod
        dst_mod = trustia_pkg / mod
        if src_mod.exists():
            shutil.copytree(src_mod, dst_mod, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc"))
            compileall.compile_dir(str(dst_mod), force=True, legacy=True, optimize=2, quiet=1)

    print("\n[2/4] Tüm Açık .py Kaynak Dosyaları İmha Ediliyor...")
    deleted_py = 0
    for root, dirs, files in os.walk(trustia_pkg):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"), ignore_errors=True)
            dirs.remove("__pycache__")
        for f in files:
            fp = Path(root) / f
            if f.endswith(".py"):
                fp.unlink()
                deleted_py += 1

    print(f"  * Tamamen Temizlenen .py Dosyası: {deleted_py} adet (Kodlar %100 gizlendi)")

    print("\n[3/4] Müşteri Belgeleri, Konfigürasyon ve Lisans Ekleniyor...")
    # Config klasörü
    cfg_dst = sdk_root / "config"
    os.makedirs(cfg_dst, exist_ok=True)
    shutil.copy2(PROJECT_ROOT / "config" / "vehicle_config.yaml", cfg_dst / "vehicle_config.yaml")

    # README ve EULA
    with open(sdk_root / "README.md", "w", encoding="utf-8") as rf:
        rf.write(README_CONTENT)
    shutil.copy2(PROJECT_ROOT / "COMMERCIAL_EULA.md", sdk_root / "COMMERCIAL_LICENSE.txt")
    shutil.copy2(PROJECT_ROOT / "pyproject.toml", sdk_root / "pyproject.toml")

    # Lisans
    if hardware_lock.lower() == "current":
        hardware_lock = LicenseManager.get_hardware_fingerprint()

    lic_data = LicenseManager.create_license(
        client_name=client_name,
        hardware_lock=hardware_lock,
        expiry_date=expiry_date,
        max_vehicles=max_vehicles
    )
    LicenseManager.save_license_file(lic_data, str(sdk_root / "trustia.lic"))

    print(f"  * Lisans Sahibi    : {lic_data['client_name']}")
    print(f"  * Donanım Kilidi   : {lic_data['hardware_lock']}")

    print("\n[4/4] Kurumsal ZIP Paketleniyor...")
    zip_path = os.path.join(output_dir, "Trustia_L4_Autonomy_Core_v2.4.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(sdk_root):
            for f in files:
                fp = Path(root) / f
                rel = fp.relative_to(staging)
                zf.write(fp, rel)

    shutil.rmtree(staging, ignore_errors=True)
    zip_size_mb = os.path.getsize(zip_path) / (1024 * 1024)

    print("=" * 80)
    print("  SAF KURUMSAL OTONOMİ SDK'SI BAŞARIYLA ÜRETİLDİ!")
    print("=" * 80)
    print(f"  Dosya : {zip_path}")
    print(f"  Boyut : {zip_size_mb:.2f} MB")
    print(f"  İçerik: %100 SAF YAZILIM KÜTÜPHANESİ (SIFIR .bat, SIFIR MENÜ)")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Trustia Pure Enterprise SDK Builder")
    parser.add_argument("--client", default="Kurumsal Alıcı ve Ortak A.Ş.", help="Müşteri adı")
    parser.add_argument("--hw-lock", default="ANY", help="Donanım kilidi")
    parser.add_argument("--expiry", default="LIFETIME", help="Geçerlilik süresi")
    parser.add_argument("--vehicles", default="UNLIMITED", help="İzin verilen araç sayısı")
    parser.add_argument("--outdir", default="", help="Çıktı klasörü")

    args = parser.parse_args()
    build_enterprise_sdk(
        client_name=args.client,
        hardware_lock=args.hw_lock,
        expiry_date=args.expiry,
        max_vehicles=args.vehicles,
        output_dir=args.outdir
    )


if __name__ == "__main__":
    main()
