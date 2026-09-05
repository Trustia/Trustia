# TRUSTIA AI — PAYA DAYALI KİTLE FONLAMASI KAMPANYA PLANI

**Girişim:** TRUSTIA AI (Milli Seviye 4 Otonom Sürüş & Savunma Robotikleri Yazılım Platformu)  
**Kurucu & CEO:** Murat Furkan Bayram (17 Yaşında, Sistem Mimarı)  
**Web Sitesi:** https://trustia.com.tr  
**LinkedIn:** https://www.linkedin.com/in/trustia  
**Tarih:** 5 Eylül 2026  

---

## 1. KAMPANYA ÖZETİ

| Parametre | Değer |
|-----------|-------|
| **Hedef Fon Tutarı** | 25.000.000 TL (~500.000 $ USD) |
| **Tavan Fon Tutarı (Overfunding)** | 40.000.000 TL |
| **Şirket Ön Değerlemesi (Pre-Money)** | 250.000.000 TL (~5.000.000 $ USD Post-Money SAFE) |
| **Yatırımcıya Teklif Edilen Pay Oranı** | %10 (25M TL / 250M TL Değerleme) |
| **Kampanya Süresi** | 60 Gün (Maksimum SPK Limiti) |
| **Hedef Platform(lar)** | fonbulucu.com / Fonangels / Startupfon |
| **SPK Yasal Üst Sınır** | 142.500.000 TL (2026) |

---

## 2. GİRİŞİM TANITIMI

### 2.1 Problem
1. **Yabancı Bağımlılık & Yüksek CAPEX:** Mevcut Seviye 4 otonom araçlar (Waymo, Cruise) araç başına 250.000$ - 350.000$ gibi devasa maliyetlerle sıfırdan üretilmektedir. Bu durum taksi filoları ve belediyeler için ölçeklenemez bir maliyet bariyeri oluşturur.
2. **GPS Kesintisi & Elektronik Harp:** Tünellerde, gökdelen kanyonlarında veya askeri sahalarda GPS sinyali kesildiğinde standart araçlar rotadan sapar.
3. **Mekanik Şasilere Yazılım Beyni:** Şasi üreticileri mükemmel mekanik araçlar yaparken, bunları Seviye-4 otonom yapacak yerli deterministik yazılım ve sensör köprüsüne sahip değildir.

### 2.2 Çözüm: Trustia Modüler Seviye-4 Dönüşüm Kiti
Trustia AI'ın geliştirdiği **tamamen yerli, %100 özgün, deterministik otonomi motoru ve donanım kiti** şu katmanlardan oluşur:

| Modül | Teknoloji | Standart |
|-------|-----------|----------|
| 🗺️ **GPS'siz 3D Poz Grafı SLAM** | 128 kanallı LiDAR + GMSL2 Kamera füzyonu ile 5cm hassasiyette haritalama | SAE J3016 Level 4 |
| ⚡ **CAN-FD Drive-by-Wire Köprüsü** | 100Hz LKAS_FD direksiyon ve 50Hz SCC_FD fren/gaz enjeksiyonu | ISO 11898-1 CAN-FD |
| 🧠 **Deterministik Rota Planlama** | <15ms Kinematic Hybrid A* & Pure Pursuit yörünge optimizasyonu | ASIL-D Deterministik |
| 🌧️ **Zorlu Hava Algılama** | 77 GHz Continental FMCW radar ağırlıklı sis/sağanak adaptasyonu | SAE J3131 |
| 🎮 **Teleoperasyon & C2 Konsolu** | WebRTC tabanlı, 100ms donanım korumalı uzaktan filo kontrolü | SAE J3216 |
| 🛡️ **Askeri İKA Otonomi Katmanı** | STANAG 4586, SAE JAUS AS6091 uyumlu insansız kara aracı beyni | NATO STANAG |

### 2.3 Kanıtlanmış Teknik Olgunluk

| Metrik | Değer |
|--------|-------|
| **Toplam Özgün Kod Satırı** | 16.000+ C++/Python |
| **Otomatik Doğrulanmış Test Sayısı** | 1.301 / 1.301 (%100 Başarı) |
| **Donanım Sepet Maliyeti (BOM)** | 32.800 $ USD (27 Doğrulanmış Parça) |
| **Teknolojik Olgunluk Seviyesi (TRL)** | TRL-6 (HIL & Simülasyonda Doğrulanmış) |

---

## 3. PAZAR BÜYÜKLÜĞÜ VE 3 KADEMELİ TİCARİ MODEL

### 3.1 Adreslenebilir Pazar (TAM / SAM / SOM)

| Pazar Katmanı | Boyut | Açıklama |
|---------------|-------|----------|
| **TAM (Toplam)** | $118 Milyar (2030) | Küresel otonom robotaksi ve insansız kara aracı pazarı |
| **SAM (Hedef)** | $15 Milyar | Türkiye, MENA, Avrupa savunma ve sivil otonom dönüşüm pazarı |
| **SOM (Ulaşılabilir)** | $50 Milyon (5 yıl) | İlk 500 robotaksi kiti + 50 askeri İKA lisansı ve AaaS gelirleri |

### 3.2 3 Kademeli Fiyatlama ve Gelir Modeli

1. **Tier 1: Sivil Seviye 4 Kiti (Temel Otonom Sürüş)**
   * **Kit Satışı (CAPEX):** 18.500 $ / kit (BOM: 11.500 $)
   * **AaaS (Yazılım Aboneliği):** 250 $ / ay (veya 0.12 $/km)
   * **Kullanım:** Kampüs içi servisler, kapalı alan lojistiği, havaalanı transferleri.

2. **Tier 2: Tam Seviye 4 Robotaksi Dönüşüm Kiti (Hyundai Ioniq 5)**
   * **Kit Satışı (CAPEX):** 35.000 $ / kit (BOM: 22.800 $, %35 brüt kâr)
   * **AaaS (Yazılım & Telemetri):** 450 $ / ay (veya 0.18 $/km)
   * **Kullanım:** Ticari taksi filoları, belediye toplu taşıma, kiralık filolar.
   * **Filo Sahibi ROI:** 14 ayda tüm araç ve kit yatırımının kendini amorti etmesi.

3. **Tier 3: NATO STANAG Askeri İKA & Ağır Sanayi Kiti**
   * **Donanım Kiti:** 55.000 $ / kit (BOM: 32.800 $)
   * **Özel Savunma Entegrasyonu:** 250.000 $ – 1.000.000 $ / proje
   * **Taktik Destek & AaaS:** 1.200 $ / ay
   * **Kullanım:** T.C. Savunma Sanayii Başkanlığı, TSK, ASELSAN, Otokar, BMC, FNSS askeri İKA platformları.

---

## 4. RESMİ AKREDİTASYONLAR VE TESCİLLER

| Kurum | Belge / Tescil | Kod / Statü |
|-------|----------------|-------------|
| 🛡️ **T.C. Savunma Sanayii Başkanlığı** | 100/100 Tam Puan Sınav Tescili | `L2zPtN4X1ZJ` |
| 📜 **KOSGEB** | İleri Girişimcilik Tescil Belgesi | `KSB01UGE0115153370` |
| 🔬 **TÜBİTAK ARBİS** | Ulusal Araştırmacı Kaydı | `TBTK-0229-6571` |
| 🏭 **ASELSAN** | Resmi Tedarikçi Portalı Kaydı | Aktif Onaylı Girişim |
| 🏢 **İTO BTM** | Ön Kuluçka 2026 II. Dönem Kabulü | İTO BTM Fulya Kampüsü |
| 📊 **Startups.watch** | Resmi Doğrulanmış Girişim | Mobilite & Derin Teknoloji |

---

## 5. KURUCU VE YÖNETİM EKİBİ

### Murat Furkan Bayram — Kurucu & CEO / Sistem Mimarı (%80 Hisse)
* **Yaş:** 17 (Doğum: 4 Şubat 2009)
* **Rol:** 16.000 satır otonomi motoru, SLAM, Hybrid A*, CAN-FD ve yapay zeka algoritmalarının mimarı.
* **Başarılar:** SSB 100/100 Tam Puan, KOSGEB İleri Girişimci, TÜBİTAK ARBİS Ulusal Araştırmacı.

### Doğukan Bayram — Kurucu Ortak & Operasyon (%20 Hisse)
* **Rol:** Reşit kurucu ortak. Resmi süreçler, operasyonel yönetim, fon ilişkileri ve organizasyon süreçlerinin koordinasyonu.

### Denizcan Özcan — Baş Donanım & Robotik Entegrasyon Mühendisi (1. Öncelikli Havuz)
* İstanbul Üniversitesi-Cerrahpaşa EEE (3.44 GPA) | ASELSAN Mühendislik Havuzu & TEKNOFEST Robotaksi Finalisti.
* Uzmanlık: CAN-FD Drive-by-Wire, sensör kablolama, FPGA ve araç gövde entegrasyonu.

---

## 6. FONLARIN KULLANIM PLANI (25.000.000 TL / ~500.000 $ USD)

| Kalem | Tutar (TL) | Tutar (USD) | Oran | Açıklama |
|-------|------------|-------------|------|----------|
| 🚗 **Donanım & Sensör Kiti Alımı** | 11.250.000 TL | 225.000 $ | %45 | İlk 2 adet Hyundai Ioniq 5 test filosunun tam dönüşümü ve 27 parçalık Seviye-4 sensör stoğu |
| 👨‍💻 **Çekirdek Mühendislik Ekibi** | 8.750.000 TL | 175.000 $ | %35 | Gömülü yazılım, SLAM, ROS2 ve donanım test mühendisleri (18 aylık operasyonel maaş) |
| 🏁 **Pist & Saha Test Operasyonları** | 3.750.000 TL | 75.000 $ | %15 | Bilişim Vadisi test pisti kiralama, Dubai World Challenge saha lojistiği ve kapalı pist testleri |
| 📋 **Fikri Mülkiyet & ASIL-D Validasyon** | 1.250.000 TL | 25.000 $ | %5 | ISO 26262 ASIL-D güvenlik denetimleri, uluslararası PCT patent tescilleri ve TÜR Belgesi |
| **TOPLAM** | **25.000.000 TL** | **500.000 $** | **%100** | **18 Aylık Tam Operasyonel Pist ve Ticari Dağıtım Bütçesi** |

---

## 7. YOL HARİTASI (ROADMAP)

| Dönem | Hedef & Çıktı |
|-------|---------------|
| **Q4 2026** | Hyundai Ioniq 5 Seviye-4 dönüşümü, İTO BTM Fulya Kampüsü Ar-Ge sahası, Dubai RTA World Challenge finalistliği |
| **Q1 2027** | Bilişim Vadisi kapalı pistinde 60 km/s slalom, yaya kaçınma ve ASIL-D MRM acil durum fren demoları |
| **Q2 2027** | Savunma Sanayii / Askeri İKA Seviye-4 entegrasyonu (ASELSAN / Otokar PoC) ve TÜR Belgesi |
| **Q3 2027** | Dubai RTA Dünya Kongresi canlı robotaksi demosu ve 1.200.000 $ ödül finali |
| **Q4 2027** | Seri A / Global Büyüme Turu ($3M-$5M), ilk 80 araçlık ticari robotaksi filo dönüşümü |
| **2028 - 2030** | 500+ araçlık küresel robotaksi ve askeri İKA filosu, AaaS sürekli yazılım abonelik operasyonları |

---

## 8. HEDEF KİTLE FONLAMA PLATFORMLARI (SPK LİSANSLI)

| Platform | Lisans Tarihi | Web Sitesi | Odak Alan |
|----------|---------------|------------|-----------|
| **fonbulucu** | SPK Onaylı | fonbulucu.com | Teknoloji & Derin Teknoloji |
| **Fonangels** | 24.02.2022 | fonangels.com | Yapay Zeka & Robotik |
| **Startupfon** | 28.09.2023 | startupfon.com | Erken Aşama Teknoloji |
| **Fongogo** | 06.01.2022 | fongogo.com | Genel Teknoloji |
| **Startupcentrum** | 19.09.2024 | startupcentrum.com | Derin Teknoloji |

---

## 9. KAMPANYA STRATEJİSİ

### Aşama 1: Ön Hazırlık (Eylül 2026)
* BTM şirketleşme ve tüzel kişilik danışmanlığı ile resmi şirket kuruluşu ve tescili.
* Profesyonel 3 dakikalık kampanya tanıtım videosu çekimi.
* SPK Bilgi Formu ve mali projeksiyon tabloları hazırlığı.

### Aşama 2: Platform Başvurusu (Ekim 2026)
* fonbulucu ve/veya Fonangels'a girişimci başvurusu.
* Yatırım Komitesi sunumu (30 dakika pitch).
* Kampanya sayfası tasarımı (web sitesi, video, teknik demo GIF'leri).

### Aşama 3: Canlı Kampanya (Kasım - Aralık 2026)
* 60 günlük canlı fonlama dönemi.
* Sosyal medya, LinkedIn, Twitter ve teknoloji basını (Webrazzi, ShiftDelete) PR kampanyası.
* Haftalık yatırımcı güncelleme bültenleri.
* TURKCOMPOSITE 2026 fuarında (21-23 Ekim) canlı tanıtım.

### Aşama 4: Kapanış & Şirketleşme (Ocak 2027)
* Hedef tutara ulaşıldığında Takasbank'tan şirket hesabına fon transferi.
* Test aracı tedariki ve mühendislik ekibi istihdamına başlangıç.

---

## 10. YASAL UYARI VE RİSK BİLGİLENDİRMESİ

Bu belge, T.C. Sermaye Piyasası Kurulu (SPK) düzenlemeleri çerçevesinde hazırlanmış bir **ön hazırlık ve strateji dokümanıdır**. Resmi kampanya başlatılmadan önce SPK Tebliği (III-35/A.2) uyarınca detaylı "Paya Dayalı Kitle Fonlaması Bilgi Formu" hazırlanacak ve yetkili platform tarafından onaylanacaktır.

---

*Hazırlayan: Murat Furkan Bayram — Trustia AI Kurucusu & Sistem Mimarı*  
*İletişim: iletisim@trustia.com.tr | https://trustia.com.tr*
