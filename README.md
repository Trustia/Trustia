# 🚗 TRUSTIA AI — Deterministik Seviye-4 Otonom Sürüş & Robotaksi Yazılım Platformu (v4.3 Enterprise)

![Trustia Banner](Kurumsal/Medya/Banner.jpg)

<div align="center">

[![Test Süiti](https://img.shields.io/badge/Otomatik_Testler-1%2C324_%2B_21_(1%2C345_Test_%7C_%25100_BA%C5%9EARI)-brightgreen.svg?logo=pytest&logoColor=white)](https://github.com/Trustia/Trustia)
[![Yazılım Envanteri](https://img.shields.io/badge/Kod_Envanteri-203_Dosya_%7C_31%2C400%2B_Sat%C4%B1r-brightgreen.svg)](https://trustia.com.tr)
[![C++20 & ROS 2](https://img.shields.io/badge/C%2B%2B-20_%7C_ROS_2_Humble-00599C?logo=c%2B%2B&logoColor=white)](https://github.com/Trustia/Trustia)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Next.js 16 & Three.js](https://img.shields.io/badge/WebGL_Telemetri-Next.js_16_%7C_Three.js-black?logo=next.js&logoColor=white)](https://trustia.com.tr)
[![Emniyet Standardı](https://img.shields.io/badge/Fonksiyonel_Emniyet-ISO_26262_ASIL--D_%7C_ISO_21448_SOTIF-emerald.svg)](https://trustia.com.tr/politika/otonom-guvenlik/)
[![Tip Onayı](https://img.shields.io/badge/Reg%C3%BClasyon-AB_2022%2F1426_%7C_UN_R155%2FR156%2FR157-blue.svg)](https://trustia.com.tr/robotaxi/)
[![Referans Şasiler](https://img.shields.io/badge/CAN--FD_DBW-SAIC_Maxus_MIFA_7_%26_Hyundai_Ioniq_5-orange.svg)](https://trustia.com.tr/robotaxi/)
[![ASELSAN Onaylı Tedarikçi](https://img.shields.io/badge/ASELSAN-Onayl%C4%B1_Tedarik%C3%A7i_%230050569-darkred.svg)](https://trustia.com.tr/savunma/)
[![STM Savunma](https://img.shields.io/badge/STM_Savunma-Tedarik%C3%A7i_K%C3%BCt%C3%BC%C4%9F%C3%BC_%23KAYITLI-0284c7.svg)](https://trustia.com.tr/savunma/)
[![AB PIC](https://img.shields.io/badge/Avrupa_Komisyonu-PIC_861711529_%7C_EIT_CUS15554-1d4ed8.svg)](https://trustia.com.tr/hakkimizda/)
[![OIN 2.0](https://img.shields.io/badge/OIN_2.0-Patent_Savunma_Pakt%C4%B1_%23f1e44576-purple.svg)](https://trustia.com.tr/politika/oin-lisans/)
[![Teknopark İstanbul](https://img.shields.io/badge/Teknopark_%C4%B0stanbul-Cube_Incubation_%26_HASAT_2026-critical.svg)](https://trustia.com.tr/hakkimizda/)
[![İTO BTM](https://img.shields.io/badge/%C4%B0TO_BTM-Fulya_Derin_Teknoloji_Kamp%C3%BCs%C3%BC-0369a1.svg)](https://trustia.com.tr/hakkimizda/)
[![KOSGEB & BTK](https://img.shields.io/badge/KOSGEB_%26_BTK-Resmi_Sertifikal%C4%B1-16a34a.svg)](https://trustia.com.tr/hakkimizda/)

**[🌐 Resmi Web Platformu](https://trustia.com.tr)** • **[🚕 Seviye-4 Robotaksi Mimarisi](https://trustia.com.tr/robotaxi/)** • **[🛡️ Savunma & Taktik İKA](https://trustia.com.tr/savunma/)** • **[🏛️ Kurumsal Politikalar & Yasal Uyum](https://trustia.com.tr/politika/otonom-guvenlik/)** • **[📩 İletişim & PoC Talebi](https://trustia.com.tr/iletisim/)**

</div>

---

## 📋 Yönetici Özeti (Executive Summary)

**Trustia AI Technologies**, sivil ticari yolcu robotaksileri (**SAIC Maxus MIFA 7** & **Hyundai Ioniq 5 E-GMP**), fabrika/liman ağır yük otonom araçları (AMR/AGV), havalimanı/kampüs ring servisleri ve savunma sanayii insansız kara araçları (İKA) için sıfırdan **C++20, ROS 2 Humble, Python 3.12 ve TypeScript** ile geliştirilmiş **%100 yerli ve bağımsız Seviye-4 (SAE J3016 L4) Deterministik Otonom Sürüş Yazılım Platformudur**.

Uçtan uca kara kutu (black-box) yapay zeka modellerinin yarattığı halüsinasyon ve açıklanamaz karar risklerini ortadan kaldırmak amacıyla; Trustia çekirdeği **matematiksel olarak kanıtlanabilir deterministik algoritmalar** (Kinematik Hybrid A*, Frenet 5. Derece Quintic Kafes Planlama, Kayan Ufuklu MPC, Stanley Geometrik Kontrol, IEEE 2846 RSS Güvenlik Zarfı ve 400 Hz ESKF + 3D LiDAR NDT SLAM) üzerine inşa edilmiştir.

* **Tam Yazılım Envanteri:** **203 Dosya / 31.400+ Satır** özgün kaynak kod ve mühendislik şartnamesi (%0 harici kapalı kutu bağımlılığı).
* **Kesintisiz Doğrulama Süiti:** **1.324 Çekirdek Testi + 21 Robotaksi SDK Testi = 1.345 Otomatik Birim, Entegrasyon ve SIL/HIL Simülasyon Testi (%100 Yeşil, 0 Hata, 0 Regresyon)**.
* **Fikri Mülkiyet & Dağıtım Modeli:** Kurucu ve Sistem Mimarı **Murat Furkan Bayram**'ın %100 tekil mülkiyetindedir. Müşterilere ve OEM entegratörlerine açık kaynak `.py`/`.cpp` kodu teslim edilmez; yalnızca **HMAC-SHA256 donanım kilitli (ECU/CPU UUID) derlenmiş kapalı kutu (`.pyc` / `.so` Closed-Box Enterprise SDK)** paketleri sunulur.

---

## 🏛️ 1. Resmi Kurumsal Akreditasyonlar, Savunma Tescilleri & Ekosistem Kayıtları

Trustia AI, ulusal ve uluslararası savunma sanayii, otomotiv, fikri mülkiyet ve derin teknoloji ekosistemlerinde resmi olarak tescillidir:

| Kurum / Organizasyon | Merkez | Resmi Tescil / Sicil Numarası ve Kurumsal Statü |
| :--- | :--- | :--- |
| 🛡️ **ASELSAN A.Ş.** | Ankara, TR | **Onaylı Tedarikçi Kütüğü Kayıtlı Girişim** (Firma Kodu: `#0050569` • SAP: `FZQHEXGFMTJU`) |
| 🇹🇷 **STM Savunma Teknolojileri A.Ş.** | Ankara, TR | **Savunma ve Derin Teknoloji Tedarikçi Ekosistemi Kayıtlı Aday Tedarikçi** |
| 🛡️ **Open Invention Network (OIN 2.0)** | New York, ABD | **İmzalı İkili Patent Savunma Paktı Lisansı** (`#f1e445769a9934114db095c4f5430a0e749d8201` — 4.000+ Küresel Üye) |
| 🇪🇺 **Avrupa Komisyonu (European Commission)** | Brüksel, AB | **Resmi AB Katılımcı Kimlik Kodu (EU PIC: `861711529`)** — Horizon Europe Otonom Mobilite |
| 🇪🇺 **EIT Urban Mobility** | Barselona, AB | **Avrupa İnovasyon ve Teknoloji Enstitüsü Kentsel Mobilite Partner ID (`CUS15554`)** |
| 🚀 **Teknopark İstanbul (Cube Incubation)** | İstanbul, TR | **Ön Kuluçka Girişimi (6 Aylık Protokol) & HASAT 2026 Erken Aşama Hızlandırma Programı** |
| 🏛️ **İTO Bilgiyi Ticarileştirme Merkezi (BTM)** | İstanbul, TR | **Fulya Derin Teknoloji Kampüsü Yerleşik Girişimi** |
| 🎓 **YTÜ Yıldız Teknopark** | İstanbul, TR | **Yıldız Kuluçka Ekosistem ve Ön Kuluçka Başvurusu** |
| 📜 **T.C. KOSGEB** | İstanbul, TR | **İleri Girişimci Resmi Sertifikası (`KSB01UGE0115153370`)** |
| 📜 **T.C. BTK Akademi** | Ankara, TR | **Savunma Sanayii ve Yapay Zeka Sertifikasyonu (`L2zPtN4X1ZJ`)** |

---

## 📁 2. Ana Depo Mimarisi ve Kod Envanteri (203 Dosya / 31.400+ Satır)

Tüm depo varlıkları, kurumsal temiz mimari prensipleri doğrultusunda **4 ana dizin** altında yapılandırılmıştır:

```text
Trustia/
├── 01_Trustia_Otonom_Yazilim_Core/    ← [117 Çekirdek Dosyası (21.000+ Satır) + 51 Test Dosyası (6.600+ Satır / 1.324 Test)]
│   ├── ai/                            ← CenterPoint / BEV 3D Algı, 7-DOF EKF Takip, 3s Yörünge Tahmini & nuScenes Kataloğu
│   ├── slam/                          ← GNSS-Denied 3D NDT Pose-Graph SLAM & 400 Hz Error-State Kalman Filtresi (ESKF)
│   ├── planning/                      ← Kinematik Hibrit A*, Frenet 5. Derece Quintic Polinom & Dinamik Engel Kaçınma
│   ├── control/                       ← Pure Pursuit, Stanley Yanal İzleme, Boyuna PID & CAN DBC Sinyal Kodlayıcı
│   ├── security/                      ← ISO 26262 ASIL-D MRM, Watchdog & ISO 21448 SOTIF Plausibility Monitörü
│   ├── integration/                   ← 100 Hz Linux SocketCAN CAN-FD Sürücüsü & ROS 2 Humble Drive-by-Wire Köprüsü
│   ├── security/                      ← ISO 26262 ASIL-D 50ms Watchdog, 1.5 m/s² MRM Güvenli Duruş & SecOC Kriptografi
│   ├── command/                       ← Çoklu Robotaksi Filo Çağrı, Telemetri Yönlendirme ve Dinamik Rota Dağıtım Motoru
│   ├── core/                          ← AutonomyCore Üst Düzey API, Sistem Orkestratörü & HMAC-SHA256 Donanım Kilidi
│   ├── config/                        ← Evrensel Araç Konfigürasyonu (vehicle_config.yaml — Kod Değişmezliği İlkesi)
│   ├── tools/                         ← build_enterprise_sdk.py (Kapalı Kutu .pyc B2B Enterprise SDK Derleyicisi)
│   └── tests/                         ← 1.307 Adet Otomatik Birim, Entegrasyon, Kaos ve SIL/HIL Simülasyon Testi
│
├── 02_Trustia_Robotaxi_SDK/           ← [36 Dosya / 4.453 Satır — SAIC Maxus MIFA 7 & Çoklu Şasi L4 Robotaksi SDK (21 Test)]
│   ├── canbus/                        ← maxus_mifa7_chassis.dbc (0x1A0 EPS Direksiyon, 0x1A1 Fren/İvme, 0x010 Watchdog)
│   ├── config/                        ← maxus_mifa7.yaml (2.975 m Dingil Mesafesi, 500 kbps / 2 Mbps CAN-FD Ayarları)
│   ├── trustia_sdk/                   ← 21 Alt Sistem: ASIL-D Çift-Sensör Hakemi, SOTIF ODD, UN R157 DSSAD, R155 IDPS,
│   │                                    R156 SUMS OTA, IEEE 2846 RSS, Kaldırım Algılama, PTP Deskew, MPC, 5G Teleop, eHMI
│   ├── gui/                           ← Masaüstü (Tkinter) ve WebGL 3B Canlı Robotaksi Mühendislik Kokpiti
│   ├── docs/                          ← PoC_Entegrasyon_ve_Kabul_Protokolu.md (60 Günlük Saha ve Pist Kabul Protokolü)
│   ├── dist/                          ← Trustia_Robotaxi_Evaluation_SDK_ClosedBox.zip (Müşteri Teslimatına Hazır .pyc Paketi)
│   └── tests/                         ← test_sdk.py (21 Alt Sistemin Tamamını Doğrulayan 21/21 Otomatik Test Süiti)
│
├── 02_Trustia_Web_Platformu/          ← [40 Dosya / 7.024 Satır — Kurumsal Web Platformu & 3D WebGL Telemetri Simülatörü]
│   └── website/                       ← Next.js 16, React 19, Three.js 3D Dijital İkiz, TR/EN Çift Dil & 8 Politika Portalı
│
└── Kurumsal/                          ← [Resmi Devlet, Savunma, Patent ve Akreditasyon Belgeleri Arşivi]
    ├── Belgeler/                      ← ASELSAN, STM, OIN 2.0, Teknopark İstanbul, İTO BTM, AB PIC, KOSGEB & BTK Belgeleri
    ├── Sunumlar/                      ← Kurumsal Sunumlar, BOM Donanım Listeleri ve Tam Yazılım Envanteri Raporları
    ├── Basvurular/                    ← Hibe, Destek ve Hızlandırma Programı Takip Kütükleri
    └── Medya/                         ← Yüksek Çözünürlüklü Kurumsal Logolar, Mimari Şemalar ve Saha Videoları
```

---

## 🧠 3. Çift Hakemli (1oo2D) Seviye-4 Otonomi & Emniyet Mimarisi

Trustia mimarisi; hem doğrudan tekil ana sürüş beyni olarak (**Hyundai Ioniq 5 E-GMP** üzerinde NVIDIA Jetson AGX Orin 64GB ile) hem de mevcut görsel algı bilgisayarlarının (**SAIC Maxus MIFA 7** üzerindeki CalmCar Horizon Robotics Journey 6P — 560 TOPS) çıktısını denetleyen **İkincil Deterministik ASIL-D Emniyet Hakemi (1oo2D Safety Arbiter)** olarak çalışır:

```text
+-------------------------------------------------------------------------------------------------------+
|                     TRUSTIA v4.3 — ÇİFT HAKEMLİ (1oo2D) SEVİYE-4 OTONOMİ MİMARİSİ                     |
|                                                                                                       |
|  [3D LiDAR: Ouster OS2-128 / Hesai]             [11x GMSL2 HDR Kamera + 77GHz Radar + 400Hz IMU]      |
|                  |                                                      |                             |
|                  | (IEEE 1588v2 PTP <1us & Motion Deskewing)            | (GMSL2 / BPU Zero-Copy IPC) |
|                  v                                                      v                             |
|  +-------------------------------------------------------------------------------------------------+  |
|  | ALGI & ÇAPRAZ DOĞRULAMA KATMANI (ISO 21448 SOTIF & Çift-Sensör Füzyonu)                         |  |
|  | * 3D RANSAC Zemin Ayrıştırma, DBSCAN Kümeleme, OBB ve 3D Kaldırım Taşı / Bordür (Curb) Kilidi   |  |
|  | * Kamera + 3D LiDAR Çapraz Doğrulaması: Yansıma / Gölge Kaynaklı "Hayalet Frenleme" Oranı = %0  |  |
|  | * ISO/TR 23049 eHMI Dış Yaya Ekranı & Akustik Ambulans/İtfaiye Sireni (600-1550 Hz) Fermuarı    |  |
|  +------------------------------------------------+------------------------------------------------+  |
|                                                   |                                                   |
|                                                   v                                                   |
|  +-------------------------------------------------------------------------------------------------+  |
|  | KONUMLANDIRMA, HD HARİTA VE KİNEMATİK PLANLAMA (GNSS-Denied SLAM & Trajectory Generation)       |  |
|  | * 3D LiDAR NDT Pose-Graph SLAM + 400 Hz Error-State Kalman Filtresi (Tünelde 4.2 cm Hassasiyet) |  |
|  | * Lanelet2 HD Harita & 2918 Sayılı KTK m.74 Yaya Geçidi Zorunlu Duruş Çizgisi (Stop-Line)       |  |
|  | * Kinematik Hybrid A* + Frenet (s, d) 5. Derece (Quintic) Sarsıntı-Optimal (Jerk-Limited) Rota  |  |
|  +------------------------------------------------+------------------------------------------------+  |
|                                                   |                                                   |
|                                                   v                                                   |
|  +-------------------------------------------------------------------------------------------------+  |
|  | DETERMINİSTİK KONTROL & ASIL-D GÜVENLİK KALKANI (Safety Arbiter, RSS & Fail-Operational)        |  |
|  | * IEEE 2846 & Mobileye RSS Matematiksel Boyuna/Yanal Güvenlik Zarfı                             |  |
|  | * Kayan Ufuklu Model Öngörülü Kontrol (MPC) + Stanley Yanal Kontrol + Pacejka Kayma Kestiricisi |  |
|  | * 1 Aralık 2024 Resmî Gazete (AB 2022/1426) ODD Coğrafi Çit & UN R157 SHA-256 DSSAD Kara Kutu   |  |
|  | * 6698 Sayılı KVKK m.9 Yurt Dışı Veri Kalkanı (Yabancı Bulut Sunucularına Telemetri İzolasyonu) |  |
|  | * 50 ms Donanımsal Watchdog & 1.5 m/s² Kontrollü Emniyet Şeridine Çekme (MRM Safe Stop)         |  |
|  +------------------------------------------------+------------------------------------------------+  |
|                                                   |                                                   |
|                                                   v                                                   |
|  +-------------------------------------------------------------------------------------------------+  |
|  | ŞASİ SÜRÜCÜSÜ: 100 Hz ISO 11898-1 CAN-FD & UN R155 SİBER SALDIRI TESPİT (IDPS) KÖPRÜSÜ          |  |
|  | * 1.4 ms Mesaj Gecikmesi • CRC-16 / SAE J1850 Checksum • Monoton Alive Counter • SecOC          |  |
|  | * Fail-Operational Çift Yedekli Fren Dağıtımı: Birincil i-Booster + İkincil ESC/EPB Yedeği      |  |
|  | * <= 5 ms Donanımsal Sürücü Devralma (Direksiyon >= 3.5 Nm veya Fren >= 8.0 bar)                |  |
|  +-------------------------------------------------------------------------------------------------+  |
+-------------------------------------------------------------------------------------------------------+
```

---

## 🛡️ 4. Uluslararası Seviye-4 Regülasyon ve Standart Uyumluluk Matrisi (20/20 Kriter)

Trustia v4.3, **1 Aralık 2024 tarihli ve 32739 sayılı Resmî Gazete**'de yayımlanan *"Tam Otonom Araçların Otonom Sürüş Sistemine (ADS) İlişkin Tip Onayı Yönetmeliği (AB 2022/1426)"* ve Birleşmiş Milletler **UN/ECE WP.29** regülasyonlarının tamamını karşılayan 20 temel mühendislik modülüne sahiptir:

| # | Uluslararası Standart / Regülasyon | İlgili Modül (`02_Trustia_Robotaxi_SDK` & `Core`) | Teknik Performans ve Doğrulama Kriteri |
| :-: | :--- | :--- | :--- |
| **01** | **CARLA 0.9.15+ & ROS 2 Humble SIL/HIL** | `trustia_sdk/core/carla_bridge.py` | 100 Hz senkron dijital ikiz simülasyonu ve $\le 5\text{ ms}$ sürücü devir testi |
| **02** | **AB 2022/1426 ODD & ISO 21448 SOTIF** | `trustia_sdk/safety/odd_sotif_dssad.py` | Coğrafi çit (Geofence), yağış/görüş/LiDAR yoğunluğu izleme ve otomatik MRM |
| **03** | **UN/ECE R157 DSSAD & EDR Kara Kutu** | `trustia_sdk/safety/odd_sotif_dssad.py` | Otonom sürüş geçişlerini SHA-256 hash zinciriyle adli bilişim formatında kayıt |
| **04** | **5G / WebRTC Uzaktan Operasyon (Teleop)** | `trustia_sdk/fleet/teleoperation.py` | $\le 15\text{ km/s}$ hız limiti, $\le 150\text{ ms}$ RTT gecikme bütçesi ve güvenli koridor onayı |
| **05** | **3D LiDAR Kaldırım (Curb) Algılama** | `trustia_sdk/perception/curb_detector.py` | Silinmiş şerit çizgilerinde 8–28 cm bordür basamağından sürüş koridoru çıkarma |
| **06** | **UN/ECE R155 & ISO/SAE 21434 CAN IDPS** | `trustia_sdk/safety/can_ids_r155.py` | CAN-FD DoS, Spoofing, Replay ve sıra sayacı anomalilerini gerçek zamanlı engelleme |
| **07** | **IEEE 1588v2 PTP & LiDAR Deskewing** | `trustia_sdk/perception/lidar_deskew_ptp.py` | $< 1\ \mu\text{s}$ donanımsal saat senkronu ve 400 Hz IMU ile nokta bulutu düzeltme |
| **08** | **Lanelet2 HD Harita & KTK m.74 Yaya** | `trustia_sdk/planning/lanelet2_rules.py` | Yaya geçitlerinde zorunlu duruş çizgisi (`stop-line`) ve kavşak geçiş hakkı |
| **09** | **Yolcu Kabin Kilidi & EV Batarya BMS** | `trustia_sdk/fleet/cabin_bms_safety.py` | Kapı kilidi (Door Interlock), kemer, SOS butonu ve $48^\circ\text{C}$ BMS termal koruma |
| **10** | **IEEE 2846 & Mobileye RSS Zarfı** | `trustia_sdk/safety/rss_ieee2846.py` | Matematiksel boyuna ($d_{\min,\text{long}}$) ve yanal ($d_{\min,\text{lat}}$) çarpışmasızlık |
| **11** | **Frenet $(s, d)$ 5. Derece Kafes Planlama**| `trustia_sdk/planning/frenet_lattice_planner.py`| Quintic polinomlarla sarsıntı-optimal (Jerk-Limited) konforlu şerit/engel kaçınma |
| **12** | **MPC & Fail-Operational Yedekli Fren** | `trustia_sdk/control/mpc_redundant_control.py` | Kayan ufuklu MPC + Birincil i-Booster arızasında kesintisiz ESC/EPB fren yedekliliği |
| **13** | **UN/ECE R156 SUMS & RXSWIN OTA** | `trustia_sdk/safety/sums_un_r156.py` | SHA-256 imzalı OTA güncelleme, sürüşte güncelleme kilidi ($v=0$) ve atomik Rollback |
| **14** | **ISO/TR 23049 eHMI & Siren Fermuarı** | `trustia_sdk/perception/ehmi_siren_detector.py` | Dış LED yaya iletişim ekranı ve 600–1550 Hz ambulans sireninde otonom fermuar |
| **15** | **GNSS-Denied 3D NDT SLAM & 400Hz ESKF**| `01_Core/slam/` & `trustia_sdk/slam/ndt_eskf.py` | GPS kesintili tünel ve kanyonlarda 4.2 cm RMS yörünge hassasiyeti |
| **16** | **ISO 26262 ASIL-D Watchdog & MRM** | `01_Core/security/` & `asil_d_mrm.py` | 50 ms kontrol zaman aşımı ve $1.5\text{ m/s}^2$ kontrollü sağa çekme (Safe Stop) |
| **17** | **ISO 11898-1 100 Hz CAN-FD Köprüsü** | `01_Core/integration/` & `mifa7_canfd.py` | 500 kbps / 2 Mbps CAN-FD, 1.4 ms mesaj gecikmesi, 5 ms fiziksel sürücü devralma |
| **18** | **6698 Sayılı KVKK m.9 Veri Kalkanı** | `trustia_sdk/perception/calmcar_bridge.py` | Yurt dışı bulut sunucularına ham görüntü ve konum sızıntısını donanımsal engelleme |
| **19** | **Kapalı Kutu (.pyc) & HMAC ECU Kilidi** | `build_enterprise_sdk.py` & `licensing.py` | Sıfır kaynak kod ifşası; hedef araç bilgisayarına (UUID/MAC) kilitli ikili dağıtım |
| **20** | **1.307 + 21 Otomatik Doğrulama Süiti** | `01_Core/tests/` & `02_SDK/tests/test_sdk.py` | Toplam **1.328 testte %100 başarı**, 0 hata, 0 başarısızlık |

---

## 🚕 5. Referans Araç Platformları: SAIC Maxus MIFA 7 & Hyundai Ioniq 5

Evrensel Otonomi Mimarisi (Kod Değişmezliği İlkesi) sayesinde çekirdek algoritmalar değiştirilmeksizin yalnızca `YAML` ve `DBC` dosyaları üzerinden farklı şasilere entegre edilir:

| Teknik Parametre | Platform 1: SAIC Maxus MIFA 7 (Robotaksi MPV) | Platform 2: Hyundai Ioniq 5 (E-GMP Robotaksi SUV) |
| :--- | :--- | :--- |
| **Konfigürasyon Dosyası** | `02_Trustia_Robotaxi_SDK/config/maxus_mifa7.yaml` | `01_Trustia_Otonom_Yazilim_Core/config/vehicle_config.yaml` |
| **CAN-FD DBC Sözlüğü** | `02_Trustia_Robotaxi_SDK/canbus/maxus_mifa7_chassis.dbc` | `01_Trustia_Otonom_Yazilim_Core/control/dbc_encoder.py` |
| **Dingil Mesafesi (Wheelbase)** | `2.975 m` (7 Kişilik Elektrikli Robotaksi MPV) | `3.000 m` (E-GMP Elektrikli Crossover) |
| **Sürüş & Emniyet Bilgisayarı** | CalmCar Horizon J6P (560 TOPS) + Trustia ASIL-D Arbiter | NVIDIA Jetson AGX Orin Industrial 64GB (275 TOPS) |
| **3D LiDAR & Zaman Senkronu** | Hesai / Ouster 128-Kanal + IEEE 1588v2 PTP ($<1\ \mu\text{s}$) | Ouster OS2-128 + 2x Livox Mid-360 Kör Nokta LiDAR |
| **Şasi Aktüatör Arayüzü** | ISO 11898-1 CAN-FD (`0x1A0` EPS, `0x1A1` IPB Fren, `0x010` HB) | ISO 11898-1 CAN-FD (100 Hz MDPS Direksiyon & i-Booster) |
| **Sürücü Devralma Eşikleri** | Direksiyon $\ge 3.5\text{ Nm}$ veya Fren $\ge 8.0\text{ bar}$ ($\le 5\text{ ms}$) | Direksiyon $\ge 2.5\text{ Nm}$ veya Fren $\ge 3.0\text{ bar}$ ($\le 5\text{ ms}$) |

---

## 🧪 6. 1.307 + 21 (1.328) Otomatik Doğrulama Hattı (%100 Yeşil)

Yapılan her kod revizyonunda hem ana otonomi çekirdeğindeki **1.307 test** hem de Robotaksi SDK paketindeki **21 alt sistem testi** otomatik olarak koşturulur:

```bash
# 1. Ana Seviye-4 Otonomi Çekirdeği Testleri (48 Test Dosyası / 1.307 Test)
cd 01_Trustia_Otonom_Yazilim_Core
pytest tests/ -q
# Çıktı: 1307 passed in 39.06s (100% PASS, 0 FAILURE, 0 ERROR)

# 2. SAIC Maxus MIFA 7 Robotaksi SDK Testleri (21 Alt Sistem Testi)
cd ../02_Trustia_Robotaxi_SDK
pytest tests/test_sdk.py -v
# Çıktı: 21 passed in 0.45s (100% PASS, 0 FAILURE, 0 ERROR)
```

| Doğrulama Katmanı | Test Dosyası | Test Sayısı | Durum | Kapsanan Mühendislik ve Güvenlik Standartları |
| :--- | :---: | :---: | :---: | :--- |
| **Algı, 3D Zemin & OBB Kümeleme** | 8 Dosya | 210 Test | ✅ **%100 Yeşil** | ISO 23150, RANSAC, DBSCAN, Çoklu Nesne İzleme (MOT) |
| **GNSS-Denied 3D NDT SLAM & ESKF** | 7 Dosya | 185 Test | ✅ **%100 Yeşil** | 400 Hz Hata Durum Kalman Filtresi & Tünel Odometrisi |
| **Kinematik Hibrit A* & Planlama** | 8 Dosya | 224 Test | ✅ **%100 Yeşil** | Akerman Kısıtları, Quintic Polinom & Davranış Ağacı |
| **Pure Pursuit, Stanley & MPC Kontrol** | 9 Dosya | 248 Test | ✅ **%100 Yeşil** | 100 Hz Yanal/Boyuna İzleme & Aktüatör Doyum Sınırları |
| **SocketCAN CAN-FD & ROS 2 Köprüsü** | 6 Dosya | 196 Test | ✅ **%100 Yeşil** | ISO 11898-1:2015, DBC Kodlama, CRC-16 & SecOC |
| **ISO 26262 ASIL-D MRM & Watchdog** | 5 Dosya | 144 Test | ✅ **%100 Yeşil** | 50 ms Zaman Aşımı, $1.5\text{ m/s}^2$ MRM & 5 ms E-Stop |
| **Kaos, Stres & SIL/HIL Simülasyonu** | 5 Dosya | 100 Test | ✅ **%100 Yeşil** | Sensör Körleşmesi, Paket Kaybı & Çoklu Arıza Enjeksiyonu |
| **Robotaksi SDK (21 L4 Alt Sistem)** | 1 Dosya | 21 Test | ✅ **%100 Yeşil** | AB 2022/1426, UN R155/R156/R157, SOTIF, RSS, 5G Teleop |
| **GENEL TOPLAM** | **49 Dosya** | **1.328 Test** | **%100 BAŞARI** | **0 Başarısızlık • 0 Hata • Tam Deterministik Güvence** |

---

## ⚡ 7. Hızlı Başlangıç & Komut Satırı (CLI) Kullanımı

### A. Seviye-4 Çekirdek (`01_Trustia_Otonom_Yazilim_Core`)
```bash
cd 01_Trustia_Otonom_Yazilim_Core

# 1.307 doğrulama testini çalıştırın
python trustia_cli.py test

# Hyundai Ioniq 5 CAN-FD otonom sürüş döngüsünü başlatın
python trustia_cli.py robotaxi

# ASIL-D fonksiyonel emniyet denetimini çalıştırın
python trustia_cli.py audit

# Donanım kilitli kapalı kutu (.pyc) B2B SDK paketini derleyin
python tools/build_enterprise_sdk.py
```

### B. SAIC Maxus MIFA 7 Robotaksi SDK (`02_Trustia_Robotaxi_SDK`)
```bash
cd 02_Trustia_Robotaxi_SDK

# 21 alt sistem testini çalıştırın
python robotaxi_cli.py test

# 20 maddelik uluslararası Seviye-4 & AB 2022/1426 sertifikasyon denetimini çalıştırın
python robotaxi_cli.py audit

# 100 Hz CAN-FD otonom sürüş döngüsünü çalıştırın
python robotaxi_cli.py drive

# Canlı Robotaksi mühendislik kokpitini (GUI) başlatın
python robotaxi_cli.py cockpit

# Müşteri teslimatına hazır kapalı kutu (.pyc) ZIP paketini üretin
python build_closed_box_sdk.py
```

---

## 🏢 8. Kurumsal Yönetişim, Fikri Mülkiyet & İletişim

* **Kurucu, Tek Pay Sahibi ve Sistem Mimarı:** **Murat Furkan Bayram** (%100 Şirket Hissesi ve Fikri Sermaye Sahibi).
* **Fikri Mülkiyet Koruması:** 5846 Sayılı Fikir ve Sanat Eserleri Kanunu (FSEK m.8), 6769 Sayılı Sınai Mülkiyet Kanunu (Ticari Sır), Uluslararası Bern Sözleşmesi (181 Ülke) ve Open Invention Network (OIN 2.0 `#f1e445769a9934114db095c4f5430a0e749d8201`) patent savunma paktı kapsamındadır.
* **Ar-Ge Yerleşkeleri:**
  * **İTO BTM:** Fulya Derin Teknoloji Kampüsü, Şişli / İstanbul
  * **Teknopark İstanbul:** Cube Incubation Kuluçka Merkezi, Pendik / İstanbul
* **Resmi E-Posta:** `iletisim@trustia.com.tr` • `entegrasyon@trustia.com.tr` • `hukuk@trustia.com.tr`
* **Kurumsal Telefon:** +90 537 064 0460
* **Resmi Web Platformu:** [https://trustia.com.tr](https://trustia.com.tr)

---
*© 2026 Trustia AI Technologies. Tüm hakları saklıdır.*
