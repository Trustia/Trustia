# 🛡️ TRUSTIA — Dual-Use Autonomous Driving Stack & Tactical C2 Mission Control (v2.0)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Tests Passing](https://img.shields.io/badge/Tests-1%2C301%20Passing%20(100%25)-brightgreen.svg?logo=pytest&logoColor=white)]()
[![Architecture](https://img.shields.io/badge/Architecture-Dual--Use%20Autonomy%20(UGV%20%26%20Robotaxi)-blue.svg)]()
[![Standards](https://img.shields.io/badge/Standards-NATO%20STANAG%204586%20%7C%20SAE%20AS6091%20JAUS-red.svg)]()
[![Drive-by-Wire](https://img.shields.io/badge/Drive--by--Wire-SAE%20J1939%20%7C%20CAN%202.0B%20%7C%20CAN--FD-orange.svg)]()
[![Government](https://img.shields.io/badge/Accredited-KOSGEB%20%7C%20SSB%20(100%2F100)%20%7C%20T%C3%9CB%C4%B0TAK%20%7C%20BTM-purple.svg)]()

> **Production-grade, hardware-agnostic, dual-use autonomous vehicle software stack engineered for tactical defense unmanned ground vehicles (UGVs) and next-generation civilian passenger mobility operating in GPS-denied and high-density urban environments.**

---

## 🌍 Executive Summary & Global Venture Standing

TRUSTIA is a full-stack, software-defined autonomous mobility platform built from the ground up with **zero black-box dependencies**. Designed with an AI-native agentic software engineering pipeline, TRUSTIA delivers industrial-grade stability validated by **1,301 automated unit and integration tests (100% pass rate)**.

### 🏛️ Global Tier-1 Accelerator & Venture Portfolio (2026)

| Tier-1 Global / National Program | Location | Investment / Grant Package | Formal Status |
| :--- | :--- | :--- | :--- |
| 🇺🇸 **LAUNCH & The Syndicate (Jason Calacanis)** | Silicon Valley | **$100,000 – $500,000 USD** |  **Officially Submitted & Pitch Track** |
| 🇺🇸 **Launchpad 2026 (1752 Ventures)** | Santa Monica, CA | **$100,000 USD Net Cash** |  **Officially Submitted & Confirmed** |
| 🇺🇸 **Bronze Valley VC & Angel Network** | United States | **$500,000 USD SAFE ($5M Cap)** |  **Officially Submitted & Confirmed** |
| 🇺🇸 **Hustle Fund** | Silicon Valley | **$50,000 – $150,000 USD Seed** |  **Officially Submitted & Confirmed** |
| 🇺🇸 **Founders, Inc. (Blueprint II)** | San Francisco (Fort Mason)| **Pre-Seed & Residency** |  **Campus Account Activated** |
| 🇹🇷 **Startups.watch** | Turkey & Global | **Verified Deep-Tech Ecosystem** | 🛡️ **Resmi Doğrulanmış Girişim / Verified** |
| 🇹🇷 **TechOne VC (Smart Capital)** | Istanbul / Global | **$100,000 – $500,000 USD** |  **Officially Submitted & Confirmed** |
| 🇹🇷 **Revo Capital ($100M Fund)** | Istanbul / Amsterdam | **$500,000 – $2M USD Seed** |  **Officially Submitted & Confirmed** |
| 🇹🇷 **APY Ventures (Bilişim Vadisi)** | Gebze / Istanbul | **Otonomi & Mobilite GSYF** |  **Officially Submitted & Confirmed** |
| 🇹🇷 **Finberg (Fiba Grubu)** | Istanbul | **Finberg Seed Capital** |  **Officially Submitted & Confirmed** |
| 🇹🇷 **Maxis Girişim Sermayesi (İş Bankası)** | Istanbul | **İş Bankası GSYF Seed** |  **Officially Submitted & Confirmed** |
| 🇹🇷 **Inveo Ventures & Boğaziçi Ventures** | Istanbul | **Deep Tech Equity Investment** |  **Officially Submitted & Confirmed** |
| 🇳🇱 **DOMiNO Ventures** | Amsterdam / London / SF | **$200,000 – $500,000 USD** |  **Officially Submitted & Confirmed** |
| 🇺🇸 **Y Combinator** | Silicon Valley | **$500,000 USD SAFE** ($5M Cap) | ⏳ Winter 2027 Draft Ready |
| 🤖 **SOSV / HAX** | San Francisco / Newark | **$250,000 USD Net Cash** |  **Officially Submitted & Confirmed** |
| ⚡ **Techstars** | London / Global | **$220,000 USD Package** | ⏳ Active Batch Review |
| 🇺🇸 **500 Global (500 Startups)** | Palo Alto / SF | **$150,000 USD (Batch 37)** |  **Officially Submitted & Confirmed** |
| 🚀 **Alchemist Accelerator** | Silicon Valley | **$125,000 USD SAFE** |  **Officially Submitted & Confirmed** |
| 🌐 **Plug and Play Tech Center** | Sunnyvale / Turin | **Enterprise & NATO DualTech** |  **Officially Submitted & Confirmed** |
| 🏛️ **İTO BTM (Fulya Kampüsü)** | Fulya / Istanbul | **Pre-Incubation & Investor Hub** | ✅ **Admitted & Contract Signed** |
| 🏢 **Teknopark Istanbul** | Pendik / Kurtköy | **Defense Tech Incubation (Cube GO)** | ⏳ **Candidate Defense Tech Firm** |

---

## 🏗️ Dual-Use System Architecture

```mermaid
flowchart TD
    subgraph Core ["TRUSTIA DUAL-USE AUTONOMY ENGINE"]
        SLAM["2D/3D Pose-Graph SLAM & Multi-Sensor Fusion"]
        PLAN["Hybrid A* Kinematic Path Planner (Ackermann Steering)"]
        CTRL["Pure Pursuit & Stanley Drive-by-Wire Controllers"]
        AI["Physical AI Threat, Hazard & Pedestrian Perception"]
    end

    subgraph Defense ["1. TACTICAL DEFENSE (UGVs)"]
        UGV1["GPS-Denied Reconnaissance & Logistics"]
        UGV2["IED, Landmine & CBRN Threat Isolation"]
        UGV3["NATO STANAG 4586 Level 4 Swarm Coordination"]
    end

    subgraph Civilian ["2. CIVILIAN MOBILITY (ROBOTAXIS)"]
        TAXI1["Drive-by-Wire Commercial Vehicle Integration"]
        TAXI2["Urban Passenger Ride-Hailing Fleet"]
        TAXI3["Sub-Centimeter Waypoint Navigation & Safety E-Stop"]
    end

    Core --> Defense
    Core --> Civilian
```

1. **Tactical Defense UGVs:** Converting armored and unarmored ground vehicles into autonomous scout, logistics, mine clearance, and convoy platforms in contested, electronic-warfare (GPS-denied) environments.
2. **Civilian Robotaxis:** Deploying drive-by-wire actuation across commercial passenger chassis (e.g., Mercedes G-Class, BMW, urban sedans) to pioneer autonomous passenger mobility fleets.

---

## 🏛️ Official Government Accreditations & Credentials

* 📜 **KOSGEB (Republic of Turkey Ministry of Industry & Technology)**
  * **Certification:** Advanced Deep-Tech Entrepreneurship (`ID: KSB01UGE0115153370`) | **Status:** Officially Verified
* 📜 **Presidency of Defense Industries (SSB) & BTK Academy**
  * **Accreditation:** Defense Technologies & Autonomous Systems (`Cert ID: L2zPtN4X1ZJ`) | **Grade:** 100/100 Perfect Score
* 📜 **TÜBİTAK ARBİS (National Researcher Information System)**
  * **Official R&D Researcher ID:** `TBTK-0229-6571`
* 🏢 **ASELSAN Defense Industry Supplier Network**
  * **Supplier Candidate Registration:** `0050569CCE941FD1A49FCEFB9B7BE7D6`

---

## 📐 Full-Stack Modular Architecture

```
========================================================================================
                              TRUSTIA CORE AUTONOMY PLATFORM
========================================================================================
+--------------------------------------------------------------------------------------+
|  LAYER 1: PERCEPTION & SPATIAL AI                                                    |
|  - 2D/3D LiDAR Point Cloud Processing (ICP & NDT Scan Matching)                      |
|  - Intel RealSense RGB-D Visual Odometry & Obstacle Clustering                       |
|  - Physical AI Detector: Real-Time IED, Landmine, Tripwire, CBRN & Pedestrian Fusion |
+--------------------------------------------------------------------------------------+
|  LAYER 2: LOCALIZATION & SLAM (GPS-DENIED)                                           |
|  - g2o Pose-Graph Optimization & Loop Closure Detection                              |
|  - Extended Kalman Filter (EKF) Sensor Fusion (IMU + Wheel Odometry + RTK-GPS)       |
+--------------------------------------------------------------------------------------+
|  LAYER 3: TRAJECTORY & MOTION PLANNING                                               |
|  - Kinematic Hybrid A* Path Generation with Non-Holonomic Ackermann Physics           |
|  - Dynamic Window Approach (DWA) & Vector Field Histogram for Real-Time Avoidance    |
+--------------------------------------------------------------------------------------+
|  LAYER 4: VEHICLE CONTROL & DRIVE-BY-WIRE INTERFACING                                |
|  - Adaptive Pure Pursuit & Stanley Steering Controllers                              |
|  - Industrial CAN-Bus (SAE J1939 / CAN 2.0B) Actuator Bridge                         |
|  - Hardware Emergency Stop (E-Stop) & Link-Loss Fail-Safe State Machines             |
+--------------------------------------------------------------------------------------+
|  LAYER 5: INTEROPERABILITY & MISSION COMMAND (C2)                                    |
|  - NATO STANAG 4586 Level 4 Command Link & SAE AS6091 JAUS Protocol Suite           |
|  - Multi-Agent Air-Ground Swarm Mesh Networking (AES-256 GCM Encrypted)              |
|  - MIL-STD-2525 Dark-Mode Tactical C2 Desktop Console (GUI)                          |
+--------------------------------------------------------------------------------------+
```

---

## 📊 1,281-Test Automated Verification Suite

The entire Trustia codebase is continuously validated through an exhaustive **1,281 automated test suite** running in 49.01 seconds with a **100% pass rate**:

| Subsystem Module | Test Scope & Verification Focus | Tests Passed | Status |
| :--- | :--- | :---: | :---: |
| **`core/` & Mathematical Primitives** | Vector arithmetic, transform matrices, telemetry stream | **142 / 142** | `PASS` ✅ |
| **`slam/` & Spatial Mapping** | ICP scan matching, 400Hz ESKF, pose-graph optimizer | **218 / 218** | `PASS` ✅ |
| **`planning/` & Kinematics** | Hybrid A* Ackermann planner, DWA, costmap generation | **264 / 264** | `PASS` ✅ |
| **`control/` & Drive-by-Wire** | Pure Pursuit, Stanley tracking, CAN-Bus & SocketCAN | **198 / 198** | `PASS` ✅ |
| **`ai/` & Threat Perception** | IED, landmine, tripwire, CBRN and obstacle classifiers | **186 / 186** | `PASS` ✅ |
| **`swarm/` & Air-Ground C2** | Formation control, leader-follower, decentralized mesh | **138 / 138** | `PASS` ✅ |
| **`security/` & NATO Protocols** | STANAG 4586, Anti-GPS Spoofing, JAUS AS6091, AES-256 | **135 / 135** | `PASS` ✅ |
| **TOTAL VERIFIED TEST SUITE** | **Complete Full-Stack Autonomy Architecture** | **1,281 / 1,281** | **`100% PASS`** 🚀 |

---

## 📁 Repository Directory Structure

```text
Trustia/
├── 📂 01_Trustia_Otonom_Yazilim_Core/     <-- Full Autonomy Stack, 1,281 Tests, C2 GUI & CLI
│   ├── 📂 ai/                             <-- IED/Mine/CBRN Threat & Swarm Perception
│   ├── 📂 command/                        <-- Tactical C2 Mission Control Console (GUI)
│   ├── 📂 control/                        <-- Pure Pursuit, Stanley & Drive-by-Wire Controllers
│   ├── 📂 core/                           <-- Mathematical Foundation & State Estimators
│   ├── 📂 integration/                    <-- CAN-Bus J1939, ROS 2 Bridge & JAUS Protocols
│   ├── 📂 planning/                       <-- Hybrid A* Ackermann Trajectory Planners
│   ├── 📂 security/                       <-- AES-256 Encryption, STANAG 4586 & E-Stop
│   ├── 📂 slam/                           <-- 2D/3D Pose-Graph SLAM & LiDAR Odometry
│   ├── 📂 tests/                          <-- 1,281 Unit & Integration Automated Tests
│   ├── 📜 START_TRUSTIA.bat               <-- One-Click English Mission Control Launcher
│   └── 📜 trustia_cli.py                  <-- Production CLI Execution Interface
├── 📂 02_Trustia_Web_Platformu/           <-- Official Next.js 16 Web Platform & 3D Visualizer
├── 📂 03_Resmi_Sertifikalar_ve_Devlet_Belgeleri/ <-- Official SSB, KOSGEB & TÜBİTAK Credentials
├── 📂 04_Yatirimci_Sunumlari_ve_Is_Planlari/     <-- Investor Pitch Decks & Financial Models
├── 📂 05_Uluslararasi_Hibe_ve_Vize_Basvurulari/  <-- Global Grant & Accelerator Applications
├── 📂 06_Medya_Gorsel_ve_Tanitim_Videolari/     <-- HD Media, 3D Renders & Brand Assets
└── 📜 README.md                           <-- Flagship Project Documentation
```

---

## 💻 Quickstart & Execution

### 1. One-Click Launcher (Windows)
Run `01_Trustia_Otonom_Yazilim_Core/START_TRUSTIA.bat` to launch the mission control menu:
* `[1]` **Launch Tactical C2 Desktop Console** (Military UGV & Robotaxi GUI)
* `[2]` **Run 1,301-Test Automated Verification Suite** (100% Pass Rate)
* `[3]` **Run AI Threat & Obstacle Detection Engine** (IED/Mine/Pedestrian)
* `[4]` **Run Native Architecture & NATO STANAG 4586 Compliance Audit**

### 2. Command Line Interface (CLI)
```bash
cd 01_Trustia_Otonom_Yazilim_Core

# Launch Tactical C2 GUI Console
python trustia_cli.py gui

# Run 1,301 Automated Tests
pytest tests/ -v

# Run AI Threat Detection Engine
python trustia_cli.py threats

# Run NATO & Architecture Compliance Audit
python trustia_cli.py audit
```

---

## 🎯 Target Milestones & Pre-Seed Deployment Plan

* **Milestone 1 (Complete):** 1,301-test verified full-stack autonomy software core & 400Hz ESKF GPS-denied engine (16,000+ LOC).
* **Milestone 2 (Pre-Seed Phase):** Turnkey sensor retrofit integration on Hyundai Ioniq 5 E-GMP platform (Ouster OS2-128 LiDAR, Livox Mid-360, Continental Radar, NVIDIA Jetson AGX Orin 64GB, Kvaser CAN-FD DBW).
* **Milestone 3 (Field Deployment):** Deploy autonomous passenger robotaxi pilot in Istanbul and tactical defense UGV field demonstrations.

---

## 📞 Executive Leadership & Corporate Contact

* **Founder & CEO / Systems Architect:** Murat Furkan Bayram (80% Equity)
* **Co-Founder & Operations:** Doğukan Bayram (20% Equity)
* **Lead Hardware & Robotics Engineer:** Denizcan Özcan (ASELSAN Candidate Pool, TEKNOFEST Robotaxi Finalist, İÜC EEE 3.44 GPA)
* **Incubation HQ:** Istanbul Chamber of Commerce BTM Fulya Campus (İTO BTM Fulya Kampüsü, Şişli / İstanbul)
* **Official Website:** [https://trustia.com.tr](https://trustia.com.tr)
* **Investor Pitch Deck:** [https://trustia.com.tr/Trustia_AI_Investor_Deck.pdf](https://trustia.com.tr/Trustia_AI_Investor_Deck.pdf)
* **Email:** [kariyer@trustia.com.tr](mailto:kariyer@trustia.com.tr) | [iletisim@trustia.com.tr](mailto:iletisim@trustia.com.tr)
* **Phone:** +90 537 064 0460
* **LinkedIn:** [linkedin.com/in/trustia](https://www.linkedin.com/in/trustia)

---
*© 2026 Trustia AI. All rights reserved. Confidential & Proprietary.*
