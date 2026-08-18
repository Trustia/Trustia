# TRUSTIA PROJESİ ZORUNLU ÇALIŞMA VE DOSYA YERLEŞİM KURALLARI (MANDATORY AGENT RULES)

> [!IMPORTANT]
> Bu kural seti, bu projede çalışacak **TÜM YAPAY ZEKA ASİSTANLARI VE AJANLAR İÇİN ZORUNLUDUR**.
> Masaüstüne veya proje kök dizinine rastgele, baştan savma dosya oluşturulamaz veya atılamaz.
> Üretilen her dosya, kod, görsel, video, PDF veya sertifika AMACINA GÖRE AŞAĞIDAKİ 6 KATEGORİDEN İLGİLİSİNE YERLEŞTİRİLMEK ZORUNDADIR.

---

## 📁 6 ANA KURUMSAL KATEGORİ VE KATI YERLEŞİM PLANI

Tüm dosyalar `C:\Users\Murat\Desktop\Trustia\` ana çatısı altında aşağıdaki 6 klasörde tutulacaktır:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Asıl Otonomi Yazılımı & Testler)
* **Buraya Konulacaklar:** Otonomi motoru, SLAM haritalama, Hybrid A* rota, Pure Pursuit kontrolcü, yapay zeka EYP/Mayın/KHKN tespit modelleri, CAN-Bus/ROS2/JAUS/Webots sürücüleri, 1.276 birim/entegrasyon testi, CLI scriptleri ve Taktik C2 Masaüstü Konsolu.
* **Kural:** Otonomi yazılımıyla ilgili tüm Python/C++ kodları ve testleri SADECE bu klasör altında oluşturulur veya düzenlenir.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Sitesi ve Platform Kodları)
* **Buraya Konulacaklar:** Canlı web sitesi kaynak kodları (Next.js 16, React 19, Tailwind CSS 4, Three.js 3D modeller, web sayfaları, bileşenler ve web API'leri).
* **Kural:** Web arayüzü ile ilgili her şey SADECE bu klasör altında `website/` içinde geliştirilir.

### 3. `03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/` 📜 (Resmi Belgeler ve Tesciller)
* **Buraya Konulacaklar:** KOSGEB sertifikaları, BTK ve SSB Savunma Sanayii sertifikaları, Aselsan tedarikçi evrakları ve Every.io'dan gelen ABD Delaware C-Corp kuruluş belgeleri (Certificate of Incorporation, EIN vb.).
* **Kural:** Resmi devlet/şirket tescil belgeleri başka hiçbir yere konulamaz.

### 4. `04_Yatirimci_Sunumlari_ve_Is_Planlari/` 💼 (Yatırımcı Dosyaları & Finans)
* **Buraya Konulacaklar:**
  * `Pitch_Decks/`: Yatırımcı sunumları (Global, Hub71, Demoday, EXIST vb.).
  * `Finansal_Tablolar/`: Bilanço, Gelir Tablosu (P&L), Nakit Akışı, Cap Table.
  * `Is_Plani_ve_Kanvas/`: İş Modeli Kanvası, İş Planı ve Finansal Raporlar.
  * `Teknik_ve_Organizasyon/`: Teknik mimari dokümanları ve organizasyon şemaları.
  * `Murat_Furkan_Bayram_CV_Resume.pdf`: Kurucu özgeçmişi.

### 5. `05_Uluslararasi_Hibe_ve_Vize_Basvurulari/` 🌍 (Global Fon ve Başvurular)
* **Buraya Konulacaklar:** EIC Accelerator (AB), EXIST (Almanya), Hub71 (Abu Dhabi), KSGC (Güney Kore), Startup Vizeleri (İngiltere Innovator Founder, Kanada SUV, Almanya, İspanya) ve ASELSAN/SSB Tedarikçi Başvuru Dosyaları.

### 6. `06_Medya_Gorsel_ve_Tanitim_Videolari/` 🎬 (Medya, Video ve Logolar)
* **Buraya Konulacaklar:**
  * `Videolar/`: Demo ve sunum MP4 videoları.
  * `Logolar_ve_Ikonlar/`: PNG, JPG, ICO marka logoları ve simgeleri.
  * `Vektorel_Cizimler/`: SVG teknik çizimleri ve ikonlar.

---

## ⛔ KESİN YASAKLAR VE ZORUNLULUKLAR
1. ❌ Masaüstüne (`C:\Users\Murat\Desktop`) veya proje köküne geçici bile olsa rastgele dosya BIRAKILAMAZ.
2. ❌ `Trustia/Trustia/` gibi iç içe çift klasör OLUŞTURULAMAZ.
3. ❌ Web kodları Core otonomi yazılımının içine, otonomi kodları web klasörünün içine KARIŞTIRILAMAZ.
4. ❌ Herhangi bir AI asistanı yeni bir dosya oluşturmadan önce YUKARIDAKİ 6 KATEGORİYİ KONTROL ETMEK VE TAM AİT OLDUĞU KLASÖRE YAZMAK ZORUNDADIR.
