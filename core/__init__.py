"""
TRUSTIA Otonomi Platformu — Altyapı (Sistem 6) Paketi.

Bu paket, otonomi yazılımının tüm üst katmanlarının üzerine kurulduğu
temel hizmetleri sağlar:

  - messaging : Yayın/abone (pub-sub) mesajlaşma katmanı
  - logging   : Seviyeli, döngülü, zaman damgalı log motoru
  - config    : Dosya + çevre değişkeni + komut satırı öncelik zincirli ayar sistemi
  - timing    : Senkron zaman ve döngü hızı yönetimi
  - transforms: WGS84, UTM ve ENU koordinat dönüşümleri
  - errors    : Seviyeli hata sınıfı hiyerarşisi
  - api       : Yönetim arayüzü (REST)

Her modül bağımsız test edilebilir ve plan dokümanında (docs/PLAN.md)
tanımlanan Sistem 6 sorumluluklarını birebir karşılar.
"""

__version__ = "0.1.0"
