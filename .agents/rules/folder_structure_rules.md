# MANDATORY AGENT GOVERNANCE & REPOSITORY RULES (TRUSTIA ENTERPRISE)

> [!IMPORTANT]
> This policy is binding for all AI models, agentic workflows, subagents, and automated developer tools interacting with the Trustia workspace.
> Non-compliance with folder boundaries or dumping files in the workspace root or Desktop is strictly prohibited.

---

## 🚨 THE 8 SUPREME DIRECTIVES (MANDATORY AGENT GOVERNANCE)

### RULE #1: TOTAL REPOSITORY SYNCHRONIZATION & ZERO OUTDATED FILE DIRECTIVE (INSTANT GLOBAL UPDATE & LIVE DEPLOY)
> Whenever ANY accomplishment, credential, official approval, supplier registration, grant milestone, or corporate data update occurs (such as ASELSAN Pre-Evaluation Approval or DEİK Invitation): **IT IS NOT ENOUGH TO ONLY UPDATE THE WEBSITE OR A SINGLE FILE. LITERALLY EVERY SINGLE RELEVANT FILE ACROSS ALL 6 REPOSITORY CATEGORIES AND ROOT DOCUMENTATION MUST BE SIMULTANEOUSLY AND COMPREHENSIVELY SYNCHRONIZED AND PROMPTLY PUSHED TO GITHUB FOR PRODUCTION DEPLOYMENT (`trustia.com.tr`).**
> * **Mandatory Scope Across All 6 Architectural Domains:**
>   1. **`01_Trustia_Otonom_Yazilim_Core/`**: Autonomy stack documentation (`docs/`), certification reports (`docs/reports/`), CLI tools (`trustia_cli.py`), and compliance records.
>   2. **`02_Trustia_Web_Platformu/`**: Homepage, About, Robotaxi, Accreditations (`InstitutionalAccreditations.tsx`), Footer, Navbar, Schema.org JSON-LD, SEO meta tags, `sitemap.xml`, and `robots.txt`.
>   3. **`03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/`**: Official government credentials, portal access logs (`Aselsan_Tedarikci_Kodlari.txt`), and state registry files.
>   4. **`04_Yatirimci_Sunumlari_ve_Is_Planlari/`**: All pitch decks (`Pitch_Decks/`), executive one-pagers, financial models, business plans, and technical specifications.
>   5. **`05_Uluslararasi_Hibe_ve_Vize_Basvurulari/`**: Master tracking guide (`Trustia_Global_Basvuru_ve_Hibe_Takip_Rehberi_2026.md` & `.pdf`), defense supplier packages, and international grant dossiers.
>   6. **`06_Medya_Gorsel_ve_Tanitim_Videolari/`**: Media kits (`Egirisim_Basin_Kiti_2026/`), press releases, and corporate media files.
>   7. **Root Governance Files:** `README.md`, `AGENTS.md`, `GEMINI.md`, and `.agents/rules/folder_structure_rules.md`.
> * **Zero Outdated File Tolerance:** Leaving any file in an outdated status (e.g. stating "pre-evaluation pending" or "applied" when an approval or invitation has been granted) is strictly forbidden. All files must reflect verified real-time ground truth.
> * **Instant Deployment Mandate:** Changes must NEVER be held locally; execute `git add -A`, corporate commit, and `git push origin main` immediately for live deployment.

### RULE #2: BILINGUAL TR/EN PARITY
> Whenever documentation or web content is created or updated, **both Turkish and English versions must be maintained in complete parity.** Global VCs (Z Fellows, EITUM, QSTP) inspect English; national bodies (ASELSAN, BAYKAR, KOSGEB) inspect Turkish.

### RULE #3: MARKDOWN & PDF TWIN SYNCHRONIZATION
> Whenever an MD pitch deck, business model, or technical specification is updated in Category 04 or 05, **its official PDF counterpart must immediately be re-generated and kept in 100% sync.**

### RULE #4: PROOF-ONLY & VERIFIED FACTS
> **Zero tolerance for speculation or unverified claims.** Every single claim must have an official reference identifier (e.g. EU PIC `#861711529`, EIT Partner `#CUS15554`, ASELSAN `#0050569`, fonbulucu `#W1MV5K`) or deterministic code proof (1,301 passed tests).

### RULE #5: CLEAN SLATE & PROFESSIONAL NAMING
> **Zero loose or duplicate filenames.** Never generate files named `_kopya`, `_yeni`, `_final_son`. Every file has a single authoritative Master name; revision history is managed strictly via Git.

### RULE #6: AUTOMOTIVE SAFETY & FAILSAFE KERNEL (ISO 26262 ASIL-D)
> The 5ms human override, 200ms hardware watchdog, and E-Stop fail-safe mechanisms inside `01_Trustia_Otonom_Yazilim_Core` MUST NEVER be bypassed, relaxed, or disabled under any circumstances.

### RULE #7: EXECUTIVE GOVERNANCE & CAP TABLE PARITY
> Standard executive roles must be consistently preserved across all documents: Murat Furkan Bayram (80% Founder & CEO / Systems Architect), Doğukan Bayram (20% Co-Founder & Operations), Denizcan Özcan (Lead Hardware & Integration Engineer).

### RULE #8: ONE-CLICK ZERO-FRICTION DEMO LAUNCHER
> Every autonomy module, AI detection model, or simulation tool must be executable and demonstrable in a single keystroke via `TRUSTIA_BASLAT.bat` or `trustia_cli.py`.

---

## 📁 The 6 Strict Architectural Domains

All files within `C:\Users\Murat\Desktop\Trustia\` MUST reside in one of the following 6 designated directories:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Autonomy Stack & Verification)
* **Contents:** Hybrid A* motion planning, 2D/3D NDT Pose-Graph LiDAR SLAM, Pure Pursuit & Stanley drive-by-wire controllers, Physical AI threat/obstacle detection (IED, landmine, tripwire, CBRN), NATO STANAG 4586 Level-4 & SAE AS6091 JAUS protocols, CAN-Bus/ROS 2 integration bridges, 1,301 automated unit/integration tests, CLI tools, and Tactical C2 Mission Control Console (GUI).
* **Strict Boundary:** All backend, robotics, algorithmic, simulation, and hardware interfacing code belongs exclusively here.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Platform & Visualizers)
* **Contents:** Enterprise Next.js 16, React 19, Tailwind CSS 4, Three.js 3D vehicle visualizers, corporate showcase pages, institutional accreditations grid, metadata, Schema.org JSON-LD, `sitemap.xml`, and `robots.txt`.
* **Strict Boundary:** All front-end web components, styles, public assets, and web configuration files belong exclusively in `website/` under this folder.

### 3. `03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/` 📜 (Government Credentials & Official Registrations)
* **Contents:** Republic of Turkey Ministry of Industry & Technology KOSGEB Advanced Entrepreneur certificate (`KSB01UGE0115153370`), BTK Academy & SSB Defense Industry certification (`L2zPtN4X1ZJ`), TÜBİTAK ARBİS National Researcher registration (`TBTK-0229-6571`), and ASELSAN candidate supplier dossier (`0050569CCE941FD1A49FCEFB9B7BE7D6`).
* **Strict Boundary:** Official governmental, ministerial, and defense supplier certifications belong exclusively here.

### 4. `04_Yatirimci_Sunumlari_ve_Is_Planlari/` 💼 (Investor Packages & Financials)
* **Consolidated Subfolders:**
  * `Pitch_Decks/`: Master Investor Pitch Deck (EN), Executive One-Pager, B-Stars, Workup, Revo, Finberg, Inveo, NATO NIF decks.
  * `Finansal_Tablolar/`: Balance Sheet (Bilanço), P&L Statement (Gelir Tablosu), Cash Flow (Nakit Akışı), Cap Table (`.csv` & `.pdf`).
  * `Is_Plani_ve_Kanvas/`: Business Model Canvas, Istanbul Robotaxi Operations & Pricing Model, Crowdfunding Master Plan.
  * `Teknik_ve_Organizasyon/`: Hyundai Ioniq 5 Level-4 Retrofit Specification, Sensor BOM Table, Organizational Structure.
  * `Murat_Furkan_Bayram_CV_Resume.pdf`: Official Founder & Systems Architect executive resume.
* **Strict Boundary:** No redundant or loose duplicate files.

### 5. `05_Uluslararasi_Hibe_ve_Vize_Basvurulari/` 🌍 (Global Grants & Accelerators)
* **Master Registry:** `Trustia_Global_Basvuru_ve_Hibe_Takip_Rehberi_2026.md` & `.pdf` (Consolidated record of 85+ applications across 15+ countries).
* **Consolidated Subfolders:**
  * `01_Avrupa_Birligi_ve_EIT_Hibeleri/`: EU Participant Register (PIC: `861711529`), EIT Urban Mobility Partner (`CUS15554`, €100k Grant: `3.1.02-1206-3732.3`), EIC Accelerator.
  * `02_Katar_QSTP_ve_Korfez_Programlari/`: QSTP Qatar ($30M Venture Fund + 4-week Doha Sprint Residency), Dubai RTA $1.2M Challenge, NEOM, Hub71.
  * `03_Savunma_Sanayii_ve_Tedarikci_Portallari/`: BAYKAR Tech Supplier Portal, ASELSAN (#0050569), SSB SAYZEK (#170), NATO DIANA.
  * `04_Z_Fellows_ve_Silikon_Vadisi/`: Z Fellows ($10k Grant, Grace Kasten / Pace Capital Interview), Emergent Ventures, Silicon Valley VC packages.
  * `05_Turkiye_Teknokent_ve_Bilisim_Vadisi/`: Bilişim Vadisi B-Stars Proving Ground, Teknopark Istanbul Cube Incubation, DEİK Digital Council.

### 6. `06_Medya_Gorsel_ve_Tanitim_Videolari/` 🎬 (Media, Visuals & Brand Assets)
* **Consolidated Subfolders:**
  * `Videolar/`: 4K/HD demonstration videos, 30 August special video, Master edit showcase videos.
  * `Logolar_ve_Ikonlar/`: HD vector logos, corporate brand banners, icons.
  * `Hyundai_Ioniq_5_Test_Araci/`: High-resolution real retrofit vehicle photographs (front, LiDAR pod, cockpit, VIP cabin, rear).
  * `Egirisim_Basin_Kiti_2026/`: Official press release kit and media distribution package.

---

## ⛔ Absolute Prohibitions
1. ❌ NO dumping of files onto `Desktop` (`C:\Users\Murat\Desktop`) or the project root.
2. ❌ NO nested duplicate folders (e.g. `Trustia/Trustia/`).
3. ❌ NO mixing of web platform code into autonomy core or vice versa.
4. ❌ NEVER break the 100% pass rate of the 1,301 automated test suite.
5. ❌ MAINTAIN enterprise corporate aesthetic: Avoid playful, informal, or non-defense styling.
