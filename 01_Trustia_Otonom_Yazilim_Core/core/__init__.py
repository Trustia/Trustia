"""
TRUSTIA Otonomi Platformu — Altyapı (Sistem 6) Paketi.
Milli Seviye-4 Robotaksi & Taktik Savunma Seyrüsefer Motoru.

Kurucu & Baş Sistem Mimarı: Murat Furkan Bayram (17 Yaşında, %80 Hisse)
Kurucu Ortak: Doğukan Bayram (%20 Hisse)
Merkez: İTO BTM Fulya Derin Teknoloji Kampüsü, Şişli / İstanbul
Tesciller: AB PIC #861711529 • EIT Partner #CUS15554 • BAYKAR • ASELSAN • TÜBİTAK ARBİS

Bu paket, otonomi yazılımının tüm üst katmanlarının üzerine kurulduğu
temel hizmetleri sağlar:

  - messaging : Yayın/abone (pub-sub) mesajlaşma katmanı
  - logging   : Seviyeli, döngülü, zaman damgalı log motoru
  - config    : Dosya + çevre değişkeni + komut satırı öncelik zincirli ayar sistemi
  - timing    : Senkron zaman ve döngü hızı yönetimi (100 Hz kontrol döngüsü)
  - transforms: WGS84, UTM ve ENU koordinat dönüşümleri
  - errors    : Seviyeli hata sınıfı hiyerarşisi (ISO 26262 ASIL-D uyumlu)
  - api       : Yönetim ve telemetri arayüzü (C-V2X / REST / MQTT)
"""

__version__ = "2.4.0"
__author__ = "Murat Furkan Bayram (Trustia AI)"
__copyright__ = "Copyright 2026, Trustia AI Technologies"

