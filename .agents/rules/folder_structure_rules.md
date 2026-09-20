# TRUSTIA DEVELOPER & AGENT WORKING PRINCIPLES

> [!NOTE]
> Core rules for all AI models, agentic workflows, and contributors interacting with the Trustia workspace.
> Focus: High engineering velocity, zero bloat, and GitHub-first development.

---

## 🎯 5 CORE WORKING PRINCIPLES

### 1. 3 ARCHITECTURAL DOMAINS
All workspace files belong exclusively to one of 3 folders:
* **`01_Trustia_Otonom_Yazilim_Core/`**: Autonomy stack, algorithms, simulation, CLI tools, and 1,301 automated tests.
* **`02_Trustia_Web_Platformu/`**: Next.js 16 production web application (`website/`).
* **`Kurumsal/`**: Consolidated corporate records (`Belgeler/`, `Sunumlar/`, `Basvurular/`, `Medya/`).
* Never drop loose files onto the `Desktop` or the workspace root.

### 2. GITHUB-FIRST (NO UNNECESSARY WEBSITE BLOAT)
* **Do NOT modify or deploy the live website (`trustia.com.tr`) for every minor grant application or routine update.**
* Committing and pushing to GitHub (`git push origin main`) is completely sufficient.
* Live website changes are reserved for major verified milestones requested explicitly by the founder.

### 3. ZERO DUPLICATE FILES & CLEAN NAMING
* Every document or asset must have a single authoritative Master location.
* Never duplicate identical files across multiple folders.
* Never leave temporary files (`test_*`, `_kopya`, `_yeni`) in the repository.

### 4. VERIFIED FACTS & GOVERNANCE INTEGRITY
* Zero tolerance for fabricated metrics or false claims.
* Founding equity and roles:
  * **Murat Furkan Bayram**: Founder & CEO / Systems Architect (80% Equity).
  * **Doğukan Bayram**: Co-Founder & Operations (20% Equity).
  * **Denizcan Özcan**: Lead Hardware & Integration Engineer.

### 5. FAILSAFE AUTOMOTIVE SAFETY (ASIL-D)
* The 5ms human override, 200ms hardware watchdog, and E-Stop breakers inside `01_Trustia_Otonom_Yazilim_Core` must never be bypassed or weakened.
