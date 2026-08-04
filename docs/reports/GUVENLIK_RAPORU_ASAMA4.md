# TRUSTIA GÜVENLİK VE ENTEGRASYON RAPORU (AŞAMA 4)

- **Proje sürümü:** 0.4.0
- **Tarih:** 2026-08-03
- **Ortam:** win32, Python 3.12.10

## 1. KAPSAM

- **Sistem 5 — Güvenlik (Shield):** acil durma anahtarı (fiziksel + yazılımsal), bağlantı kaybı yönetimi (dur -> bekle -> geri dön), komut doğrulama (tehlikeli/geçersiz komut engelleme), HMAC-SHA256 mesaj imzalama + zaman penceresi (yeniden oynatma koruması), denetim kaydı (kim-ne-zaman-ne yaptı).
- **Sistem 8 — Araç/Sensör Entegrasyonu:** CAN/CAN FD katmanı (motor/direksiyon komutları), çok marka LiDAR ve kamera sürücü soyutlaması, donanım soyutlama katmanı, JAUS mesaj katmanı (AS6009/AS6091 temelli — Mobility, Positioning, Payload servisleri) ve core.api komut eşlemesi.

## 2. GÖSTERİ

1. **JAUS komut kanalı:** GCS -> MobilityService (SetSpeed) -> araç uç noktası -> core.api komutuna eşleme -> güvenlik süzgeci -> CAN motor/direksiyon çerçeveleri.
2. **Acil durum:** operatör EMERGENCY_STOP gönderir; aynı döngüdeki sürüş komutu güvenlik süzgeci tarafından reddedilir ('acil durumda sürüş komutu engellendi').
3. **Bağlantı kaybı:** telemetri kesilir; araç güvenli durma, bekleme ve ardından ana üsse dönme (RETURN_HOME) davranışını uygular; dönüş komutu bir kez üretilir ve denetime düşer.
4. **Görev koşusu:** komuta merkezi görevi simülasyonda koşturur; kayıt ve rapor üretilir (asama4/G-A01.*).

## 3. KANIT DOSYALARI

- `asama4/denetim.jsonl` — tüm güvenlik olayları.
- `asama4/G-A01.jsonl` — görev kaydı (telemetri + sonuç).
- `asama4/G-A01.md` + SVG grafikler — görev raporu.

## 4. GÜVENLİK KONTROL LİSTESİ

| PLAN 3.6 maddesi | Durum |
|---|---|
| Bağlantı kaybında güvenli durma | uygulandı (LinkLossManager) |
| Komut doğrulama: geçersiz/tehlikeli komut engelleme | uygulandı (CommandGuard) |
| Yetkilendirme: rol tabanlı erişim | uygulandı (Sistem 3 auth) |
| Mesaj bütünlüğü + yeniden oynatma koruması | uygulandı (HMAC-SHA256) |
| Denetim kaydı | uygulandı (AuditLog) |
| Acil durma anahtarı protokolü | uygulandı (EmergencyStop, fiziksel+yazılımsal) |

## 5. YORUM

- JAUS uç noktaları arasındaki mesajlaşma 32 baytlık sabit başlık + JSON gövdeyle birebir kodlanıp çözülür; servis ayrımı (Mobility/Positioning/Payload) başlıkta taşınır.
- Güvenlik zinciri fail-safe'dir: acil durum veya bağlantı kaybında sürüş komutları zincir tarafından engellenir; açık kurtarma olmadan araç hareket edemez.
