# 🛡️ TRUSTIA — ASELSAN & SSB EYDEP Tedarikçi ve Yerlileştirme Başvuru Paketi

**Belge Kodu:** `TRST-SUPP-2026-V2`  
**Başvuru Tipi:** ASELSAN "Gücümüz Bir" Tedarikçi & Yerlileştirme Programı / SSB EYDEP A Sınıfı Yazılım Tedarikçi Başvurusu  
**Başvuru Kodu (ASELSAN Portal):** `0050569CCE941FD1A49FCEFB9B7BE7D6`  
**Tarih:** 5 Eylül 2026  
**Gizlilik Derecesi:** HİZMETE ÖZEL / TİCARİ GİZLİ  

---

## 🏛️ 1. GİRİŞİM VEYA FİRMA KÜNYESİ & İZLEME KODLARI

| Metrik / Kayıt | Tanım / Kod | Durum |
|---|---|---|
| **Ürün/Platform Adı** | TRUSTIA — Milli Otonomi Platformu (v2.0 Askeri Sınıf) | Tamamlandı (Üretime Hazır) |
| **KOSGEB İleri Girişimcilik Sertifikası** | `KSB01UGE0115153370` (Tarih: 06.08.2026) | %100 Resmi Onaylı |
| **SSB & BTK Akademi Savunma Sanayii** | Sertifika No: `L2zPtN4X1ZJ` | 100/100 Tam Puan |
| **TÜBİTAK ARBİS Kaydı** | Araştırmacı Kimlik No: `TBTK-0229-6571` | Kayıtlı & Doğrulanmış |
| **ASELSAN Portal Başvuru Kodu** | `0050569CCE941FD1A49FCEFB9B7BE7D6` | İşlemde / Dosya Eki Hazır |
| **UK Dept for Business & Trade (GEP)** | UK Innovator Founder Visa Portfolio | Hazır |
| **Estonia Startup Visa / EU Residency** | Başvuru Kodu: `UKOR-OKJT-5597` | Kayıtlı |

---

## 📐 2. TEKNİK MİMARİ VE YERLİ OTONOMİ KABİLİYETLERİ

TRUSTIA, GPS/GNSS sinyalinin kesildiği, yanıltıldığı (jamming/spoofing) veya hiç bulunmadığı kapalı/çatışmalı alanlarda çalışmak üzere tasarlanmış **%100 Yerli Katkı Oranlı** insansız kara aracı (İKA) otonom sürüş ve komut-kontrol platformudur.

```text
                               TRUSTIA PLATFORMU
+-------------------------------------------------------------------+
|  SİSTEM 9: Yapay Zeka Algı & Askeri Tehdit Tespit Modülleri       |
|            (EYP/Mayın, CBRN Gaz Analizi, Hava-Kara Sürü)          |
+-------------------------------------------------------------------+
|  SİSTEM 1: Otonomi Çekirdeği (GPS'siz SLAM + Kinematik Rota)       |
+-------------------------------------------------------------------+
|  SİSTEM 8: Araç / Sensör Entegrasyonu (CAN, LiDAR, ROS 2, JAUS)   |
+-------------------------------------------------------------------+
|  SİSTEM 3: Komuta Merkezi (MIL-STD-2525 C2 Konsolu & Sesli Komut) |
|  SİSTEM 5: Siber Güvenlik (HMAC-SHA256, E-Stop, RTH Eve Dönüş)    |
+-------------------------------------------------------------------+
|  SİSTEM 6 & 7: Test & Sertifikasyon (1.301 Otomatik Test)         |
+-------------------------------------------------------------------+
```

### Öne Çıkan Askeri Kabiliyetler:
1. 📡 **GPS'siz 3D Poz Grafı SLAM (Position Graph SLAM):** Visual Odometry, Wheel Odometry ve LiDAR ICP Scan-Matching ile haritalama ve santimetre hassasiyetinde konumlanma.
2. 💣 **EYP, Mayın & Patlayıcı Tespiti (`ai/bomb_detector.py`):** Metal dedektör sinyali, termal anomali ve GPR derinlik yansıması sentezi ile EYP, Anti-Personel/Anti-Tank mayını ve tuzak teli tespiti; otomatik 30m karantina bölgesi izolasyonu.
3. ☢️ **KHKN / CBRN Tehdit Analizi (`ai/cbrn_detector.py`):** Radyasyon (Geiger) ve Kimyasal Harp Gazı (Sarin, VX) yayılım modellemesi ve rüzgar altı güvenli rotalama.
5. 🐝 **Hava-Kara Sürü Otonomisi (`ai/swarm.py`, `ai/air_ground_swarm.py`):** Çoklu İKA ve İHA keşif verisi entegreli lider-takipçi formasyon yönetimi.
5. 🗣️ **Taktik Sesli Komut Çözümleyici (`command/voice_command.py`):** Operatör sesli girdilerini doğrudan otonom sürüş görevlerine dönüştürme.
6. 🔒 **Siber Güvenlik & Acil Durdurma (`security/estop.py`, `security/linkloss.py`):** Kriptografik mesaj doğrulaması, E-Stop acil durma ve telsiz bağlantısı koptuğunda Otonom Eve Dönüş (Return-to-Home).

---

## 📜 3. ASKERİ STANDARTLAR VE SERTİFİKASYON UYUM MATRİSİ

| Standart / Şart | Sertifikasyon / Protokol | Modül Kanıtı | Durum |
|---|---|---|---|
| **SAE AS6091 / AS6009** | JAUS (Joint Architecture for Unmanned Systems) | `integration/jaus.py` | SAĞLANDI |
| **STANAG 4586** | NATO Birlikte Çalışabilirlik Standardı | Uyumlu Mesaj Yapısı | SAĞLANDI |
| **ROS 2 Bridge** | Open Robotics ROS 2 Humble/Jazzy Köprüsü | `integration/ros2_bridge.py` | SAĞLANDI |
| **CAN 2.0 / CAN FD** | ISO 11898 Sürücü & Aktüatör Katmanı | `integration/can.py` | SAĞLANDI |
| **TÜR Belgesi (TOBB)** | %100 Yerli Bağımlılıksız Kod Taraması | `core/certification.py` | **SAĞLANDI (%100)** |
| **MIL-STD-2525** | Askeri Semboloji Komuta Konsolu | `command/tactical_gui.py` | SAĞLANDI |
| **TSE TS ISO/IEC 25051** | Yazılım Kalite ve Test Şartı (1.000+ Test) | **1.301 Geçen Test** | **SAĞLANDI (%100)** |

---

## 📊 4. KALİTE GÜVENCE VE TEST DOĞRULAMA KANITLARI

- **Otomatik Birim ve Entegrasyon Test Sayısı:** 1.301 Adet (Tüm modüller kapsama altındadır)
- **Test Süresi:** ~43 saniye
- **Test Başarı Oranı:** **%100** (`1301 passed in 43.86s`)
- **Sertifikasyon Denetim Skoru:** **9 / 9 Şart SAĞLANDI**
- **Çalışma Zamanı Harici Bağımlılığı:** **0 (Sıfır Dış Bağımlılık / Saf Python)**

---

## 📑 5. RESMİ BAŞVURU EKLERİ VE DOSYA ENVANTERİ

Başvuru dosyası paketine aşağıdaki resmi teknik ve admi belgeler dahildir:

1. **Ek-1:** TRUSTIA Sertifikasyon Uygunluk Raporu (`docs/reports/SERTIFIKASYON_RAPORU_ASAMA6.md`)
2. **Ek-2:** %100 Yerli Katkı AST Bağımlılık Analizi Çıktısı
3. **Ek-3:** KOSGEB İleri Girişimcilik Sertifika Fotokopisi (`KSB01UGE0115153370`)
4. **Ek-4:** SSB & BTK Akademi 100/100 Tam Puan Başarı Sertifikası (`L2zPtN4X1ZJ`)
5. **Ek-5:** TÜBİTAK ARBİS Kayıt Belgesi (`TBTK-0229-6571`)
6. **Ek-6:** Yazılım Kalite, Güvenlik ve Mimari Raporları (`docs/reports/GUVENLIK_RAPORU_ASAMA4.md`, `YAPAYZEKA_RAPORU_ASAMA5.md`)

---

## ✍️ 6. BEYAN VE TAAHHÜT

İşbu dosyada sunulan TRUSTIA — Milli Otonomi Platformu (v2.0 Askeri Sınıf) yazılım mimarisinin, tüm kodlarının, test suite altyapısının ve yerlileştirme metriklerinin tarafımızca geliştirildiğini, herhangi bir kısıtlayıcı lisans içermediğini ve ASELSAN "Gücümüz Bir" Tedarikçi & Yerlileştirme Programı ve SSB EYDEP değerlendirmelerine eksiksiz hazır olduğunu beyan ve taahhüt ederiz.

**Tedarikçi Adayı:** TRUSTIA Otonomi Ekibi  
**İletişim / Portal Başvuru Kod:** `0050569CCE941FD1A49FCEFB9B7BE7D6`  
