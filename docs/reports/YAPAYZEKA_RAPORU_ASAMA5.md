# TRUSTIA YAPAY ZEKA RAPORU — AŞAMA 5

- **Proje:** TRUSTIA Otonom Araç Platformu (MVP, saf Python — dış bağımlılık yok)
- **Tarih:** 2026-08-03
- **Kapsam:** Sistem 9 (Yapay Zeka Algı) + Sistem 7 (Test Altyapısı tamamlama)
- **Durum:** AŞAMA 5 TAMAMLANDI

---

## 1. AŞAMA HEDEFİ (PLAN 3.2, Satır 131/129)

| Sistem | Plan Bileşenleri | Bu Aşamada Gerçekleşen |
|---|---|---|
| Sistem 9: Yapay Zeka Algı (100.000 satır plan) | Derin öğrenme modelleri, eğitim altyapısı, arazi sınıflandırma, nesne tanıma | MiniMLP (saf Python, ileri+geri yayılım, SGD), sentetik veri üretici, eğitim-keşif iş akışı, 6 sınıflı arazi sınıflandırıcı, geçilebilirlik (traversability) haritası, LiDAR küme nesne tanıma, gündüz/gece sensör füzyonu |
| Sistem 7: Test Altyapısı (170.000 satır plan) | 1.000+ otomatik test, simülasyon doğrulama, performans ölçümleri, rapor üretici | **1.246 otomatik test**, 66 görev koşusu doğrulama matrisi, 582 senaryo üretim matrisi, zaman bütçesi testleri, rapor üretici ayrıştırıcı düzeltmesi |

## 2. MODÜL ENVANTERİ (`ai/` paketi)

| Modül | Görev |
|---|---|
| `ai/mlp.py` | `MiniMlp`: tam bağlı ağ, tanh + softmax, cross-entropy, minibatch SGD, JSON serileştirme. Geri yayılım gradyanları sonlu fark ile test edildi |
| `ai/features.py` | `lidar_features`, `terrain_cell`, `cluster_shape`, `thermal_signal`, `pixel_darkness` — sınıflandırıcı girdi öznitelikleri |
| `ai/training.py` | Sentetik Gauss veri üretimi, veri bölme, `train_classifier`, karışıklık matrisi, model kaydet/yükle |
| `ai/traversability.py` | 6 arazi sınıfı (asfalt/çimen/çamur/kaya/çukur/su), geçilebilirlik skorları, `TraversabilityMap` (planlama maliyeti) |
| `ai/object_detector.py` | Küme şekli → nesne sınıfı (araç/insan/bilinmeyen engel), güven eşiği, en yakın tehlike |
| `ai/fusion.py` | RGB + termal tespitleri birleştirme; gece termal, gündüz RGB ağırlıklı |

## 3. ÖLÇÜLEN METRİKLER

| Metrik | Değer | Not |
|---|---|---|
| Otomatik test sayısı | **1.246** (tamamı yeşil) | Hedef 1.000+ — AŞAMA 4'te 306 idi |
| Test başarı oranı | %100 | `python -m pytest tests -q` |
| Tam süit süresi | ~3 dk 50 sn | 66 görev koşusu + 582 senaryo doğrulaması dahil |
| MLP eğitim doğruluğu (ara) | %93.9 | 240 örnek, 60 epoch, 6 sınıf |
| MLP keşif (eval) doğruluğu | %91.7 | %25 ayrılmış veri |
| Kural tabanlı sınıflandırma | %94.2 | Merkez mesafesi eşleştirme |
| XOR öğrenimi (model sağlık testi) | %100 | 5 tohumda tekrarlanabilir |
| Geri yayılım doğruluğu | < 1e-4 | Analitik ↔ sonlu fark karşılaştırması |
| Nesne tanıma | araç %100, insan %93 güven | LiDAR küme öznitelikleri |
| Görev koşusu (kesif, seed 11) | Başarılı, 22 adım, 2.2 s | Konum hatası 0.05 m, rota sapması 0.16 m |
| Geçilebilirlik haritası | 64 hücre, %42 geçilebilir | Rastgele özniteliklerle üretildi |
| Adım maliyeti (simülasyon) | < 10 ms | 10 Hz gerçek zaman bütçesinin altında |

## 4. GÖREV KOŞUSU DOĞRULAMA MATRİSİ (Sistem 7)

- 5 görev tipi (devriye, kesif, lojistik, engelli-parkur, gps-koridor) × tohum seçkisi: **66 bağımsız koşu**
- Her koşu iddiası: başarı, çarpışma yok, yasak bölge ihlali yok, süre aşımı yok, sıkışma yok, saha içi, ≥1 rota noktasına ulaşım
- Senaryo üretim matrisi: 5 tip × 40 tohum = 200 geçerli görev tanımı + sınır/üretim sağlığı doğrulaması (582 test)

## 5. BAŞARISIZLIK ANALİZİ

Bu raporda başarısız test yoktur. Geliştirme sırasında yakalanıp giderilen hatalar:

1. **MLP `_backward`**: girdi katmanı aktivasyonları karışıyordu → katmana göre girdi seçimi düzeltildi.
2. **MLP gradyan tamponları**: tuple (değişmez) üzerine yazım hatası → değişebilir liste kullanımı.
3. **`_dot` artığı**: geliştirme sırasında yarım bırakılmış kod → nöron başına hesaplama ile temizlendi.
4. **Nesne merkezleri**: öznitelik merkezleri ölçümlü küme örnekleriyle hizalanmadığında insan araçla karışıyordu → gerçek küme istatistiklerine göre yeniden kalibre edildi.
5. **Füzyon boş senaryo**: sensör yokken gündüz seviyesi 0 kalıyordu → varsayılan 1.0.
6. **`parse_summary` (rapor üretici)**: `"306 passed,"` gibi virgüllü çıktılar ayrıştırılamıyordu → regex tabanlı ayrıştırıcı.
7. **Traversability maliyet**: geçilmez hücre 20.0 ile sınırlanıyordu → 50.0 (1/0.02).

## 6. SÜRÜM VE KAPSAM NOTLARI

- Bu rapor, PLAN.md "Rapor Formatı" şartına uygundur (başlık, senaryo listesi, metrik tablosu, başarısızlık analizi, sürüm).
- Tüm `ai/` kodu saf Python'dur; hiçbir dış makine öğrenmesi bağımlılığı yoktur.
- Kanıt ürünleri: `docs/reports/asama5/` → `arazi_model.json` (eğitilmiş model), `METRIKLER.json`, `ai-gorev.jsonl` (görev kaydı).
- Tekrar üretim: `python demos/asama5_ai_demo.py`; testler: `python -m pytest tests -q`.
