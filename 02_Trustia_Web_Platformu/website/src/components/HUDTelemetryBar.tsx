"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";

export default function HUDTelemetryBar() {
  const { lang } = useLanguage();
  const [zuluTime, setZuluTime] = useState<string>("00:00:00Z");

  useEffect(() => {
    const updateZulu = () => {
      const now = new Date();
      const h = String(now.getUTCHours()).padStart(2, "0");
      const m = String(now.getUTCMinutes()).padStart(2, "0");
      const s = String(now.getUTCSeconds()).padStart(2, "0");
      setZuluTime(`${h}:${m}:${s}Z`);
    };
    updateZulu();
    const interval = setInterval(updateZulu, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="w-full border-y border-white/10 bg-[#090b0e]/75 backdrop-blur-md py-2.5 px-3 sm:px-6 font-mono text-[10px] sm:text-[11px] uppercase tracking-wider text-slate-300 relative z-20">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3 sm:gap-6">
        {/* Metric 1: Location */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          <span className="text-slate-500 font-semibold">// {lang === "tr" ? "SAHA:" : "SITE:"}</span>
          <span className="text-white font-bold">TRİPY MOBİLİTY // TEKNOPARK</span>
          <span className="text-[#E4F80D] font-bold text-[9px] hidden md:inline">[39.8732°N 32.7481°E]</span>
        </div>

        {/* Metric 2: CAN-FD Latency */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          <span className="text-slate-500 font-semibold">// {lang === "tr" ? "VERİ YOLU:" : "BUS:"}</span>
          <span className="text-[#E4F80D] font-bold tabular-nums">100 Hz SENKRON</span>
          <span className="text-slate-400 text-[10px]">1.4 ms GECİKME</span>
        </div>

        {/* Metric 3: Safety Arbiter */}
        <div className="hidden sm:flex items-center gap-1.5 sm:gap-2">
          <span className="text-slate-500 font-semibold">// {lang === "tr" ? "EMNİYET:" : "SAFETY:"}</span>
          <span className="text-white font-bold">ISO 26262 ASIL-D</span>
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
        </div>

        {/* Metric 4: Real-Time Zulu Clock */}
        <div className="flex items-center gap-1.5 sm:gap-2 ml-auto sm:ml-0">
          <span className="text-slate-500 font-semibold">// ZULU:</span>
          <span className="text-emerald-400 font-bold tabular-nums tracking-widest">{zuluTime}</span>
        </div>
      </div>
    </div>
  );
}
