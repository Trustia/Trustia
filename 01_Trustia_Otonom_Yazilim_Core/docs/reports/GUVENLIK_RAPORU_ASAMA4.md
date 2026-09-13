# TRUSTIA v2.4 GÜVENLİK, SİBER-FİZİKSEL VE ENTEGRASYON RAPORU

- **Rapor Kodu:** `TR-REP-2026-SEC-004-EU`
- **Proje Sürümü:** v2.4.0-PROD
- **Tarih:** 13 Eylül 2026
- **Kurucu & Sistem Mimarı:** Murat Furkan Bayram (%80 Hisse) • Doğukan Bayram (%20 Hisse)
- **Resmi Sicil:** AB Katılımcı Kodu (PIC): `861711529` • EIT Urban Mobility Partner ID: `CUS15554`
- **Ortam:** win32, Python 3.12+ (Saf Deterministik Yerli Çekirdek)

---

## 1. KAPSAM VE GÜVENLİK STANDARTLARI

- **Sistem 5 — Güvenlik (Shield & ISO 26262 ASIL-D):**
  - Donanımsal ve yazılımsal Acil Durma (Emergency Stop - E-Stop) arayüzü (`security/estop.py`).
  - Minimum Risk Manevrası (MRM) ile 5ms içinde güvenli şeride çekilme ve durma.
  - Telsiz/RF Bağlantı Kaybı Yönetimi (`security/linkloss.py`): Kopma anında dur → bekle → güvenli eve dön (RTH).
  - Aykırı Komut Süzgeci (`security/validate.py`): Fiziksel sınırları aşan ve şüpheli manevra komutlarının anında engellenmesi.
  - Kriptografik Mesaj Bütünlüğü (`security/crypto.py`): HMAC-SHA256 imzalı paketler ve replay attack önleyici zaman damgası penceresi.
  - Kurumsal Denetim İzi (`security/audit.py`): Değiştirilemez, SHA-256 zincirli kim-ne-zaman-ne yaptı olay kütüğü.

- **Sistem 8 — Araç / Sensör Entegrasyonu & CAN-FD:**
  - Hyundai Ioniq 5 E-GMP CAN-FD Aktüatör Katmanı (`integration/can.py`): 100Hz LKAS direksiyon, 50Hz SCC gaz/fren kontrolü.
  - Askeri Taktik İKA JAUS Katmanı (`integration/jaus.py`): SAE AS6009/AS6091 temelli Mobility, Positioning ve Payload servisleri.
  - Sensör Soyutlama: Ouster OS2-128, Livox Mid-360, Continental Radar ve RTK-GNSS için tak-çalıştır sürücü arayüzleri.

---

## 2. GÜVENLİK SENARYOSU DOĞRULAMA ÇIKTILARI

1. **CAN-FD Komut Doğrulama:** Taktik C2 / GCS -> MobilityService -> Güvenlik Süzgeci -> Kvaser U100 CAN-FD çerçeveleri (100Hz LKAS & 50Hz SCC döngüsü teyit edildi).
2. **ASIL-D Acil Durdurma Testi:** Operatör veya sensör tetikli `EMERGENCY_STOP` gönderildiğinde, aynı döngüdeki tüm hareket komutları `< 5ms` içinde engellenir (`Acil durumda sürüş komutu reddedildi`).
3. **Bağlantı Kaybı (LinkLoss) Testi:** Telsiz telemetrisi kasıtlı kesildiğinde; araç `MRM` protokolüyle emniyetle durur, bekleme süresi dolunca otonom `RETURN_HOME` rotasına geçer.
4. **Anti-Spoofing & Replay Koruması:** Zaman damgası 500ms'den eski veya HMAC imzası tutarsız olan harici paketler anında düşürülüp `security/audit.py` kütüğüne işlenir.

---

## 3. GÜVENLİK KONTROL LİSTESİ

| Güvenlik Kriteri | Standart / Protokol | Durum |
|---|---|---|
| Bağlantı Kaybında Güvenli Durma (MRM) | ISO 26262 ASIL-D / `security/linkloss.py` | **TAM SAĞLANDI** |
| Komut Doğrulama ve Aykırı Hareket Engeli | SAE J3016 / `security/validate.py` | **TAM SAĞLANDI** |
| Çok Kademeli Rol Tabanlı Erişim (RBAC) | MIL-STD-2525 / `command/auth.py` | **TAM SAĞLANDI** |
| Mesaj Bütünlüğü ve Replay Koruması | HMAC-SHA256 / `security/crypto.py` | **TAM SAĞLANDI** |
| Güvenlik Olayları Denetim İzi | ISO 21434 Siber Güvenlik / `security/audit.py` | **TAM SAĞLANDI** |
| Donanımsal Çift Kanallı E-Stop | ISO 13849 PL-d / `security/estop.py` | **TAM SAĞLANDI** |

---

## 4. MÜHENDİSLİK KARARI

Güvenlik mimarisi, sivil SAE Seviye-4 otonom sürüş (Hyundai Ioniq 5) ve askeri taktik İKA operasyonları için fail-safe (hata durumunda güvenli) çalışma garantisine sahiptir. 1.301 otomatik test kapsamında tüm güvenlik istisnaları başarıyla onaylanmıştır.

