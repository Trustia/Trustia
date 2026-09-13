# TRUSTIA PROJESİ ZORUNLU ÇALIŞMA VE DOSYA YERLEŞİM KURALLARI (MANDATORY AGENT RULES)

> [!IMPORTANT]
> Bu kural seti, bu projede çalışacak **TÜM YAPAY ZEKA ASİSTANLARI VE AJANLAR İÇİN ZORUNLUDUR**.
> Masaüstüne veya proje kök dizinine rastgele, baştan savma dosya oluşturulamaz veya atılamaz.
> Üretilen her dosya, kod, görsel, video, PDF veya sertifika AMACINA GÖRE AŞAĞIDAKİ 6 KATEGORİDEN İLGİLİSİNE YERLEŞTİRİLMEK ZORUNDADIR.

---

## 📁 6 ANA KURUMSAL KATEGORİ VE KATI YERLEŞİM PLANI

Tüm dosyalar `C:\Users\Murat\Desktop\Trustia\` ana çatısı altında aşağıdaki 6 klasörde tutulacaktır:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Asıl Otonomi Yazılımı & Testler)
* **Buraya Konulacaklar:** Otonomi motoru, SLAM haritalama, Hybrid A* rota, Pure Pursuit kontrolcü, yapay zeka EYP/Mayın/KHKN tespit modelleri, CAN-Bus/ROS2/JAUS/Webots sürücüleri, 1.301 birim/entegrasyon testi, CLI scriptleri ve Taktik C2 Masaüstü Konsolu.
* **Kural:** Otonomi yazılımıyla ilgili tüm Python/C++ kodları ve testleri SADECE bu klasör altında oluşturulur veya düzenlenir.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Sitesi ve Platform Kodları)
* **Buraya Konulacaklar:** Canlı web sitesi kaynak kodları (Next.js 16, React 19, Tailwind CSS 4, Three.js 3D modeller, web sayfaları, bileşenler ve web API'leri).
* **Kural:** Web arayüzü ile ilgili her şey SADECE bu klasör altında `website/` içinde geliştirilir.

### 3. `03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/` 📜 (Resmi Belgeler ve Tesciller)
* **Buraya Konulacaklar:** KOSGEB sertifikaları, BTK ve SSB Savunma Sanayii sertifikaları, İTO BTM Ön Kuluçka Taahhütnameleri, Aselsan ve TÜBİTAK tedarikçi/araştırmacı evrakları.
* **Kural:** Resmi devlet/şirket tescil belgeleri başka hiçbir yere konulamaz.

### 4. `04_Yatirimci_Sunumlari_ve_Is_Planlari/` 💼 (Yatırımcı Dosyaları & Finans)
* **Buraya Konulacaklar:**
  * `Pitch_Decks/`: Yatırımcı sunumları (Global, Hub71, Demoday, EXIST vb.).
  * `Finansal_Tablolar/`: Bilanço, Gelir Tablosu (P&L), Nakit Akışı, Cap Table.
  * `Is_Plani_ve_Kanvas/`: İş Modeli Kanvası, İş Planı ve Finansal Raporlar.
  * `Teknik_ve_Organizasyon/`: Teknik mimari dokümanları ve organizasyon şemaları.
  * `Murat_Furkan_Bayram_CV_Resume.pdf`: Kurucu özgeçmişi.

### 5. `05_Uluslararasi_Hibe_ve_Vize_Basvurulari/` 🌍 (Global Fon ve Başvurular)
* **Buraya Konulacaklar:**
  * `Trustia_Global_Basvuru_ve_Hibe_Takip_Rehberi_2026.md` & `.pdf`: 85+ uluslararası ve ulusal başvurunun resmi takip ve durum kütüğü.
  * `01_Avrupa_Birligi_ve_EIT_Hibeleri/`: EIT Urban Mobility (100k€ hibe, Partner ID: `CUS15554`, PIC: `861711529`) ve EIC Accelerator.
  * `02_Katar_QSTP_ve_Korfez_Programlari/`: QSTP 30M$ Fon + Doha Sprint kuluçkası, Dubai RTA $1.2M yarışması, NEOM ve Hub71.
  * `03_Savunma_Sanayii_ve_Tedarikci_Portallari/`: BAYKAR Tech, ASELSAN (#0050569), SSB SAYZEK (#170), NATO DIANA.
  * `04_Z_Fellows_ve_Silikon_Vadisi/`: Z Fellows canlı mülakat rehberleri (Grace Kasten), Emergent Ventures, Silikon Vadisi fonları.
  * `05_Turkiye_Teknokent_ve_Bilisim_Vadisi/`: Bilişim Vadisi B-Stars, Teknopark İstanbul Cube Incubation, DEİK.

### 6. `06_Medya_Gorsel_ve_Tanitim_Videolari/` 🎬 (Medya, Video ve Logolar)
* **Buraya Konulacaklar:**
  * `Videolar/`: Demo ve sunum MP4 videoları.
  * `Logolar_ve_Ikonlar/`: PNG, JPG, ICO marka logoları ve simgeleri.
  * `Hyundai_Ioniq_5_Test_Araci/`: Gerçek araç ve sensör retrofit fotoğrafları.
  * `Egirisim_Basin_Kiti_2026/`: Resmi basın ve medya tanıtım kiti.

---

## ⛔ KESİN YASAKLAR VE ZORUNLULUKLAR
1. ❌ Masaüstüne (`C:\Users\Murat\Desktop`) veya proje köküne geçici bile olsa rastgele dosya BIRAKILAMAZ.
2. ❌ `Trustia/Trustia/` gibi iç içe çift klasör OLUŞTURULAMAZ.
3. ❌ Web kodları Core otonomi yazılımının içine, otonomi kodları web klasörünün içine KARIŞTIRILAMAZ.
4. ❌ Herhangi bir AI asistanı yeni bir dosya oluşturmadan önce YUKARIDAKİ 6 KATEGORİYİ KONTROL ETMEK VE TAM AİT OLDUĞU KLASÖRE YAZMAK ZORUNDADIR.

---

## 🧠 KALICI PROJE HAFIZASI VE GÜNCEL DURUM (PERMANENT CONTEXT)
* **Kurucu & Lider:** Murat Furkan Bayram (17 yaşında, Kurucu & CEO / Sistem Mimarı, %80 Hisse, TC: 59476566862, Tel: `0537 064 04 60`, E-posta: `kariyer@trustia.com.tr`, LinkedIn: `https://www.linkedin.com/in/trustia`).
* **Kurucu Ortak & Operasyon:** Doğukan Bayram (%20 Hisse, Reşit Kurucu Ortak).
* **Mühendislik Havuzu:** Denizcan Özcan (ASELSAN Aday Mühendis Havuzu & TEKNOFEST Robotaksi Finalisti, İÜC EEE 4. Sınıf, 3.44 GPA) 1. Öncelikli Donanım ve Entegrasyon Mühendisi.
* **Resmi Tescil ve Belgeler:** 
  * BTK Akademi "Türk Savunma Sanayii Ürün ve Platformları" Eğitim Katılım Sertifikası (Belge No: `L2zPtN4X1ZJ`)
  * KOSGEB İleri Girişimci Eğitimi Katılım Belgesi (`KSB01UGE0115153370`)
  * TÜBİTAK ARBİS Milli Araştırmacı Sicili (`TBTK-0229-6571`)
  * ASELSAN Tedarikçi Portalı Resmi Girişimi (Başvuru No: `0050569CCE941FD1A49FCEFB9B7BE7D6`, 05.08.2026 — Yazılım Geliştirme, Sistem Platform Entegrasyonu, Kara Platform Entegrasyonu Ön Değerlendirme Devam Ediyor)
  * 🇹🇷 **BAYKAR Teknoloji (Baykar Tech):** Resmi Alt Yüklenici / Tedarikçi Portalı (`baykartech.com/tr/contact/tedarikci-basvurusu/`) üzerinden Seviye-4 otonomi, GPS-denied 3D LiDAR SLAM, taktik yazılım ve İTO BTM tescili ile tedarikçi başvurusu eksiksiz tamamlandı (**"Teşekkürler! Bilgileriniz tarafımıza ulaşmıştır, en kısa sürede sizinle irtibat kuracağız."** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **DEİK (Dış Ekonomik İlişkiler Kurulu - deik.org.tr):** T.C. Ticaret Bakanlığı bünyesindeki ticari diplomasi çatı kuruluna Seviye-4 otonomi, GNSS-denied 3D SLAM ve İTO BTM tescili ile "Dijital Teknolojiler İş Konseyi" kapsamında resmi Ön Bilgi Talep Formu üzerinden başvuru eksiksiz tamamlandı (**"Başarıyla doldurmuş olduğunuz ön bilgi talep formu... sizlerle en yakın zamanda temasa geçeceğiz."** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇶🇦 **QSTP (Katar Bilim ve Teknoloji Parkı - Qatar Foundation, Doha):**
    * **30M$ Tech Venture Fon Başvurusu (9 Sayfa):** Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu, $500k Pre-Seed SAFE, güncel Master Pitch Deck ve YouTube robotaksi videosuyla resmi başvuru eksiksiz tamamlandı (**"Girişiminiz hakkında bize bilgi verdiğiniz için teşekkür ederiz... sonraki adımlar için sizinle iletişime geçeceğiz."** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
    * **Resmi Kuluçka & Doha Sprint Programı Başvurusu (8 Sayfa):** 4 hafta Doha yüz yüze Sprint, otel/konaklama ve ofis tahsisi, Katar şirket tescil desteği, %1.5 ertelenmiş SAFE şartları, Education City üniversiteleriyle Ar-Ge taahhüdü ve 1.301 test kanıtıyla resmi kuluçka başvurusu eksiksiz tamamlandı (**"QSTP'nin Kuluçka Programına katılmak için başvurunuz için teşekkür ederiz. Herhangi bir sorumuz olursa, ekibimizden bir üye sizinle iletişime geçecektir."** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇪🇺 **Avrupa Komisyonu (European Commission - ec.europa.eu):** Resmi Katılımcı Kayıt Defteri (Participant Register) tescili eksiksiz tamamlandı. Trustia Teknoloji adına 9 haneli resmi Avrupa Birliği Katılımcı Kimlik Kodu (**PIC Numarası: `861711529`**) üretildi ve Horizon Europe / EIT fonlama sistemine kalıcı olarak işlendi (13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇪🇺 **EIT Urban Mobility (Avrupa İnovasyon ve Teknoloji Enstitüsü - eiturbanmobility.eu):** Resmi Partner Bilgi Formu (NetSuite PIF Portal) üzerinden Trustia Teknoloji adına PIC Kodu (`861711529`), Seviye-4 otonom mobilite vizyonu, İTO BTM Fulya Kampüsü adresi, Yapı Kredi Bankası IBAN ve SWIFT (`YAPITRISXXX`) bilgileriyle resmi ortaklık tescili eksiksiz tamamlandı. Resmi Avrupa Birliği İş Ortağı ve Tedarikçi Kimlik Kodu (**Partner ID: `CUS15554`**) tahsis edildi ve EITUM İş Ortağı Portalı canlıya alındı (**"Your form has been submitted successfully!"** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇪🇺 **EIT Urban Mobility "Girişimcilere Mali Destek İçin Açık Çağrı 26-28" Resmi Hibe ve Yatırım Başvurusu:** Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu, 1.301 test, 16.000 satır kod, 100.000€ talep, İngilizce Master Pitch Deck ve resmi BTM kuruluş belgesiyle NetSuite Grant Portal üzerinden eksiksiz tamamlanarak gönderildi (Başvuru Kimliği: **`3.1.02-1206-3732.3`**, Durum: **"Gönderildi"** - 13 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * İTO BTM Fulya Kampüsü, Şişli / İstanbul 2026-II. Dönem Sözleşmeli Ön Kuluçka Girişimi
  * Startups.watch Resmi Doğrulanmış Girişim (Mobilite & Derin Teknoloji Ekosistemi)
  * 🌐 **Crunchbase Resmi Doğrulanmış Kurumsal Profil & Aktif Finansman Turu:** `crunchbase.com/organization/trustia-ai` (Isı Puanı: **85 ⬆**, CB Sırası: 534.468, 1 Eylül 2026 Aktif $500k Ön Tohumlama Turu, Kurucu Murat Furkan Bayram, egirişim basın referansı ve Şişli/İstanbul HQ ile küresel risk sermayesi radarına eksiksiz işlendi - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
* **Yazılım & Test:** 16.000 satır özgün deterministik otonomi mimarisi (Hybrid A*, 3D NDT LiDAR SLAM, Pure Pursuit), 1.301/1.301 otomatik birim ve entegrasyon testi (%100 Başarı).
* **Donanım Platformu:** Hyundai Ioniq 5 E-GMP Otonom Seviye-4 Dönüşüm Kiti (Ouster OS2-128 LiDAR, 2x Livox Mid-360, Continental Radarlar, Septentrio RTK GNSS, NVIDIA Jetson AGX Orin 64GB, Kvaser U100 CAN-FD).
* **Küresel Melek & Fon Başvuruları (Eylül 2026 - Tümü Ekran Görüntüsüyle Onaylandı):**
  * 🇺🇸 **The Bridge Residency (Entrepreneurs First - San Francisco Bay Area):** Silikon Vadisi 8 haftalık derin teknoloji kurucu rezidansı ve tohum fonuna Seviye-4 deterministik otonomi, 3D LiDAR SLAM ve 1.301 testle resmi başvuru eksiksiz tamamlandı (**"TEŞEKKÜR EDERİM - Başvurunuz alındı."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇬🇧/🇺🇸 **Entrepreneur First (EF - Londra & San Francisco - Reid Hoffman & Greylock):** Dünyanın 1 numaralı derin teknoloji ve sistem mimarı kurucu fonuna Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu ve 1.301 testle resmi başvuru tamamlandı (**"Thank you - Made with Fillout"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸 **Berkeley SkyDeck (UC Berkeley & Silikon Vadisi - $200,000 SkyDeck Fund):** Dünyanın 1 numaralı üniversite & derin teknoloji hızlandırıcısına Seviye-4 otonomi mimarisi, 16.000 satır deterministik kod, 1.301 test ve Executive One-Pager ile resmi Airtable başvuru formu üzerinden başvuru eksiksiz tamamlandı (**"Formu gönderdiğiniz için teşekkür ederiz!"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸 **Trucks Venture Capital (San Francisco - Reilly Brennan):** Dünyanın 1 numaralı otonom araç & robotaksi tohum fonu yönetici ortağı Reilly Brennan'a Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu, 1.301 test ve Executive One-Pager ile $500k Pre-Seed SAFE yatırım başvurusu doğrudan iletildi (12 Eylül 2026).
  * 🇹🇷 **Türkiye Yapay Zeka İnisiyatifi (TRAI - turkiye.ai):** Türkiye'nin resmi yapay zekâ çatı platformu ve girişim haritasına Seviye-4 otonom sürüş, 3D LiDAR SLAM ve robotaksi mimarisiyle başvuru eksiksiz tamamlandı (**"Başvurunuz alındı! En kısa sürede sizinle iletişime geçeceğiz."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Savunma Sanayii Başkanlığı (SSYZ / SAYZEK):** Cumhurbaşkanlığı Savunma Sanayii Başkanlığı Yapay Zekâ Platformu'na Seviye-4 otonomi, GNSS-denied 3D SLAM ve taktik İKA mimarisiyle resmi Simülasyon Portali ve yüksek başarımlı süper bilgisayar kaynak tahsisi başvurusu "Simport Yöneticisi" rolüyle tamamlandı (Başvuru No: `170`, Durum: **"Onay Bekliyor"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Bilişim Vadisi (B-Stars Mobilite Hızlandırma Programı):** Türkiye'nin Otonom Test Pisti ve Mobilite Hızlandırma üssüne Seviye-4 otonomi, 16.000 satır kod, 1.301 test ve Bilişim Vadisi özel Master Pitch Deck ile resmi portal üzerinden başvuru eksiksiz tamamlandı (**"B-STARS MOBİLİTE HIZLANDIRMA PROGRAMI BAŞVURUNUZ ALINMIŞTIR"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **İstanbul Kent Konseyi Gençlik Meclisi:** İstanbul'un yerel yönetim ve kent politikaları gençlik lokomotifine Seviye-4 otonomi, İTO BTM tescili ve sistem mimarı kimliğiyle resmi başvuru tamamlandı (**"Başvurunuz başarıyla kaydedildi. Teşekkür ederiz!"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🌍 **G20 Y20 (Youth 20) USA 2026 Türkiye Delegasyonu:** T.C. Dışişleri Bakanlığı himayesinde Washington D.C. zirvesine Seviye-4 otonomi, güvenilir yapay zeka ve dijital dönüşüm vizyonuyla resmi başvuru tamamlandı (12 Eylül 2026).
  * 🇹🇷 **Türkiye Siber Güvenlik Kümelenmesi (SSB & T.C. Cumhurbaşkanlığı Dijital Dönüşüm Ofisi - siberkume.org.tr):** Savunma Sanayii Başkanlığı ve Cumhurbaşkanlığı Dijital Dönüşüm Ofisi himayesindeki resmi kümelenmeye Seviye-4 otonomi, GNSS-denied 3D LiDAR SLAM, siber-fiziksel araç güvenliği (CAN-Bus / ISO 21434) ve 1.301 testle resmi Girişim Başvuru Formu üzerinden eksiksiz başvuruldu (**"Başvurunuz Alındı! Başvurunuz başarıyla alınmıştır. En kısa sürede sizinle iletişime geçecektir."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **T.C. Cumhurbaşkanlığı Yatırım ve Finans Ofisi (Invest in Türkiye - invest.gov.tr):** Cumhurbaşkanlığı Çankaya Köşkü ve Beştepe nezdindeki en üst resmi yatırım otoritesine Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, taktik İKA / robotaksi mimarisi, 1.301 test ve Executive One-Pager ile resmi stratejik yatırım ve küresel fonlama başvurusu eksiksiz tamamlandı (**"E-postanız başarıyla gönderilmiştir."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **TÜGVA (Türkiye Gençlik Vakfı - İcathane Genel Merkez):** Türkiye Gençlik Vakfı Genel Merkez İcathane teknoloji ve inovasyon programına Seviye-4 otonom sistemler, robotik ve yazılım mimarisiyle resmi başvuru tamamlandı (**"Başvurun bize ulaştı! Başvurun başarıyla alınmıştır."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **AK Parti Gençlik Kolları Genel Merkezi:** Resmi başvuru portalı (`basvuru.akparti.org.tr`) üzerinden Seviye-4 otonom sistem mimarı, İTO BTM tescili ve kurumsal profille resmi adaylık/komisyon başvurusu tamamlandı (**"Başvurunuz kaydedildi"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸 **Z Fellows ($10k Grant / San Francisco - Cory Levy & Grace Kasten):** Başvuru kabul edilerek 10 dakikalık canlı Zoom mülakatı aşamasına geçildi (Görüşmeci: Grace Kasten - Pace Capital Partner, Randevu: 17 Eylül 2026 Perşembe 19:40 TRT - Onaylandı).
  * 🇹🇷 **İTO BTM (Bilgiyi Ticarileştirme Merkezi):** Ağustos 2026 Girişim KPI Takip Formu 150M TL değerleme, 16.000 satır kod, 1.301 test, BTM Yatırımcı İlişkileri Ofisi Uzmanı Burak Gültekin görüşmesi ve Z Fellows mülakat başarısıyla eksiksiz tamamlanarak gönderildi (**"Yanıtınız kaydedildi"** - 10 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸 **LAUNCH & The Syndicate (Jason Calacanis):** $100k-$500k çek ve 14-15 Eylül canlı sunum havuzuna başvuruldu.
  * 🇦🇪 **Dubai World Challenge for Self-Driving Transport (RTA Dubai):** $1.200.000 (1.2M$) nakit ödüllü küresel Seviye-4 Robotaksi yarışmasına başvuruldu (Durum: Gönderildi / Onaylandı — Kasım 2026 Finalist İlanı, Eylül 2027 Dünya Kongresi Ödül Töreni).
  * 🇸🇦 **NEOM Investment Fund & Autonomous Mobility (Suudi Arabistan - 500 Milyar $ Mega Şehir):** Dünyanın ilk sıfır-sürücülü, sadece Seviye-4 otonom araçlara tahsisli mega şehri ve yatırım fonuna Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM ve Hyundai Ioniq 5 mimarisiyle resmi stratejik yatırım ve PoC başvurusu eksiksiz tamamlandı (**"BAŞVURUNUZ BAŞARIYLA TAMAMLANDI. İlginizi belirttiğiniz için teşekkür ederiz."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇬🇧 **Episode 1 Ventures (Londra - B2B & Derin Teknoloji VC):** Londra merkezli erken aşama derin teknoloji fonuna Seviye-4 otonomi mimarisi, 16.000 satır deterministik kod, 1.301 test, $500k Pre-Seed SAFE ve İngilizce Master Pitch Deck ile resmi portal üzerinden başvuru eksiksiz tamamlandı (**"Girişim başvurunuz için teşekkür ederiz. Başvurunuzu en kısa sürede inceleyeceğiz."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸/🇫🇷 **Starburst Aerospace (Los Angeles & Paris - Küresel Havacılık ve Savunma Hızlandırıcısı):** NASA, Boeing, Lockheed Martin ve Thales destekli dünyanın 1 numaralı havacılık/savunma hızlandırıcısına Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu ve 1.301 testle resmi başvuru tamamlandı (**"BİZİMLE İLETİŞİME GEÇTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ! SİZİN MESAJ BAŞARIYLA GÖNDERİLDİ."** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇬🇧 **Ascension (Londra - Pre-Seed / Seed Derin Teknoloji & Mobilite VC):** Londra merkezli erken aşama otonomi ve mobilite fonuna Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu, 1.301 test ve Master Pitch Deck ile resmi portal üzerinden başvuru eksiksiz tamamlandı (**"Bu formu gönderdiğiniz için teşekkür ederiz - en kısa sürede sizinle iletişime geçmeyi hedefliyoruz!"** - 12 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇬🇧 **24Haymarket (Mayfair, Londra - Özel Aile Ofisi ve Melek Yatırımcı Sendikası):** Londra'nın en köklü özel yatırım ağına Seviye-4 otonomi mimarisi, 1.301 test, $500k Pre-Seed SAFE ve Ioniq 5 dönüşüm kitiyle resmi finansman başvurusu eksiksiz tamamlandı (12 Eylül 2026).
  * 🇺🇸 **Launchpad 2026 (1752 Ventures / Santa Monica):** $100,000 nakit yatırım sanal programına başvuruldu.
  * 🇺🇸 **Bronze Valley VC & Angel Fund (Gust):** $500k Pre-Seed SAFE ($5M Cap, %20 İndirim) şartlarıyla başvuruldu.
  * 🇺🇸 **Future Mindset (Gelecek Odaklı Zihniyet Fonu - Gust):** Vizyon başvurusu gönderildi.
  * 🇺🇸 **Hustle Fund (Silikon Vadisi):** Çok adımlı form üzerinden eksiksiz başvuruldu.
  * 🇺🇸 **Boost VC ($500k Pre-Seed / Adam Draper):** $500,000 nakit yatırım ve San Mateo robotik hızlandırma başvurusu İngilizce Master Pitch Deck ve Hyundai Ioniq 5 İngilizce Fotoğraflı Master Plan ile eksiksiz tamamlandı (2 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇺🇸 **Founders, Inc. (f.inc - San Francisco Fort Mason Blueprint II):** Hesap açıldı, giriş yapıldı.
  * 🇹🇷 **TechOne VC (Smart Capital Deep Tech):** 28 adımlı başvuru onaylandı.
  * 🇹🇷 **Revo Capital ($100M VC Fonu):** Başvuruldu.
  * 🇹🇷 **APY Ventures (Bilişim Vadisi GSYF):** Mobilite, otonomi ve derin teknoloji odağında resmi portal üzerinden 500k$ taleple eksiksiz tamamlandı (**"Formunuz başarıyla gönderildi"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **J-Start (Derin Teknoloji Fonu):** TRL-6 Hyundai Ioniq 5 mimarisi, 15M TL bütçe talebi ve 1.301 testle resmi Airtable portalı üzerinden başvuru eksiksiz tamamlandı (**"Başvurunuz alınmıştır"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Teknoloji ve İnovasyon Fonu (TKYB / Kalkınma Girişim Sermayesi):** Sanayi ve Teknoloji Bakanlığı & TKYB resmi fonuna Seviye-4 otonomi ve Master Pitch Deck ile başvuru eksiksiz tamamlandı (**"Başvuru formu başarıyla değerlendirmeye gönderildi"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **OİBventure (Uludağ Otomotiv İhracatçıları Birliği - Mobilite İnovasyon Programı):** Türkiye'nin otomotiv sanayii çatı birliğine Seviye-4 otonom robotaksi dönüşüm kiti ve Master Pitch Deck ile resmi portal üzerinden başvuru eksiksiz tamamlandı (9 Eylül 2026).
  * 🇹🇷 **Finberg (Fiba Grubu VC):** Başvuruldu.
  * 🇹🇷 **Inveo Ventures:** Başvuruldu.
  * 🇹🇷 **Boğaziçi Ventures:** Başvuruldu.
  * 🇳🇱/🇬🇧 **DOMiNO Ventures (Amsterdam/Londra):** Başvuruldu.
  * 🇹🇷 **Türk Telekom Ventures (PİLOT 14. Dönem):** Başvuruldu.
  * 🇹🇷 **İş Girişim Sermayesi (İş Bankası GSYO - BIST: ISGSY):** 10M-20M TL ($500k) yatırımlık başvuru ve Hyundai Ioniq 5 Seviye-4 Fotoğraflı Master Planı ile eksiksiz tamamlandı (2 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Maxis Girişim Sermayesi (İş Bankası GSYF):** Başvuruldu.
  * 🇹🇷 **ŞirketOrtağım Melek Yatırım Ağı:** Başvuruldu.
  * 🇹🇷 **Martı Technologies (NYSE: MRT / Oğuz Alper Öktem):** Martı TAG "Türkiye Otonom Araç İttifakı" kapsamında Seviye-4 Robotaksi pilotu teklifi ve Executive One-Pager ile doğrudan LinkedIn InMail üzerinden ulaşıldı (2 Eylül 2026).
  * 🇹🇷 **Dijitalpark Teknokent (Çekmeköy / Türk-Alman Üniv.):** Ön Kuluçka başvurusu (Otomotiv Tasarımı ve Mühendislik / Seviye-4 Otonom Dönüşüm Kiti) eksiksiz tamamlandı (2 Eylül 2026), Kuluçka Uzmanı Yiğit Şener doğrudan ulaştı (3 Eylül 2026).
  * 📰 **egirişim (Hilmi Öğütcü):** Özel manşet haberi ve medya tanıtımı başvurusu 9 parçalık resmi basın kiti (HD logolar, Ioniq 5 test aracı fotoğrafları, 30 Ağustos ve İstanbul robotaksi demo videoları, kurucu profili) ile eksiksiz gönderildi (3 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 📰 **Webrazzi:** Resmi Girişim İnceleme Formu üzerinden Seviye-4 otonomi, 1.301 test ve Hyundai Ioniq 5 robotaksi mimarisiyle haber başvurusu tamamlandı (**"Cevaplarınız başarıyla kaydedildi"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🏆 **Webrazzi Arena 2026 (Webrazzi Summit - Wyndham Grand Levent):** 21 Ekim 2026 canlı sahne sunumu ve yatırımcı yarışması başvurusu Seviye-4 otonomi, Hyundai Ioniq 5 mimarisi ve Master Pitch Deck ile resmi portal üzerinden eksiksiz tamamlandı (**"Başvurunuz başarıyla alınmıştır!"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **fonbulucu (SPK Paya Dayalı Kitle Fonlama - Kampanya Kodu: W1MV5K):** 15.000.000 TL hedef (18M TL fonlama tavanı, 150M TL değerleme, %10 pay) ile Seviye-4 Robotaksi kampanyası 12 sekme, TRL-6 Hyundai Ioniq 5 mimarisi, 3 yıllık nakit akışı ve YouTube tanıtım videosuyla eksiksiz tamamlanarak resmi olarak **Ön İncelemeye Sunuldu** (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Ford Otosan / Driventure (Kurumsal Girişim Sermayesi & İnovasyon):** Seviye-4 elektrikli ticari otonomi ve fabrika içi hat besleme / çekici otonomlaştırma PoC başvurusu web portalı üzerinden eksiksiz tamamlandı ve gönderildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **FNSS Savunma Sistemleri (Birim Müdürü Dr. Raşit Karakuş Referanslı):** Web iletişim portalı ve `supplychain@fnss.com.tr` tedarikçi masası üzerinden taktik İKA (Gölge Süvari), GPS-denied 3D SLAM ve yerli otonomi yazılımı aday tedarikçi başvurusu One-Pager ve resmi tescil belgeleri eklenerek eksiksiz tamamlandı ve gönderildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Karsan Otomotiv (Ar-Ge Direktörü Barış Hulisioğlu):** Otonom e-ATAK / e-JEST vizyonuna yönelik Seviye-4 otonomi yazılım mimarisi, GNSS-denied 3D LiDAR SLAM ve PoC iş birliği başvurusu resmi kurumsal portal ve LinkedIn InMail üzerinden Ar-Ge Direktörü Barış Hulisioğlu'na doğrudan iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **BMC Otomotiv & Savunma Sanayii:** Kirpi, Vuran, Altuğ taktik tekerlekli/paletli zırhlı araçlar ve ticari çekici ailesine yönelik yerli Seviye-4 otonomi, GNSS-denied 3D SLAM ve taktik konvoy yazılımı başvurusu resmi portal (`bmc.com.tr/mesaj-iletildi`) ve `info@bmc.com.tr` üzerinden Savunma Sanayi ve Ar-Ge Direktörlüğü'ne iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Nurol Makina ve Sanayi A.Ş. (Ejder Yalçın & Yörük 4x4):** Taktik tekerlekli zırhlı araç ailesine yönelik Seviye-4 otonom konvoy (platooning), GNSS-denied 3D LiDAR SLAM ve EYP tespit yazılımı entegrasyonu PoC teklifi resmi başvuru ve One-Pager ile Genel Müdürlük ve İş Geliştirme/Pazarlama (`marketing@nurolmakina.com.tr`, `info@nurolmakina.com.tr`) masasına doğrudan iletildi (12 Eylül 2026).
  * 🇹🇷 **MTA (Maden Tetkik ve Arama Genel Müdürlüğü):** Yeraltı maden ocakları ve tünellerde GPS'siz (GNSS-Denied) 3D LiDAR SLAM, otonom maden nakliyesi ve keşif robotu teknolojisi iş birliği teklifi resmi başvuru ve One-Pager ile Genel Müdürlük ve İstanbul İrtibat (`mta@mta.gov.tr`, `istanbul@mta.gov.tr`) masasına doğrudan iletildi (12 Eylül 2026).
  * 🇹🇷 **Borusan Ventures (Borusan Holding CVC - Lojistik & Mobilite):** Tohum öncesi yatırım, Borusan Port konteyner sahası ve Borusan Lojistik depo içi otonom aktarma PoC başvurusu resmi portal üzerinden eksiksiz tamamlandı ve gönderildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Netlog Lojistik (Türkiye Entegre Lojistik & Depo Devi):** Kapalı mega depolar için GNSS-denied 3D LiDAR SLAM, akülü çekici ve AGV/forklift otonom aktarma pilot test (PoC) teklifi resmi kurumsal portal üzerinden iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Ekol Lojistik (Lotus Mega Tesis & Ar-Ge Merkezi):** Depo içi akülü çekici, AGV/forklift otonomizasyonu ve GNSS-denied 3D SLAM pilot test (PoC) teklifi resmi portal üzerinden Ar-Ge Merkezi ve İnovasyon Direktörlüğü'ne iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **YILPORT Holding (Gebze Konteyner Terminali):** Rıhtım-istif arası otonom terminal çekicisi (yard tractor), GNSS-denied 3D LiDAR SLAM pilot test (PoC) teklifi resmi portal üzerinden iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Mersin Uluslararası Limanı (MIP - PSA Group):** Türkiye'nin en büyük konteyner limanı için rıhtım vinçleri ve saha otomasyonu otonom aktarma çekicisi (PoC) başvurusu web portalı ve `mip-cc@globalpsa.com` üzerinden iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Asyaport Liman A.Ş. (MSC Transit Hub):** Türkiye'nin ilk ve en büyük transit konteyner limanında rıhtım-istif arası otonom terminal çekicisi (yard truck) PoC başvurusu resmi web portalı (`Form iletildi`) ve `operation@asyaport.com` / `planning@asyaport.com` üzerinden iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Marport Liman İşletmeleri (Arkas Holding & TIL / Ambarlı Limanı - İstanbul):** Marmara'nın en büyük konteyner limanı için rıhtım-istif arası otonom terminal çekicisi, GNSS-denied 3D LiDAR SLAM PoC başvurusu resmi kurumsal portal üzerinden iletildi (8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Vestel Ventures (Zorlu Holding CVC):** Vestel City mega üretim kampüsü iç lojistik/AGV otonomizasyonu ve CVC yatırım başvurusu Pitch Deck & One-Pager ile `info@vestelventures.com` üzerinden resmi olarak iletildi (8 Eylül 2026).
  * 🇹🇷 **Diffusion Capital Partners (DCP - Türkiye Deep Tech & Robotik Fonu):** 500.000 € tohum öncesi yatırım için 16.000 satır deterministik otonomi, GNSS-denied SLAM, 1.301 test ve Hyundai Ioniq 5 mimarisiyle `contact@dcp.vc` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **ScaleX Ventures (Developer-First & Deep Tech VC):** $500k-$2M tohum öncesi yatırım için 16k satır deterministik kod, 1.301 test ve Seviye-4 otonomi mimarisiyle `contact@scalexventures.com` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **Galata Business Angels (GBA - Türkiye Melek Yatırım Ağı):** Tohum öncesi melek turu, Seviye-4 otonomi, BTM ve KOSGEB tescilleriyle `info@galatabusinessangels.com` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **212 VC (212.vc - B2B & Deep Tech Global VC):** $500k-$3M tohum öncesi yatırım için resmi 3 adımlı dealflow portalı üzerinden One-Pager ve Pitch Deck yüklenerek resmi başvuru tamamlandı (**"Yanıtınız kaydedildi"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Logo Ventures (Logo Yazılım CVC - B2B & Mobilite):** $250k-$1.5M tohum öncesi yatırım için deterministik otonomi, endüstriyel depo SLAM ve B2B kurumsal mimariyle `contact@logoventures.com.tr` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **Collective Spark (Erken Aşama Teknoloji VC):** $500k-$2M tohum öncesi yatırım için derin teknoloji, GNSS-denied SLAM ve Seviye-4 yazılım mimarisiyle `contact@collectivespark.com` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **Keiretsu Forum Türkiye (Küresel Melek Yatırım Ağı):** Tohum öncesi melek turu, Seviye-4 otonomi, BTM tescili ve BTK Akademi sertifikasıyla `info@keiretsuforum.com.tr` masasına resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **Alesta Yatırım (Escort Teknoloji CVC - BIST: ESCOM):** Resmi portal (`alestayatirim.com/basvuru?basarili=1`) üzerinden deterministik otonomi, 1.301 test ve Pitch Deck yüklenerek resmi başvuru tamamlandı (**"Başvurunuz alındı"** - 8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Bulls Girişim Sermayesi (Bulls GSYO - BIST: BVGYO):** Tohum öncesi yatırım için resmi web portalı (`bullsgirisim.com/tr/proje-basvurusu`) üzerinden One-Pager ve Seviye-4 otonomi mimarisiyle resmi başvuru tamamlandı (8 Eylül 2026).
  * 🇹🇷 **Hedef Girişim Sermayesi (Hedef GSYO - BIST: HDFGS):** 15.000.000 TL tohum öncesi finansman, Seviye-4 otonomi, 1.301 test ve One-Pager ile resmi portal üzerinden başvuru yapıldı (**"Başvurunuz başarıyla iletildi"** - 8 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Pardus Girişim Sermayesi (Pardus GSYO - BIST: PRDGS):** BIST halka açık GSYO resmi proje portalı üzerinden deterministik otonomi, 1.301 test ve Pitch Deck yüklenerek resmi başvuru tamamlandı (**"Gönderildi, teşekkürler!"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **İstinye Garage Incubation Hub (İstinye Üniversitesi Kuluçka Merkezi):** Genel başvuru kapsamında Seviye-4 otonomi, eMobilite/lojistik, 15m² ofis talebi ve One-Pager ile resmi portal üzerinden başvuru tamamlandı (**"Teşekkürler! Form yanıtınız alındı"** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **İnci Radar & Vinci Venture Capital (İnci Holding CVC - Mobilite & Lojistik):** Mobilite-Otomotiv, endüstriyel lojistik ve fabrika/depo içi Seviye-4 otonomi, 1.301 test ve Master Pitch Deck ile resmi portal (`inciradar.com/tr/basvuru-formu/`) üzerinden resmi başvuru tamamlandı (**"Mesajınız için teşekkürler. Gönderildi."** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **TEB Girişim Bankacılığı (Start Up Kuluçka Programı):** BNP Paribas & TEB ortaklığı Start Up Programına Seviye-4 otonomi, 1.301 test, BTM Fulya tescili ve TRL-6 Ioniq 5 mimarisiyle resmi portal (`teblegirisim.com/kulucka-merkezi/Start-Up/7`) üzerinden başvuru eksiksiz tamamlandı (**"Teşekkürler. Başvurunuz ilgili birimlere iletilmiştir."** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🇹🇷 **Workup Girişimcilik Programı (Türkiye İş Bankası & Hackquarters):** Pre-seed aşamasında, Mobilite Lojistik ve Akıllı Şehirler dikeyinde 10 MB Master Pitch Deck yüklenerek resmi başvuru tamamlandı (**"Teşekkür ederiz! Bilgileriniz alınmıştır. Hızlandırma programına kabul edilmeniz halinde, bir sonraki adımlar için Workup ekibi sizinle iletişime geçecektir."** - 9 Eylül 2026 - Ekran Görüntüsüyle Onaylandı).
  * 🌍 **Önceki Başvurular:** Bilkent Cyberpark GDP, Z Fellows ($10k), Workup İş Bankası, Emergent Ventures ($100k), NATO NIF (€1B), Fark Labs, Sabancı SUCool, TİM-TEB, Shield Capital, Starburst, Seedcamp, a16z Speedrun, Thiel Fellowship ($250k), Soma Fellows ($100k-$2M), Techstars, Y Combinator (Kış 2027).
* **BTM Randevusu:** 4 Eylül 2026 Cuma 15:00 - 15:30 (İTO BTM Fulya Kampüsü, Yatırımcı İlişkileri Ofisi Birebir Danışmanlık - Murat & Abisi).
* **Fuar:** TURKCOMPOSITE 2026 / BTM Startup Village Fuarı (21-23 Ekim 2026) başvurusu tamamlandı.
* **Masaüstü Dosyası:** `C:\Users\Murat\Desktop\Çıktı` altında 10 adet 2 Eylül 2026 güncel, kurumsal A4 PDF dosyası (Hyundai Ioniq 5 Fotoğraflı Master Plan, Master Pitch Deck, One-Pager, Finansal Model, BMC, CV'ler) hazır.

