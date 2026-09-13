# TRUSTIA PROJESİ ZORUNLU ÇALIŞMA VE DOSYA YERLEŞİM KURALLARI (MANDATORY PROJECT RULES)

> [!IMPORTANT]
> Bu kural seti, bu projede çalışacak **TÜM YAPAY ZEKA ASİSTANLARI VE AJANLAR İÇİN ZORUNLUDUR**.
> Masaüstüne veya proje kök dizinine rastgele, baştan savma dosya oluşturulamaz veya atılamaz.
> Üretilen her dosya, kod, görsel, video, PDF veya sertifika AMACINA GÖRE AŞAĞIDAKİ 6 KATEGORİDEN İLGİLİSİNE YERLEŞTİRİLMEK ZORUNDADIR.

---

## 🚨 1. EN TEMEL VE ZORUNLU ALTIN KURAL: ANINDA HER YERDEN GÜNCELLEME VE CANLIYA DEPLOY (INSTANT GLOBAL UPDATE & DEPLOY)

> [!CRITICAL]
> **1. KURAL (EN BAŞTA GELEN VE TARTIŞMASIZ ZORUNLULUK):**
> Projede yeni bir gelişme olduğu, yeni bir başvuru/tescil/kod/özellik yapıldığı veya herhangi bir bilgi güncellendiği anda; **O ŞEY ANINDA VE İSTİSNASIZ BÜTÜN HER YERDEN GÜNCELLENECEK VE DERHAL GITHUB'A PUSH EDİLİP CANLIYA (`trustia.com.tr`) DEPLOY EDİLECEKTİR.**
> 
> * **Neler Anında Güncellenmek Zorundadır?**
>   1. **Canlı Web Platformu:** Ana sayfa, Hakkımızda, Robotaxi, İletişim, Footer, Navbar ve ilgili tüm bileşenler.
>   2. **SEO & Arama Motoru Verileri:** Sayfa meta etiketleri, OpenGraph, Twitter Cards, Schema.org JSON-LD kurumsal grafiği.
>   3. **Harita ve Tarayıcılar:** `sitemap.xml` (güncel `lastmod` tarihi ile) ve `robots.txt` AI tarayıcı direktifleri.
>   4. **Master Dokümantasyon:** `README.md`, `AGENTS.md`, `GEMINI.md` ve `.agents/rules/` kuralları.
>   5. **Yatırımcı ve Hibe Dosyaları:** Kategori 04'teki ilgili pitch deck ve modeller, Kategori 05'teki Master Takip Kütüğü (`.md` & `.pdf`).
> * **Kesin Şart:** Değişiklik yapılıp yerel bilgisayarda ASLA bekletilemez; anında `git add -A`, kurumsal commit ve `git push origin main` yapılarak GitHub Actions üzerinden `trustia.com.tr` canlı ortamına ve Google indeksine fırlatılacaktır!

---

## 📁 6 ANA KURUMSAL KATEGORİ VE KATI YERLEŞİM PLANI

Tüm dosyalar `C:\Users\Murat\Desktop\Trustia\` ana çatısı altında aşağıdaki 6 klasörde tutulacaktır:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Asıl Otonomi Yazılımı & Testler)
* **Buraya Konulacaklar:** Otonomi motoru, SLAM haritalama (3D NDT / ICP), Hybrid A* rota planlama, Pure Pursuit ve Stanley kontrolcüler, yapay zeka EYP/Mayın/KHKN tespit modelleri, CAN-Bus/ROS2/JAUS/Webots sürücüleri, 1.301 birim/entegrasyon testi, CLI scriptleri ve Taktik C2 Masaüstü Konsolu (GUI).
* **Kural:** Otonomi yazılımıyla ilgili tüm Python/C++ kodları ve testleri SADECE bu klasör altında oluşturulur veya düzenlenir. 1.301 testin %100 başarı oranı asla bozulamaz.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Sitesi ve Platform Kodları)
* **Buraya Konulacaklar:** Canlı web sitesi kaynak kodları (Next.js 16, React 19, Tailwind CSS 4, Three.js 3D modeller, web sayfaları, kurumsal akreditasyon bileşenleri, Schema.org JSON-LD, sitemap.xml ve robots.txt).
* **Kural:** Web arayüzü ile ilgili her şey SADECE bu klasör altında `website/` içinde geliştirilir. Canlı yayın [trustia.com.tr](https://trustia.com.tr) adresine GitHub Actions CI/CD üzerinden otomatik derlenir ve dağıtılır.

### 3. `03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/` 📜 (Resmi Belgeler ve Tesciller)
* **Buraya Konulacaklar:** KOSGEB İleri Girişimci katılım belgesi (`KSB01UGE0115153370`), BTK ve SSB Savunma Sanayii sertifikaları (`L2zPtN4X1ZJ`), İTO BTM Ön Kuluçka Sözleşmesi, Aselsan Tedarikçi Başvuru Evrakları (`0050569CCE941FD1A49FCEFB9B7BE7D6`) ve TÜBİTAK ARBİS Milli Araştırmacı Sicili (`TBTK-0229-6571`).
* **Kural:** Resmi devlet/şirket tescil belgeleri başka hiçbir yere konulamaz.

### 4. `04_Yatirimci_Sunumlari_ve_Is_Planlari/` 💼 (Yatırımcı Dosyaları & Finans)
* **Buraya Konulacaklar (4 Ana Alt Klasör + Kurucu CV):**
  * `Pitch_Decks/`: Master Investor Pitch Deck (EN), Executive One-Pager, B-Stars, Workup, Revo, Finberg, Inveo, NATO NIF sunumları.
  * `Finansal_Tablolar/`: Bilanço (Balance Sheet), Gelir Tablosu (P&L), Nakit Akışı (Cash Flow), Cap Table (`.csv` ve `.pdf`).
  * `Is_Plani_ve_Kanvas/`: İş Modeli Kanvası, İstanbul Robotaksi Operasyon & Fiyatlandırma Modeli, Kitle Fonlama Kampanya Planı.
  * `Teknik_ve_Organizasyon/`: Hyundai Ioniq 5 Seviye-4 Dönüşüm Şartnamesi, 27 parçalık Sensör BOM Listesi, Organizasyon Şeması.
  * `Murat_Furkan_Bayram_CV_Resume.pdf`: Kurucu & Sistem Mimarı resmi özgeçmişi.

### 5. `05_Uluslararasi_Hibe_ve_Vize_Basvurulari/` 🌍 (Global Fon ve Başvurular)
* **Buraya Konulacaklar (Tek Resmi Takip Kütüğü + 5 Konsolide Alt Klasör):**
  * `Trustia_Global_Basvuru_ve_Hibe_Takip_Rehberi_2026.md` & `.pdf`: 85+ uluslararası ve ulusal başvurunun resmi takip ve durum kütüğü.
  * `01_Avrupa_Birligi_ve_EIT_Hibeleri/`: Avrupa Komisyonu Katılımcı Kimlik Kodu (PIC: `861711529`), EIT Urban Mobility Partner ID (`CUS15554`, €100.000 Hibe Çağrısı: `3.1.02-1206-3732.3`), EIC Accelerator.
  * `02_Katar_QSTP_ve_Korfez_Programlari/`: QSTP 30M$ Venture Fon + 4 Haftalık Doha Sprint Kuluçkası, Dubai RTA $1.2M yarışması, NEOM Mega Şehir, Hub71 Abu Dhabi.
  * `03_Savunma_Sanayii_ve_Tedarikci_Portallari/`: BAYKAR Tech Resmi Tedarikçi Başvurusu, ASELSAN (#0050569), SSB SAYZEK (#170), NATO DIANA.
  * `04_Z_Fellows_ve_Silikon_Vadisi/`: Z Fellows canlı mülakat rehberleri (Grace Kasten / Pace Capital, 17 Eylül 2026), Emergent Ventures, Silikon Vadisi fonları.
  * `05_Turkiye_Teknokent_ve_Bilisim_Vadisi/`: Bilişim Vadisi B-Stars Otonom Test Pisti, Teknopark İstanbul Cube Incubation, DEİK Dijital Teknolojiler İş Konseyi.

### 6. `06_Medya_Gorsel_ve_Tanitim_Videolari/` 🎬 (Medya, Video ve Logolar)
* **Buraya Konulacaklar:**
  * `Videolar/`: 4K/HD demo videoları, 30 Ağustos zafer bayramı videosu, Master edit tanıtım filmleri.
  * `Logolar_ve_Ikonlar/`: PNG, JPG, ICO marka logoları, yüksek çözünürlüklü banner'lar ve simgeler.
  * `Hyundai_Ioniq_5_Test_Araci/`: Gerçek retrofit test aracı fotoğrafları (ön, tavan LiDAR podu, kokpit C2, VIP yolcu alanı, arka).
  * `Egirisim_Basin_Kiti_2026/`: Resmi egirişim basın kiti ve medya yayın paketi.

---

## ⛔ KESİN YASAKLAR VE ZORUNLULUKLAR
1. 🚨 **1. ZORUNLU KURAL (ANINDA HER YERDEN GÜNCELLEME VE CANLIYA DEPLOY):** Projede herhangi bir şey yapıldığı/oluştuğu anda o bilgi A'dan Z'ye BÜTÜN dosyalardan, web sitesinden, SEO'dan, dokümanlardan güncellenmek ve BEKLEMEDEN GitHub'a push edilip canlıya deploy edilmek ZORUNDADIR. Hiçbir güncelleme yerelde asılı bırakılamaz.
2. ❌ Masaüstüne (`C:\Users\Murat\Desktop`) veya proje köküne geçici bile olsa rastgele dosya BIRAKILAMAZ.
3. ❌ `Trustia/Trustia/` gibi iç içe çift klasör OLUŞTURULAMAZ.
4. ❌ Web kodları Core otonomi yazılımının içine, otonomi kodları web klasörünün içine KARIŞTIRILAMAZ.
5. ❌ Herhangi bir AI asistanı yeni bir dosya oluşturmadan önce YUKARIDAKİ 6 KATEGORİYİ KONTROL ETMEK VE TAM AİT OLDUĞU KLASÖRE YAZMAK ZORUNDADIR.
6. ❌ Tasarım ve içerikte çocukça, gayriciddi veya şablon görüntüler kullanılamaz; daima uluslararası kurumsal savunma ve otonomi standardı korunacaktır.

---

## 🧠 KALICI PROJE HAFIZASI VE GÜNCEL DURUM (PERMANENT CONTEXT)
* **Kurucu & Lider:** Murat Furkan Bayram (17 yaşında, Kurucu & CEO / Sistem Mimarı, %80 Hisse, TC: `59476566862`, Tel: `0537 064 04 60`, E-posta: `kariyer@trustia.com.tr`, LinkedIn: `https://www.linkedin.com/in/trustia`).
* **Kurucu Ortak & Operasyon:** Doğukan Bayram (%20 Hisse, Reşit Kurucu Ortak).
* **Mühendislik Havuzu:** Denizcan Özcan (ASELSAN Aday Mühendis Havuzu & TEKNOFEST Robotaksi Finalisti, İÜC EEE 4. Sınıf, 3.44 GPA) 1. Öncelikli Donanım ve Entegrasyon Mühendisi.
* **Canlı Web Platformu & Canlı Yayın:** `https://trustia.com.tr` (14 Eylül 2026 itibarıyla GitHub Actions CI/CD üzerinden tam derlenmiş ve canlıya alınmıştır).
* **Resmi Tescil ve Belgeler:** 
  * 🇪🇺 **Avrupa Komisyonu (European Commission - ec.europa.eu):** Resmi Katılımcı Kayıt Defteri (Participant Register) tescili tamamlandı. Trustia Teknoloji adına 9 haneli resmi Avrupa Birliği Katılımcı Kimlik Kodu (**PIC Numarası: `861711529`**) tahsis edildi ve Horizon Europe / EIT sistemine kalıcı olarak işlendi.
  * 🇪🇺 **EIT Urban Mobility (Avrupa İnovasyon ve Teknoloji Enstitüsü):** Resmi Partner Bilgi Formu (NetSuite PIF Portal) üzerinden ortaklık tescili tamamlandı. Resmi AB İş Ortağı Kodu (**Partner ID: `CUS15554`**) tahsis edildi. €100.000 hibe başvurusu (Başvuru No: `3.1.02-1206-3732.3`) resmi olarak gönderildi.
  * 🇶🇦 **QSTP (Katar Bilim ve Teknoloji Parkı - Qatar Foundation, Doha):**
    * **30M$ Tech Venture Fon Başvurusu (9 Sayfa):** Seviye-4 deterministik otonomi, GNSS-denied 3D LiDAR SLAM, Hyundai Ioniq 5 platformu ve $500k Pre-Seed SAFE ile başvuru tamamlandı.
    * **Resmi Kuluçka & Doha Sprint Programı Başvurusu (8 Sayfa):** 4 hafta Doha yüz yüze Sprint, konaklama/otel, ofis ve Katar şirket tescili desteğiyle resmi kuluçka başvurusu eksiksiz tamamlandı.
  * 🇹🇷 **BAYKAR Teknoloji (Baykar Tech):** Resmi Alt Yüklenici / Tedarikçi Portalı üzerinden Seviye-4 otonomi, GPS-denied 3D LiDAR SLAM, taktik yazılım ve İTO BTM tescili ile tedarikçi başvurusu eksiksiz tamamlandı.
  * 🇹🇷 **DEİK (Dış Ekonomik İlişkiler Kurulu - deik.org.tr):** T.C. Ticaret Bakanlığı bünyesindeki ticari diplomasi çatı kuruluna "Dijital Teknolojiler İş Konseyi" kapsamında resmi başvuru tamamlandı.
  * 🇹🇷 **ASELSAN Tedarikçi Portalı:** Resmi Başvuru Girişimi (Başvuru No: `0050569CCE941FD1A49FCEFB9B7BE7D6` — Yazılım Geliştirme, Sistem Platform Entegrasyonu, Kara Platform Entegrasyonu Ön Değerlendirme Sürecinde).
  * 🇹🇷 **Savunma Sanayii Başkanlığı (SSYZ / SAYZEK):** Cumhurbaşkanlığı Savunma Sanayii Başkanlığı Yapay Zekâ Platformu'na Seviye-4 otonomi, GNSS-denied 3D SLAM ile resmi Simülasyon Portali başvurusu tamamlandı (Başvuru No: `170`, Durum: **"Onay Bekliyor"**).
  * 🇹🇷 **fonbulucu (SPK Paya Dayalı Kitle Fonlama - Kampanya Kodu: W1MV5K):** 15.000.000 TL hedef (18M TL fonlama tavanı, 150M TL değerleme, %10 pay) ile Seviye-4 Robotaksi kampanyası resmi olarak **Ön İncelemeye Sunuldu**.
  * 🌐 **Crunchbase Resmi Doğrulanmış Kurumsal Profil:** `crunchbase.com/organization/trustia-ai` (Isı Puanı: **85 ⬆**, CB Sırası: 534.468, 1 Eylül 2026 Aktif $500k Ön Tohumlama Turu).
  * 🇺🇸 **Z Fellows ($10k Grant / San Francisco):** 10 dakikalık canlı Zoom mülakatı aşamasında (Görüşmeci: Grace Kasten - Pace Capital Partner, Randevu: 17 Eylül 2026 Perşembe 19:40 TRT).
  * 🇦🇪 **Dubai World Challenge for Self-Driving Transport (RTA Dubai):** $1.200.000 nakit ödüllü küresel Seviye-4 Robotaksi yarışması resmi başvurusu tamamlandı (Kasım 2026 Finalist Aşaması).
  * 🇸🇦 **NEOM Investment Fund & Autonomous Mobility (Suudi Arabistan):** 500 Milyar $ mega şehir otonomi yatırımı ve PoC başvurusu eksiksiz tamamlandı.
  * 🇹🇷 **Bilişim Vadisi (B-Stars Mobilite Hızlandırma Programı):** Otonom Test Pisti ve hızlandırma üssüne başvuru eksiksiz tamamlandı.
  * 🇹🇷 **İTO BTM Fulya Kampüsü:** 2026-II. Dönem Sözleşmeli Ön Kuluçka Girişimi.
  * 📜 **KOSGEB İleri Girişimci Sertifikası:** Belge No `KSB01UGE0115153370`.
  * 📜 **BTK Akademi Savunma Sanayii Ürün ve Platformları Sertifikası:** Belge No `L2zPtN4X1ZJ` (100/100 Tam Puan).
  * 📜 **TÜBİTAK ARBİS Milli Araştırmacı Sicili:** Sicil No `TBTK-0229-6571`.
* **Yazılım & Test:** 16.000+ satır özgün deterministik otonomi mimarisi (Hybrid A*, 3D NDT LiDAR SLAM, Pure Pursuit), 1.301/1.301 otomatik birim ve entegrasyon testi (%100 Başarı).
* **Donanım Platformu:** Hyundai Ioniq 5 E-GMP Otonom Seviye-4 Dönüşüm Kiti (Ouster OS2-128 LiDAR, 2x Livox Mid-360, Continental ARS 408-21 Radar, Septentrio RTK GNSS, NVIDIA Jetson AGX Orin 64GB, Kvaser U100 CAN-FD).
* **Dosya Düzeni & Masaüstü Temizliği:** Masaüstündeki geçici çıktılar tamamen 04, 05 ve 06 ana klasörlerine dağıtılmış, masaüstü %100 temizlenmiş ve tüm değişiklikler GitHub `main` dalına işlenerek canlıya alınmıştır.
