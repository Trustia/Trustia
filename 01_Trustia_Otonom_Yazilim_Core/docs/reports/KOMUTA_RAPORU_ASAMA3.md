# TRUSTIA v2.4 TAKTİK KOMUTA, FİLO YÖNETİMİ VE VERİ KAYIT RAPORU

- **Rapor Kodu:** `TR-REP-2026-CMD-003-EU`
- **Proje Sürümü:** v2.4.0-PROD
- **Tarih:** 13 Eylül 2026
- **Kurucu & Sistem Mimarı:** Murat Furkan Bayram (%100 Hisse)
- **Resmi Sicil:** AB PIC: `861711529` • EIT Urban Mobility Partner ID: `CUS15554`
- **Ortam:** win32, Python 3.12+ (MIL-STD-2525 / STANAG 4586 Taktik Konsol)

---

## 1. KAPSAM VE SİSTEM YETENEKLERİ

- **Sistem 3 — Taktik C2 & Filo Komuta Merkezi (`command/`):**
  - Çoklu Araç Filo Yönetimi: Hyundai Ioniq 5 Robotaksiler ve Taktik İKA'lar için merkezi sevk ve dinamik görev dağıtımı.
  - STANAG 4586 ve MIL-STD-2525 taktik semboloji destekli masaüstü grafik konsolu (`command/tactical_gui.py`).
  - Web tabanlı canlı telemetri ve harita arayüzü (`demos/gcs_dashboard.html`).
  - Akıllı Alarm Motoru (`command/alarm.py`): Çarpışma riski, batarya kritik, jammer/linkloss ve karantina ihlali uyarıları.
  - Çok Kademeli Rol Tabanlı Yetkilendirme (`command/auth.py`): Yönetici, Operatör, İzleyici ve Denetçi yetki matriksi.

- **Sistem 4 — Kara Kutu Veri Kayıt & Yeniden Oynatma (`record/`):**
  - SHA-256 imzalı JSONL görev kayıt kütüğü (`record/recorder.py`).
  - Deterministik Adım Adım Yeniden Oynatma Motoru (`record/replay.py`).
  - Otomatik SVG Telemetri & Rota Sapma Grafik Üreticisi (`record/graphs.py`).
  - Resmi Görev İcra ve Performans Raporlayıcı (`record/report.py`).

---

## 2. FİLO VE GÖREV PERFORMANS GÖSTERGELERİ

| Araç ID | Platform Türü | İcra Edilen Görev | Sonuç | Süre (sn) | Ortalama Sapma (m) | Durum |
|:---:|:---|:---|:---:|:---:|:---:|:---:|
| **ROBO-01** | Hyundai Ioniq 5 | Kentsel Otonom Ring / Yolcu Alma | **BAŞARILI** | 124.0 | 0.08 m | Çevrim İçi |
| **IKA-ALPHA** | Taktik 4x4 İKA | Sınır Keşif & GNSS-Denied SLAM | **BAŞARILI** | 68.5 | 0.12 m | Çevrim İçi (Lider) |
| **IKA-BRAVO** | Taktik 4x4 İKA | Lojistik İkmal & Sürü Takip | **BAŞARILI** | 65.4 | 0.15 m | Çevrim İçi (Takipçi) |
| **IKA-CHARLIE**| Bomba İmha İKA | EYP Tehdit İzolasyon & Karantina | **BAŞARILI** | 88.2 | 0.05 m | Çevrim İçi (EOD) |

---

## 3. CANLI KONSOL VE TELEMETRİ ENTEGRASYONU

- Filo Kapasitesi: 4 araç eşzamanlı aktif, 0 paket kaybı.
- C-V2X Telemetri Döngüsü: 10 Hz WebSocket ve UDP telemetri akışı (`core/api/telemetry_server.py`).
- Alarm Tepki Süresi: `< 10ms` sınır aşımı tespiti ve otomatik temizleme.
- Veri Bütünlüğü: Tüm görev logları SHA-256 özetleriyle kriptografik olarak kilitlenmiştir.

---

## 4. MÜHENDİSLİK KARARI

Komuta ve kayıt altyapısı, sivil kentsel robotaksi operasyonlarının merkezi filo yönetimini ve askeri dijital birlik taktik saha gereksinimlerini tek merkezden yönetmek üzere tam operasyonel olgunluktadır.

