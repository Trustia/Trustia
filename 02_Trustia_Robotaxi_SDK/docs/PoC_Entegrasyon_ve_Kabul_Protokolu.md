# TRUSTIA SEVİYE-4 ROBOTAKSİ PLATFORMU (SAIC MAXUS MIFA 7)
## Seviye-4 Otonom Sürüş PoC Entegrasyon ve Kabul Protokolü (ICD)

**Belge No:** TRU-ICD-2026-MIFA7  
**Kapsam:** SAIC Maxus MIFA 7 Elektrikli MPV Seviye-4 Otonomi Entegrasyonu  
**Sistem Mimarı:** Murat Furkan Bayram (%100 Fikri Mülkiyet Sahibi)  
**Standartlar:** ISO 26262:2018 ASIL-D • ISO 11898-1:2015 CAN-FD • UN/ECE R157 ALKS • ISO 14229 UDS  

---

### 1. SİSTEM MİMARİSİ VE BİLEŞEN DAĞILIMI

```
+---------------------------------------------------------------------------------------------------+
|                        SAIC MAXUS MIFA 7 — ÇİFT HAKEMLİ (1oo2D) EMNİYET MİMARİSİ                  |
|                                                                                                   |
|  [HESAI / OUSTER LIDAR]      [11x KAMERA + RADAR]                                                 |
|           |                           |                                                           |
|           | (1000BASE-T1 Ethernet)    | (GMSL2 SerDes)                                            |
|           v                           v                                                           |
|  +---------------------------------------------------------------------------------------------+  |
|  | BİRİNCİL SÜRÜŞ BEYNİ: CalmCar Horizon Robotics Journey 6P (560 TOPS)                         |  |
|  | * CalmDrive 3.0 End-to-End Multimodal Vision-Language-Action (VLA) Algı ve Rota Adayı       |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Aday Yörünge & Bounding Box)                   |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  | İKİNCİL DETERMINİSTİK EMNİYET HAKEMİ: TRUSTIA ROBOTAXI SDK v4.3 (ASIL-D | 21 ALT SİSTEM)    |  |
|  | * 3D LiDAR NDT & 400 Hz Error-State Kalman Filtresi (ESKF) ile Bağımsız Konumlandırma       |  |
|  | * Çift-Sensör Çapraz Doğrulama (Cross-Sensor Validation - 0 Hayalet Frenleme)               |  |
|  | * Kinematik Hybrid A* + Frenet Frame + S-Curve Jerk-Limited Trajectory Optimizer            |  |
|  | * Stanley + MPC Yanal/Boyuna Kontrol + Lastik Kayma / Sürtünme Kestiricisi (Pacejka)        |  |
|  | * UNECE R157 Kara Kutu (DSSAD), SOTIF ISO 21448 ODD, UDS 0x19/0x22, V2X SPaT & VRU Tahmini |  |
|  | * KVKK m.9 Uç Veri Kalkanı (Çin CalmForge Bulut Senkronizasyon İzolasyonu)                  |  |
|  | * 50ms Donanımsal Watchdog & Minimal Risk Maneuver (MRM) Güvenli Durma Makinesi             |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Onaylanmış Aktüatör Komutları)                 |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  | ŞASİ SÜRÜCÜSÜ: ISO 11898-1 CAN-FD HESAPLAMA HATTI (500 kbps Arbitraj / 2.0 Mbps Veri)       |  |
|  | * ID 0x1A0 (416): Maxus MIFA 7 EPS Direksiyon Açı & Tork Komutu (100 Hz)                     |  |
|  | * ID 0x1A1 (417): Maxus MIFA 7 IPB Elektro-Hidrolik Fren & MCU İtme Torku (50 Hz)           |  |
|  | * ID 0x010 (16) : ASIL-D Yaşam Sinyali & Watchdog Kalp Atışı (50 Hz)                         |  |
|  | * ID 0x014 (20) : Minimal Risk Maneuver (MRM) Acil Frenleme ve EPB Kilitleme                |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 |                                                 |
|                                                 v                                                 |
|                         [INFINEON AURIX TC397 / ŞASİ AKTÜATÖRLERİ]                               |
|                         * Direksiyon Motoru (EPS) | Elektronik Fren (IPB)                         |
+---------------------------------------------------------------------------------------------------+
```

---

### 2. GECİKME BÜTÇESİ VE ZAMANLAMA SLA (END-TO-END LATENCY SLA)

Otonom sürüş sisteminde sensörden aktüatöre toplam tepki süresi kritik emniyet sınırıdır. Trustia SDK, 50 Hz döngüde **maksimum 105 milisaniye** içinde tüm döngüyü tamamlar:

| İşlem Adımı | Modül | Maksimum Süre (SLA) | İletişim Protokolü |
| :--- | :--- | :--- | :--- |
| **1. Sensör Verisi Toplama** | Hesai LiDAR & IMU | **5.0 ms** (±0.5 ms) | PTP (IEEE 802.1AS) TSN Ethernet |
| **2. CalmCar Algı Çıktısı** | Horizon J6P (CalmDrive) | **35.0 ms** (±2.0 ms) | BPU Cuda IPC / Shared Memory |
| **3. Çift-Sensör Çapraz Doğrulama** | Trustia Safety Arbiter | **15.0 ms** (±1.0 ms) | POSIX SHM (Zero-Copy) |
| **4. Kinematik Rota Planlama** | Trustia Hybrid A* | **25.0 ms** (±2.5 ms) | Kinematik Bisiklet Modeli |
| **5. Stanley Yol Takip Denetimi** | Trustia Stanley Controller | **10.0 ms** (±1.0 ms) | Yanal ve Boyuna PID |
| **6. CAN-FD Çerçeve Kodlama & Tx** | Trustia Mifa7 CAN-FD Bridge | **5.0 ms** (±0.5 ms) | SocketCAN / PEAK PCAN-FD |
| **TOPLAM TEPKİ SÜRESİ (KRİTİK HAT)**| **UÇTAN UCA (Sensor to Actuator)** | **$\le$ 95.0 ms** | **ASIL-D HARD REAL-TIME ONAYLI** |

---

### 3. FİZİKSEL ARAÇTA İLK GÜN ENTEGRASYON PROTOKOLÜ (DAY-1 RUNBOOK)

Hacettepe Teknokent veya Teknopark İstanbul kapalı pistine SAIC Maxus MIFA 7 aracı çekildiğinde, test mühendisinin adım adım uygulayacağı prosedür:

#### Adım 1: Fiziksel Veri Yolu Bağlantısı ve Direnç Ölçümü
1. Araç kontağını kapatın (`Ignition OFF`).
2. OBD-II portu veya şasi CAN breakout konnektöründe **Pin 6 (CAN_H)** ile **Pin 14 (CAN_L)** arasına dijital multimetre bağlayın.
3. **Ölçülen Hat Direnci:** **$60.0\ \Omega \pm 3.0\ \Omega$** olmalıdır.
   * *120 $\Omega$ okunuyorsa:* Hat sonlandırma direnci eksiktir; PEAK PCAN cihazındaki dahili 120 $\Omega$ anahtarını açın.
   * *40 $\Omega$ veya altı okunuyorsa:* Fazla direnç vardır; harici direnci devreden çıkarın.
4. PEAK-System PCAN-USB Pro FD adaptörünü araca ve Linux test bilgisayarına bağlayın.

#### Adım 2: Linux SocketCAN Arayüzünü Başlatma
```bash
# can0 arayüzünü 500 kbps arbitraj / 2.0 Mbps veri hızıyla ayağa kaldır
sudo ip link set can0 down || true
sudo ip link set can0 up type can \
  bitrate 500000 sample-point 0.8 \
  dbitrate 2000000 dsample-point 0.75 \
  fd on restart-ms 100

# Soket tampon belleklerini optimize et
sudo sysctl -w net.core.rmem_max=8388608
sudo sysctl -w net.core.wmem_max=8388608

# Hata çerçevelerini kontrol et (Hata sayısı 0 olmalıdır)
ip -details -statistics link show can0
```

#### Adım 3: Sürücü Manuel Müdahale (Takeover / Override) Güvenlik Doğrulaması
Otonom sürüş devredeyken sürücünün direksiyona veya pedala dokunduğu anda sistemin gücü anında insana devrettiği tescillenir:
* **Direksiyon Müdahale Eşiği:** Sürücü direksiyonu ters yöne çevirdiğinde ölçülen tork **$\ge 3.5\ \text{Nm}$** olduğu anda otonomi devreden çıkar ve sistem `MANUAL_OVERRIDE` durumuna geçer.
* **Fren Müdahale Eşiği:** Sürücü frene dokunduğu an ana merkez basıncı **$\ge 8.0\ \text{bar}$** olduğu anda CAN-FD komutları kesilir ve araç sürücünün ayağına bırakılır.
* **Watchdog Kesintisi:** Test bilgisayarının gücü çekildiğinde veya kablo koptuğunda, araç beyni **$\le 40\ \text{ms}$** içinde (2 eksik kalp atışı) güvenli duruşa geçer.

#### Adım 4: 0 km/h Statik Aktüatör Testi
1. Araç park halinde (`P` modunda), kontak açık.
2. `canbus/maxus_mifa7_chassis.dbc` dosyasındaki `0x1A0` mesajıyla direksiyon motoruna **+5.0 derece** açı komutu gönderilir:
   ```bash
   cansend can0 1A0##100F40000000000000000000000000000
   ```
3. Direksiyon simidinin kabin içinde fiziksel olarak sağa 5 derece döndüğü gözlemlenir.
4. Direksiyon simidi sıfır dereye getirilir. Aktüatör eşlemesi başarıyla tamamlanmıştır.

#### Adım 5: 10 km/h Kapalı Pist Otonom Sürüş Testi
1. Araç Hacettepe Teknokent kapalı test pistine alınır.
2. Tavan LiDAR'ından ve IMU'dan gelen verilerle `trustia_sdk` başlatılır.
3. Araç 10 km/h hızda kapalı pist şeridini otonom olarak takip eder; yanal sapma (CTE) **$< 5.0\ \text{cm}$** toleransla ölçülür.

---

### 4. CAN DBC SİNYAL HARİTASI VE AKTÜATÖR KODLARI

Tam DBC dosyası `canbus/maxus_mifa7_chassis.dbc` dizininde oluşturulmuştur:

* **0x1A0 (416) `MIFA7_STEERING_CMD` (100 Hz):**
  * `STEER_TARGET_ANGLE`: [-35.0°, +35.0°], Çözünürlük: 0.01°/bit.
  * `STEER_TARGET_RATE`: [0, 500°/s], Çözünürlük: 0.1°/s/bit.
  * `STEER_MAX_TORQUE`: [0, 6.0 Nm], Çözünürlük: 0.01 Nm/bit.
  * `STEER_ROLLING_COUNTER`: [0 - 15] Sürekli artan monoton sayaç.
  * `STEER_CHECKSUM`: SAE J1850 8-bit CRC koruması.
* **0x1A1 (417) `MIFA7_ACCEL_BRAKE_CMD` (50 Hz):**
  * `TARGET_ACCEL`: [-6.5 m/s², +2.5 m/s²], Çözünürlük: 0.01 m/s²/bit.
  * `TARGET_SPEED`: [0, 20.0 m/s] (~72 km/h azami).
  * `TARGET_BRAKE_PRESSURE`: [0, 150 bar] i-Booster hidrolik basınç hedefi.
* **0x010 (16) `MIFA7_SAFETY_HEARTBEAT` (50 Hz):**
  * `ASIL_STATUS_CODE`: 0x01 (Nominal ASIL-D), 0x02 (Degraded), 0xEE (MRM Stop).
  * `WATCHDOG_COUNTER`: 50 ms zaman aşımı sayacı.

---

### 5. POC TEST AŞAMALARI VE KABUL KRİTERLERİ (ACCEPTANCE CRITERIA)

PoC süreci aşağıdaki 3 fazda ve teknik doğrulama kriterlerine göre icra edilir:

1. **Fikri Mülkiyet ve Dağıtım Modeli:**
   * Trustia AI algoritmaları, Hybrid A* kinematik modeli ve ASIL-D güvenlik hakemi kodları Murat Furkan Bayram'ın %100 şahsi mülkiyetindedir (5846 Sayılı FSEK m.8).
   * Müşteri ve entegratörlere açık kaynak `.py` kodu teslim edilmez; derlenmiş kapalı kutu Linux binary'si (`.so` / `.pyc`), HMAC donanım kilidi ve `vehicle_config.yaml` ayar dosyası formatında teslim edilir.

2. **60 Günlük PoC Mühendislik Yol Haritası:**
   * **Faz 1 (Gün 1 - 15) Veri Yolu ve Aktüatör Eşlemesi:** Maxus MIFA 7 CAN-FD veriyolu dinleme, DBC sinyal eşleme, direksiyon açısı ve fren aktüatör kalibrasyonu.
   * **Faz 2 (Gün 16 - 35) Çoklu Algı ve Emniyet Hakemi Entegrasyonu:** CalmCar / kamera algı akışı ile Trustia Safety Arbiter'ın laboratuvar bench testi, 50ms Watchdog doğrulama.
   * **Faz 3 (Gün 36 - 60) Kapalı Pist Otonom Sürüş Doğrulaması:** Kapalı test pistinde 50 km/s azami hızda şerit takip, kavşak geçişi, dinamik engel kaçınma ve MRM güvenli durma kabul testleri.

3. **Teknik Kabul ve Devreye Alma Kriterleri:**
   * Uçtan uca döngü gecikmesinin $\le 95.0\ \text{ms}$ olduğu tescillenmelidir.
   * Acil durumlarda 50 ms içinde MRM devreye girmeli, 1.5 m/s² kontrollü frenlemeyle araç emniyet şeridine çekilmelidir.
   * Donanımsal devralmada (takeover) $\ge 3.5\ \text{Nm}$ direksiyon veya $\ge 8.0\ \text{bar}$ fren müdahalesinde 5 ms içinde otonomi manuel sürücüye devredilmelidir.
