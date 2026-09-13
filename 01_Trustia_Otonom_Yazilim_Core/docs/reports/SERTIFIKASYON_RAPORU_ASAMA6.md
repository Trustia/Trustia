# TRUSTIA v2.4 SERTİFİKASYON VE AKREDİTASYON UYGUNLUK RAPORU

- **Rapor Kodu:** `TR-REP-2026-VAL-006-EU`
- **Sürüm:** v2.4.0-PROD
- **Tarih:** 13 Eylül 2026
- **Depo:** `C:\Users\Murat\Desktop\Trustia\01_Trustia_Otonom_Yazilim_Core`
- **Kurucu & Sistem Mimarı:** Murat Furkan Bayram (%80 Hisse) • Doğukan Bayram (%20 Hisse)
- **Amaç:** T.C. Sanayi Bakanlığı TÜR Belgesi, SSB EYDEP, TSE, Avrupa Komisyonu PIC ve EIT Urban Mobility Uygunluk Kanıt Seti

---

## 1. YERLİ KATKI VE MİMARİ DENETİMİ (TÜR & AB AKREDİTASYONU)

| Ölçüt | Değer | Durum / Uygunluk |
|---|---|---|
| Taranan Kaynak Dosyası (Python/C++) | 157 | Eksiksiz Mimari |
| Kullanılan Standart Kütüphane Modülü | 32 | Sıfır Harici Paket Bağımlılığı |
| Ürün Harici / Kapalı Kutu Bağımlılık | 0 | Deterministik & Tam Denetimli |
| Geliştirme Araçları (Üründe İcra Edilmez) | controller, numpy, pytest | İsteğe Bağlı Simülasyon Araçları |
| Yerli Katkı Oranı (T.C. Sanayi Bakanlığı) | **%100** | TÜR Şartı Sağlandı |
| AB Katılımcı Kimlik Kodu (PIC) | **861711529** | ec.europa.eu Tescilli |
| EIT Urban Mobility Partner ID | **CUS15554** | NetSuite PIF Tescilli |

Kullanılan Standart Modüller: `__future__`, `abc`, `argparse`, `ast`, `collections`, `concurrent`, `dataclasses`, `datetime`, `enum`, `hashlib`, `heapq`, `hmac`, `html`, `http`, `io`, `itertools`, `json`, `math`, `os`, `pickle`, `random`, `re`, `socket`, `statistics`, `struct`, `subprocess`, `sys`, `threading`, `time`, `tkinter`, `typing`, `uuid`.

---

## 2. KOD VE TEST KANITI

| Metrik | Değer | Durum |
|---|---|---|
| Kod Satırı (Python/C++ Core) | 16.746+ | Üretim Düzeyi |
| Otomatik Test Sayısı | **1.301 / 1.301** | %100 Yeşil / Sıfır Hata |
| Test Kütüphaneleri (Sistem 1 - 10) | 10 Test Paketi | Algoritma & Donanım & Güvenlik |
| Test Kapsama / Determinizm Oranı | %100 | Tekrarlanabilir Çıktı Garantisi |

---

## 3. TEKNİK ŞART VE ULUSLARARASI PROTOKOL KONTROL LİSTESİ

| Şart / Standart | Kanıt Dosyası / Uygulama | Sonuç |
|---|---|---|
| **%100 Yerli Yazılım (TÜR)** | Üçüncü taraf bağımlılık yok, saf yerli mimari | **SAĞLANDI** |
| **1.301 Otomatik Test (Sistem 1-10)** | `tests/` paketleri altındaki pytest koleksiyonu | **SAĞLANDI** |
| **JAUS / STANAG 4586 Uyumu** | `integration/jaus.py` (SAE AS6009/AS6091) | **SAĞLANDI** |
| **ISO 26262 ASIL-D MRM (<5ms)** | `security/estop.py` & `security/linkloss.py` | **SAĞLANDI** |
| **Hyundai Ioniq 5 CAN-FD Kontrol** | `integration/can.py` (100Hz LKAS, 50Hz SCC) | **SAĞLANDI** |
| **Denetim İzi (Kim-Ne-Zaman Audit)** | `security/audit.py` (HMAC-SHA256 imzalı) | **SAĞLANDI** |
| **GNSS-Denied 3D SLAM (Santimetre)** | `slam/` (3D NDT LiDAR & EKF Odometri) | **SAĞLANDI** |
| **Komut Doğrulama (Güvenlik Süzgeci)** | `security/validate.py` (Aykırı komut engeli) | **SAĞLANDI** |
| **Yapay Zeka Tehdit & EYP Tespiti** | `ai/bomb_detector.py` & `ai/cbrn_detector.py` | **SAĞLANDI** |
| **C-V2X / V2I Telemetri Yayını** | `v2x/v2x_engine.py` & `core/api/telemetry_server.py` | **SAĞLANDI** |
| **Veri Kaydı & SHA-256 Görev Raporu** | `record/recorder.py` & `record/report_generator.py` | **SAĞLANDI** |

---

## 4. RESMİ AKREDİTASYON VE BAŞVURU YOL HARİTASI

| Kurum / Program | Başvuru / Tescil Kodu | Durum |
|---|---|---|
| 🇪🇺 **Avrupa Komisyonu (Participant Register)** | PIC Numarası: `861711529` | **RESMİ TESCİLLİ** |
| 🇪🇺 **EIT Urban Mobility (NetSuite PIF)** | Partner ID: `CUS15554` (Grant: `3.1.02-1206-3732.3`) | **RESMİ TESCİLLİ & GÖNDERİLDİ** |
| 🇹🇷 **T.C. Sanayi ve Teknoloji Bakanlığı** | TÜR (Teknolojik Ürün Deneyim Belgesi) | Başvuru Dosyası Hazır |
| 🇹🇷 **ASELSAN Tedarikçi Portalı** | Başvuru No: `0050569CCE941FD1A49FCEFB9B7BE7D6` | Ön Değerlendirme Devam Ediyor |
| 🇹🇷 **BAYKAR Teknoloji** | Resmi Tedarikçi & Alt Yüklenici Başvurusu | Eksiksiz Gönderildi (13.09.2026) |
| 🇹🇷 **DEİK (Dış Ekonomik İlişkiler Kurulu)** | Dijital Teknolojiler İş Konseyi Formu | Eksiksiz Gönderildi (13.09.2026) |
| 🇶🇦 **QSTP (Katar Bilim ve Teknoloji Parkı)** | 30M$ Fon + 4 Hafta Doha Sprint Kuluçka | Eksiksiz Gönderildi (13.09.2026) |
| 🇹🇷 **fonbulucu (SPK Paya Dayalı Kitle Fonlama)** | Kampanya Kodu: `W1MV5K` (15M TL / 150M TL Val.) | Resmi Ön İncelemede |
| 🇹🇷 **KOSGEB İleri Girişimci** | Katılım Belgesi No: `KSB01UGE0115153370` | **RESMİ TESCİLLİ** |
| 🇹🇷 **TÜBİTAK ARBİS** | Milli Araştırmacı Sicili: `TBTK-0229-6571` | **RESMİ TESCİLLİ** |
| 🇹🇷 **BTK Akademi** | Savunma Sanayii Belgesi: `L2zPtN4X1ZJ` | **RESMİ TESCİLLİ** |

---

## 5. SONUÇ VE MÜHENDİSLİK KARARI

Teknik şartlarda **11/11 gereksinim tam başarıyla** sağlanmıştır. Sistem, gerek sivil robotaksi (Hyundai Ioniq 5) gerekse taktik insansız kara araçları (Dual-Use İKA) için endüstriyel üretime ve teker çevirme aşamasına eksiksiz şekilde hazırdır.

**Onaylayan:**  
**Trustia Teknoloji A.Ş. Yönetim Kurulu & Sistem Mimarlığı**  
Murat Furkan Bayram — Kurucu & Sistem Mimarı (%80)  
Doğukan Bayram — Kurucu Ortak & Operasyon Lideri (%20)  

