# 🛠️ TRUSTIA — DONANIM MİMARİSİ VE PARÇA LİSTESİ (BILL OF MATERIALS - BOM)

**Doküman Tarihi:** Eylül 2026  
**Amaç:** Fiziksel bir insansız kara aracı (İKA) prototipi veya donanım entegrasyonu yapmak isteyen mühendislik ekibi için satın alınacak standart endüstriyel parça listesi.

---

## 1. ARAÇ İÇİ BEYİN VE BİLGİSAYAR DONANIMI (EDGE COMPUTER)

| Parça Adı | Önerilen Model / Özellik | Adet | Tahmini Maliyet | Kullanım Amacı |
|---|---|---|---|---|
| **Endüstriyel Otonomi Bilgisayarı** | NVIDIA Jetson AGX Orin Industrial (64GB RAM) veya Advantech ARK-2250R | 1 | $1,800 - $2,500 | TRUSTIA Otonomi Beyninin (`python`) çalıştığı ana bilgisayar |
| **CAN-Bus Arabirim Modülü** | Kvaser Leaf Light v2 CAN-to-USB veya Peak PCAN-USB | 1 | $250 - $350 | Araç motor/direksiyon CAN hattı ile bilgisayar bağlantısı |
| **Endüstriyel Güç Kaynağı** | Mean Well SD-100A-12 (12V/24V DC-DC Dönüştürücü) | 1 | $60 - $100 | Bilgisayar ve sensörlerin voltaj regülasyonu |

---

## 2. ALGI VE TEHDİT SENSÖRLERİ (SENSORS)

| Parça Adı | Önerilen Model / Özellik | Adet | Tahmini Maliyet | Kullanım Amacı |
|---|---|---|---|---|
| **3D LiDAR Lazer Tarayıcı** | Hesai Pandar XT-32 veya Ouster OS1-32 (32 Kanal, 120m) | 1 | $3,500 - $5,000 | SLAM haritalama ve engel algılama |
| **Termal Kızılötesi Kamera** | FLIR Boson 640 (LWIR, 640x512, USB/Ethernet) | 1 | $1,500 - $2,200 | Gece/gündüz zemin ısıl anomali ve insan/araç tespiti |
| **Metal Dedektörü Bobini** | CEIA CMD Askeri Mayın Arama Bobini veya Vallon VMR3 | 1 | $800 - $1,500 | Toprak altı metal ve EYP indüksiyon algılama |
| **GPR Radar (Yere Nüfuz Eden)** | Impulse Radar PinPoint GPR / IDS GeoRadar | 1 | $2,000 - $3,500 | Toprak altı derinlik yansıması ve plastik mayın tespiti |
| **KHKN / CBRN Gaz Sensörü** | Mirion RDS-31 (Radyasyon) + Smiths Chemical Sniffer | 1 | $1,200 - $2,000 | Kimyasal ve radyolojik tehlike tespiti |

---

## 3. SÜRÜŞ AKTUATÖRLERİ (DRIVE-BY-WIRE ACTUATORS)

*(Not: Eğer aracınız vites ve direksiyonu zaten elektronikse bu parçalara gerek yoktur.)*

| Parça Adı | Önerilen Model / Özellik | Adet | Tahmini Maliyet | Kullanım Amacı |
|---|---|---|---|---|
| **Direksiyon Aktüatörü** | Linak LA36 Endüstriyel Lineer Aktüatör veya Kinetek Servo | 1 | $300 - $500 | Direksiyonu fiziksel olarak döndürme |
| **Fren / Gaz Aktüatörü** | Stroke Lineer Piston (12V DC, 500N) | 2 | $150 - $250 | Fren pedalına fiziksel basma |

---

## 4. TOPLAM DONANIM MALİYET ÖZETİ

* **Temel Otonomi Paketi (Bilgisayar + CAN + LiDAR + Kamera)**: ~$5,500 - $8,000 USD
* **Tam Askeri EYP/Mayın/KHKN İzolasyon Paketi**: ~$10,000 - $15,000 USD

Bu donanım parçaları satın alınıp araca vidalandığında, projenizdeki **`TRUSTIA`** yazılımı tam teşekküllü fiziksel bir askeri otonom robota dönüşür!
