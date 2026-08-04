# 🛡️ TRUSTIA — Milli Otonomi Platformu (v2.0 Askeri Sınıf)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Build & Tests](https://img.shields.io/badge/Tests-1277%20Passed-brightgreen.svg)]()
[![License](https://img.shields.io/badge/Sertifikasyon-%25100%20Yerli%20Katk%C4%B1-orange.svg)]()
[![Standards](https://img.shields.io/badge/Standards-SAE%20JAUS%20%7C%20STANAG%204586%20%7C%20ROS%202-red.svg)]()

> **GPS'siz ortamlarda çalışan insansız kara araçları (İKA) için tasarlanmış, sıfır dış bağımlılıklı, %100 yerli katkı sertifikasyonu uyumlu askeri otonomi yazılım platformu.**

---

## 📐 1. Genel Mimari (9 Ana Sistem & Gelişmiş Savunma Modülleri)

TRUSTIA platformu, sürücü donanımından komuta merkezine, 3D Pose Graph SLAM'den EYP/Mayın ve KHKN Gaz tespitine kadar 9 entegre alt sistemden oluşur:

```
                            TRUSTIA PLATFORMU
+-------------------------------------------------------------------+
|  SİSTEM 9: Yapay Zeka Algı & Tehdit Tespit Modülleri              |
|            (BombDetector, CbrnDetector, SwarmCoordinator, AirGround)|
+-------------------------------------------------------------------+
|  SİSTEM 1: Otonomi Çekirdeği                                      |
|  +---------------------------------------------------------------+|
|  | ALGI (Gözler)  →  SLAM (Yer bulma)  →  PLANLAMA (Akıl)        ||
|  |                    →  KONTROL (Eller)                         ||
|  +---------------------------------------------------------------+|
+-------------------------------------------------------------------+
|  SİSTEM 8: Araç/Sensör Entegrasyonu (CAN, LiDAR, ROS 2, JAUS, VO) |
+-------------------------------------------------------------------+
|  SİSTEM 2: Simülasyon   |  SİSTEM 3: Komuta Merkezi (Fleet & Voice)|
|  SİSTEM 4: Veri Kayıt   |  SİSTEM 5: Güvenlik (Shield)            |
+-------------------------------------------------------------------+
|  SİSTEM 6: Altyapı (Mesajlaşma, Log, Ayar, Dönüşüm, API, Hata)    |
|  SİSTEM 7: Test & Sertifikasyon Altyapısı                         |
+-------------------------------------------------------------------+
```

---

## 🚀 2. Öne Çıkan Gelişmiş Kabiliyetler

* 📡 **GPS'siz Konumlanma & Haritalama (SLAM)**: ICP2D/3D tarama eşleştirme, Wheel/Visual Odometry ve g2o benzeri Poz Grafı Optimizasyonu (`slam/`).
* 🧠 **Dinamik Rota Planlama**: Kinematik kısıtlı Hybrid A*, RRT*, DWA (Dynamic Window Approach) ve Potansiyel Alan Vektör Engel Kaçınma (`planning/`).
* 💣 **EYP, Mayın & Mühimmat Tespiti**: Metal indüksiyonu, Termal ısı anomalisi ve GPR Radar füzyonlu askeri patlayıcı tespiti & 30m karantina izolasyonu (`ai/bomb_detector.py`).
* ☢️ **KHKN / CBRN Tehdit Analizi**: Radyasyon, Kimyasal Harp Gazı (Sarin/VX) ve Rüzgar Altı Yayılım Karantinası (`ai/cbrn_detector.py`).
* 🐝 **Çoklu İKA & Hava-Kara Sürü Zekası**: Kama, Saf, Kolon, Baklava formasyonlu İKA ve İHA keşif entegrasyonlu hibrit sürü otonomisi (`ai/swarm.py`, `ai/air_ground_swarm.py`).
* 📷 **Kameralı Görsel Odometri (Visual Odometry)**: Çift/tek kamera karelerinden piksel hareket analizi ile kameralı ilerleme hesabı (`slam/visual_odometry.py`).
* 🗣️ **Taktik Sesli Komut Çözümleyici**: Operatörün sesli/metin komutlarını otonom sürüş iradesine çeviren doğal dil işleme katmanı (`command/voice_command.py`).
* 🔒 **Siber Güvenlik & Acil Durum (Shield)**: HMAC-SHA256 imzalı iletişim, Acil Durma (E-Stop), Telsiz Bağlantı Kaybında Otonom Eve Dönüş (LinkLoss / Return-to-Home) (`security/`).
* 🌐 **NATO, SAE & ROS 2 Standart Uyum**: Donanım kilitsiz SAE AS6091 / AS6009 JAUS mesaj seti, CAN 2.0 / CAN FD sürücü katmanı ve ROS 2 Köprü Modülü (`integration/ros2_bridge.py`).

---

## 💻 3. Hızlı Başlangıç

### 1. Tek Tıkla Başlatıcı (Windows)
Klasör içindeki **`TRUSTIA_BASLAT.bat`** dosyasına çift tıklayarak Taktik Masaüstü Konsolunu, Sertifikasyon Denetimini veya Tehdit Analizini anında çalıştırabilirsiniz.

### 2. Komut Satırı (CLI)
```bash
# Taktik Masaüstü Konsolu
python trustia_cli.py gui

# %100 Yerli Katkı AST Sertifikasyon Denetimi
python trustia_cli.py audit

# 1.277 Adet Otomatik Test Süitini Koşturma
python trustia_cli.py test
```
