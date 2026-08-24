"use client";

import {
  Building2,
  ShieldCheck,
  Globe2,
  Award,
  CheckCircle2,
  ArrowUpRight,
  Sparkles,
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { t } = useLanguage();

  const accreditations = [
    {
      id: "btm",
      org: t("eco_card1_org"),
      title: t("eco_card1_title"),
      desc: t("eco_card1_desc"),
      status: t("eco_card1_status"),
      statusColor: "emerald",
      badgeText: "2026 KABULÜ",
      icon: Building2,
      location: "Şişli Polat Tower, İstanbul",
      highlight: true,
    },
    {
      id: "teknopark",
      org: t("eco_card2_org"),
      title: t("eco_card2_title"),
      desc: t("eco_card2_desc"),
      status: t("eco_card2_status"),
      statusColor: "cyan",
      badgeText: "CUBE GO SÜRECİ",
      icon: ShieldCheck,
      location: "Pendik, İstanbul // Savunma Teknoparkı",
      highlight: true,
    },
    {
      id: "yc",
      org: t("eco_card3_org"),
      title: t("eco_card3_title"),
      desc: t("eco_card3_desc"),
      status: t("eco_card3_status"),
      statusColor: "amber",
      badgeText: "FALL 2026",
      icon: Globe2,
      location: "San Francisco, CA // USA",
      highlight: false,
    },
    {
      id: "ssb",
      org: t("eco_card4_org"),
      title: t("eco_card4_title"),
      desc: t("eco_card4_desc"),
      status: t("eco_card4_status"),
      statusColor: "lime",
      badgeText: "100/100 SKOR",
      icon: Award,
      location: "Ankara // Devlet Tescil: L2zPtN4X1ZJ",
      highlight: false,
    },
  ];

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-12 bg-[#06080b] border-t border-b border-white/10">
      <div className="max-w-6xl mx-auto space-y-8">
        
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
          <div className="max-w-2xl space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-[10px] sm:text-xs font-mono font-bold tracking-widest uppercase">
              <Sparkles className="w-3.5 h-3.5" />
              <span>{t("eco_badge")}</span>
            </div>
            <h2 className="text-xl sm:text-3xl font-extrabold text-white tracking-tight leading-snug">
              {t("eco_title")}
            </h2>
          </div>
          <p className="text-slate-400 text-xs sm:text-sm font-normal max-w-md leading-relaxed border-l-2 border-emerald-500/40 pl-3">
            {t("eco_desc")}
          </p>
        </div>

        {/* 4 Accreditations Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
          {accreditations.map((item) => {
            const IconComponent = item.icon;

            return (
              <div
                key={item.id}
                className={`p-5 sm:p-6 rounded-2xl bg-[#0a0d13] border transition-all duration-300 flex flex-col justify-between group relative overflow-hidden shadow-xl ${
                  item.highlight
                    ? "border-emerald-500/30 hover:border-emerald-400/60 hover:shadow-emerald-500/5"
                    : "border-white/10 hover:border-white/25"
                }`}
              >
                <div className="space-y-3.5">
                  {/* Top Bar: Icon & Badge */}
                  <div className="flex items-center justify-between">
                    <div
                      className={`p-2.5 rounded-xl transition-colors ${
                        item.statusColor === "emerald"
                          ? "bg-emerald-500/10 text-emerald-400"
                          : item.statusColor === "cyan"
                          ? "bg-cyan-500/10 text-cyan-400"
                          : item.statusColor === "amber"
                          ? "bg-amber-500/10 text-amber-400"
                          : "bg-[#C8FF00]/10 text-[#C8FF00]"
                      }`}
                    >
                      <IconComponent className="w-5 h-5" />
                    </div>

                    <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-white/5 border border-white/10 text-slate-300 uppercase tracking-wider">
                      {item.badgeText}
                    </span>
                  </div>

                  {/* Institution Organization & Title */}
                  <div>
                    <div className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider mb-1">
                      {item.org}
                    </div>
                    <h3 className="text-sm sm:text-base font-bold text-white group-hover:text-emerald-400 transition-colors leading-tight">
                      {item.title}
                    </h3>
                  </div>

                  {/* Description */}
                  <p className="text-slate-400 text-xs leading-relaxed font-normal">
                    {item.desc}
                  </p>
                </div>

                {/* Bottom Status Pill & Location */}
                <div className="pt-4 mt-4 border-t border-white/10 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="inline-flex items-center gap-1.5 text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-white/[0.04] border border-white/15 text-white">
                      <CheckCircle2 className="w-3 h-3 text-emerald-400" />
                      <span>{item.status}</span>
                    </span>
                    <ArrowUpRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-white transition-colors" />
                  </div>
                  <div className="text-[9px] font-mono text-slate-500 truncate">
                    📍 {item.location}
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
