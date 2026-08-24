"use client";

import {
  Building2,
  ShieldCheck,
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
      badgeText: "2026 KABULÜ",
      icon: Building2,
      location: "Şişli Polat Tower, İstanbul",
      glowColor: "emerald",
    },
    {
      id: "teknopark",
      org: t("eco_card2_org"),
      title: t("eco_card2_title"),
      desc: t("eco_card2_desc"),
      status: t("eco_card2_status"),
      badgeText: "CUBE GO SÜRECİ",
      icon: ShieldCheck,
      location: "Pendik, İstanbul // Savunma Teknoparkı",
      glowColor: "cyan",
    },
  ];

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-12 bg-[#06080b] border-t border-b border-white/10">
      <div className="max-w-5xl mx-auto space-y-8">
        
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

        {/* 2 Focused Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
          {accreditations.map((item) => {
            const IconComponent = item.icon;
            const isEmerald = item.glowColor === "emerald";

            return (
              <div
                key={item.id}
                className={`p-6 sm:p-7 rounded-2xl bg-[#0a0d13] border transition-all duration-300 flex flex-col justify-between group relative overflow-hidden shadow-xl ${
                  isEmerald
                    ? "border-emerald-500/30 hover:border-emerald-400/70 hover:shadow-[0_0_30px_rgba(16,185,129,0.1)]"
                    : "border-cyan-500/30 hover:border-cyan-400/70 hover:shadow-[0_0_30px_rgba(6,182,212,0.1)]"
                }`}
              >
                <div className="space-y-4">
                  {/* Top Bar: Icon & Badge */}
                  <div className="flex items-center justify-between">
                    <div
                      className={`p-3 rounded-xl transition-colors ${
                        isEmerald
                          ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                          : "bg-cyan-500/10 text-cyan-400 border border-cyan-500/20"
                      }`}
                    >
                      <IconComponent className="w-6 h-6" />
                    </div>

                    <span
                      className={`text-[10px] font-mono font-bold px-2.5 py-1 rounded border uppercase tracking-wider ${
                        isEmerald
                          ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-300"
                          : "bg-cyan-500/10 border-cyan-500/30 text-cyan-300"
                      }`}
                    >
                      {item.badgeText}
                    </span>
                  </div>

                  {/* Institution Organization & Title */}
                  <div>
                    <div className="text-[11px] font-mono font-bold text-slate-400 uppercase tracking-wider mb-1.5">
                      {item.org}
                    </div>
                    <h3
                      className={`text-base sm:text-lg font-bold text-white transition-colors leading-tight ${
                        isEmerald
                          ? "group-hover:text-emerald-400"
                          : "group-hover:text-cyan-400"
                      }`}
                    >
                      {item.title}
                    </h3>
                  </div>

                  {/* Description */}
                  <p className="text-slate-300 text-xs sm:text-sm leading-relaxed font-normal">
                    {item.desc}
                  </p>
                </div>

                {/* Bottom Status Pill & Location */}
                <div className="pt-5 mt-5 border-t border-white/10 space-y-2.5">
                  <div className="flex items-center justify-between">
                    <span
                      className={`inline-flex items-center gap-2 text-[11px] font-mono font-bold px-3 py-1 rounded-full border ${
                        isEmerald
                          ? "bg-emerald-500/10 border-emerald-500/40 text-emerald-300"
                          : "bg-cyan-500/10 border-cyan-500/40 text-cyan-300"
                      }`}
                    >
                      <CheckCircle2 className="w-3.5 h-3.5" />
                      <span>{item.status}</span>
                    </span>
                    <ArrowUpRight className="w-4 h-4 text-slate-500 group-hover:text-white transition-colors" />
                  </div>
                  <div className="text-[10px] font-mono text-slate-500">
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
