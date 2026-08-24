"use client";

import Link from "next/link";
import { ChevronRight } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function Navbar() {
  const { lang, setLang, t } = useLanguage();

  const handleScrollToOtonomi = (e: React.MouseEvent) => {
    e.preventDefault();
    const elem = document.getElementById("otonomi");
    if (elem) {
      elem.scrollIntoView({ behavior: "smooth" });
    } else {
      window.location.href = "/#otonomi";
    }
  };

  return (
    <header className="fixed top-2.5 sm:top-4 left-1/2 -translate-x-1/2 w-[96%] sm:w-[94%] max-w-6xl z-40 transition-all duration-500">
      {/* 100% Fully Transparent Header with No Background or Border anywhere */}
      <div className="relative px-1 sm:px-2 py-1.5 sm:py-2 bg-transparent border-none shadow-none flex items-center justify-between">
        
        {/* Brand Logo with Dynamic High-Res Waving Flag on the Diagonal Tip of "I" */}
        <Link href="/" className="relative inline-flex items-center group select-none py-1 pr-5 sm:pr-6 shrink-0">
          <span className="font-syncopate font-bold text-xs sm:text-base md:text-lg tracking-[0.14em] sm:tracking-[0.2em] text-white uppercase group-hover:text-slate-200 transition-colors">
            TRUSTIA
          </span>
          
          <span className="relative font-syncopate font-black text-xs sm:text-base md:text-lg tracking-[0.14em] sm:tracking-[0.2em] text-[#C8FF00] drop-shadow-[0_0_15px_rgba(200,255,0,0.8)] ml-1 sm:ml-1.5 inline-block">
            AI
            
            {/* Dynamic Flag Floating Directly Over the Top-Right Diagonal of "I" */}
            <span
              className="absolute -top-2 -right-4 sm:-top-2.5 sm:-right-5 z-20 flex items-center pointer-events-none"
              title={lang === "tr" ? "Milli Teknoloji (Türkiye)" : "Delaware C-Corp (United States)"}
            >
              <span className="relative block w-4 h-2.5 sm:w-5 sm:h-3.5 rounded-[2px] sm:rounded-[2.5px] overflow-hidden shadow-[0_2px_8px_rgba(0,0,0,0.9)] border border-white/40 animate-flag-wave transition-transform duration-300">
                {lang === "tr" ? (
                  /* eslint-disable-next-line @next/next/no-img-element */
                  <img
                    key="tr-flag"
                    src="/flags/tr.svg"
                    alt="Türkiye Bayrağı"
                    className="w-full h-full object-cover transition-opacity duration-300"
                  />
                ) : (
                  /* eslint-disable-next-line @next/next/no-img-element */
                  <img
                    key="us-flag"
                    src="/flags/us.svg"
                    alt="USA Flag"
                    className="w-full h-full object-cover transition-opacity duration-300"
                  />
                )}
              </span>
            </span>
          </span>
        </Link>

        {/* Center Navigation Links (Hidden on mobile, 100% Preserved on Desktop) */}
        <nav className="hidden lg:flex items-center gap-1 sm:gap-2 bg-transparent border-none p-0 shadow-none">
          {/* 1. HAKKIMIZDA / ABOUT US */}
          <Link
            href="/hakkimizda/"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_about")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 2. OTONOMİ / AUTONOMY */}
          <button
            onClick={handleScrollToOtonomi}
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 cursor-pointer drop-shadow-md"
          >
            {t("nav_autonomy")}
          </button>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 3. TEHDİT TESPİTİ / THREAT DETECTION */}
          <Link
            href="/politika/siber/"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_threat")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 4. SÜRÜ ZEKASI / SWARM INTEL */}
          <Link
            href="/politika/etik/"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_swarm")}
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 5. SERTİFİKASYON / CERTIFICATION */}
          <Link
            href="/politika/yerlilik/"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            {t("nav_cert")}
          </Link>
        </nav>

        {/* Right Action Area: Language Switcher & Contact Button */}
        <div className="flex items-center gap-1.5 sm:gap-3 shrink-0">
          {/* TR / EN Language Toggle Pill (Responsive for mobile & desktop) */}
          <div className="flex items-center p-0.5 sm:p-1 rounded-lg sm:rounded-xl bg-black/60 border border-white/15 backdrop-blur-md text-[10px] sm:text-xs font-mono font-bold shadow-lg">
            <button
              onClick={() => setLang("tr")}
              className={`px-1.5 sm:px-2.5 py-0.5 sm:py-1 rounded-md sm:rounded-lg transition-all duration-300 cursor-pointer ${
                lang === "tr"
                  ? "bg-[#C8FF00] text-black shadow-[0_0_10px_rgba(200,255,0,0.5)] font-black"
                  : "text-slate-400 hover:text-white"
              }`}
            >
              TR
            </button>
            <button
              onClick={() => setLang("en")}
              className={`px-1.5 sm:px-2.5 py-0.5 sm:py-1 rounded-md sm:rounded-lg transition-all duration-300 cursor-pointer ${
                lang === "en"
                  ? "bg-[#C8FF00] text-black shadow-[0_0_10px_rgba(200,255,0,0.5)] font-black"
                  : "text-slate-400 hover:text-white"
              }`}
            >
              EN
            </button>
          </div>

          {/* Contact Button (Compact on mobile, full size on desktop) */}
          <Link
            href="/iletisim/"
            className="px-2.5 sm:px-5 py-1.5 sm:py-2.5 rounded-lg sm:rounded-xl bg-[#C8FF00] text-black font-mono font-black text-[10px] sm:text-xs tracking-wider uppercase flex items-center gap-1 sm:gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all duration-300 group cursor-pointer"
          >
            <span>{t("nav_contact")}</span>
            <ChevronRight className="w-3 h-3 sm:w-3.5 sm:h-3.5 group-hover:translate-x-1 transition-transform" />
          </Link>
        </div>

      </div>
    </header>
  );
}
