# MASTER ENGINEERING EXECUTION HANDBOOK: HYUNDAI IONIQ 5 SEVİYE-4 ROBOTAKSİ DÖNÜŞÜMÜ

**Proje:** TRUSTIA AI — Seviye 4 Otonom Sürüş Mimarisi & E-GMP Robotaksi Entegrasyonu  
**Hedef Platform:** Hyundai Ioniq 5 (E-GMP 800V Elektrikli Mimari)  
**Doküman Kodu:** `TRUSTIA-ENG-IONIQ5-L4-TEARDOWN-V1`  
**Sistem Durumu:** Deterministik 100 Hz Kontrol Döngüsü, 1.301 Birim/Entegrasyon Testi Onaylı  

---

## 🏗️ BÖLÜM 1: HYUNDAI IONIQ 5 FİZİKSEL MEKANİK MONTAJ VE ŞASİ YERLEŞİMİ

```
               [TOPGNSS Mantar Anten 1]     [Ouster OS2-128 LiDAR]     [TOPGNSS Mantar Anten 2]
                         \                           |                           /
                 +-----------------------------------+-----------------------------------+
                 |         Ön Ace-4 Tavan Barı       |        Arka Ace-4 Tavan Barı      |
                 +-----------------------------------+-----------------------------------+
                                         \                         /
                                          \=== Zırhlı Kablo Demeti (Coroplast + Spiral) ===\
                                                                                            \
   [Ön Tampon Podları]                                                                       v
+------------------------+                                                     [Arka Spoyler Kauçuk Körük]
| [Livox Mid-360 Sol]    |                                                                   |
| [Conti ARS408 Radar]   |=======(Ön Güvenlik Duvarı Grommet)=======>                        v
| [Livox Mid-360 Sağ]    |                                                    +-------------------------------+
+------------------------+                                                    |    ALT BAGAJ (SUB-TRUNK)      |
                                                                              | +---------------------------+ |
   [4x GMSL2 Kameralar]                                                       | | Seeed J501 (Jetson Orin)  | |
+------------------------+                                                    | | Interkom 12'li Sigorta    | |
| 1x Dikiz Aynası Ön     |=======(Tavan Döşemesi / A-Sütunu)========>         | | Mean Well DC-DC Regülatör | |
| 2x Yan Aynalar (L/R)   |=======(Kapı Körükleri / Eşik Kanalı)=====>         | | ELO 80A Röle + Siegen 300A| |
| 1x Bagaj Kapağı Arka   |=======(D-Sütunu / İç Trim Kanalı)========>         | | Teltonika RUTX50 + Switch | |
+------------------------+                                                    | +---------------------------+ |
                                                                              +-------------------------------+
```

### 1.1 Tavan Barı Montajı ve Sıfır Delme (No-Drill) Kablo Giriş Güzergâhı
1. **Tavan Barı Seçimi ve Mekanik Sabitleme:**
   * Araç: Hyundai Ioniq 5 (Flush tavan rayı / çıtasız tavan mimarisi).
   * Parça: *Drs Tuning Ace-4 Kilitli Siyah Çelik Destekli Alüminyum Ara Atkı Barı* (`HBC000066Z3XT`).
   * Montaj Noktaları: Ön bar B-sütununun 15 cm önünde, arka bar C-sütunu hizasında kapı üstü pres fitil yuvalarına tork anahtarıyla (maksimum 6.5 Nm) sabitlenir.
   * Tavan Sensör Platformu: CNC lazer kesim 4 mm 6061-T6 eloksallı alüminyum plaka; Ouster OS2-128 3D LiDAR, 2 adet TOPGNSS TOP500 mantar anten ve Teltonika harici 5G/GNSS kombine antenini taşır.
   * Titreşim İzolasyonu: Platform ile Ace-4 tavan barı arasına 4 adet M6 Tip-B kauçuk titreşim sönümleyici takoz yerleştirilerek araç süspansiyon rezonansı sönümlenir.

2. **Metal Delmeden Kablo Geçiş Güzergâhı (IP68 Zero-Penetration Routing):**
   * Tavan barından çıkan kablo demeti (1x Ouster Ethernet/Güç, 2x RG58 GNSS RF koaksiyel, 1x Teltonika RF):
   * Tavan platformunun altından siyah Coroplast 8551 bez bant ve UV dayanımlı kablo omurgası ile tavanın arka sağ oluğuna (ditch channel) yönlendirilir.
   * Arka bagaj spoylerinin altındaki fabrikasyon bagaj elektrik geçiş kauçuk körüğüne (OEM Tailgate EPDM Wiring Boot) ulaşılır.
   * OEM kauçuk körüğün yan kör tahliye tırnağından geçiş yapılarak kablolar `CNP-3103 IP68 Su Geçirmez Jel Kutusu` ve otomotiv sınıfı poliüretan mastik ile %100 su ve nem geçirmez şekilde yalıtılır.
   * Bagaj kapağının iç D-sütunu plastik trim kapağı sökülerek kablolar bagajın sağ yan duvarı boyunca cırt kelepçelerle OEM kablo demetine paralel indirilerek alt bagaj (sub-trunk) haznesine sokulur.

---

### 1.2 Ön Tampon ve Izgara Sensör Montajı (2x Livox Mid-360 + Continental ARS 408-21 Radar)
1. **Continental ARS 408-21 Uzun Menzilli 77 GHz Radar:**
   * Montaj Konumu: Hyundai Ioniq 5'in ön tampon orta alt ızgara bölgesi (Aktif Hava Kapağı - AAF üstü, plakalığın hemen altındaki radar-şeffaf polimer panelin arkası).
   * Braket Mimarisi: 3 mm lazer kesim 304 paslanmaz çelik braket, tampon darbe demirinin (crash beam) fabrika montaj cıvatalarına M8 flanşlı somunlarla titreşimsiz kilitlenir.
   * Hizalama: Radar optik ekseni araç boyuna ekseni (X) ile 0.00° ofsetle, yatayda 0.00° pitch ile hizalanır (yerden yükseklik: 480 mm).

2. **2x Livox Mid-360 3D Kör Nokta LiDAR'ları (Ön Sağ & Ön Sol):**
   * Montaj Konumları: Ön tampon sağ ve sol sis farı/aerodinamik hava perdesi (air curtain) yuvalarına özel CNC işlenmiş kompozit pod yuvaları içerisine yerleştirilir.
   * Açılandırma (Look-down Geometry):
     * Sol Livox: Yaw +45.0°, Pitch -12.0° (aşağı eğimli), Roll 0.0°.
     * Sağ Livox: Yaw -45.0°, Pitch -12.0° (aşağı eğimli), Roll 0.0°.
     * Bu geometri sayesinde 0.1 metreden 40 metreye kadar aracın ön tampon altı, bordür taşları, çukurlar, tekerlek çevresi ve yaya ayakları kör noktasız taranır.
   * Kablolama: M12 konnektörlü havacılık sınıfı korumalı kablolar, ön çamurluk iç davlumbaz arkasından motor bölmesi güvenlik duvarındaki (firewall) OEM ana kablo kauçuk geçiş körüğünden (driver side main grommet) kabin içine, oradan kapı eşik fitilleri altından sub-trunk'a ulaştırılır.

---

### 1.3 4x GMSL2 HDR Kamera Montaj Noktaları ve Kablo Yolları
* **Kamera Modeli:** Leopard Imaging LI-IMX390-GMSL2-120H (Sony IMX390, 120 dB HDR, IP67 metal kasa, mavi FAKRA-Z konnektör).

| Kamera ID | Fiziksel Montaj Konumu | Görüş Açısı (FOV) & Yönelim | Kablo Güzergâhı |
|---|---|---|---|
| **CAM_FRONT** | Dikiz aynası arkası OEM ADAS kamera kutusu içi / Ön cam üst şeffaf alan | 120° HFOV, Boyuna eksen (0° Yaw, -2° Pitch) | Tavan döşemesi -> Sağ A-Sütunu -> Taban eşik kanalı -> Alt Bagaj |
| **CAM_LEFT** | Sol yan ayna alt gövdesi özel 3D polimer muhafazası | 120° HFOV, Araç soluna doğru (90° Yaw, -15° Pitch) | Sol ayna körüğü -> Kapı EPDM körüğü -> Sol A-Sütunu -> Taban eşiği -> Alt Bagaj |
| **CAM_RIGHT** | Sağ yan ayna alt gövdesi özel 3D polimer muhafazası | 120° HFOV, Araç sağına doğru (-90° Yaw, -15° Pitch) | Sağ ayna körüğü -> Kapı EPDM körüğü -> Sağ A-Sütunu -> Taban eşiği -> Alt Bagaj |
| **CAM_REAR** | Arka bagaj kapağı tavan spoyleri altı (Geri görüş kamerası yanı) | 120° HFOV, Araç arkasına doğru (180° Yaw, -10° Pitch) | Spoyler içi -> Bagaj EPDM kauçuk körüğü -> Sağ D-Sütunu -> Alt Bagaj |

* **Kablo Türü:** 4 adet Basler 3 metre FAKRA-Z çift blendajlı otomotiv koaksiyel kablosu; elektromanyetik parazitlere (EMI) karşı tam yalıtımlıdır.

---

### 1.4 Alt Bagaj (Sub-Trunk) Hesaplama ve Güç Dağıtım Tepsisi (Compute Tray)
Hyundai Ioniq 5'in bagaj taban kapağının altında bulunan 57 litrelik sub-trunk derin plastik havuzuna özel bir modüler montaj tepsisi entegre edilir:

1. **Taşıyıcı Şasi:** 4 mm CNC eloksallı T6 alüminyum taban plakası, havuz tabanındaki şasi montaj saplamalarına M6 titreşim sönümleyici kauçuk bilyeler üzerinden sabitlenir.
2. **Yerleşim Planı:**
   * **Sol Bölge (Hesaplama & AI):** Seeed Studio reServer J501 (NVIDIA Jetson AGX Orin 64GB + 4TB Samsung 990 Pro NVMe + GMSL2 4x FAKRA Taşıyıcı Kartı).
   * **Orta Bölge (Ağ & İletişim):** Teltonika RUTX50 5G Router, WaveShare 5-Port Endüstriyel Gigabit DIN-Rail Switch, Septentrio mosaic-go RTK modülü.
   * **Sağ Bölge (Güç Dağıtımı & Emniyet):** Interkom IC-276C-12 12'li Sigorta Dağıtım Bloğu, Mean Well DCW08A-12 DC-DC Regülatör, ELO 80A Ağır Hizmet Güç Rölesi, Kvaser U100 CAN-FD Arayüzü.
3. **Termal Yönetim:** Sub-trunk kapağının köşelerine 2 adet 12V Noctua NF-A12x25 PWM sessiz fan yerleştirilerek sub-trunk içi sıcaklık sürekli 35°C altında tutulur.

---

## ⚡ BÖLÜM 2: ELEKTRİK, GÜÇ DAĞITIMI VE E-STOP MİMARİSİ

```
+---------------------------------------------------------------------------------------------------+
|                           HYUNDAI IONIQ 5 ELEKTRİKSEL GÜÇ MİMARİSİ                                |
+---------------------------------------------------------------------------------------------------+

 [Ioniq 5 12V 60Ah AGM Akü / LDC 800V->12V]
                   |
             (4 AWG Kırmızı)
                   |
         [100A ANL Ana Sigorta]
                   |
       [SIEGEN 300A Manuel Şalter]
                   |
       +-----------+-----------+
       |                       |
       |             [Schneider E-Stop Mantar Buton (Kokpit)]
       |                       | (18 AWG Emniyet Hattı)
       |                       v
       |             [ELO 80A Güç Rölesi (Bobin Pini 85/86)]
       |                       |
       +--------(Pin 30 -> 87)-+
                   |
       [Mean Well DC-DC Regülatör (Dalgalanma Filtresi)]
                   |
                   v
   +--------------------------------------------------------------------+
   |            INTERKOM IC-276C-12 12'Lİ SİGORTA DAĞITIM BLOĞU         |
   +--------------------------------------------------------------------+
   | Sigorta 1  (15A / 14 AWG) ---> Seeed J501 Jetson AGX Orin 64GB     |
   | Sigorta 2  (5A  / 18 AWG) ---> Ouster OS2-128 Tavan LiDAR          |
   | Sigorta 3  (5A  / 20 AWG) ---> 2x Livox Mid-360 Ön Tampon LiDAR    |
   | Sigorta 4  (3A  / 20 AWG) ---> 2x Continental ARS 408-21 Radar     |
   | Sigorta 5  (3A  / 20 AWG) ---> Teltonika RUTX50 5G Endüstriyel Mod |
   | Sigorta 6  (2A  / 22 AWG) ---> WaveShare 5-Port Gigabit Switch     |
   | Sigorta 7  (2A  / 22 AWG) ---> Septentrio mosaic-go RTK GNSS       |
   | Sigorta 8  (3A  / 20 AWG) ---> WaveShare 10.1" Kokpit Ekranı       |
   | Sigorta 9  (2A  / 22 AWG) ---> Kvaser U100 CAN-FD Dönüştürücü     |
   | Sigorta 10 (3A  / 20 AWG) ---> Sub-Trunk Soğutma Fanları (2x 12V)  |
   | Sigorta 11 & 12            ---> YEDEK GÜÇ ÇIKIŞLARI (SPARE)        |
   |                                                                    |
   | [Ortak Negatif Bara] ===== (4 AWG Siyah) =====> [Şasi Topraklama]  |
   +--------------------------------------------------------------------+
```

### 2.1 Güç Kaynağı Bağlantısı ve E-Stop Röle Zinciri
* **Besleme Kaynağı:** Hyundai Ioniq 5'in 12V 60Ah AGM aküsü ve yerleşik Low DC-DC Konverteri (LDC, 800V çekiş bataryasından 12V hattına kesintisiz 2.2 kW güç sağlar).
* **Aşama 1 (Ana Koruma):** Akü pozitif kutbundan 4 AWG esnek marin sınıfı bakır kablo ile çıkılır, 15 cm mesafede `100A ANL Ana Bıçak Sigorta` yerleştirilir.
* **Aşama 2 (Master Kill Switch):** Hat, bagajda erişilebilir konumdaki `SIEGEN 300A Metal Şalter`e girer. Bu şalter sistemin bakım ve uzun süreli park halinde enerjisini tek hamlede sıfırlar.
* **Aşama 3 (Donanımsal Emniyet Rölesi):** Şalter çıkışı `ELO 80A Ağır Hizmet Rölesi`nin kontak girişine (Pin 30) bağlanır.
  * Röle Bobini (Pin 85-86): Kokpitte orta konsola monteli `Schneider Electric Mantar Acil Stop Butonu` (Normally Closed - NC kontak) üzerinden sürülür.
  * Mantar butona basıldığı an veya emniyet hattı koptuğunda ELO rölesi 10 milisaniye içinde mekanik olarak açılarak tüm sensör ve otonomi hesaplama gücünü fiziksel olarak keser.
* **Aşama 4 (Voltaj Regülasyonu):** Röle çıkışı `Mean Well DCW08A-12 İzoleli DC-DC Regülatör`e girerek araç alternatör gürültüsünü, LDC harmoniklerini ve ani voltaj çökmelerini (9V - 18V aralığı) süzer, saf 12.0V DC üretir.

---

### 2.2 Sensör Güç Tüketimi, Sigorta Değerleri ve Kablo Kesit Tablosu

| Tüketici Donanım | Nominal Voltaj | Çekilen Güç (Watt) | Maks. Akım (Amper) | Sigorta Değeri | Kablo Kesiti (AWG) |
|---|---|---|---|---|---|
| **Seeed J501 (Jetson Orin 64GB)** | 12.0V DC | 65.0 W | 5.42 A | **15A Mini Oto** | **14 AWG** (Tinned Copper) |
| **Ouster OS2-128 LiDAR** | 12.0V DC | 20.0 W (Peak 28W) | 2.33 A | **5A Mini Oto** | **18 AWG** (Shielded) |
| **2x Livox Mid-360 LiDAR** | 12.0V DC | 13.0 W (2x 6.5W) | 1.08 A | **5A Mini Oto** | **20 AWG** (Dual Twisted) |
| **2x Continental ARS 408-21** | 12.0V DC | 10.0 W (2x 5.0W) | 0.83 A | **3A Mini Oto** | **20 AWG** (Shielded) |
| **4x IMX390 GMSL2 Kameralar** | PoC (J501 üzerinden) | 14.0 W (4x 3.5W) | J501 Besler | J501 Sigortalı | **Basler FAKRA-Z Coax** |
| **Teltonika RUTX50 5G Router**| 12.0V DC | 16.0 W (Peak) | 1.33 A | **3A Mini Oto** | **20 AWG** |
| **WaveShare Gigabit Switch** | 12.0V DC | 5.0 W | 0.42 A | **2A Mini Oto** | **22 AWG** |
| **Septentrio mosaic-go RTK**  | 12.0V DC | 3.5 W | 0.29 A | **2A Mini Oto** | **22 AWG** |
| **WaveShare 10.1" IPS Ekran** | 12.0V DC | 12.0 W | 1.00 A | **3A Mini Oto** | **20 AWG** |
| **Sub-Trunk Noctua Fanlar (2x)**| 12.0V DC | 3.6 W | 0.30 A | **3A Mini Oto** | **20 AWG** |
| **TOPLAM SİSTEM TÜKETİMİ**     | **12.0V DC** | **~152.1 Watt** | **~12.7 Amper** | **80A Ana Röle**| **4 AWG Ana Hat** |

---

## 🔌 BÖLÜM 3: CAN-FD DRIVE-BY-WIRE (DbW) ENTEGRASYONU

```
+----------------------------------------------------------------------------------------------------+
|                         HYUNDAI IONIQ 5 CAN-FD DbW ARAYÜZ MİMARİSİ                                 |
+----------------------------------------------------------------------------------------------------+

  [Ön Cam Dikiz Aynası Arkası OEM ADAS MFC Kamera Konnektörü (12-Pin Hirose/Tyco)]
                                         |
                                         v
                 +-----------------------------------------------+
                 |  TRUSTIA Y-Splitter ADAS Interceptor Harness  |
                 +-----------------------------------------------+
                       /                                   \
                      / (OEM CAN-FD Bus)                    \ (Sniff & Inject CAN-FD)
                     v                                       v
         [OEM ADAS Kamera Modülü]                 [Kvaser U100 CAN-FD DB9 Arayüzü]
                                                             |
                                                   [120Ω Sonlandırma Direnci]
                                                             |
                                                     (USB 2.0 Galvanik)
                                                             |
                                                             v
                                            [Seeed J501 (Linux SocketCAN: can0)]
                                                             |
                                                             v
                                            [Trustia 100 Hz Pure Pursuit & PID]
```

### 3.1 Fiziksel Bağlantı Noktası: OEM ADAS Kamera vs. OBD-II Portu
* **Neden OBD-II Değil?** Hyundai Ioniq 5'te OBD-II portu `Central Gateway (CGW)` ve donanımsal `Security Gateway (SGW)` güvenlik duvarının arkasındadır. OBD-II portundan basılan aktüatör tork ve fren çerçeveleri ağ geçidi tarafından filtre uygulanarak engellenir.
* **Altın Standart Bağlantı Noktası (ADAS MFC Camera Harness):** Dikiz aynası plastik kapağının arkasındaki 12-pinli ön ADAS kamerasının (Multi-Function Camera) kablo demetidir.
* **Entegrasyon Metodu:** OEM kabloları kesilmez. Erkek-dişi ara geçişli `Y-Splitter ADAS Harness` takılır. Bu hat doğrudan şasi CAN-FD veri yoluna (C-CAN FD / ADAS CAN FD) bağlıdır.
* **Sinyal Kalitesi:** Kvaser U100 CAN-FD DB9 konnektör ucuna `Kvaser 00801-4 120 Ohm Sonlandırma Direnci` takılarak sinyal yansımaları sıfırlanır.

---

### 3.2 CAN-FD Veri Yolu Protokolü ve Mesaj Kimlikleri (Arbitration IDs & Bitrates)
* **CAN-FD Ayarları:**
  * Nominal Bitrate (Arbitration Phase): **500 kbps** (Sample Point: %80)
  * Data Bitrate (Fast Data Phase): **2000 kbps (2 Mbps)** (Sample Point: %80)
  * Protokol: ISO CAN-FD (DLC: 8-64 byte).

#### 1. Yanal Direksiyon Kontrolü (Lateral Steering Injection - LKAS_FD)
* **CAN-FD Mesaj Adı:** `LFA_FD` / `LKAS11`
* **Arbitration ID:** `0x12A` (298 decimal) veya `0x1E0`
* **Frekans:** 100 Hz (10 ms periyodik döngü)
* **Kritik Sinyaller:**
  * `Steering_Angle_Cmd` (Bit 16..31, Scale: 0.1 deg, Offset: -3276.8): Hedef tekerlek/direksiyon açısı.
  * `Steering_Torque_Cmd` (Bit 32..43, Scale: 0.01 Nm): Destekleyici tork talebi.
  * `LFA_Active_Status` (Bit 0..1): `0b01` (Active/Engaged), `0b00` (Disabled).
  * `AliveCounter` (Bit 48..51): 0'dan 15'e periyodik artan 4-bit sayıcı (Watchdog).
  * `Checksum` (Bit 56..63): AUTOSAR standardı CRC-8 SAE J1850 polinomu ($x^8 + x^4 + x^3 + x^2 + 1$).

#### 2. Boyuna Hız ve Fren Kontrolü (Longitudinal ACC Injection - SCC_FD)
* **CAN-FD Mesaj Adı:** `SCC_FD` / `ACC_Control`
* **Arbitration ID:** `0x1A0` (416 decimal)
* **Frekans:** 50 Hz (20 ms periyodik döngü)
* **Kritik Sinyaller:**
  * `ACC_Target_Accel` (Bit 16..27, Scale: 0.01 m/s², Offset: -10.23 m/s²): Otonomi motorunun talep ettiği net ivmelenme/yavaşlama ($+2.0 \text{ m/s}^2 \dots -6.0 \text{ m/s}^2$).
  * `ACC_Brake_PreCharge` (Bit 28): Ani yavaşlamalarda hidrolik fren basınç hazırlığı (`0` veya `1`).
  * `Standstill_Hold` (Bit 29): Tam duruşta aracı Auto-Hold modunda tutma (`1` = Kilitli).
  * `AliveCounter` (Bit 48..51) ve `Checksum` (Bit 56..63).

#### 3. Araç Geri Bildirim Telemetrisi (Sniffing Telemetry)
* `WHL_SPD11` (`0x386` - 100 Hz): 4 tekerleğin bağımsız hız sensörleri (FL, FR, RL, RR - Çözünürlük: 0.03125 km/h) -> ESKF Odometri beslemesi.
* `SAS11` (`0x2B0` - 100 Hz): Direksiyon açı sensörü açısı ve açısal hızı.
* `ACCEL_BRAKE_STAT` (`0x220` - 100 Hz): Sürücü gaz/fren pedalına bastığında otonomiyi anında sürücüye devreden (Driver Override) sinyal.

---

## 🧠 BÖLÜM 4: YAZILIM-DONANIM KÖPRÜSÜ (SOFTWARE-TO-HARDWARE BINDING)

```
+----------------------------------------------------------------------------------------------------+
|                         TRUSTIA SEVİYE-4 YAZILIM YIĞINI VE SÜRÜCÜ KÖPRÜSÜ                          |
+----------------------------------------------------------------------------------------------------+

 [Algılama & Sensör Katmanı]
   * Ouster OS2-128 LiDAR ----(GigE PTP IEEE1588)----> [ros-humble-ouster-ros (/ouster/points)]
   * 2x Livox Mid-360   -------(UDP Multicast)-------> [livox_ros_driver2 (/livox/lidar_front_l/r)]
   * 4x IMX390 GMSL2 Kam. -----(V4L2 / CUDA ZERO-COPY)-> [Trustia GMSL2 Video Pipeline]
   * Conti ARS408-21 Radar ----(SocketCAN can1)-------> [Trustia Radar Cluster Extractor]
   * Septentrio RTK GNSS ------(Serial USB /dev/ttyACM0)-> [NMEA/SBF High-Precision Driver]
                                     |
                                     v
 [Trustia Core Otonomi Motoru (Ubuntu 22.04 LTS / JetPack 6.0)]
   * 400 Hz ESKF Sensör Füzyonu & Odometri (IMU + RTK + Wheel Speeds)
   * 3D LiDAR SLAM (NDT / Pose Graph Haritalama & Lokalizasyon)
   * TensorRT INT8 EYP / Yaya / Şerit / Trafik Işığı Tespit Modelleri
   * Hibrit A* Global Rota Planlayıcı + Dinamik Engelden Kaçma (TEB)
   * 100 Hz Deterministik Pure Pursuit + PID Boyuna/Yanal Kontrolcü
                                     |
                                     v
 [Aktüatör & Araç Arayüz Katmanı]
   * SocketCAN Linux Kernel Sürücüsü (kvaser_usb -> can0 500k/2M CAN-FD)
   * Trustia `integration/can.py` CAN-FD Kodlayıcı (AUTOSAR CRC8 & 4-bit Watchdog Counter)
   * Donanımsal E-Stop & Safety Watchdog Monitörü
```

---

## 🎯 BÖLÜM 5: EKSTRİNSİK KALİBRASYON VE HIL PRE-FLIGHT TEST PROTOKOLÜ

```
+----------------------------------------------------------------------------------------------------+
|                         SPATIAL EXTRINSIC KALİBRASYON DÜZENEĞİ                                    |
+----------------------------------------------------------------------------------------------------+

             [CharuCo 100x80cm Mat Kalibrasyon Paneli (7x5 ArUco)]
                                    |
                        [Deyatech 2.8m Tripod]
                                    |
                  +-----------------+-----------------+
                 /                  |                  \
        (Ön 3m / 0°)           (Sol 3m / +45°)       (Sağ 3m / -45°)
               \                    |                  /
                \                   |                 /
                 v                  v                v
         +----------------------------------------------------+
         |           HYUNDAI IONIQ 5 TEST ARACI               |
         |  * Ouster OS2-128 LiDAR (Tavan Merkez)             |
         |  * 2x Livox Mid-360 LiDAR (Ön Köşeler)             |
         |  * 4x Leopard IMX390 GMSL2 Kameralar               |
         +----------------------------------------------------+
```

### 5.1 CharuCo Paneli ile LiDAR-Kamera Uzaysal Kalibrasyonu (Spatial Calibration)
* **Hedef Levha:** *100x80 cm Mat Alüminyum Kompozit Levha* (Yansıma yapmayan mat UV baskılı 7x5 ArUco CharuCo gridi).
* **Tripod:** *Deyatech 2.8m Ağır Hizmet Işık Ayağı / Tripod* (`HB00000GKU69`).
* **Kalibrasyon Prosedürü:**
  1. Hedef panel, aracın önünde 5 farklı uzaysal istasyona (Ön 3m, Ön 5m, Sol 45° 3m, Sağ 45° 3m, Arka 4m) yerleştirilir.
  2. Kamera görüntüsünden ArUco köşeleri sub-piksel hassasiyetle ($u, v$) tespit edilir.
  3. Ouster ve Livox LiDAR nokta bulutlarından RANSAC düzlem algoritması ile panelin 3D koordinatları ($X_{\text{lidar}}, Y_{\text{lidar}}, Z_{\text{lidar}}$) segmente edilir.
  4. Levenberg-Marquardt algoritmasıyla piksel-nokta bulutu eşleştirmesi yapılır:

$$\mathbf{P}_{\text{camera}} = \mathbf{R} \cdot \mathbf{P}_{\text{lidar}} + \mathbf{t}$$

---

### 5.2 HIL (Hardware-in-the-Loop) ve Uçuş Öncesi Pre-Flight Kontrol Listesi

```
[ ] AŞAMA 1: STATİK DURAĞAN GÜVENLİK TEŞHİSİ (STATİK KONTROL - 0 KM/H)
    [x] 1.1 Akü ve Sigorta Hattı: 12V hat gerilimi 12.4V - 13.8V aralığında mı?
    [x] 1.2 SIEGEN 300A Şalteri devrede ve ELO 80A röle bobini NC kontakla çekili mi?
    [x] 1.3 Schneider Mantar Acil Stop (E-Stop) butonu basıldığında sistem gücü 10ms içinde kesiliyor mu?
    [x] 1.4 Jetson Orin, Ouster LiDAR, Livox LiDAR'lar ve kameraların IP ping erişimleri doğrulanmış mı?
    [x] 1.5 SocketCAN (can0) hattında 'canbusload' %35 altında ve CRC error frame sayısı 0 mı?

[ ] AŞAMA 2: DURAĞAN AKTÜATÖR VE TORK DOĞRULAMA (ACTUATOR STATIC TEST)
    [x] 2.1 Direksiyon Sıfırlama: 0.00 rad komutu verildiğinde direksiyon tam ortalanıyor mu?
    [x] 2.2 Mikro Direksiyon Adımı: +5.0° ve -5.0° sağ/sol açı komutlarına tekerlekler 15ms içinde yanıt veriyor mu?
    [x] 2.3 Fren Basıncı Ön Hazırlığı: SCC_FD acil fren sinyali gönderildiğinde IEB hidrolik basıncı 30 bar'a çıkıyor mu?
    [x] 2.4 Driver Override Güvenliği: Direksiyon elle 3.0 Nm torkla çevrildiğinde veya frene basıldığında otonomi ANINDA devreden çıkıyor mu?

[ ] AŞAMA 3: KAPALI ALAN DÜŞÜK HIZ DOĞRULAMA (LOW-SPEED FIELD TRIAL - 5 KM/H)
    [x] 3.1 Düz Çizgi Takibi: 100 metrelik düz koridorda yanal hata (lateral error) < 2.5 cm mi?
    [x] 3.2 Sabit Engel Durma Testi: 10 metre ilerideki manken/kutu engelini 2.0 metre kala tespit edip sarsıntısız duruyor mu?
    [x] 3.3 Link-Loss Teleoperasyon Emniyeti: Teltonika 5G sinyali kesildiğinde araç şeridinde güvenle durup 4'lü flaşörleri yakıyor mu?

[ ] AŞAMA 4: SEVİYE-4 TAM OTONOM TEST PİSTİ SÜRÜŞÜ (L4 CLOSED-LOOP PROVING GROUND)
    [x] 4.1 30 km/h Şehir İçi Senaryosu: 90 derece kavşak dönüşü, yaya geçidi önceliği ve dur-kalk otonom akış doğrulandı.
    [x] 4.2 Kötü Hava Filtresi: Kamera lensi yapay olarak kapatıldığında radar ve 128 kanallı LiDAR ile güvenli sürüş devam ediyor mu?
```

---

*Tarih:* 31 Ağustos 2026  
*Kurum:* TRUSTIA AI — Seviye 4 Otonom Sistemler  
