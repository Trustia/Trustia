"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import CorporateContactForm from "@/components/CorporateContactForm";
import Link from "next/link";
import { ArrowLeft, Mail, MapPin, Clock, Send, ShieldCheck } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function ContactPage() {
  const { lang, t } = useLanguage();

  return (
    <main className="min-h-screen bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black">
      <Navbar />

      {/* Hero Header (Mobile-optimized padding, desktop 100% untouched) */}
      <section className="pt-24 sm:pt-32 pb-8 sm:pb-12 px-4 sm:px-6 bg-[#0b0e14] border-b border-white/10 relative overflow-hidden">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none" />

        <div className="max-w-6xl mx-auto relative z-10">
          <div className="flex flex-col items-start gap-2.5 sm:gap-3 mb-4 sm:mb-6">
            <Link
              href="/"
              className="inline-flex items-center gap-2 text-xs font-mono text-slate-400 hover:text-[#C8FF00] transition-colors group"
            >
              <ArrowLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4 group-hover:-translate-x-1 transition-transform" />
              <span>{t("contact_back")}</span>
            </Link>

            <div className="inline-flex items-center gap-2 px-2.5 sm:px-3 py-0.5 sm:py-1 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-[10px] sm:text-xs font-mono font-bold tracking-wider uppercase">
              <span>{t("contact_page_badge")}</span>
            </div>
          </div>

          <h1 className="text-2xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight mb-2 sm:mb-3">
            {t("contact_page_title")}
          </h1>
          <p className="text-slate-400 text-xs sm:text-sm md:text-base max-w-2xl font-normal leading-relaxed">
            {t("contact_page_desc")}
          </p>
        </div>
      </section>

      {/* Main Content Layout */}
      <section className="py-8 sm:py-16 px-4 sm:px-6 max-w-6xl mx-auto font-sans">
        
        {/* ========================================================================= */}
        {/* 1. MOBILE-ONLY VIEW (lg:hidden) — Sleek Quick Directory & Integrated Form */}
        {/* ========================================================================= */}
        <div className="block lg:hidden space-y-6">
          
          {/* Mobile Quick Department Email Pills */}
          <div className="p-4 rounded-2xl bg-[#0c1017] border border-white/10 space-y-3 shadow-lg">
            <div className="flex items-center justify-between border-b border-white/10 pb-2.5">
              <div className="flex items-center gap-2 text-[#C8FF00] font-mono text-xs font-bold uppercase tracking-wider">
                <Mail className="w-4 h-4" />
                <span>{t("contact_dept_title")}</span>
              </div>
              <span className="text-[10px] font-mono text-slate-400">7/24 Aktif</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-[11px]">
              <a 
                href="mailto:iletisim@trustia.com.tr" 
                className="p-2.5 rounded-xl bg-white/[0.03] border border-white/5 flex items-center justify-between hover:border-[#C8FF00]/40 transition-colors"
              >
                <span className="text-slate-300">Genel Santral:</span>
                <span className="text-[#C8FF00] font-bold">iletisim@trustia.com.tr</span>
              </a>

              <a 
                href="mailto:entegrasyon@trustia.com.tr" 
                className="p-2.5 rounded-xl bg-white/[0.03] border border-white/5 flex items-center justify-between hover:border-[#C8FF00]/40 transition-colors"
              >
                <span className="text-slate-300">Teknik SDK:</span>
                <span className="text-[#C8FF00] font-bold">entegrasyon@trustia.com.tr</span>
              </a>

              <a 
                href="mailto:kariyer@trustia.com.tr" 
                className="p-2.5 rounded-xl bg-white/[0.03] border border-white/5 flex items-center justify-between hover:border-[#C8FF00]/40 transition-colors"
              >
                <span className="text-slate-300">Kariyer & İK:</span>
                <span className="text-[#C8FF00] font-bold">kariyer@trustia.com.tr</span>
              </a>

              <a 
                href="mailto:hukuk@trustia.com.tr" 
                className="p-2.5 rounded-xl bg-white/[0.03] border border-white/5 flex items-center justify-between hover:border-[#C8FF00]/40 transition-colors"
              >
                <span className="text-slate-300">Hukuk & Lisans:</span>
                <span className="text-[#C8FF00] font-bold">hukuk@trustia.com.tr</span>
              </a>
            </div>

            {/* Compact Location info */}
            <div className="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono text-slate-400">
              <span className="flex items-center gap-1.5 text-slate-300">
                <MapPin className="w-3.5 h-3.5 text-[#C8FF00]" />
                <span>USA (Delaware Inc.) • TR (İstanbul)</span>
              </span>
              <span className="text-[#C8FF00]">24 Saat Yanıt</span>
            </div>
          </div>

          {/* Mobile Form Component */}
          <div>
            <CorporateContactForm />
          </div>
        </div>

        {/* ========================================================================= */}
        {/* 2. DESKTOP VIEW (hidden lg:grid) — 100% UNTOUCHED ORIGINAL 2-COLUMN GRID */}
        {/* ========================================================================= */}
        <div className="hidden lg:grid lg:grid-cols-12 gap-12">
          
          {/* Left Column: Contact Cards & Email Addresses */}
          <div className="lg:col-span-5 space-y-6">
            
            {/* Primary Email Card */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/40 transition-colors">
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <Mail className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">{t("contact_gen_badge")}</h4>
                  <a
                    href="mailto:iletisim@trustia.com.tr"
                    className="text-base sm:text-lg font-bold text-white hover:text-[#C8FF00] transition-colors font-mono"
                  >
                    iletisim@trustia.com.tr
                  </a>
                </div>
              </div>
              <p className="text-slate-400 text-xs leading-relaxed border-t border-white/10 pt-3">
                {t("contact_gen_note")}
              </p>
            </div>

            {/* Department Email Addresses */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4">
              <h5 className="font-mono text-xs font-bold text-white uppercase tracking-wider border-b border-white/10 pb-3">
                {t("contact_dept_title")}
              </h5>

              <div className="space-y-3 font-mono text-xs">
                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">{t("contact_dept_tech")}</span>
                  <a href="mailto:entegrasyon@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    entegrasyon@trustia.com.tr
                  </a>
                </div>

                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">{t("contact_dept_hr")}</span>
                  <a href="mailto:kariyer@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    kariyer@trustia.com.tr
                  </a>
                </div>

                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">{t("contact_dept_legal")}</span>
                  <a href="mailto:hukuk@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    hukuk@trustia.com.tr
                  </a>
                </div>

                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">{t("contact_dept_invest")}</span>
                  <a href="mailto:kariyer@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    kariyer@trustia.com.tr
                  </a>
                </div>
              </div>
            </div>

            {/* Location & Hours Card */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4">
              <div className="flex items-start gap-3">
                <MapPin className="w-5 h-5 text-[#C8FF00] shrink-0 mt-0.5" />
                <div>
                  <h5 className="font-mono text-xs font-bold text-white uppercase tracking-wider">{t("contact_loc_title")}</h5>
                  <p className="text-slate-400 text-xs mt-1">
                    {t("contact_loc_hq")}
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3 border-t border-white/10 pt-4">
                <Clock className="w-5 h-5 text-[#C8FF00] shrink-0 mt-0.5" />
                <div>
                  <h5 className="font-mono text-xs font-bold text-white uppercase tracking-wider">{t("contact_hours_title")}</h5>
                  <p className="text-slate-400 text-xs mt-1">
                    {t("contact_hours_desc")}
                  </p>
                </div>
              </div>
            </div>

          </div>

          {/* Right Column: Interactive Multi-Department Form */}
          <div className="lg:col-span-7">
            <CorporateContactForm />
          </div>

        </div>
      </section>

      <Footer />
    </main>
  );
}
