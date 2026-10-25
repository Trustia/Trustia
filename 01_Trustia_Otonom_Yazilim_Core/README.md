# 🚗 01_Trustia_Otonom_Yazilim_Core

> **Seviye-4 Deterministik Otonom Sürüş Yazılım Çekirdeği (16.400+ Satır C++20 / ROS 2 / Python)**

Bu dizin, Trustia Seviye-4 otonom sürüş yazılımının algoritmik çekirdeğini, CAN-FD araç entegrasyon sürücülerini, 3D LiDAR SLAM haritalama motorunu ve 1.307 testlik doğrulama hattını barındırır.

---

## 📁 Alt Modüller ve Fonksiyonel Harita

```text
01_Trustia_Otonom_Yazilim_Core/
├── ai/            ← 3D Zemin Ayrıştırma, Engel Kümeleme & Yönlendirilmiş Sınırlayıcı Kutu (OBB)
├── command/       ← Robotaksi Filo Çağrı, Telemetri Dağıtım ve Rota Tahsisi
├── control/       ← Stanley ve Pure Pursuit Yanal İzleme & DBC Sinyal Kodlayıcı
├── core/          ← AutonomyCore Üst Düzey API, Durum Makineleri & Lisans Doğrulama
├── integration/   ← 100 Hz SocketCAN CAN-FD Aktüatör Sürücüsü & ROS 2 Humble Köprüsü
├── planning/      ← Kinematik Hibrit A* & Quintic Polynomial Yumuşak Yörünge Planlayıcı
├── security/      ← ISO 26262 ASIL-D MRM Safe Stop, 50ms Watchdog & 5ms Acil Devralma
├── slam/          ← GNSS-Denied 3D NDT Pose-Graph SLAM & 400Hz ESKF Kalman Filtresi
├── tests/         ← 1.307 Adet Otomatik Birim, Entegrasyon ve Simülasyon Testi
└── tools/         ← build_enterprise_sdk.py (Kapalı Kutu B2B SDK Dağıtım Aracı)
```

---

## 🧪 1.307 Testin Yürütülmesi

Tüm test kütüphanesi regresyonsuz olarak tek komutla koşturulur:

```bash
# Çekirdek dizininde testleri çalıştırın
pytest tests/ -q

# Beklenen Çıktı:
# 1307 passed in 39.06s (100% PASS, 0 FAILURE, 0 ERROR)
```

---

## 🔒 Güvenlik & Standartlar
- **ISO 26262 ASIL-D:** 50 ms kontrol zaman aşımı (Watchdog), 1.5 m/s² kontrollü emniyetli sağa çekme (MRM).
- **CAN-FD Entegrasyonu:** 100 Hz döngü frekansı, 1.4 ms mesaj gecikmesi, HMAC-SHA256 SecOC mesaj kimlik doğrulaması.
- **Evrensel Araç Uyumu:** Araç boyutları ve aktüatör sınırları `config/vehicle_config.yaml` üzerinden yönetilir. Çekirdek algoritmalar değiştirilmez.

---
*© 2026 Trustia AI Technologies. Tüm hakları saklıdır.*
