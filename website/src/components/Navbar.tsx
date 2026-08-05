"use client";

import Link from "next/link";
import { ChevronRight, Globe } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function Navbar() {
  const { lang, toggleLang, t } = useLanguage();

  const handleScrollToOtonomi = (e: React.MouseEvent) => {
    e.preventDefault();
    const elem = document.getElementById("otonomi");
    if (elem) {
      elem.scrollIntoView({ behavior: "smooth" });
    } else {
      window.location.href = "/";
    }
  };

  return (
    <header className="fixed top-4 left-1/2 -translate-x-1/2 w-[94%] max-w-6xl z-40 transition-all duration-500">
      {/* 100% Fully Transparent Header with No Background or Border anywhere */}
      <div className="relative px-2 py-2 bg-transparent border-none shadow-none flex items-center justify-between">
        
        {/* Pure Typography Brand Logo: Sleek Syncopate "TRUSTIA AI" + Small Turkish Flag Badge on top-right tip of "I" */}
        <Link href="/" className="flex items-center gap-1.5 group select-none py-1">
          <span className="font-syncopate font-bold text-base md:text-lg tracking-[0.2em] text-white uppercase group-hover:text-slate-200 transition-colors">
            TRUSTIA
          </span>
          <span className="relative inline-flex items-center font-syncopate font-black text-base md:text-lg tracking-[0.2em] text-[#C8FF00] drop-shadow-[0_0_15px_rgba(200,255,0,0.8)]">
            AI
            {/* Small Turkish Flag Badge positioned right at top-right diagonal tip of "I" */}
            <span className="absolute -top-1 -right-3.5 flex items-center justify-center w-3.5 h-2.5 rounded-[1px] overflow-hidden border border-white/20 shadow-[0_0_8px_rgba(227,10,23,0.9)]">
              {/* Official Turkish Flag SVG */}
              <svg viewBox="0 0 1200 800" className="w-full h-full object-cover">
                <rect width="1200" height="800" fill="#E30A17" />
                <circle cx="425" cy="400" r="200" fill="#ffffff" />
                <circle cx="475" cy="400" r="160" fill="#E30A17" />
                <polygon points="583.333,400 706.879,440.147 630.528,335.048 630.528,464.952 706.879,359.853" fill="#ffffff" transform="rotate(-15 625 400)" />
              </svg>
            </span>
          </span>
        </Link>

        {/* Center Navigation Links (100% Frameless & Transparent) */}
        <nav className="hidden lg:flex items-center gap-1 sm:gap-2 bg-transparent border-none p-0 shadow-none">
          {/* 1. HAKKIMIZDA */}
          <Link
            href="/hakkimizda"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_about")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 2. OTONOMİ */}
          <button
            onClick={handleScrollToOtonomi}
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 cursor-pointer drop-shadow-md"
          >
            {t("nav_autonomy")}
          </button>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 3. TEHDİT TESPİTİ */}
          <Link
            href="/politika/siber"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_threat")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 4. SÜRÜ ZEKASI */}
          <Link
            href="/politika/etik"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_swarm")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 5. SERTİFİKASYON */}
          <Link
            href="/politika/yerlilik"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_cert")}
          </Link>
        </nav>

        {/* Right CTA Button & Language Switcher */}
        <div className="flex items-center gap-3">
          {/* TR / EN Language Toggle Pill */}
          <button
            onClick={toggleLang}
            className="px-3 py-1.5 rounded-lg bg-black/40 border border-white/10 backdrop-blur-md text-white font-mono text-xs font-bold tracking-wider flex items-center gap-1.5 hover:border-[#C8FF00]/50 hover:text-[#C8FF00] transition-all cursor-pointer shadow-md"
            title="Switch Language / Dil Değiştir"
          >
            <Globe className="w-3.5 h-3.5 text-[#C8FF00]" />
            <span>{lang === "tr" ? "TR" : "EN"}</span>
          </button>

          {/* Contact Button */}
          <Link
            href="/iletisim"
            className="px-4 md:px-5 py-2.5 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center gap-1.5 md:gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all duration-300 group cursor-pointer"
          >
            <span>{t("nav_contact")}</span>
            <ChevronRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </Link>
        </div>
      </div>
    </header>
  );
}
