# TRUSTIA SİMÜLASYON RAPORU (AŞAMA 2)

- **Proje sürümü:** 0.2.0
- **Tarih:** 2026-08-16
- **Ortam:** win32, Python 3.12.10
- **Görev koşusu sayısı:** 50
- **Dünya boyutu:** 40 x 40 m

## 1. GENEL SONUÇ

| Metrik | Değer |
|---|---|
| Görev başarı oranı | %100.0 |
| Çarpışma sayısı | 0 |
| Yasak bölge ihlali | 0 |
| Süre aşımı | 0 |
| Saha dışı | 0 |
| Ortalama görev süresi | 49.3 sn |
| GPS'siz konum hatası (ort) | 1.55 m |
| Rota sapması (ort) | 1.82 m |
| Engel tepki süresi (ort) | 0.000 sn |
| Minimum engel payı (ort) | 0.00 m |

## 2. GÖREV TİPİNE GÖRE DAĞILIM

| Görev tipi | Koşu | Başarı | Başarı Oranı | Konum Hatası (m) |
|---|---|---|---|---|
| devriye | 10 | 10 | %100.0 | 3.15 |
| engelli-parkur | 10 | 10 | %100.0 | 0.90 |
| gps-koridor | 10 | 10 | %100.0 | 0.87 |
| kesif | 10 | 10 | %100.0 | 1.70 |
| lojistik | 10 | 10 | %100.0 | 1.13 |

## 3. YORUM

- Görev başarı oranı %100 olmayan durumların her biri çarpışma/ihlal/süre analizine açıktır; tekrar üretim deterministik seed ile birebir tekrarlanabilir.
- GPS'siz koridor görevlerindeki konum hatası, odometri birikim hatası + LiDAR engel kaçınmasının etkileşimidir.
- Tüm koşular aynı koşucu (otonomi zinciri) ile üretildi: algı → SLAM → planlama → kontrol → araç.
