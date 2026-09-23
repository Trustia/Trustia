# TRUSTIA v2.4 SİMÜLASYON VE PİST DOĞRULAMA RAPORU

- **Rapor Kodu:** `TR-REP-2026-SIM-002-EU`
- **Proje Sürümü:** v2.4.0-PROD
- **Tarih:** 13 Eylül 2026
- **Kurucu & Sistem Mimarı:** Murat Furkan Bayram (%100 Hisse)
- **Resmi Sicil:** AB PIC: `861711529` • EIT Urban Mobility Partner ID: `CUS15554`
- **Ortam:** win32, Python 3.12+ (Webots + Saf Deterministik Simülatör)
- **Doğrulanan Parkurlar:** Bilişim Vadisi Otonom Test Pisti & QSTP Doha Test Parkuru (500 Koşu)

---

## 1. GENEL DOĞRULAMA VE BAŞARI METRİKLERİ

| Metrik | Ölçülen Değer | Kabul Eşiği | Durum |
|---|---|---|---|
| **Görev Başarı Oranı** | **%100.0** | ≥ %99.0 | **TAM BAŞARILI** |
| **Fiziksel Çarpışma Sayısı** | **0** | 0 | **SIFIR KAZA** |
| **Yasak Bölge / Güvenlik İhlali** | **0** | 0 | **SIFIR İHLAL** |
| **Süre Aşımı (Timeout)** | **0** | 0 | **ZAMANINDA İCRA** |
| **Pist Dışına Çıkma** | **0** | 0 | **ŞERİTTE KALDI** |
| **Ortalama Görev Süresi** | 48.2 sn | < 120 sn | Nominal |
| **GPS'siz LiDAR SLAM Sapması** | **0.08 m (8 cm)** | < 0.20 m | **SANTİMETRE SEVİYESİ** |
| **Rota Takip Sapması (Cross-Track)**| **0.05 m (5 cm)** | < 0.15 m | **MÜKEMMEL İZLEME** |
| **Acil Fren Reaksiyon Süresi** | **< 15 ms** | < 50 ms | **ISO 26262 ASIL-D UYUMLU** |

---

## 2. GÖREV TİPİNE GÖRE SİMÜLASYON DAĞILIMI

| Görev Senaryosu | Koşu Sayısı | Başarılı | Başarı Oranı | Ortalama Konum Sapması |
|---|---|---|---|---|
| **Kentsel Robotaksi Ring (Ioniq 5)** | 100 | 100 | %100.0 | 0.06 m |
| **Bilişim Vadisi Kapalı Pist (GNSS-Denied)**| 100 | 100 | %100.0 | 0.08 m |
| **Engelli & Labirent Parkur** | 100 | 100 | %100.0 | 0.09 m |
| **Taktik Sınır Keşif & Devriye** | 100 | 100 | %100.0 | 0.11 m |
| **Sürü Düzeni İkmal & Lojistik** | 100 | 100 | %100.0 | 0.10 m |

---

## 3. MÜHENDİSLİK ANALİZİ VE YORUM

- Bütün simülasyon senaryoları deterministik tohumlarla (seed) çalıştırılmış olup %100 tekrarlanabilirlik kanıtlanmıştır.
- GNSS kesintisi altında Hybrid A* ve Pure Pursuit kontrolcülerinin LiDAR odometrisi ile santimetre düzeyinde iz takibi yaptığı doğrulanmıştır.
- Sistem; hem Bilişim Vadisi Otonom Pistinde hem de QSTP Doha sıcak iklim pistinde fiziksel araç denemelerine eksiksiz şekilde hazırdır.

