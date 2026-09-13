"use client";

import { useState } from "react";
import Image from "next/image";
import { ZoomIn, X, ShieldCheck, CheckCircle2, Award, ExternalLink } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { lang } = useLanguage();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const accreditations = [
    {
      flag: "🇪🇺",
      name: "Avrupa Komisyonu",
      code: "PIC: 861711529",
      desc: "ec.europa.eu Tescilli Katılımcı",
      status: "Onaylandı",
      statusColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30"
    },
    {
      flag: "🇪🇺",
      name: "EIT Urban Mobility",
      code: "Partner: CUS15554",
      desc: "100k€ Hibe #3.1.02-1206-3732.3",
      status: "Canlıda",
      statusColor: "text-[#C8FF00] bg-[#C8FF00]/10 border-[#C8FF00]/30"
    },
    {
      flag: "🇶🇦",
      name: "Katar QSTP (Doha)",
      code: "30M$ Fon + Sprint",
      desc: "Qatar Foundation 4 Hafta Rezidans",
      status: "Alındı",
      statusColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30"
    },
    {
      flag: "🇹🇷",
      name: "BAYKAR Teknoloji",
      code: "Tedarikçi Portalı",
      desc: "Seviye-4 3D SLAM & Taktik İKA",
      status: "Kayıt Alındı",
      statusColor: "text-cyan-400 bg-cyan-500/10 border-cyan-500/30"
    },
    {
      flag: "🇹🇷",
      name: "ASELSAN Portalı",
      code: "#0050569CCE941FD1",
      desc: "Kara Platform Entegrasyonu",
      status: "Değerlendirmede",
      statusColor: "text-amber-400 bg-amber-500/10 border-amber-500/30"
    },
    {
      flag: "🇹🇷",
      name: "SSB SAYZEK",
      code: "Başvuru #170",
      desc: "Simport Otonomi Simülasyon Yöneticisi",
      status: "Onay Bekliyor",
      statusColor: "text-amber-400 bg-amber-500/10 border-amber-500/30"
    },
    {
      flag: "🇺🇸",
      name: "Z Fellows (San Francisco)",
      code: "$10k Hibe Mülakatı",
      desc: "Grace Kasten (Pace Capital) Zoom",
      status: "17 Eylül",
      statusColor: "text-purple-400 bg-purple-500/10 border-purple-500/30"
    },
    {
      flag: "🇹🇷",
      name: "DEİK İş Konseyi",
      code: "Dijital Teknolojiler",
      desc: "Ticari Diplomasi & Otonomi İhracatı",
      status: "Onaylandı",
      statusColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30"
    },
    {
      flag: "🇦🇪",
      name: "Dubai RTA Challenge",
      code: "$1.200.000 Ödül",
      desc: "Global Seviye-4 Robotaksi Yarışması",
      status: "Finalist Adayı",
      statusColor: "text-cyan-400 bg-cyan-500/10 border-cyan-500/30"
    },
    {
      flag: "🇸🇦",
      name: "NEOM Otonom Mobilite",
      code: "$500B Mega Şehir",
      desc: "Seviye-4 Sürücüsüz Filo PoC Teklifi",
      status: "Alındı",
      statusColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30"
    },
    {
      flag: "🇹🇷",
      name: "İTO BTM Fulya Kampüsü",
      code: "2026-II Sözleşmeli",
      desc: "İstanbul Ticaret Odası Ön Kuluçka",
      status: "Yerleşik",
      statusColor: "text-[#C8FF00] bg-[#C8FF00]/10 border-[#C8FF00]/30"
    },
    {
      flag: "🇹🇷",
      name: "SPK fonbulucu",
      code: "Kampanya: W1MV5K",
      desc: "15.000.000 TL Hedef (150M TL Val.)",
      status: "Ön İnceleme",
      statusColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30"
    }
  ];

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-8 bg-[#05070a] border-t border-b border-white/10">
      {/* Background Grid Pattern */}
      <div className="absolute inset-0 bg-tactical-grid opacity-10 pointer-events-none" />

      <div className="max-w-7xl mx-auto space-y-6 relative z-10">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 pb-2 border-b border-white/10">
          <div>
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-slate-400 text-[10px] font-mono tracking-wider uppercase mb-1.5">
              <ShieldCheck className="w-3 h-3 text-[#C8FF00]" />
              <span>{lang === "tr" ? "RESMİ AKREDİTASYON VE EKOSİSTEM" : "OFFICIAL ACCREDITATIONS & ECOSYSTEM"}</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Doğrulanmış Kurumsal ve Küresel Tesciller" : "Verified Enterprise & Global Registrations"}
            </h2>
          </div>
          <div className="text-left sm:text-right">
            <span className="text-[11px] font-mono text-slate-400">
              {lang === "tr" ? "12 Doğrulanmış Girişim / AB & Savunma" : "12 Verified Credentials / EU & Defense"}
            </span>
          </div>
        </div>

        {/* 2-Column Balanced Master Grid (Left: Compact Certificate with Zoom, Right: High-End Credentials) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          
          {/* LEFT COLUMN: Compact Official Seal with Magnifying / Zoom Feature (5 Cols) */}
          <div className="lg:col-span-5 flex flex-col justify-between p-4 rounded-2xl bg-[#080b10] border border-white/15 shadow-xl relative group">
            
            {/* Top Badge */}
            <div className="flex items-center justify-between gap-2 pb-3 mb-2 border-b border-white/10">
              <div className="flex items-center gap-2">
                <Award className="w-4 h-4 text-[#C8FF00]" />
                <span className="text-xs font-bold text-white tracking-wide">
                  {lang === "tr" ? "T.C. Cumhurbaşkanlığı SSB & İTO BTM" : "SSB Defense & ITO BTM Cluster"}
                </span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 font-semibold">
                {lang === "tr" ? "Mühürlü Belge" : "Official Seal"}
              </span>
            </div>

            {/* Clickable Image Container with Magnifier Overlay */}
            <div 
              onClick={() => setIsModalOpen(true)}
              className="relative w-full aspect-[16/10] rounded-xl overflow-hidden cursor-zoom-in border border-white/10 bg-black/60 shadow-inner group/img"
            >
              <Image
                src="/accreditations-showcase.jpg"
                alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
                fill
                className="object-cover object-center group-hover/img:scale-105 transition-transform duration-500 filter contrast-105"
                sizes="(max-width: 768px) 100vw, 40vw"
              />

              {/* Hover Dark Gradient Overlay */}
              <div className="absolute inset-0 bg-black/40 opacity-0 group-hover/img:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center gap-2 backdrop-blur-[2px]">
                <div className="p-3 rounded-full bg-black/80 border border-[#C8FF00] text-[#C8FF00] shadow-[0_0_20px_rgba(200,255,0,0.5)] scale-90 group-hover/img:scale-100 transition-transform">
                  <ZoomIn className="w-5 h-5" />
                </div>
                <span className="text-xs font-mono font-bold text-white tracking-wider bg-black/70 px-3 py-1 rounded-md border border-white/20">
                  {lang === "tr" ? "TIKLA & BÜYÜTÜP İNCELE" : "CLICK TO EXPAND"}
                </span>
              </div>
            </div>

            {/* Bottom Caption */}
            <div className="pt-3 mt-2 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span className="truncate">T.C. SSB • İTO • BTM • KOSGEB • Teknopark</span>
              <button
                onClick={() => setIsModalOpen(true)}
                className="text-[#C8FF00] hover:text-white inline-flex items-center gap-1 font-semibold transition-colors shrink-0 ml-2"
              >
                <span>{lang === "tr" ? "Büyüt" : "Zoom"}</span>
                <ZoomIn className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* RIGHT COLUMN: 12 High-End Compact Accreditation Cards (7 Cols) */}
          <div className="lg:col-span-7 grid grid-cols-2 sm:grid-cols-3 gap-2.5 content-start">
            {accreditations.map((item, idx) => (
              <div
                key={idx}
                className="p-3 rounded-xl bg-[#080b10] border border-white/10 hover:border-[#C8FF00]/50 hover:bg-[#0c1017] transition-all duration-200 flex flex-col justify-between space-y-1 group shadow-sm"
              >
                <div className="flex items-center justify-between gap-1">
                  <div className="flex items-center gap-1.5 min-w-0">
                    <span className="text-xs shrink-0">{item.flag}</span>
                    <span className="text-[11px] font-bold text-white truncate group-hover:text-[#C8FF00] transition-colors">
                      {item.name}
                    </span>
                  </div>
                  <span className={`text-[8.5px] font-mono px-1.5 py-0.2 rounded border font-semibold shrink-0 ${item.statusColor}`}>
                    {item.status}
                  </span>
                </div>

                <div className="font-mono text-[10px] font-semibold text-slate-200 tracking-tight">
                  {item.code}
                </div>

                <div className="text-[9px] text-slate-400 line-clamp-1 leading-tight">
                  {item.desc}
                </div>
              </div>
            ))}
          </div>

        </div>

      </div>

      {/* FULL-SCREEN LIGHTBOX MODAL */}
      {isModalOpen && (
        <div 
          onClick={() => setIsModalOpen(false)}
          className="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4 sm:p-8 animate-in fade-in duration-200"
        >
          <div 
            onClick={(e) => e.stopPropagation()}
            className="relative max-w-5xl w-full bg-[#0a0d14] rounded-2xl border border-white/20 overflow-hidden shadow-[0_25px_70px_rgba(0,0,0,0.9)] space-y-3 p-4 sm:p-6"
          >
            {/* Modal Header */}
            <div className="flex items-center justify-between border-b border-white/10 pb-3">
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-5 h-5 text-[#C8FF00]" />
                <h3 className="text-sm sm:text-base font-bold text-white">
                  {lang === "tr" ? "Resmi Devlet & Savunma Sanayii Akreditasyon Konsorsiyumu" : "Official State & Defense Industry Accreditation Consortium"}
                </h3>
              </div>
              <button
                onClick={() => setIsModalOpen(false)}
                className="p-1.5 rounded-lg bg-white/10 text-slate-300 hover:text-white hover:bg-white/20 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Full-Res Image */}
            <div className="relative w-full aspect-[16/9] rounded-xl overflow-hidden border border-white/10 bg-black">
              <Image
                src="/accreditations-showcase.jpg"
                alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
                fill
                className="object-contain"
                priority
              />
            </div>

            {/* Modal Footer Info */}
            <div className="flex flex-col sm:flex-row items-center justify-between gap-2 pt-2 text-xs text-slate-400 font-mono">
              <span>T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı • İTO • BTM Fulya • KOSGEB • Teknopark İstanbul</span>
              <button
                onClick={() => setIsModalOpen(false)}
                className="px-4 py-1.5 rounded-md bg-white/10 hover:bg-white/20 text-white font-semibold text-xs transition-colors"
              >
                {lang === "tr" ? "Kapat (Esc)" : "Close (Esc)"}
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
