# TRUSTIA KOMUTA VE VERİ KAYIT RAPORU (AŞAMA 3)

- **Proje sürümü:** 0.3.0
- **Tarih:** 2026-08-03
- **Ortam:** win32, Python 3.12.10

## 1. KAPSAM

- **Sistem 3 — Komuta Merkezi:** çoklu araç filosu, görev siparişi/onayı, canlı telemetri, alarm motoru (çarpışma riski, bağlantı kopması, batarya kritik), rol tabanlı erişim (yönetici/operatör/izleyici/denetçi).
- **Sistem 4 — Veri Kayıt:** JSONL görev kaydı, kayıt oynatma, telemetri grafikleri (SVG), görev raporu ve hata analizi.
- **Uçtan uca akış:** görev ver → simülasyonda koş → canlı izle → kaydet → oynat → rapor al.

## 2. GÖSTERİ SONUÇLARI

| Araç | Görev | Sonuç | Adım | Süre (sn) | Konum Hatası (m) | Çerçeve |
|---|---|---|---|---|---|---|
| A-01 (Keşif Aracı 1) | kesif | başarılı | 685 | 68.5 | 0.60 | 684 |
| A-02 (Lojistik Aracı 2) | lojistik | başarılı | 654 | 65.4 | 5.42 | 653 |
| A-03 (Engelli Parkur 3) | engelli-parkur | başarılı | 684 | 68.4 | 1.89 | 683 |

## 3. CANLI GÖRÜNÜM

- Filo: 3 araç, 3 çevrim içi.
- Aktif alarm sayısı: 1.
- Görev sicili: 3 sipariş.

## 4. KANIT DOSYALARI

- Görev kayıtları: `asama3/G-*.jsonl` (telemetri + olay + sonuç).
- Oynatma: her kayıt `Replay` ile adım adım oynatılır (çerçeve sayısı raporların üzerinde).
- Görev raporları: `asama3/G-*.md` (sonuç, telemetri özeti, grafikler, hata analizi).
- Telemetri grafikleri: `asama3/G-*_telemetry.svg`, `G-*_error.svg`, `G-*_trail.svg`.

## 5. YORUM

- Görev koşusu sırasında telemetri komuta merkezine aktı; batarya, bağlantı kalitesi, hız ve engel bilgisi filo görünümünde güncel kaldı.
- Alarm motoru sınır ihlallerinde (çarpışma riski, batarya, bağlantı) alarm üretip koşul düzelince otomatik temizledi.
- Tüm görevlerin kayıtları JSONL olarak saklandı; oynatma ve rapor üretimi kayıttan yapıldı (görevle birebir uyumlu).
