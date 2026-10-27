# 🧠 01_Trustia_Otonom_Yazilim_Core — Seviye-4 Deterministik Otonom Sürüş Çekirdeği (v4.3 Enterprise)

> **114 Çekirdek Kaynak Dosyası (19.414 Satır) + 48 Otomatik Test Dosyası (5.926 Satır / 1.307 Test) = 162 Dosya / 25.340 Satır C++20, ROS 2 Humble ve Python 3.12 Otonomi Çekirdeği**

Bu dizin, **Trustia AI Technologies** tarafından sıfırdan geliştirilen; ticari robotaksiler (**Hyundai Ioniq 5 E-GMP** & **SAIC Maxus MIFA 7**), endüstriyel otonom yük araçları (AMR/AGV) ve savunma sanayii insansız kara araçları (İKA) için ortak temel oluşturan **Seviye-4 Deterministik Otonom Sürüş Yazılım Çekirdeğini (`AutonomyCore`)** barındırır.

---

## 📁 1. Alt Sistemler ve Dizin Mimarisi (162 Dosya)

```text
01_Trustia_Otonom_Yazilim_Core/
├── ai/                  ← 3D LiDAR RANSAC Zemin Ayrıştırma, DBSCAN Engel Kümeleme, OBB & Yörünge Tahmini
├── slam/                ← GNSS-Denied 3D NDT Pose-Graph SLAM & 400 Hz Error-State Kalman Filtresi (ESKF)
├── planning/            ← Kinematik Hibrit A*, Frenet 5. Derece Quintic Polinom & Otonom Durum Makinesi (FSM)
├── control/             ← Pure Pursuit, Stanley Yanal İzleme, Boyuna PID & CAN-FD DBC Sinyal Kodlayıcı
├── integration/         ← 100 Hz Linux SocketCAN CAN-FD Sürücüsü & ROS 2 Humble Drive-by-Wire Köprüsü
├── security/            ← ISO 26262 ASIL-D 50ms Watchdog, 1.5 m/s² MRM Güvenli Duruş & SecOC Kriptografi
├── command/             ← Çoklu Araç Telemetri Yönlendiricisi, Filo Çağrı & Dinamik Rota Tahsis Motoru
├── core/                ← AutonomyCore Üst Düzey API, Sistem Orkestratörü & HMAC-SHA256 Donanım Kilidi
├── config/              ← Evrensel Araç Konfigürasyonu (vehicle_config.yaml — Kod Değişmezliği İlkesi)
├── tools/               ← build_enterprise_sdk.py (Kapalı Kutu .pyc B2B Enterprise SDK Derleyicisi)
├── tests/               ← 48 Test Dosyası / 1.307 Adet Otomatik Birim, Entegrasyon, Kaos ve SIL/HIL Testi
└── trustia_cli.py       ← Komut Satırı Yönetim, Test, Simülasyon ve ASIL-D Denetim Aracı
```

---

## 🧪 2. 1.307 Testlik Doğrulama Kütüphanesinin Yürütülmesi (%100 Yeşil)

Yapılan her kod değişikliğinden sonra tüm test süiti tek komutla koşturulur ve **0 hata / 0 başarısızlık** kuralıyla doğrulanır:

```bash
# Tüm 1.307 testi koşturun
pytest tests/ -q

# Beklenen Çıktı:
# 1307 passed in 39.06s (100% PASS, 0 FAILURE, 0 ERROR)
```

### CLI Komutları:
```bash
python trustia_cli.py test       # 1.307 doğrulama testini çalıştırır
python trustia_cli.py robotaxi   # 100 Hz CAN-FD otonom sürüş döngüsünü simüle eder
python trustia_cli.py audit      # ISO 26262 ASIL-D fonksiyonel emniyet denetimini yapar
python trustia_cli.py info       # Kurumsal tescil ve envanter künyesini görüntüler
```

---

## 🔒 3. Fonksiyonel Emniyet (ISO 26262 ASIL-D) & Mimari İlkeler

* **Evrensel Otonomi (Kod Değişmezliği):** Çekirdekteki matematiksel modeller (Hybrid A*, Pure Pursuit, Stanley, 3D NDT SLAM) araca göre değiştirilmez; dingil mesafesi, hız limitleri ve CAN ID'leri yalnızca `config/vehicle_config.yaml` üzerinden yönetilir.
* **50 ms Watchdog & Minimal Risk Maneuver (MRM):** Kontrol döngüsünde 50 ms'yi aşan gecikmelerde sistem panik freni yapmaz; $1.5\text{ m/s}^2$ kontrollü yavaşlamayla aracı sağ emniyet şeridine çekerek durdurur.
* **5 ms Donanımsal Sürücü Devralma:** Güvenlik sürücüsü direksiyona veya fren pedalına dokunduğu anda ($\le 5\text{ ms}$) otonomi devreden çıkarak kontrolü insana devreder.
* **B2B Kapalı Kutu Dağıtım:** `tools/build_enterprise_sdk.py` aracı ile kaynak kodlar `.pyc` bytecode formatına derlenir ve HMAC-SHA256 donanım kilidi (CPU/MAC UUID) ile şifrelenir.

---
*© 2026 Trustia AI Technologies — Kurucu & Sistem Mimarı: Murat Furkan Bayram (%100 Fikri Mülkiyet).*
