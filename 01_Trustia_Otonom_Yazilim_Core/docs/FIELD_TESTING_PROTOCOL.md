# 🚜 TRUSTIA v2.4 — SEVİYE-4 TİCARİ VE ROBOTAKSİ SAHA TEST PROTOKOLÜ
## (Field Testing & Proving Ground Validation Protocol)

**Doküman Kodu:** `TR-DOC-2026-VAL-04`  
**Sürüm:** v2.4.0-PROD  
**Yürürlük Tarihi:** 13 Eylül 2026 (Revize: 30 Eylül 2026)  
**Sistem Mimarı & Yetkili:** Murat Furkan Bayram (%100 Kurucu & Sistem Mimarı)  
**Resmi Sicil & Akreditasyon:** AB Katılımcı Kodu (PIC): `861711529` | EIT Urban Mobility Partner ID: `CUS15554`  
**Test Sahaları:** Bilişim Vadisi Otonom Test Pisti (Gebze) & Proving Ground Parkurları  

---

## 1. GİRİŞ VE TEST KAPSAMI

Bu protokol, Trustia Seviye-4 otonomi yazılım çekirdeğinin **Hyundai Ioniq 5 E-GMP Otonom Robotaksi**, elektrikli servis minibüsleri ve endüstriyel lojistik taşıtları üzerinde icra edeceği fiziksel kapalı pist ve yarı açık saha testlerinin güvenlik, kalibrasyon ve doğrulama süreçlerini düzenler.

Yazılım, **1.307 / 1.307 otomatik testten (%100 Başarı)** geçmiş olup; fiziksel pist aşamasında ISO 26262 ASIL-D fonksiyonel güvenlik ve SAE J3016 Seviye-4 otonom emniyet normlarını eksiksiz karşılamakla yükümlüdür.

---

## 2. PİST ÖNCESİ SİSTEM VE SENSÖR SAĞLIK KONTROLÜ (PRE-RUN CHECK)

Test günü pist sahasına çıkmadan önce aşağıdaki kontroller adım adım tamamlanarak Teleoperasyon / Filo Masasına kaydedilmelidir:

| Sıra | Bileşen / Alt Sistem | Kontrol Kriteri | Beklenen Değer / Durum |
|:---:|:---|:---|:---|
| **1** | **Donanımsal E-Stop (Acil Durdurma)** | Fiziksel çift kanallı E-Stop butonu ve teleoperasyon acil durdurma devresi | Kontak açıldığında 5ms içinde çekici röle kesimi ve fren basıncı aktivasyonu |
| **2** | **NVIDIA Jetson AGX Orin (64GB)** | Güç, termal ve CUDA/TensorRT çekirdek durumu | Sıcaklık < 55°C, 275 TOPS INT8 hazır, NVDLA 1 & 2 senkron |
| **3** | **Kvaser U100 CAN-FD Arayüzü** | 500 kbps / 2 Mbps CAN-FD veri yolu bütünlüğü | Bus-off hatası 0, hata sayacı (TEC/REC) < 10, 100Hz LKAS döngüsü aktif |
| **4** | **Ouster OS2-128 3D LiDAR** | 128 ışın demeti ve PTP IEEE 1588 zaman senkronizasyonu | 100 Mbps Ethernet akışı, 2.62M nokta/sn, 0 paket kaybı |
| **5** | **Livox Mid-360 LiDAR (2x)** | Ön/yan kör nokta kapsama açısı ve yansıma verisi | Non-repetitive tarama deseni aktif, 360° x 59° FOV teyitli |
| **6** | **Continental ARS408-21 Radar (2x)** | 77 GHz milimetre dalga Doppler ve mesafe tespiti | CAN-FD 0x200..0x203 mesajları akıyor, yağmur/sis paraziti filtrelenmiş |
| **7** | **Septentrio AsteRx-m3 RTK GNSS/INS** | Santimetre hassasiyetli RTK düzeltmesi ve IMU jiroskopu | RTK Fix (Konum sapması < 2 cm), IMU drift < 0.05°/saat |
| **8** | **Moxa VPort / C-V2X RSU Modülü** | 5.9 GHz DSRC / C-V2X V2I haberleşme testi | Gecikme < 12ms, sinyal gücü > -75 dBm, paket iletim oranı %99.8 |

---

## 3. AŞAMALI SAHA SÜRÜŞ VE GÜVENLİK TEST ADIMLARI

### Adım 1: Düşük Hız Manuel & Teleoperasyon Kalibrasyonu (5 - 10 km/h)
* **Amaç:** Drive-by-Wire aktüatör gecikmesinin ve direksiyon açısı geribildiriminin doğrulanması.
* **Prosedür:** Kvaser CAN-FD üzerinden direksiyon açısı komutları 5° adımlarla verilir. Tekerlek kodlayıcıları (wheel encoder) ve INS jirosundan okunan dönüş açısı çakıştırılır. Hata eşiği: `< 0.3°`.

### Adım 2: Engel Önünde Deterministik Acil Durma (Dynamic E-Stop & AEB)
* **Amaç:** 30 km/h ve 50 km/h süratte aniden beliren engellere karşı Pure Pursuit ve Hibrit A* acil kaçış / frenleme testi.
* **Prosedür:** Araç güzergahına 25 metre mesafede fırlatılabilir manken/mukavva hedef bırakılır. 
* **Başarı Kriteri:** Füzyon algoritması hedefi 15ms içinde tespit eder, CAN-FD `0x1A1` (SCC fren) mesajı 0.8g ivmeyle aracı hedefe 2.0 metre kala güvenle durdurur.

### Adım 3: GPS-Denied (GNSS Kesintisi) Tünel ve Otopark Parkur Testi
* **Amaç:** Uydu sinyalinin kesildiği kapalı otopark ve tünel koşullarında 3D NDT LiDAR SLAM kararlılığı.
* **Prosedür:** Kapalı otopark / tünel etabında GNSS anteni izole edilir.
* **Başarı Kriteri:** 1.000 metre kesintisiz sürüş boyunca SLAM konum drifti kümülatif olarak `< %0.15` (1.5 metre altı) olmalıdır.

### Adım 4: LinkLoss (Haberleşme Kaybı) Güvenli Durma (MRM) Testi
* **Amaç:** Filo teleoperasyon konsolu ile araç arasındaki haberleşmenin 500ms üzerinde kesilmesi durumunda Seviye-4 otonom emniyet devresi.
* **Prosedür:** RF / hücresel veri hattı kesilir.
* **Başarı Kriteri:** Sistem `security/linkloss.py` protokolünü devreye sokar; şerit içinde kalarak 5 saniye içinde emniyetli şekilde sağa yanaşır (Minimum Risk Maneuver - MRM) ve 4'lü ikazları yakarak güvenle durur.

### Adım 5: Yapay Zeka Çevresel Engel ve Zemin Tespiti
* **Amaç:** Yol üzerindeki yabancı cisimler (döküntü, lastik parçası, bordür, yol bozukluğu) ve zemin anomalilerinin sınıflandırılması.
* **Prosedür:** Parkur üzerine farklı test cisimleri ve yol engelleri yerleştirilir.
* **Başarı Kriteri:** Algı modelleri engelleri 20 metre mesafeden en az %96 doğrulukla tespit edip güvenli teğet mesafesi hesaplayarak rotayı dinamik olarak yeniden planlar.

---

## 4. ONAY VE TEST SERTİFİKASYONU

Test icra raporları, her test sürüşü sonrasında `record/recorder.py` tarafından SHA-256 zaman damgalı JSONL formatında otomatik üretilir. 

**Mühür ve İmza:**  
**Trustia AI — Otonom Sistemler Mühendislik Heyeti**  
Murat Furkan Bayram — Kurucu & Sistem Mimarı (%100 Mülkiyet)  

