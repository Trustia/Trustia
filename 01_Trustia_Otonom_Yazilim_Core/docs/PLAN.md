# TRUSTIA — MİLLİ OTONOMİ PLATFORMU
## Proje Planı ve Teknik Yol Haritası — Sürüm 2.4 (Dual-Use Robotaksi & Askeri Mimari)

---

## BÖLÜM 1: PROJE KİMLİĞİ

### 1.1 Vizyon
Türkiye ve Avrupa'nın elektrikli binek araçları (Hyundai Ioniq 5) ve insansız kara araçları (İKA) için geliştirilen; GPS karartmalı ortamlarda 3D LiDAR SLAM ile çalışan, %100 yerli katkı sertifikasyonuna uyumlu, NATO STANAG / SAE JAUS / ISO 11898 CAN-FD standartlarında Seviye-4 otonomi yazılım platformu.

### 1.2 Misyon
Taksi filolarına, belediyelere ve araç üreticilerine (BAYKAR, ASELSAN, HAVELSAN, FNSS, Otokar, BMC vb.) donanım-bağımsız otonom "beyin" yazılımı ve 48 saatte tak-çalıştır dönüşüm kiti sağlamak.

---

## BÖLÜM 2: UYUMLULUK VE STANDARTLAR

| Standart / Belge | Organizasyon | Kullanım Alanı | Durum |
|---|---|---|---|
| **Avrupa Komisyonu PIC** | European Commission | AB Katılımcı Kayıt Defteri (PIC: `861711529`) | **TESCİLLİ** |
| **EIT Urban Mobility** | EIT / Horizon Europe | Partner ID: `CUS15554` (100k€ Hibe: `3.1.02-1206-3732.3`) | **ONAYLI PARTNER** |
| **BAYKAR Tedarikçi** | Baykar Tech | Seviye-4 Otonomi & 3D LiDAR SLAM | **BAŞVURU ALINDI** |
| **ASELSAN Tedarikçi** | ASELSAN | Kara Platformu Otonomi (No: `0050569CCE941FD1A49FCEFB9B7BE7D6`) | **ÖN DEĞERLENDİRMEDE** |
| **ISO 11898 CAN-FD** | Bosch / ISO | Hyundai Ioniq 5 LKAS_FD & SCC_FD 5 Mbps Sürüş Hattı | **ENTEGRE EDİLDİ (`integration/can.py`)** |
| **ISO 26262 ASIL-D** | ISO | Minimal Risk Maneuver (MRM) Güvenli Durma | **ENTEGRE EDİLDİ (`security/linkloss.py`)** |
| **SAE AS6091 (JAUS)** | SAE International | Komuta-Kontrol Mesaj Seti | **ENTEGRE EDİLDİ (`integration/jaus.py`)** |
| **STANAG 4586** | NATO | Taktik Birlikte Çalışabilirlik Seviyesi 4 | **UYUMLU** |
| **TÜR Belgesi** | TOBB / Sanayi Bak. | %100 Yerli Katkı Doğrulaması (Sıfır Harici Bağımlılık) | **AST İLE DOĞRULANDI (`core/certification.py`)** |

---

## BÖLÜM 3: TAMAMLANMIŞ SİSTEM MİMARİSİ VE TEST DURUMU

* **Birim & Entegrasyon Testleri**: 1.301 test %100 doğrulandı (`python -m pytest`).
* **Otomatik Denetim**: AST taramasıyla harici runtime bağımlılığı taşımadığı (%100 yerli katkı) onaylandı.
* **Taktik Arayüz**: NATO MIL-STD-2525 Standartlarında Masaüstü C2 Konsolu (`command/tactical_gui.py`).
* **Donanım BOM**: 27 parçalık Seviye-4 dönüşüm kiti (Ouster OS2-128 + Jetson Orin 64GB) onaylandı.

**NİHAİ DURUM: TRUSTIA Platformu v2.4 sürümü itibariyle %100 tamamlanmış, tüm testleri geçmiş, AB PIC ve ulusal savunma tescilleriyle üretime ve ticari lansmana hazır hale gelmiştir.**

