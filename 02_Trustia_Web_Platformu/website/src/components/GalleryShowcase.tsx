"use client";

import { useState } from "react";
import { ShieldCheck, Cpu, Radio, Eye, ChevronLeft, ChevronRight } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function GalleryShowcase() {
  const { lang, t } = useLanguage();
  const [activeSlide, setActiveSlide] = useState(0);

  const photos = [
    { src: "/gallery/1.webp", title: t("gallery_p1_title"), badge: t("gallery_p1_badge"), alt: "HAVELSAN BARKAN UGV" },
    { src: "/gallery/2.jpg", title: t("gallery_p2_title"), badge: t("gallery_p2_badge"), alt: "OTOKAR ALPAR UGV" },
    { src: "/gallery/3.jpeg", title: t("gallery_p3_title"), badge: t("gallery_p3_badge"), alt: "Obstacle Avoidance UGV" },
    { src: "/gallery/4.jpg", title: t("gallery_p4_title"), badge: t("gallery_p4_badge"), alt: "HAVELSAN KAPGAN 8x8 UGV" },
    { src: "/gallery/5.jpg", title: t("gallery_p5_title"), badge: t("gallery_p5_badge"), alt: "ENGA 6x6 Tactical UGV" },
  ];

  return (
    <section className="relative w-full py-12 sm:py-16 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#090c10] border-t border-b border-white/10">
      
      {/* Section Header */}
      <div className="text-center max-w-2xl mx-auto mb-8 sm:mb-12 space-y-2.5 sm:space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-[11px] sm:text-xs font-mono font-bold tracking-widest uppercase">
          <Eye className="w-3.5 h-3.5" />
          <span>{t("gallery_badge")}</span>
        </div>
        <h3 className="text-xl sm:text-3xl md:text-4xl font-extrabold text-white tracking-tight">
          {t("gallery_title")}
        </h3>
        <p className="text-slate-400 text-xs sm:text-sm font-normal">
          {t("gallery_desc")}
        </p>
      </div>

      {/* ========================================================================= */}
      {/* 1. MOBILE-ONLY VIEW (sm:hidden) — Sleek Touch Slider & Compact Telemetry */}
      {/* ========================================================================= */}
      <div className="block sm:hidden space-y-6">
        
        {/* Mobile Horizontal Snap-Scroll Swipe Carousel */}
        <div className="relative">
          <div 
            onScroll={(e) => {
              const el = e.currentTarget;
              const slide = Math.round(el.scrollLeft / (el.clientWidth * 0.85));
              setActiveSlide(Math.min(photos.length - 1, Math.max(0, slide)));
            }}
            className="flex overflow-x-auto snap-x snap-mandatory gap-3.5 pb-2 pt-1 px-1 scrollbar-none no-scrollbar"
            style={{ scrollbarWidth: "none", msOverflowStyle: "none" }}
          >
            {photos.map((p, idx) => (
              <div 
                key={idx}
                className="snap-center shrink-0 w-[86vw] max-w-[340px] relative group rounded-2xl overflow-hidden border border-white/15 shadow-2xl aspect-[16/10] bg-[#07090c]"
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={p.src}
                  alt={p.alt}
                  className="w-full h-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent"></div>
                <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
                  <span className="font-bold text-white text-[11px] tracking-wide">{p.title}</span>
                  <span className="text-[#C8FF00] text-[9px] bg-black/70 px-2 py-0.5 rounded border border-[#C8FF00]/30 font-bold shadow-md">
                    {p.badge}
                  </span>
                </div>
              </div>
            ))}
          </div>

          {/* Swipe Indicator Dots & Swipe Hint */}
          <div className="flex items-center justify-between pt-3 px-2">
            <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider flex items-center gap-1">
              <span>← {lang === "tr" ? "KAYDIRIN" : "SWIPE"} →</span>
            </span>

            {/* Glowing Indicator Dots */}
            <div className="flex items-center gap-1.5">
              {photos.map((_, dotIdx) => (
                <span
                  key={dotIdx}
                  className={`transition-all duration-300 rounded-full ${
                    dotIdx === activeSlide
                      ? "w-5 h-1.5 bg-[#C8FF00] shadow-[0_0_8px_rgba(200,255,0,0.8)]"
                      : "w-1.5 h-1.5 bg-white/20"
                  }`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* Mobile Telemetry & Cyber Security Compact Grid (2 Columns) */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
          
          {/* Telemetry Card 1 */}
          <div className="p-4 rounded-xl bg-[#0c1017] border border-white/15 space-y-2 shadow-lg">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Cpu className="w-3.5 h-3.5" />
                <span>{t("gallery_card1_badge")}</span>
              </div>
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-emerald-400">
                <span>{t("gallery_card1_status")}</span>
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              </div>
            </div>
            <h4 className="text-xs font-bold text-white">{t("gallery_card1_title")}</h4>
            <p className="text-slate-400 text-[11px] leading-relaxed font-normal">
              {t("gallery_card1_desc")}
            </p>
          </div>

          {/* Security Card 2 */}
          <div className="p-4 rounded-xl bg-[#0c1017] border border-white/15 space-y-2 shadow-lg">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Radio className="w-3.5 h-3.5" />
                <span>{t("gallery_card2_badge")}</span>
              </div>
              <div className="flex items-center gap-1 text-[10px] font-mono text-[#C8FF00]">
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>STANAG 4586</span>
              </div>
            </div>
            <h4 className="text-xs font-bold text-white">{t("gallery_card2_title")}</h4>
            <p className="text-slate-400 text-[11px] leading-relaxed font-normal">
              {t("gallery_card2_desc")}
            </p>
          </div>

        </div>

      </div>

      {/* ========================================================================= */}
      {/* 2. DESKTOP VIEW (hidden sm:block) — 100% UNTOUCHED ORIGINAL 2-ROW GRID   */}
      {/* ========================================================================= */}
      <div className="hidden sm:block max-w-6xl mx-auto space-y-6">
        
        {/* ROW 1: 3 Rectangular 16:9 Photos Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          
          {/* Photo 1: HAVELSAN BARKAN UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/1.webp"
              alt="HAVELSAN BARKAN UGV Field Terrain Trial"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">{t("gallery_p1_title")}</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">{t("gallery_p1_badge")}</span>
            </div>
          </div>

          {/* Photo 2: OTOKAR ALPAR Heavy UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/2.jpg"
              alt="OTOKAR ALPAR Sensor Fusion & Radar"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">{t("gallery_p2_title")}</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">{t("gallery_p2_badge")}</span>
            </div>
          </div>

          {/* Photo 3: Tactical Offroad High Mobility UGV Chassis */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/3.jpeg"
              alt="Tactical Autonomous Obstacle Avoidance Trial"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">{t("gallery_p3_title")}</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">{t("gallery_p3_badge")}</span>
            </div>
          </div>

        </div>

        {/* ROW 2: 2 Center Photos (Exact 16:9 Aspect Ratio) + Left & Right Flanking Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 items-center">
          
          {/* LEFT BOŞLUK DOLGUSU: Tactical Telemetry Card 1 */}
          <div className="p-5 rounded-2xl bg-[#0e121a] border border-white/10 flex flex-col justify-between aspect-video shadow-2xl">
            <div className="space-y-1.5">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Cpu className="w-3.5 h-3.5" />
                <span>{t("gallery_card1_badge")}</span>
              </div>
              <h4 className="text-xs font-bold text-white">{t("gallery_card1_title")}</h4>
              <p className="text-slate-400 text-[11px] leading-relaxed font-normal line-clamp-2">
                {t("gallery_card1_desc")}
              </p>
            </div>
            <div className="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono text-emerald-400">
              <span>{t("gallery_card1_status")}</span>
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            </div>
          </div>

          {/* CENTER Photo 4: HAVELSAN KAPGAN 8x8 Heavy UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/4.jpg"
              alt="HAVELSAN KAPGAN 8x8 Heavy UGV Threat Fusion"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">{t("gallery_p4_title")}</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">{t("gallery_p4_badge")}</span>
            </div>
          </div>

          {/* CENTER Photo 5: ENGA 6x6 Tactical UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/5.jpg"
              alt="ENGA 6x6 Tactical UGV Multi-Agent Swarm"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">{t("gallery_p5_title")}</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">{t("gallery_p5_badge")}</span>
            </div>
          </div>

          {/* RIGHT BOŞLUK DOLGUSU: Tactical Cyber Security Card 2 */}
          <div className="p-5 rounded-2xl bg-[#0e121a] border border-white/10 flex flex-col justify-between aspect-video shadow-2xl">
            <div className="space-y-1.5">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Radio className="w-3.5 h-3.5" />
                <span>{t("gallery_card2_badge")}</span>
              </div>
              <h4 className="text-xs font-bold text-white">{t("gallery_card2_title")}</h4>
              <p className="text-slate-400 text-[11px] leading-relaxed font-normal line-clamp-2">
                {t("gallery_card2_desc")}
              </p>
            </div>
            <div className="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono text-[#C8FF00]">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>STANAG 4586</span>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
