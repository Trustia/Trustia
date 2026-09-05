# TRUSTIA AI — OTONOM ARAÇ OPERASYON, GÜVENLİK, SİGORTA VE YASAL İZİNLER REHBERİ

Bu belge; Trustia AI Hyundai Ioniq 5 Seviye-4 Robotaksi test aracının **kaskosu, sigortası, arıza emniyeti, direksiyona insan müdahalesi, hırsızlık/kaçırılma koruması, park/garaj yeri, montaj ekibi, test sahaları ve devlet izin süreçlerini** A'dan Z'ye açıklayan resmi kurumsal operasyon dokümanıdır.

---

## 🛡️ 1. KASKO, SİGORTA VE HUKUKİ GÜVENCE

### 1.1 Özel Ar-Ge ve Test Aracı Kaskosu (Genişletilmiş Kloz)
* **Poliçe Türü:** Türkiye'de otonom ve prototip test araçları için büyük sigorta şirketleri (Allianz, Aksigorta, Anadolu Sigorta) tarafından sağlanan **"Ar-Ge & Otonom Sürüş Test Araçları Özel Kasko Poliçesi"** düzenlenir.
* **Kapsam:** Standart kaskoya ek olarak; araç üzerindeki 1.14M TL değerindeki **LiDAR, kamera, radar, bilgisayar ve sensörler poliçeye "Aksesuar & Özel Elektronik Ekipman" olarak fatura bedelleriyle eklenir.** Dolayısıyla sensörlere gelebilecek en ufak çizik, darbe, çalınma veya taş sıçraması %100 sigorta teminatı altındadır.
* **Üçüncü Şahıs Mali Mesuliyet:** Test esnasında olası bir temas durumunda üçüncü şahıslara ve çevreye gelebilecek zararlar için 50.000.000 TL limitli İMM (İhtiyari Mali Mesuliyet) kalkanı uygulanır.

### 1.2 T Plaka (Sarı Kuşaklı Geçici Ar-Ge Test Plakası)
* Karayolları Trafik Yönetmeliği Madde 46 uyarınca; Ar-Ge ve otonomi geliştiren yerli teknoloji şirketlerine T.C. İçişleri Bakanlığı Emniyet Genel Müdürlüğü ve Noterler Birliği tarafından **"Geçici Test Plakası (T Plaka)"** tahsis edilir.
* Bu plaka ile prototip araçlar resmi olarak trafiğe kapalı ve izinli açık güzergahlarda yasal güvenceyle test edilir.

---

## 🎮 2. DİREKSİYONA EL SÜRÜLÜRSE / İNSAN MÜDAHALESİ (OVERRIDE)

Otonom araçlarda dünya standardı **ISO 26262 ASIL-D ve SAE J3016 İnsan Önceliği (Human Takeover)** kuralıdır.

```
[İnsan Direksiyona Dokundu] ──> [Tork > 2.0 Nm] ──> [5 ms İçinde Otonomi Devre Dışı] ──> [Tam Kontrol İnsanda]
[İnsan Frene Dokundu]        ──> [Basınç > 5 bar] ──> [1 ms İçinde Otonomi Devre Dışı] ──> [Fren İnsanda]
[İnsan Gaza Bastı]          ──> [Gaz > %5]       ──> [Otonomi Hız Sınırlaması Kapatılır]
```

### 2.1 Anında Devre Dışı Kalma (Torque & Brake Override)
* **Direksiyona El Sürülürse:** Güvenlik sürücüsü veya araç içindeki biri direksiyonu hafifçe tutup çevirdiği an (2.0 Nm tork eşiği aşıldığında), Trustia kontrolcüsü **5 milisaniye içinde direksiyon motorunun kontrolünü bırakır.** Direksiyon tamamen normal bir insan aracına dönüşür.
* **Frene Basılırsa:** Fren pedalına 1 milimetre dahi basıldığı anda CAN-FD hattındaki otonom fren komutu kesilir ve arabanın orijinal hidrolik freni sürücünün ayağına geçer.
* **Fiziksel E-Stop Butonu:** Konsoldaki Schneider mantar butona basıldığı an tüm otonomi sisteminin elektriği kesilir, araba standart fabrika moduna döner.

### 2.2 Kaza veya Arıza Durumu (Fail-Safe & Minimum Risk Maneuver)
* Bir sensör kopsa, kablo çıksa veya bilgisayar donarsa:
  1. **200ms Emniyet Bekçisi (Watchdog):** Sistem anında arızayı algılar.
  2. **Dörtlüleri Yakar & Kornayı Çalar:** Çevredeki yayaları ve araçları uyarır.
  3. **Güvenli Kenara Çekme (MRM - Minimum Risk Maneuver):** Aracı şerit çizgileri içinde yavaşlatıp yumuşak bir frenle güvenli şekilde durdurur ve el frenini (EPB) çeker.
* **Kara Kutu (Black Box):** Samsung 4TB SSD her saniye 350 MB hızla LiDAR, kamera, direksiyon açısı ve fren telemetrisini kaydeder. Olası bir durumda milisaniyelik adli kaza analizi yapılır.

---

## 🔒 3. HIRSIZLIK, KAÇIRILMA VE SİBER GÜVENLİK KORUMASI

Aracın çalınması, kaçırılması veya kötü niyetli müdahalelere karşı 4 kademeli savunma mimarisi aktiftir:

1. **5G GPS Geofencing (Sanal Çit Kalkanı):**
   * Teltonika RUTX50 5G Router, aracın GPS koordinatlarını saniyede 10 kez Trustia Bulut Sunucusuna gönderir.
   * Araç belirlenen test güzergahının (örn: BTM Fulya Kampüsü veya Bilişim Vadisi Pisti) **5 metre dışına izinsiz çıkarsa sistem otomatik olarak motoru ve tekerlekleri kilitler (Remote Immobilizer).**
2. **Uzaktan Teleoperasyon & Acil Kapatma:**
   * Trustia C2 Taktik Konsolundan tek bir butonla araç uzaktan stop ettirilebilir ve kapıları kilitlenebilir.
3. **7/24 Canlı Kabin ve Çevre Kamera Kaydı:**
   * 4 adet dış kamera ve 1 adet kokpit içi geniş açı kamera, araca yaklaşan veya içine binen herkesin yüzünü anında 5G ile buluta aktarır.
4. **Şifreli CAN-Bus İzolasyonu:**
   * Araçtaki otonomi beyni harici USB veya kablosuz yetkisiz saldırılara karşı çift katmanlı güvenlik duvarıyla (Firewall & Seed-Key Authentication) korunur.

---

## 🏢 4. ARABAYI NEREYE KOYACAĞIZ? (GARAJ, PARK & ŞARJ YERİ)

Aracın duracağı ve muhafaza edileceği 2 resmi kurumsal üs belirlenmiştir:

### 4.1 Ana Merkez: İTO BTM Fulya Kampüsü, Şişli / İstanbul
* **Adres:** İTO BTM Fulya Kampüsü, Şişli / İstanbul.
* **Özellikler:**
  * 7/24 Özel Güvenlikli ve Bariyerli Kapalı Yeraltı Otoparkı.
  * 360° Güvenlik Kameraları ve Yangın Söndürme Sistemleri.
  * Elektrikli Araç AC Hızlı Şarj İstasyonları (Ioniq 5 her an şarjda bekler).
  * Ofisimizin hemen altında, asansörle doğrudan iniş imkanı.

### 4.2 Test & Ar-Ge Üssü: Bilişim Vadisi Otonom Araç Test Merkezi (Gebze)
* Türkiye'nin resmi Mobilite İnovasyon Merkezi kapalı hangarları ve otonomi test garajı.
* Sanayi ve Teknoloji Bakanlığı onaylı otonom araç garajlama ve şarj alanı.

---

## 🛠️ 5. MONTAJI KİM YAPACAK, NEREDE VE NASIL YAPILACAK?

Montaj işlemi aracın orijinal gövdesine ve garantisine **asla zarar vermeyen, delme/kesme içermeyen "Tak-Çalıştır (Plug-and-Play)" modüler mimariyle** yapılır:

### 5.1 Montaj Ekibi:
* **Sistem Mimarı & Lider:** Murat Furkan Bayram (Trustia Kurucu & CEO).
* **Donanım & Test Mühendisi:** Denizcan Özcan (ASELSAN & TEKNOFEST Robotaksi Finalisti, İÜC Elektrik-Elektronik).
* **Mekanik / Elektrik Desteği:** BTM / Bilişim Vadisi Mobilite Hızlandırma Atölyesi Kıdemli Teknisyenleri.

### 5.2 Montaj Aşamaları (Toplam Süre: 2 Gün):
1. **1. Gün (Mekanik):** Drs Tuning siyah tavan barı Ioniq 5'in tavan raylarına kilitlenir. Ouster LiDAR ve kameralar M6 kauçuk titreşim takozlarıyla bara vidalanır. Tampon Livox LiDAR'ları 3D baskılı ABS braketlerle ızgaraya takılır.
2. **2. Gün (Elektrik & Kablolama):** Kablo demeti IP68 buat kutusundan bagaja alınır. Bagaj alt havuzuna Seeed J501 Orin bilgisayarı, Interkom sigorta panosu ve Teltonika router vidalanır. OBD-II / Kamera soketine Kvaser CAN-FD arayüzü takılır.

---

## 🚦 6. TEST SÜRECİ VE AŞAMALI YOL HARİTASI

Testler 4 kademeli uluslararası güvenlik protokolüyle yürütülür:

```
[Aşama 1: Simülasyon] ──> [Aşama 2: Kapalı Test Pisti] ──> [Aşama 3: Kampüs İçi] ──> [Aşama 4: İzinli Açık Yol]
(Webots 3D - 1.301 Test)   (Bilişim Vadisi 1.5 km Pist)    (BTM / İTÜ Ayazağa)       (T Plaka & Güvenlik Şoförü)
```

1. **1. Aşama (Simülasyon - TAMAMLANDI ✅):** 1.301 birim ve entegrasyon testi Webots 3D ortamında %100 başarıyla tamamlandı.
2. **2. Aşama (Kapalı Otonom Test Pisti):** Bilişim Vadisi Gebze Kapalı Test Pisti'nde (trafiğe kapalı 1.5 km asfalt parkur, cansız yaya mankenleri, yapay kavşaklar ve trafik ışıkları) 0 risk ile ilk sürüşler yapılır.
3. **3. Aşama (Kampüs & Teknopark Alanı):** İTO BTM Fulya Kampüsü ve Teknopark İstanbul kapalı kampüs yollarında 20-30 km/s hızla yolcu alma/bırakma testleri.
4. **4. Aşama (Açık Yol & Trafik Testi):** Koltukta emniyet sürücüsü otururken, T plaka ve bakanlık izinleriyle belirlenen Şişli/Fulya veya Gebze güzergahında Seviye 4 sürüş.

---

## 📜 7. DEVLET İZİNLERİ VE RESMÎ REGÜLASYON BAŞVURULARI

Türkiye'de otonom araç testleri için yürütülen yasal süreç:

1. **T.C. Sanayi ve Teknoloji Bakanlığı (Milli Teknoloji Genel Müdürlüğü):**
   * *Mobilite Araç ve Teknolojileri Yol Haritası* kapsamında "Otonom Araç Test Başvuru Dosyası" sunulur.
2. **T.C. Ulaştırma ve Altyapı Bakanlığı (KGM):**
   * Belirlenen pilot test koridorları için yol güvenlik izni.
3. **İTO BTM ve Bilişim Vadisi Destek Mektubu:**
   * BTM Ön Kuluçka sözleşmemiz ve Bilişim Vadisi altyapısı sayesinde izin onayları çok hızlı çıkar.

---

*Tarih:* 5 Eylül 2026  
*Kurum:* TRUSTIA AI — Seviye 4 Otonom Sistemler  
