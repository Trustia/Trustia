# 🛠️ TRUSTIA — DONANIM MİMARİSİ VE PARÇA LİSTESİ (BILL OF MATERIALS - BOM)
### (HYUNDAI IONIQ 5 SEVİYE-4 ROBOTAKSİ & DUAL-USE TAKTİK İKA DONANIM KİTİ)

**Doküman Tarihi:** Eylül 2026 (Sürüm 2.4 — Doğrulandı)  
**Hedef Platform:** Hyundai Ioniq 5 (E-GMP 800V Mimarisi) & Taktik Askeri İKA Şasileri  
**Donanım Lideri:** Denizcan Özcan (ASELSAN Aday Mühendis Havuzu, İÜC EEE 3.44 GPA)  
**Tedarik Durumu:** %100 Doğrulanmış Canlı Tedarikçi Sepeti  

---

## 1. 27 PARÇALIK SEVİYE-4 DONANIM VE SENSÖR BOM TABLOSU

| Alt Sistem / Bileşen | Marka / Model / Teknik Özellik | Tedarikçi / Dağıtıcı | Birim Tutar (TL) | Görev & Entegrasyon |
|---|---|---|---|---|
| **Çatı 3D LiDAR** | Ouster OS2-128 Rev 7 (128 Kanal, 200m+, 360°) | Leo Drive Teknoloji | **351.258,60 TL** | 3D NDT Pose Graph SLAM, otoyol & kentsel derinlik algılama |
| **Kör Nokta LiDAR (2x)** | Livox Mid-360 Katı Hal LiDAR (360° x 59°) | Orbi Elektronik | **232.730,40 TL** | Ön sağ/sol tampon bordür, çukur, yaya ve kör nokta tespiti |
| **Merkezi Yapay Zeka** | Seeed reServer J501 + NVIDIA Jetson AGX Orin 64GB (275 TOPS) | Seeed Studio | **181.470,15 TL** | 16.000 satır otonomi çekirdeği, TensorRT derin öğrenme, 100Hz döngü |
| **ROS2 Rosbag SSD** | Samsung 990 PRO 4TB NVMe SSD (7450 MB/s) | PTTAVM / Tulparlife | **50.220,00 TL** | 128-LiDAR nokta bulutu ve telemetri yüksek hızlı veri kaydı |
| **GMSL2 Kameralar (4x)** | Leopard Sony IMX390 HDR Otomotiv Kamerası | Mouser Electronics | **98.351,00 TL** | Trafik ışıkları, şerit çizgileri, yol tabelaları ve yaya tespiti |
| **77 GHz Radarlar (2x)** | Continental ARS 408-21 Uzun Menzilli Radar | Alibaba / Continental | **59.345,00 TL** | Yoğun sis, sağanak yağış ve çöl kum fırtınasında 250m menzil |
| **RTK GNSS + IMU** | Septentrio mosaic-go Dual Anten Heading + IMU | Digi-Key / e-komponent | **52.084,00 TL** | Santimetre hassasiyetinde küresel konum ve açısal hız |
| **5G & V2X Router** | Teltonika RUTX50 Çift SIM Endüstriyel 5G/V2X | Hepsiburada / ESET | **35.349,00 TL** | Sub-20ms canlı C2 telemetrisi, MQTT ve teleoperasyon köprüsü |
| **CAN-FD Arabirimi** | Kvaser U100 Galvanik İzoleli CAN-FD USB | Elektronomi | **24.213,00 TL** | Hyundai Ioniq 5 LKAS_FD ve SCC_FD 5 Mbps kontrol veriyolu |
| **Kokpit Ekranı** | WaveShare 10.1 inç Kapasitif HDMI Dokunmatik Ekran | Trendyol / ERNPAZAR | **21.118,00 TL** | Kabin içi yolcu görev durumu, rota haritası ve telemetri |
| **Mekanik & Güç Dağıtımı** | Tavan Barı, ELO 80A Röle, Mean Well DC-DC Regülatör | Yerli Üretim / Bosch | **114.029,28 TL** | Titreşim sönümleyici tavan plakası, 12V/24V regüle güç dağıtımı |
| **TOPLAM DONANIM BOM** | **27 Parçalık Eksiksiz Seviye-4 Anahtar Teslim Kiti** | **Onaylı Distribütörler** | **1.148.829,43 TL (~$23.800)** | **48 Saatte Şasiyi Delmeden Tak-Çalıştır Dönüşüm** |

---

## 2. DUAL-USE (SAVUNMA VE SİVİL) UYUMLULUK

1. **Sivil Robotaksi Mimarisi**: Hyundai Ioniq 5 800V E-GMP platformunda 18 dakikada ultra hızlı şarj ve 24 saat kesintisiz filo operasyonu.
2. **Askeri Taktik İKA Mimarisi**: IP68/IP69K sızdırmazlık standartları, MIL-STD zırhlı kablaj ve NATO STANAG 4586 uyumlu mesajlaşma protokolü ile taktik kara platformlarına doğrudan entegre edilebilir.

