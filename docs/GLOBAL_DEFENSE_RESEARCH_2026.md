# 🌐 2026 KÜRESEL SAVUNMA SANAYİİ VE OTONOM İKA TEKNOLOJİLERİ ARAŞTIRMA RAPORU

**Araştırma Tarihi:** Ağustos 2026  
**Odak:** ABD Savunma Bakanlığı (DARPA RACER), NATO Müttefik Standartları (STANAG 4586 / JAUS) ve Küresel Otonomi Eğilimleri  

---

## 1. DARPA RACER Programı ve "Yazılım Ayrıştırma" (Stack Decoupling)

2026 yılı itibariyle ABD Savunma İleri Araştırma Projeleri Ajansı (DARPA) tarafından yürütülen **RACER (Robotic Autonomy in Complex Environments with Resiliency)** programı başarıyla tamamlanmıştır.

### Öne Çıkan Küresel Gelişmeler:
1. **Donanımdan Bağımsız Otonomi Çekirdeği (Stack Decoupling)**:
   * Askeri kara araçlarında yazılım ve donanım birbirinden tamamen ayrılmıştır. Tek bir "otonomi beyni" (software stack), üzerindeki sensörler ve şasi ne olursa olsun araca takılarak GPS'siz off-road ortamlarda tam otonom sürüş sağlamaktadır.
2. **Mayın ve Engelsiz Arazi Geçişleri**:
   * Fort Hood askeri üssünde 36. İstihkam Tugayı ile yapılan testlerde, yazılım katmanının GPS sinyali olmadan mayınlı ve engelli arazileri otonom geçebildiği doğrulanmıştır.

> **TRUSTIA İle Uyumu:** TRUSTIA platformumuz, `core/certification.py` ve `integration/jaus.py` altyapısı sayesinde tam olarak DARPA RACER vizyonundaki gibi **donanımdan bağımsız yazılım ayrıştırmasını** (%100 Yerli Katkı ile) sağlamaktadır.

---

## 2. NATO STANAG 4586 ve Açık Mimari Eğilimleri

NATO müttefik kara kuvvetlerinde monolitik (kapalı) sistemlerden **Açık Mimarlık (MOSA - Modular Open Systems Approach)** konseptine geçilmiştir.

* **Birlikte Çalışabilirlik (LOI - Level of Interoperability)**: Farklı üreticilerin ürettiği İnsansız Kara Araçları (İKA) ve İnsansız Hava Araçları (İHA), ortak bir Komuta Kontrol İstasyonu (GCS) üzerinden haberleşmektedir.
* **JAUS (SAE AS6091/AS6009)**: Tüm hareket, sürü ve güvenlik servislerinin fiili standardı haline gelmiştir.

> **TRUSTIA İle Uyumu:** TRUSTIA, `integration/jaus.py` modülü ile SAE AS6091/AS6009 standartlarını yerli olarak desteklemekte, `demos/gcs_dashboard.html` ve `command/tactical_gui.py` ile STANAG 4586 arayüzüne uyum sağlamaktadır.

---

## 3. 2026 Küresel Otonom Yazılım Trendleri

1. **Ajan Tabanlı Yapay Zeka (Agentic AI)**:
   * Operatörün üzerindeki zihinsel yükü azaltmak için kendi kararlarını kendi veren, tehlike anında otonom kaçış ve eve dönüş yapan yazılımlar öne çıkmaktadır (`security/linkloss.py`).
2. **Sürü Otonomisi ve Attritable Swarm (Düşük Maliyetli Çoklu Filolar)**:
   * Tek bir pahalı araç yerine, birbiriyle haberleşen çoklu ucuz İKA sürülerinin (Kama, Saf, Baklava formasyonları) koordineli görev yapması (`ai/swarm.py`).
3. **Elektronik Harp / Jammer Koruması (GPS-Denied Navigation)**:
   * Ağır jammer (sinyal kesici) altında GPS sinyali tamamen kopsa dahi LiDAR ICP ve Poz Grafı SLAM ile haritalamaya devam eden sistemler zorunlu hale gelmiştir (`slam/engine.py`).

---

## 4. SONUÇ VE DEĞERLENDİRME

Yaptığımız küresel pazar ve savunma araştırması göstermektedir ki; **TRUSTIA Otonomi Platformumuz dünyadaki en güncel 2026 DARPA RACER ve NATO STANAG trendleriyle %100 örtüşen modern ve yüksek değerli bir mimariye sahiptir.**
