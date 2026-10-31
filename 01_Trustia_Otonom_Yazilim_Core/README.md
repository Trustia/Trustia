# 🧠 01_Trustia_Otonom_Yazilim_Core — Seviye-4 Deterministik Otonom Sürüş Çekirdeği (v4.4 Enterprise)

> **119 Çekirdek Kaynak Dosyası (25.000+ Satır) + 52 Otomatik Test Dosyası (6.800+ Satır / 1.329 Test) = 171 Dosya / 31.800+ Satır C++20, ROS 2 Humble ve Python 3.12 Otonomi Çekirdeği**

Bu dizin, **Trustia AI Technologies** tarafından sıfırdan geliştirilen; ticari robotaksiler (**Hyundai Ioniq 5 E-GMP** & **SAIC Maxus MIFA 7**), endüstriyel otonom yük araçları (AMR/AGV) ve savunma sanayii insansız kara araçları (İKA) için ortak temel oluşturan **Seviye-4 Deterministik Otonom Sürüş Yazılım Çekirdeğini (`AutonomyCore`)** barındırır.

---

## 📁 1. Alt Sistemler ve Dizin Mimarisi (171 Dosya)

```text
01_Trustia_Otonom_Yazilim_Core/
├── ai/                  ← CenterPoint BEV ONNX/TensorRT 3D Derin Algı, 7-DOF EKF Çoklu Nesne Takibi, 3s Yörünge & Niyet Kestirimi
├── data/                ← Ham .bin ve .pcd LiDAR Sürüş Veri Kütüphanesi (KITTI/nuScenes Standart Formatı)
├── models/              ← trustia_centerpoint_backbone.onnx Derin Öğrenme Çıkarım Modeli (Opset 17)
├── slam/                ← GNSS-Denied 3D NDT Pose-Graph SLAM & 400 Hz Error-State Kalman Filtresi (ESKF)
├── planning/            ← Kinematik Hibrit A*, Dinamik Engel Kaçınma, Frenet 5. Derece Quintic Polinom & FSM
├── control/             ← Pure Pursuit, Stanley Yanal İzleme, Boyuna PID & CAN-FD DBC Sinyal Kodlayıcı
├── security/            ← ISO 26262 ASIL-D 50ms Watchdog, 1.5 m/s² MRM & ISO 21448 SOTIF Plausibility Monitörü
├── integration/         ← 100 Hz Linux SocketCAN CAN-FD Sürücüsü & ROS 2 Humble Drive-by-Wire Köprüsü
├── command/             ← Çoklu Araç Telemetri Yönlendiricisi, Filo Çağrı & Dinamik Rota Tahsis Motoru
├── core/                ← AutonomyCore Üst Düzey API, process_perception() Tekil Döngü & HMAC Donanım Kilidi
├── config/              ← Evrensel Araç Konfigürasyonu (vehicle_config.yaml — Kod Değişmezliği İlkesi)
├── tools/               ← export_centerpoint_onnx.py, generate_sample_lidar.py & build_enterprise_sdk.py
├── tests/               ← 52 Test Dosyası / 1.329 Adet Otomatik Birim, Entegrasyon, Kaos ve SIL/HIL Testi
└── trustia_cli.py       ← Komut Satırı Yönetim, Test, Simülasyon, 3D Algı ve ASIL-D Denetim Aracı
```

---

## 🧪 2. 1.329 Testlik Doğrulama Kütüphanesinin Yürütülmesi (%100 Yeşil)

Yapılan her kod değişikliğinden sonra tüm test süiti tek komutla koşturulur ve **0 hata / 0 başarısızlık** kuralıyla doğrulanır:

```bash
# Tüm 1.329 çekirdek testini koşturun
pytest tests/ -q

# Beklenen Çıktı:
# 1329 passed in 32.26s (100% PASS, 0 FAILURE, 0 ERROR)
```

### CLI Komutları:
```bash
python trustia_cli.py test          # 1.329 doğrulama testini çalıştırır
python trustia_cli.py perception    # ONNX CenterPoint 3D algı, 7-DOF EKF takip, 3s tahmin ve SOTIF konsolunu başlatır
python trustia_cli.py robotaxi      # 100 Hz CAN-FD otonom sürüş döngüsünü simüle eder
python trustia_cli.py audit         # ISO 26262 ASIL-D fonksiyonel emniyet denetimini yapar
python trustia_cli.py info          # Kurumsal tescil ve envanter künyesini görüntüler
```

---

## 🔒 3. Fonksiyonel Emniyet (ISO 26262 ASIL-D & ISO 21448 SOTIF) & Mimari İlkeler

* **Evrensel Otonomi (Kod Değişmezliği):** Çekirdekteki matematiksel modeller (Hybrid A*, Pure Pursuit, Stanley, 3D NDT SLAM) araca göre değiştirilmez; dingil mesafesi, hız limitleri ve CAN ID'leri yalnızca `config/vehicle_config.yaml` üzerinden yönetilir.
* **3D Derin Algı & 7-DOF EKF Takip:** CenterPoint/PointPillars mimarisiyle 22.4 ms sürede nuScenes 7 sınıf tespiti, Döndürülmüş BEV IoU ve 3D NMS. 7-DOF EKF ile nesnelerin gerçek hız vektörleri ($v_x, v_y$) hesaplanır.
* **3 Saniyelik Gelecek Yörünge Kestirimi:** Yaya geçitlerindeki yayaların ve araçların 3 saniye sonra nerede olacağı ($t \in [0.5, 3.0]$ s) modellenir, dinamik kaçınma rotaları buna göre planlanır.
* **ISO 21448 SOTIF Plausibility & Hayalet Engel Kalkanı:** İmkansız kinematik sıçramalar ($a > 12\text{ m/s}^2$) ve kamera halüsinasyonları 3D LiDAR nokta bulutu yoğunluğuyla elenir, hayalet frenleme sıfırlanır.
* **50 ms Watchdog & Minimal Risk Maneuver (MRM):** Kontrol döngüsünde 50 ms'yi aşan gecikmelerde sistem panik freni yapmaz; $1.5\text{ m/s}^2$ kontrollü yavaşlamayla aracı sağ emniyet şeridine çekerek durdurur.
* **5 ms Donanımsal Sürücü Devralma:** Güvenlik sürücüsü direksiyona veya fren pedalına dokunduğu anda ($\le 5\text{ ms}$) otonomi devreden çıkarak kontrolü insana devreder.
* **B2B Kapalı Kutu Dağıtım:** `tools/build_enterprise_sdk.py` aracı ile kaynak kodlar `.pyc` bytecode formatına derlenir ve HMAC-SHA256 donanım kilidi (CPU/MAC UUID) ile şifrelenir.

---
*© 2026 Trustia AI Technologies — Kurucu & Sistem Mimarı: Murat Furkan Bayram (%100 Fikri Mülkiyet).*
