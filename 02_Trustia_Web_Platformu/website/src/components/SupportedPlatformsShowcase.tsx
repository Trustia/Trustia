"use client";

import Link from "next/link";
import { Car, Shield, Tractor, ArrowRight, Check, ChevronRight } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function SupportedPlatformsShowcase() {
  const { lang } = useLanguage();

  const solutions = [
    {
      id: "civilian",
      num: "01",
      icon: Car,
      tag: lang === "tr" ? "SİVİL MOBİLİTE" : "CIVIL MOBILITY",
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
    <section id="otonomi" className="relative z-20 py-16 sm:py-24 px-4 sm:px-8 lg:px-12 bg-[#080a0e] border-b border-white/10">
      <div className="max-w-7xl mx-auto space-y-12 sm:space-y-16">
        
        {/* Executive Balanced Header (Left: Title & Badge, Right: Architectural Scope) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-12 items-end pb-8 border-b border-white/10">
          <div className="lg:col-span-7 space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>{lang === "tr" ? "UYGULAMA ALANLARI VE PLATFORM ENTEGRASYONU" : "DEPLOYMENT DOMAINS & INTEGRATION"}</span>
            </div>

            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-tight">
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

        {/* 3 Refined Architectural Panels (Full width, No clunky box clutter!) */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 sm:gap-8 items-stretch">
          {solutions.map((item) => {
            const Icon = item.icon;
            return (
              <div
                key={item.id}
                className="p-6 sm:p-8 rounded-2xl bg-[#0c0f15] border border-white/10 hover:border-white/20 transition-all duration-300 flex flex-col justify-between space-y-6 group"
              >
                {/* Upper Content */}
                <div className="space-y-5">
                  {/* Top Bar: Number & Category Badge */}
                  <div className="flex items-center justify-between pb-4 border-b border-white/5">
                    <span className="font-mono text-xs font-bold text-slate-500 group-hover:text-slate-300 transition-colors">
                      {item.num} //
                    </span>
                    <span className="px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-[10px] font-mono text-slate-300 uppercase tracking-wider font-semibold">
                      {item.tag}
                    </span>
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
                  <div className="pt-3 border-t border-white/5 space-y-2">
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                      {lang === "tr" ? "Teknik Yetkinlikler:" : "Key Technical Features:"}
                    </div>
                    {item.specs.map((specText, sIdx) => (
                      <div key={sIdx} className="flex items-start gap-2 text-xs text-slate-300 font-sans">
                        <Check className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
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
