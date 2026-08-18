# TRUSTIA TEST RAPORU

- **Proje sürümü:** 0.1.0
- **Tarih:** 2026-08-03
- **Ortam:** win32, Python 3.12.10
- **Çalıştırma:** `pytest` (Sistem 7 rapor üretici)

## 1. SONUÇ ÖZETİ

| Kategori | Durum | Test | Geçti | Başarısız | Başarı Oranı | Süre (sn) |
|---|---|---|---|---|---|---|
| Sistem 6: Altyapı | GEÇTİ | 88 | 88 | 0 | %100.0 | 0.45 |
| Sistem 1: Otonomi Çekirdeği | GEÇTİ | 73 | 73 | 0 | %100.0 | 0.42 |
| **TOPLAM** | | **161** | **161** | **0** | %100.0 | **0.87** |

## 2. KAPSANAN SİSTEMLER

| Sistem | Modüller | Doğrulanan Yetenekler |
|---|---|---|
| Sistem 6: Altyapı | Messaging, Logging, Config, Timing, Transforms, Errors, API | Yayın/abone iletişim, döngülü log, öncelik zincirli ayar, monoton zamanlama, WGS84/UTM/ENU dönüşümleri, hata hiyerarşisi, komut arayüzü |
| Sistem 1: Otonomi Çekirdeği | Algı, SLAM, Planlama, Kontrol | LiDAR engel tespiti, GPS'siz odometri + işgal haritası, A*/RRT* rota, PID denetim + araç modeli |

## 3. METRİKLER (BU AŞAMADA ÖLÇÜLENLER)

| Metrik | Değer | Not |
|---|---|---|
| Otomatik test sayısı | 161 | Sistem 6 + Sistem 1 birim testleri |
| Test başarı oranı | %100.0 | Hedef %100 |
| Koordinat dönüşüm doğruluğu | <1e-7 derece | WGS84↔UTM gidiş-dönüş |
| Odometri entegrasyonu | <1e-9 m | Düz çizgi ve dairesel dönüş |
| A* rota bulma | %100 senaryo | Serbest alan + duvar dolanımı |
| Engel tespiti | Tek küme/tek engel | Kümeleme + tehlike skoru |
| PID denetim | Kararlı, antivindup | Kademe ve sınır testleri |

## 4. BAŞARISIZLIK ANALİZİ

Bu raporda başarısız veya hatalı test bulunmamaktadır.

Kampanya sırasında tespit edilip giderilen hatalar (geliştirme kaydı):

1. **Log motoru**: `dataclass` içe aktarımı eksikti → düzeltildi.
2. **UTM dönüşümü**: boylam serisinde `cos(phi1)` bölmesi eksikti (≈3 km sapma) → Karney serisi uygulandı.
3. **Algı filtresi**: 2D taramada tüm noktalar zemin sanılıp eleniyordu → elevation=0 koruması eklendi.
4. **A***: hücre anahtarlarında `round`/`int` tutarsızlığı duvar dolanımını kırıyordu → `int` ile hizalandı.
5. **RRT**: `_steer` çağrısında adım argümanı eksikti → eklendi.
6. **MessageBus**: öncelik sıralaması kuyrukta uygulanmıyordu → öncelik sıralı yerleştirme eklendi.

## 5. SÜRÜM VE KAPSAM NOTLARI

- Bu rapor, PLAN.md'nin 'Rapor Formatı' şartına uygun üretilmiştir.
- Kod ve testler C:\Users\Murat\Desktop\Yeni\trustia altındadır; tekrar üretim: `python -m pytest tests/`
- Sonraki aşama (AŞAMA 2, Sistem 2) simülasyon görev koşularını (10.000 koşu) bu çekirdek üzerinde başlatacaktır.
