# TRUSTIA.COM.TR KURUMSAL POLİTİKALAR VE METİN GÜNCELLEME PAKETİ (REV.4)
## Tüm Politika Sayfaları, Alt Bilgi (Footer) ve Meta Etiketleri İçin Birebir Kopya-Yapıştır Değişim Metinleri

**Tarih:** 25 Ekim 2026  
**Kapsam:** 10 Adet Politika Sayfası, Ortak Footer ve JSON-LD / Meta Verileri  
**Hedef:** Sitedeki riskli ve belgesiz tüm unsurların (NATO NCAGE başvuru no, MSB 5201 izinsiz ihracat, ASELSAN/BAYKAR onaylanmamış unvanlar, abartılı hibe iddiaları) kaldırılması; yerlerinin uluslararası otomotiv ve derin teknoloji standartlarıyla (ISO 26262 ASIL-D, ISO 21434 CSMS, UN ECE R155/R156/R157, 1 Aralık 2024 ADS Yönetmeliği, KVKK m.9, OIN, EIT Urban Mobility) eksiksiz doldurulması.

---

### 1. YAZILIM LİSANSLAMA POLİTİKASI (SLA & EULA)
**URL:** `https://trustia.com.tr/politika/lisans/`  
**Değişecek Başlık:** TR-SLA-2026/Rev.4 | Sürüm: Kurumsal v4.0

```markdown
# YAZILIM LİSANSLAMA, SON KULLANICI LİSANS SÖZLEŞMESİ (EULA) VE HİZMET SEVİYESİ TAAHHÜDÜ (SLA)
**Doküman Kodu:** TR-SLA-2026/Rev.4 | **Sürüm:** Kurumsal v4.0  
**Yasal Dayanak:** 5846 Sayılı FSEK, 6098 Sayılı TBK, 6102 Sayılı TTK, UN ECE R156 (SUMS), ISO 26262 ASIL-D

### Genel Bakış ve Kapsam
İşbu sözleşme; TRUSTIA TEKNOLOJİ YAZILIM VE BİLİŞİM A.Ş. ("Trustia") tarafından geliştirilen Seviye 4 Otonom Sürüş Yazılım Çekirdeği, Algoritmik Karar Motorları ve Araç İçi Entegrasyon Katmanının (ROS 2 / POSIX / AUTOSAR Adaptive Uyumlu Köprü API'leri) orijinal ekipman üreticileri (OEM), ticari filo işletmecileri, sistem entegratörleri ve araştırma kurumları ("Lisans Alan") tarafından kullanım koşullarını, garanti kapsamını, kusur bazlı hizmet seviyesi (SLA) sınırlarını ve tarafların yasal sorumluluklarını düzenler.

---

### Madde 1 — Fikri Mülkiyet, Lisans Türü ve Kullanım Kısıtlamaları
1.1. **Lisansın Niteliği:** Trustia, Lisans Alan’a ilgili sipariş formunda belirtilen adet ve tanımlı araç şasisi/donanım düğümü ile sınırlı olmak üzere; dünya çapında, inhisari olmayan (non-exclusive), devredilemez, alt lisans verilemez ticari yazılım çalıştırma lisansı tahsis eder.  
1.2. **Mülkiyet Hakları:** Yazılım çekirdeği, kaynak kodları, veri setleri, matematiksel optimizasyon modelleri ve derlenmiş kütüphaneler üzerindeki tüm fikri mülkiyet hakları münhasıran Trustia'ya aittir (5846 Sayılı Kanun m. 2/3).  
1.3. **Tersine Mühendislik Yasağı:** Lisans Alan; yazılımın kaynak koduna dönüştürülmesi (decompilation), tersine mühendisliğe tabi tutulması (reverse engineering) veya güvenlik mekanizmalarının aşılması yönünde hiçbir girişimde bulunamaz.  
1.4. **Açık Kaynak Bileşenler ve Lisans Ayrımı:** Yazılım mimarisinde yararlanılan açık kaynaklı altyapı kütüphaneleri (Linux çekirdeği, ROS 2 altyapısı), kendi özgün açık kaynak lisanslama şartlarına (Apache 2.0, MIT, BSD) tabidir. Trustia’nın özgün deterministik karar ve yol planlama modülleri dinamik bağlantılı bağımsız API katmanları üzerinden korunmakta olup copyleft/GPL bulaşıcılığına karşı izole edilmiştir.

---

### Madde 2 — Sistem Entegrasyonu, Görev Tanımı (ODD) ve Sorumluluk Sınırları
2.1. **Yazılım Katmanı Sınırı:** Trustia, yalnızca tanımlı yazılım çekirdeğinin teknik şartnameye uygunluğundan sorumludur. Fiziksel araç şasisi, aktüatörler (direksiyon açı motorları, elektro-hidrolik fren sistemleri), kablo tesisatı, CAN-FD geçitleri ve sensör montaj rijitliği araç entegratörünün münhasır sorumluluğundadır.  
2.2. **İşletimsel Tasarım Alanı (ODD):** Seviye 4 otonomi yazılımı, yalnızca taraflarca yazılı olarak onaylanan ODD sınırları içerisinde (tanımlı coğrafi çit, hava durumu, azami operasyonel hız ve yol altyapısı) çalışmak üzere tasarlanmıştır. Belirlenen ODD parametreleri dışındaki kullanım veya operatör ihlallerinden doğabilecek kazalardan Trustia sorumlu tutulamaz.  
2.3. **Yasal İzinler ve Test Ruhsatları:** T.C. Sanayi ve Teknoloji Bakanlığı Otonom Sürüş Sistemleri (ADS) Yönetmeliği uyarınca gerekli yol test izinleri, plaka tahsisleri ve saha test sigortalarının temini Lisans Alan'a aittir.

---

### Madde 3 — Kusur Odaklı Servis Seviyesi Taahhüdü (Fault-Based SLA)
Teknik destek ve SLA garantileri; yalnızca Lisans Alan tarafından yazılı bildirilen, standart ortamda yeniden üretilebilen ve Trustia yazılım çekirdeğinden kaynaklandığı kanıtlanan arızaları kapsar:

| Arıza Seviyesi | Tanım ve Etki Kapsamı | İlk Müdahale | Çözüm / Geçici Çözüm |
|---|---|---|---|
| **Seviye 1 (Kritik - P1)** | Otonomi çekirdeğinin çökmesi veya acil duruşa (MRM) yol açan yazılımsal kilitlenmeler. | 4 Saat | 24 Saat (Kök Neden & Yama) |
| **Seviye 2 (Yüksek - P2)** | Sensör veri ayrıştırma sapması, harita lokalizasyon doğruluğunun tolerans dışına çıkması. | 12 Saat | 72 Saat (Kalibrasyon Düzeltmesi) |
| **Seviye 3 (Rutin - P3)** | Dokümantasyon güncellemeleri, telemetri arayüz bildirimleri. | 2 İş Günü | Bir sonraki minör sürüm |

---

### Madde 4 — Fonksiyonel Emniyet, SOTIF ve Fail-Safe Güvenceleri
4.1. **ASIL-D Güvenlik Mimarisinin Korunması:** Yazılım; fiziksel sürücü müdahalesinin (tork algılama veya fren basınç eşiği) 5 milisaniye içerisinde komut yetkisini insan operatöre devretmesini sağlayan donanım öncelikli güvenlik kilitlerini barındırır. Bu kilit hiçbir arayüz ile devre dışı bırakılamaz.  
4.2. **Watchdog ve Güvenli Durum (MRC):** Ana otonomi işlemcisi ile emniyet denetleyicisi arasındaki çevrim süresinde 200 ms üzerinde bir gecikme oluştuğunda, sistem deterministik olarak Minimum Risk Manevrası (MRM) başlatır ve aracı şeridinde kontrollü şekilde asgari risk durumuna (MRC) ulaştırır.  
4.3. **UN ECE R156 Yazılım Güncelleme Yönetimi (SUMS):** Tüm uzaktan ve kablolu yazılım güncellemeleri kriptografik dijital imza (ECDSA) ile korunur; araç tip onayı kimlik kütüğüne işlenmeden güncellenemez.
```

---

### 2. OTONOM GÜVENLİK VE FONKSİYONEL EMNİYET PROTOKOLÜ
**URL:** `https://trustia.com.tr/politika/otonom-guvenlik/`  
**Değişecek Başlık:** TR-SAF-2026/Rev.4 | Sürüm: Emniyet v4.0

```markdown
# SEVİYE 4 OTONOM SÜRÜŞ EMNİYETİ VE FONKSİYONEL GÜVENLİK PROTOKOLÜ
**Doküman Kodu:** TR-SAF-2026/Rev.4 | **Sürüm:** Emniyet v4.0  
**Uluslararası Standartlar:** ISO 26262:2018 (ASIL-D), ISO 21448:2022 (SOTIF), UN ECE R157, 1 Aralık 2024 ADS Yönetmeliği

### Emniyet Vizyonu ve Sıfır Kaza İlkesi
Trustia AI olarak otonom sürüş mimarimizin merkezinde insan hayatının mutlak korunması yer alır. Seviye 4 (SAE J3016) mimarimiz; tekil arıza noktalarını (Single Point of Failure - SPoF) tamamen ortadan kaldıran çok katmanlı sensör yedekliliği, deterministik yol planlaması, bağımsız emniyet gözetleyicileri (Safety Supervisors) ve donanımsal arıza-emniyet (Fail-Safe / Fail-Operational) ilkeleri üzerine inşa edilmiştir.

---

### Madde 1 — ISO 26262 ASIL-D Fonksiyonel Güvenlik ve Emniyet Yaşam Döngüsü
1.1. **Tehlike Analizi ve Risk Değerlendirmesi (HARA):** Otonomi yazılımımızın tüm işlevsel blokları ISO 26262 uyarınca sınıflandırılmış; direksiyon, ivmelenme ve frenleme aktüatör komut zincirleri en yüksek emniyet seviyesi olan ASIL-D gereksinimlerine göre tasarlanmıştır.  
1.2. **Kilit Adım Denetleyicisi (Lockstep Supervisor):** Ana algoritma işlemcisine paralel çalışan harici otomotiv sınıfı güvenlik mikrodenetleyicisi (Safety MCU / AURIX mimarisi), otonom kararların dinamik araç sınırları (azami yanal ivme: 0.3G, azami sapma açısı: 35 deg/s) içerisinde kaldığını bağımsız olarak doğrular.  
1.3. **5ms İnsan Operatör Öncelik Devri (Driver Override):** Güvenlik sürücüsünün direksiyon simidine 2.5 Nm üzeri tork uygulaması veya fren pedalına basması durumunda, emniyet devresi 5 milisaniye içinde tüm aktüatör yetkisini insana devreder.

---

### Madde 2 — Beklenen İşlev Emniyeti (ISO 21448 SOTIF)
2.1. **Heterojen Sensör Füzyonu:** Algılama sistemi; 3D LiDAR nokta bulutları, 360° HDR otomotiv kameraları ve 77 GHz milimetre dalga radarlarının verilerini düşük ve yüksek seviyede harmanlar. Sis veya aşırı güneş parlaması gibi tekil sensör körlenmelerinde sistem otomatik olarak diğer sensör kanallarıyla doğrulama marjını genişletir.  
2.2. **Çevresel Sınırların Tespiti (ODD Monitor):** Görüş mesafesinin 30 metrenin altına inmesi veya aşırı kar örtüsü nedeniyle yol çizgilerinin kaybolması durumunda sistem SOTIF protokolleri uyarınca hız limitini kademeli düşürür ve ODD çıkış manevrası planlar.

---

### Madde 3 — 200ms Watchdog Zamanlayıcı ve Minimum Risk Manevrası (MRM / MRC)
3.1. **Watchdog Kalp Atışı:** Algı, planlama ve kontrol düğümleri arasında saniyede en az 50 Hz döngü ile kalp atışı sinyali paylaşılır. Herhangi bir yazılım modülünden 200 milisaniye boyunca yanıt alınamaması durumunda sistem derhal arıza moduna geçer.  
3.2. **Minimum Risk Manevrası (MRM):** Arıza durumunda sistem panik frenleme yerine; aracın mevcut şerit içinde güvenli şekilde yavaşlamasını, dörtlü acil flaşörlerini yakmasını ve azami 0.25G yavaşlama ivmesi ile kontrollü olarak asgari risk durumunda (MRC) durmasını sağlar.

---

### Madde 4 — 1 Aralık 2024 ADS Yönetmeliği ve Veri Kayıt Sistemleri (EDR / DSSAD)
4.1. **Otonom Sürüş Veri Depolama Sistemi (DSSAD):** Sanayi ve Teknoloji Bakanlığı ADS Yönetmeliği ve UN ECE R157 uyarınca, otonom sistemin aktif/pasif olduğu zaman damgaları, sürücü devir talepleri ve arıza kayıtları silinemez WORM tabanlı yerel kara kutu (EDR) ünitesine kaydedilir.  
4.2. **Çarpışma Algılama ve Bağımsız E-Stop:** Araç kokpitinde bulunan donanımsal çift kontaklı acil durdurma (E-Stop) butonu ve darbe sensörleri, çarpışma algılandığı anda aktüatör hatlarının elektriğini 10 ms içinde mekanik olarak keser.
```

---

### 3. YERLİ TEKNOLOJİ VE ÖZGÜN MİMARİ POLİTİKASI
**URL:** `https://trustia.com.tr/politika/yerlilik/`  
**Değişecek Başlık:** TR-IND-2026/Rev.4 | Sürüm: Yerlilik v4.0

```markdown
# ÖZGÜN YAZILIM GELİŞTİRME, YERLİ TEKNOLOJİ VE EKOSİSTEM UYUMLULUK POLİTİKASI
**Doküman Kodu:** TR-IND-2026/Rev.4 | **Sürüm:** Yerlilik v4.0  
**Yasal Dayanak:** 5746 Sayılı Ar-Ge Kanunu, Sanayi ve Teknoloji Bakanlığı Yerli Malı Tebliği (SGM 2014/35), EIT Urban Mobility Prensipleri

### Misyon ve Yerli Mühendislik Vizyonu
Trustia AI, Türkiye’nin akıllı mobilite ve otonom araç teknolojilerindeki küresel rekabet gücünü artırmak amacıyla, kritik otonomi yazılım katmanlarında sıfır dış bağımlılık prensibiyle çalışmaktadır. Algoritmik mimarimiz, üçüncü taraf yabancı kapalı kutu yazılımlara veya ambargo riskli bulut servislerine bağımlı olmaksızın, tamamen yerli mühendislik iş gücüyle Türkiye'de geliştirilmektedir.

---

### Madde 1 — Özgün Yazılım Çekirdeği ve Sıfır Tedarikçi Bağımlılığı (Vendor Lock-in)
1.1. **Katmanlı Çekirdek Mimarisi:** Trustia’nın otonom sürüş mimarisi (3D SLAM Lokalizasyonu, Dinamik Yol Planlama - Hybrid A* & Lattice Planner, Kinematik Araç Modeli ve Model Öngörülü Kontrol - MPC); yerli mühendislik ekibimiz tarafından C++ ve Python dillerinde geliştirilmiştir.  
1.2. **Standartlara Dayalı Donanım Bağımsızlığı:** Yazılımımız, belirli bir donanım üreticisine bağlı kalmamak üzere AUTOSAR Adaptive, ROS 2 Humble ve standart POSIX tabanlı gömülü Linux mimarileriyle uyumlu bir soyutlama katmanı (HAL) kullanır. Bu sayede yerli ve uluslararası tüm elektrikli araç şasilerine entegre edilebilir.  
1.3. **Çevrimdışı Çalışma Kabiliyeti (GNSS-Denied):** Sistemimiz; GPS/uydu sinyalinin kesildiği tünellerde veya kapalı otoparklarda harici bir sinyal kaynağına ihtiyaç duymaksızın araç üzerindeki LiDAR, IMU ve tekerlek enkoderi verileriyle santimetre hassasiyetinde lokalizasyon icra eder.

---

### Madde 2 — Sanayi ve Teknoloji Bakanlığı Kriterleri ve Yerli Katkı Oranı
2.1. **Yerli Malı Tebliği Uyumluluğu:** Geliştirilen yazılım paketleri, Bilim, Sanayi ve Teknoloji Bakanlığı’nın SGM 2014/35 sayılı Yerli Malı Tebliği kapsamında %100 yerli katkı oranı kriterlerine uygun mühendislik girdisi ile üretilmektedir.  
2.2. **Tescil ve Kaynak Kodu Güvenliği:** Yazılım sürümlerimiz, Türk Patent ve Marka Kurumu (TÜRKPATENT) tescil süreçleri ve 5846 sayılı FSEK telif kayıtları ile güvence altına alınmaktadır.

---

### Madde 3 — Uluslararası İnovasyon Ekosistemi ve AB İşbirlikleri
3.1. **Avrupa Komisyonu Katılımcı Kimliği (PIC: 861711529):** Trustia, Avrupa Birliği Çerçeve Programları (Horizon Europe) nezdinde resmi katılımcı tüzel kişilik tesciline sahiptir ve sivil sürdürülebilir ulaşım konsorsiyumlarında yer almaktadır.  
3.2. **EIT Urban Mobility Katılımı (Partner ID: CUS15554):** Avrupa İnovasyon ve Teknoloji Enstitüsü (EIT) Ulaşım Ekosistemi kapsamında; karbon-nötr toplu taşıma, mikromobilite optimizasyonu ve şehir içi otonom servis teknolojileri alanlarında Ar-Ge projeleri yürütmektedir.  
3.3. **Doğrulanabilir Kuluçka Merkezleri:** Şirketimiz Ar-Ge ve mühendislik faaliyetlerini İstanbul Ticaret Odası Bilgiyi Ticarileştirme Merkezi (İTO BTM Fulya Kampüsü) bünyesinde resmi sözleşmeli olarak sürdürmektedir.
```

---

### 4. SİBER GÜVENLİK YÖNETİM SİSTEMİ (CSMS)
**URL:** `https://trustia.com.tr/politika/siber/`  
**Değişecek Başlık:** TR-SEC-2026/Rev.4 | Sürüm: Siber v4.0

```markdown
# OTOMOTİV SİBER GÜVENLİK YÖNETİM SİSTEMİ (CSMS) VE AĞ GÜVENLİĞİ POLİTİKASI
**Doküman Kodu:** TR-SEC-2026/Rev.4 | **Sürüm:** Siber v4.0  
**Uluslararası Standartlar:** ISO/SAE 21434:2021, UN ECE R155 (CSMS), UN ECE R156 (SUMS), NIST SP 800-53

### Siber Güvenlik Yaklaşımı ve Sıfır Güven (Zero-Trust) Mimarisi
Bağlantılı ve otonom araçlar (CAV), modern ulaşım altyapısının en kritik bileşenlerindendir. Trustia AI, otonom araç yazılım çekirdeğini ve araç içi haberleşme ağlarını; uzaktan müdahalelere, yetkisiz veri manipülasyonuna, CAN-Bus enjeksiyon saldırılarına ve hizmet dışı bırakma tehditlerine karşı "Derinlemesine Savunma" ve "Sıfır Güven" ilkeleriyle korur.

---

### Madde 1 — ISO/SAE 21434 ve UN ECE R155 Uyumluluğu
1.1. **Tehdit Analizi ve Risk Değerlendirmesi (TARA):** Sistem mimarimizdeki tüm varlıklar ve saldırı yüzeyleri ISO/SAE 21434 metodolojisine göre sürekli değerlendirilmekte, risk seviyeleri otomotiv güvenlik hedefleriyle eşleştirilmektedir.  
1.2. **Siber Güvenlik Yönetim Sistemi (CSMS):** Tasarımdan üretime, operasyondan hizmetten çıkarmaya kadar olan tüm yazılım yaşam döngüsü UN ECE R155 gereksinimleriyle uyumlu olarak yönetilir.

---

### Madde 2 — Araç İçi Ağ Güvenliği ve SecOC
2.1. **CAN-FD Ağ İzolasyonu ve Şifreleme:** Kritik aktüatör hatlarına (direksiyon ve frenleme) dış gateway veya bilgi-eğlence ünitelerinden doğrudan erişim engellenmiştir. Araç içi haberleşmede AUTOSAR Güvenli Yerleşik Haberleşme (SecOC) protokolleri uygulanır.  
2.2. **Kriptografik Komut Doğrulama:** Kontrol bilgisayarından aktüatörlere gönderilen her komut çerçevesi AES-128 CMAC veya HMAC-SHA256 algoritmaları ile imzalanır. Dinamik sayaç (monotonic counter) ve zaman damgası kontrolü ile paket tekrarı saldırıları engellenir.

---

### Madde 3 — Donanımsal Güvenlik ve Güvenli Önyükleme (Secure Boot)
3.1. **Donanımsal Güvenlik Modülü (HSM / TPM 2.0):** Şifreleme anahtarları ve cihaz kimlik sertifikaları araç üzerindeki güvenli donanım alanında (HSM) saklanır; fiziksel veya yazılımsal yollarla dışarı aktarılamaz.  
3.2. **Güvenli Önyükleme (Secure Boot):** İşletim sistemi çekirdeği ve otonomi yazılımları başlatılırken kriptografik imza doğrulaması yapılır. İmzalanmamış hiçbir ikili dosya yürütülemez.

---

### Madde 4 — Güvenli Uzaktan Güncelleme (OTA) ve Zafiyet Yönetimi (PSIRT)
4.1. **UN ECE R156 SUMS Uyumlu OTA:** Kablosuz yazılım güncellemeleri, uçtan uca TLS 1.3 şifreli tüneller üzerinden, ikili imza doğrulaması ve güvenli geri alma (A/B partitioning fail-safe rollback) mimarisi ile gerçekleştirilir.  
4.2. **Ürün Güvenliği Olay Müdahale Ekibi (PSIRT):** Olası güvenlik açıklarının bildirilmesi için kurumsal `security@trustia.com.tr` kanalı işletilir.
```

---

### 5. YAPAY ZEKA VE KARAR VERME ETİĞİ
**URL:** `https://trustia.com.tr/politika/etik/`  
**Değişecek Başlık:** TR-ETH-2026/Rev.4 | Sürüm: Etik v4.0

```markdown
# YAPAY ZEKA ETİĞİ, GÜVENLİ KARAR ALMA VE SAVUNMASIZ YOL KULLANICILARI POLİTİKASI
**Doküman Kodu:** TR-ETH-2026/Rev.4 | **Sürüm:** Etik v4.0  
**Uluslararası İlkeler:** AB Yapay Zeka Yasası (EU AI Act - Reg. 2024/1689), UNESCO YZ Etiği Tavsiyesi, BMVI Otonom Sürüş Etik Kuralları

### Etik İlkeler Bildirgesi
Trustia AI; geliştirdiği otonom sürüş algoritmalarında, yapay zeka karar mekanizmalarında ve filo koordinasyon modellerinde insan onurunu, kişi güvenliğini ve toplumsal refahı tüm ticari hedeflerin üzerinde tutar. Sistemlerimiz; öngörülebilir, denetlenebilir, adil ve insani değerlere tam uyumlu bir felsefeyle programlanmaktadır.

---

### Madde 1 — İnsan Yaşamının Dokunulmazlığı ve İkilem (Dilemma) Yönetimi
1.1. **Alman Etik Komisyonu (BMVI) Prensipleri:** Otonom karar algoritmalarımız; kaçınılmaz kaza ikilemlerinde insan hayatını kişilerin yaşı, cinsiyeti, engellilik durumu, ırkı veya herhangi bir kişisel niteliğine göre tartmayı veya önceliklendirmeyi kesinlikle reddeder.  
1.2. **Mülkiyet Zararına Karşı Can Güvenliği:** Bir kaza senaryosunun kaçınılmaz hale gelmesi durumunda, yazılımımız maddi hasar oluşturabilecek manevraları insan hayatına gelebilecek zararların mutlak önünde tutar.  
1.3. **Pozitif Ayrımcılık Yasağı:** Sistem, yolcular ile araç dışındaki yayalar arasında yapay bir hiyerarşi kurmaz; her koşulda toplam yaralanma riskini asgariye indiren deterministik frenleme yörüngesini icra eder.

---

### Madde 2 — Savunmasız Yol Kullanıcılarının Korunması (VRU - Vulnerable Road Users)
2.1. **Öncelikli Koruma Çemberi:** Şehir içi otonomi operasyonlarında yayalar, çocuklar, bebek arabaları, tekerlekli sandalyeli bireyler, bisikletliler ve mikromobilite kullanıcıları "Savunmasız Yol Kullanıcısı" (VRU) olarak tanımlanır.  
2.2. **Genişletilmiş Güvenlik Marjı:** VRU algılandığı anda sistem yanal takip mesafesini otomatik olarak artırır; yaya adımları ve hareket belirsizlikleri için çoklu olasılık modelleri çalıştırılır. Okul çevrelerinde operasyonel hız proaktif olarak 20 km/s altına indirilir.

---

### Madde 3 — Şeffaflık, Açıklanabilirlik (Explainable AI) ve İnsan Gözetimi
3.1. **AB Yapay Zeka Yasası Uyumluluğu:** Otonom sürüş yazılımımız, Regulation (EU) 2024/1689 kapsamında "Yüksek Riskli Yapay Zeka Sistemi" olarak sınıflandırılmış olup şeffaflık, risk yönetimi ve veri kalitesi denetimlerine tabidir.  
3.2. **İnsan Gözetimi (Human-on-the-Loop):** Sistem; yetkili filo teleoperatörlerinin veya araç içi güvenlik sürücülerinin her an telemetriyi izleyebileceği ve anında devreye girebileceği çift yönlü arayüzlerle desteklenir.  
3.3. **Kara Kutu Ayrıştırma Yeteneği:** Karar alma motorunda kullanılan modeller, her bir frenleme ve yönlendirme kararının arkasındaki sensör girdi gerekçelerini denetlenebilir kütüklere işler; denetlenemeyen kararlara izin verilmez.
```

---

### 6. FİKRİ VE SINAİ MÜLKİYET POLİTİKASI
**URL:** `https://trustia.com.tr/politika/mulkiyet/`  
**Değişecek Başlık:** TR-IP-2026/Rev.4 | Sürüm: Mülkiyet v4.0

```markdown
# FİKRİ VE SINAİ MÜLKİYET HAKLARI, AÇIK İNOVASYON VE PATENT UYUMLULUK BİLDİRİSİ
**Doküman Kodu:** TR-IP-2026/Rev.4 | **Sürüm:** Mülkiyet v4.0  
**Yasal Dayanak:** 6769 Sayılı Sınai Mülkiyet Kanunu, 5846 Sayılı FSEK, Ticari Sırlar Hukuku, Open Invention Network Prensipleri

### Fikri Haklar Politikası
Trustia AI; tescilli otonom sürüş algoritmalarını, yazılım mimarilerini, donanım-yazılım köprü tasarımlarını ve kurumsal marka kimliğini korurken, küresel açık inovasyon ekosistemine ve açık kaynak patent barışına tam sadakat gösterir.

---

### Madde 1 — Ticari Marka, Unvan ve Kurumsal Kimlik Hakları
1.1. **Marka Tescili:** "TRUSTIA", "TRUSTIA AI" markaları, logoları, grafik arayüz tasarımları ve web platformu; 6769 sayılı Sınai Mülkiyet Kanunu kapsamında koruma altındadır.  
1.2. **İzinsiz Kullanım Yasağı:** Trustia’nın yazılı izni olmaksızın ticari marka ve logolarımızın ticari reklam, sponsorluk izlenimi yaratma veya üçüncü taraf ürün tanıtımlarında kullanılması yasaktır.

---

### Madde 2 — Yazılım Telifi, Algoritmik Mülkiyet ve Ticari Sırlar
2.1. **Telif Koruması:** Deterministik otonomi çekirdeği, SLAM lokalizasyon kütüphaneleri, yol planlama ve kontrolcü kod blokları 5846 sayılı FSEK uyarınca ilim ve edebiyat eseri niteliğinde korunmaktadır.  
2.2. **Ticari Sırların Gizliliği:** Çekirdek yazılımımızın kaynak kodları, model parametreleri ve entegrasyon arayüz dokümantasyonları kurumsal ticari sır (Trade Secret) statüsündedir; yalnızca Kurumsal Gizlilik Sözleşmesi (NDA) tahtında yetkili ortaklarla paylaşılır.

---

### Madde 3 — Açık İnovasyon, OIN Katılımı ve Açık Kaynak Uyumluluğu
3.1. **Open Invention Network (OIN) Paktı:** Trustia AI; küresel açık kaynak patent savunma konsorsiyumu Open Invention Network topluluğunun lisansiyesidir. Linux Sistem Tanımı (LSD) kapsamındaki temel teknolojilere ilişkin patentlerin karşılıklı olarak bir dava konusu yapılmayacağını taahhüt eden küresel patent barışı anlaşmasına tam uyum sağlar.  
3.2. **Açık Kaynak Lisans Hijyeni:** Sistemimizde kullanılan açık kaynak kütüphaneler (ROS 2 Humble, Linux Kernel, Eigen, Ceres, PCL); katı açık kaynak lisans uyumluluk prosedürlerimiz gereğince taranmakta, telif ihlali riski barındırmayan lisans modelleri (Apache-2.0, MIT, BSD) modüler mimari ile entegre edilmektedir.
```

---

### 7. ÇİFT KULLANIMLI (DUAL-USE) TEKNOLOJİ VE İHRACAT POLİTİKASI
**URL:** `https://trustia.com.tr/politika/ihracat/`  
**Değişecek Başlık:** TR-EXP-2026/Rev.4 | Sürüm: İhracat v4.0

```markdown
# ÇİFT KULLANIMLI (DUAL-USE) TEKNOLOJİLER, İHRACAT KONTROLÜ VE TİCARET UYUMLULUK POLİTİKASI
**Doküman Kodu:** TR-EXP-2026/Rev.4 | **Sürüm:** İhracat v4.0  
**Uluslararası Rejimler:** Wassenaar Düzenlemesi (Dual-Use), AB Tüzüğü 2021/821, T.C. Ticaret Bakanlığı İhracat Rejimi, 5201 Sayılı Kanun İzin Çerçevesi

### Küresel Ticaret ve İhracat Uyumluluk Taahhüdü
Trustia AI; geliştirdiği otonom sürüş sistemleri, sensör füzyon yazılımları ve araç kontrol algoritmalarının uluslararası transferinde, ihracatında ve sınır ötesi teknoloji ortaklıklarında Türkiye Cumhuriyeti kanunlarına, uluslararası çift kullanımlı (dual-use) teknoloji ihracat kontrol rejimlerine ve Birleşmiş Milletler Güvenlik Konseyi kararlarına tam uyum göstermeyi kurumsal politika olarak benimsemiştir.

---

### Madde 1 — Çift Kullanımlı (Dual-Use) Sivil Teknoloji Rejimi
1.1. **Temel Ticari Odak:** Trustia yazılım platformu; temel olarak sivil karayolu taşımacılığı, Seviye 4 Robotaksi operasyonları, lojistik kampüs araçları ve akıllı ulaşım altyapıları için geliştirilmiş bir sivil yazılım teknolojisidir.  
1.2. **Wassenaar Düzenlemesi ve Çift Kullanım İlkeleri:** Sistemimizin yüksek hassasiyetli haritalama (3D SLAM), otonom seyrüsefer ve gömülü kontrol yetenekleri; Çift Kullanımlı Malzeme ve Teknolojilerin İhracat Denetimine İlişkin Wassenaar Düzenlemesi ve T.C. Ticaret Bakanlığı’nın ilgili tebliğleri uyarınca incelenir.

---

### Madde 2 — Savunma Mevzuatı ve T.C. Resmi İzinlerine Kesin Tabiyet İlkesi
2.1. **5201 Sayılı Kanun Hükümleri:** Otonomi yazılımlarımızın veya ilgili teknik verilerin savunma sanayii, insansız kara araçları (İKA) veya askeri platformlara uyarlanması veya bu alanda yurt dışına transferi gündeme geldiğinde; 5201 sayılı Kanun uyarınca T.C. Milli Savunma Bakanlığı (MSB) ve T.C. Savunma Sanayii Başkanlığı’nın (SSB) resmi kuruluş, üretim ve ihracat izinleri eksiksiz olarak alınmadan hiçbir sınır ötesi transfer gerçekleştirilemez.  
2.2. **Firma Tanıtım Kodlarının Niteliği:** Şirketimiz nezdinde yürütülen kurumsal kodlandırma kayıtları yalnızca firma tanıtım kimliği mahiyetinde olup, yetkili kamu otoritelerinden alınması zorunlu olan münferit ihracat lisanslarının yerine geçmez.

---

### Madde 3 — Uluslararası Yaptırımlar, Ambargolar ve Son Kullanıcı Beyanı (EUC)
3.1. **Yaptırım Uyumu:** Birleşmiş Milletler Güvenlik Konseyi (BMGK), Avrupa Birliği veya yürürlükteki uluslararası yaptırım listelerinde yer alan kişi, kurum, rejim veya ambargo altındaki ülkelere hiçbir teknoloji transferi veya yazılım teslimi sağlanamaz.  
3.2. **Son Kullanıcı ve Son Kullanım Doğrulaması:** İhracat veya teknoloji işbirliklerinde alıcı taraftan resmi "Nihai Kullanıcı Belgesi" (End-User Certificate - EUC) talep edilir; yazılımın kitle imha silahları veya yetkisiz askeri amaçlarla kullanılmayacağı teyit altına alınır.
```

---

### 8. KVKK VE UÇ BİLİŞİM AYDINLATMA METNİ
**URL:** `https://trustia.com.tr/politika/kvkk/`  
**Değişecek Başlık:** TR-KVKK-2026/Rev.4 | Sürüm: KVKK v4.0

```markdown
# 6698 SAYILI KANUN UYARINCA KİŞİSEL VERİLERİN KORUNMASI VE UÇ BİLİŞİM AYDINLATMA METNİ
**Doküman Kodu:** TR-KVKK-2026/Rev.4 | **Sürüm:** KVKK v4.0  
**Yasal Dayanak:** 6698 Sayılı KVKK (12 Mart 2024 / 7499 Sayılı Kanun Değişikliği Dahil), Aydınlatma Yükümlülüğü Tebliği

### Veri Sorumlusunun Kimliği
6698 sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") uyarınca, veri sorumlusu sıfatıyla **TRUSTIA TEKNOLOJİ YAZILIM VE BİLİŞİM A.Ş.** ("Trustia AI" - İTO BTM Fulya Yerleşkesi, Şişli / İstanbul), kişisel verilerinizin hukuka ve dürüstlük kurallarına uygun olarak işlenmesine ve gizliliğine azami hassasiyet göstermektedir.

---

### Madde 1 — İşlenen Kişisel Veri Kategorileri ve Toplama Yöntemleri
1.1. **Kurumsal İletişim Verileri:** Web sitemiz, demo başvuru formları ve ticari iletişim kanalları üzerinden paylaştığınız ad-soyad, kurumsal e-posta, unvan, şirket adı ve telefon numarası bilgileri.  
1.2. **Dijital İz ve İşlem Güvenliği Verileri:** Web sitesi ziyaretçilerimizin IP adresleri, oturum çerezleri ve erişim log kütükleri (5651 Sayılı Kanun uyarınca).  
1.3. **Otonom Test Filosu ve Çevresel Algılama Verileri:** Saha test araçlarımızın üzerinde yer alan kamera ve LiDAR sensörleri vasıtasıyla, yalnızca seyir güvenliği ve engel tespiti amacıyla kamusal alandan anlık olarak toplanan çevresel görüntü kayıtları.

---

### Madde 2 — Uç Bilişim (Edge AI) ve Gerçek Zamanlı Anonimleştirme
2.1. **Bellek İçi (In-Memory) Anonimleştirme:** Otonom test araçlarımızdaki kamera ve LiDAR sensörlerinden gelen ham görüntü akışları; araç içi merkezi yapay zeka işlemcisinde (Edge AI) doğrudan uçta işlenir. Yayaların yüzleri ve trafikteki diğer araçların tescil plakaları, veri kalıcı depolama birimine yazılmadan önce RAM seviyesinde pikselleştirme algoritmalarıyla anında geri döndürülemez biçimde anonim hale getirilir.  
2.2. **Biyometrik Veri İşleme Yasağı:** Trustia AI, kamusal alandan toplanan görüntüler üzerinden kişilerin kimlik tespiti, yüz tanıma veya biyometrik profil çıkarma işlemlerini kesinlikle yapmaz ve bu amaçla veri saklamaz.  
2.3. **DSSAD ve Güvenlik Kütükleri:** Otonom sürüş kaza veri kayıt sisteminde (DSSAD / EDR) tutulan veriler yalnızca araç dinamiğini (hız, fren basıncı, direksiyon açısı, sistem müdahale zamanı) içermekte olup kişisel veri barındırmaz.

---

### Madde 3 — Veri İşleme Amaçları ve Hukuki Sebepler
Kişisel verileriniz; KVKK Madde 5/2 uyarınca kanunlarda açıkça öngörülmesi, bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması ve meşru menfaatlerimiz kapsamında işlenir.

---

### Madde 4 — Yurt Dışına Veri Aktarımı (KVKK Madde 9 Yeni Düzenlemesi)
12 Mart 2024 tarihli ve 7499 sayılı Kanun ile yenilenen KVKK Madde 9 uyarınca;  
4.1. **Yerel Depolama İlkesi:** Saha operasyon kütükleri ve kurumsal veriler Türkiye Cumhuriyeti sınırları içerisindeki güvenli sunucularda saklanır; kural olarak yurt dışına aktarılmaz.  
4.2. **Uluslararası Bulut / AB İşbirlikleri:** Uluslararası Ar-Ge projeleri kapsamında yurt dışı aktarımı zorunlu olduğunda; Kişisel Verileri Koruma Kurulu tarafından ilan edilen **Standart Sözleşmelerin (Standard Contractual Clauses)** akdedilmesi ve Kurum'a tescili güvencesiyle aktarım icra edilir.

---

### Madde 5 — İlgili Kişinin Hakları ve Başvuru Usulü
KVKK Madde 11 uyarınca ilgili kişiler hak taleplerini `kvkk@trustia.com.tr` kayıtlı e-posta adresine veya şirket adresimize yazılı olarak iletebilirler.
```

---

### 9. KURUMSAL GİZLİLİK VE ÇEREZ POLİTİKASI
**URL:** `https://trustia.com.tr/politika/gizlilik/`  
**Değişecek Başlık:** TR-PRIV-2026/Rev.4 | Sürüm: Gizlilik v4.0

```markdown
# KURUMSAL VERİ GİZLİLİĞİ, ÇEREZ VE DİJİTAL PLATFORM KULLANIM İLKELERİ
**Doküman Kodu:** TR-PRIV-2026/Rev.4 | **Sürüm:** Gizlilik v4.0  
**Uluslararası Uyumluluk:** GDPR, 5651 Sayılı Kanun, e-Gizlilik Direktifi

### Kurumsal Gizlilik Taahhüdü
Trustia AI olarak; `trustia.com.tr` alan adı üzerinden sunduğumuz dijital hizmetlerde ve kurumsal müşteri iletişimlerinde paylaşılan tüm bilgilerin gizliliğini en üst düzeyde korumayı taahhüt ederiz.

---

### Madde 1 — Çerez (Cookie) Kullanımı ve Yönetimi
1.1. **Zorunlu Çerezler:** Web sitemizin teknik olarak çalışabilmesi ve güvenlik doğrulamalarının yapılabilmesi için zorunlu çerezler kullanılmaktadır.  
1.2. **Analitik Çerezler:** Sitemizin kullanıcı deneyimini ölçümlemek amacıyla yalnızca anonimleştirilmiş IP adresleri üzerinden istatistiki analitik çerezler tutulmaktadır.  
1.3. **Pazarlama Çerezleri Yasağı:** Platformumuzda kullanıcıların davranışsal profillerini çıkaran veya üçüncü taraf reklam ağlarıyla veri paylaşan izleme çerezleri KESİNLİKLE KULLANILMAZ.  
1.4. **Çerez Tercihleri:** Ziyaretçiler diledikleri an tarayıcı ayarları üzerinden çerezleri temizleme veya engelleme hakkına sahiptir.

---

### Madde 2 — Kurumsal Gizlilik ve Gizlilik Sözleşmesi (NDA) İlkeleri
2.1. **Teknik Şartnameler:** Trustia AI tarafından OEM ortaklarına ve yatırımcılara sunulan mühendislik şartnameleri, sensör şemaları ve CAN-FD sinyal tabloları gizli niteliktedir.  
2.2. **Gizlilik Sözleşmesi:** Bu kapsamdaki her türlü teknik veri paylaşımı, taraflar arasında akdedilecek resmi Karşılıklı Gizlilik Sözleşmesi (Mutual NDA) hükümlerine tabidir.

---

### Madde 3 — Telemetri ve Ağ İletişim Güvenliği
3.1. **Uçtan Uca Şifreleme:** Web platformumuz ve araç teleoperasyon kontrol köprüleri arasındaki tüm veri akışları en az 256-bit TLS 1.3 protokolü ile korunur.  
3.2. **Sızma Testleri:** Sistem altyapımız, düzenli olarak harici bağımsız penetrasyon testlerine tabi tutulur.
```

---

### 10. OPEN INVENTION NETWORK (OIN) BİLDİRGESİ
**URL:** `https://trustia.com.tr/politika/oin-lisans/`  
**Değişecek Başlık:** TR-OIN-2026/Rev.4 | Sürüm: OIN v4.0

```markdown
# OPEN INVENTION NETWORK (OIN) AÇIK İNOVASYON VE PATENT BARIŞI BİLDİRGESİ
**Doküman Kodu:** TR-OIN-2026/Rev.4 | **Sürüm:** OIN v4.0  
**Uluslararası Dayanak:** Open Invention Network Community License Agreement, Linux System Definition (LSD)

### Açık İnovasyon ve Patent Barışı Misyonu
Trustia AI; açık kaynak yazılım ekosisteminin işbirlikçi gücüne inanmakta ve otonom araç yazılım teknolojilerinin gelişiminde açık standartların desteklenmesini savunmaktadır. Bu doğrultuda şirketimiz, açık kaynak topluluğunu patent davalarına karşı koruyan küresel platform **Open Invention Network (OIN)** lisansiyesi olarak toplulukta yer almaktadır.

---

### Madde 1 — Open Invention Network (OIN) Katılımı ve Taraflar
1.1. **Topluluk Üyeliği:** Trustia Teknoloji Yazılım ve Bilişim A.Ş., Open Invention Network LLC tarafından yürütülen OIN Lisans Sözleşmesi’ni akdederek 4.000'den fazla küresel teknoloji şirketi ve otomotiv üreticisi ile birlikte OIN Topluluk Üyesi (Community Licensee) olmuştur.  
1.2. **Konsorsiyum Desteği:** Google, IBM, Sony, Toyota, SUSE, Philips ve Red Hat gibi dünya devlerinin desteklediği bu konsorsiyum, açık kaynak yazılımların küresel patent davalarından bağımsız, güvenli bir şekilde ticarileşmesini sağlar.

---

### Madde 2 — Lisans Kapsamı ve Linux Sistem Tanımı (LSD)
2.1. **Çapraz Patent Dokunulmazlığı (Non-Aggression):** OIN sözleşmesi uyarınca Trustia; OIN üyesi 4.000'i aşkın kuruluşa karşı, "Linux Sistem Tanımı" (LSD) kapsamındaki yazılım bileşenleri üzerinde sahip olduğu veya olabileceği patentleri bir patent davası konusu yapmayacağını karşılıklı olarak taahhüt etmiştir.  
2.2. **Karşılıklı Telifsiz Lisans Hakkı:** Bu taahhüt karşılığında Trustia; diğer tüm OIN üyelerinin portföyünde bulunan patentlere karşı, Linux Sistemi bileşenlerini telifsiz (royalty-free), dünya çapında ve güvenli şekilde kullanma ve dağıtma hakkı kazanmıştır.

---

### Madde 3 — Otonomi Mimarisi ile Açık Kaynak Entegrasyon Güvencesi
3.1. **Kullanılan LSD Bileşenleri:** Trustia otonomi mimarisinde yararlanılan Linux çekirdeği, ROS 2 haberleşme omurgası, OpenCV görüntü işleme kütüphaneleri ve temel ağ protokolleri OIN koruma şemsiyesi kapsamındadır.  
3.2. **Tescilli Kod ile Açık Kaynak Ayrımı:** Trustia’nın sıfırdan geliştirdiği özgün deterministik karar motorları, yörünge optimizasyon kütüphaneleri ve araç kontrol algoritmaları bağımsız fikri mülkiyetimiz olup, OIN patent barışı sayesinde açık kaynak kütüphanelerle güvenli bir mimaride bir arada çalışmaktadır.  
3.3. **OEM Güvencesi:** Bu uyumluluk; Trustia ile çalışacak araç üreticilerine (OEM) ve filo operatörlerine, üçüncü taraf patent risklerine karşı küresel düzeyde hukuki güvence ve öngörülebilirlik sunar.
```

---

### 11. ORTAK FOOTER (SİTE ALTLIĞI) İÇİN YENİ KURUMSAL METİN

Tüm sayfalarda en altta yer alan Footer bileşenindeki değişiklikler:

* **SİLİNECEK ESKİ METİN:**
  `ASELSAN: #0050569 • NATO: TR2625846`  
  `NATO NCAGE Askeri Tedarikçi`  
  `ASELSAN Potansiyel Tedarikçi`  
  `İhracat Kontrol (5201/MSB)`  
  `STANAG 4586`

* **YERİNE KONULACAK YENİ RESMİ METİN:**
  ```text
  TRUSTIA AI
  Şehir içi sivil Robotaksi filoları ve zorlu otonom test sahaları için geliştirilmiş Seviye 4 yerli otonomi yazılım platformu.
  İstanbul, Türkiye'de geliştirildi.
  İTO BTM Fulya Kampüsü, Şişli / İstanbul

  Standartlar & Uyumluluk:
  SAE J3016 Seviye 4 • ISO 26262 ASIL-D • ISO/SAE 21434 CSMS • UN ECE R155/R156/R157 • EIT Urban Mobility Partner

  AKREDİTASYON VE TESCİLLER:
  - OIN Küresel Patent Paktı Lisansiyesi (#f1e44576)
  - Avrupa Birliği Horizon Europe (PIC: 861711529)
  - EIT Urban Mobility Ortaklığı (CUS15554)
  - İTO BTM Girişimcilik Tescili
  - İhracat Kontrolü & Çift Kullanım (Dual-Use)
  ```

---

### 12. GOOGLE VE META AÇIKLAMASI (META DESCRIPTION)

* **SİLİNECEK ESKİ METİN:**
  `... NATO NCAGE (TR26258467723), ASELSAN tedarikçi (#0050569), Avrupa Komisyonu (PIC: 861711529), Malta Enterprise ve İTO BTM tescilli ...`

* **YERİNE KONULACAK YENİ RESMİ METİN:**
  ```html
  <meta name="description" content="Trustia AI; şehir içi sivil Robotaksi filoları için ISO 26262 ASIL-D, 3D SLAM ve Seviye 4 yerli otonomi yazılım platformudur. Open Invention Network (OIN 2.0 Lisansı: #f1e44576), AB Horizon Europe (PIC: 861711529), EIT Urban Mobility (CUS15554) ve İTO BTM tescilli derin teknoloji girişimi (İstanbul, Türkiye)." />
  ```
