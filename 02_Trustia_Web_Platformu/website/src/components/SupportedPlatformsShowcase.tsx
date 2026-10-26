"use client";

import { useState } from "react";
import Link from "next/link";
import { Car, Shield, Tractor, ArrowRight, Check, ChevronRight } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TopographicCanvas from "@/components/TopographicCanvas";

const DOMAIN_THEMES: Record<
  string,
  {
    accentBorder: string;
    numColor: string;
    badgeBg: string;
    iconBg: string;
    checkColor: string;
    glow: string;
  }
> = {
  civilian: {
    accentBorder: "hover:border-emerald-500/50",
    numColor: "text-emerald-400",
    badgeBg: "bg-emerald-500/10 border-emerald-500/30 text-emerald-300",
    iconBg: "bg-emerald-500/20 text-emerald-400",
    checkColor: "text-emerald-400",
    glow: "group-hover:shadow-[0_0_30px_rgba(52,211,153,0.15)]",
  },
  defense: {
    accentBorder: "border-white/15 hover:border-[#E4F80D]/60",
    numColor: "text-[#E4F80D]",
    badgeBg: "bg-[#E4F80D]/10 border-[#E4F80D]/30 text-[#E4F80D]",
    iconBg: "bg-[#E4F80D]/20 text-[#E4F80D]",
    checkColor: "text-[#E4F80D]",
    glow: "group-hover:shadow-[0_0_30px_rgba(228,248,13,0.15)]",
  },
  industrial: {
    accentBorder: "hover:border-cyan-500/50",
    numColor: "text-cyan-400",
    badgeBg: "bg-cyan-500/10 border-cyan-500/30 text-cyan-300",
    iconBg: "bg-cyan-500/20 text-cyan-400",
    checkColor: "text-cyan-400",
    glow: "group-hover:shadow-[0_0_30px_rgba(6,182,212,0.15)]",
  },
};

export default function SupportedPlatformsShowcase() {
  const { lang } = useLanguage();
  const [activeTab, setActiveTab] = useState(0);
  const [touchStartX, setTouchStartX] = useState<number | null>(null);

  const handleTouchStart = (e: React.TouchEvent) => {
    setTouchStartX(e.targetTouches[0].clientX);
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (touchStartX === null) return;
    const touchEndX = e.changedTouches[0].clientX;
    const diff = touchStartX - touchEndX;
    if (diff > 50) {
      // swipe left -> next tab
      setActiveTab((prev) => (prev + 1) % solutions.length);
    } else if (diff < -50) {
      // swipe right -> prev tab
      setActiveTab((prev) => (prev - 1 + solutions.length) % solutions.length);
    }
    setTouchStartX(null);
  };

  const solutions = [
    {
      id: "civilian",
      num: "01",
      icon: Car,
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
      shortLabel: lang === "tr" ? "01 Sivil" : "01 Civil",
      title: lang === "tr" ? "Seviye 4 Robotaksi Filoları" : "Level-4 Robotaxi Fleets",
      subtitle: lang === "tr" ? "Şehir İçi Otonom Yolcu Taşımacılığı" : "Urban Autonomous Ride-Hailing",
      desc: lang === "tr"
        ? "Binek ve hafif ticari elektrikli araçlar için tak-çalıştır otonom sürüş beyni. Şehir içi karmaşık kavşaklar, trafik ışıkları, dinamik yaya geçitleri ve yolcu çağırma operasyonları için geliştirilmiştir."
        : "Plug-and-play autonomous driving stack tailored for passenger EVs, navigating dense urban intersections, signalized corridors, and ride-hailing services.",
      specs: lang === "tr"
        ? [
            "Elektronik Direksiyon (Drive-by-Wire CAN-FD)",
            "1 Aralık 2024 ADS Yönetmeliği Uyumluluğu",
            "UN ECE R157 DSSAD / EDR Kara Kutu Kaydı"
          ]
        : [
            "Drive-by-Wire CAN-FD Actuation Layer",
            "Full Compliance with Ministry ADS Regulations",
            "UN ECE R157 DSSAD / EDR Black-Box Logging"
          ],
      fleet: lang === "tr" ? "Hyundai Ioniq 5, SAIC Maxus MIFA 7, TOGG" : "Hyundai Ioniq 5, SAIC Maxus MIFA 7, TOGG",
      ctaLink: "/robotaxi/",
      ctaText: lang === "tr" ? "Hyundai Ioniq 5 Robotaksi Çözümü" : "Explore Robotaxi Solution"
    },
    {
      id: "defense",
      num: "02",
      icon: Shield,
      tag: lang === "tr" ? "SAVUNMA VE GÜVENLİK" : "DEFENSE & TACTICAL",
      shortLabel: lang === "tr" ? "02 Savunma" : "02 Defense",
      title: lang === "tr" ? "Taktik İnsansız Kara Araçları (İKA)" : "Tactical Defense UGVs",
      subtitle: lang === "tr" ? "GPS Olmayan Sahalarda Tam Otonomi" : "Full Autonomy in GNSS-Denied Theaters",
      desc: lang === "tr"
        ? "Elektronik harp, tüneller ve uydu sinyalinin kesildiği çatışma alanlarında; araç üzeri 3D LiDAR SLAM ve sürü zekası (swarm) ile görev yapan tekerlekli ve paletli savunma robotları."
        : "Engineered for GPS-jammed and contested operational environments; tactical ground robots powered by on-edge 3D LiDAR SLAM, ESKF sensor fusion, and multi-agent swarm intelligence.",
      specs: lang === "tr"
        ? [
            "GPS'siz Seyrüsefer (GNSS-Denied 3D LiDAR SLAM)",
            "Çoklu Robot Sürü Koordinasyonu (Swarm)",
            "Askeri JAUS & ROS 2 Humble Çift Kullanımlı Protokol"
          ]
        : [
            "GNSS-Denied 3D LiDAR SLAM Localization",
            "Multi-Agent Swarm Consensus & Formations",
            "Military JAUS & ROS 2 Dual-Use Architecture"
          ],
      fleet: lang === "tr" ? "Hafif, Orta ve Ağır Sınıf Taktik İKA Platformları" : "Light, Medium & Heavy Tactical Wheeled/Tracked UGVs",
      ctaLink: "/politika/lisans/",
      ctaText: lang === "tr" ? "Savunma Entegrasyon Şartnamesi" : "Defense Integration Specs"
    },
    {
      id: "industrial",
      num: "03",
      icon: Tractor,
      tag: lang === "tr" ? "ENDÜSTRİ VE LOJİSTİK" : "HEAVY INDUSTRY",
      shortLabel: lang === "tr" ? "03 Endüstri" : "03 Industry",
      title: lang === "tr" ? "Ağır Hizmet, Maden ve Liman Otonomisi" : "Mining, Ports & Heavy Logistics",
      subtitle: lang === "tr" ? "Zorlu Sahalarda 7/24 Kesintisiz Çalışma" : "24/7 Driverless Heavy Operations",
      desc: lang === "tr"
        ? "Açık maden ocakları, intermodal liman terminalleri ve tarım arazilerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır kamyon, çekici ve otonom yük taşıyıcı (AGV) yazılım mimarisi."
        : "Heavy-duty autonomous logistics operating 24/7 across open-pit mines, container shipping berths, and agricultural tracts, eliminating human exposure from high-hazard industrial zones.",
      specs: lang === "tr"
        ? [
            "Ağır Arazi ve Çamur Deformasyon Algılama",
            "Otonom Konvoy Takibi & Yük Taşıma",
            "Termal Gece ve Sisli Hava Görüş Füzyonu"
          ]
        : [
            "Off-Road Soil & Mud Terrain Deformation AI",
            "Autonomous Leader-Follower Convoy Tracking",
            "Thermal LWIR Night & Dense Fog Perception"
          ],
      fleet: lang === "tr" ? "Maden Kamyonları, Otonom Çekiciler, Liman AGV" : "Heavy Haul Trucks, Yard Tractors, Seaport AGVs",
      ctaLink: "/iletisim/",
      ctaText: lang === "tr" ? "Endüstriyel Çözüm Talebi" : "Request Industrial Briefing"
    }
  ];

  return (
    <section id="otonomi" className="relative z-20 py-12 sm:py-24 px-4 sm:px-8 lg:px-12 bg-gradient-to-b from-[#090b0e] via-[#0c1017] to-[#090b0e] border-b border-white/10 overflow-hidden select-none">
      {/* 1. Tactical Topographic Elevation Contours Canvas Layer */}
      <div className="absolute inset-0 opacity-20 pointer-events-none mix-blend-screen">
        <TopographicCanvas
          className="absolute inset-0 w-full h-full pointer-events-none"
          inkColor="168, 159, 140"
          bands={36}
          step={9}
          freq={0.018}
          interactive={false}
        />
      </div>

      {/* 2. Atmospheric Multi-Point Lighting Accents behind the 3 domains */}
      <div className="absolute top-1/3 left-[15%] -translate-x-1/2 w-[450px] h-[450px] rounded-full blur-[140px] bg-emerald-500/10 pointer-events-none" />
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[550px] h-[550px] rounded-full blur-[160px] bg-[#E4F80D]/10 pointer-events-none" />
      <div className="absolute top-1/3 right-[15%] translate-x-1/2 w-[450px] h-[450px] rounded-full blur-[140px] bg-cyan-500/10 pointer-events-none" />

      {/* 3. Subtle Engineering Dot Grid */}
      <div
        className="absolute inset-0 pointer-events-none opacity-20"
        style={{
          backgroundImage: "radial-gradient(rgba(255, 255, 255, 0.12) 1px, transparent 1px)",
          backgroundSize: "36px 36px",
        }}
      />

      <div className="max-w-7xl mx-auto space-y-8 sm:space-y-16 relative z-10">
        
        {/* Executive Balanced Header (Left: Title & Badge, Right: Architectural Scope) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-12 items-end pb-6 sm:pb-8 border-b border-white/10">
          <div className="lg:col-span-7 space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[10px] sm:text-[11px] font-mono tracking-wider uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>{lang === "tr" ? "UYGULAMA ALANLARI VE PLATFORM ENTEGRASYONU" : "DEPLOYMENT DOMAINS & INTEGRATION"}</span>
            </div>

            <h2 className="text-xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-tight">
              {lang === "tr"
                ? "Çift Kullanımlı (Dual-Use) Otonomi Çözümleri"
                : "Dual-Use Autonomous Solutions"}
            </h2>
          </div>

          <div className="lg:col-span-5">
            <p className="text-xs sm:text-sm text-slate-300 font-normal leading-relaxed">
              {lang === "tr"
                ? "Trustia AI; donanım bağımsız evrensel yazılım mimarisiyle sivil elektrikli araçlardan taktik savunma robotlarına ve ağır hizmet maden kamyonlarına kadar her şasiye 100 Hz standart CAN-FD köprüsüyle entegre olur."
                : "A sovereign hardware-agnostic autonomy stack interfacing seamlessly across passenger EVs, tactical defense robotics, and heavy mining fleets via 100 Hz CAN-FD abstraction."}
            </p>
          </div>
        </div>

        {/* 1. Mobile Segmented Tab Switcher + Interactive Glass Card (lg:hidden) */}
        <div className="block lg:hidden space-y-4">
          {/* Segmented Switcher Bar */}
          <div className="flex items-center p-1 rounded-xl bg-white/[0.05] border border-white/10 gap-1 shadow-inner">
            {solutions.map((item, idx) => {
              const Icon = item.icon;
              const isActive = activeTab === idx;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(idx)}
                  className={`flex-1 flex items-center justify-center gap-1.5 py-2.5 px-2 rounded-lg text-xs font-mono font-bold transition-all duration-200 cursor-pointer ${
                    isActive
                      ? "bg-white text-slate-950 shadow-md scale-[1.02]"
                      : "text-slate-400 hover:text-white"
                  }`}
                >
                  <Icon className={`w-3.5 h-3.5 shrink-0 ${isActive ? "text-slate-950" : "text-slate-400"}`} />
                  <span className="truncate">{item.shortLabel}</span>
                </button>
              );
            })}
          </div>

          {/* Active Domain Glassmorphic Card (Touch Swipe Enabled) */}
          <div
            className="p-5 rounded-2xl bg-gradient-to-b from-[#141b27] via-[#0d121c] to-[#07090e] border border-white/15 shadow-2xl backdrop-blur-md flex flex-col justify-between space-y-5 transition-all duration-300"
            onTouchStart={handleTouchStart}
            onTouchEnd={handleTouchEnd}
          >
            {/* Upper Content */}
            <div className="space-y-4">
              {/* Top Bar: Number, Tag & Dot Indicators */}
              <div className="flex items-center justify-between pb-3.5 border-b border-white/10">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-slate-400">
                    {solutions[activeTab].num} //
                  </span>
                  <span className="px-2.5 py-0.5 rounded bg-white/10 border border-white/15 text-[10px] font-mono text-slate-200 uppercase tracking-wider font-semibold">
                    {solutions[activeTab].tag}
                  </span>
                </div>

                {/* Progress Indicators & Quick Navigation Dots */}
                <div className="flex items-center gap-1.5">
                  {solutions.map((_, dotIdx) => (
                    <button
                      key={dotIdx}
                      onClick={() => setActiveTab(dotIdx)}
                      className={`h-1.5 rounded-full transition-all duration-300 cursor-pointer ${
                        activeTab === dotIdx
                          ? "w-6 bg-white"
                          : "w-1.5 bg-white/20 hover:bg-white/40"
                      }`}
                      aria-label={`Geçiş ${dotIdx + 1}`}
                    />
                  ))}
                </div>
              </div>

              {/* Title & Subtitle */}
              <div className="space-y-1">
                <h3 className="text-xl font-bold text-white tracking-tight leading-snug">
                  {solutions[activeTab].title}
                </h3>
                <div className="text-xs font-mono text-slate-400">
                  {solutions[activeTab].subtitle}
                </div>
              </div>

              {/* Narrative Description */}
              <p className="text-xs text-slate-300 leading-relaxed font-sans">
                {solutions[activeTab].desc}
              </p>

              {/* Technical Specifications List */}
              <div className="pt-3 border-t border-white/10 space-y-2">
                <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                  {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                </div>
                {solutions[activeTab].specs.map((specText, sIdx) => (
                  <div key={sIdx} className="flex items-start gap-2 text-xs text-slate-200 font-sans">
                    <Check className="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5" />
                    <span>{specText}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Bottom Footer: Compatible Fleet & Sleek Touch Action Button */}
            <div className="pt-4 border-t border-white/10 space-y-3.5">
              <div className="text-[11px] font-mono text-slate-400">
                <span className="text-slate-200 font-semibold">{lang === "tr" ? "Uyumlu Şasi:" : "Compatible Fleet:"}</span>{" "}
                <span className="text-slate-300">{solutions[activeTab].fleet}</span>
              </div>

              <Link
                href={solutions[activeTab].ctaLink}
                className="w-full py-3 px-4 rounded-xl bg-white/10 hover:bg-white/15 border border-white/20 text-white flex items-center justify-between text-xs font-mono font-bold uppercase tracking-wider transition-all duration-200 cursor-pointer shadow-lg active:scale-[0.99]"
              >
                <span>{solutions[activeTab].ctaText}</span>
                <ArrowRight className="w-4 h-4 text-white" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. Desktop 3-Column Architectural Panels (Rich Tactical Glass with Domain Lighting) */}
        <div className="hidden lg:grid lg:grid-cols-3 gap-6 sm:gap-8 items-stretch">
          {solutions.map((item) => {
            const Icon = item.icon;
            const theme = DOMAIN_THEMES[item.id] || DOMAIN_THEMES.defense;
            return (
              <div
                key={item.id}
                className={`p-6 sm:p-8 rounded-2xl bg-gradient-to-b from-[#141b27]/90 via-[#0d121c]/95 to-[#07090e]/95 border border-white/10 ${theme.accentBorder} ${theme.glow} backdrop-blur-md transition-all duration-300 flex flex-col justify-between space-y-6 group relative overflow-hidden`}
              >
                {/* Subtle top edge glow strip */}
                <div
                  className="absolute top-0 inset-x-0 h-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                  style={{
                    background:
                      item.id === "civilian"
                        ? "linear-gradient(90deg, transparent, #34d399, transparent)"
                        : item.id === "defense"
                        ? "linear-gradient(90deg, transparent, #E4F80D, transparent)"
                        : "linear-gradient(90deg, transparent, #38bdf8, transparent)",
                  }}
                />

                {/* Upper Content */}
                <div className="space-y-5">
                  {/* Top Bar: Number & Category Badge */}
                  <div className="flex items-center justify-between pb-4 border-b border-white/10">
                    <div className="flex items-center gap-2">
                      <span className={`font-mono text-xs font-bold ${theme.numColor}`}>
                        {item.num} //
                      </span>
                      <span className={`px-2.5 py-0.5 rounded border text-[10px] font-mono uppercase tracking-wider font-semibold ${theme.badgeBg}`}>
                        {item.tag}
                      </span>
                    </div>

                    <div className={`w-8 h-8 rounded-lg flex items-center justify-center ${theme.iconBg}`}>
                      <Icon className="w-4 h-4" />
                    </div>
                  </div>

                  {/* Title & Subtitle */}
                  <div className="space-y-1">
                    <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight leading-snug">
                      {item.title}
                    </h3>
                    <div className="text-[11px] font-mono text-slate-400">
                      {item.subtitle}
                    </div>
                  </div>

                  {/* Narrative Description */}
                  <p className="text-xs text-slate-300 leading-relaxed font-sans">
                    {item.desc}
                  </p>

                  {/* Technical Specifications List */}
                  <div className="pt-3 border-t border-white/10 space-y-2">
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                      {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                    </div>
                    {item.specs.map((specText, sIdx) => (
                      <div key={sIdx} className="flex items-start gap-2 text-xs text-slate-300 font-sans">
                        <Check className={`w-3.5 h-3.5 ${theme.checkColor} shrink-0 mt-0.5`} />
                        <span>{specText}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Bottom Footer: Compatible Fleet & Sleek Action Link */}
                <div className="pt-5 border-t border-white/10 space-y-3.5">
                  <div className="text-[11px] font-mono text-slate-400">
                    <span className="text-slate-200 font-semibold">{lang === "tr" ? "Uyumlu Şasi:" : "Compatible Fleet:"}</span>{" "}
                    <span className="text-slate-300">{item.fleet}</span>
                  </div>

                  <Link
                    href={item.ctaLink}
                    className="inline-flex items-center gap-2 text-xs font-mono font-semibold text-white group-hover:text-slate-200 uppercase tracking-wider transition-colors pt-1"
                  >
                    <span>{item.ctaText}</span>
                    <ArrowRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-1" />
                  </Link>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}