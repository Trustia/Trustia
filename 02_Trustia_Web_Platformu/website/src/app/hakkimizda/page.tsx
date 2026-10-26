"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import {
  ArrowLeft,
  Shield,
  Cpu,
  Target,
  Award,
  CheckCircle2,
  Lock,
  Radio,
  MapPin,
  Building,
  Zap,
  Activity,
  Layers,
  ChevronRight,
  ShieldCheck,
  Scale,
  Compass,
  FileText,
  Car,
  Globe,
  Check,
  ArrowRight,
  ExternalLink,
  Terminal,
  Clock
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function AboutPage() {
  const { lang } = useLanguage();

  const specs = [
    { label: lang === "tr" ? "Fikri Mülkiyet & Sermaye" : "IP Custody & Equity", value: lang === "tr" ? "%100 Milli & Bağımsız" : "100% Sovereign & Proprietary" },
    { label: lang === "tr" ? "Yazılım Çekirdeği" : "Core Architecture", value: "C++20 • Python 3.12 • ROS 2" },
    { label: lang === "tr" ? "Otomatik Doğrulama" : "Automated Verification", value: lang === "tr" ? "1.307 / 1.307 Test (%100 Başarı)" : "1,307 / 1,307 Unit Tests (100%)" },
    { label: lang === "tr" ? "Fonksiyonel Emniyet" : "Safety Integrity", value: "ISO 26262 ASIL-D • 5ms Override" },
    { label: lang === "tr" ? "Konumlandırma (GNSS-Denied)" : "Localization (GNSS-Denied)", value: lang === "tr" ? "3D LiDAR SLAM • 4.2 cm Hassasiyet" : "3D LiDAR SLAM • 4.2 cm Drift" },
    { label: lang === "tr" ? "Araç Arayüzü (DBW)" : "Actuation Interface (DBW)", value: "100 Hz Standart CAN-FD / SecOC" },
    { label: lang === "tr" ? "Savunma Ekosistemi" : "Defense Supplier Registry", value: "ASELSAN & STM (#0050569)" },
    { label: lang === "tr" ? "Küresel Patent Güvencesi" : "Global Patent Defense", value: "OIN Lisansiyesi (#f1e44576)" },
  ];

  const pillars = [
    {
      num: "01",
      title: lang === "tr" ? "Deterministik Karar Çekirdeği" : "Deterministic Decision Core",
      tag: "C++20 & HYBRID A*",
      desc: lang === "tr"
        ? "Kestirilemez ve kapalı kutu derin öğrenme modelleri yerine; her senaryoda önceden simüle edilebilen, matematiksel sınırları tanımlı Hybrid A*, Voronoi geometri yörüngeleri ve Stanley kinematik kontrolcü mimarisi kullanıyoruz. Yolcu ve yaya güvenliği şansa veya yapay zeka halüsinasyonlarına bırakılamaz."
        : "Engineered on mathematically provable trajectory planning models rather than unpredictable black-box heuristics. Utilizing deterministic Hybrid A*, Voronoi spatial decomposition, and Stanley geometric tracking controllers to eliminate algorithmic hallucination."
    },
    {
      num: "02",
      title: lang === "tr" ? "ISO 26262 ASIL-D Fonksiyonel Emniyet" : "ISO 26262 ASIL-D Functional Safety",
      tag: "5ms HARDWARE INTERRUPT",
      desc: lang === "tr"
        ? "Otomotiv endüstrisinin en yüksek güvenlik seviyesi olan ASIL-D standartlarına uygun mimarimiz; fiziksel emniyet sürücüsünün direksiyon veya fren pedalına uygulayacağı en ufak müdahalede (2.5 Nm üzeri tork) sistemi 5 milisaniye içinde devreden çıkararak şasi kontrolünü anında sürücüye iade eder."
        : "Engineered under automotive safety integrity level ASIL-D. A hard-interrupt hardware relay instantly yields chassis control to the human driver within 5 milliseconds upon detecting steering torque exceeding 2.5 Nm or brake pedal actuation."
    },
    {
      num: "03",
      title: lang === "tr" ? "Evrensel Donanım Bağımsızlığı & CAN-FD" : "Hardware-Agnostic CAN-FD Bridge",
      tag: "100 Hz UNIVERSAL HAL",
      desc: lang === "tr"
        ? "Fiziksel araç üreticilerine bağımlı kalmaksızın geliştirilen donanım soyutlama katmanımız (HAL); Hyundai E-GMP (Ioniq 5), SAIC Maxus MIFA 7, TOGG, ticari minibüsler ve zırhlı araç şasilerine standart 100 Hz CAN-FD ve ROS 2 Humble köprüleri üzerinden sıfır kod değişikliğiyle entegre olur."
        : "Our hardware abstraction layer (HAL) interfaces with Hyundai E-GMP (Ioniq 5), SAIC Maxus MIFA 7, commercial shuttles, and military wheeled platforms via standardized 100 Hz CAN-FD and ROS 2 protocols with zero kernel code alterations."
    },
    {
      num: "04",
      title: lang === "tr" ? "GPS Olmayan Sahalarda Seyrüsefer (GNSS-Denied)" : "GNSS-Denied Navigation Architecture",
      tag: "3D LiDAR NDT & 400Hz ESKF",
      desc: lang === "tr"
        ? "Şehir içi tüneller, kapalı otoparklar, yüksek gökdelen kanyonları veya elektronik harp sahalarında uydu sinyali kesilse dahi; araç üzerindeki 3D LiDAR NDT haritalama ve 400 Hz ESKF IMU sensör füzyonu ile uyduya ihtiyaç duymadan 4.2 santimetre yanal hassasiyetle kesintisiz görev icra eder."
        : "Operational through tunnels, dense skyscraper canyons, and electronic countermeasure environments. In-vehicle 3D LiDAR NDT registration and 400 Hz ESKF IMU fusion maintain uninterrupted centimeter trajectory tracking without relying on GNSS signals."
    }
  ];

  const domains = [
    {
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
      title: lang === "tr" ? "Şehir İçi Seviye 4 Robotaksi Filoları" : "Urban Level-4 Robotaxi Fleets",
      desc: lang === "tr"
        ? "Binek ve hafif ticari elektrikli araçlar (Hyundai Ioniq 5, SAIC Maxus MIFA 7) için tasarlanan otonom sürüş beyni; kentsel kavşaklar, trafik ışıkları, dur-kalk trafiği ve dinamik yaya geçitlerinde tam bağımsız çalışır. 1 Aralık 2024 ADS Yönetmeliği ve UN ECE R157 kara kutu (DSSAD/EDR) standartlarına tam uyumludur."
        : "Commercial Robotaxi platform engineered for passenger EVs, navigating complex intersections, traffic lights, dynamic pedestrian crossings, and dense traffic under UN ECE R157 and ADS automotive homologation standards."
    },
    {
      tag: lang === "tr" ? "SAVUNMA VE GÜVENLİK" : "DEFENSE & TACTICAL",
      title: lang === "tr" ? "Taktik İnsansız Kara Araçları (İKA)" : "Tactical Unmanned Ground Vehicles (UGV)",
      desc: lang === "tr"
        ? "Milli savunma sanayii ekosistemimiz için tasarlanan çift kullanımlı (dual-use) modülümüz; hafif, orta ve ağır sınıf taktik İKA'lara otonom intikal, konvoy takibi, sınır devriyesi ve sürü (swarm) zekası kazandırır. Askeri JAUS ve güvenli telemetri hatları ile tam uyumludur."
        : "Dual-use autonomy stack delivering autonomous patrol, convoy following, and multi-agent swarm consensus to light, medium, and heavy tactical ground robots with military JAUS and secure datalink compliance."
    },
    {
      tag: lang === "tr" ? "ENDÜSTRİ VE LOJİSTİK" : "INDUSTRY & LOGISTICS",
      title: lang === "tr" ? "Ağır Hizmet, Maden ve Liman Otonomisi" : "Heavy Logistics, Mining & Seaports",
      desc: lang === "tr"
        ? "Açık maden ocakları, intermodal liman terminalleri ve lojistik merkezlerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır kamyon, çekici ve otonom yük taşıyıcı (AGV) yazılım çözümleri."
        : "24/7 autonomous fleet operations across open-pit mines, container shipping terminals, and heavy distribution hubs, removing human exposure from high-hazard operational zones."
    }
  ];

  const credentials = [
    {
      org: "Open Invention Network (OIN)",
      role: lang === "tr" ? "Küresel Patent Savunma Paktı Lisansiyesi" : "Global Patent Non-Aggression Community Licensee",
      id: "Lisans No: f1e445769a9934114db095c4f5430a0e749d8201",
      desc: lang === "tr"
        ? "Google, IBM, Sony, Toyota, SUSE ve Red Hat tarafından desteklenen pakt kapsamında Trustia; 4.000'den fazla küresel kuruluşa karşı patent dokunulmazlığı kazanmıştır."
        : "Bilateral executed license conferring patent immunity across 4,000+ participating international corporations covering Linux and Level-4 autonomy software."
    },
    {
      org: "ASELSAN & STM Savunma Ekosistemi",
      role: lang === "tr" ? "Kayıtlı Girişim ve Yazılım Tedarikçi Ağı" : "Defense Supplier & Startup Ecosystem Registry",
      id: "Tedarikçi Kodu: #0050569 • STM Ekosistem 2026",
      desc: lang === "tr"
        ? "ASELSAN Tedarikçi Kütüğü'ne 'Yazılım Geliştirme' alanında kayıtlı girişim statüsündeyiz. STM derin teknoloji girişimcilik ekosistemi ve SSB SAYZEK portalı onaylıdır."
        : "Formally registered in the ASELSAN Defense Supplier Registry (#0050569) under Software Engineering and accredited within the STM deep-tech ecosystem."
    },
    {
      org: "Avrupa Komisyonu & EIT Urban Mobility",
      role: lang === "tr" ? "AB Katılımcı Sicili & İnovasyon Ortaklığı" : "European Commission PIC & EIT Innovation Partner",
      id: "EU PIC: 861711529 • Partner ID: CUS15554",
      desc: lang === "tr"
        ? "Avrupa Komisyonu Katılımcı Kayıt Sicili (Participant Register) nezdinde tüzel kişilik onaylıdır. EIT Urban Mobility resmi inovasyon ortağı olarak konsorsiyumlarda yer alır."
        : "Formally validated under the European Commission Participant Register and an active Innovation Partner of EIT Urban Mobility across EU transport projects."
    },
    {
      org: "İTO BTM, KOSGEB & TÜBİTAK ARBİS",
      role: lang === "tr" ? "Kuluçka Yerleşkesi & Milli Araştırmacı Sicili" : "Incubation Campus & National Researcher Registry",
      id: "BTM Fulya Kampüsü • KOSGEB İleri Girişimci • ARBİS",
      desc: lang === "tr"
        ? "İstanbul Ticaret Odası Bilgiyi Ticarileştirme Merkezi (BTM Fulya) bünyesinde yerleşik Ar-Ge faaliyeti; KOSGEB İleri Girişimcilik ve TÜBİTAK ARBİS tescillidir."
        : "Headquartered at Istanbul Chamber of Commerce BTM (Fulya Campus), backed by KOSGEB Advanced Entrepreneurship certification and verified under TUBITAK ARBIS."
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
              <span>{lang === "tr" ? "MİLLİ ÇİFT AMAÇLI OTONOMİ MİMARİSİ" : "SOVEREIGN DUAL-USE AUTONOMY CORE"}</span>
            </div>

            <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-snug">
              Trustia AI <br />
              <span className="text-[#E5D6BC] font-semibold block sm:inline">
                {lang === "tr" ? "Seviye-4 Otonom Sürüş ve Robotaksi Yazılım Çekirdeği" : "Level-4 Autonomous Driving & Robotaxi Stack"}
              </span>
            </h1>

            <p className="text-[#d6cebf] text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Trustia AI; şehir içi ticari Robotaksi filoları ve GPS sinyalinin kesildiği zorlu harekat sahalarında görev yapan İnsansız Kara Araçları (İKA) için sıfırdan geliştirilmiş, yabancı kapalı kutu kütüphanelere bağımlı olmayan Seviye-4 otonom sürüş yazılım çekirdeği sunan bağımsız bir derin teknoloji şirketidir."
                : "Trustia AI is an independent deep-tech autonomy company engineering deterministic Level-4 autonomous driving software for urban commercial Robotaxi fleets and GPS-denied tactical ground robotics with zero foreign black-box dependencies."}
            </p>

            {/* Quick Accreditation Badges Row */}
            <div className="flex flex-wrap items-center gap-2 pt-2 text-[10px] font-mono">
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🇹🇷 ASELSAN & STM Tedarikçi Kütüğü (#0050569)
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🛡️ Open Invention Network Lisansiyesi (#f1e44576)
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🇪🇺 AB Komisyonu PIC (861711529)
              </span>
              <span className="px-2.5 py-1 rounded bg-[#251f17] border border-[#E5D6BC]/20 text-[#E5D6BC]/90 shadow-sm">
                🏛️ İTO BTM Fulya Kampüsü
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
                v2.4 STABLE
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
                ? "Trustia AI; İstanbul merkezli olarak, fikri mülkiyeti bütünüyle yerli sermayeye ait, sıfırdan inşa edilmiş deterministik bir otonomi çekirdeği geliştirme kararıyla kurulmuştur. 16.400'ü aşkın satırdan oluşan özgün C++20 ve Python mimarimiz; yabancı hiçbir kapalı kütüphaneye dayanmaksızın 1.307 otomatik test hattıyla doğrulanmış olup, sivil karayollarında Robotaksi filolarından zorlu coğrafyalardaki taktik savunma robotlarına kadar her türlü araç şasisine tak-çalıştır entegre edilebilmektedir."
                : "Trustia AI was established in Istanbul with 100% sovereign equity and proprietary source code custody. Comprising over 16,400 lines of original C++20 and Python architecture, validated across 1,307 automated verification test suites, our stack interfaces plug-and-play across passenger EVs and tactical platforms alike."}
            </p>
          </div>
        </div>

        {/* 3. Four Core Engineering Pillars (Hairline Separated Specs - No Clunky Box Clutter!) */}
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

        {/* 5. Institutional Credibility & Accreditations (Clean Executive Dossier) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start pt-8 border-t border-[#E5D6BC]/15">
          <div className="lg:col-span-4 space-y-2 lg:sticky lg:top-28">
            <span className="text-[11px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold block">
              // 04 AKREDİTASYONLAR VE GÜVENCE
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Devlet, AB ve Patent Paktı Tescilleri" : "Institutional Credentials & Registry"}
            </h2>
            <p className="text-xs text-[#d6cebf]/80 leading-relaxed font-sans pt-1">
              {lang === "tr"
                ? "Trustia AI; bağımsız mühendisliğini savunma kütükleri, AB araştırma ağları ve küresel patent koruma paktlarıyla kurumsal güvence altına almıştır."
                : "Certified under national defense supplier registries, European Commission bodies, and global patent alliances."}
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

        {/* 6. Physical Infrastructure & Proving Grounds */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-8 border-t border-[#E5D6BC]/15">
          <div className="p-6 sm:p-7 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 space-y-3">
            <div className="flex items-center gap-2 text-[#E5D6BC] font-mono text-xs uppercase font-semibold">
              <Building className="w-4 h-4 text-[#E5D6BC]" />
              <span>{lang === "tr" ? "YÖNETİM VE AR-GE MERKEZİ" : "HEADQUARTERS & R&D"}</span>
            </div>
            <div className="text-base font-bold text-white">İTO BTM Kampüsü</div>
            <p className="text-xs text-[#d6cebf] leading-relaxed font-sans">
              {lang === "tr"
                ? "İstanbul Ticaret Odası Bilgiyi Ticarileştirme Merkezi (BTM Fulya Kampüsü, Şişli / İstanbul). Çekirdek yazılım mimarisi, simülasyon sunucuları ve filo teleoperasyon merkezi."
                : "Istanbul Chamber of Commerce BTM (Fulya Campus, Sisli / Istanbul). Core autonomy stack engineering and fleet teleoperation hub."}
            </p>
          </div>

          <div className="p-6 sm:p-7 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 space-y-3">
            <div className="flex items-center gap-2 text-[#E5D6BC] font-mono text-xs uppercase font-semibold">
              <MapPin className="w-4 h-4 text-[#E5D6BC]" />
              <span>{lang === "tr" ? "SAHA TEST VE PİST SAHALARI" : "PROVING GROUNDS"}</span>
            </div>
            <div className="text-base font-bold text-white">Bilişim Vadisi & Hacettepe Teknokent</div>
            <p className="text-xs text-[#d6cebf] leading-relaxed font-sans">
              {lang === "tr"
                ? "Bilişim Vadisi Gebze 1.5 km kapalı test pisti ve Hacettepe Teknokent otonom sürüş test sahası. Gerçek araç üzerinde CAN-FD aktüatör, SLAM ve dinamik engel testleri."
                : "Bilisim Vadisi Gebze 1.5 km proving grounds and Hacettepe Teknokent autonomous track. Drive-by-Wire verification and dynamic obstacle avoidance trials."}
            </p>
          </div>
        </div>

        {/* 7. Executive OEM Partnership Call to Action */}
        <div className="p-8 sm:p-10 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/15 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="space-y-1.5 max-w-xl">
            <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Otonomi Projenizi Birlikte Hayata Geçirelim" : "Deploy Level-4 Autonomy on Your Fleet"}
            </h3>
            <p className="text-xs text-[#d6cebf] leading-relaxed">
              {lang === "tr"
                ? "Robotaksi filoları, OEM lisanslama süreçleri, teknik şartnameler ve yatırım görüşmeleri için doğrudan mühendislik heyetimizle iletişime geçebilirsiniz."
                : "For Robotaxi fleet deployment, OEM licensing frameworks, and strategic investment dialogues, connect directly with our engineering leadership."}
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
