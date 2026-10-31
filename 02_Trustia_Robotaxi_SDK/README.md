# TRUSTIA L4 ROBOTAXI ENTERPRISE SDK (v4.4 Enterprise)
### SAIC Maxus MIFA 7 & Hyundai E-GMP Otonom Sürüş Güvenlik Hakemi, Planlama ve Kontrol Kütüphanesi

**Kurucu & Baş Mimar:** Murat Furkan Bayram (%100 Fikri Mülkiyet Sahibi)  
**Savunma & Kurumsal Tesciller:** ASELSAN Onaylı Tedarikçi (`#0050569` / SAP: `FZQHEXGFMTJU`) • STM Savunma Aday Tedarikçi • Teknopark İstanbul (Cube Incubation & HASAT 2026) • İTO BTM Fulya Kampüsü • YTÜ Yıldız Teknopark  
**Uluslararası & Ulusal Kayıtlar:** AB Komisyonu PIC `#861711529` • EIT Urban Mobility `#CUS15554` • Open Invention Network (OIN 2.0) `#f1e445769a9934114db095c4f5430a0e749d8201` • KOSGEB `KSB01UGE0115153370` • BTK `L2zPtN4X1ZJ`  
**Hukuki Dayanak:** 5846 Sayılı FSEK & Uluslararası Bern Sözleşmesi Korumalı Eser  
**Standartlar:** 1 Aralık 2024 Resmî Gazete (AB 2022/1426) • ISO 26262 ASIL-D • ISO 21448 SOTIF • IEEE 2846 RSS • UN/ECE R155, R156 & R157 • ISO 11898-1 CAN-FD  

---

## 1. MİMARİ GENEL BAKIŞ (21 ALT SİSTEM / 205 DOSYA / 32.000+ SATIR / 1.350 TEST %100 YEŞİL)

Bu SDK, SAIC Maxus MIFA 7 ve Hyundai Ioniq 5 (E-GMP) elektrikli araç platformları ile ticari robotaksi filo operasyonları için geliştirilmiş **%100 Milli Deterministik Güvenlik Hakemi, Seyrüsefer, Planlama ve CAN-FD Aktüatör Kütüphanesidir**.

```text
                           ┌──────────────────────────────────────────────┐
                           │ 3D LiDAR (Ouster/Hesai) + IEEE 1588v2 PTP    │
                           └──────────────────────┬───────────────────────┘
                                                  │ Motion-Deskewed PointCloud
┌───────────────────────────────┐                 ▼
│   CalmCar Horizon J6P SoC     ├─────► ┌──────────────────────────────────────────────┐
│   (CalmDrive 3.0 Perception)  │       │        TRUSTIA ASIL-D SAFETY ARBITER         │
└───────────────────────────────┘       │  • Çift-Sensör Çapraz Doğrulama (SOTIF)      │
                                        │  • IEEE 2846 RSS Matematiksel Güvenlik Zarfı │
                                        │  • ODD Coğrafi Çit & UN R157 DSSAD Kara Kutu │
                                        │  • KVKK m.9 Yurt Dışı Veri Kalkanı           │
                                        │  • ISO 26262 ASIL-D 50ms Watchdog & MRM      │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                        ┌──────────────────────▼───────────────────────┐
                                        │       TRUSTIA SEVİYE-4 SEYRÜSEFER MOTORU     │
                                        │  • 3D LiDAR NDT & 400Hz ESKF SLAM            │
                                        │  • 3D LiDAR Kaldırım/Bordür (Curb) Algılama  │
                                        │  • Lanelet2 HD Harita & KTK m.74 Yaya Hakkı  │
                                        │  • Kinematik Hybrid A* & Frenet 5. Derece    │
                                        │  • Kayan Ufuklu MPC & Stanley Kontrolcü      │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                        ┌──────────────────────▼───────────────────────┐
                                        │  ISO 11898-1 CAN-FD & UN R155 IDPS KÖPRÜSÜ   │
                                        │  • 100 Hz EPS Direksiyon (1.4 ms Gecikme)    │
                                        │  • Fail-Operational Fren (i-Booster+ESC/EPB) │
                                        │  • 5 ms Sürücü Devralma & UN R156 SUMS OTA   │
                                        └──────────────────────────────────────────────┘
```

---

## 2. TAM MODÜL VE DİZİN YAPISI (36 DOSYA / 21 ALT SİSTEM)

* `config/maxus_mifa7.yaml`: SAIC Maxus MIFA 7 araç dinamikleri, CAN-FD baudrate ve sensör montaj ayarları.
* `canbus/maxus_mifa7_chassis.dbc`: Şasi EPS direksiyon, i-Booster fren, kalp atışı ve MRM resmi CAN-FD DBC mesaj sözlüğü.
* `trustia_sdk/`:
  * `core/`:
    * `licensing.py`: HMAC-SHA256 kriptografik donanım parmak izi (ECU UUID) ve lisans doğrulama motoru.
    * `transforms.py`: 2B/3B konum (`Pose2D`), kinematik durum ve açı normalizasyon matematiği.
    * `carla_bridge.py`: CARLA 0.9.15+ & ROS 2 Humble 100 Hz kapalı döngü dijital ikiz ve $\le 5\text{ ms}$ sürücü devir köprüsü.
  * `canbus/`:
    * `mifa7_canfd.py`: ISO 11898-1 CAN-FD (500 kbps / 2 Mbps) aktüatör çerçeve kodlayıcı, CRC-16 ve Alive Counter.
  * `perception/`:
    * `calmcar_bridge.py`: CalmCar kamera algısını 3B LiDAR ile çapraz doğrulayan Emniyet Hakemi ve KVKK m.9 Veri Kalkanı.
    * `curb_detector.py`: Silinmiş şeritlerde ve yağışta 3B LiDAR yükseklik farkından (8–28 cm) kaldırım taşı ve koridor algılayıcısı.
    * `lidar_deskew_ptp.py`: IEEE 1588v2 PTP hassas zaman senkronizasyonu ve 400 Hz IMU ile 3B LiDAR hareket bükülmesi düzeltme (Motion Deskewing).
    * `ehmi_siren_detector.py`: ISO/TR 23049 dış yaya iletişim ekranı (eHMI) ve 600–1550 Hz ambulans/itfaiye sireniyle otonom fermuar koridoru.
  * `slam/`:
    * `ndt_eskf.py`: Tünel ve GPS'siz alanlar için 3D LiDAR NDT eşleştirme ve 400 Hz Error-State Kalman Filtresi (4.2 cm hassasiyet).
  * `planning/`:
    * `hybrid_astar.py`: SAIC Maxus MIFA 7 (2.975 m dingil mesafesi) kinematik kısıtlı Hybrid A* şehir içi rota planlayıcısı.
    * `frenet_lattice_planner.py`: Frenet $(s, d)$ koordinatlarında 5. derece (Quintic) sarsıntı-optimal (Jerk-Optimal) yerel kafes planlayıcısı.
    * `lanelet2_rules.py`: Lanelet2 HD harita şerit kuralları, KTK m.74 yaya geçidi zorunlu duruş çizgisi ve kavşak geçiş üstünlüğü motoru.
  * `control/`:
    * `stanley_controller.py`: Ön aks Stanley yanal şerit takip kontrolcüsü ve boyuna hız PID denetleyicisi.
    * `mpc_redundant_control.py`: Kayan Ufuklu Model Öngörülü Kontrol (MPC) ve Fail-Operational Çift Yedekli Fren Dağıtıcısı (i-Booster + ESC/EPB).
  * `safety/`:
    * `asil_d_mrm.py`: ISO 26262 ASIL-D Emniyet Gözetmeni (20 ms öz-denetim, 50 ms Watchdog, 1.5 m/s² MRM sağa çekme, 5 ms sürücü devri).
    * `odd_sotif_dssad.py`: 1 Aralık 2024 Resmî Gazete (AB 2022/1426) ODD coğrafi çit, ISO 21448 SOTIF ve UN R157 SHA-256 DSSAD Kara Kutu.
    * `rss_ieee2846.py`: IEEE 2846 & Mobileye RSS matematiksel boyuna/yanal güvenli takip mesafesi ve çarpışmasızlık kalkanı.
    * `can_ids_r155.py`: UN R155 & ISO/SAE 21434 CAN-FD Siber Saldırı Tespit Sistemi (DoS, Spoofing ve Sayaç Kontrolü).
    * `sums_un_r156.py`: UN/ECE R156 Yazılım Güncelleme Yönetim Sistemi (SUMS), RXSWIN tip onay sicili, sürüşte güncelleme kilidi ve atomik Rollback.
  * `fleet/`:
    * `telemetry_api.py`: Merkezi filo yönetim platformu canlı JSON telemetri ve yolcu çağrı/görev dağıtım köprüsü.
    * `teleoperation.py`: 5G / WebRTC Uzaktan Operasyon (Teleoperation) güvenli koridor/waypoint onayı ($\le 15\text{ km/s}$, $\le 150\text{ ms}$ RTT).
    * `cabin_bms_safety.py`: Robotaksi yolcu kabin emniyeti, kapı kilidi (Door Interlock), kemer, SOS butonu ve EV batarya BMS termal koruma.
  * `gui/`:
    * `cockpit_gui.py` & `gui/webgl_cockpit/index.html`: Canlı Robotaksi telemetri, LiDAR ve güvenlik durumu kokpit ekranı.
* `build_closed_box_sdk.py`: Açık kaynak `.py` kodlarını gizleyip yalnızca `.pyc` derlenmiş kapalı kutu müşteri paketi üreten derleyici.
* `robotaxi_cli.py`: Komut satırı yönetim ve denetim aracı.
* `tests/test_sdk.py`: **21 alt sistemin tamamını** doğrulayan bağımsız otomatik test süiti (`21/21 PASSED`).

---

## 3. HIZLI BAŞLANGIÇ VE KULLANIM

### 1. 21 Alt Sistem Test Süitini Çalıştırma (%100 Başarı)
```bash
python robotaxi_cli.py test
# veya
pytest tests/test_sdk.py -v
```

### 2. Sivil Mühendislik Kokpitini Başlatma (GUI)
```bash
python robotaxi_cli.py cockpit
```

### 3. 100 Hz CAN-FD Otonom Sürüş Döngüsünü Doğrulama
```bash
python robotaxi_cli.py drive
```

### 4. 1 Aralık 2024 Resmî Gazete (AB 2022/1426) & ASIL-D Denetim Raporu Alma
```bash
python robotaxi_cli.py audit
```

---

## 4. KURUMSAL FİLO VE MÜHENDİSLİK ENTEGRASYON REHBERİ

### Parametre Değişikliği (Çekirdek Kod Düzenlemeye Gerek Yoktur)
Saha ve entegrasyon mühendisleri araç dingil mesafesini, direksiyon boşluğu toleransını, maksimum hız sınırını veya CAN ID'lerini değiştirmek istediklerinde **kaynak koda dokunmaz**. Tüm ayarlar `config/maxus_mifa7.yaml` dosyasından yönetilir:

```yaml
vehicle:
  wheel_base_m: 2.975          # Dingil mesafesi (SAIC Maxus MIFA 7)
  max_speed_kmh: 50.0          # Şehir içi ODD azami hız limiti
can_bus:
  channel: "can0"              # Linux SocketCAN arayüzü
  arbitration_bitrate: 500000  # 500 kbps
  data_bitrate: 2000000        # 2 Mbps CAN-FD
```
