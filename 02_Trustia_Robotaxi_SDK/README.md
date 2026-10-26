# TRUSTIA L4 ROBOTAXI ENTERPRISE SDK (v2.4)
### SAIC Maxus MIFA 7 & Hyundai E-GMP Otonom Sürüş Güvenlik Hakemi ve Kontrol Kütüphanesi

**Kurucu & Baş Mimar:** Murat Furkan Bayram (%100 Fikri Mülkiyet Sahibi)  
**Tescil & Akreditasyon:** AB PIC #861711529 • EIT Urban Mobility #CUS15554  
**Hukuki Dayanak:** 5846 Sayılı FSEK & Uluslararası Bern Sözleşmesi Korumalı Eser  
**Standartlar:** ISO 26262 ASIL-D • ISO 11898-1 CAN-FD • UN/ECE R157 • 1 Aralık 2024 Resmî Gazete Otonom Tebliği  

---

## 1. MİMARİ GENEL BAKIŞ

Bu SDK, SAIC Maxus MIFA 7 elektrikli MPV platformu ve ticari filo operasyonları için geliştirilmiş **%100 Milli Deterministik Güvenlik Hakemi, Seyrüsefer ve CAN-FD Aktüatör Kütüphanesidir**.

```
                           ┌───────────────────────────────┐
                           │      LiDAR (Hesai / Ouster)   │
                           └───────────────┬───────────────┘
                                           │ Pointcloud
┌───────────────────────────────┐          ▼
│   CalmCar Horizon J6M SoC     ├─────► ┌───────────────────────────────────────┐
│   (CalmDrive 3.0 Perception)  │       │     TRUSTIA SAFETY ARBITER            │
└───────────────────────────────┘       │  • Çift-Sensör Çapraz Doğrulama       │
                                        │  • KVKK m.9 Uç Güvenlik Kalkanı       │
                                        │  • ISO 26262 ASIL-D 50ms Watchdog     │
                                        └──────────────────┬────────────────────┘
                                                           │
                                        ┌──────────────────▼────────────────────┐
                                        │    TRUSTIA SEVİYE-4 SEYRÜSEFER MOTORU │
                                        │  • 3D LiDAR NDT & 400Hz ESKF SLAM     │
                                        │  • Kinematik Hybrid A* Planlayıcı     │
                                        │  • Stanley & Pure Pursuit Kontrolör   │
                                        └──────────────────┬────────────────────┘
                                                           │
                                        ┌──────────────────▼────────────────────┐
                                        │  ISO 11898-1 CAN-FD SÜRÜCÜSÜ (500k/2M)│
                                        │  (Maxus MIFA 7 EPS & i-Booster CAN-FD)│
                                        └──────────────────┬────────────────────┘
                                                           │
                                           ┌───────────────▼───────────────┐
                                           │ Infineon AURIX TC397 / ECU    │
                                           └───────────────────────────────┘
```

---

## 2. MODÜL VE DİZİN YAPISI

* `config/maxus_mifa7.yaml`: SAIC Maxus MIFA 7 araç dinamikleri, CAN baudrate ve sensör montaj ayarları.
* `trustia_sdk/`:
  * `core/`: Kriptografik lisans yöneticisi (`licensing.py`), koordinat ve kinematik dönüşümleri (`transforms.py`).
  * `canbus/`: ISO 11898-1 CAN-FD aktüatör çerçeve kodlayıcı ve çözücü (`mifa7_canfd.py`).
  * `perception/`: CalmCar deterministik emniyet hakemi ve KVKK veri kalkanı (`calmcar_bridge.py`).
  * `slam/`: 3D LiDAR NDT ve 400 Hz Error-State Kalman Filtresi (`ndt_eskf.py`).
  * `planning/`: SAIC Maxus MIFA 7 kinematik Hybrid A* rota planlayıcısı (`hybrid_astar.py`).
  * `control/`: Stanley yol takip ve boyuna hız PID denetleyicisi (`stanley_controller.py`).
  * `safety/`: ISO 26262 ASIL-D Minimal Risk Maneuver (MRM) ve 50ms Watchdog (`asil_d_mrm.py`).
  * `fleet/`: Merkezi filo bulut platformu ve operasyon merkezi için JSON telemetri ve görev köprüsü (`telemetry_api.py`).
  * `gui/`: Sivil test sürücüsü ve saha mühendisi Robotaksi Kokpit Konsolu (`cockpit_gui.py`).
* `robotaxi_cli.py`: Komut satırı yönetim aracı.
* `tests/test_sdk.py`: 9 temel alt sistemin otomatik doğrulama süiti.

---

## 3. HIZLI BAŞLANGIÇ VE KULLANIM

### 1. Test Süitini Çalıştırma (%100 Başarı)
```bash
python robotaxi_cli.py test
```

### 2. Sivil Mühendislik Kokpitini Başlatma (GUI)
```bash
python robotaxi_cli.py cockpit
```

### 3. CAN-FD Otonom Sürüş Döngüsünü Doğrulama
```bash
python robotaxi_cli.py drive
```

### 4. Mevzuat ve ASIL-D Denetim Raporu Alma
```bash
python robotaxi_cli.py audit
```

---

## 4. KURUMSAL FİLO VE MÜHENDİSLİK ENTEGRASYON REHBERİ

### Parametre Değişikliği (Kod Düzenlemeye Gerek Yoktur)
Saha ve entegrasyon mühendisleri araç dingil mesafesini, maksimum hız sınırını veya CAN ID'lerini değiştirmek istediklerinde **kaynak koda dokunmaz**. Tüm ayarlar `config/maxus_mifa7.yaml` dosyasından yönetilir:

```yaml
vehicle:
  wheel_base_m: 2.975          # Dingil mesafesi
  max_speed_kmh: 50.0          # Şehir içi azami hız limiti
can_bus:
  channel: "can0"              # Soket CAN arayüzü
  arbitration_bitrate: 500000  # 500 kbps
  data_bitrate: 2000000        # 2 Mbps
```

---

## 5. SAVUNMA / SİVİL AYRIMI BEYANI

Bu paket **yalnızca sivil Seviye-4 otonom yolcu taşımacılığı (Robotaksi)** teknolojilerini içermektedir. Trustia AI bünyesindeki askeri taktik seyrüsefer, EYP/mayın tespit ve NATO STANAG sistemleri bu paketten tamamen arındırılmıştır ve ayrı bir savunma fikri mülkiyeti olarak korunmaktadır.
