# MANDATORY AGENT GOVERNANCE & REPOSITORY RULES (TRUSTIA ENTERPRISE)

> [!IMPORTANT]
> This policy is binding for all AI models, agentic workflows, subagents, and automated developer tools interacting with the Trustia workspace.
> Non-compliance with folder boundaries or dumping files in the workspace root or Desktop is strictly prohibited.

---

## 🚨 THE 8 SUPREME DIRECTIVES (MANDATORY AGENT GOVERNANCE)

### RULE #1: TOTAL REPOSITORY SYNCHRONIZATION & ZERO OUTDATED FILE DIRECTIVE (INSTANT GLOBAL UPDATE & LIVE DEPLOY)
> Whenever ANY accomplishment, credential, official approval, supplier registration, grant milestone, or corporate data update occurs (such as ASELSAN Pre-Evaluation Approval or DEİK Invitation): **IT IS NOT ENOUGH TO ONLY UPDATE THE WEBSITE OR A SINGLE FILE. LITERALLY EVERY SINGLE RELEVANT FILE ACROSS ALL 3 REPOSITORY ARCHITECTURAL DOMAINS AND ROOT DOCUMENTATION MUST BE SIMULTANEOUSLY AND COMPREHENSIVELY SYNCHRONIZED AND PROMPTLY PUSHED TO GITHUB FOR PRODUCTION DEPLOYMENT (`trustia.com.tr`).**
> * **Mandatory Scope Across All 3 Architectural Domains:**
>   1. **`01_Trustia_Otonom_Yazilim_Core/`**: Autonomy stack documentation (`docs/`), certification reports (`docs/reports/`), CLI tools (`trustia_cli.py`), and compliance records.
>   2. **`02_Trustia_Web_Platformu/`**: Homepage, About, Robotaxi, Accreditations (`InstitutionalAccreditations.tsx`), Footer, Navbar, Schema.org JSON-LD, SEO meta tags, `sitemap.xml`, and `robots.txt`.
>   3. **`Kurumsal/` (Consolidated Corporate Assets - 4 Clean Subfolders):**
>      * `Belgeler/`: Official government credentials, portal access logs (`Aselsan_Tedarikci_Kodlari.txt`), and state registry files.
>      * `Sunumlar/`: All pitch decks (`Master_Pitch_Deck_EN/TR.pdf`, `Executive_One_Pager_EN.pdf`, B-Stars, Workup, Revo, Finberg, Inveo, NATO NIF decks, `Cap_Table.csv`, and `Ioniq5_Fotografli_Master_Plan_TR/EN.pdf`).
>      * `Basvurular/`: Master tracking guide (`Takip_Rehberi_2026.md` & `.pdf`), ASELSAN Axcelerate submission ZIP, Malta Enterprise, NATO DIANA, and Z Fellows interview master guides.
>      * `Medya/`: Brand logos, master banner, real Hyundai Ioniq 5 test vehicle photo suite, master demo/zafer/edit videos, and official press releases.
>   4. **Root Governance Files:** `README.md`, `AGENTS.md`, `GEMINI.md`, and `.agents/rules/folder_structure_rules.md`.
> * **Zero Outdated File Tolerance:** Leaving any file in an outdated status (e.g. stating "pre-evaluation pending" or "applied" when an approval or invitation has been granted) is strictly forbidden. All files must reflect verified real-time ground truth.
> * **Instant Deployment Mandate:** Changes must NEVER be held locally; execute `git add -A`, corporate commit, and `git push origin main` immediately for live deployment.

### RULE #2: BILINGUAL TR/EN PARITY
> Whenever documentation or web content is created or updated, **both Turkish and English versions must be maintained in complete parity.** Global VCs (Z Fellows, EITUM, QSTP) inspect English; national bodies (ASELSAN, BAYKAR, KOSGEB) inspect Turkish.

### RULE #3: MARKDOWN & PDF TWIN SYNCHRONIZATION
> Whenever an MD pitch deck, business model, or tracking registry is updated in `Kurumsal/Sunumlar/` or `Kurumsal/Basvurular/`, **its official PDF counterpart must immediately be re-generated and kept in 100% sync.**

### RULE #4: PROOF-ONLY & VERIFIED FACTS
> **Zero tolerance for speculation or unverified claims.** Every single claim must have an official reference identifier (e.g. EU PIC `#861711529`, EIT Partner `#CUS15554`, ASELSAN `#0050569`, fonbulucu `#W1MV5K`) or deterministic code proof (1,301 passed tests).

### RULE #5: CLEAN SLATE, ZERO DUPLICATE & PROFESSIONAL NAMING
> **Zero loose, test, or duplicate files.** Never generate files named `_kopya`, `_yeni`, `_final_son`, `test_*`. Every document has a single authoritative Master name; duplicate file copies across multiple folders are strictly forbidden. Revision history is managed strictly via Git.

### RULE #6: AUTOMOTIVE SAFETY & FAILSAFE KERNEL (ISO 26262 ASIL-D)
> The 5ms human override, 200ms hardware watchdog, and E-Stop fail-safe mechanisms inside `01_Trustia_Otonom_Yazilim_Core` MUST NEVER be bypassed, relaxed, or disabled under any circumstances.

### RULE #7: EXECUTIVE GOVERNANCE & CAP TABLE PARITY
> Standard executive roles must be consistently preserved across all documents: Murat Furkan Bayram (80% Founder & CEO / Systems Architect), Doğukan Bayram (20% Co-Founder & Operations), Denizcan Özcan (Lead Hardware & Integration Engineer).

### RULE #8: ONE-CLICK ZERO-FRICTION DEMO LAUNCHER
> Every autonomy module, AI detection model, or simulation tool must be executable and demonstrable in a single keystroke via `TRUSTIA_BASLAT.bat` or `trustia_cli.py`.

---

## 📁 The 3 Strict Architectural Domains

All files within `C:\Users\Murat\Desktop\Trustia\` MUST reside in one of the following 3 designated directories:

### 1. `01_Trustia_Otonom_Yazilim_Core/` 🚀 (Autonomy Stack & Verification)
* **Contents:** Hybrid A* motion planning, 2D/3D NDT Pose-Graph LiDAR SLAM, Pure Pursuit & Stanley drive-by-wire controllers, Physical AI threat/obstacle detection (IED, landmine, tripwire, CBRN), NATO STANAG 4586 Level-4 & SAE AS6091 JAUS protocols, CAN-Bus/ROS 2 integration bridges, 1,301 automated unit/integration tests, CLI tools, and Tactical C2 Mission Control Console (GUI).
* **Strict Boundary:** All backend, robotics, algorithmic, simulation, and hardware interfacing code belongs exclusively here.

### 2. `02_Trustia_Web_Platformu/` 🌐 (Web Platform & Visualizers)
* **Contents:** Enterprise Next.js 16, React 19, Tailwind CSS 4, Three.js 3D vehicle visualizers, corporate showcase pages, institutional accreditations grid, metadata, Schema.org JSON-LD, `sitemap.xml`, and `robots.txt`.
* **Strict Boundary:** All front-end web components, styles, public assets, and web configuration files belong exclusively in `website/` under this folder.

### 3. `Kurumsal/` 🏢 (Consolidated Corporate Assets, Decks & Media)
Streamlined single repository domain structured into 4 dedicated functional directories:
* **`Belgeler/` 📜 (Official State & Institutional Credentials):**
  * KOSGEB Advanced Entrepreneur Certificate (`KSB01UGE0115153370`)
  * BTK Academy & SSB Defense Industry 100/100 Certification (`L2zPtN4X1ZJ`)
  * İTO BTM Executed Pre-Incubation Agreement & Official Company Incorporation Registry
  * Open Invention Network (OIN 2.0) Global Patent Defense License Agreement
  * ASELSAN SAP Credentials (`Aselsan_Tedarikci_Kodlari.txt`) & NATO NCAGE Codification Docket
  * Executive Identity, Residence & Clean Criminal Record Dossier
* **`Sunumlar/` 💼 (Pitch Decks, Financials & Master Plans):**
  * `Master_Pitch_Deck_TR.pdf` & `Master_Pitch_Deck_EN.pdf` (with `.md` source)
  * `Executive_One_Pager_EN.pdf` (with `.md` source)
  * `Ioniq5_Fotografli_Master_Plan_TR.pdf` & `Ioniq5_Photo_Master_Plan_EN.pdf` (Single Authoritative Master)
  * Targeted Pitch Decks: NATO NIF, Revo Capital, Workup, Inveo, Finberg, Bilişim Vadisi, Dubai Challenge
  * `Cap_Table.csv` & `Finansal_Model_ve_Cap_Table.pdf`
  * `Robotaksi_Operasyon_Modeli.md` & `.pdf`
  * `Organizasyon_Yapisi.pdf` & `Murat_Furkan_Bayram_CV.pdf`
* **`Basvurular/` 🌍 (Grant Tracking & Application Dossiers):**
  * `Takip_Rehberi_2026.md` & `Takip_Rehberi_2026.pdf` (88+ Global & Domestic Applications Registry)
  * `ASELSAN_Axcelerate_Basvuru_Paketi.zip` (Submitted Candidate Supplier Package)
  * `Malta_Enterprise_Application_Dossier.md` & `.pdf` (€1.5M Tech Grant)
  * `NATO_DIANA_Application_Dossier.md` & `.pdf`
  * `Z_Fellows_Interview_Master_Guide.md` & `Emergent_Ventures_Proposal.docx`
  * `Singapur_GIA_Basvuru_Onayi.png`
* **`Medya/` 🎬 (Media Assets, Vehicle Photography & Demonstration Videos):**
  * High-resolution official logos and master corporate banners
  * Crunchbase verified organization and ranking snapshots
  * Real Hyundai Ioniq 5 Level-4 retrofit photo suite (`Ioniq5_Foto_1..7.png`, `Ioniq5_On_Capraz.png`, `Ioniq5_Tavan_LiDAR.png`)
  * Single master demonstration videos: `Robotaksi_Demo.mp4`, `Zafer_Bayrami.mp4`, `Master_Edit.mp4`
  * Official Press Release: `Basin_Bulteni_ASELSAN.pdf`

---

## ⛔ Absolute Prohibitions
1. ❌ NO dumping of files onto `Desktop` (`C:\Users\Murat\Desktop`) or the project root.
2. ❌ NO nested duplicate folders (e.g. `Trustia/Trustia/`).
3. ❌ NO duplicate file copies scattered across folders — adhere strictly to single authoritative masters.
4. ❌ NO mixing of web platform code into autonomy core or vice versa.
5. ❌ NEVER break the 100% pass rate of the 1,301 automated test suite.
6. ❌ MAINTAIN enterprise corporate aesthetic: Avoid playful, informal, or non-defense styling.
