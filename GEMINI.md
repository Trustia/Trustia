# TRUSTIA PROJESİ ZORUNLU ÇALIŞMA VE DOSYA YERLEŞİM KURALLARI (MANDATORY PROJECT RULES)

> [!IMPORTANT]
> Bu kural seti, bu projede çalışacak **TÜM YAPAY ZEKA ASİSTANLARI VE AJANLAR İÇİN ZORUNLUDUR**.
> Masaüstüne veya proje kök dizinine rastgele, baştan savma dosya oluşturulamaz veya atılamaz.
> Üretilen her dosya, kod, görsel, video, PDF veya sertifika AMACINA GÖRE AŞAĞIDAKİ 3 ANA KLASÖRDEN İLGİLİSİNE YERLEŞTİRİLMEK ZORUNDADIR.

---

## 🚨 EN TEMEL VE ZORUNLU 8 ALTIN KURAL (THE 8 SUPREME DIRECTIVES)

### 1. KURAL: BÜTÜN REPO VE 3 ANA ALANDA ANINDA EKSİKSİZ GÜNCELLEME VE CANLIYA DEPLOY (TOTAL REPOSITORY SYNCHRONIZATION & ZERO OUTDATED FILE DIRECTIVE)
> [!CRITICAL]
> Projede yeni bir gelişme olduğu, yeni bir resmi onay/başvuru/tescil/kod/özellik yapıldığı veya herhangi bir kurumsal bilgi güncellendiği anda; **SADECE WEB SİTESİ VEYA TEK BİR DOSYA DEĞİL, TRUSTIA PROJE ÇATISI ALTINDAKİ 3 ANA KLASÖRÜN HEPSİ VE İÇLERİNDEKİ İSTİSNASIZ BÜTÜN DOSYALAR EŞZAMANLI VE EKSİKSİZ GÜNCELLENECEK VE DERHAL GITHUB'A PUSH EDİLİP CANLIYA (`trustia.com.tr`) DEPLOY EDİLECEKTİR.**
> * **Repo Çapında İstisnasız Güncellenmesi Zorunlu 3 Ana Alan ve Dosya Kapsamı:**
>   1. **`01_Trustia_Otonom_Yazilim_Core/` (Otonomi Motoru & Teknik Kütükler):** `trustia_cli.py` konsol çıktıları, `docs/` altındaki tüm teknik analizler, `docs/reports/` altındaki tedarikçi başvuru paketleri (`TEDARIKCI_BASVURU_PAKETI.md`, `SERTIFIKASYON_RAPORU_ASAMA6.md`), lisans ve uygunluk kütükleri.
>   2. **`02_Trustia_Web_Platformu/` (Canlı Web Platformu & Arama Motorları):** `website/` altındaki Ana Sayfa, Hakkımızda, Robotaxi, İletişim, `InstitutionalAccreditations.tsx`, Footer, Navbar, Schema.org JSON-LD kurumsal grafiği, OpenGraph/Twitter Cards meta etiketleri, `sitemap.xml` (güncel `lastmod` tarihi) ve `robots.txt`.
>   3. **`Kurumsal/` (Birleşik Kurumsal Varlıklar - 4 Temiz Alt Klasör):**
>      * `Belgeler/`: Devlet/kurum onay belgeleri, portal erişim kodları, SAP kullanıcı bilgileri (`Aselsan_Tedarikci_Kodlari.txt`) ve resmi tescil kütükleri.
>      * `Sunumlar/`: Master Pitch Decks (TR/EN), Executive One-Pager (MD/PDF), B-Stars, Workup, Revo, Finberg, Inveo, NATO NIF sunumları, Cap Table (`.csv`), Finansal Model ve Ioniq 5 Seviye-4 Fotoğraflı Master Plan.
>      * `Basvurular/`: `Takip_Rehberi_2026.md` ve ikiz resmi `.pdf` çıktısı, ASELSAN Axcelerate ZIP başvuru paketi, Malta Enterprise, NATO DIANA ve Z Fellows mülakat rehberleri.
>      * `Medya/`: Kurumsal logolar, HD banner'lar, Ioniq 5 test aracı fotoğrafları, demo/zafer bayramı/master videolar ve basın bülteni.
>   4. **Kök Dizin Yönetim Belgeleri:** `README.md`, `AGENTS.md`, `GEMINI.md`, `.agents/rules/folder_structure_rules.md`.
> * **Sıfır Eskimiş Dosya Toleransı (Zero Outdated File Policy):** Repodaki herhangi bir dosyanın veya sunumun güncel olmayan eski bir statüde (örneğin onaylanmış bir süreç için "ön değerlendirmede" veya davet alınmış bir kurum için "başvuru yapıldı" şeklinde) bırakılması kesinlikle yasaktır!
> * **Anında Canlıya Dağıtım Şartı:** Tüm güncellemeler yapıldıktan sonra yerel bilgisayarda ASLA bekletilemez; anında `git add -A`, kurumsal commit ve `git push origin main` yapılarak GitHub Actions üzerinden `trustia.com.tr` canlı ortamına ve Google indeksine fırlatılacaktır!

### 2. KURAL: ÇİFT DİLLİ KÜRESEL EŞİTLİK (BILINGUAL TR/EN PARITY)
> [!CRITICAL]
> Web sitesine veya dokümantasyona yeni bir özellik, başvuru veya metin eklendiğinde **hem Türkçe hem de İngilizce versiyonu eşzamanlı ve eksiksiz üretilmek zorundadır.**
> * Silikon Vadisi (Z Fellows), Avrupa Birliği (EIT Urban Mobility) ve Katar (QSTP) İngilizce dokümanları; ASELSAN, BAYKAR ve KOSGEB Türkçe dokümanları inceler.
> * İki dil arasında asla bilgi kopukluğu veya gecikme olamaz; web sitesindeki dil değiştirici (`TR`/`EN`) her sayfada tam kurumsal karşılığı sunmalıdır.

### 3. KURAL: MD & PDF OTOMATİK İKİZLEME VE SENKRONİZASYON (MARKDOWN & PDF TWIN SYNCHRONIZATION)
> [!CRITICAL]
> `Kurumsal/Sunumlar/` ve `Kurumsal/Basvurular/` altındaki herhangi bir `.md` (Markdown) sunumu, iş planı, teknik şartname veya takip kütüğü güncellendiğinde; **onun resmi kurumsal PDF versiyonu da derhal güncellenmek zorundadır.**
> * Bir yatırımcıya, jüriye veya devlet kurumuna sunulacak resmi PDF dosyasının Markdown'daki en son bilgilerden geri kalması kesinlikle yasaktır.
> * Web sitesinden indirilen PDF'ler (`public/*.pdf`) ile `Kurumsal/` altındaki PDF'ler daima %100 senkronize tutulacaktır.

### 4. KURAL: SADECE KANITLI VE TESCİLLİ BİLGİ İLKESİ (PROOF-ONLY & VERIFIED FACTS)
> [!CRITICAL]
> Proje dosyalarına, web sitesine, sunumlara veya teknik belgelere **asla tahmini, uydurma veya doğrulanmamış bilgi yazılamaz.**
> * Yazılan her kurumsal bilginin arkasında doğrulanmış resmi bir numara (Örn: ASELSAN `#0050569`, AB PIC `#861711529`, EIT Partner `#CUS15554`, EIT Hibe `#3.1.02-1206-3732.3`, fonbulucu `#W1MV5K`, SSB SAYZEK `#170`, BTK `#L2zPtN4X1ZJ`, KOSGEB `#KSB01UGE0115153370`) veya somut bir test kanıtı (1.301 test, 16.000 satır deterministik kod) olmak zorundadır.

### 5. KURAL: DAĞINIK VE KOPYA İSİMLENDİRME YASAĞI (CLEAN SLATE & PROFESSIONAL NAMING)
> [!CRITICAL]
> Klasörlerde `sunum_yeni.pdf`, `kopya_kopya.md`, `final_son_gercek.pdf`, `test2.png` gibi gayriciddi, dağınık veya çift isimli dosyalar **oluşturulamaz ve barındırılamaz.**
> * Her belgenin ve varlığın tek bir resmi "Master" adı olur; güncellemeler doğrudan o ana dosyanın üzerine yapılır ve versiyonlama Git geçmişine bırakılır.
> * Masaüstünde veya klasör içlerinde geçici deneme dosyası bırakılamaz.

### 6. KURAL: KIRILMAZ GÜVENLİK VE ASIL-D FAILSAFE KİLİDİ (AUTOMOTIVE SAFETY & FAILSAFE KERNEL)
> [!CRITICAL]
> Otonomi yazılımındaki (`01_Trustia_Otonom_Yazilim_Core`) **5ms anlık sürücü müdahalesi (override), 200ms donanım watchdog mekanizması ve E-Stop acil durum fren kesicisi** ASLA koddan çıkarılamaz, bypass edilemez veya gevşetilemez.
> * Gerçek Hyundai Ioniq 5 test aracında ve sahada can güvenliği, ISO 26262 ASIL-D ve STANAG 4586 askeri güvenlik standartları tavizsiz korunur.

### 7. KURAL: KURUMSAL YÖNETİŞİM VE CAP TABLE STANDARDI (EXECUTIVE GOVERNANCE & CAP TABLE PARITY)
> [!CRITICAL]
> Bütün dosyalarda, web sitesinde, yatırımcı sunumlarında ve resmi yazışmalarda kurucu heyet unvan ve ortaklık oranları tek ve tutarlı olmak zorundadır:
> * **Murat Furkan Bayram:** Kurucu & CEO / Sistem Mimarı (%80 Hisse).
> * **Doğukan Bayram:** Kurucu Ortak & Operasyon Direktörü (%20 Hisse, Reşit Kurucu Ortak).
> * **Denizcan Özcan:** Baş Donanım ve Entegrasyon Mühendisi (ASELSAN Aday Havuzu & TEKNOFEST Finalisti).
> * Hiçbir belgede yetkisiz unvan değişikliği veya hisse tutarsızlığı yapılamaz.

### 8. KURAL: SIFIR SÜRTÜNME VE TEK TIKLA DEMO ÇALIŞTIRMA (ONE-CLICK ZERO-FRICTION DEMO LAUNCHER)
> [!CRITICAL]
> Otonomi çekirdeğine eklenen her yeni algoritma, tehdit tespit modeli veya simülasyon aracı; karmaşık terminal parametrelerine ihtiyaç duymadan `01_Trustia_Otonom_Yazilim_Core` altındaki `TRUSTIA_BASLAT.bat` menüsünden (`1`, `2`, `3`, `4`) veya `trustia_cli.py` üzerinden **tek tıkla çalıştırılabilir ve anında canlı demo yapılabilir olmak zorundadır.**

---

## 📁 3 ANA MİMARİ ALAN VE SADELEŞTİRİLMİŞ KURUMSAL DÜZEN

Tüm dosyalar `C:\Users\Murat\Desktop\Trustia\` ana çatısı altında aşağıdaki 3 klasörde tutulur:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Asıl Otonomi Yazılımı & Testler)
* **Buraya Konulacaklar:** Otonomi motoru, SLAM haritalama (3D NDT / ICP), Hybrid A* rota planlama, Pure Pursuit ve Stanley kontrolcüler, yapay zeka EYP/Mayın/KHKN tespit modelleri, CAN-Bus/ROS2/JAUS/Webots sürücüleri, 1.301 birim/entegrasyon testi, CLI scriptleri ve Taktik C2 Masaüstü Konsolu (GUI).
* **Kural:** Otonomi yazılımıyla ilgili tüm Python/C++ kodları ve testleri SADECE bu klasör altında oluşturulur veya düzenlenir. 1.301 testin %100 başarı oranı asla bozulamaz.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Sitesi ve Platform Kodları)
* **Buraya Konulacaklar:** Canlı web sitesi kaynak kodları (Next.js 16, React 19, Tailwind CSS 4, Three.js 3D modeller, web sayfaları, kurumsal akreditasyon bileşenleri, Schema.org JSON-LD, sitemap.xml ve robots.txt).
* **Kural:** Web arayüzü ile ilgili her şey SADECE bu klasör altında `website/` içinde geliştirilir. Canlı yayın [trustia.com.tr](https://trustia.com.tr) adresine GitHub Actions CI/CD üzerinden otomatik derlenir ve dağıtılır.

### 3. `Kurumsal/` 🏢 (Birleşik Kurumsal Varlıklar, Sunumlar ve Medya)
Gereksiz kopyalardan ve şişkinlikten arındırılmış, 4 net amaca ayrılmış tek çatı klasör:
* **`Belgeler/` 📜 (Resmi Devlet Belgeleri & Tesciller):**
  * KOSGEB İleri Girişimci katılım belgesi (`KSB01UGE0115153370`)
  * BTK ve SSB Savunma Sanayii sertifikası (`L2zPtN4X1ZJ`)
  * İTO BTM İmzalı Ön Kuluçka Sözleşmesi ve Resmi Kuruluş Tescil Belgesi
  * OIN (Open Invention Network) Patent Savunma Paktı Lisans Sözleşmesi
  * ASELSAN SAP erişim kodları (`Aselsan_Tedarikci_Kodlari.txt`) ve NATO NCAGE tescil kaydı
  * Kurucu resmi kimlik, ikametgah ve adli sicil belgeleri
* **`Sunumlar/` 💼 (Yatırımcı Dosyaları, Finans & Master Planlar):**
  * `Master_Pitch_Deck_TR.pdf` & `Master_Pitch_Deck_EN.pdf` (.md kaynaklı)
  * `Executive_One_Pager_EN.pdf` (.md kaynaklı)
  * `Ioniq5_Fotografli_Master_Plan_TR.pdf` & `Ioniq5_Photo_Master_Plan_EN.pdf` (Tek Master Kopya)
  * Hedef Fon Sunumları: NATO NIF, Revo Capital, Workup, Inveo, Finberg, Bilişim Vadisi, Dubai Challenge
  * `Cap_Table.csv` & `Finansal_Model_ve_Cap_Table.pdf`
  * `Robotaksi_Operasyon_Modeli.md` & ikiz `.pdf`
  * `Organizasyon_Yapisi.pdf` & `Murat_Furkan_Bayram_CV.pdf`
* **`Basvurular/` 🌍 (Takip Kütüğü ve Kritik Başvuru Paketleri):**
  * `Takip_Rehberi_2026.md` & `Takip_Rehberi_2026.pdf` (88+ başvuru takip kütüğü)
  * `ASELSAN_Axcelerate_Basvuru_Paketi.zip` (Resmi teslim edilmiş paket)
  * `Malta_Enterprise_Application_Dossier.md` & `.pdf` (€1.5M hibe)
  * `NATO_DIANA_Application_Dossier.md` & `.pdf`
  * `Z_Fellows_Interview_Master_Guide.md` & `Emergent_Ventures_Proposal.docx`
  * `Singapur_GIA_Basvuru_Onayi.png`
* **`Medya/` 🎬 (Logolar, Araç Fotoğrafları, Tanıtım Videoları):**
  * Resmi HD logolar ve kurumsal banner'lar
  * Crunchbase doğrulanmış profil ve trend grafikleri
  * Hyundai Ioniq 5 Seviye-4 gerçek retrofit fotoğrafları (`Ioniq5_Foto_1..7.png`, `Ioniq5_On_Capraz.png`, `Ioniq5_Tavan_LiDAR.png`)
  * `Robotaksi_Demo.mp4`, `Zafer_Bayrami.mp4`, `Master_Edit.mp4` (Tekil master videolar)
  * `Basin_Bulteni_ASELSAN.pdf`

---

## ⛔ KESİN YASAKLAR VE ZORUNLULUKLAR
1. 🚨 **1. ZORUNLU KURAL (ANINDA HER YERDEN GÜNCELLEME VE CANLIYA DEPLOY):** Projede herhangi bir şey yapıldığı/oluştuğu anda o bilgi A'dan Z'ye BÜTÜN dosyalardan, web sitesinden, SEO'dan, dokümanlardan güncellenmek ve BEKLEMEDEN GitHub'a push edilip canlıya deploy edilmek ZORUNDADIR. Hiçbir güncelleme yerelde asılı bırakılamaz.
2. 🚨 **2. ZORUNLU KURAL (ÇİFT DİLLİ EŞİTLİK):** Web ve dokümantasyon daima TR ve EN olarak eşzamanlı güncellenir.
3. 🚨 **3. ZORUNLU KURAL (MD & PDF İKİZLEME):** Güncellenen her Markdown dokümanının PDF çıktısı anında güncellenir.
4. 🚨 **4. ZORUNLU KURAL (KANITLI BİLGİ):** Resmi tescil veya test kanıtı olmayan hiçbir veri dosyalara yazılamaz.
5. 🚨 **5. ZORUNLU KURAL (TEMİZ İSİMLENDİRME VE SIFIR KOPYA):** "kopya", "yeni", "final_son", "test_*" gibi dosya isimleri yasaktır; sadece tekil Master isim kullanılır. Aynı dosyanın farklı klasörlerde mükerrer kopyalanması kesinlikle yasaktır!
6. 🚨 **6. ZORUNLU KURAL (ASIL-D GÜVENLİK KİLİDİ):** 5ms sürücü override ve 200ms watchdog asla bypass edilemez.
7. 🚨 **7. ZORUNLU KURAL (KURUMSAL YÖNETİŞİM):** Murat Furkan Bayram (%80 CEO), Doğukan Bayram (%20 Operasyon), Denizcan Özcan (Baş Donanım Mühendisi) unvan ve oranları daima korunur.
8. 🚨 **8. ZORUNLU KURAL (TEK TIKLA ÇALIŞTIRMA):** Tüm otonomi bileşenleri `TRUSTIA_BASLAT.bat` ve `trustia_cli.py` üzerinden tek tıkla çalışmak zorundadır.
9. ❌ Masaüstüne (`C:\Users\Murat\Desktop`) veya proje köküne geçici bile olsa rastgele dosya BIRAKILAMAZ.
10. ❌ `Trustia/Trustia/` gibi iç içe çift klasör OLUŞTURULAMAZ.
11. ❌ Web kodları Core otonomi yazılımının içine, otonomi kodları web klasörünün içine KARIŞTIRILAMAZ.
12. ❌ Herhangi bir AI asistanı yeni bir dosya oluşturmadan önce YUKARIDAKİ 3 ANA KLASÖRÜ KONTROL ETMEK VE TAM AİT OLDUĞU KLASÖRE YAZMAK ZORUNDADIR.
13. ❌ Tasarım ve içerikte çocukça, gayriciddi veya şablon görüntüler kullanılamaz; daima uluslararası kurumsal savunma ve otonomi standardı korunacaktır.

---

## 🧠 KALICI PROJE HAFIZASI VE GÜNCEL DURUM (PERMANENT CONTEXT)
* **Kurucu & Lider:** Murat Furkan Bayram (17 yaşında, Kurucu & CEO / Sistem Mimarı, %80 Hisse, TC: `59476566862`, Tel: `0537 064 04 60`, E-posta: `kariyer@trustia.com.tr`, LinkedIn: `https://www.linkedin.com/in/trustia`).
* **Kurucu Ortak & Operasyon:** Doğukan Bayram (%20 Hisse, Reşit Kurucu Ortak).
* **Mühendislik Havuzu:** Denizcan Özcan (ASELSAN Aday Mühendis Havuzu & TEKNOFEST Robotaksi Finalisti, İÜC EEE 4. Sınıf, 3.44 GPA) 1. Öncelikli Donanım ve Entegrasyon Mühendisi.
* **Canlı Web Platformu & Canlı Yayın:** `https://trustia.com.tr` (GitHub Actions CI/CD üzerinden tam derlenmiş ve canlıya alınmıştır).
* **Resmi Tescil ve Belgeler:** 
  * 🇪🇺 **Avrupa Komisyonu (European Commission - ec.europa.eu):** Resmi Katılımcı Kayıt Defteri (Participant Register) tescili tamamlandı. Trustia Teknoloji adına 9 haneli resmi Avrupa Birliği Katılımcı Kimlik Kodu (**PIC Numarası: `861711529`**) tahsis edildi ve Horizon Europe / EIT sistemine kalıcı olarak işlendi.
  * 🇪🇺 **EIT Urban Mobility (Avrupa İnovasyon ve Teknoloji Enstitüsü):** Resmi Partner Bilgi Formu (NetSuite PIF Portal) üzerinden ortaklık tescili tamamlandı. Resmi AB İş Ortağı Kodu (**Partner ID: `CUS15554`**) tahsis edildi. €100.000 hibe başvurusu (Başvuru No: `3.1.02-1206-3732.3`) resmi olarak gönderildi.
  * 🇶🇦 **QSTP (Katar Bilim ve Teknoloji Parkı - Qatar Foundation, Doha):**
    * **30M$ Tech Venture Fon Başvurusu (9 Sayfa):** Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu ve $500k Pre-Seed SAFE ile başvuru tamamlandı.
    * **Resmi Kuluçka & Doha Sprint Programı Başvurusu (8 Sayfa):** 4 hafta Doha yüz yüze Sprint, konaklama/otel, ofis ve Katar şirket tescili desteğiyle resmi kuluçka başvurusu eksiksiz tamamlandı.
  * 🇹🇷 **BAYKAR Teknoloji (Baykar Tech):** Resmi Alt Yüklenici / Tedarikçi Portalı üzerinden Seviye-4 otonomi, GPS-denied 3D LiDAR SLAM, taktik yazılım ve İTO BTM tescili ile tedarikçi başvurusu eksiksiz tamamlandı.
  * 🇹🇷 **DEİK (Dış Ekonomik İlişkiler Kurulu - deik.org.tr):** T.C. Ticaret Bakanlığı koordinasyonundaki ticari diplomasi çatı kurulu bünyesindeki "Dijital Teknolojiler İş Konseyi"nden Trustia'ya resmi kurumsal üyelik daveti iletildi (14 Eylül 2026).
  * 🇹🇷 **ASELSAN Tedarikçi Portalı & Axcelerate Girişimcilik Merkezi:** 
    * **Tedarikçi Portalı:** "Yazılım Geliştirme" faaliyet alanı ön değerlendirmesi **RESMEN OLUMLU SONUÇLANDI** (Başvuru No: `0050569CCE941FD1A49FCEFB9B7BE7D6`). "TRUSTIA AI OTONOM SISTEMLERI" resmi potansiyel tedarikçi olarak kaydedildi, kurumsal SAP portal erişim kodu (`FZQHEXGFMTJU`) tahsis edildi ve Kurul Toplantısı onay sürecine geçildi.
    * **ASELSAN Girişimcilik Merkezi (Axcelerate - AGM):** GNSS-denied 3D LiDAR SLAM, taktik Seviye-4 otonomi, İTO BTM tescili ve 8 resmi PDF'lik başvuru paketiyle resmi başvuru **EKSİKSİZ İLETİLDİ VE GÖNDERİLDİ** (20 Eylül 2026). Durum: **"Başvuru İletildi ✔ -> Uygunluk Değerlendirmesi Aşamasında 🟡"**. SST (Savunma Sistem Teknolojileri / İnsansız Kara Araçları) teknik entegrasyon havuzuna alındı.
  * 🎖️ **NATO NSPA & T.C. Milli Savunma Bakanlığı (MSB TMKB):** Resmi NATO NCAGE Askeri Tedarikçi Kodu başvurusu (Referans No: `TR26258467723`) e-posta doğrulamasıyla tamamlandı ve MSB Türk Milli Kodlandırma Bürosu onayına sevk edildi (Sorumlu: Medine AYGUN, `tmkb@msb.gov.tr`, `+90 312 410 6184`).
  * 🇹🇷 **Savunma Sanayii Başkanlığı (SSYZ / SAYZEK):** Cumhurbaşkanlığı Savunma Sanayii Başkanlığı Yapay Zekâ Platformu'na Seviye-4 otonomi, GNSS-denied 3D SLAM ile resmi Simülasyon Portali başvurusu tamamlandı (Başvuru No: `170`, Durum: **"Onay Bekliyor"**).
  * 🇲🇹 **Malta Enterprise (Start-up Finance & MSRP - maltaenterprise.com):** Trustia AI Avrupa Otonomi Genel Merkezi (Naxxar/Lija Palazzo HQ) ve 3+5 yıllık resmi Avrupa Birliği (Schengen) oturumu için 1.500.000 € (€1.5M) Hibe / Teknoloji Desteği (Başvuru No: `100062411`) ve Girişimci İkamet İzni (Başvuru No: `100062412`, CRM No: `CRM:0175017`) başvuruları **RESMEN VE EKSİKSİZ GÖNDERİLDİ** (Çifte Durum: **"Form başarıyla gönderildi"**).
  * 🇹🇷 **fonVenture & fonbulucu (SPK Paya Dayalı Kitle Fonlama):** 15.000.000 TL hedef (18M TL fonlama tavanı, 150M TL değerleme, %10 pay) ile Seviye-4 Robotaksi kampanyası için resmi değerlendirme ve yatırımcı paketi (Master Deck, One-Pager, Ioniq 5 Planı) fonVenture Komitesine sunuldu.
  * 🌐 **Crunchbase Resmi Doğrulanmış Kurumsal Profil:** `crunchbase.com/organization/trustia-ai` (Isı Puanı: **93 ⬆**, Büyüme Puanı: **91 ⬆**, CB Sırası: **98.893 ⬆**, 1 Eylül 2026 Aktif $500k Ön Tohumlama Turu).
  * 🇺🇸 **Z Fellows ($10k Grant / San Francisco):** 10 dakikalık canlı Zoom mülakatı aşamasında (Görüşmeci: Grace Kasten - Pace Capital Partner, Randevu: 17 Eylül 2026 Perşembe 19:40 TRT).
  * 🇦🇪 **Dubai World Challenge for Self-Driving Transport (RTA Dubai):** $1.200.000 nakit ödüllü küresel Seviye-4 Robotaksi yarışması resmi başvurusu tamamlandı (Kasım 2026 Finalist Aşaması).
  * 🇸🇦 **NEOM Investment Fund & Autonomous Mobility (Suudi Arabistan):** 500 Milyar $ mega şehir otonomi yatırımı ve PoC başvurusu eksiksiz tamamlandı.
  * 🇸🇬 **Singapur Hükümeti (Startup SG & GIA - Enterprise Singapore):** Murat Furkan Bayram adına resmi Kurucu Profili (**ID: `#57428`**) %100 onaylandı; Küresel İnovasyon İttifakı (GIA) Hızlandırma Başvurusu (**Yanıt ID: `6aa85fa93dc42d7feef1bc57`**) tamamlanarak B2Match ve Asya-Pasifik derin teknoloji ağına dahil olundu (14 Eylül 2026).
  * 🇹🇷 **Teknopark İstanbul (HASAT 2026):** T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı (SSB) ve İTO çatı ortaklığındaki 100M TL destek ve yatırım havuzlu "HASAT 2026" teknoloji sahnesi resmi yarışma başvurusu tamamlandı (Durum: **"Başvurunuz Başarıyla Alındı! 🎉"**).
  * 🇹🇷 **ŞirketOrtağım Melek Yatırımcı Ağı (sirketortagim.com):** T.C. Hazine ve Maliye Bakanlığı akredite Bireysel Katılım Yatırımcısı (BKY) ağına 1M - 5M TL öz sermaye ve Master Pitch Deck ile resmi online girişim başvurusu **RESMEN VE EKSİKSİZ GÖNDERİLDİ** (20 Eylül 2026). Durum: **"Başvurunuz Alındı ✔ -> Seçim Komitesi Değerlendirmesi Aşamasında 🟡"**.
  * 🇹🇷 **Bilişim Vadisi (B-Stars Mobilite Hızlandırma Programı):** Otonom Test Pisti ve hızlandırma üssüne başvuru eksiksiz tamamlandı.
  * 🇹🇷 **İTO BTM Fulya Kampüsü:** 2026-II. Dönem Sözleşmeli Ön Kuluçka Girişimi. Feedback Round - 2 yatırımcı eşleşme başvurusu tamamlandı (Inveo Ventures, Startup Burada, Fuzul Ventures ile 23 Eylül 2026 Fulya Kampüsü yüz yüze görüşmesi).
  * 📜 **KOSGEB İleri Girişimci Sertifikası:** Belge No `KSB01UGE0115153370`.
  * 📜 **BTK Akademi Savunma Sanayii Ürün ve Platformları Sertifikası:** Belge No `L2zPtN4X1ZJ` (100/100 Tam Puan).
  * 📜 **TÜBİTAK ARBİS Milli Araştırmacı Sicili:** Sicil No `TBTK-0229-6571`.
  * 🛡️ **Open Invention Network (OIN 2.0 - openinventionnetwork.com):** Google, IBM, Sony, Toyota ve Red Hat destekli küresel açık kaynak patent savunma paktı resmi lisans sözleşmesi (Belge No: `f1e445769a9934114db095c4f5430a0e749d8201`, Tier 5 - 0 $ Katılım Ücreti) OIN CEO'su Keith Bergelt ve Murat Furkan Bayram tarafından **RESMEN ÇİFT TARAFLI İMZALANDI VE YÜRÜRLÜĞE GİRDİ** (16 Eylül 2026). Trustia'nın Linux, ROS2 ve Seviye-4 otonomi kodları uluslararası patent dokunulmazlığı ve karşılıklı lisans koruması altına alındı.
  * 🇺🇸 **Dorm Room Fund (First Round Capital - dormroomfund.com):** First Round Capital destekli dünyanın 1 numaralı genç/öğrenci kurucu fonuna $40,000 - $100,000 SAFE yatırımı için San Francisco takımı üzerinden resmi başvuru tamamlandı (16 Eylül 2026, Durum: **"Başvurunuz Başarıyla Alındı!"**).
* **Yazılım & Test:** 16.000+ satır özgün deterministik otonomi mimarisi (Hybrid A*, 3D NDT LiDAR SLAM, Pure Pursuit), 1.301/1.301 otomatik birim ve entegrasyon testi (%100 Başarı).
* **Donanım Platformu:** Hyundai Ioniq 5 E-GMP Otonom Seviye-4 Dönüşüm Kiti (Ouster OS2-128 LiDAR, 2x Livox Mid-360, Continental ARS 408-21 Radar, Septentrio RTK GNSS, NVIDIA Jetson AGX Orin 64GB, Kvaser U100 CAN-FD).
* **Dosya Düzeni & Sadeleştirilmiş Yapı:** 6 dağınık kategori yerine 3 ana klasör (`01_Core`, `02_Web`, `Kurumsal/`) modeline geçilmiş; 50+ mükerrer kopya ve gereksiz dosya temizlenerek tekil ve deterministik yapı sağlanmıştır.
