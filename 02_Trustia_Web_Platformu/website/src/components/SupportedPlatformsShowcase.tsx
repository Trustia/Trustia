"use client";

import { useState } from "react";
import Link from "next/link";
import { Car, Shield, Tractor, ArrowRight, Check } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function SupportedPlatformsShowcase() {
  const { lang } = useLanguage();
  const [activeSlide, setActiveSlide] = useState(0);

  const handleScroll = (e: React.UIEvent<HTMLDivElement>) => {
    const scrollLeft = e.currentTarget.scrollLeft;
    const itemWidth = e.currentTarget.offsetWidth * 0.82;
    const idx = Math.round(scrollLeft / itemWidth);
    setActiveSlide(Math.min(Math.max(idx, 0), 2));
  };

  const solutions = [
    {
      id: "civilian",
      num: "01",
      icon: Car,
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
      shortLabel: lang === "tr" ? "01 Sivil" : "01 Civil",
      title: lang === "tr" ? "Seviye 4 Robotaksi Filoları" : "Level-4 Robotaxi Fleets",
      subtitle: lang === "tr" ? "Şehir İçi Otonom Yolcu Taşımacılığı (20 Modül)" : "Urban Autonomous Ride-Hailing (20 Modules)",
      desc: lang === "tr"
        ? "Binek ve hafif ticari elektrikli araçlar için 29.748+ satırlık tak-çalıştır otonom sürüş beyni. Şehir içi karmaşık kavşaklar, Lanelet2 yaya geçitleri, trafik ışıkları ve yolcu çağırma operasyonları için geliştirilmiştir."
        : "Plug-and-play 29,748+ LOC autonomous driving stack tailored for passenger EVs, navigating dense urban intersections, signalized corridors, and ride-hailing services.",
      specs: lang === "tr"
        ? [
            "100 Hz CAN-FD, Frenet Lattice & Kayan Ufuklu MPC",
            "1 Aralık 2024 Resmî Gazete (AB 2022/1426) Tam Uyum",
            "IEEE 2846 RSS, UN R155 IDPS, R156 SUMS & R157 DSSAD"
          ]
        : [
            "100 Hz CAN-FD, Frenet Lattice & Receding-Horizon MPC",
            "Full Compliance with EU 2022/1426 ADS Homologation",
            "IEEE 2846 RSS, UN R155 IDPS, R156 SUMS & R157 DSSAD"
          ],
      fleet: lang === "tr" ? "Hyundai Ioniq 5, SAIC Maxus MIFA 7, TOGG" : "Hyundai Ioniq 5, SAIC Maxus MIFA 7, TOGG",
      ctaLink: "/robotaxi/",
      ctaText: lang === "tr" ? "Robotaksi Mimarisi (20 Modül)" : "Robotaxi Architecture (20 Modules)"
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
        ? "Elektronik harp, tüneller ve uydu sinyalinin kesildiği çatışma alanlarında; IEEE 1588v2 PTP senkronlu 3D LiDAR SLAM, 400 Hz ESKF ve sürü zekası (swarm) ile görev yapan savunma robotları."
        : "Engineered for GPS-jammed and contested operational environments; tactical ground robots powered by IEEE 1588v2 PTP 3D LiDAR SLAM, 400 Hz ESKF, and multi-agent swarm intelligence.",
      specs: lang === "tr"
        ? [
            "GNSS-Denied 3D LiDAR SLAM & PTP Motion Deskewing",
            "ASELSAN (#0050569) & STM Savunma Ekosistemi Uyumlu",
            "Askeri JAUS & ROS 2 Humble Çift Kullanımlı Protokol"
          ]
        : [
            "GNSS-Denied 3D LiDAR SLAM & PTP Motion Deskewing",
            "ASELSAN (#0050569) & STM Defense Ecosystem Ready",
            "Military JAUS & ROS 2 Dual-Use Architecture"
          ],
      fleet: lang === "tr" ? "Hafif, Orta ve Ağır Sınıf Taktik İKA Platformları" : "Light, Medium & Heavy Tactical Wheeled/Tracked UGVs",
      ctaLink: "/politika/lisans/",
      ctaText: lang === "tr" ? "Savunma Entegrasyonu" : "Defense Specifications"
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
        ? "Açık maden ocakları, havalimanı apronları, intermodal liman terminalleri ve tarım arazilerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır kamyon, çekici ve AGV yazılım mimarisi."
        : "Heavy-duty autonomous logistics operating 24/7 across open-pit mines, airport aprons, and container shipping berths, eliminating human exposure from high-hazard zones.",
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
      ctaText: lang === "tr" ? "Endüstriyel Çözümler" : "Industrial Solutions"
    }
  ];

  return (
    <section id="otonomi" className="relative z-20 py-10 sm:py-24 px-4 sm:px-8 lg:px-12 bg-[#E5D6BC] text-[#14120c] border-b border-[#26221b]/15 select-none overflow-hidden">
      <div className="max-w-7xl mx-auto space-y-6 sm:space-y-14 relative z-10">
        
        {/* Tactical Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-3 lg:gap-12 items-end pb-4 sm:pb-8 border-b border-[#26221b]/15">
          <div className="lg:col-span-8 space-y-2">
            <div className="text-[10px] sm:text-[11px] font-mono tracking-wider uppercase font-bold text-[#5c5344]">
              {lang === "tr" ? "UYGULAMA ALANLARI VE PLATFORM ENTEGRASYONU" : "DEPLOYMENT DOMAINS & CHASSIS INTEGRATION"}
            </div>

            <h2 className="text-base sm:text-2xl md:text-3xl lg:text-[34px] font-extrabold text-[#14120c] tracking-tight leading-snug">
              {lang === "tr"
                ? "Çift Kullanımlı (Dual-Use) Otonomi Çözümleri"
                : "Dual-Use Autonomous Driving Stack"}
            </h2>
          </div>

          <div className="lg:col-span-4">
            <p className="text-xs sm:text-sm text-[#383226] font-medium leading-relaxed">
              {lang === "tr"
                ? "Donanım bağımsız evrensel yazılım mimarisi; sivil elektrikli araçlardan taktik savunma robotlarına ve ağır maden filolarına kadar her şasiye 100 Hz CAN-FD ile entegre olur."
                : "Hardware-agnostic universal autonomy stack interfacing seamlessly across passenger EVs, tactical defense UGVs, and heavy mining fleets via 100 Hz CAN-FD."}
            </p>
          </div>
        </div>

        {/* 1. Mobile Horizontal Swipeable Cards (lg:hidden) */}
        <div className="block lg:hidden space-y-3">
          {/* Centered Minimal Indicator Dots (No text) */}
          <div className="flex items-center justify-center gap-1.5 pb-0.5">
            {solutions.map((_, i) => (
              <div
                key={i}
                className={`h-1 rounded-full transition-all duration-300 ${
                  activeSlide === i ? "w-6 bg-[#14120c]" : "w-1.5 bg-[#26221b]/30"
                }`}
              />
            ))}
          </div>

          {/* Swipe Track */}
          <div
            onScroll={handleScroll}
            className="flex gap-3.5 overflow-x-auto snap-x snap-mandatory scrollbar-none pb-2 -mx-4 px-4"
          >
            {solutions.map((item) => {
              const Icon = item.icon;
              return (
                <div
                  key={item.id}
                  className="w-[84vw] max-w-[340px] shrink-0 snap-center p-5 bg-[#DCD0B8] border border-[#26221b]/20 shadow-md flex flex-col justify-between space-y-4"
                >
                  <div className="space-y-3.5">
                    {/* Top Bar: Number, Tag & Icon */}
                    <div className="flex items-center justify-between pb-3 border-b border-[#26221b]/15">
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-xs font-bold text-[#26221b]">
                          {item.num} //
                        </span>
                        <span className="text-[10px] font-mono text-[#5c5344] uppercase tracking-wider font-bold">
                          {item.tag}
                        </span>
                      </div>
                      <Icon className="w-4 h-4 text-[#14120c] shrink-0" />
                    </div>

                    {/* Title & Subtitle */}
                    <div className="space-y-1">
                      <h3 className="text-base font-bold text-[#14120c] tracking-tight leading-snug">
                        {item.title}
                      </h3>
                      <div className="text-[11px] font-mono text-[#5c5344]">
                        {item.subtitle}
                      </div>
                    </div>

                    {/* Narrative Description */}
                    <p className="text-xs text-[#26221b] leading-relaxed font-sans">
                      {item.desc}
                    </p>

                    {/* Technical Specifications */}
                    <div className="pt-2.5 border-t border-[#26221b]/15 space-y-1.5">
                      <div className="text-[10px] font-mono text-[#5c5344] uppercase tracking-wider font-bold">
                        {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                      </div>
                      {item.specs.map((specText, sIdx) => (
                        <div key={sIdx} className="flex items-start gap-2 text-[11px] text-[#26221b] font-sans font-medium">
                          <Check className="w-3 h-3 text-[#14120c] shrink-0 mt-0.5" />
                          <span>{specText}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Bottom Footer: Compatible Fleet & Underline Link */}
                  <div className="pt-3 border-t border-[#26221b]/15 space-y-2.5">
                    <div className="text-[10px] font-mono text-[#5c5344]">
                      <span className="text-[#14120c] font-bold">
                        {lang === "tr" ? "Uyumlu Şasi:" : "Compatible Fleet:"}
                      </span>{" "}
                      <span className="text-[#26221b]">{item.fleet}</span>
                    </div>

                    <Link
                      href={item.ctaLink}
                      className="inline-flex items-center gap-2 text-xs font-mono font-bold text-[#14120c] hover:text-black uppercase tracking-wider transition-colors pt-1 border-b-2 border-[#14120c] w-fit group"
                    >
                      <span className="whitespace-nowrap">{item.ctaText}</span>
                      <ArrowRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-1 shrink-0" />
                    </Link>
                  </div>
                </div>
              );
            })}
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
                      <span className="text-[10px] font-mono text-[#5c5344] uppercase tracking-wider font-bold">
                        {item.tag}
                      </span>
                    </div>

                    <Icon className="w-4 h-4 text-[#14120c]" />
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
