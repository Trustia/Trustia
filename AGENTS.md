# TRUSTIA PROJESİ ÇALIŞMA VE MİMARİ REHBERİ (AGENTS.md)

> [!NOTE]
> Bu rehber, Trustia Seviye-4 Otonom Sürüş projesinde çalışan yapay zeka asistanları (AI Agents) ve sistem mimarları için bağlayıcı çalışma prensiplerini ve kurumsal hafızayı belirler.
> **Son Güncelleme:** 28 Ekim 2026 | **Sürüm:** v4.4 (Enterprise L4 Core & Robotaxi SDK — 203 Dosya / 31.400+ Satır)

---

## 🎯 6 TEMEL MÜHENDİSLİK VE ÇALIŞMA İLKESİ

### 1. ANA KLASÖR DÜZENİ (TEMİZ REPO MİMARİSİ)
Tüm proje varlıkları istisnasız aşağıdaki ana dizinler altında organize edilir:
1. **`01_Trustia_Otonom_Yazilim_Core/`**: Seviye-4 otonomi yazılımı (C++20/ROS2/Python), 1.324 testlik doğrulama kütüphanesi, CenterPoint/BEV 3B derin algı, 7-DOF EKF takip, 3s yörünge tahmini, ISO 21448 SOTIF monitörü, CAN-FD sürücüleri, 3D LiDAR SLAM ve Enterprise SDK derleyicisi.
2. **`02_Trustia_Robotaxi_SDK/`**: SAIC Maxus MIFA 7 & Çoklu Şasi Seviye-4 Robotaksi Değerlendirme SDK'sı (21 alt sistem, 21 doğrulama testi, Closed-Box SDK paketleyici).
3. **`02_Trustia_Web_Platformu/`**: Kurumsal web sitesi (`website/`, Next.js 16, React 19 ve 3D Three.js telemetri arayüzü).
4. **`Kurumsal/`**: Resmi devlet, savunma ve akreditasyon belgeleri (`Belgeler/`, `Sunumlar/`, `Basvurular/`, `Medya/`).
* *Kök dizine veya masaüstüne geçici, döküntü veya mükerrer dosya bırakılamaz.*

### 2. B2B ENTERPRISE SDK & FİKRİ MÜLKİYET (IP) KORUMA KURALI
* Alıcılara (OEM'ler, filo işletmecileri, belediyeler, savunma firmaları) **asla açık kaynak `.py` kodu teslim edilmez**.
* Dağıtım sadece `tools/build_enterprise_sdk.py` ile üretilen derlenmiş kapalı kutu (`.pyc` bytecode), HMAC-SHA256 donanım kilidi (Hardware-Locked) ve şifrelenmiş lisans dosyası formatında yapılır.
* Kaynak kodlar şirketin en değerli sermayesidir; repodaki açık kaynak dosyaları korunur, müşteriye yalnızca kapalı paket sunulur.

### 3. EVRENSEL OTONOMİ MİMARİSİ (KOD DEĞİŞMEZLİĞİ)
* Otonomi çekirdeğindeki matematiksel ve algoritmik modeller (Pure Pursuit, Hybrid A*, 3D NDT SLAM) araca veya sahaya göre **değiştirilmez**.
* Araç boyutları (dingil mesafesi, maksimum dönüş açısı), hız limitleri ve CAN parametreleri sadece ve sadece **`config/vehicle_config.yaml`** üzerinden yönetilir.
* Yazılım; hem şehir içi Robotaksiyi (50 km/s), hem fabrika içi ağır yük AGV'sini (15 km/s), hem de havalimanı ring servisini aynı çekirdekle çalıştırır.

### 4. 1.345 TESTİN KESİNTİSİZ %100 YEŞİL KALMASI
* Yapılan her kod değişikliğinden sonra `pytest tests/ -q` komutu koşturulmalı ve **1.324 Core + 21 Robotaxi SDK testinin tamamının (1.345 test - %100) yeşil geçtiği** teyit edilmelidir.
* 0 başarısızlık (0 failure) ve 0 hata (0 error) kuralı esnetilemez.

### 5. OTOMOTİV EMNİYET VE ASIL-D FAILSAFE GÜVENCESİ
* 50 ms kontrol zaman aşımı (Watchdog), 1.4 ms CAN-FD mesaj gecikmesi, 1.5 m/s² kontrollü sağa çekme yavaşlaması (Minimal Risk Maneuver - MRM), ISO 21448 SOTIF hayalet engel baskılama ve acil frenleme (E-Stop) emniyet katmanları asla devre dışı bırakılamaz veya bypass edilemez.

### 6. DOĞRU BİLGİ VE KURUMSAL YÖNETİŞİM
* Uydurma, varsayıma dayalı veya doğrulanmamış bilgi yazılamaz.
* **Kurucu ve Tek Pay Sahibi:** Murat Furkan Bayram (%100 Hisse, Kurucu & CEO / Sistem Mimarı).

---

## 📁 DİZİN DÜZENİ VE SORUMLULUK HARİTASI

```text
Trustia/
├── 01_Trustia_Otonom_Yazilim_Core/    ← 20.800+ Satır L4 Çekirdek, 1.324 Test, CAN-FD Hyundai Ioniq 5
│   ├── ai/                            ← 3D Derin Algı (CenterPoint), 7-DOF EKF Takip & 3s Tahmin
│   ├── command/                       ← Robotaksi Filo Çağrı & Dağıtım Motoru
│   ├── control/                       ← Pure Pursuit / Stanley Yanal Kontrol & DBC Kodlama
│   ├── core/                          ← AutonomyCore Üst Düzey API & HMAC Donanım Lisanslama
│   ├── integration/                   ← SocketCAN CAN-FD Arabirimi & ROS 2 Köprüsü
│   ├── planning/                      ← Kinematik Hibrit A* & Dinamik Engel Kaçınma Planlayıcı
│   ├── security/                      ← ISO 26262 ASIL-D MRM & ISO 21448 SOTIF Plausibility Monitörü
│   ├── slam/                          ← GNSS-Denied 3D NDT Pose-Graph SLAM & 400Hz ESKF
│   ├── tests/                         ← 1.324 Adet Otomatik Birim & Entegrasyon Testi
│   └── tools/                         ← build_enterprise_sdk.py (Kapalı Kutu Dağıtım Aracı)
├── 02_Trustia_Robotaxi_SDK/           ← 3.310 Satır SAIC Maxus MIFA 7 L4 Robotaksi SDK, 21 Alt Sistem, 21 Test
├── 02_Trustia_Web_Platformu/          ← 7.024 Satır Web Platformu (Next.js 16, Three.js WebGL Telemetri)
├── Kurumsal/                          ← Birleşik Kurumsal ve Yasal Varlıklar
│   ├── Belgeler/                      ← Resmi Tescil, Tedarikçi ve Akreditasyon Belgeleri
│   ├── Sunumlar/                      ← Pitch Deck'ler, BOM Listeleri ve Mühendislik Planları
│   ├── Basvurular/                    ← Destek, Hibe ve Hızlandırma Takip Kütükleri
│   └── Medya/                         ← Yüksek Çözünürlüklü Kurumsal Logolar ve Videolar
├── .gitignore                         ← Temiz Git Dışlama Kuralları
├── AGENTS.md                          ← Yapay Zeka Asistanları ve Geliştirici Çalışma Rehberi
└── README.md                          ← Ana Kurumsal Tanıtım ve Mühendislik Dokümantasyonu
```

---

## 🧠 GÜNCEL KURUMSAL TESCİLLER & KALICI HAFIZA (12 EKİM 2026)

* **Kurucu & Sistem Mimarı:** Murat Furkan Bayram (%100 Mülkiyet, Tel: +90 537 064 0460, E-posta: `kariyer@trustia.com.tr` / `iletisim@trustia.com.tr`).
* **Resmi Akreditasyon ve Tescil Kütüğü:**
  * 🛡️ **ASELSAN A.Ş.:** Onaylı Tedarikçi Kütüğü (Firma Kodu: `#0050569`, SAP: `FZQHEXGFMTJU`).
  * 🇹🇷 **STM Savunma Teknolojileri:** Aday Tedarikçi Kütüğü.
  * 🇪🇺 **Avrupa Komisyonu:** Katılımcı Kimlik Kodu (`EU PIC: 861711529`).
  * 🇪🇺 **EIT Urban Mobility:** Partner ID (`CUS15554`).
  * 🚀 **Teknopark İstanbul (Cube Incubation):** Ön Kuluçka Girişimi & HASAT 2026 Hızlandırma Programı.
  * 🏛️ **İTO BTM (Fulya Derin Teknoloji Kampüsü):** Yerleşik Girişimci.
  * 🎓 **YTÜ Yıldız Teknopark:** Ekosistem ve Ön Kuluçka Başvurusu.
  * 🛡️ **Open Invention Network (OIN):** İmzalı İkili Patent Savunma Paktı Lisansı.
  * 📜 **KOSGEB:** İleri Girişimci Sertifikası (`KSB01UGE0115153370`).
  * 📜 **BTK:** Savunma Sanayii ve Yapay Zeka Sertifikasyonu (`L2zPtN4X1ZJ`).

---
*© 2026 Trustia AI Technologies. Tüm hakları saklıdır.*
