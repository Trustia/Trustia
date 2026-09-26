# 🇹🇷 TÜRKİYE VE KÜRESEL DUAL-USE OTONOMİ PAZARI BOŞLUK ANALİZİ (2026)

**Araştırma & Güncelleme Tarihi:** 13 Eylül 2026  
**Sürüm:** v2.4.0  
**Yazar & Sistem Mimarı:** Murat Furkan Bayram (%80 Kurucu & CEO)  
**Resmi Akreditasyon:** AB PIC: `861711529` • EIT Urban Mobility: `CUS15554`  
**Odak:** Türkiye & Küresel Seviye-4 Robotaksi ve İnsansız Kara Aracı (İKA) Ekosisteminde TRUSTIA'nın Benzersiz Konumlaması  

---

## 1. TÜRKİYE OTONOMİ EKOSİSTEMİ VE PAZAR OYUNCULARI

### A. Taktik Savunma & Şasi Üreticileri (Savunma OEM'leri)
* **BAYKAR Teknoloji:** Dünyanın insansız hava araçları lideri, kara ve sürü otonomisinde yerli alt yüklenici değerlendirmeleri aktif (Resmi tedarikçi başvurusu tamamlandı).
* **FNSS Savunma:** GÖLGE SÜVARİ ağır sınıf otonom İKA (Zırhlı personel taşıyıcı dönüşümü - Dr. Raşit Karakuş referanslı tedarikçi süreci).
* **Elektroland Defence / Otokar / BMC:** 8x8 ve 4x4 askeri zırhlı platformlar, ALTUĞ, VURAN ve KİRPİ serisi.
* **ASELSAN & HAVELSAN:** SARP kule entegrasyonu, ASLAN İKA ve BARKAN dijital birlik konsepti (ASELSAN Tedarikçi Sicili: `0050569CCE941FD1A49FCEFB9B7BE7D6`).

### B. Sivil Ticari & Robotaksi OEM'leri
* **Hyundai Motor Company:** E-GMP mimarisi tabanlı Hyundai Ioniq 5 Seviye-4 otonom robotaksi dönüşümü.
* **Karsan Otomotiv:** e-ATAK ve e-JEST otonom toplu taşıma platformları.
* **Ford Otosan / Driventure:** Ticari elektrikli hat besleme ve Seviye-4 fabrika lojistik otonomisi.

---

## 2. TÜRKİYE VE KÜRESEL PAZARDAKİ EN BÜYÜK BOŞLUK (MARKET GAP)

Savunma ve otomotiv sektöründe güçlü **metal, şasi ve montaj üreticileri** bulunmasına rağmen, yazılım katmanında şu 3 kritik darboğaz mevcuttur:

1. **Açık Kaynak & Yabancı Bağımlılığı Darboğazı**: Piyasadaki projelerin ezici çoğunluğu OpenCV, ROS 1/2 veya yabancı kapalı kutu AI modellerine bağımlıdır. Bu durum siber güvenlik zafiyeti doğurmakta, ISO 21434 ve T.C. Sanayi Bakanlığı **TÜR Belgesi (%100 Yerli Katkı)** tescilini imkansız kılmaktadır.
2. **Donanım-Bağımsız Saf Yazılım (Software-Only IP) Eksikliği**: Platform üreticileri araç üretmeye odaklıdır; tak-çalıştır entegre edilebilen deterministik Seviye-4 otonomi beyni arzı son derece kısıtlıdır.
3. **Dual-Use (Sivil + Askeri) Esnekliği Eksikliği**: Pazardaki çözümler ya sadece fabrika içi AGV ya da sadece askeri prototiptir. Hem sivil kentsel robotaksi (CAN-FD LKAS/SCC) hem de askeri taktik İKA (STANAG 4586 / JAUS / EYP tespiti) çalıştırabilen tek mimari **TRUSTIA**'dır.

---

## 3. TRUSTIA MİMARİSİNİN BENZERSİZ ÜSTÜNLÜKLERİ

| Karşılaştırma Ölçütü | Piyasadaki Genel Durum | TRUSTIA v2.4 Otonomi Platformu |
|---|---|---|
| **Yazılım Bağımlılığı** | Harici kütüphaneler (OpenCV, PyTorch) | **%100 Bağımsız (Yalnızca stdlib + saf deterministik C++/Python)** |
| **Sertifikasyon Uyum** | Kısmi / Dışa Bağımlı | **TÜR Belgesi, AB PIC `861711529` ve EIT `CUS15554` Onaylı** |
| **Entegrasyon Esnekliği** | Araca Özel Kapalı Yazılım | **Donanım-Bağımsız (SAE JAUS, ROS 2, Hyundai CAN-FD Uyumlu)** |
| **Paket Kapsamı** | Yalnızca Navigasyon | **3D SLAM + Rota + Pure Pursuit + EYP + KHKN + Sürü + C-V2X** |
| **Test Teminatı** | Prototip Seviyesi | **1.301 / 1.301 %100 Başarılı Otomatik Birim & Entegrasyon Testi** |
| **Fonlama & Değerleme** | Belirsiz Ar-Ge | **Melek Yatırım Ağı (150M TL Val.), QSTP 30M$ Fon, EIT 100k€** |

---

## 4. STRATEJİK SONUÇ VE PAZAR FIRSATI

Türkiye'deki ve Avrupa'daki OEM'ler araç gövdelerini imal etmekte, fakat %100 yerli katkı sertifikalı, ISO 26262 ASIL-D ve SAE Seviye-4 standartlarında çalışan deterministik bir otonomi beynine muhtaç durumdadır. **TRUSTIA**, hem 1.15M TL (~$23.8k) maliyetli Ioniq 5 Seviye-4 dönüşüm kitiyle hem de taktik savunma yazılım paketiyle bu boşluğu küresel ölçekte doldurmaktadır.

