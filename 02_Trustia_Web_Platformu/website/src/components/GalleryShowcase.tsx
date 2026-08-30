"use client";

import { useState } from "react";
import { ShieldCheck, Cpu, Eye } from "lucide-react";
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
    <section className="relative w-full py-16 sm:py-20 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#07090c] border-b border-white/10">
      
      {/* Section Header */}
      <div className="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-3">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
          <Eye className="w-3.5 h-3.5 text-slate-400" />
          <span>{t("gallery_badge")}</span>
        </div>
        <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          {t("gallery_title")}
        </h3>
        <p className="text-slate-400 text-xs sm:text-sm font-normal">
          {t("gallery_desc")}
        </p>
      </div>

      {/* Mobile Swipe View */}
      <div className="block sm:hidden space-y-6">
        <div className="flex overflow-x-auto snap-x snap-mandatory gap-3.5 pb-2 pt-1 px-1 scrollbar-none no-scrollbar">
          {photos.map((p, idx) => (
            <div 
              key={idx}
              className="snap-center shrink-0 w-[86vw] max-w-[340px] relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-[16/10] bg-[#07090c]"
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
                <span className="text-slate-200 text-[9px] bg-black/70 px-2 py-0.5 rounded border border-white/20 font-bold shadow-md">
                  {p.badge}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Desktop Clean Grid */}
      <div className="hidden sm:block max-w-6xl mx-auto space-y-6">
        {/* ROW 1: 3 Photos */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          {photos.slice(0, 3).map((p, idx) => (
            <div key={idx} className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#0c0f14]">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={p.src}
                alt={p.alt}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
              <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
                <span className="font-bold text-white text-[11px]">{p.title}</span>
                <span className="text-slate-200 text-[9px] bg-black/70 px-2 py-0.5 rounded border border-white/20 font-bold">{p.badge}</span>
              </div>
            </div>
          ))}
        </div>

        {/* ROW 2: 2 Photos */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {photos.slice(3, 5).map((p, idx) => (
            <div key={idx} className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#0c0f14]">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={p.src}
                alt={p.alt}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
              <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
                <span className="font-bold text-white text-[11px]">{p.title}</span>
                <span className="text-slate-200 text-[9px] bg-black/70 px-2 py-0.5 rounded border border-white/20 font-bold">{p.badge}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

    </section>
  );
}
