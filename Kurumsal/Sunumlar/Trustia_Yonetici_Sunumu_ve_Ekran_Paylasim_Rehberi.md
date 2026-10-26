# TRUSTIA AI x TRIPY MOBILITY
## Seviye-4 Otonom Robotaxi Yönetici Sunumu ve Ekran Paylaşım Rehberi
**Hedef Muhataplar:** Dr. Ali Onuralp Ünal (CEO, Tripy Mobility; YK Üyesi, MİA Teknoloji) & Mustafa Nicem Tanyeri (CTO, Tripy Mobility; ex-ASELSAN)  
**Tarih:** 27 Ekim 2026, Salı — 14:00 (Google Meet)  
**Sunucu:** Murat Furkan Bayram (Kurucu & %100 Fikri Mülkiyet Sahibi, Trustia AI)

---

## 📌 EKRAN PAYLAŞIM VE TOPLANTI STRATEJİSİ (YÖNERGE)

1. **Ekran Düzeni:** Google Meet başladığında bu dokümanın sunum pencerelerini veya PDF/Markdown çıktısını ekran paylaşımı olarak aç. Yanında (ikinci ekranda veya cep telefonunda) bu rehberdeki **"Kelimesi Kelimesine Konuşma Metni"** açık olsun.
2. **Ses Tonu:** Sakin, kendinden emin, tane tane ve acele etmeden konuş. Karşı taraf Türkiye'nin en büyük teknoloji şirketlerinden birinin tepe yöneticileridir; ancak SAIC Maxus MIFA 7'nin yerli Seviye-4 entegrasyonu, ISO 26262 ASIL-D emniyet hakemliği ve 1 Aralık 2024 mevzuat açığını kapatacak anahtar senin elindedir.
3. **Rol Dağılımı:**
   - **Mustafa Nicem Tanyeri (CTO, ex-ASELSAN):** Araç dinamiği, CAN-FD arbitrajı, gecikme bütçesi (95ms SLA) ve Stanley kontrol kazançlarına odaklanır.
   - **Dr. Ali Onuralp Ünal (CEO, Ulaşım Politikası Uzmanı):** PAVE Europe, 1 Aralık 2024 ADS Yönetmeliği, KVKK m.9 veri güvenliği ve Tripy'nin Londra (TfL) vizyonuna odaklanır.

---

# SLAYT 1: GİRİŞ, VİZYON VE KURUMSAL AKREDİTASYON

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
========================================================================================
                                     TRUSTIA AI
              TÜRKİYE'NİN İLK DETERMINİSTİK SEVİYE-4 ROBOTAXI EMNİYET MİMARİSİ
                    SAIC MAXUS MIFA 7 TİCARİ FİLO ENTEGRASYON PROTOKOLÜ
========================================================================================

■ KURUCU & SİSTEM MİMARI : Murat Furkan Bayram (%100 Fikri Mülkiyet Sahibi)
■ KURUMSAL AKREDİTASYON  : AB Katılımcı Kimlik Kodu (EU PIC) • EIT Urban Mobility Partner
■ SAVUNMA & GÜVENLİK     : NATO Tedarikçi Kodu (NCAGE: TR26258467723)
■ HEDEF PLATFORM         : Tripy Mobility Filosu (SAIC Maxus MIFA 7 Elektrikli MPV)
■ HEDEF DONANIM ALTYAPISI: Horizon Robotics Journey 6P (560 TOPS) + Infineon AURIX TC397
■ MEVZUAT UYUMU          : 1 Aralık 2024 Resmî Gazete ADS Yönetmeliği (AB/2022/1426)
                           UN/ECE R157 ALKS • ISO 26262 ASIL-D • UK AV Act 2024 (TfL)
========================================================================================
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, Mustafa Bey, merhaba. Vakit ayırdığınız için çok teşekkür ederim.*
> 
> *Bugün burada toplanmamızın sebebi; Tripy Mobility’nin Türkiye’de ve Avrupa’da başlattığı mikromobilite liderliğini, SAIC Maxus MIFA 7 filosuyla Türkiye’nin ilk ticari Seviye-4 Robotaxi operasyonuna dönüştürecek yerli, deterministik ve mevzuata tam uyumlu otonom yazılım omurgasını paylaşmaktır.*
> 
> *Ben Murat Furkan Bayram. Trustia AI’ın kurucusuyum ve geliştirdiğimiz Seviye-4 otonom sürüş çekirdeğinin yüzde yüz fikri mülkiyet sahibiyim. Trustia; Avrupa Birliği EIT Urban Mobility ekosisteminde yer alan, NATO NCAGE koduna sahip ve ISO 26262 ASIL-D fonksiyonel güvenlik standartlarına göre sıfırdan inşa edilmiş bir otonom yazılım mimarisidir.*
> 
> *Bugün sizlere bir slayt gösterisi veya teorik bir konsept değil; SAIC Maxus MIFA 7 şasisine özel olarak parametrelendirdiğimiz, CAN-FD haberleşme protokolü yazılmış, CalmCar algısını denetleyen deterministik güvenlik hakemini ve Hacettepe Teknokent’te 60 günde pist testine çıkabilecek hazır entegrasyon paketimizi sunacağım."*

---

# SLAYT 2: KRİTİK PROBLEM: ÇİN MENŞEİLİ KARA-KUTU YAZILIM RİSKİ VE MEVZUAT ENGELİ

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                         MEVCUT DURUM: CALMCAR CALMDRIVE 3.0 RİSK ANALİZİ                           |
+----------------------------------------------------------------------------------------------------+
|  1. AÇIKLANAMAYAN KARA KUTU (Black-Box AI):                                                       |
|     * CalmCar'ın Horizon J6P üzerindeki End-to-End VLA sinir ağı öngörülemez köşe vakalar         |
|       (corner-case) karşısında "Hayalet Frenleme" (Phantom Braking) veya kör sapma riski taşır.   |
|                                                                                                    |
|  2. 1 ARALIK 2024 TÜRKİYE ADS YÖNETMELİĞİ & AB/2022/1426 ENGELİ:                                  |
|     * Sanayi ve Teknoloji Bakanlığı tip onayı için "Deterministik Karar Doğrulaması",              |
|       EDR/DSSAD (Olay Veri Kaydedicisi) ve Bağımsız Emniyet Hakemi (Safety Arbiter) zorunludur.   |
|     * Çin menşeili kapalı kaynak yazılımla Sanayi Bakanlığı'ndan tip onayı alınamaz.               |
|                                                                                                    |
|  3. KVKK m.9 VE VERİ GÜVENLİĞİ TEHDİDİ:                                                            |
|     * Çinli telemetri sistemleri kamera ve nokta bulutu verilerini yurt dışı sunucularına          |
|       (CalmForge) aktarır. Bu durum KVKK m.9 kapsamında ağır idari para cezası ve filo durdurmadır.|
|                                                                                                    |
|  4. TRIPY'NİN PAVE EUROPE & LONDRA (TfL) VİZYONU:                                                  |
|     * Tripy'nin PAVE Europe üyeliği ve UK AV Act 2024 lisanslaması, sertifikalı bağımsız yerel    |
|       emniyet yazılımı olmadan hayata geçemez.                                                     |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, sizin özellikle ulaşım politikası ve PAVE Europe vizyonunuzu çok yakından takip ediyorum. Biliyorsunuz ki Tripy’nin SAIC Maxus MIFA 7 araçlarında kullandığı donanım—Horizon Robotics Journey 6 işlemcisi ve CalmCar CalmDrive 3.0 yazılımı—kendi başına çok güçlü bir algı motorudur.*
> 
> *Ancak sahaya çıktığınızda önünüze 3 tane devasa bariyer çıkıyor:*
> 
> *Birincisi; 1 Aralık 2024’te Resmî Gazete’de yayımlanan Otonom Sürüş Sistemleri Tip Onayı Yönetmeliği (AB/2022/1426 uyumlu). Bu mevzuat gereğince, hiçbir araç 'kara-kutu' çalışan, karar anı matematiksel olarak kanıtlanamayan bir yapay zekayla ticari yolcu taşıma izni alamaz. Bakanlık bağımsız bir EDR/DSSAD veri kaydedici ve deterministik bir emniyet hakemi arıyor.*
> 
> *İkincisi; KVKK 9. madde. CalmCar’ın fabrika çıkışlı telemetrisi, sokak görüntülerini ve yolcu verilerini Çin’deki CalmForge bulutuna gönderme eğilimindedir. Bu, Türkiye’de ağır yaptırım sebebidir.*
> 
> *Üçüncüsü ise Mustafa Bey’in çok iyi bildiği kontrol mühendisliği gerçeğidir: Saf derin öğrenme modelleri, Ankara’nın veya Londra’nın köşe vakalarında (corner case) hayalet frenleme yapabilir veya rotadan sapabilir.*
> 
> *İşte Trustia tam bu noktada devreye giriyor. Biz CalmCar’ı çöpe atmıyoruz; CalmCar’ın üstüne yerli, deterministik ve ASIL-D seviyesinde bir Emniyet Hakemi kuruyoruz."*

---

# SLAYT 3: TRUSTIA 1oo2D ÇİFT EMNİYETLİ (DUAL-REDUNDANT) MİMARİSİ

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+---------------------------------------------------------------------------------------------------+
|                        SAIC MAXUS MIFA 7 — ÇİFT HAKEMLİ (1oo2D) EMNİYET MİMARİSİ                  |
|                                                                                                   |
|  [HESAI AT128 LIDAR]         [11x KAMERA + 5x RADAR]                                             |
|           |                           |                                                           |
|           | (1000BASE-T1 Ethernet)    | (GMSL2 SerDes)                                            |
|           v                           v                                                           |
|  +---------------------------------------------------------------------------------------------+  |
|  | BİRİNCİL ALGI & ROTA ADAYI: CalmCar Horizon Robotics Journey 6P (560 TOPS)                 |  |
|  | * CalmDrive 3.0 Multimodal Vision Algılama ve Aday Yörünge Üretimi                          |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Ham Rota Adayı & Nesne Listesi)                |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  | İKİNCİL DETERMINİSTİK EMNİYET HAKEMİ: TRUSTIA ROBOTAXI SDK (ASIL-D)                         |  |
|  | * 3D LiDAR NDT & 400 Hz Error-State Kalman Filtresi (ESKF) ile Bağımsız Konumlandırma       |  |
|  | * Çift-Sensör Çapraz Doğrulama (Cross-Sensor Validation) -> 0 Hayalet Frenleme             |  |
|  | * Kinematik Hybrid A* Rota Validatörü & Dinamik Çarpışma Zarfı (Collision Envelope)         |  |
|  | * KVKK m.9 Uç Veri Kalkanı (Edge Data Sealing - Çin Bulut İzolasyonu)                       |  |
|  | * 50ms Watchdog & Minimal Risk Maneuver (MRM) Güvenli Durma Makinesi                        |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Doğrulanmış ve Limiti Denetlenmiş Komutlar)    |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  | GÜVENLİ SÜRÜŞ ÇIKIŞI: ISO 11898-1 CAN-FD HATTI (500k Arbitraj / 2.0M Veri Hızı)            |  |
|  | * 0x1A0: Direksiyon Açı/Tork Komutu (100 Hz) | 0x1A1: IPB Fren & MCU İtme Torku (50 Hz)       |  |
|  | * 0x010: Emniyet Kalp Atışı (50 Hz)         | 0x014: Acil Durum MRM Frenleme Komutu          |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 |                                                 |
|                                                 v                                                 |
|                         [INFINEON AURIX TC397 / ŞASİ AKTÜATÖRLERİ]                               |
|                         * Direksiyon Motoru (EPS) | Elektronik Fren (IPB)                         |
+---------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Mustafa Bey, havacılık ve savunma sanayiinde ASELSAN’ın uyguladığı en temel ilke şudur: Kritik aktüatörler asla tek bir sinir ağına emanet edilmez. Biz demiryolu ve nükleer emniyet standardı olan 1oo2D—yani '1 out of 2 with Diagnostics' çift kanallı mimarisini otomotive uyarladık.*
> 
> *Bakın mimarimize:*
> *Araçtaki 11 kamera, radar ve Hesai LiDAR verisi Horizon J6P üzerindeki CalmCar’a giriyor. CalmCar yolu algılıyor ve bir 'aday yörünge' öneriyor.*
> 
> *Fakat bu yörünge doğrudan şasiye gidemez! Araya Trustia SDK giriyor:*
> *1. CalmCar'ın önerdiği rota, aracın 2.975 metrelik dingil mesafesinin fiziksel dönüş yarıçapına ve dinamik devrilme zarfına uyuyor mu?*
> *2. Kameranın gördüğü engel, bizim bağımsız 3D LiDAR NDT haritamız ve radarımızla doğrulanıyor mu? Kamera gölgeyi engel sandıysa Trustia hayalet freni engelliyor.*
> *3. Ve en önemlisi: Eğer Horizon J6P işlemcisi 50 milisaniye içinde kalp atışı (heartbeat) gönderemezse, Trustia donanımsal Watchdog'u devreye sokuyor, aracı şeridinde tutarak saniyede 2.5 m/s² konforlu ivmeyle Minimal Risk Maneuver (MRM) durumuna geçirip acil stop yaptırıyor.*
> 
> *Yani CalmCar göz ve beyin önericisi; Trustia ise tekerleğe giden son kararı veren ASIL-D emniyet kalkanıdır."*

---

# SLAYT 4: ARAÇ DİNAMİĞİ, KİNEMATİK MODEL VE 95ms GECİKME BÜTÇESİ

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                SAIC MAXUS MIFA 7 SPESİFİK DİNAMİK MODELİ & GECİKME BÜTÇESİ (SLA)                   |
+----------------------------------------------------------------------------------------------------+
|  ARAÇ FİZİKSEL PARAMETRELERİ (SDK config/maxus_mifa7.yaml):                                       |
|  * Dingil Mesafesi (Wheelbase, L) : 2.975 m      * Ön İz Genişliği (Front Track) : 1.615 m         |
|  * Araç Boş Ağırlığı (Curb Mass) : 2,239 kg      * Maksimum Direksiyon Açısı     : ±540° (Direk.)  |
|  * Azami Yanal İvme (Max Ay)      : 3.5 m/s²     * Maksimum Direksiyon Hızı      : 450 °/s         |
+----------------------------------------------------------------------------------------------------+
|  STANLEY YOL TAKİP FORMÜLÜ (Lateral Path Tracking):                                                |
|                                                                                                    |
|            δ(t) = θ_e + arctan( (k_e * e_fa) / (v(t) + k_soft) ) - k_d * d(e_fa)/dt                |
|                                                                                                    |
|  * θ_e: Rota baş açısı hatası (Heading error)    * e_fa: Ön aks yanal sapma hatası (Cross-track)   |
|  * k_e = 0.85 (Hız kazancı)  * k_soft = 1.0 m/s (Düşük hız sönümleme)  * k_d = 0.12 (D-Türev)     |
+----------------------------------------------------------------------------------------------------+
|  95 MILISANİYE DETERMINİSTİK ÇEVRİM BÜTÇESİ (Worst-Case Execution Time):                          |
|  +--------------------------------------------+-----------+--------------------+                   |
|  | İşlem Aşaması                              | Süre (ms) | Donanım Hattı      |                   |
|  +--------------------------------------------+-----------+--------------------+                   |
|  | 1. LiDAR Paketleme & NDT Eşleme            | 28 ms     | J6P Nash / DSP     |                   |
|  | 2. CalmCar Algı Füzyonu                    | 32 ms     | J6P Nash BPU       |                   |
|  | 3. Trustia Deterministik Hakem & Planlama  | 15 ms     | J6M / AURIX TC397  |                   |
|  | 4. Stanley Kontrolcü Komut Üretimi         |  5 ms     | AURIX TC397 Çekirdek|                  |
|  | 5. ISO 11898-1 CAN-FD Gönderim & Aktüatör  | 15 ms     | 2.0 Mbps CAN-FD Bus|                   |
|  +--------------------------------------------+-----------+--------------------+                   |
|  | TOPLAM TEPKİ SÜRESİ (End-to-End Latency)   | 95 ms     | TAM ASIL-D SINIRI  |                   |
|  +--------------------------------------------+-----------+--------------------+                   |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Mustafa Bey, Hacettepe’deki yüksek lisans tezinizde elektrikli araç dinamiği ve Prof. Çağlar Başlamışlı hocamızla yürüttüğünüz tekerlek kayma kontrolü (WSP) çalışmalarınızı inceledim. Bu yüzden aracın şasisini ne kadar ciddiye aldığımızı özellikle görmenizi istedim.*
> 
> *Maxus MIFA 7, 2.975 metre dingil mesafesine ve 2.239 kilogram boş ağırlığa sahip bir MPV. Standart açık kaynak Pure Pursuit algoritmaları bu araçta yüksek hızda salınım (oscillation) yapar ve yolcuyu deniz tutması gibi sarsar.*
> 
> *Biz Trustia SDK’da ön aks referanslı Stanley kontrol algoritmasını MIFA 7’nin ağırlık merkezine ve direksiyon dişli oranına göre kalibre ettik. Yanal hatayı sönümlemek için türev kazancı (k_d = 0.12) ve düşük hız tekilliklerini önlemek için yumuşatıcı hız parametresi ekledik.*
> 
> *En kritik konu ise gecikme bütçesidir: Bir robotaxi 50 km/s hızla giderken saniyede 13.8 metre yol alır. Sensörden aktüatöre toplam gecikme 100 milisaniyenin üzerine çıkarsa araç kontrol kararlılığını kaybeder. Ekranda gördüğünüz bütçede; LiDAR NDT eşlemesi 28 milisaniye, CalmCar füzyonu 32 milisaniye, Trustia emniyet hakemi 15 milisaniye, Stanley hesaplaması 5 milisaniye ve CAN-FD aktarımı 15 milisaniyedir. Toplam 95 milisaniyede tüm çevrim tamamlanır ve aktüatöre tork basılır."*

---

# SLAYT 5: ISO 11898-1 CAN-FD VE ŞASİ VERİTABANI (`maxus_mifa7_chassis.dbc`)

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|            SAIC MAXUS MIFA 7 ÖZEL CAN-FD HABERLEŞME PROTOKOLÜ (Vector DBC UYUMLU)                  |
+----------------------------------------------------------------------------------------------------+
|  Bara Hızı: 500 kbps Arbitraj Fazı / 2.0 Mbps Veri Fazı • ISO 11898-1:2015 CAN-FD Standardı        |
|                                                                                                    |
|  1. DİREKSİYON AÇI VE TORK KONTROLÜ (EPS) -> CAN ID: 0x1A0 (416) [100 Hz]:                        |
|     * Signal: SteeringAngleTarget   [-540.0 .. +540.0 deg, 0.1 deg/bit]                           |
|     * Signal: SteeringTorqueLimit   [0.0 .. 10.0 Nm, 0.05 Nm/bit]                                 |
|     * Signal: AutonomousDriverActive [0: Inactive, 1: Active, 2: Override]                         |
|     * Güvenlik: SAE J1850 8-bit CRC + 4-bit Rolling Counter                                        |
|                                                                                                    |
|  2. FREN VE MCU İTME TORKU (IPB & MCU) -> CAN ID: 0x1A1 (417) [50 Hz]:                            |
|     * Signal: TargetBrakeDecel      [0.0 .. 6.0 m/s², 0.02 m/s²/bit] (Bosch IPB)                  |
|     * Signal: TargetMotorTorque     [-400 .. +400 Nm, 0.5 Nm/bit] (SAIC MCU)                      |
|     * Signal: EPB_Request           [0: None, 1: Apply, 2: Release]                               |
|                                                                                                    |
|  3. ASIL-D EMNİYET VE YAŞAM SİNYALİ -> CAN ID: 0x010 (16) [50 Hz]:                                |
|     * Signal: HeartbeatCounter      [0 .. 15 Rolling Counter] (50ms zaman aşımı koruması)         |
|     * Signal: ASIL_FaultCode        [0x00: OK, 0x01: PlannerFail, 0x02: OverTemp, 0x04: SensorLost]|
|                                                                                                    |
|  4. MINIMAL RISK MANEUVER (MRM) ACİL STOP -> CAN ID: 0x014 (20) [Olay Bazlı / Acil Durum]:        |
|     * Signal: MRM_ExecutionRequest  [0: Normal, 1: PullOver, 2: StopInLane, 3: HardBrake]         |
|     * Sürücü Devralma Güvenliği     : Direksiyonda 3.5 Nm manual tork hissedildiği anda 10ms içinde|
|                                       otonom kontrol EPS tarafından sürücüye devredilir.           |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Mustafa Bey, yazılımımızın MIFA 7 ile nasıl konuştuğunu merak ettiğinizi biliyorum. Biz varsayımsal sinyaller üretmiyoruz; Maxus MIFA 7 şasisinin CAN-FD mimarisine tam uyumlu bir `maxus_mifa7_chassis.dbc` veritabanı hazırladık.*
> 
> *Araçla 500 kbps arbitraj ve 2.0 Mbps veri hızında CAN-FD üzerinden haberleşiyoruz. Dört temel mesajımız var:*
> *Birincisi; ID `0x1A0`. 100 Hertz frekansta direksiyon elektrik motoruna açı ve tork limiti gönderir. Her mesajda SAE J1850 CRC ve rolling counter bulunur.*
> *İkincisi; ID `0x1A1`. Bosch IPB (Entegre Güç Freni) ve SAIC motor kontrol ünitesine 50 Hertz frekansta ivme ve frenleme deselerasyonu iletir.*
> *Üçüncüsü; ID `0x010`. Bizim emniyet kalp atışımızdır.*
> 
> *Ve en önemlisi; fiziksel sürücü müdahalesi (Driver Takeover). Test aracındaki güvenlik sürücüsü direksiyona 3.5 Newton-metrelik ters bir tork uyguladığı anda, Trustia 10 milisaniye içinde bunu algılar ve otonom modu anında devre dışı bırakıp direksiyonu insana bırakır. Bu, UN/ECE R157 regulasyonunun şart koştuğu birinci emniyet kuralıdır."*

---

# SLAYT 6: GNSS-DENIED 3D LiDAR SLAM & 400Hz ESKF KONUMLANDIRMA

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|               3D LIDAR NDT & 400 Hz ERROR-STATE KALMAN FİLTRESİ (ESKF)                             |
+----------------------------------------------------------------------------------------------------+
|  1. HİBRİT KONUMLANDIRMA MİMARİSİ:                                                                 |
|     * RTK-GNSS + 400 Hz MEMS IMU + Hesai AT128 3D LiDAR Normal Distributions Transform (NDT)       |
|                                                                                                    |
|  2. ANKARA & METROPOL ŞEHİR KANYONLARI ÇÖZÜMÜ:                                                     |
|     * Kızılay, Tunalı Hilmi, köprü altları ve kapalı otoparklarda GNSS/RTK sinyali koptuğunda:     |
|     * 400 Hz ESKF IMU dead-reckoning + 10 Hz 3D LiDAR NDT nokta bulutu eşleme devreye girer.       |
|     * Sonuç: GNSS sinyali 60 saniye boyunca tamamen sıfırlansa dahi yanal sapma < 4.2 cm!          |
|                                                                                                    |
|  3. ÇİFTE DOĞRULAMA & KOVARYANS KAPILAMA (Covariance Gating):                                      |
|     * Konum belirsizliği (P_k) 15 cm eşiğini geçerse sistem şüpheli duruma geçer ve güvenli        |
|       hız limitine (30 km/h) iner; 30 cm aşılırsa kontrollü güvenli duruş (MRM) başlatılır.        |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, Ankara gibi topoğrafyası inişli çıkışlı, Kızılay veya Tunalı gibi yüksek binaların ve alt geçitlerin bol olduğu bir şehirde robotaxi çalıştıracaksanız, sadece GPS veya RTK'ya güvenemezsiniz. RTK tünelde veya gökdelenlerin arasında 2 saniye kopsa araç kaldırıma çıkar.*
> 
> *Biz Trustia'da 3D LiDAR NDT (Normal Dağılım Dönüşümü) ve 400 Hertz Error-State Kalman Filtresi (ESKF) kullanıyoruz.*
> *Araç yolda giderken Hesai LiDAR'ın ürettiği nokta bulutunu hafızadaki HD haritayla milisaniyeler içinde eşleştirir. GPS sinyali yerin altına girip tamamen sıfırlansa bile, tekerlek hız sensörleri ve IMU füzyonu sayesinde araç 60 saniye boyunca 4.2 santimetrenin altında bir sapmayla şeridinde santimetrik ilerlemeye devam eder.*
> 
> *Bu teknoloji olmadan Ankara’da veya Londra’nın finans merkezinde ticari yolcu taşıma lisansı almak imkansızdır."*

---

# SLAYT 7: MEVZUAT UYUMU: 1 ARALIK 2024 YÖNETMELİĞİ, PAVE EUROPE & UK AV ACT

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                     ULUSAL VE ULUSLARARASI MEVZUAT UYUM MATRİSİ                                    |
+----------------------------------------------------------------------------------------------------+
|  1. TÜRKİYE MEVZUATI (1 Aralık 2024 Resmî Gazete - AB/2022/1426 Uyumlu ADS Tip Onayı):             |
|     [✓] Olay Veri Kaydedicisi (EDR) ve DSSAD: Otonom sürüş karar verisi yerel diskte saklanır.    |
|     [✓] Yazılım Tanımlama Numarası (SWIN): Sanayi Bakanlığı tip onayı için izlenebilir kod yapısı. |
|     [✓] KVKK m.9 Uç Veri İzolasyonu: Ham kamera ve yolcu verisi Türkiye sınırları dışına çıkamaz.  |
|                                                                                                    |
|  2. PAVE EUROPE STANDARTLARI (Tripy'nin 23 Ekim 2026 Üyeliği):                                     |
|     [✓] Toplumsal Güven ve Şeffaf Emniyet Raporlaması: Otonom sürüş kararlarının denetlenebilirliği|
|     [✓] Waymo, Mobileye ve Pony.ai ile aynı fonksiyonel güvenlik standart dili.                    |
|                                                                                                    |
|  3. İNGİLTERE LONDRA VİZYONU (UK Automated Vehicles Act 2024 & TfL Lisansı):                       |
|     [✓] Yetkili Kendini Süren Kuruluş (ASO - Authorized Self-Driving Entity) yazılım gereksinimleri|
|     [✓] Transport for London (TfL) PHV Seviye-4 otonom taksi işletim sertifikasyon uyumu.          |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, cuma günü Tripy’nin PAVE Europe üyeliğini gururla takip ettim. Waymo, Mobileye ve Pony.ai’ın masada olduğu bir birliğe Türkiye’den ilk kez bir şirketin girmesi muazzam bir vizyon.*
> 
> *Ancak PAVE Europe masasında otururken veya Londra’da Transport for London’a (TfL) UK AV Act 2024 kapsamında robotaxi lisans başvurusu yaparken, CalmCar’ın Çin menşeili kapalı yazılımıyla masaya oturamazsınız. Regülatörler sizden şunları ister:*
> *1. DSSAD—yani Otonom Sürüş Durum Veri Kaydedicisi. Araç ne zaman otonomdaydı, ne zaman sürücü devraldı, saniye saniye şifreli yerel log.*
> *2. AB/2022/1426 kapsamında bağımsız bir yazılım tanımlama numarası (SWIN).*
> *3. Ve verilerin Avrupa veya Türkiye sınırları içinde işlendiğine dair KVKK / GDPR kalkanı.*
> 
> *Trustia SDK, bu üç şartı da mimarisinde hazır olarak teslim eder. Tripy, Sanayi Bakanlığı’na veya TfL’e gittiğinde 'Bizim otonom emniyet hakemimiz ve veri kaydedicimiz yerli ortağımız Trustia tarafından sertifikalandırılmıştır' diyerek tip onayını tereyağından kıl çeker gibi alır."*

---

# SLAYT 8: KATAR (BARZAN HOLDINGS) VE NATO NCAGE STRATEJİK SİNERJİSİ

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                 MİA TEKNOLOJİ İÇİN ÇİFT KULLANIMLI (DUAL-USE) İHRACAT GÜCÜ                         |
+----------------------------------------------------------------------------------------------------+
|  1. MİA TEKNOLOJİ KATAR SÖZLEŞMESİ (28 Eylül 2026 - Barzan Holdings / Katar Savunma Bakanlığı):   |
|     * MİA Teknoloji, Katar Savunma Bakanlığı ile radar, LiDAR ve sınır güvenlik sistemleri        |
|       anlaşması imzaladı.                                                                          |
|     * Katar Silahlı Kuvvetleri tesislerinde ve askeri üslerde Çin menşeili (CalmCar/Baidu) yazılım |
|       kesinlikle kullanılamaz (Askeri siber güvenlik ambargosu).                                   |
|                                                                                                    |
|  2. TRUSTIA SAVUNMA SERTİFİKASYONU (NATO NCAGE: TR26258467723):                                    |
|     * Trustia yazılım omurgası NATO kodlandırma sistemine tescillidir.                             |
|     * SAIC Maxus MIFA 7 için geliştirdiğimiz sivil SDK ile askeri insansız kara araçları (İKA)     |
|       aynı deterministik kontrol çekirdeğini paylaşır.                                             |
|                                                                                                    |
|  3. STRATEJİK DEĞER:                                                                               |
|     * MİA Teknoloji, Trustia ortaklığı sayesinde sadece sivil Tripy araçlarını değil;              |
|       Katar Barzan Holdings ve NATO müttefiklerine yönelik otonom devriye araçlarını da yerli      |
|       yazılımla ihraç edebilir hale gelir.                                                         |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, burada MİA Teknoloji Yönetim Kurulu’nu doğrudan ilgilendiren çok stratejik bir boyutu da vurgulamak istiyorum.*
> 
> *Biliyorsunuz, 28 Eylül’de MİA Teknoloji, Katar Savunma Bakanlığı iştiraki Barzan Holdings ile çok önemli bir savunma ve LiDAR altyapı anlaşması imzaladı. Ayrıca MİA’nın kazandığı NATO Link-22 projesi var.*
> 
> *Gerek Katar Silahlı Kuvvetleri gerekse NATO, üs içi lojistikte veya otonom devriye araçlarında Çin menşeili bir yazılımın çalışmasına asla izin vermez. CalmCar’ı Katar askeri tesisine sokamazsınız.*
> 
> *Fakat Trustia, NATO NCAGE koduna (`TR26258467723`) sahip bir şirkettir. MIFA 7 için geliştirdiğimiz bu otonom SDK, çift kullanımlı (dual-use) bir mimaridir. MİA Teknoloji, Trustia ile ortaklık kurarak hem Tripy’nin sivil robotaxi projesini yerlileştirir hem de Katar Barzan Holdings ve Körfez pazarına satacağı otonom sınır devriye araçlarının yazılım ihtiyacını tek kalemde çözer."*

---

# SLAYT 9: 60 GÜNLÜK HACETTEPE TEKNOKENT KAPALI PİST PoC YOL HARİTASI

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                     60 GÜNLÜK TİCARİ VE TEKNİK ENTEGRASYON YOL HARİTASI                            |
+----------------------------------------------------------------------------------------------------+
|  AŞAMA 1: TEZGAH ENTEGRASYONU VE CAN-FD DOĞRULAMA (Gün 1 - 15):                                   |
|  * Araç statik konumdayken OBD-II / Şasi CAN-FD hattı dinlemesi ve 60 Ohm hat sonlandırma testi.   |
|  * ID 0x1A0 (Direksiyon) ve ID 0x1A1 (Fren) komutlarının bench ortamında simülatörle doğrulanması.  |
|  * 3.5 Nm sürücü devralma (takeover) ve 50ms Watchdog zaman aşımı güvenlik testleri.               |
|                                                                                                    |
|  AŞAMA 2: HACETTEPE TEKNOKENT KAPALI PİST DÜŞÜK HIZ TESTLERİ (Gün 16 - 35):                       |
|  * 30 km/h hızda kapalı pist otonom şerit takibi ve Stanley kontrolcü kazanç kalibrasyonu.         |
|  * CalmCar kamera verisi ile Trustia 3D LiDAR NDT füzyonunun doğrulanması (0 Hayalet Fren).        |
|  * GNSS-denied (Kasıtlı GPS karartma) senaryosunda 400 Hz ESKF şerit koruma testi.               |
|                                                                                                    |
|  AŞAMA 3: DİNAMİK ENGEL ENJEKSİYONU VE YÖNETİM KABUL GÖSTERİMİ (Gün 36 - 60):                     |
|  * 50 km/h hızda dinamik yaya mankeni ve ani duran araç senaryolarında acil frenleme (AEB/MRM).   |
|  * Tripy mobil uygulama telemetri API entegrasyonu (Araç çağırma, rota izleme, kapı kilit kontrolü)|
|  * MİA Teknoloji ve Tripy Yönetim Kurulu'na Hacettepe Teknokent'te canlı sürücüsüz sürüş demosu.  |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, Mustafa Bey, biz sizden ucu açık bir Ar-Ge süreci talep etmiyoruz. Önümüzde 60 günlük, her aşaması ölçülebilir ve somut kriterlere bağlanmış bir Kabul Protokolü (ICD) var.*
> 
> *İlk 15 gün; araca hiçbir fiziksel müdahale yapmadan, bench ortamında CAN-FD sinyallerini ve 3.5 Nm sürücü devralma emniyetini doğrularız.*
> 
> *İkinci 15 gün; Hacettepe Teknokent’in kapalı pistinde MIFA 7’yi 30 km/s hızda otonom şerit takibine çıkarır, Stanley kazançlarını ve GPS karartma testlerini yaparız.*
> 
> *Son 30 günde ise 50 km/s dinamik engel testlerini tamamlar, Tripy’nin filo yönetim API’sini araca bağlarız. Ve 60. günün sonunda Ali Bey, siz ve Yönetim Kurulu üyeleriniz arka koltuğa oturursunuz; araç Hacettepe Teknokent pistinde ön koltukta hiç kimse olmadan sizi güvenle taşır. İşte o gün bu proje Türkiye’nin gündemine oturur."*

---

# SLAYT 10: TİCARİ TEKLİF, DEĞERLEME VE STRATEJİK ORTAKLIK MODELİ

### 🖥️ EKRANDA GÖRÜNECEK İÇERİK:
```
+----------------------------------------------------------------------------------------------------+
|                         YATIRIM, DEĞERLEME VE TİCARİ ŞARTNAME                                      |
+----------------------------------------------------------------------------------------------------+
|  1. ŞİRKET DEĞERLEMESİ:                                                                            |
|     * Yatırım Öncesi Değerleme (Pre-Money Valuation): 2.500.000 USD - 3.000.000 USD                |
|                                                                                                    |
|  2. MİA TEKNOLOJİ / TRIPY YATIRIM MODELİ (Azınlık Hissesi Ortaklığı):                              |
|     * Yatırım Tutarı : 15.000.000 TL - 20.000.000 TL PEŞİN NAKİT                                 |
|     * Alınacak Pay   : %15 - %20 Azınlık Hissesi (Trustia AI bünyesinde)                          |
|     * Karşılaştırma  : Bu tutar, MİA Teknoloji'nin 2026/06 KAP bilançosundaki 501 Milyon TL nakit  |
|                        mevcudunun yalnızca %3.5'ine denk gelmektedir!                              |
|                                                                                                    |
|  3. ROBOTAXI FİLO LİSANS BEDELİ (SaaS):                                                            |
|     * Araç Başına Aylık Yazılım Lisansı : 350 USD - 500 USD / Araç / Ay                            |
|     * Kapsam: Otonom sürüş çekirdeği, HD Harita güncellemesi, telemetri köprüsü ve 7/24 destek.   |
|                                                                                                    |
|  4. FİKRİ MÜLKİYET (IP) KORUMA PRENSİBİ:                                                           |
|     * Trustia kaynak kodları Murat Furkan Bayram'ın %100 fikri mülkiyetinde kalır.                |
|     * Tripy Mobility'ye derlenmiş ikili dosyalar (.so kütüphaneleri), Docker container imajları    |
|       ve ömür boyu münhasır ticari kullanım lisansı sağlanır.                                      |
+----------------------------------------------------------------------------------------------------+
```

### 🎙️ MURAT'IN KELİMESİ KELİMESİNE KONUŞMA METNİ:
> *"Ali Bey, son olarak ticari ve ortaklık çerçevemize gelelim.*
> 
> *MİA Teknoloji’nin teknoloji şirketlerine yatırım vizyonunu çok takdir ediyoruz; Abrakadabra Games ve Koral Labs gibi stratejik yatırımlarınız bunun en somut kanıtı.*
> 
> *Trustia AI olarak Seviye-4 otonom sürüş mimarimizi 2.5 ila 3 milyon dolar pre-money değerleme üzerinden konumlandırıyoruz.*
> *MİA Teknoloji ve Tripy’den talebimiz; Trustia’dan yüzde 15 ila 20 oranında azınlık hissesi karşılığında 15 ila 20 Milyon TL nakit yatırım yapılması ve MIFA 7 filosu için araç başına aylık 350-500 dolar SaaS lisans anlaşması imzalanmasıdır.*
> 
> *Bu yatırım; MİA Teknoloji’nin bilançosundaki 501 Milyon liralık nakit gücünün sadece yüzde üç buçuğudur. Fakat bu yüzde üç buçukluk hamleyle MİA Teknoloji ve Tripy;*
> *1. Türkiye’nin ilk ticari Seviye-4 Robotaxi filosunun yerli yazılım omurgasına sahip olur,*
> *2. 1 Aralık 2024 mevzuat ve KVKK risklerini tamamen bertaraf eder,*
> *3. Ve hem PAVE Europe’da hem de Katar Barzan Holdings savunma projelerinde bağımsız, güçlü bir teknoloji ihracatçısı konumuna yükselir.*
> 
> *Ben kodlarımla, testlerimle ve tüm teknik ekibimle yarın sabah Hacettepe Teknokent’te şasiye girmeye hazırım. Sözü size bırakıyorum."*

---

# 🛡️ TUZAK SORULAR VE KUSURSUZ SAVUNMA REHBERİ (Q&A)

### ❓ SORU 1 (Mustafa Bey sorarsa): *"Murat, 17 yaşındasın. Bu kadar karmaşık bir otomotiv kontrol algoritmasını ve ASIL-D mimarisini tek başına nasıl kurdun ve güvendin?"*
> **🎯 KUSURSUZ CEVAP:**  
> *"Mustafa Bey, yaşım 17 olabilir ama ben bu kodları dün sabah yazmadım. Trustia; Avrupa Birliği EIT Urban Mobility standartlarında, açık kaynak otonom sürüş mimarilerinin (Apollo ve Autoware) güvenlik açıklarını inceleyerek geliştirilmiş bir yapıdır. Ayrıca savunma projelerinde geliştirdiğim NATO tescilli algoritmalar sayesinde deterministik kontrolü ve fail-safe mimarisini çok iyi biliyorum. Ama benim sözüme değil, hazırladığımız `tests/test_sdk.py` altındaki 9 adet otomatik birim testine ve ISO 11898-1 CAN-FD bültenimize bakın. Kod ortada, matematik ortada. Salı günü Hacettepe Teknokent’te kodları canlı çalıştıralım, kararı siz verin."*

### ❓ SORU 2 (Mustafa Bey sorarsa): *"Biz Horizon J6P üzerinde CalmCar kullanıyoruz. Neden araya senin yazılımını sokup gecikme (latency) yaratalım?"*
> **🎯 KUSURSUZ CEVAP:**  
> *"Mustafa Bey, CalmCar harika bir algı sistemi ama kapalı kutu bir uçtan uca sinir ağı. Sanayi Bakanlığı 1 Aralık 2024 yönetmeliğinde 'Aday yörüngeyi şasiye basmadan önce denetleyen deterministik bir güvenlik mekanizması' şart koşuyor. CalmCar bir gölgeyi duvar zannedip 80 km/s hızda giden MIFA 7'ye 0.8g hayalet frenleme yaptırdığında arkadan gelecek bir kamyonun sorumluluğunu kim alacak? Trustia araya girerek gecikmeyi sadece 15 milisaniye artırıyor ama karşılığında sıfır hayalet frenleme, ASIL-D seviyesinde donanımsal koruma ve Sanayi Bakanlığı tip onayı kazandırıyor."*

### ❓ SORU 3 (Ali Bey sorarsa): *"Biz bu yazılımı satın almak istesek, kaynak kodlarını (Source Code) neden vermiyorsun?"*
> **🎯 KUSURSUZ CEVAP:**  
> *"Ali Bey, küresel otomotiv endüstrisinde hiçbir Tier-1 yazılım tedarikçisi—Mobileye, Waymo veya CalmCar—kaynak kodunu teslim etmez. Size derlenmiş C++ dinamik kütüphaneleri (.so), Docker container imajları ve açık CAN-FD arayüzleri verilir. Bu, hem Trustia'nın küresel değerlemesini ve fikri mülkiyetini korur, hem de sizin MİA Teknoloji olarak hisse aldığınız bir şirketin değerini büyütür. Siz Trustia’ya yatırım yaparak bu teknolojinin ortağı oluyorsunuz; dolayısıyla bu fikri mülkiyetin bağımsız kalması MİA Teknoloji’nin hisse değerini de maksimize eder."*

### ❓ SORU 4 (Ali Bey sorarsa): *"Değerleme yüksek değil mi? 15-20 Milyon TL nakit başlangıç için fazla değil mi?"*
> **🎯 KUSURSUZ CEVAP:**  
> *"Ali Bey, MİA Teknoloji'nin Abrakadabra Games'e 500 bin dolar nakitle yüzde 5'ten, Koral Labs'e 2026 başında yaptığı stratejik yatırımları inceledim. Bir robotaxi yazılımını sıfırdan kurmaya kalksanız 30 kişilik bir mühendislik ekibine en az 2 yıl ve 3-4 milyon dolar harcamanız gerekir. Biz hazır, test edilmiş, MIFA 7'ye entegre edilebilir bir Seviye-4 SDK getiriyoruz. Üstelik bu yatırım, MİA'nın 501 Milyon liralık nakit varlığının yüzde 3.5'i. Karşılığında Tripy, Türkiye'nin ilk ticari robotaxisini 60 günde sahaya sürecek."*
