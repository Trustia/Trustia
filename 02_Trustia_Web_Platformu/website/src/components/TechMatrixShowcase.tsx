"use client";

import { Compass, Layers, Radar, Radio, Lock, Cpu, CloudRain, Wifi, Activity, ShieldCheck, Zap } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function TechMatrixShowcase() {
  const { lang } = useLanguage();

  const capabilities = [
    {
      id: "slam",
      icon: Compass,
      title: lang === "tr" ? "GPS'siz 3D SLAM" : "GPS-Denied 3D SLAM",
      desc: lang === "tr"
        ? "Uydu sinyali olmadan 3D LiDAR ve kameralarla santimetre hassasiyetinde haritalama."
        : "Centimeter-accurate 3D mapping and localization operating without satellite GPS.",
      badge: lang === "tr" ? "0 Dış Bağımlılık" : "Zero GPS Dependency"
    },
    {
      id: "prediction",
      icon: Activity,
      title: lang === "tr" ? "5s Yörünge Tahmini" : "5s Trajectory AI",
      desc: lang === "tr"
        ? "Yaya ve araçların 5 saniyelik hareketini önceden kestirerek sıfır kaza güvenliği sağlar."
        : "Multimodal intent prediction modeling paths 5s ahead for proactive avoidance.",
      badge: lang === "tr" ? "Öngörülü Güvenlik" : "Predictive Safety"
    },
    {
      id: "v2x",
      icon: Wifi,
      title: lang === "tr" ? "V2X Akıllı Şehir" : "V2X Infrastructure",
      desc: lang === "tr"
        ? "Akıllı ışıklardan (SPaT/GLOSA) sinyal sürelerini alır, araçlar arası frenleme paylaşır."
        : "C-V2X engine communicating directly with smart traffic lights and emergency fleets.",
      badge: lang === "tr" ? "C-V2X / SPaT" : "Connected V2X"
    },
    {
      id: "weather",
      icon: CloudRain,
      title: lang === "tr" ? "Zorlu Hava Filtresi" : "All-Weather Filter",
      desc: lang === "tr"
        ? "Sis, sağanak ve çamurda sensör körleşmesini telafi edip 77GHz radara ağırlık verir."
        : "Dynamic sensor degradation adaptation for dense fog, rain, and lens occlusion.",
      badge: lang === "tr" ? "Sis / Yağmur / Çamur" : "All-Weather"
    },
    {
      id: "teleop",
      icon: Radio,
      title: lang === "tr" ? "Filo Teleoperasyonu" : "Fleet Teleoperation",
      desc: lang === "tr"
        ? "Merkezdeki operatörün araca uzaktan güvenle müdahale etmesini sağlayan C2 köprüsü."
        : "Low-latency WebRTC teleoperation bridge for remote human-in-the-loop guidance.",
      badge: lang === "tr" ? "Düşük Gecikme" : "Low-Latency"
    },
    {
      id: "tested",
      icon: ShieldCheck,
      title: lang === "tr" ? "1.301 Doğrulanmış Test" : "1,301 Verified Tests",
      desc: lang === "tr"
        ? "16.000+ satır özgün kod, HMAC-SHA256 şifreleme ve %100 başarılı 1.301 birim test."
        : "16,000+ lines of sovereign code with 100% pass rate across 1,301 test suites.",
      badge: lang === "tr" ? "%100 Başarı" : "100% Pass Rate"
    }
  ];

  return (
    <section id="teknoloji" className="relative z-20 py-10 sm:py-20 px-3.5 sm:px-8 bg-[#07090c] border-b border-white/10">
      <div className="max-w-6xl mx-auto space-y-6 sm:space-y-12">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto space-y-2 sm:space-y-3">
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 sm:px-3 sm:py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[10px] sm:text-[11px] font-mono tracking-wider uppercase">
            <span>{lang === "tr" ? "TEKNOLOJİK ÇEKİRDEK & MODÜLLER" : "CORE TECHNOLOGY & MODULES"}</span>
          </div>
          
          <h2 className="text-xl sm:text-3xl font-bold text-white tracking-tight leading-snug">
            {lang === "tr" ? "Güvenilir, Deterministik Otonomi Mimarisi" : "Deterministic, Battle-Tested Autonomy Core"}
          </h2>
          
          <p className="text-xs sm:text-sm text-slate-400 font-normal leading-relaxed max-w-2xl mx-auto">
            {lang === "tr"
              ? "Her türlü hava, trafik ve harekat koşulunda hatasız çalışan Seviye 4 yerli yazılım katmanlarımız."
              : "Level-4 sovereign autonomy software layers designed for flawless operation across all traffic, tactical, and weather conditions."}
          </p>
        </div>

        {/* 
          2-Column Compact Grid on Mobile, 3-Column on Desktop (No endless vertical scrolling!)
        */}
        <div className="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 gap-2.5 sm:gap-5">
          {capabilities.map((item) => {
            const Icon = item.icon;
            return (
              <div
                key={item.id}
                className="p-3 sm:p-6 rounded-xl bg-[#0c0f14] border border-white/10 hover:border-white/20 transition-all duration-300 flex flex-col justify-between space-y-2 sm:space-y-4 group"
              >
                <div className="space-y-1.5 sm:space-y-3">
                  <div className="flex items-center justify-between gap-1">
                    <div className="w-7 h-7 sm:w-10 sm:h-10 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 group-hover:text-white transition-colors shrink-0">
                      <Icon className="w-3.5 h-3.5 sm:w-5 sm:h-5" />
                    </div>
                    <span className="text-[8px] sm:text-[10px] font-mono text-slate-400 px-1.5 py-0.5 rounded bg-white/5 border border-white/5 truncate shrink-0">
                      {item.badge}
                    </span>
                  </div>

                  <h3 className="text-xs sm:text-base font-bold text-white tracking-tight leading-snug">
                    {item.title}
                  </h3>

                  <p className="text-[10px] sm:text-xs text-slate-400 font-normal leading-relaxed line-clamp-3 sm:line-clamp-none">
                    {item.desc}
                  </p>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
