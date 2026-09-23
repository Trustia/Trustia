# 🚜 TRUSTIA v2.4 — SEVİYE-4 DUAL-USE SAHA VE DONANIM TEST PROTOKOLÜ
## (Field Testing & Validation Protocol — Proving Ground Operations)

**Doküman Kodu:** `TR-DOC-2026-VAL-04`  
**Sürüm:** v2.4.0-PROD  
**Yürürlük Tarihi:** 13 Eylül 2026  
**Sistem Mimarı & Yetkili:** Murat Furkan Bayram (%80 Kurucu & CEO)  
**Resmi Sicil & Akreditasyon:** AB Katılımcı Kodu (PIC): `861711529` | EIT Urban Mobility Partner ID: `CUS15554`  
**Test Sahaları:** Bilişim Vadisi Otonom Test Pisti (Gebze) & QSTP Otonomi Test Parkuru (Doha / Katar)

---

## 1. GİRİŞ VE TEST KAPSAMI

Bu protokol, Trustia Seviye-4 otonomi yazılım çekirdeğinin hem **Hyundai Ioniq 5 E-GMP Otonom Robotaksi** platformunda hem de **Taktik İnsansız Kara Aracı (İKA / Dual-Use UGV)** üzerinde icra edeceği fiziksel kapalı pist ve yarı açık saha testlerinin güvenlik, kalibrasyon ve doğrulama süreçlerini düzenler.

Yazılım, **1.301 / 1.301 otomatik testten (%100 Başarı)** geçmiş olup; fiziksel pist aşamasında ISO 26262 ASIL-D fonksiyonel güvenlik ve STANAG 4586 / MIL-STD-810H askeri dayanım standartlarını karşılamakla yükümlüdür.

---

## 2. PİST ÖNCESİ SİSTEM VE SENSÖR SAĞLIK KONTROLÜ (PRE-FLIGHT / PRE-RUN CHECK)

Test günü pist sahasına çıkmadan önce aşağıdaki kontroller adım adım tamamlanarak Taktik C2 Masasına kaydedilmelidir:

| Sıra | Bileşen / Alt Sistem | Kontrol Kriteri | Beklenen Değer / Durum |
|:---:|:---|:---|:---|
| **1** | **Donanımsal E-Stop (Acil Durdurma)** | Fiziksel çift kanallı E-Stop butonu ve uzaktan 433/868 MHz telsiz rölesi | Kontak açıldığında 5ms içinde çekici röle kesimi ve fren basıncı aktivasyonu |
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

### Adım 3: GPS-Denied (GNSS Kesintisi) Tünel ve Ormanlık Parkur Testi
* **Amaç:** Uydu sinyalinin kasıtlı olarak kesildiği veya karıştırıldığı (RF Jamming / Spoofing) koşullarda 3D NDT LiDAR SLAM kararlılığı.
* **Prosedür:** Bilişim Vadisi kapalı otopark/tünel etabında GNSS anteni izole edilir.
* **Başarı Kriteri:** 1.000 metre kesintisiz sürüş boyunca SLAM konum drifti kümülatif olarak `< %0.15` (1.5 metre altı) olmalıdır.

### Adım 4: LinkLoss (Komuta Bağlantı Kaybı) Güvenli Durma (MRM) Testi
* **Amaç:** Taktik C2 konsolu ile araç arasındaki şifreli haberleşmenin 500ms üzerinde kesilmesi durumunda Seviye-4 otonom emniyet devresi.
* **Prosedür:** RF link kesici tetiklenir.
* **Başarı Kriteri:** Sistem `security/linkloss.py` protokolünü devreye sokar; şerit içinde kalarak 5 saniye içinde emniyetli şekilde sağa yanaşır (Minimum Risk Maneuver - MRM) ve 4'lü ikazları yakarak durur.

### Adım 5: Yapay Zeka Tehdit & EYP/Mayın Taktik Algılama Testi (Dual-Use)
* **Amaç:** Sivil parkurda yol üzerindeki yabancı cisimler (döküntü, lastik parçası), askeri senaryoda ise gömülü EYP, tuzak teli ve KHKN tehditlerinin sınıflandırılması.
* **Prosedür:** Parkur üzerine 4 farklı test cismi yerleştirilir.
* **Başarı Kriteri:** `ai/bomb_detector.py` ve `ai/cbrn_detector.py` modelleri cisimleri 20 metre mesafeden en az %96 doğrulukla tespit edip 15 metre karantina yarıçapı hesaplayarak yolu dinamik olarak yeniden planlar.

---

## 4. ONAY VE TEST SERTİFİKASYONU

Test icra raporları, her test sürüşü sonrasında `record/recorder.py` tarafından SHA-256 zaman damgalı JSONL ve SVG formatında otomatik üretilir. İlgili kayıtlar Sanayi ve Teknoloji Bakanlığı, Bilişim Vadisi Test Pisti Yönetimi, ASELSAN Tedarikçi İzleme Kurulu ve EIT Urban Mobility denetim masasına sunulmak üzere kurumsal arşivde muhafaza edilir.

**Mühür ve İmza:**  
**Trustia Teknoloji A.Ş. — Otonom Sistemler Mühendislik Heyeti**  
Murat Furkan Bayram — Kurucu & Sistem Mimarı (%100)  
Denizcan Özcan — Donanım ve Entegrasyon Mühendisi  
