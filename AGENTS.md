# TRUSTIA PROJESİ ÇALIŞMA VE DOSYA DÜZENİ REHBERİ

> [!NOTE]
> Bu rehber, Trustia projesinde çalışan yapay zeka asistanları ve geliştiriciler için temel çalışma prensiplerini belirler.
> Amaç: Gereksiz bürokrasi ve dosya şişkinliğini önlemek, temiz ve odaklı bir kod/doküman tabanı korumaktır.

---

## 🎯 5 TEMEL ÇALIŞMA İLKESİ

### 1. 3 ANA KLASÖR DÜZENİ (TEMİZ ÇALIŞMA ALANI)
* Tüm proje dosyaları sadece aşağıdaki 3 ana klasör altında tutulur:
  1. **`01_Trustia_Otonom_Yazilim_Core/`**: Otonomi yazılımı, algoritmalar, testler ve teknik dokümanlar.
  2. **`02_Trustia_Web_Platformu/`**: Web sitesi kaynak kodları (`website/`).
  3. **`Kurumsal/`**: Şirketin resmi belgeleri, sunumları, başvuruları ve medya varlıkları (`Belgeler/`, `Sunumlar/`, `Basvurular/`, `Medya/`).
* Masaüstüne (`C:\Users\Murat\Desktop`) veya proje kök dizinine geçici/baştan savma dosya bırakılamaz.

### 2. WEB SİTESİNİ ŞİŞİRMEME & GITHUB MERKEZLİ ÇALIŞMA
* **Her yeni başvuruda veya küçük gelişmede web sitesini (`trustia.com.tr`) kurcalamaya veya bileşen eklemeye GEREK YOKTUR.**
* Yapılan geliştirmeler, belgeler ve güncellemeler GitHub'a (`git push origin main`) pushlandığı anda yeterlidir.
* Canlı web sitesi sadece kurucu özel olarak talep ettiğinde veya büyük bir kurumsal lansman olduğunda güncellenir.

### 3. SIFIR MÜKERRER KOPYA VE TEMİZ İSİMLENDİRME
* Bir dosyanın birden fazla klasöre kopyalanması yasaktır. Her belgenin tek bir master kopyası olur.
* `test_*`, `kopya`, `yeni`, `final_son` gibi dağınık dosya isimleri repoda bırakılmaz.
* Sürüm takibi için dosya adı değiştirmek yerine Git geçmişi kullanılır.

### 4. DOĞRU BİLGİ VE KURUMSAL YÖNETİŞİM
* Uydurma, tahmini veya doğrulanmamış bilgi yazılamaz.
* Kurucu ortaklık ve yönetim yapısı sabittir:
  * **Murat Furkan Bayram:** Kurucu & CEO / Sistem Mimarı (%100 Hisse).
  * **Denizcan Özcan:** Baş Donanım ve Entegrasyon Mühendisi.

### 5. OTOMOTİV EMNİYET VE FAILSAFE KİLİDİ (ASIL-D)
* `01_Trustia_Otonom_Yazilim_Core` içindeki 5ms sürücü müdahalesi (override), 200ms watchdog ve E-Stop mekanizmaları güvenlik gereği asla bypass edilemez.

---

## 📁 DİZİN DÜZENİ ÖZETİ

```text
Trustia/
├── 01_Trustia_Otonom_Yazilim_Core/    ← Otonomi Çekirdeği (Python/C++, 1.301 Test, CLI, C2 GUI)
├── 02_Trustia_Web_Platformu/          ← Web Platformu (Next.js 16, React 19)
├── Kurumsal/                          ← Birleşik Kurumsal Varlıklar
│   ├── Belgeler/                      ← Resmi devlet/kurum onay belgeleri ve tesciller
│   ├── Sunumlar/                      ← Master Pitch Deck'ler, finans modelleri ve planlar
│   ├── Basvurular/                    ← Takip rehberi kütüğü ve resmi başvuru dosyaları
│   └── Medya/                         ← HD logolar, araç fotoğrafları ve master videolar
├── AGENTS.md                          ← Çalışma rehberi
└── README.md                          ← Ana proje dokümantasyonu
```

---

## 🧠 GÜNCEL KURUMSAL DURUM & KALICI HAFIZA
* **Kurucu:** Murat Furkan Bayram (%100 CEO & Sistem Mimarı, 0537 064 04 60, kariyer@trustia.com.tr).
* **Mühendislik:** Denizcan Özcan (ASELSAN Aday Havuzu & TEKNOFEST Robotaksi Finalisti).
* **Resmi Akreditasyonlar:**
  * 🇪🇺 Avrupa Komisyonu PIC: `861711529`
  * 🇪🇺 EIT Urban Mobility Partner ID: `CUS15554` (€100k hibe başvurusu)
  * 🇹🇷 ASELSAN Potansiyel Tedarikçi (`0050569CCE941FD1A49FCEFB9B7BE7D6`, SAP: `FZQHEXGFMTJU`) & Axcelerate AGM Başvurusu (Uygunluk Aşamasında)
  * 🇹🇷 ŞirketOrtağım Melek Yatırımcı Ağı Başvurusu (Komite İncelemesinde)
  * 🇹🇷 BAYKAR Tedarikçi Başvurusu
  * 🇹🇷 DEİK Dijital Teknolojiler İş Konseyi Üyelik Daveti
  * 🎖️ NATO NCAGE Tedarikçi Kodu (`TR26258467723` - MSB Onayında)
  * 🛡️ Open Invention Network (OIN 2.0) İmzalı Patent Savunma Paktı Lisansı
  * 🇲🇹 Malta Enterprise €1.5M Hibe & MSRP İkamet Başvuruları
  * 🇶🇦 QSTP Katar 30M$ Fon + Doha Sprint Başvurusu
  * 🇺🇸 Z Fellows ($10k Grant) & Dorm Room Fund (First Round Capital)
  * 🇹🇷 İTO BTM Fulya Kampüsü Ön Kuluçka & Teknopark İstanbul HASAT 2026
  * 📜 KOSGEB (`KSB01UGE0115153370`) ve BTK Savunma Sanayii (`L2zPtN4X1ZJ`) Sertifikaları
