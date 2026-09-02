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
  User,
  Zap,
  Activity,
  Layers,
  ChevronRight
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function AboutPage() {
  const { lang } = useLanguage();

  const pillars = [
    {
      icon: Cpu,
      title: lang === "tr" ? "16.000+ Satır Özgün Mimari" : "16,000+ Lines Sovereign Code",
      desc: lang === "tr"
        ? "Yabancı kaynak kod veya hazır kapalı kutu kütüphanelere bağımlı olmaksızın, sıfırdan geliştirilmiş deterministik C++ / Python otonomi çekirdeği."
        : "Built from scratch with zero dependency on foreign black-box libraries, engineered for mathematical determinism and real-time execution.",
      stat: "16.000+ Satır"
    },
    {
      icon: Shield,
      title: lang === "tr" ? "1.301 / 1.301 Doğrulanmış Test" : "1,301 Automated Unit Tests",
      desc: lang === "tr"
        ? "SLAM haritalama, Pure Pursuit yol izleme, acil frenleme ve CAN-FD aktüatör hatlarında %100 başarı oranına sahip otomatik test mimarisi."
        : "Rigorous 100% pass rate across SLAM localization, path tracking, obstacle braking, and CAN-FD real-time latency tests.",
      stat: "%100 Başarı"
    },
    {
      icon: Zap,
      title: lang === "tr" ? "Donanım Bağımsızlığı" : "Hardware-Agnostic Core",
      desc: lang === "tr"
        ? "Hyundai E-GMP (Ioniq 5), TOGG, Otokar, Havelsan ve FNSS platformlarına 100 Hz standart CAN-FD / ROS 2 köprüsü ile tak-çalıştır entegrasyon."
        : "Plug-and-play abstraction layer interfacing with Hyundai E-GMP, commercial EVs, and military tactical UGVs via CAN-FD / ROS 2.",
      stat: "Tak-Çalıştır"
    },
    {
      icon: Lock,
      title: lang === "tr" ? "Sıfır Dış Bağımlılık (GPS-Denied)" : "GPS-Denied Navigation",
      desc: lang === "tr"
        ? "Elektronik harp, tüneller veya uydu sinyalinin kesildiği harekat sahalarında 3D LiDAR SLAM ile santimetre hassasiyetinde seyrüsefer."
        : "Centimeter-accurate 3D LiDAR SLAM localization operating independently of satellite signals in contested or indoor environments.",
      stat: "ASIL-D / STANAG"
    }
  ];

  const credentials = [
    {
      org: lang === "tr" ? "T.C. Savunma Sanayii Başkanlığı (SSB)" : "Turkish Defense Industry Agency (SSB)",
      reg: "L2zPtN4X1ZJ",
      type: lang === "tr" ? "100/100 Tam Puan Sertifikasyonu" : "100/100 Perfect Score Certification",
      status: "Resmi Onaylı"
    },
    {
      org: lang === "tr" ? "Startups.watch Girişimcilik Platformu" : "Startups.watch Ecosystem",
      reg: "Ana Sayfa #1",
      type: lang === "tr" ? "Resmi Doğrulanmış Girişim Listesi" : "Verified Deep-Tech Venture",
      status: "Doğrulandı"
    },
    {
      org: lang === "tr" ? "KOSGEB Başkanlığı" : "KOSGEB Entrepreneurship Agency",
      reg: "KSB01UGE0115153370",
      type: lang === "tr" ? "İleri Girişimci Tescili & Ar-Ge Desteği" : "Advanced Entrepreneur Accreditation",
      status: "Tescilli"
    },
    {
      org: lang === "tr" ? "TÜBİTAK ARBİS" : "TÜBİTAK National Researcher Registry",
      reg: "TBTK-0229-6571",
      type: lang === "tr" ? "Milli Araştırmacı Sicil Kaydı" : "National Defense & AI Researcher",
      status: "Aktif Sicil"
    },
    {
      org: lang === "tr" ? "İTO Bilgiyi Ticarileştirme Merkezi (BTM)" : "Istanbul Chamber of Commerce (BTM)",
      reg: "2026-II Sözleşme",
      type: lang === "tr" ? "Fulya Polat Tower Ön Kuluçka Girişimi" : "Fulya Polat Tower Pre-Incubation",
      status: "Yerleşik"
    }
  ];

  return (
    <main className="min-h-screen bg-[#07090d] text-white font-sans selection:bg-slate-700 selection:text-white pt-20 sm:pt-24 pb-16">
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-10 sm:space-y-14">

        {/* 1. Header */}
        <div className="space-y-3 pb-6 border-b border-white/10">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-white flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-slate-200 font-semibold">{lang === "tr" ? "HAKKIMIZDA" : "ABOUT US"}</span>
          </div>

          <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px] font-mono font-medium tracking-wider uppercase">
            <span>{lang === "tr" ? "KURUMSAL PROFİL VE MİSYON" : "CORPORATE PROFILE & MISSION"}</span>
          </div>

          <h1 className="text-2xl sm:text-4xl md:text-5xl font-bold text-white tracking-tight leading-tight">
            Trustia AI <br />
            <span className="text-slate-300 font-semibold">
              {lang === "tr" ? "Milli Deterministik Otonomi Mimarisi" : "Sovereign Autonomous Systems"}
            </span>
          </h1>

          <p className="text-slate-400 text-xs sm:text-sm md:text-base max-w-3xl leading-relaxed">
            {lang === "tr"
              ? "Trustia AI (İstanbul, Türkiye); şehir içi sivil Robotaksi filoları ve GPS sinyalinin bulunmadığı zorlu sahalarda görev yapan İnsansız Kara Araçları (İKA) için Seviye 4 yerli otonom sürüş yazılım çekirdeği geliştiren derin teknoloji şirketidir."
              : "Trustia AI is a deep-tech autonomy company engineering sovereign Level-4 autonomous driving software for commercial Robotaxi fleets and GPS-denied tactical Unmanned Ground Vehicles."}
          </p>
        </div>

        {/* 2. Executive Leadership & Founder Card */}
        <div className="p-6 sm:p-8 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
            <div className="flex items-center gap-3.5">
              <div className="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-200">
                <User className="w-6 h-6" />
              </div>
              <div>
                <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                  {lang === "tr" ? "KURUCU & SİSTEM MİMARI / CEO" : "FOUNDER & AUTONOMOUS SYSTEMS ARCHITECT"}
                </div>
                <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
                  Murat Furkan Bayram
                </h2>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <a
                href="https://www.linkedin.com/in/trustia"
                target="_blank"
                rel="noopener noreferrer"
                className="px-3.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 hover:bg-slate-800 text-xs font-mono transition-colors"
              >
                LinkedIn Profili →
              </a>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
            <div className="lg:col-span-8 space-y-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
              <p>
                {lang === "tr"
                  ? "T.C. Savunma Sanayii Başkanlığı 100/100 tam puan sertifikasyonuna ve KOSGEB İleri Girişimci tesciline sahip otonomi mimarıdır. 16.000 satırlık deterministik otonomi çekirdeğini, 3D LiDAR SLAM motorunu ve 1.301 birim test altyapısını bizzat geliştirmiştir."
                  : "Certified autonomy systems architect with 100/100 perfect score certification from the Turkish Defense Industry Agency and KOSGEB Advanced Entrepreneur accreditation. Architected the 16,000-line deterministic codebase, 3D LiDAR SLAM, and 1,301 automated verification test suites."}
              </p>
              <p className="text-slate-400 text-xs">
                {lang === "tr"
                  ? "İTO Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Polat Tower bünyesinde yerleşik olarak şirketin teknoloji, Ar-Ge ve kurumsal konsorsiyum süreçlerini yönetmektedir."
                  : "Based at the Istanbul Chamber of Commerce (BTM) Fulya Polat Tower campus, leading technology architecture, commercial deployment, and strategic defense partnerships."}
              </p>
            </div>

            {/* Quick Badges Grid */}
            <div className="lg:col-span-4 grid grid-cols-2 gap-2 text-[11px] font-mono">
              <div className="p-3 rounded-lg bg-[#07090d] border border-slate-800">
                <div className="text-slate-500 text-[9px] uppercase">SSB SINAVI</div>
                <div className="font-bold text-white mt-0.5">100 / 100</div>
              </div>
              <div className="p-3 rounded-lg bg-[#07090d] border border-slate-800">
                <div className="text-slate-500 text-[9px] uppercase">KOSGEB</div>
                <div className="font-bold text-white mt-0.5">İleri Girişimci</div>
              </div>
              <div className="p-3 rounded-lg bg-[#07090d] border border-slate-800">
                <div className="text-slate-500 text-[9px] uppercase">STARTUPS.WATCH</div>
                <div className="font-bold text-white mt-0.5">#1 Doğrulandı</div>
              </div>
              <div className="p-3 rounded-lg bg-[#07090d] border border-slate-800">
                <div className="text-slate-500 text-[9px] uppercase">İTO BTM</div>
                <div className="font-bold text-white mt-0.5">Fulya Kampüs</div>
              </div>
            </div>
          </div>

          {/* Core Leadership & Engineering Team Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4 border-t border-slate-800">
            <div className="p-4 rounded-xl bg-[#07090d] border border-slate-800/80 flex items-start gap-3.5">
              <div className="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center text-slate-300 shrink-0">
                <User className="w-5 h-5" />
              </div>
              <div className="space-y-1">
                <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                  {lang === "tr" ? "KURUCU ORTAK & COO / ŞİRKET MÜDÜRÜ" : "CO-FOUNDER & COO / OPERATIONS"}
                </div>
                <h3 className="text-sm font-bold text-white">Doğukan Bayram</h3>
                <p className="text-xs text-slate-400 leading-relaxed">
                  {lang === "tr"
                    ? "Reşit kurucu ortak ve yetkili şirket müdürü. Resmi sözleşmeler, kurumsal yönetim, fon ilişkileri ve hukuki temsil süreçlerini idare etmektedir."
                    : "Authorized corporate manager and COO. Oversees corporate governance, commercial contracting, investor operations, and legal representation."}
                </p>
              </div>
            </div>

            <div className="p-4 rounded-xl bg-[#07090d] border border-slate-800/80 flex items-start gap-3.5">
              <div className="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center text-slate-300 shrink-0">
                <Cpu className="w-5 h-5" />
              </div>
              <div className="space-y-1">
                <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                  {lang === "tr" ? "BAŞ DONANIM & ROBOTİK ENTEGRASYON" : "LEAD HARDWARE & ROBOTICS INTEGRATION"}
                </div>
                <h3 className="text-sm font-bold text-white">Denizcan Özcan</h3>
                <p className="text-xs text-slate-400 leading-relaxed">
                  {lang === "tr"
                    ? "TEKNOFEST Robotaksi Finalisti ve ASELSAN mühendislik havuzu üyesi. CAN-FD Drive-by-Wire, LiDAR/Radar kablolama ve araç gövde entegrasyonundan sorumludur."
                    : "TEKNOFEST Autonomous Robotaxi Finalist, ASELSAN engineering pool. Specializes in CAN-FD DBW actuation, LiDAR/Radar sensor harness, and EV integration."}
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* 3. Four Core Engineering Pillars */}
        <div className="space-y-4">
          <div>
            <div className="text-xs font-mono text-slate-400 font-semibold tracking-wider uppercase">
              {lang === "tr" ? "TEKNOLOJİK YETKİNLİKLER" : "CORE CAPABILITIES"}
            </div>
            <h2 className="text-xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "4 Temel Mühendislik İlkesi" : "4 Engineering Pillars"}
            </h2>
          </div>

          {/* 2-Column Grid on Mobile, 4-Column on Desktop (No endless vertical stack!) */}
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4">
            {pillars.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div
                  key={idx}
                  className="p-4 sm:p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-2.5 flex flex-col justify-between"
                >
                  <div className="space-y-2">
                    <div className="w-8 h-8 rounded-lg bg-slate-800/60 border border-slate-700 flex items-center justify-center text-slate-300">
                      <Icon className="w-4 h-4" />
                    </div>
                    <h3 className="text-xs sm:text-sm font-bold text-white leading-tight">
                      {item.title}
                    </h3>
                    <p className="text-[10px] sm:text-xs text-slate-400 leading-relaxed line-clamp-4 sm:line-clamp-none">
                      {item.desc}
                    </p>
                  </div>
                  <div className="pt-2 border-t border-slate-800 text-[10px] font-mono text-slate-300 font-semibold">
                    {item.stat}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 4. Official Accreditations & Registry Table */}
        <div className="space-y-4">
          <div>
            <div className="text-xs font-mono text-slate-400 font-semibold tracking-wider uppercase">
              {lang === "tr" ? "DEVLET VE EKOSİSTEM TESCİLLERİ" : "OFFICIAL REGISTRY & ACCREDITATIONS"}
            </div>
            <h2 className="text-xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Resmi Akreditasyon ve Tescil Sicilleri" : "Official State & Ecosystem Registrations"}
            </h2>
          </div>

          {/* Clean Corporate Table */}
          <div className="rounded-2xl border border-slate-800 bg-[#0f131a] overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs font-sans">
                <thead className="bg-[#07090d] text-slate-400 font-mono text-[11px] uppercase tracking-wider border-b border-slate-800">
                  <tr>
                    <th className="py-3 px-4 sm:px-6">Resmi Kurum</th>
                    <th className="py-3 px-4 sm:px-6">Sicil / Protokol No</th>
                    <th className="py-3 px-4 sm:px-6">Akreditasyon Türü</th>
                    <th className="py-3 px-4 sm:px-6 text-right">Durum</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800 text-slate-300">
                  {credentials.map((c, i) => (
                    <tr key={i} className="hover:bg-slate-900/40 transition-colors">
                      <td className="py-3.5 px-4 sm:px-6 font-semibold text-white">
                        {c.org}
                      </td>
                      <td className="py-3.5 px-4 sm:px-6 font-mono text-slate-400">
                        {c.reg}
                      </td>
                      <td className="py-3.5 px-4 sm:px-6 text-slate-300">
                        {c.type}
                      </td>
                      <td className="py-3.5 px-4 sm:px-6 text-right">
                        <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-950/60 border border-emerald-800 text-emerald-400 font-mono text-[10px] font-semibold">
                          <CheckCircle2 className="w-3 h-3" />
                          <span>{c.status}</span>
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* 5. Physical Infrastructure & Proving Grounds */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="p-5 sm:p-6 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-2">
            <div className="flex items-center gap-2 text-slate-400 font-mono text-xs uppercase font-semibold">
              <Building className="w-4 h-4" />
              <span>Ar-Ge ve Yönetim Merkezi</span>
            </div>
            <div className="text-base font-bold text-white">İTO BTM Kampüsü</div>
            <div className="text-xs text-slate-400 leading-relaxed">
              Fulya Mah. Yeşilçimen Sok. Polat Tower Rezidans, Şişli / İstanbul.
            </div>
          </div>

          <div className="p-5 sm:p-6 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-2">
            <div className="flex items-center gap-2 text-slate-400 font-mono text-xs uppercase font-semibold">
              <MapPin className="w-4 h-4" />
              <span>Saha Test ve Pist Alanı</span>
            </div>
            <div className="text-base font-bold text-white">Bilişim Vadisi Test Sahası</div>
            <div className="text-xs text-slate-400 leading-relaxed">
              Gebze Yerleşkesi 1.5 km kapalı pist ve sivil otonom test parkuru.
            </div>
          </div>
        </div>

      </div>

      <Footer />
    </main>
  );
}
