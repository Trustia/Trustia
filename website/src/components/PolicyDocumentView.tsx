"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { ArrowLeft, CheckCircle2, ShieldCheck, ArrowRight, Printer, FileText, Award, Lock, Scale, Globe, Shield } from "lucide-react";

const iconMap: Record<string, any> = {
  FileText,
  Award,
  Lock,
  ShieldCheck,
  Scale,
  Globe,
  Shield,
};

export default function PolicyDocumentView({
  currentSlug,
  policy,
  policyData,
}: {
  currentSlug: string;
  policy: any;
  policyData: Record<string, any>;
}) {
  const IconComponent = iconMap[policy.iconName] || FileText;

  return (
    <main className="min-h-screen bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black">
      {/* 1. Header Navbar */}
      <Navbar />

      {/* 2. Page Hero Header */}
      <section className="pt-32 pb-12 px-6 bg-[#0b0e14] border-b border-white/10 relative overflow-hidden">
        {/* Background Grid Pattern */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none" />
        
        <div className="max-w-6xl mx-auto relative z-10">
          {/* Back Button */}
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-xs font-mono text-slate-400 hover:text-[#C8FF00] mb-6 transition-colors group"
          >
            <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
            <span>← ANA SAYFAYA DÖN</span>
          </Link>

          {/* Category & Badges */}
          <div className="flex flex-wrap items-center gap-3 mb-4">
            <span className="px-3 py-1 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-xs font-mono font-bold tracking-wider uppercase">
              {policy.category}
            </span>
            <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-slate-300 text-xs font-mono">
              {policy.badge}
            </span>
            <span className="px-3 py-1 rounded bg-white/5 border border-white/10 text-slate-300 text-xs font-mono">
              {policy.subBadge}
            </span>
          </div>

          {/* Title */}
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight">
            {policy.title}
          </h1>
        </div>
      </section>

      {/* 3. Main Policy Layout: Left Sticky Sidebar + Right Legal Document */}
      <section className="py-12 px-6 max-w-6xl mx-auto font-sans">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          {/* Left Column: Interactive Policy Directory Sidebar (4 Cols) */}
          <aside className="lg:col-span-4 space-y-4">
            <div className="sticky top-28 p-5 rounded-2xl bg-[#0c0f16] border border-white/10 space-y-4 shadow-xl">
              <div className="flex items-center justify-between border-b border-white/10 pb-3">
                <span className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">KURUMSAL POLİTİKALAR</span>
                <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/10">7 DOKÜMAN</span>
              </div>

              <nav className="space-y-1.5 font-mono text-xs font-medium">
                {Object.entries(policyData).map(([slug, item]) => {
                  const isActive = slug === currentSlug;
                  const ItemIcon = iconMap[item.iconName] || FileText;

                  return (
                    <Link
                      key={slug}
                      href={`/politika/${slug}`}
                      className={`flex items-center justify-between p-3 rounded-xl transition-all duration-200 group ${
                        isActive
                          ? "bg-[#C8FF00] text-black font-bold shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                          : "text-slate-300 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10"
                      }`}
                    >
                      <div className="flex items-center gap-2.5 overflow-hidden">
                        <ItemIcon className={`w-4 h-4 shrink-0 ${isActive ? "text-black" : "text-[#C8FF00]"}`} />
                        <span className="truncate">{item.category}</span>
                      </div>
                      <ArrowRight className={`w-3.5 h-3.5 shrink-0 transition-transform ${isActive ? "translate-x-0" : "-translate-x-1 opacity-0 group-hover:opacity-100 group-hover:translate-x-0"}`} />
                    </Link>
                  );
                })}
              </nav>

              {/* Legal Verification Stamp */}
              <div className="p-3.5 rounded-xl bg-white/[0.02] border border-white/10 text-[11px] text-slate-400 leading-relaxed font-mono">
                <div className="text-white font-bold mb-1 flex items-center gap-1.5">
                  <ShieldCheck className="w-4 h-4 text-[#C8FF00]" />
                  <span>HUKUKİ YETERLİLİK</span>
                </div>
                Bu doküman T.C. mevzuatları ve uluslararası savunma sanayii standartlarına tam uyumlu resmi politikadır.
              </div>
            </div>
          </aside>

          {/* Right Column: Complete Legal Document (8 Cols) */}
          <div className="lg:col-span-8 space-y-8">
            
            {/* Top Summary Card */}
            <div className="p-6 sm:p-8 rounded-2xl bg-[#0d1118] border border-white/10 flex items-start gap-4 shadow-lg relative overflow-hidden">
              <div className="absolute top-0 right-0 p-4 opacity-5 pointer-events-none">
                <IconComponent className="w-32 h-32 text-white" />
              </div>

              <div className="p-3.5 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 shrink-0 relative z-10">
                <IconComponent className="w-6 h-6" />
              </div>
              <div className="relative z-10">
                <div className="flex items-center justify-between gap-2 mb-2">
                  <h4 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">KURUMSAL ÖZET BİLDİRİMİ</h4>
                  <button
                    onClick={() => window.print()}
                    className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-white/5 hover:bg-white/10 border border-white/10 text-slate-300 hover:text-white text-[11px] font-mono transition-colors cursor-pointer"
                  >
                    <Printer className="w-3.5 h-3.5" />
                    <span>YAZDIR / İNDİR</span>
                  </button>
                </div>
                <p className="text-slate-200 text-base leading-relaxed font-normal">
                  {policy.content.summary}
                </p>
              </div>
            </div>

            {/* Document Sections */}
            {policy.content.sections.map((section: any, idx: number) => (
              <div key={idx} className="space-y-4 p-8 rounded-2xl bg-[#0c0e14] border border-white/10 hover:border-white/20 transition-colors">
                <h3 className="text-xl font-bold text-white tracking-tight flex items-center gap-2.5 border-b border-white/10 pb-4">
                  <CheckCircle2 className="w-5 h-5 text-[#C8FF00] shrink-0" />
                  <span>{section.heading}</span>
                </h3>
                <ul className="space-y-4 pl-2 text-slate-300 text-sm sm:text-base leading-relaxed font-normal">
                  {section.items.map((item: string, itemIdx: number) => (
                    <li key={itemIdx} className="flex items-start gap-3">
                      <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00] mt-2 shrink-0" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}

            {/* Official Corporate Footer Seal */}
            <div className="p-6 rounded-2xl bg-white/[0.02] border border-white/10 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-400">
              <div>
                <span className="text-slate-200 font-bold">TRUSTIA TEKNOLOJİ YAZILIM A.Ş.</span> — HUKUK DEPARTMANI
                <p className="text-[11px] text-slate-400 font-normal">Son Güncelleme: 04 Ağustos 2026 | İstanbul, Türkiye</p>
              </div>
              <div className="px-3 py-1.5 rounded bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] font-bold text-[11px] uppercase tracking-wider">
                YÜRÜRLÜKTEDİR ✓
              </div>
            </div>

          </div>

        </div>
      </section>

      {/* 4. Footer */}
      <Footer />
    </main>
  );
}
