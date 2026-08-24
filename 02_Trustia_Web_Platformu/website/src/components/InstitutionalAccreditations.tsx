"use client";

import {
  Building2,
  ShieldCheck,
  Globe2,
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
      location: "Şişli Polat Tower",
      color: "emerald",
    },
    {
      id: "teknopark",
      org: t("eco_card2_org"),
      title: t("eco_card2_title"),
      desc: t("eco_card2_desc"),
      status: t("eco_card2_status"),
      badgeText: "CUBE GO SÜRECİ",
      icon: ShieldCheck,
      location: "Pendik, İstanbul",
      color: "cyan",
    },
    {
      id: "yc",
      org: t("eco_card3_org"),
      title: t("eco_card3_title"),
      desc: t("eco_card3_desc"),
      status: t("eco_card3_status"),
      badgeText: "FALL 2026",
      icon: Globe2,
      location: "San Francisco, CA",
      color: "amber",
    },
  ];

  return (
    <section className="relative z-20 py-6 sm:py-8 px-4 sm:px-8 bg-[#06080b] border-t border-b border-white/10">
      <div className="max-w-6xl mx-auto space-y-4">
        
        {/* Compact Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div className="flex items-center gap-2.5">
            <span className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-[10px] font-mono font-bold tracking-wider uppercase">
              <Sparkles className="w-3 h-3" />
              <span>{t("eco_badge")}</span>
            </span>
            <h2 className="text-sm sm:text-base font-bold text-white tracking-tight">
              {t("eco_title")}
            </h2>
          </div>
          <span className="text-[11px] font-mono text-slate-400">
            {t("eco_desc")}
          </span>
        </div>

        {/* 3 Compact Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5 sm:gap-4">
          {accreditations.map((item) => {
            const IconComponent = item.icon;
            const isEmerald = item.color === "emerald";
            const isCyan = item.color === "cyan";

            return (
              <div
                key={item.id}
                className={`p-4 sm:p-4.5 rounded-xl bg-[#090c10] border transition-all duration-300 flex flex-col justify-between group relative shadow-lg ${
                  isEmerald
                    ? "border-emerald-500/25 hover:border-emerald-400/60 hover:shadow-emerald-500/5"
                    : isCyan
                    ? "border-cyan-500/25 hover:border-cyan-400/60 hover:shadow-cyan-500/5"
                    : "border-amber-500/25 hover:border-amber-400/60 hover:shadow-amber-500/5"
                }`}
              >
                <div className="space-y-2.5">
                  {/* Top Bar: Icon & Badge */}
                  <div className="flex items-center justify-between">
                    <div
                      className={`p-2 rounded-lg ${
                        isEmerald
                          ? "bg-emerald-500/10 text-emerald-400"
                          : isCyan
                          ? "bg-cyan-500/10 text-cyan-400"
                          : "bg-amber-500/10 text-amber-400"
                      }`}
                    >
                      <IconComponent className="w-4 h-4" />
                    </div>

                    <span
                      className={`text-[9px] font-mono font-bold px-2 py-0.5 rounded border uppercase tracking-wider ${
                        isEmerald
                          ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-300"
                          : isCyan
                          ? "bg-cyan-500/10 border-cyan-500/30 text-cyan-300"
                          : "bg-amber-500/10 border-amber-500/30 text-amber-300"
                      }`}
                    >
                      {item.badgeText}
                    </span>
                  </div>

                  {/* Institution Organization & Title */}
                  <div>
                    <div className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">
                      {item.org}
                    </div>
                    <h3 className="text-xs sm:text-sm font-bold text-white group-hover:text-slate-100 transition-colors leading-snug">
                      {item.title}
                    </h3>
                  </div>

                  {/* Description */}
                  <p className="text-slate-400 text-[11px] sm:text-xs leading-relaxed font-normal">
                    {item.desc}
                  </p>
                </div>

                {/* Bottom Status Pill & Location */}
                <div className="pt-3 mt-3 border-t border-white/10 flex items-center justify-between text-[10px] font-mono">
                  <span
                    className={`inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border font-bold ${
                      isEmerald
                        ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-300"
                        : isCyan
                        ? "bg-cyan-500/10 border-cyan-500/30 text-cyan-300"
                        : "bg-amber-500/10 border-amber-500/30 text-amber-300"
                    }`}
                  >
                    <CheckCircle2 className="w-3 h-3" />
                    <span>{item.status}</span>
                  </span>

                  <span className="text-slate-500 truncate max-w-[120px]">
                    📍 {item.location}
                  </span>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
