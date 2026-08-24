"use client";

import { useState } from "react";
import { Compass, Radar, Radio, Lock, Cpu, Crosshair, Layers } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function TechMatrixShowcase() {
  const { lang, t } = useLanguage();
  const [activeTab, setActiveTab] = useState<"all" | "otonomi" | "tehdit" | "suru" | "siber" | "test">("all");
  const [mobileCardIndex, setMobileCardIndex] = useState(0);

  const techFeatures = [
    {
      id: "slam",
      category: "otonomi",
      number: "01",
      badge: t("card_1_badge"),
      title: t("card_1_title"),
      desc: t("card_1_desc"),
      tags: ["ICP 3D Scan Matching", "Pose Graph Optimization", "Visual Odometry (VO)", "NDT Mapping"],
      metric: t("card_1_metric"),
      metricLabel: t("card_1_label"),
      icon: Compass,
    },
    {
      id: "planning",
      category: "otonomi",
      number: "02",
      badge: t("card_2_badge"),
      title: t("card_2_title"),
      desc: t("card_2_desc"),
      tags: ["Hybrid A*", "RRT* Pathfinding", "DWA Local Avoidance", "Dynamic Costmap"],
      metric: t("card_2_metric"),
      metricLabel: t("card_2_label"),
      icon: Layers,
    },
    {
      id: "threat",
      category: "tehdit",
      number: "03",
      badge: t("card_3_badge"),
      title: t("card_3_title"),
      desc: t("card_3_desc"),
      tags: ["GPR Radar Fusion", "Thermal Anomaly", "Plume Dispersion", "30m Quarantine Ring"],
      metric: t("card_3_metric"),
      metricLabel: t("card_3_label"),
      icon: Radar,
    },
    {
      id: "swarm",
      category: "suru",
      number: "04",
      badge: t("card_4_badge"),
      title: t("card_4_title"),
      desc: t("card_4_desc"),
      tags: ["UAV-UGV Synchronization", "Mesh Ad-Hoc Network", "Multi-Agent Consensus", "Tactical Formations"],
      metric: t("card_4_metric"),
      metricLabel: t("card_4_label"),
      icon: Radio,
    },
    {
      id: "cyber",
      category: "siber",
      number: "05",
      badge: t("card_5_badge"),
      title: t("card_5_title"),
      desc: t("card_5_desc"),
      tags: ["HMAC-SHA256", "Anti-Spoofing Guard", "LinkLoss RTH", "Hardware E-Stop"],
      metric: t("card_5_metric"),
      metricLabel: t("card_5_label"),
      icon: Lock,
    },
    {
      id: "ros2",
      category: "test",
      number: "06",
      badge: t("card_6_badge"),
      title: t("card_6_title"),
      desc: t("card_6_desc"),
      tags: ["ROS 2 Humble Core", "SocketCAN Bridge", "400Hz ESKF Fusion", "STANAG 4586 Level 4"],
      metric: t("card_6_metric"),
      metricLabel: t("card_6_label"),
      icon: Cpu,
    },
  ];

  const filteredFeatures = activeTab === "all" ? techFeatures : techFeatures.filter(f => f.category === activeTab);

  return (
    <section id="otonomi" className="relative z-20 py-12 sm:py-24 px-4 sm:px-12 bg-[#090b0e] border-t border-white/10">
      {/* Background Subtle Radar Lines */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(200,255,0,0.05),rgba(255,255,255,0))]" />

      <div className="max-w-6xl mx-auto relative z-10">
        
        {/* Section Title & Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-12 gap-4 sm:gap-6">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-[11px] sm:text-xs font-mono font-bold tracking-widest uppercase mb-2 sm:mb-3">
              <Crosshair className="w-3.5 h-3.5" />
              <span>{t("matrix_badge")}</span>
            </div>
            <h3 className="text-2xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight">
              {t("matrix_title")}
            </h3>
          </div>
          <p className="text-slate-400 text-xs sm:text-sm font-normal max-w-md leading-relaxed border-l-2 border-[#C8FF00] pl-3 sm:pl-4">
            {t("matrix_desc")}
          </p>
        </div>

        {/* Filter Tabs (Horizontal Smooth Scroll on Mobile, Full Row on Desktop) */}
        <div className="flex flex-nowrap overflow-x-auto gap-2 mb-6 sm:mb-10 pb-3 border-b border-white/10 no-scrollbar scrollbar-none">
          <button
            onClick={() => setActiveTab("all")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "all"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_all")}
          </button>
          <button
            onClick={() => setActiveTab("otonomi")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "otonomi"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_otonomi")}
          </button>
          <button
            onClick={() => setActiveTab("tehdit")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "tehdit"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_tehdit")}
          </button>
          <button
            onClick={() => setActiveTab("suru")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "suru"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_suru")}
          </button>
          <button
            onClick={() => setActiveTab("siber")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "siber"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_siber")}
          </button>
          <button
            onClick={() => setActiveTab("test")}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[11px] sm:text-xs font-mono font-bold tracking-wider shrink-0 transition-all cursor-pointer ${
              activeTab === "test"
                ? "bg-[#C8FF00] text-black shadow-[0_0_15px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            {t("tab_test")}
          </button>
        </div>

        {/* ========================================================================= */}
        {/* 1. MOBILE-ONLY VIEW (sm:hidden) — Horizontal Snap-Scroll Card Carousel   */}
        {/* ========================================================================= */}
        <div className="block sm:hidden space-y-4">
          <div 
            onScroll={(e) => {
              const el = e.currentTarget;
              const idx = Math.round(el.scrollLeft / (el.clientWidth * 0.85));
              setMobileCardIndex(Math.min(filteredFeatures.length - 1, Math.max(0, idx)));
            }}
            className="flex overflow-x-auto snap-x snap-mandatory gap-3.5 pb-2 pt-1 px-1 scrollbar-none no-scrollbar"
            style={{ scrollbarWidth: "none", msOverflowStyle: "none" }}
          >
            {filteredFeatures.map((item) => {
              const ItemIcon = item.icon;
              return (
                <div
                  key={item.id}
                  className="snap-center shrink-0 w-[86vw] max-w-[340px] p-5 rounded-2xl bg-[#0c0f16] border border-white/15 shadow-2xl flex flex-col justify-between"
                >
                  <div className="space-y-3">
                    {/* Top Header: Number & Icon */}
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-1.5">
                        <span className="font-mono text-xs font-bold text-[#C8FF00]">{item.number} //</span>
                        <span className="font-mono text-[9px] uppercase tracking-wider text-slate-300 font-bold bg-white/5 px-2 py-0.5 rounded border border-white/10">
                          {item.badge}
                        </span>
                      </div>
                      <div className="p-2 rounded-xl bg-white/5 text-[#C8FF00]">
                        <ItemIcon className="w-4 h-4" />
                      </div>
                    </div>

                    {/* Title & Desc */}
                    <div>
                      <h4 className="text-base font-bold text-white mb-1.5 leading-snug">
                        {item.title}
                      </h4>
                      <p className="text-slate-400 text-[11px] leading-relaxed font-normal">
                        {item.desc}
                      </p>
                    </div>

                    {/* Tags */}
                    <div className="flex flex-wrap gap-1 pt-1">
                      {item.tags.map((tag, idx) => (
                        <span
                          key={idx}
                          className="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white/[0.04] border border-white/10 text-slate-300"
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Bottom Metric Bar */}
                  <div className="pt-4 mt-4 border-t border-white/10 flex items-end justify-between">
                    <div>
                      <div className="text-lg font-mono font-black text-[#C8FF00]">
                        {item.metric}
                      </div>
                      <div className="text-[9px] font-mono text-slate-400 uppercase tracking-wider">
                        {item.metricLabel}
                      </div>
                    </div>
                    <span className="text-[9px] font-mono text-[#C8FF00] font-bold bg-[#C8FF00]/10 px-2 py-0.5 rounded border border-[#C8FF00]/30">
                      MIL-SPEC
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Swipe Indicator Dots & Swipe Hint */}
          <div className="flex items-center justify-between pt-2 px-2">
            <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
              ← {lang === "tr" ? "KATMANLARI KAYDIRIN" : "SWIPE LAYERS"} →
            </span>

            {/* Glowing Dots */}
            <div className="flex items-center gap-1.5">
              {filteredFeatures.map((_, dotIdx) => (
                <span
                  key={dotIdx}
                  className={`transition-all duration-300 rounded-full ${
                    dotIdx === mobileCardIndex
                      ? "w-4 h-1.5 bg-[#C8FF00] shadow-[0_0_8px_rgba(200,255,0,0.8)]"
                      : "w-1.5 h-1.5 bg-white/20"
                  }`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* 2. DESKTOP VIEW (hidden sm:grid) — 100% UNTOUCHED 3-COLUMN ORIGINAL GRID */}
        {/* ========================================================================= */}
        <div className="hidden sm:grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredFeatures.map((item) => {
            const ItemIcon = item.icon;
            return (
              <div
                key={item.id}
                className="p-7 rounded-2xl bg-[#0c0f16] border border-white/10 hover:border-[#C8FF00]/50 transition-all duration-300 group flex flex-col justify-between hover:shadow-[0_10px_30px_rgba(200,255,0,0.1)] relative overflow-hidden"
              >
                <div className="space-y-4">
                  {/* Top Bar: Number & Icon */}
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold text-[#C8FF00]">{item.number} //</span>
                      <span className="font-mono text-[10px] uppercase tracking-wider text-slate-400 font-bold bg-white/5 px-2 py-0.5 rounded border border-white/10">
                        {item.badge}
                      </span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-white/5 text-[#C8FF00] group-hover:bg-[#C8FF00]/10 transition-colors">
                      <ItemIcon className="w-5 h-5" />
                    </div>
                  </div>

                  {/* Title & Desc */}
                  <div>
                    <h4 className="text-lg font-bold text-white mb-2 group-hover:text-[#C8FF00] transition-colors leading-snug">
                      {item.title}
                    </h4>
                    <p className="text-slate-400 text-xs leading-relaxed font-normal">
                      {item.desc}
                    </p>
                  </div>

                  {/* Tags */}
                  <div className="flex flex-wrap gap-1.5 pt-2">
                    {item.tags.map((tag, idx) => (
                      <span
                        key={idx}
                        className="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.03] border border-white/5 text-slate-400"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Bottom Metric Bar */}
                <div className="pt-6 mt-6 border-t border-white/10 flex items-end justify-between">
                  <div>
                    <div className="text-xl font-mono font-black text-white group-hover:text-[#C8FF00] transition-colors">
                      {item.metric}
                    </div>
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                      {item.metricLabel}
                    </div>
                  </div>
                  <div className="text-[10px] font-mono text-[#C8FF00] flex items-center gap-1 font-bold group-hover:translate-x-1 transition-transform">
                    <span>MIL-SPEC</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
