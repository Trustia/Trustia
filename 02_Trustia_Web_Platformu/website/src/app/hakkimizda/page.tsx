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
  ArrowRight
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function AboutPage() {
  const { lang } = useLanguage();

  const keyMetrics = [
    {
      value: "16.000+",
      label: lang === "tr" ? "Özgün Kaynak Kod" : "Lines Sovereign Code",
      sub: lang === "tr" ? "C++20 & Python Çekirdek" : "C++20 & Python Stack"
    },
    {
      value: "1.301 / 1.301",
      label: lang === "tr" ? "Doğrulanmış Test" : "Automated Tests",
      sub: lang === "tr" ? "%100 Başarı Oranı" : "100% Pass Rate"
    },
    {
      value: "5 ms",
      label: lang === "tr" ? "Acil Devralma" : "Hardware Override",
      sub: lang === "tr" ? "ISO 26262 ASIL-D" : "ASIL-D Fail-Safe"
    },
    {
      value: "%100",
      label: lang === "tr" ? "Milli Mülkiyet" : "Sovereign IP",
      sub: lang === "tr" ? "Sıfır Dış Bağımlılık" : "Zero Foreign Dependency"
    }
  ];

  const pillars = [
    {
      icon: Cpu,
      title: lang === "tr" ? "Deterministik Karar ve Kontrol Çekirdeği" : "Deterministic Decision Core",
      subtitle: lang === "tr" ? "Matematiksel Olarak Kanıtlanabilir Otonomi" : "Mathematically Verifiable Safety",
      desc: lang === "tr"
        ? "Kestirilemez ve kapalı kutu derin öğrenme modelleri yerine; her trafik senaryosunda önceden simüle edilebilen, matematiksel sınırları tanımlı Hybrid A*, Voronoi geometri yörüngeleri ve Stanley kinematik kontrolcü mimarisi kullanıyoruz. Sistemimiz, yolcuların ve yayaların güvenliğini şansa bırakmayan deterministik bir mühendislik temeline dayanır."
        : "Engineered on mathematically provable trajectory planning models rather than unpredictable black-box heuristics. Utilizing deterministic Hybrid A*, Voronoi spatial decomposition, and Stanley geometric tracking controllers to ensure verifiable passenger and pedestrian safety."
    },
    {
      icon: ShieldCheck,
      title: lang === "tr" ? "ISO 26262 ASIL-D Fonksiyonel Emniyet" : "ISO 26262 ASIL-D Functional Safety",
      subtitle: lang === "tr" ? "5 Milisaniye Donanımsal Sürücü Önceliği" : "5ms Hardware Takeover Override",
      desc: lang === "tr"
        ? "Otomotiv endüstrisinin en yüksek emniyet seviyesi olan ASIL-D standartlarına uygun olarak tasarlanan mimarimiz; fiziksel emniyet sürücüsünün direksiyon simidine veya fren pedalına uygulayacağı en ufak müdahalede (2.5 Nm üzeri tork) sistemi 5 milisaniye içinde devreden çıkararak şasi kontrolünü anında sürücüye iade eder."
        : "Engineered under automotive safety integrity level ASIL-D. A hard-interrupt hardware relay instantly yields chassis control to the human driver within 5 milliseconds upon detecting steering torque exceeding 2.5 Nm or brake pedal actuation."
    },
    {
      icon: Zap,
      title: lang === "tr" ? "Evrensel Donanım Bağımsızlığı & CAN-FD" : "Hardware-Agnostic CAN-FD Bridge",
      subtitle: lang === "tr" ? "Her Şasiye 100 Hz Tak-Çalıştır Entegrasyon" : "100 Hz Plug-and-Play DBW Interface",
      desc: lang === "tr"
        ? "Fiziksel araç üreticilerine bağımlı kalmaksızın geliştirilen donanım soyutlama katmanımız (HAL); Hyundai E-GMP (Ioniq 5), SAIC Maxus MIFA 7, TOGG, ticari minibüsler ve taktik zırhlı araç şasilerine standart 100 Hz CAN-FD ve ROS 2 Humble köprüleri üzerinden sıfır kod değişikliğiyle entegre olur."
        : "Our hardware abstraction layer (HAL) interfaces with Hyundai E-GMP (Ioniq 5), SAIC Maxus MIFA 7, commercial shuttles, and military wheeled platforms via standardized 100 Hz CAN-FD and ROS 2 protocols with zero kernel code alterations."
    },
    {
      icon: Lock,
      title: lang === "tr" ? "GPS Olmayan Sahalarda Seyrüsefer (GNSS-Denied)" : "GNSS-Denied Navigation Architecture",
      subtitle: lang === "tr" ? "Uydu Sinyali Kesilse Dahi Kesintisiz Otonomi" : "Centimeter Precision Under Jamming",
      desc: lang === "tr"
        ? "Şehir içi tüneller, kapalı otoparklar, yüksek gökdelen kanyonları veya çatışma alanlarındaki elektronik harp karartmalarında dahi; araç üzerindeki 3D LiDAR NDT haritalama ve 400 Hz ESKF IMU sensör füzyonu ile uyduya ihtiyaç duymadan 4.2 santimetre yanal hassasiyetle rotasını korur."
        : "Operational through tunnels, dense skyscraper canyons, and electronic countermeasure environments. In-vehicle 3D LiDAR NDT registration and 400 Hz ESKF IMU fusion maintain uninterrupted centimeter trajectory tracking without relying on GNSS signals."
    }
  ];

  const domains = [
    {
      icon: Car,
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
      title: lang === "tr" ? "Şehir İçi Seviye 4 Robotaksi Filoları" : "Urban Level-4 Robotaxi Fleets",
      desc: lang === "tr"
        ? "Binek ve hafif ticari elektrikli araçlar için tasarlanan Robotaksi yazılım çekirdeğimiz; kentsel kavşaklar, trafik ışıkları, dur-kalk trafiği ve yaya geçitlerinde tam bağımsız seyrüsefer sunar. 1 Aralık 2024 ADS Yönetmeliği ve UN ECE R157 kara kutu (DSSAD/EDR) standartlarına tam uyumludur."
        : "Commercial Robotaxi platform engineered for passenger EVs, navigating complex intersections, traffic lights, dynamic pedestrian crossings, and dense traffic under UN ECE R157 and ADS automotive homologation standards."
    },
    {
      icon: Shield,
      tag: lang === "tr" ? "SAVUNMA VE GÜVENLİK" : "DEFENSE & TACTICAL",
      title: lang === "tr" ? "Taktik İnsansız Kara Araçları (İKA)" : "Tactical Unmanned Ground Vehicles (UGV)",
      desc: lang === "tr"
        ? "Milli savunma sanayii ekosistemimiz için tasarlanan çift kullanımlı (dual-use) modülümüz; hafif, orta ve ağır sınıf taktik İKA'lara otonom intikal, konvoy takibi, sınır devriyesi ve sürü (swarm) zekası yeteneği kazandırır. Askeri JAUS ve STANAG veri köprüleri ile tam uyumludur."
        : "Dual-use autonomy stack delivering autonomous patrol, convoy following, and multi-agent swarm consensus to light, medium, and heavy tactical ground robots with military JAUS and secure datalink compliance."
    },
    {
      icon: Building,
      tag: lang === "tr" ? "ENDÜSTRİ VE LOJİSTİK" : "INDUSTRY & LOGISTICS",
      title: lang === "tr" ? "Ağır Hizmet, Maden ve Liman Otonomisi" : "Heavy Logistics, Mining & Seaports",
      desc: lang === "tr"
        ? "Açık maden ocakları, intermodal liman terminalleri ve lojistik merkezlerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır kamyon, çekici ve otonom yük taşıyıcı (AGV) yazılım çözümleri."
        : "24/7 autonomous fleet operations across open-pit mines, container shipping terminals, and heavy distribution hubs, removing human exposure from high-hazard operational zones."
    }
  ];

  const institutionalTrust = [
    {
      badge: "KÜRESEL PATENT BARIŞI",
      badgeEn: "GLOBAL PATENT DEFENSE",
      title: "Open Invention Network (OIN)",
      id: "Lisans No: f1e445769a9934114db095c4f5430a0e749d8201",
      idEn: "License ID: f1e445769a9934114db095c4f5430a0e749d8201",
      desc: lang === "tr"
        ? "Google, IBM, Sony, Toyota, SUSE ve Red Hat tarafından desteklenen küresel patent savunma paktına 'Community Licensee' statüsünde tarafız. Linux, ROS 2 ve otonom araç yazılım çekirdeğimiz 4.000'den fazla küresel teknoloji kuruluşuna karşı karşılıklı patent dokunulmazlığı güvencesi altındadır."
        : "Official Community Licensee of the Open Invention Network (OIN LLC, New York), securing reciprocal patent immunity and global intellectual property defense covering our Linux, ROS 2, and autonomy software stacks across 4,000+ participating international companies."
    },
    {
      badge: "MİLLİ SAVUNMA EKOSİSTEMİ",
      badgeEn: "NATIONAL DEFENSE ECOSYSTEM",
      title: "ASELSAN & STM Tedarikçi Portalları",
      id: "Tedarikçi Kodu: #0050569 • STM Ekosistem 2026",
      idEn: "Supplier Code: #0050569 • STM Ecosystem 2026",
      desc: lang === "tr"
        ? "ASELSAN Tedarikçi Kütüğü'ne 'Yazılım Geliştirme' alanında kayıtlı girişim statüsündeyiz. STM (Savunma Teknolojileri Mühendislik) girişimcilik ekosisteminde yer alarak Türk Savunma Sanayii standartlarında derin teknoloji üretme yeterliliğimizi tescilledik."
        : "Officially registered in the ASELSAN Defense Supplier Registry (#0050569) under Software Engineering and accredited within the STM Defense Technologies deep-tech entrepreneurial ecosystem."
    },
    {
      badge: "AVRUPA BİRLİĞİ AKREDİTASYONU",
      badgeEn: "EUROPEAN UNION PARTNERSHIP",
      title: "Avrupa Komisyonu & EIT Urban Mobility",
      id: "EU PIC: 861711529 • Partner ID: CUS15554",
      idEn: "EU PIC: 861711529 • Partner ID: CUS15554",
      desc: lang === "tr"
        ? "Avrupa Komisyonu Katılımcı Kayıt Sicili (Participant Register) nezdinde tüzel kişilik onayına sahibiz. Avrupa İnovasyon ve Teknoloji Enstitüsü (EIT) Urban Mobility resmi inovasyon ortağı olarak Avrupa genelinde akıllı ulaşım konsorsiyumlarında yer alıyoruz."
        : "Formally validated under the European Commission Participant Register (EU PIC: 861711529) and an active Innovation Partner of EIT Urban Mobility (Partner ID: CUS15554), collaborating across European autonomous transport initiatives."
    },
    {
      badge: "AR-GE VE KURUMSAL ALTYAPI",
      badgeEn: "R&D & INSTITUTIONAL SEED",
      title: "İTO BTM, KOSGEB & TÜBİTAK ARBİS",
      id: "Fulya Kampüsü • KOSGEB İleri Girişimci • TBTK-ARBİS",
      idEn: "Fulya Campus • KOSGEB Advanced Entrepreneur • ARBIS",
      desc: lang === "tr"
        ? "İstanbul Ticaret Odası Bilgiyi Ticarileştirme Merkezi (BTM Fulya Kampüsü) bünyesinde Ar-Ge faaliyetlerimizi sürdürmekteyiz. KOSGEB İleri Girişimcilik tescili ve TÜBİTAK ARBİS Milli Araştırmacı sicili ile kurumsal güvenilirliğimiz denetlenmektedir."
        : "Headquartered at Istanbul Chamber of Commerce BTM (Fulya Incubation Campus), backed by KOSGEB Advanced Entrepreneurship certification and verified under the TUBITAK ARBIS National Researcher Registry."
    }
  ];

  return (
    <main className="min-h-screen bg-[#06080b] text-white font-sans selection:bg-slate-700 selection:text-white pt-28 sm:pt-36 pb-20">
      <Navbar />

      <div className="max-w-6xl mx-auto px-4 sm:px-8 space-y-16 sm:space-y-24">

        {/* 1. Executive Hero Header */}
        <div className="space-y-6 max-w-4xl">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-white flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-slate-200 font-semibold">{lang === "tr" ? "KURUMSAL" : "CORPORATE"}</span>
            <span>/</span>
            <span className="text-slate-400">{lang === "tr" ? "HAKKIMIZDA" : "ABOUT US"}</span>
          </div>

          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
            <ShieldCheck className="w-3.5 h-3.5 text-slate-400" />
            <span>{lang === "tr" ? "KURUMSAL PROFİL & MÜHENDİSLİK MİSYONU" : "CORPORATE PROFILE & ENGINEERING CHARTER"}</span>
          </div>

          <h1 className="text-3xl sm:text-5xl md:text-6xl font-extrabold text-white tracking-tight leading-[1.15]">
            Trustia AI <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-200 via-slate-400 to-slate-500 font-semibold">
              {lang === "tr" ? "Milli Deterministik Otonomi Mimarisi" : "Sovereign Autonomous Systems"}
            </span>
          </h1>

          <p className="text-slate-300 text-sm sm:text-base md:text-lg leading-relaxed font-normal">
            {lang === "tr"
              ? "Trustia AI; şehir içi ticari Robotaksi filoları ve GPS sinyalinin bulunmadığı zorlu harekat sahalarında görev yapan İnsansız Kara Araçları (İKA) için sıfırdan geliştirilmiş, donanım bağımsız Seviye-4 otonom sürüş yazılım çekirdeği sunan bağımsız bir derin teknoloji şirketidir."
              : "Trustia AI is a sovereign deep-tech autonomy company engineering deterministic Level-4 autonomous driving software for urban commercial Robotaxi fleets and GPS-denied tactical defense robotics."}
          </p>

          {/* Key Metrics Strip */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-white/10">
            {keyMetrics.map((m, idx) => (
              <div key={idx} className="p-4 rounded-xl bg-[#0b0e14] border border-white/10 space-y-1">
                <div className="text-xl sm:text-2xl md:text-3xl font-extrabold text-white tracking-tight font-mono">
                  {m.value}
                </div>
                <div className="text-xs font-semibold text-slate-300">
                  {m.label}
                </div>
                <div className="text-[10px] text-slate-500 font-mono">
                  {m.sub}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 2. Corporate Heritage & Sovereign Code Narrative */}
        <div className="p-6 sm:p-10 rounded-3xl bg-[#0a0d13] border border-white/10 space-y-8">
          <div className="space-y-2">
            <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
              {lang === "tr" ? "KURULUŞ HİKAYESİ VE EGEMEN YAZILIM VİZYONU" : "ORIGIN & SOVEREIGN SOFTWARE CHARTER"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr"
                ? "Neden Dışa Bağımsız, Özgün Bir Otonomi Çekirdeği?"
                : "Why Sovereign, Zero-Dependency Autonomy?"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-10 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
            <div className="space-y-4">
              <p>
                {lang === "tr"
                  ? "Küresel otomotiv ve savunma endüstrisi köklü bir paradigma değişiminden geçmektedir. Direksiyonu ve karar mekanizmasını devralan otonom sürüş yazılımları, modern araçların en kritik bileşeni haline gelmiştir. Ancak günümüzde sunulan yabancı otonomi kitlerinin büyük bölümü; kapalı kutu algoritmalar, öngörülemeyen kara kutu yapay zeka modelleri ve sürekli yabancı bulut sunucu bağımlılığı barındırmaktadır."
                  : "The global automotive and defense sectors are undergoing a profound paradigm shift. Autonomous driving software has emerged as the definitive core of modern mobility. However, most commercial autonomy platforms rely heavily on closed-source black-box models, external cloud telemetry, and opaque decision heuristics."}
              </p>
              <p>
                {lang === "tr"
                  ? "Bu durum araç üreticilerini (OEM) ve filo operatörlerini ciddi ambargo, lisans iptali, veri sızıntısı ve uzaktan müdahale tehditleriyle baş başa bırakmaktadır. Türkiye'nin ve iş ortaklarımızın bu alanda bağımsız olabilmesi için dışa bağımlılığı sıfıra indiren bir mimari zorunluluktur."
                  : "This dependency exposes vehicle manufacturers (OEMs) and commercial operators to sudden supply chain sanctions, licensing revocations, telemetry data leaks, and critical operational vulnerabilities. Total software sovereignty is non-negotiable."}
              </p>
            </div>

            <div className="space-y-4">
              <p>
                {lang === "tr"
                  ? "Trustia AI; İstanbul merkezli olarak, fikri mülkiyeti bütünüyle şahsıma ve yerli sermayeye ait, sıfırdan inşa edilmiş deterministik bir otonomi çekirdeği geliştirme kararıyla kurulmuştur. Kaynak kodlarımız hiçbir yabancı kapalı kutu kütüphaneye dayanmaz."
                  : "Trustia AI was established in Istanbul with 100% sovereign equity and proprietary source code custody. Every line of our autonomy stack has been engineered from the ground up without foreign proprietary black boxes."}
              </p>
              <p>
                {lang === "tr"
                  ? "16.000'i aşkın satırdan oluşan özgün mimarimiz; 1.301 otomatik test hattı ile doğrulanmış olup, sivil karayollarında Robotaksi filolarından zorlu coğrafyalardaki askeri robotlara kadar her türlü araç şasisine tak-çalıştır entegre edilebilmektedir."
                  : "Comprising over 16,000 lines of original C++ and Python architecture, validated across 1,301 automated verification test suites, our stack interfaces plug-and-play across passenger EVs and tactical platforms alike."}
              </p>
            </div>
          </div>
        </div>

        {/* 3. Four Core Engineering Pillars */}
        <div className="space-y-6">
          <div className="space-y-2">
            <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
              {lang === "tr" ? "TEKNOLOJİK YETKİNLİKLER & MÜHENDİSLİK İLKELERİ" : "TECHNICAL EXCELLENCE & PRINCIPLES"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "4 Temel Mühendislik Sütunumuz" : "4 Engineering Pillars"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {pillars.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div
                  key={idx}
                  className="p-6 sm:p-8 rounded-2xl bg-[#0a0d13] border border-white/10 space-y-4 hover:border-white/20 transition-all group"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 group-hover:text-white transition-colors">
                      <Icon className="w-5 h-5" />
                    </div>
                    <div>
                      <span className="text-[10px] font-mono text-slate-400 uppercase tracking-wider block">
                        {item.subtitle}
                      </span>
                      <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                        {item.title}
                      </h3>
                    </div>
                  </div>

                  <p className="text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
                    {item.desc}
                  </p>
                </div>
              );
            })}
          </div>
        </div>

        {/* 4. Dual-Use Applications (Civilian, Defense, Heavy Industry) */}
        <div className="space-y-6">
          <div className="space-y-2">
            <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
              {lang === "tr" ? "UYGULAMA SAHALARI & ÇİFT KULLANIMLI MİMARİ" : "OPERATIONAL DOMAINS & DUAL-USE CAPABILITY"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Teknoloji Nerede ve Nasıl Çalışıyor?" : "Deployment Environments"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {domains.map((d, idx) => {
              const Icon = d.icon;
              return (
                <div
                  key={idx}
                  className="p-6 rounded-2xl bg-[#0a0d13] border border-white/10 space-y-4 flex flex-col justify-between"
                >
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-300">
                        <Icon className="w-5 h-5" />
                      </div>
                      <span className="px-2 py-0.5 rounded bg-white/5 border border-white/10 text-[9px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                        {d.tag}
                      </span>
                    </div>

                    <h3 className="text-base font-bold text-white tracking-tight">
                      {d.title}
                    </h3>

                    <p className="text-xs text-slate-400 leading-relaxed font-sans">
                      {d.desc}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. Institutional Credibility & Accreditations Narrative */}
        <div className="space-y-6">
          <div className="space-y-2">
            <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
              {lang === "tr" ? "KURUMSAL GÜVENİLİRLİK & ULUSLARARASI AKREDİTASYONLAR" : "INSTITUTIONAL TRUST & GOVERNANCE"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Devlet, AB ve Küresel Ekosistem Onaylarımız" : "Institutional Accreditations & Registry"}
            </h2>
            <p className="text-xs sm:text-sm text-slate-400 max-w-2xl leading-relaxed">
              {lang === "tr"
                ? "Trustia AI; bağımsız mühendisliğini devletimizin savunma kütükleri, Avrupa Birliği araştırma ağları ve küresel patent koruma paktlarıyla tescilleyerek kurumsal güvence altına almıştır."
                : "Trustia AI operates with institutional credibility certified under national defense registries, European Commission research bodies, and global patent defense alliances."}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {institutionalTrust.map((item, idx) => (
              <div
                key={idx}
                className="p-6 sm:p-7 rounded-2xl bg-[#0a0d13] border border-white/10 space-y-3 flex flex-col justify-between"
              >
                <div className="space-y-2.5">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono text-slate-400 font-semibold uppercase tracking-wider">
                      {lang === "tr" ? item.badge : item.badgeEn}
                    </span>
                    <span className="inline-flex items-center gap-1 text-[10px] font-mono text-emerald-400 bg-emerald-950/60 border border-emerald-800 px-2 py-0.5 rounded-full font-semibold">
                      <Check className="w-3 h-3" />
                      <span>{lang === "tr" ? "Onaylı" : "Certified"}</span>
                    </span>
                  </div>

                  <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                    {item.title}
                  </h3>

                  <div className="text-[11px] font-mono text-slate-400 py-1 px-2.5 rounded bg-black/40 border border-white/5 inline-block">
                    {lang === "tr" ? item.id : item.idEn}
                  </div>

                  <p className="text-xs text-slate-300 leading-relaxed font-sans pt-1">
                    {item.desc}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 6. Physical Infrastructure, Proving Grounds & Executive CTA */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          {/* Headquarters Card (6 cols) */}
          <div className="lg:col-span-6 p-6 sm:p-8 rounded-2xl bg-[#0a0d13] border border-white/10 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <div className="flex items-center gap-2 text-slate-400 font-mono text-xs uppercase font-semibold">
                <Building className="w-4 h-4 text-slate-300" />
                <span>{lang === "tr" ? "YÖNETİM VE AR-GE MERKEZİ" : "HEADQUARTERS & R&D"}</span>
              </div>
              <div className="text-lg font-bold text-white">İTO BTM Kampüsü</div>
              <p className="text-xs text-slate-300 leading-relaxed font-sans">
                {lang === "tr"
                  ? "İstanbul Ticaret Odası Bilgiyi Ticarileştirme Merkezi (BTM Fulya Kampüsü, Şişli / İstanbul). Çekirdek yazılım mimarisi, simülasyon sunucuları ve teleoperasyon merkezi."
                  : "Istanbul Chamber of Commerce Bilgiyi Ticarileştirme Merkezi (BTM Fulya Campus, Sisli / Istanbul). Core autonomy stack engineering and fleet teleoperation."}
              </p>
            </div>
            <div className="pt-3 border-t border-white/5 text-[11px] font-mono text-slate-400">
              İstanbul, Türkiye
            </div>
          </div>

          {/* Proving Grounds Card (6 cols) */}
          <div className="lg:col-span-6 p-6 sm:p-8 rounded-2xl bg-[#0a0d13] border border-white/10 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <div className="flex items-center gap-2 text-slate-400 font-mono text-xs uppercase font-semibold">
                <MapPin className="w-4 h-4 text-slate-300" />
                <span>{lang === "tr" ? "SAHA TEST VE PİST SAHALARI" : "TESTING & PROVING GROUNDS"}</span>
              </div>
              <div className="text-lg font-bold text-white">Bilişim Vadisi & Hacettepe Teknokent</div>
              <p className="text-xs text-slate-300 leading-relaxed font-sans">
                {lang === "tr"
                  ? "Gebze Bilişim Vadisi 1.5 km kapalı test pisti ve Hacettepe Teknokent otonom sürüş test sahası. Gerçek araç üzerinde CAN-FD aktüatör, SLAM ve dinamik engel testleri."
                  : "Gebze Bilisim Vadisi 1.5 km proving grounds and Hacettepe Teknokent autonomous track. Drive-by-Wire verification and dynamic obstacle avoidance trials."}
              </p>
            </div>
            <div className="pt-3 border-t border-white/5 text-[11px] font-mono text-slate-400">
              Gebze & Ankara, Türkiye
            </div>
          </div>
        </div>

        {/* 7. Executive Compliance & Contact Box */}
        <div className="p-8 sm:p-10 rounded-3xl bg-gradient-to-b from-[#0e121a] to-[#07090d] border border-white/10 space-y-6">
          <div className="space-y-2 max-w-2xl">
            <span className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
              {lang === "tr" ? "İŞ BİRLİĞİ VE OEM ENTEGRASYONU" : "PARTNERSHIPS & OEM INTEGRATION"}
            </span>
            <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr"
                ? "Otonomi Projenizi Birlikte Hayata Geçirelim"
                : "Deploy Level-4 Autonomy on Your Fleet"}
            </h3>
            <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
              {lang === "tr"
                ? "Robotaksi filoları, araç üreticisi (OEM) lisanslama süreçleri, teknik şartnameler ve yatırım görüşmeleri için doğrudan mühendislik heyetimizle iletişime geçebilirsiniz."
                : "For Robotaxi fleet deployment, OEM licensing frameworks, technical specifications, and strategic investment dialogues, connect directly with our engineering leadership."}
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-4 pt-2">
            <Link
              href="/iletisim/"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white hover:bg-slate-200 text-slate-950 font-bold text-xs font-mono uppercase tracking-wider transition-all"
            >
              <span>{lang === "tr" ? "İletişime Geçin" : "Contact Engineering"}</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href="/politika/oin-lisans/"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-slate-300 hover:text-white font-mono text-xs tracking-wider transition-all"
            >
              <FileText className="w-4 h-4 text-slate-400" />
              <span>{lang === "tr" ? "Kurumsal Politikaları İncele" : "Review Corporate Policies"}</span>
            </Link>
          </div>
        </div>

      </div>

      <Footer />
    </main>
  );
}
