"use client";

import Image from "next/image";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { lang } = useLanguage();

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-8 bg-[#06080b] border-t border-b border-white/10">
      <div className="max-w-5xl mx-auto space-y-6">
        
        {/* Subtle, Minimalist Header */}
        <div className="text-center">
          <span className="text-[11px] sm:text-xs font-mono font-bold tracking-[0.25em] text-slate-400 uppercase">
            {lang === "tr" ? "DESTEKLEYEN KURUMLAR & EKOSİSTEM" : "SUPPORTING INSTITUTIONS & ECOSYSTEM"}
          </span>
        </div>

        {/* 3D Official Institutional Showcase (Exactly matching the video in 100% crisp 3D quality) */}
        <div className="relative w-full rounded-2xl overflow-hidden border border-white/10 shadow-[0_20px_50px_rgba(0,0,0,0.8)] bg-[#07090c] group">
          <Image
            src="/accreditations-showcase.jpg"
            alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
            width={1280}
            height={720}
            className="w-full h-auto object-cover object-center group-hover:scale-[1.01] transition-transform duration-700 filter contrast-105 brightness-100"
            priority
          />
        </div>

      </div>
    </section>
  );
}
