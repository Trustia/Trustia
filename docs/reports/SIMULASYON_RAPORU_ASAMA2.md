# TRUSTIA SİMÜLASYON RAPORU (AŞAMA 2)

- **Proje sürümü:** 0.2.0
- **Tarih:** 2026-08-03
- **Ortam:** win32, Python 3.12.10
- **Görev koşusu sayısı:** 10000
- **Dünya boyutu:** 40 x 40 m

## 1. GENEL SONUÇ

| Metrik | Değer |
|---|---|
| Görev başarı oranı | %99.5 |
| Çarpışma sayısı | 23 |
| Yasak bölge ihlali | 1 |
| Süre aşımı | 6 |
| Saha dışı | 24 |
| Ortalama görev süresi | 66.1 sn |
| GPS'siz konum hatası (ort) | 1.62 m |
| Rota sapması (ort) | 2.34 m |
| Engel tepki süresi (ort) | 0.274 sn |
| Minimum engel payı (ort) | 1.31 m |

## 2. GÖREV TİPİNE GÖRE DAĞILIM

| Görev tipi | Koşu | Başarı | Başarı Oranı | Konum Hatası (m) |
|---|---|---|---|---|
| devriye | 2000 | 1985 | %99.2 | 3.16 |
| engelli-parkur | 2000 | 1987 | %99.4 | 1.31 |
| gps-koridor | 2000 | 1998 | %99.9 | 1.11 |
| kesif | 2000 | 1980 | %99.0 | 1.33 |
| lojistik | 2000 | 1996 | %99.8 | 1.18 |

## 3. YORUM

- Görev başarı oranı %100 olmayan durumların her biri çarpışma/ihlal/süre analizine açıktır; tekrar üretim deterministik seed ile birebir tekrarlanabilir.
- GPS'siz koridor görevlerindeki konum hatası, odometri birikim hatası + LiDAR engel kaçınmasının etkileşimidir.
- Tüm koşular aynı koşucu (otonomi zinciri) ile üretildi: algı → SLAM → planlama → kontrol → araç.
