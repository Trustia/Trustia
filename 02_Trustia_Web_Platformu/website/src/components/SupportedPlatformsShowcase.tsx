"use client";

import { useState } from "react";
import Link from "next/link";
import { Car, Shield, Tractor, ArrowRight, Check } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

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
      setActiveTab((prev) => (prev + 1) % solutions.length);
    } else if (diff < -50) {
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
    <section id="otonomi" className="relative z-20 py-16 sm:py-24 px-4 sm:px-8 lg:px-12 bg-[#E5D6BC] text-[#14120c] border-b border-[#26221b]/15 select-none overflow-hidden">
      <div className="max-w-7xl mx-auto space-y-8 sm:space-y-14 relative z-10">
        
        {/* Overland-Style Tactical Header (High-contrast military sand) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-12 items-end pb-6 sm:pb-8 border-b border-[#26221b]/15">
          <div className="lg:col-span-7 space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-[#26221b]/10 border border-[#26221b]/15 text-[#26221b] text-[10px] sm:text-[11px] font-mono tracking-wider uppercase font-bold">
              <span className="text-[#26221b] font-bold">[+]</span>
              <span>{lang === "tr" ? "UYGULAMA ALANLARI VE PLATFORM ENTEGRASYONU" : "DEPLOYMENT DOMAINS & CHASSIS INTEGRATION"}</span>
            </div>

            <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-[#14120c] tracking-tight leading-tight">
              {lang === "tr"
                ? "Çift Kullanımlı (Dual-Use) Otonomi Çözümleri"
                : "Dual-Use Autonomous Driving Stack"}
            </h2>
          </div>

          <div className="lg:col-span-5">
            <p className="text-xs sm:text-sm text-[#383226] font-medium leading-relaxed">
              {lang === "tr"
                ? "Trustia AI; donanım bağımsız evrensel yazılım mimarisiyle sivil elektrikli araçlardan taktik savunma robotlarına ve ağır hizmet maden kamyonlarına kadar her şasiye 100 Hz standart CAN-FD köprüsüyle entegre olur."
                : "A sovereign hardware-agnostic autonomy stack interfacing seamlessly across passenger EVs, tactical defense robotics, and heavy mining fleets via 100 Hz CAN-FD abstraction."}
            </p>
          </div>
        </div>

        {/* 1. Mobile Segmented Tab Switcher + Card (lg:hidden) */}
        <div className="block lg:hidden space-y-4">
          <div className="flex items-center p-1 bg-[#26221b]/10 border border-[#26221b]/15 gap-1">
            {solutions.map((item, idx) => {
              const Icon = item.icon;
              const isActive = activeTab === idx;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(idx)}
                  className={`flex-1 flex items-center justify-center gap-1.5 py-2.5 px-2 text-xs font-mono font-bold transition-all duration-200 cursor-pointer ${
                    isActive
                      ? "bg-[#14120c] text-[#E5D6BC] shadow-md"
                      : "text-[#383226] hover:text-black"
                  }`}
                >
                  <Icon className="w-3.5 h-3.5 shrink-0" />
                  <span className="truncate">{item.shortLabel}</span>
                </button>
              );
            })}
          </div>

          {/* Active Card Mobile */}
          <div
            className="p-5 bg-[#DCD0B8] border border-[#26221b]/20 shadow-md flex flex-col justify-between space-y-5 transition-all duration-300"
            onTouchStart={handleTouchStart}
            onTouchEnd={handleTouchEnd}
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between pb-3.5 border-b border-[#26221b]/15">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-[#26221b]">
                    {solutions[activeTab].num} //
                  </span>
                  <span className="px-2.5 py-0.5 bg-[#26221b]/10 border border-[#26221b]/20 text-[10px] font-mono text-[#14120c] uppercase tracking-wider font-bold">
                    {solutions[activeTab].tag}
                  </span>
                </div>

                <div className="flex items-center gap-1.5">
                  {solutions.map((_, dotIdx) => (
                    <button
                      key={dotIdx}
                      onClick={() => setActiveTab(dotIdx)}
                      className={`h-1.5 transition-all duration-300 cursor-pointer ${
                        activeTab === dotIdx
                          ? "w-6 bg-[#14120c]"
                          : "w-1.5 bg-[#26221b]/30"
                      }`}
                      aria-label={`Geçiş ${dotIdx + 1}`}
                    />
                  ))}
                </div>
              </div>

              <div className="space-y-1">
                <h3 className="text-xl font-bold text-[#14120c] tracking-tight leading-snug">
                  {solutions[activeTab].title}
                </h3>
                <div className="text-xs font-mono text-[#5c5344] font-medium">
                  {solutions[activeTab].subtitle}
                </div>
              </div>

              <p className="text-xs text-[#26221b] leading-relaxed font-sans">
                {solutions[activeTab].desc}
              </p>

              <div className="pt-3 border-t border-[#26221b]/15 space-y-2">
                <div className="text-[10px] font-mono text-[#5c5344] uppercase tracking-wider font-bold">
                  {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                </div>
                {solutions[activeTab].specs.map((specText, sIdx) => (
                  <div key={sIdx} className="flex items-start gap-2 text-xs text-[#26221b] font-sans font-medium">
                    <Check className="w-3.5 h-3.5 text-[#14120c] shrink-0 mt-0.5" />
                    <span>{specText}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-4 border-t border-[#26221b]/15 space-y-3.5">
              <div className="text-[11px] font-mono text-[#5c5344]">
                <span className="text-[#14120c] font-bold">{lang === "tr" ? "Uyumlu Şasi:" : "Compatible Fleet:"}</span>{" "}
                <span className="text-[#26221b]">{solutions[activeTab].fleet}</span>
              </div>

              <Link
                href={solutions[activeTab].ctaLink}
                className="w-full py-3 px-4 bg-[#14120c] hover:bg-black text-[#E5D6BC] flex items-center justify-between text-xs font-mono font-bold uppercase tracking-wider transition-all duration-200 cursor-pointer shadow-md"
              >
                <span>{solutions[activeTab].ctaText}</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. Desktop 3-Column Panels (Overland AI Tactical Sand Style) */}
        <div className="hidden lg:grid lg:grid-cols-3 gap-6 sm:gap-8 items-stretch">
          {solutions.map((item) => {
            const Icon = item.icon;
            return (
              <div
                key={item.id}
                className="p-6 sm:p-8 bg-[#DCD0B8] border border-[#26221b]/20 hover:border-[#26221b]/50 shadow-[0_2px_12px_rgba(38,34,27,0.06)] transition-all duration-300 flex flex-col justify-between space-y-6 group"
              >
                {/* Upper Content */}
                <div className="space-y-5">
                  {/* Top Bar: Number & Category Badge */}
                  <div className="flex items-center justify-between pb-4 border-b border-[#26221b]/15">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold text-[#26221b]">
                        {item.num} //
                      </span>
                      <span className="px-2.5 py-0.5 bg-[#26221b]/10 border border-[#26221b]/20 text-[10px] font-mono text-[#14120c] uppercase tracking-wider font-bold">
                        {item.tag}
                      </span>
                    </div>

                    <div className="w-8 h-8 flex items-center justify-center bg-[#26221b]/10 text-[#14120c]">
                      <Icon className="w-4 h-4" />
                    </div>
                  </div>

                  {/* Title & Subtitle */}
                  <div className="space-y-1">
                    <h3 className="text-lg sm:text-xl font-bold text-[#14120c] tracking-tight leading-snug">
                      {item.title}
                    </h3>
                    <div className="text-[11px] font-mono text-[#5c5344] font-medium">
                      {item.subtitle}
                    </div>
                  </div>

                  {/* Narrative Description */}
                  <p className="text-xs text-[#26221b] leading-relaxed font-sans">
                    {item.desc}
                  </p>

                  {/* Technical Specifications List */}
                  <div className="pt-3 border-t border-[#26221b]/15 space-y-2">
                    <div className="text-[10px] font-mono text-[#5c5344] uppercase tracking-wider font-bold">
                      {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                    </div>
                    {item.specs.map((specText, sIdx) => (
                      <div key={sIdx} className="flex items-start gap-2 text-xs text-[#26221b] font-sans font-medium">
                        <Check className="w-3.5 h-3.5 text-[#14120c] shrink-0 mt-0.5" />
                        <span>{specText}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Bottom Footer: Compatible Fleet & Action Link */}
                <div className="pt-5 border-t border-[#26221b]/15 space-y-3.5">
                  <div className="text-[11px] font-mono text-[#5c5344]">
                    <span className="text-[#14120c] font-bold">{lang === "tr" ? "Uyumlu Şasi:" : "Compatible Fleet:"}</span>{" "}
                    <span className="text-[#26221b] font-medium">{item.fleet}</span>
                  </div>

                  <Link
                    href={item.ctaLink}
                    className="inline-flex items-center gap-2 text-xs font-mono font-bold text-[#14120c] hover:text-black uppercase tracking-wider transition-colors pt-1 border-b border-[#14120c]/40 hover:border-black"
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
