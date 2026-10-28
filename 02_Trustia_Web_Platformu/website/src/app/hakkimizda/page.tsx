"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import {
  ArrowLeft,
  ShieldCheck,
  ArrowRight,
  Terminal,
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function AboutPage() {
  const { lang } = useLanguage();

  const specs = [
    { label: lang === "tr" ? "Fikri Mülkiyet & Sermaye" : "IP Custody & Equity", value: lang === "tr" ? "%100 Milli & Bağımsız (Murat Furkan Bayram)" : "100% Sovereign & Proprietary" },
    { label: lang === "tr" ? "Yazılım Envanteri" : "Codebase Inventory", value: lang === "tr" ? "203 Dosya / 31.400+ Satır (C++20 • Python • ROS 2)" : "203 Files / 31,400+ Lines (C++20 • Python • ROS 2)" },
    { label: lang === "tr" ? "Otomatik Doğrulama" : "Automated Verification", value: lang === "tr" ? "1.324 Çekirdek + 21 SDK Testi = 1.345 Test (%100 Başarı)" : "1,324 Core + 21 SDK Tests = 1,345 Tests (100% Pass)" },
    { label: lang === "tr" ? "Emniyet & Regülasyon" : "Safety & Homologation", value: "ISO 26262 ASIL-D • IEEE 2846 • AB 2022/1426" },
    { label: lang === "tr" ? "Konumlandırma (GNSS-Denied)" : "Localization (GNSS-Denied)", value: lang === "tr" ? "3D LiDAR NDT SLAM • PTP Deskewing • 4.2 cm" : "3D LiDAR NDT SLAM • PTP Deskewing • 4.2 cm" },
    { label: lang === "tr" ? "Planlama & Kontrol" : "Planning & Control", value: "Hybrid A* • Frenet Lattice • MPC • Lanelet2" },
    { label: lang === "tr" ? "Araç Arayüzü & Siber Zırh" : "Actuation & Cyber Shield", value: "100 Hz CAN-FD • UN R155 IDPS • UN R156 SUMS" },
    { label: lang === "tr" ? "Savunma Tedarikçi Kütüğü" : "Defense Supplier Registry", value: "ASELSAN (#0050569) & STM Savunma" },
    { label: lang === "tr" ? "Küresel Patent Güvencesi" : "Global Patent Defense", value: "OIN 2.0 Lisansiyesi (#f1e44576)" },
  ];

  const pillars = [
    {
      num: "01",
      title: lang === "tr" ? "Deterministik Karar, Frenet Kafes & MPC Kontrol" : "Deterministic Decision, Frenet Lattice & MPC Control",
      tag: "HYBRID A* • FRENET • MPC",
      desc: lang === "tr"
        ? "Kestirilemez ve kapalı kutu derin öğrenme modelleri yerine; her senaryoda önceden simüle edilebilen Hybrid A*, Frenet (s, d) 5. derece sarsıntı-optimal (jerk-optimal) kafes planlayıcı, Lanelet2 trafik kural motoru ve Kayan Ufuklu Model Öngörülü Kontrol (MPC) kullanıyoruz. Yolcu ve yaya güvenliği yapay zeka halüsinasyonlarına bırakılamaz."
        : "Engineered on mathematically provable trajectory planning models rather than unpredictable black-box heuristics. Utilizing deterministic Hybrid A*, Frenet quintic jerk-optimal lattice planning, Lanelet2 rule enforcement, and Receding-Horizon MPC."
    },
    {
      num: "02",
      title: lang === "tr" ? "ISO 26262 ASIL-D, IEEE 2846 RSS & SOTIF Emniyeti" : "ISO 26262 ASIL-D, IEEE 2846 RSS & SOTIF Safety",
      tag: "5ms OVERRIDE • IEEE 2846 RSS",
      desc: lang === "tr"
        ? "ASIL-D fonksiyonel emniyet, IEEE 2846 RSS matematiksel takip/yanal güvenlik zarfı ve ISO 21448 SOTIF sınır denetçisi bir arada çalışır. Sürücünün direksiyon (2.5 Nm) veya fren müdahalesinde sistemi 5 ms içinde devreden çıkarır; 50 ms Watchdog aşımında ise 1.5 m/s² kontrollü sağa çekme (MRM) ve 5G/WebRTC Teleoperasyon devrini tetikler."
        : "Combines ASIL-D functional safety, IEEE 2846 RSS mathematical safety envelopes, and ISO 21448 SOTIF ODD monitoring. Yields chassis control within 5ms upon 2.5 Nm driver intervention or executes 1.5 m/s² MRM pullover on 50ms watchdog timeout."
    },
    {
      num: "03",
      title: lang === "tr" ? "100 Hz CAN-FD, UN R155 IDPS & UN R156 SUMS OTA" : "100 Hz CAN-FD, UN R155 IDPS & UN R156 SUMS OTA",
      tag: "100 Hz HAL • UN R155/R156/R157",
      desc: lang === "tr"
        ? "Donanım soyutlama katmanımız (HAL); Hyundai E-GMP (Ioniq 5), SAIC Maxus MIFA 7 ve taktik şasilere standart 100 Hz CAN-FD üzerinden sıfır çekirdek kod değişikliğiyle entegre olur. UN R155 siber saldırı tespit sistemi (IDPS), UN R156 güvenli OTA güncelleme (SUMS/RXSWIN) ve UN R157 DSSAD/EDR kriptografik kara kutu standartlarını barındırır."
        : "Our hardware abstraction layer (HAL) interfaces with Hyundai Ioniq 5, SAIC Maxus MIFA 7, and tactical platforms via 100 Hz CAN-FD with UN R155 CAN IDPS, UN R156 SUMS OTA management, and UN R157 DSSAD/EDR black-box logging."
    },
    {
      num: "04",
      title: lang === "tr" ? "GNSS-Denied 3D LiDAR SLAM & IEEE 1588v2 PTP" : "GNSS-Denied 3D LiDAR SLAM & IEEE 1588v2 PTP",
      tag: "3D NDT SLAM • 400Hz ESKF • PTP",
      desc: lang === "tr"
        ? "Şehir içi tüneller, kapalı otoparklar, gökdelen kanyonları veya elektronik harp sahalarında uydu sinyali kesilse dahi; IEEE 1588v2 PTP donanım zaman senkronizasyonu, 3D LiDAR hareket bükülmesi düzeltme (deskewing), 3D NDT SLAM ve 400 Hz ESKF IMU füzyonu ile 4.2 cm hassasiyetle kesintisiz görev icra eder."
        : "Operational through tunnels, dense urban canyons, and electronic countermeasure zones. IEEE 1588v2 PTP time sync, LiDAR motion deskewing, 3D NDT registration, and 400 Hz ESKF IMU fusion maintain 4.2 cm localization accuracy without GNSS."
    }
  ];

  const domains = [
    {
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
      title: lang === "tr" ? "Şehir İçi Seviye 4 Robotaksi Filoları" : "Urban Level-4 Robotaxi Fleets",
      desc: lang === "tr"
        ? "Binek ve hafif ticari elektrikli araçlar (Hyundai Ioniq 5, SAIC Maxus MIFA 7) için tasarlanan 20 modüllü otonom sürüş beyni; 1 Aralık 2024 Resmî Gazete (AB 2022/1426) Tam Otonom Araçların Tip Onayı Yönetmeliği, UN R155/R156/R157, kabin/BMS emniyet kilidi, eHMI ve siren koridoru standartlarına tam uyumludur."
        : "20-module commercial Robotaxi platform engineered for passenger EVs under EU 2022/1426, UN ECE R155/R156/R157, cabin/BMS interlock, and ISO/TR 23049 eHMI standards."
    },
    {
      tag: lang === "tr" ? "SAVUNMA VE GÜVENLİK" : "DEFENSE & TACTICAL",
      title: lang === "tr" ? "Taktik İnsansız Kara Araçları (İKA)" : "Tactical Unmanned Ground Vehicles (UGV)",
      desc: lang === "tr"
        ? "Milli savunma sanayii ekosistemimiz (ASELSAN & STM) için tasarlanan çift kullanımlı (dual-use) modülümüz; hafif, orta ve ağır sınıf taktik İKA'lara GNSS-Denied otonom intikal, konvoy takibi, sınır devriyesi ve sürü (swarm) zekası kazandırır."
        : "Dual-use autonomy stack delivering GNSS-denied patrol, convoy following, and multi-agent swarm consensus to light, medium, and heavy tactical ground vehicles."
    },
    {
      tag: lang === "tr" ? "ENDÜSTRİ VE LOJİSTİK" : "INDUSTRY & LOGISTICS",
      title: lang === "tr" ? "Ağır Hizmet, Maden ve Liman Otonomisi" : "Heavy Logistics, Mining & Seaports",
      desc: lang === "tr"
        ? "Açık maden ocakları, havalimanı apronları, intermodal liman terminalleri ve lojistik merkezlerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır kamyon, çekici ve otonom yük taşıyıcı (AGV) yazılım çözümleri."
        : "24/7 autonomous fleet operations across open-pit mines, airport aprons, container shipping terminals, and heavy distribution hubs."
    }
  ];

  const credentials = [
    {
      org: "ASELSAN A.Ş. Onaylı Tedarikçi Kütüğü",
      role: lang === "tr" ? "Onaylı Savunma Sanayii Yazılım & Otonomi Tedarikçisi" : "Approved Defense Software & Autonomy Supplier",
      id: "Firma Kodu: #0050569 • SAP: FZQHEXGFMTJU",
      desc: lang === "tr"
        ? "ASELSAN A.Ş. Tedarikçi Kütüğü'ne #0050569 firma kodu, FZQHEXGFMTJU SAP numarası ve 0050569CCE941FD1A49FCEFB9B7BE7D6 takip kodu ile otonom sistemler ve gömülü yazılım geliştirme alanında resmen kayıtlıyız."
        : "Formally registered in the ASELSAN Inc. Approved Supplier Registry (#0050569, SAP: FZQHEXGFMTJU, Tracking: 0050569CCE941FD1A49FCEFB9B7BE7D6) for autonomous systems and software engineering."
    },
    {
      org: "STM Savunma Teknolojileri Mühendislik ve Ticaret A.Ş.",
      role: lang === "tr" ? "Aday Tedarikçi Kütüğü & Savunma Ekosistemi" : "Registered Candidate Supplier & Defense Ecosystem",
      id: "STM Tedarikçi Sistemi • Otonom Kara Sistemleri",
      desc: lang === "tr"
        ? "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı (SSB) iştiraki STM Savunma Teknolojileri A.Ş. resmi tedarikçi portalında otonom sürüş, sürü zekası ve gömülü yazılım aday tedarikçisi olarak kayıtlıdır."
        : "Registered candidate supplier within STM Defense Technologies Inc. for autonomous ground navigation, swarm intelligence, and embedded software."
    },
    {
      org: "Open Invention Network (OIN 2.0)",
      role: lang === "tr" ? "Küresel Patent Savunma Paktı Lisansiyesi" : "Global Patent Non-Aggression Community Licensee",
      id: "Lisans No: f1e445769a9934114db095c4f5430a0e749d8201",
      desc: lang === "tr"
        ? "Google, IBM, Sony, Toyota, SUSE ve Red Hat tarafından desteklenen pakt kapsamında Trustia; 4.000'den fazla küresel kuruluşa karşı Linux ve Seviye-4 otonomi çekirdeğinde tam patent dokunulmazlığı kazanmıştır."
        : "Bilateral executed license conferring patent immunity across 4,000+ participating international corporations covering Linux and Level-4 autonomy software."
    },
    {
      org: "Teknopark İstanbul, İTO BTM & YTÜ Yıldız Teknopark",
      role: lang === "tr" ? "Derin Teknoloji Kuluçka & Ar-Ge Ekosistemi" : "Deep-Tech Incubation & R&D Campuses",
      id: "Cube Incubation (HASAT 2026) • BTM Fulya • YTÜ Teknopark",
      desc: lang === "tr"
        ? "Teknopark İstanbul Cube Incubation Ön Kuluçka Girişimi (6 Aylık Protokol & HASAT 2026), İstanbul Ticaret Odası BTM Fulya Derin Teknoloji Kampüsü yerleşik girişimcisi ve YTÜ Yıldız Teknopark ekosistem başvurusu sahibidir."
        : "Incubated at Teknopark Istanbul Cube Incubation (HASAT 2026), resident entrepreneur at Istanbul Chamber of Commerce BTM Fulya Deep-Tech Campus, and applicant at YTU Yildiz Technopark."
    },
    {
      org: "Avrupa Komisyonu & EIT Urban Mobility",
      role: lang === "tr" ? "AB Katılımcı Sicili & Kentsel Mobilite Ortaklığı" : "European Commission PIC & EIT Innovation Partner",
      id: "EU PIC: 861711529 • Partner ID: CUS15554",
      desc: lang === "tr"
        ? "Avrupa Komisyonu Katılımcı Kayıt Sicili (Participant Register - Horizon Europe) nezdinde 861711529 PIC kodu ile onaylıdır ve EIT Urban Mobility (CUS15554) kentsel mobilite partneridir."
        : "Validated under the European Commission Participant Register (PIC: 861711529) and registered partner of EIT Urban Mobility (CUS15554)."
    },
    {
      org: "KOSGEB & BTK Resmi Sertifikasyonları",
      role: lang === "tr" ? "İleri Girişimci & Savunma Sanayii Yapay Zeka Sertifikası" : "Advanced Entrepreneur & Defense AI Certification",
      id: "KOSGEB: KSB01UGE0115153370 • BTK: L2zPtN4X1ZJ",
      desc: lang === "tr"
        ? "T.C. Sanayi ve Teknoloji Bakanlığı KOSGEB İleri Girişimci Sertifikası (KSB01UGE0115153370) ve BTK Akademi Savunma Sanayii & Yapay Zeka Sertifikasyonu (L2zPtN4X1ZJ) ile tescillidir."
        : "Certified under Ministry of Industry and Technology KOSGEB Advanced Entrepreneurship (KSB01UGE0115153370) and BTK Defense Industry & AI Certification (L2zPtN4X1ZJ)."
    }
  ];

  return (
    <main className="min-h-screen bg-gradient-to-b from-[#1c1813] via-[#28221a] to-[#1c1813] text-[#f5efe6] font-sans selection:bg-[#E4F80D] selection:text-black pt-28 sm:pt-36 pb-20 relative overflow-hidden">
      <Navbar />

      {/* Ambient Tactical Sand/Gold Glow */}
      <div className="absolute top-0 inset-x-0 h-[600px] bg-[radial-gradient(ellipse_at_top,rgba(229,214,188,0.10),transparent_70%)] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 lg:px-12 space-y-16 sm:space-y-24">

        {/* 1. Executive Split Hero Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start pb-12 border-b border-[#E5D6BC]/15">
          
          {/* Left Column: Breadcrumb, Main Title, Core Vision (7 Cols) */}
          <div className="lg:col-span-7 space-y-5">
            <div className="flex items-center gap-2 text-xs font-mono text-[#E5D6BC]/70">
              <Link href="/" className="hover:text-[#E5D6BC] flex items-center gap-1 transition-colors">
                <ArrowLeft className="w-3.5 h-3.5" />
                <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
              </Link>
              <span>/</span>
              <span className="text-[#E5D6BC] font-semibold">{lang === "tr" ? "KURUMSAL" : "CORPORATE"}</span>
              <span>/</span>
              <span className="text-[#d6cebf]">{lang === "tr" ? "HAKKIMIZDA" : "ABOUT US"}</span>
            </div>

            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#E5D6BC]/10 border border-[#E5D6BC]/25 text-[#E5D6BC] text-[11px] font-mono tracking-wider uppercase">
              <ShieldCheck className="w-3.5 h-3.5 text-[#E5D6BC]" />
              <span>{lang === "tr" ? "MİLLİ ÇİFT AMAÇLI OTONOMİ MİMARİSİ • 203 DOSYA / 31.400+ SATIR" : "SOVEREIGN DUAL-USE AUTONOMY CORE • 203 FILES / 31,400+ LOC"}</span>
            </div>

            <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-snug">
              Trustia AI <br />
              <span className="text-[#E5D6BC] font-semibold block sm:inline">
                {lang === "tr" ? "Seviye-4 Otonom Sürüş ve Robotaksi Yazılım Çekirdeği" : "Level-4 Autonomous Driving & Robotaxi Stack"}
              </span>
            </h1>

            <p className="text-[#d6cebf] text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Trustia AI; şehir içi ticari Robotaksi filoları ve GPS sinyalinin kesildiği zorlu harekat sahalarında görev yapan İnsansız Kara Araçları (İKA) için sıfırdan geliştirilmiş, yabancı kapalı kutu kütüphanelere bağımlı olmayan 31.400+ satırlık Seviye-4 otonom sürüş yazılım çekirdeği ve kapalı kutu (.pyc) B2B SDK sunan bağımsız bir derin teknoloji şirketidir."
                : "Trustia AI is an independent deep-tech autonomy company engineering a deterministic 31,400+ line Level-4 autonomous driving software core and closed-box (.pyc) B2B SDK for urban Robotaxi fleets and GPS-denied tactical ground robotics."}
            </p>

            {/* Quick Accreditation Badges Row */}
            <div className="flex flex-wrap items-center gap-2 pt-2 text-[10px] font-mono">
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🛡️ ASELSAN (#0050569 / SAP: FZQHEXGFMTJU)
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🇹🇷 STM Savunma Tedarikçi Kütüğü
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🚀 Teknopark İstanbul • İTO BTM • YTÜ Teknopark
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🛡️ OIN Lisansiyesi (#f1e44576)
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🇪🇺 AB PIC (861711529) &amp; EIT (CUS15554)
              </span>
            </div>
          </div>

          {/* Right Column: Executive Specification Dossier (5 Cols) */}
          <div className="lg:col-span-5 p-5 sm:p-6 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/25 space-y-4 shadow-xl">
            <div className="flex items-center justify-between border-b border-[#E5D6BC]/15 pb-3">
              <div className="flex items-center gap-2">
                <Terminal className="w-4 h-4 text-[#E5D6BC]" />
                <span className="font-mono text-xs font-semibold text-[#E5D6BC] uppercase tracking-wider">
                  {lang === "tr" ? "SİSTEM ÖZELLİKLERİ VE KİMLİK" : "EXECUTIVE SPECIFICATIONS"}
                </span>
              </div>
              <span className="px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-800 text-emerald-400 text-[10px] font-mono font-semibold">
                v4.4 ENTERPRISE
              </span>
            </div>

            <div className="space-y-2.5 font-mono text-xs divide-y divide-[#E5D6BC]/10">
              {specs.map((s, idx) => (
                <div key={idx} className="pt-2.5 first:pt-0 flex items-center justify-between gap-4">
                  <span className="text-[#E5D6BC]/75 text-[11px] shrink-0">{s.label}</span>
                  <span className="text-[#f5efe6] font-semibold text-right text-[11px] truncate">{s.value}</span>
                </div>
              ))}
            </div>
          </div>

        </div>

        {/* 2. Corporate Heritage & Sovereign Code Narrative (Editorial 2-Column) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
          <div className="lg:col-span-4 space-y-2 lg:sticky lg:top-28">
            <span className="text-[11px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold block">
              // 01 KURULUŞ VE VİZYON
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Neden Bağımsız, Özgün Bir Otonomi Çekirdeği?" : "Why Sovereign, Zero-Dependency Autonomy?"}
            </h2>
            <p className="text-xs text-[#d6cebf]/80 leading-relaxed font-sans pt-1">
              {lang === "tr"
                ? "Dışa bağımlı otonomi sistemlerinin taşıdığı ambargo ve güvenlik risklerine karşı milli mühendislik cevabı."
                : "A decisive engineering response against foreign black-box dependencies, cloud tracking, and sudden supply chain sanctions."}
            </p>
          </div>

          <div className="lg:col-span-8 space-y-4 text-xs sm:text-sm text-[#d6cebf] leading-relaxed font-sans">
            <p>
              {lang === "tr"
                ? "Küresel otomotiv ve savunma endüstrisi köklü bir paradigma değişiminden geçmektedir. Direksiyonu, freni ve karar mekanizmasını devralan otonom sürüş yazılımları, modern araçların en stratejik bileşeni haline gelmiştir. Ancak günümüzde pazara sunulan yabancı otonomi kitlerinin büyük bölümü; kapalı kutu algoritmalar, öngörülemeyen kara kutu yapay zeka modelleri ve sürekli yabancı bulut sunucu bağımlılığı barındırmaktadır."
                : "The global automotive and defense industries are undergoing a fundamental transformation. Autonomous driving software has emerged as the definitive core of modern mobility. However, most commercial autonomy platforms rely heavily on closed-source black-box models, external cloud telemetry, and opaque decision heuristics."}
            </p>
            <p>
              {lang === "tr"
                ? "Bu bağımlılık; araç üreticilerini (OEM) ve filo operatörlerini beklenmedik ambargolar, uzaktan lisans iptalleri, telemetri sızıntıları ve operasyonel felç riskleriyle karşı karşıya bırakmaktadır. Türkiye'nin ve iş ortaklarımızın bu alanda tam egemen olabilmesi için dışa bağımlılığı sıfıra indiren bir mimari vazgeçilmez bir zorunluluktur."
                : "This dependency exposes vehicle manufacturers (OEMs) and commercial operators to sudden supply chain sanctions, licensing revocations, telemetry data leaks, and critical operational vulnerabilities. Total software sovereignty is non-negotiable."}
            </p>
            <p>
              {lang === "tr"
                ? "Trustia AI; Kurucu ve Sistem Mimarı Murat Furkan Bayram (%100 Tek Pay Sahibi) liderliğinde İstanbul merkezli olarak, fikri mülkiyeti bütünüyle yerli sermayeye ait deterministik bir otonomi çekirdeği geliştirme kararıyla kurulmuştur. Toplam 203 dosya ve 31.400'ü aşkın satırdan oluşan özgün C++20, Python 3.12 ve ROS 2 Humble mimarimiz; yabancı hiçbir kapalı kütüphaneye dayanmaksızın 1.324 çekirdek testi ve 21 kapalı kutu SDK testiyle (%100 başarı, 0 hata) doğrulanmış olup, 1 Aralık 2024 Resmî Gazete (AB 2022/1426) Tam Otonom Araçların Tip Onayı Yönetmeliği'nin tüm 20 mühendislik kriterini eksiksiz karşılamaktadır."
                : "Trustia AI was established in Istanbul by Founder & Systems Architect Murat Furkan Bayram (100% Equity) with complete proprietary source code custody. Comprising 203 files and over 31,400 lines of original C++20, Python 3.12, and ROS 2 Humble architecture, validated across 1,324 core tests and 21 SDK tests (1,345 tests total) (100% pass), our stack fulfills all 20 international Level-4 and EU 2022/1426 homologation criteria."}
            </p>
          </div>
        </div>

        {/* 3. Four Core Engineering Pillars */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start pt-8 border-t border-[#E5D6BC]/15">
          <div className="lg:col-span-4 space-y-2 lg:sticky lg:top-28">
            <span className="text-[11px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold block">
              // 02 MÜHENDİSLİK MİMARİSİ
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "4 Temel Mühendislik İlkesi" : "4 Engineering Pillars"}
            </h2>
            <p className="text-xs text-[#d6cebf]/80 leading-relaxed font-sans pt-1">
              {lang === "tr"
                ? "Güvenliği olasılıklara bırakmayan, matematiksel olarak doğrulanabilir deterministik kontrol temelleri."
                : "Verifiable mathematical safety guarantees engineered for real-time automotive execution."}
            </p>
          </div>

          <div className="lg:col-span-8 divide-y divide-white/10">
            {pillars.map((item, idx) => (
              <div key={idx} className="py-6 first:pt-0 last:pb-0 space-y-2">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <span className="font-mono text-xs text-[#E5D6BC] font-bold">{item.num}</span>
                    <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                      {item.title}
                    </h3>
                  </div>
                  <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-[#E5D6BC]/15">
                    {item.tag}
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-[#d6cebf] leading-relaxed font-sans pl-7">
                  {item.desc}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* 4. Dual-Use Applications (Sleek Minimal 3-Column) */}
        <div className="space-y-6 pt-8 border-t border-[#E5D6BC]/15">
          <div className="space-y-1">
            <span className="text-[11px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold block">
              // 03 UYGULAMA ALANLARI
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Çift Kullanımlı (Dual-Use) Teknoloji Yaklaşımı" : "Dual-Use Technology Applications"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
            {domains.map((d, idx) => (
              <div key={idx} className="p-6 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 space-y-3 flex flex-col justify-between">
                <div className="space-y-2">
                  <span className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
                    {d.tag}
                  </span>
                  <h3 className="text-base font-bold text-white tracking-tight">
                    {d.title}
                  </h3>
                  <p className="text-xs text-[#d6cebf] leading-relaxed font-sans">
                    {d.desc}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 5. Institutional Credibility & Accreditations */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start pt-8 border-t border-[#E5D6BC]/15">
          <div className="lg:col-span-4 space-y-2 lg:sticky lg:top-28">
            <span className="text-[11px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold block">
              // 04 AKREDİTASYONLAR VE GÜVENCE
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Savunma, Devlet, AB ve Patent Paktı Tescilleri" : "Defense, State, EU & Patent Registry"}
            </h2>
            <p className="text-xs text-[#d6cebf]/80 leading-relaxed font-sans pt-1">
              {lang === "tr"
                ? "Trustia AI; bağımsız mühendisliğini ASELSAN ve STM savunma kütükleri, Teknopark İstanbul, İTO BTM, AB araştırma ağları ve küresel patent koruma paktlarıyla kurumsal güvence altına almıştır."
                : "Certified under ASELSAN and STM defense supplier registries, Teknopark Istanbul, ITO BTM, European Commission bodies, and global patent alliances."}
            </p>
          </div>

          <div className="lg:col-span-8 space-y-4">
            {credentials.map((c, idx) => (
              <div key={idx} className="p-5 sm:p-6 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 space-y-2">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1">
                  <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                    {c.org}
                  </h3>
                  <span className="font-mono text-[10px] text-[#E5D6BC] px-2 py-0.5 rounded bg-[#18140f] border border-[#E5D6BC]/20 shrink-0 self-start sm:self-auto">
                    {c.id}
                  </span>
                </div>
                <div className="text-[11px] font-mono text-emerald-400 font-semibold">
                  {c.role}
                </div>
                <p className="text-xs text-slate-300 leading-relaxed font-sans pt-1">
                  {c.desc}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* 6. Executive OEM Partnership Call to Action */}
        <div className="p-8 sm:p-10 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="space-y-1.5 max-w-xl">
            <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Otonomi Projenizi Birlikte Hayata Geçirelim" : "Deploy Level-4 Autonomy on Your Fleet"}
            </h3>
            <p className="text-xs text-[#d6cebf] leading-relaxed">
              {lang === "tr"
                ? "Robotaksi filoları, kapalı kutu (.pyc) B2B Değerlendirme SDK'sı, OEM lisanslama süreçleri ve teknik şartnameler için doğrudan mühendislik heyetimizle iletişime geçebilirsiniz."
                : "For Robotaxi fleet deployment, closed-box (.pyc) B2B Evaluation SDKs, OEM licensing frameworks, and technical blueprints, connect directly with our engineering leadership."}
            </p>
          </div>

          <div className="flex items-center gap-3 shrink-0">
            <Link
              href="/iletisim/"
              className="px-5 py-2.5 rounded-lg bg-[#E5D6BC] hover:bg-white text-[#14120c] font-bold text-xs font-mono uppercase tracking-wider transition-all inline-flex items-center gap-2 shadow-lg"
            >
              <span>{lang === "tr" ? "İletişime Geçin" : "Contact"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>

            <Link
              href="/politika/oin-lisans/"
              className="px-4 py-2.5 rounded-lg bg-white/5 hover:bg-white/10 border border-[#E5D6BC]/15 text-slate-300 hover:text-white font-mono text-xs tracking-wider transition-all"
            >
              <span>{lang === "tr" ? "Politikalar" : "Policies"}</span>
            </Link>
          </div>
        </div>

      </div>

      <Footer />
    </main>
  );
}
