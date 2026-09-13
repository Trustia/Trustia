# TRUSTIA AI — TÜRKİYE'NİN İLK SEVİYE-4 OTONOM ROBOTAKSİ & PAYLAŞIMLI MOBİLİTE MASTER PLANI (2026)

> **Belge Türü:** Kurumsal Karar & Kitle Fonlaması Master Strateji Belgesi  
> **Sürüm:** 2.0 — Final  
> **Tarih:** Eylül 2026  
> **Kurucu & CEO:** Murat Furkan Bayram (17 Yaşında, Sistem Mimarı, %80 Hisse)  
> **Kurucu Ortak:** Doğukan Bayram (%20 Hisse, Reşit Temsilci)  
> **Donanım Lideri:** Denizcan Özcan (İÜC EEE 3.44 GPA, ASELSAN Aday Mühendis Havuzu, TEKNOFEST Robotaksi Finalisti)  
> **Resmi Konum:** İTO Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Kampüsü, Şişli / Beşiktaş, İstanbul  
> **Resmi Tesciller:** KOSGEB İleri Girişimci (`KSB01UGE0115153370`) • TÜBİTAK ARBİS (`TBTK-0229-6571`) • BTK Akademi (`L2zPtN4X1ZJ`) • Avrupa Komisyonu PIC: `861711529` • EIT Urban Mobility Partner ID: `CUS15554`  
> **Kurumsal Başvurular (85+ Toplam):** BAYKAR Tedarikçi Ağı, DEİK Dijital Teknolojiler İş Konseyi, QSTP 30M$ Fon, Doha Sprint Kuluçka.  

---

## 1. STRATEJİK VİZYON VE ETİK İLKELER (THE NORTH STAR)

### 1.1. Tek ve Net Odak: Sivil Seviye-4 Otonom Mobilite
Trustia AI; enerjisini askeri ihaleler, tarım arazileri veya bürokratik lisanslar arasında bölmeyi bırakmış; tüm mühendislik gücünü **Türkiye'nin İlk Sivil Seviye-4 Otonom Yolcu Aracını (Hyundai Ioniq 5) yola çıkarmaya** odaklamıştır. Askeri İKA ve tarım algoritmalarımız hazır durumdadır; ancak ana vitrinimiz ve milyar dolarlık pazarımız sivil otonom mobilitedir.

### 1.2. Kimsenin Ekmeğiyle Oynamadan Geleceği İnşa Etmek
16 milyonluk İstanbul'da sadece 19.000 sarı taksi bulunmakta olup kronik bir araç ve konfor krizi yaşanmaktadır. Trustia AI, taksicilerin ekmeğini elinden alan bir düşman değil; Oğuz Alper Öktem'in (Martı TAG) paylaşımlı yolculukta açtığı yolda, taksi esnafı ve filo sahiplerinin gelecekte kendi robotaksilerini işletebilmelerini sağlayacak **milli otonomi yazılım ve donanım altyapısıdır**.

---

## 2. DÜNYANIN EN İYİ PLATFORM ARACI VE SEVİYE-4 DONANIM BOM PAKETİ

### 2.1. Neden Hyundai Ioniq 5 (E-GMP Platformu)?
* **800V Ultra Hızlı Şarj:** %10'dan %80'e sadece **18 dakikada** şarj olarak 24 saat kesintisiz filo operasyonu sağlar.
* **Açık CAN-FD & Steer-by-Wire:** Comma.ai ve bağımsız otonomi araştırmacıları tarafından protokolleri çözülmüş, yazılımla doğrudan direksiyon ve fren kontrolüne izin veren dünyadaki en açık elektrikli mimaridir.
* **Küresel Standart:** Google Waymo ve Motional'ın milyarlarca dolarlık robotaksi filoları için resmi olarak seçtiği şasidir.

### 2.2. 27 Parçalık Seviye-4 Donanım ve Sensör BOM Tablosu

| Bileşen / Parça | Model & Teknik Özellik | Görev & Fonksiyon | Maliyet (TL) |
| :--- | :--- | :--- | :--- |
| **Ana 3D LiDAR** | Ouster OS2-128 (128 Kanal, 200m+) | Tavan 360° uzun menzilli nokta bulutu & 3D NDT SLAM | **530.000 TL** |
| **Kör Nokta LiDAR** | 2x Livox Mid-360 (Katı Hal) | Ön sağ/sol çamurluk kör nokta yaya ve engel algılama | **65.000 TL** |
| **Yapay Zeka Beyin** | NVIDIA Jetson AGX Orin 64GB (275 TOPS) | Gömülü Linux, TensorRT deterministik derin öğrenme | **95.000 TL** |
| **RTK GNSS + IMU** | Septentrio Dual Anten + Endüstriyel IMU | Santimetre hassasiyetinde küresel konum & açısal hız | **85.000 TL** |
| **HDR Kameralar** | 4x GMSL2 Otomotiv Kamerası (Sony Sensör) | Trafik ışığı, şerit çizgileri, tabela ve yaya tespiti | **45.000 TL** |
| **CAN-FD Arayüzü** | Kvaser U100 CAN-FD / Comma Panda | Aracın ADAS ve direksiyon kontrol ünitesine doğrudan erişim | **38.000 TL** |
| **Mekanik & Enerji** | Özel Tavan Barı, PDU Panosu, DC-DC Regülatör | Tavan montaj podu, 12V/24V regüle güç dağıtımı | **122.000 TL** |
| **TOPLAM DONANIM** | **27 Parçalık Eksiksiz Seviye-4 Dönüşüm Kiti** | **Anahtar Teslim Modüler Retrofit Mimarisi** | **980.000 TL** |

---

## 3. KANITLANMIŞ YAZILIM MİMARİSİ VE TEKNOLOJİK OLGUNLUK (TRL-6)

* **16.000 Satır Özgün Deterministik Motor:** Sıfırdan C++17/20 ve Python ile geliştirilen mimarimiz;
* **3D NDT LiDAR SLAM:** GPS sinyali kesilse bile (tünel, Maslak gökdelen kanyonu) 5 cm hassasiyetle lokalizasyon sağlar.
* **Kinematik Hybrid A* & Pure Pursuit:** <15 ms çevrim süresiyle deterministik güvenli rota çizer ve direksiyon açısını yönetir.
* **1.301 / 1.301 Otomatik Test:** %100 başarıyla CI/CD hatlarında doğrulanmıştır.

---

## 4. 16 MİLYONLUK İSTANBUL ROBOTAKSİ OPERASYON PLANI

### 4.1. Mobil Uygulama (Trustia Ride — iOS & Android)
1. **Tarihli & Saatli Rezervasyon (Scheduled):** Uçuş veya toplantı öncesi saat seçilir; araç 5 dakika önce biniş cebine yanaşır.
2. **Anlık Çağırma (On-Demand):** En yakın bekleme noktasındaki araç çağrılır; ücret yolculuk öncesi sabittir.

### 4.2. Kabin Protokolü & 3 Yolcu Kuralı
* **Ön Koltuk:** TAMAMEN BOŞTUR (sürücüsüz).
* **Arka Koltuk:** En fazla 3 yolcu. E-GMP düz tabanı limuzin ferahlığı sunar. Arka tablette klima, Spotify ve canlı 3D LiDAR algı ekranı ile "Acil Durum Kenara Çek" butonu yer alır.

### 4.3. 3 Pilot Koridor (Coğrafi Çitleme - ODD)
1. **Havalimanı Express:** İstanbul Havalimanı (İST) ↔ Kuzey Marmara Otoyolu ↔ Maslak / Levent / BTM Fulya.
2. **Finans & Teknoloji Hattı:** BTM Fulya / Şişli ↔ Büyükdere Caddesi ↔ Levent Plazalar / Vadistanbul.
3. **Banliyö Ringi:** Bahçeşehir / Kayaşehir ↔ Olimpiyat / Mahmutbey Metro Aktarma İstasyonları.

### 4.4. Filo Lojistiği, Şarj & Hijyen Protokolü
* **Staging Hubs:** Vadistanbul, Kanyon otoparkları ve BTM Fulya'da kiralanan ayrılmış akıllı bekleme cepleri (boş gezme yok).
* **18 Dakikada Şarj:** Batarya %20 altına indiğinde araç otomatik olarak Trugo/ZES 350 kW istasyonuna gider ve 18 dakikada dolar.
* **Gece 01:00 - 05:00 Bakımı:** Buharlı antibakteriyel koltuk temizliği, sensör optik bakımı ve telemetri teşhisi. Otonom ticari filo kaskosu ile kara kutu güvencesi.

---

## 5. FİYATLANDIRMA MODELİ VE BİRİM EKONOMİ (SARI TAKSİDEN KAT KAT UCUZ)

### 5.1. Fiyat Kıyaslama Tablosu

| Parametre / Mesafe | UKOME 2026 Sarı Taksi | Trustia AI Seviye-4 Robotaksi | Vatandaşın Kazancı |
| :--- | :--- | :--- | :--- |
| **Açılış Ücreti** | 71,94 TL | **25,00 TL** | **%65 Daha Ucuz** |
| **Kilometre Başı** | 47,92 TL | **18,50 TL** | **%61 Daha Ucuz** |
| **İndi-Bindi (Kısa Mesafe)** | **230,00 TL (Zorunlu)** | **YOK (Sıfır İndi-Bindi Cezası)** | **Tam Adalet** |
| **1.5 km Kısa Yolculuk** | 230,00 TL | **52,75 TL** | **4 KAT DAHA UCUZ!** |
| **10 km Şehir İçi Yolculuk** | ~700,00 TL (Trafikle) | **~250,00 TL (Sabit & Şeffaf)** | **%64 Daha Ucuz!** |
| **Enerji Maliyeti (100 km)** | ~380 TL (Dizel 8.5L) | **~64 TL (Elektrik 16 kWh)** | **6 Kat Düşük Enerji** |

### 5.2. Tek Bir Aracın Günlük & Aylık Nakit Akışı
* **Günlük Sefer:** 16 Sefer (220 km) = **5.040 TL Günlük Ciro** (Aylık ~151.200 TL).
* **Günlük Toplam Gider:** (Şarj + Temizlik + Kasko/Bakım + Otopark) = **590 TL**.
* **Tek Bir Aracın Günlük Net Kârı:** **4.450 TL**
* **Tek Bir Aracın Aylık Net Kârı:** **133.500 TL NET NAKİT AKIŞI!**

---

## 6. FONBULUCU.COM KİTLE FONLAMASI VE KURUŞU KURUŞUNA BÜTÇE

### 6.1. Kampanya Finansal Parametreleri
* **Taban Hedef Fon Tutarı:** **15.000.000 TL** (~400.000 $)
* **Ek Fonlama Tavanı (%20):** **18.000.000 TL** (~475.000 $)
* **Şirket Ön Değerlemesi:** **150.000.000 TL** (~4.000.000 $)
* **Yatırımcılara Arz Edilen Pay:** **%8.5 — %10.0**
* **Kurucularda Kalan Pay:** **%90.0 — %91.5** (Şirket kontrolü kurucularda kalır)
* **Platform:** fonbulucu.com (Kampanya Kodu: W1MV5K - SPK Lisanslı Paya Dayalı Kitle Fonlama)

### 6.2. Kuruşu Kuruşuna Fon Kullanım Raporu (Use of Funds - 15.000.000 TL)

| Harcama Kalemi | Bütçe (TL) | Oran | Detay ve Gerekçe |
| :--- | :--- | :--- | :--- |
| **Hyundai Ioniq 5 Test Aracı** | **2.600.000 TL** | **%17.3** | Düşük kilometreli, 800V E-GMP elektrikli şasi şirketin tapulu demirbaşı olur. |
| **Seviye-4 Sensör Kiti (BOM)** | **1.150.000 TL** | **%7.7** | Ouster 128-LiDAR, 2x Livox Mid-360, Jetson Orin 64GB, Septentrio RTK, 4x Kamera. |
| **Mekanik Montaj & Tavan Podu** | **150.000 TL** | **%1.0** | Alüminyum tavan barı, CNC sensör braketleri, PDU güç panosu ve kablolama. |
| **Çekirdek Mühendislik Ekibi** | **5.200.000 TL** | **%34.7** | **18 Aylık Runway:** Murat (Sistem Mimarı), Denizcan (Donanım) ve test mühendisi maaşları. |
| **Pist Testleri, Saha & Kasko** | **2.100.000 TL** | **%14.0** | Bilişim Vadisi pist kiralama, kapalı alan testleri, ticari otonom kasko ve 18 aylık şarj. |
| **SPK, Şirket Kuruluş & Patent** | **1.800.000 TL** | **%12.0** | A.Ş. kuruluşu, fonbulucu komisyonu, Takasbank/MKK harçları ve TürkPatent tescili. |
| **Acil Durum Rezervi (%10)** | **1.400.000 TL** | **%9.3** | Kur dalgalanması, gümrük vergisi ve yedek sensör stoğu için güvence fonu. |
| **Lansman & 4K Video Filmi** | **600.000 TL** | **%4.0** | Boş koltuklu 4K sinematik video prodüksiyonu, egirişim PR ve BTM Demo Day lansmanı. |
| **TOPLAM HEDEF BÜTÇE** | **15.000.000 TL** | **%100** | **18 Aylık Eksiksiz Anahtar Teslim Robotaksi Operasyonu** |

### 6.3. Bütçe Esnekliği ve Şirket İçi Kullanım Serbestisi (Hukuki Not)
1. **Para Şirketin Emrindedir:** Takasbank blokesi çözüldüğünde para doğrudan Trustia A.Ş.'nin banka hesabına geçer. Tek harcama yetkilisi Yönetim Kurulu'dur (Murat & Doğukan).
2. **Mühendislik Maaşının Kuruculara Akışı:** "Mühendislik Ekibi" bütçesi zaten Murat ve çekirdek kurucuların yasal maaşıdır; her ay şahsi hesaplara yatar.
3. **Kalemler Arası Kaydırma:** Maaş veya operasyondan artan bütçe Yönetim Kurulu Kararı ile doğrudan 2. araç alımına, daha üst LiDAR'lara veya sunucuya kaydırılabilir. Bu SPK ve bağımsız mali denetim nezdinde tamamen yasaldır.

---

## 7. KURUCU YÖNETİM VE MÜHENDİSLİK HEYETİ (EXECUTIVE DOSSIER)

* **MURAT FURKAN BAYRAM (Kurucu & CEO / Baş Sistem Mimarı, %80 Hisse):**
  * 17 Yaşında sistem mimarı. 16.000 satır deterministik C++/Python otonomi motorunun tek mimarı.
  * 3D NDT LiDAR SLAM, Kinematic Hybrid A*, Pure Pursuit, CAN-FD Drive-by-Wire, ROS2 Humble.
  * KOSGEB İleri Girişimci (`KSB01UGE0115153370`), TÜBİTAK ARBİS Milli Araştırmacı, BTK Akademi Savunma Sertifikası (`L2zPtN4X1ZJ`).
  * İTO BTM Fulya Kampüsü Yerleşik Girişimcisi, Startups.watch doğrulanmış kurucusu.
* **DENİZCAN ÖZCAN (Donanım & Robotik Entegrasyon Mühendisi):**
  * İstanbul Üniversitesi-Cerrahpaşa Elektrik-Elektronik Mühendisliği 4. Sınıf (3.44 GPA).
  * **ASELSAN Aday Mühendis Havuzu** & **TEKNOFEST Robotaksi Finalisti**.
  * Araç CAN-FD / CAN-Bus hat dinleme, FPGA, sensör kablolama, PDU güç dağıtımı, kalibrasyon.
  * Hyundai Ioniq 5'in fiziksel kablolama, tavan podu ve Jetson Orin donanım entegrasyonundan sorumlu lider.
* **DOĞUKAN BAYRAM (Kurucu Ortak & Operasyon Direktörü, %20 Hisse):**
  * Reşit kurucu ortak ve şirketin resmi imza yetkilisi.
  * SPK yasal süreçleri, Takasbank/MKK entegrasyonu, İTO BTM ve devlet hibe ilişkileri.
  * Filo kiralama, lojistik anlaşmaları ve saha bekleme hub'larının resmi yönetimi.

---

## 8. KAMPANYA SONRASI 12 AYLIK KİLOMETRE TAŞLARI (ROADMAP)

| Dönem | Ulaşılacak Somut Hedef (Milestone) | Çıktı & Doğrulama |
| :--- | :--- | :--- |
| **Ay 1** | Takasbank'tan fonun kasaya geçmesi, A.Ş. tescili, Hyundai Ioniq 5 aracının satın alınması. | Araç ruhsatı & şirket bilançosu. |
| **Ay 2** | Ouster 128-LiDAR, Jetson Orin ve sensörlerin Denizcan tarafından araca montajı ve kalibrasyonu. | Canlı sensör veri akışı & CAN-FD testi. |
| **Ay 3** | Bilişim Vadisi Test Pisti'nde kapalı alan ilk boş sürücü koltuklu test sürüşü ve 4K sinematik video çekimi. | **TÜRKİYE LANSMAN VİDEOSU YAYINI.** |
| **Ay 4 - 6** | Oğuz Alper Öktem (Martı TAG) ile robotaksi pilot protokolü masasına oturulması ve BTM Fulya ringi. | Martı Autonomous Pilot Sözleşmesi. |
| **Ay 7 - 12** | Trustia Ride mobil uygulaması ile ilk 100 davetli yolcunun taşınması ve Seri A turuna hazırlık. | Şirket değerlemesinin 500M TL'ye çıkması. |

---

**NİHAİ ONAY VE KURUCU TAAHHÜDÜ:**  
İşbu belge; Trustia AI'ın Seviye-4 otonom robotaksi operasyonunu, 15.000.000 TL fonbulucu kitle fonlaması başvurusunu ve kurumsal büyüme stratejisini eksiksiz olarak kayıt altına almaktadır.  

**Murat Furkan Bayram** (Kurucu & CEO / Sistem Mimarı, %80)  
**Doğukan Bayram** (Kurucu Ortak & Operasyon Direktörü, %20)  
**Denizcan Özcan** (Donanım & Entegrasyon Mühendisi)  
**İTO Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Kampüsü, Beşiktaş / İstanbul**  
