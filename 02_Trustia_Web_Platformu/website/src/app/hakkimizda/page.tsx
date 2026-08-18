"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { ArrowLeft, Shield, Cpu, Target, Award, CheckCircle2, Lock, Terminal, Radio, MapPin, Building } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function AboutPage() {
  const { lang, t } = useLanguage();

  return (
    <main className="min-h-screen bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black">
      <Navbar />

      {/* Hero Header (Responsive spacing, desktop 100% untouched) */}
      <section className="pt-24 sm:pt-32 pb-10 sm:pb-16 px-4 sm:px-6 bg-[#0b0e14] border-b border-white/10 relative overflow-hidden">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none" />

        <div className="max-w-6xl mx-auto relative z-10">
          <div className="flex flex-col items-start gap-2.5 sm:gap-3 mb-4 sm:mb-6">
            <Link
              href="/"
              className="inline-flex items-center gap-2 text-xs font-mono text-slate-400 hover:text-[#C8FF00] transition-colors group"
            >
              <ArrowLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4 group-hover:-translate-x-1 transition-transform" />
              <span>{t("about_back")}</span>
            </Link>

            <div className="inline-flex items-center gap-2 px-2.5 sm:px-3 py-0.5 sm:py-1 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-[10px] sm:text-xs font-mono font-bold tracking-wider uppercase">
              <span>{t("about_badge")}</span>
            </div>
          </div>

          <h1 className="text-2xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight mb-3 sm:mb-4">
            {t("about_title")}
          </h1>
          <p className="text-slate-300 text-xs sm:text-sm md:text-base max-w-3xl font-normal leading-relaxed">
            {t("about_desc")}
          </p>
        </div>
      </section>

      {/* Main Content Sections */}
      <section className="py-10 sm:py-16 px-4 sm:px-6 max-w-6xl mx-auto">
        
        {/* ========================================================================= */}
        {/* 1. MOBILE-ONLY VIEW (lg:hidden) — Sleek Compact Mobile About Layout      */}
        {/* ========================================================================= */}
        <div className="block lg:hidden space-y-6">
          
          {/* Mobile 3 Strategic Pillars (Compact Grid) */}
          <div className="grid grid-cols-1 gap-3.5">
            {/* Pillar 1 */}
            <div className="p-4 rounded-xl bg-[#0c1017] border border-white/10 space-y-2 shadow-lg">
              <div className="flex items-center gap-2.5">
                <div className="p-2 rounded-lg bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <Shield className="w-4 h-4" />
                </div>
                <h3 className="text-sm font-bold text-white tracking-tight">
                  {t("about_c1_title")}
                </h3>
              </div>
              <p className="text-slate-400 text-xs leading-relaxed pl-1">
                {t("about_c1_desc")}
              </p>
            </div>

            {/* Pillar 2 */}
            <div className="p-4 rounded-xl bg-[#0c1017] border border-white/10 space-y-2 shadow-lg">
              <div className="flex items-center gap-2.5">
                <div className="p-2 rounded-lg bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <Cpu className="w-4 h-4" />
                </div>
                <h3 className="text-sm font-bold text-white tracking-tight">
                  {t("about_c2_title")}
                </h3>
              </div>
              <p className="text-slate-400 text-xs leading-relaxed pl-1">
                {t("about_c2_desc")}
              </p>
            </div>

            {/* Pillar 3 */}
            <div className="p-4 rounded-xl bg-[#0c1017] border border-white/10 space-y-2 shadow-lg">
              <div className="flex items-center gap-2.5">
                <div className="p-2 rounded-lg bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <Target className="w-4 h-4" />
                </div>
                <h3 className="text-sm font-bold text-white tracking-tight">
                  {t("about_c3_title")}
                </h3>
              </div>
              <p className="text-slate-400 text-xs leading-relaxed pl-1">
                {t("about_c3_desc")}
              </p>
            </div>
          </div>

          {/* Mobile Founder & Leadership Card */}
          <div className="p-5 rounded-2xl bg-[#0c1017] border border-white/15 space-y-3 shadow-xl">
            <div className="space-y-1.5">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-[10px] font-mono font-bold tracking-widest uppercase">
                <Award className="w-3 h-3" />
                <span>{t("about_founder_badge")}</span>
              </div>
              <h3 className="text-xl font-extrabold text-white tracking-tight">
                {t("about_founder_title")}
              </h3>
              <p className="text-xs font-mono text-[#C8FF00] font-bold">
                {t("about_founder_role")}
              </p>
              <p className="text-slate-300 text-xs leading-relaxed pt-1">
                {t("about_founder_bio")}
              </p>
            </div>

            {/* Credentials Badges on Mobile */}
            <div className="p-3.5 rounded-xl bg-black/50 border border-white/10 space-y-2 font-mono text-[11px] text-slate-300">
              <div className="flex items-center gap-2 text-[#C8FF00] font-bold">
                <CheckCircle2 className="w-3.5 h-3.5 shrink-0" />
                <span>KOSGEB İleri Girişimci #2026</span>
              </div>
              <div className="flex items-center gap-2 text-white">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                <span>BTK & SSB Savunma Sanayii Akademi</span>
              </div>
              <div className="flex items-center gap-2 text-white">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                <span>Delaware C-Corp Inc. (USA)</span>
              </div>
            </div>
          </div>

          {/* Mobile Architecture & Standards */}
          <div className="p-4 rounded-xl bg-[#07090c] border border-white/10 space-y-2.5">
            <h4 className="text-sm font-bold text-white tracking-tight">
              {t("about_arch_title")}
            </h4>
            <p className="text-slate-400 text-xs leading-relaxed">
              {t("about_arch_desc")}
            </p>
            <div className="pt-2 flex flex-wrap gap-1.5 font-mono text-[10px]">
              <span className="px-2.5 py-1 rounded bg-white/5 border border-white/10 text-slate-300">STANAG 4586 L4</span>
              <span className="px-2.5 py-1 rounded bg-white/5 border border-white/10 text-slate-300">SAE AS6091 (JAUS)</span>
              <span className="px-2.5 py-1 rounded bg-white/5 border border-white/10 text-slate-300">ISO 26262 ASIL-D</span>
              <span className="px-2.5 py-1 rounded bg-white/5 border border-white/10 text-slate-300">ROS 2 Humble</span>
            </div>
          </div>

        </div>

        {/* ========================================================================= */}
        {/* 2. DESKTOP VIEW (hidden lg:block) — 100% UNTOUCHED ORIGINAL DESKTOP GRID */}
        {/* ========================================================================= */}
        <div className="hidden lg:block">
          
          {/* Executive Summary 3-Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
            <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
              <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
                <Shield className="w-6 h-6" />
              </div>
              <h3 className="text-lg font-bold text-white tracking-tight">
                {t("about_c1_title")}
              </h3>
              <p className="text-slate-400 text-xs leading-relaxed">
                {t("about_c1_desc")}
              </p>
            </div>

            <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
              <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
                <Cpu className="w-6 h-6" />
              </div>
              <h3 className="text-lg font-bold text-white tracking-tight">
                {t("about_c2_title")}
              </h3>
              <p className="text-slate-400 text-xs leading-relaxed">
                {t("about_c2_desc")}
              </p>
            </div>

            <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
              <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
                <Target className="w-6 h-6" />
              </div>
              <h3 className="text-lg font-bold text-white tracking-tight">
                {t("about_c3_title")}
              </h3>
              <p className="text-slate-400 text-xs leading-relaxed">
                {t("about_c3_desc")}
              </p>
            </div>
          </div>

          {/* Founder & Lead Profile */}
          <div className="p-8 sm:p-10 rounded-3xl bg-[#0c1017] border border-white/10 relative overflow-hidden mb-16">
            <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
              <div className="space-y-3 max-w-2xl">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-xs font-mono font-bold tracking-widest uppercase">
                  <Award className="w-3.5 h-3.5" />
                  <span>{t("about_founder_badge")}</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                  {t("about_founder_title")}
                </h3>
                <p className="text-sm font-mono text-[#C8FF00] font-bold">
                  {t("about_founder_role")}
                </p>
                <p className="text-slate-300 text-xs sm:text-sm leading-relaxed font-normal pt-2">
                  {t("about_founder_bio")}
                </p>
              </div>

              <div className="p-6 rounded-2xl bg-black/40 border border-white/10 space-y-3 shrink-0 font-mono text-xs text-slate-300 w-full md:w-auto">
                <div className="flex items-center gap-2 text-[#C8FF00] font-bold">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>KOSGEB İleri Girişimci #2026</span>
                </div>
                <div className="flex items-center gap-2 text-white">
                  <CheckCircle2 className="w-4 h-4 text-[#C8FF00]" />
                  <span>BTK & SSB Savunma Akademisi</span>
                </div>
                <div className="flex items-center gap-2 text-white">
                  <CheckCircle2 className="w-4 h-4 text-[#C8FF00]" />
                  <span>Delaware C-Corp Inc. (USA)</span>
                </div>
              </div>
            </div>
          </div>

          {/* Architecture & Integration Details */}
          <div className="p-8 rounded-3xl bg-[#07090c] border border-white/10 space-y-4">
            <h4 className="text-xl font-bold text-white tracking-tight">
              {t("about_arch_title")}
            </h4>
            <p className="text-slate-400 text-xs sm:text-sm leading-relaxed font-normal">
              {t("about_arch_desc")}
            </p>
            <div className="pt-4 flex flex-wrap gap-3">
              <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-xs font-mono text-slate-300">
                STANAG 4586 L4
              </span>
              <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-xs font-mono text-slate-300">
                SAE AS6091 (JAUS)
              </span>
              <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-xs font-mono text-slate-300">
                ISO 26262 ASIL-D
              </span>
              <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-xs font-mono text-slate-300">
                ROS 2 Humble
              </span>
            </div>
          </div>

        </div>

      </section>

      <Footer />
    </main>
  );
}
