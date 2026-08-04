"use client";

import Link from "next/link";
import { ChevronRight } from "lucide-react";

export default function Navbar() {
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
        
        {/* Pure Typography Brand Logo: Sleek Syncopate "TRUSTIA AI" */}
        <Link href="/" className="flex items-center gap-1.5 group select-none py-1">
          <span className="font-syncopate font-bold text-base md:text-lg tracking-[0.2em] text-white uppercase group-hover:text-slate-200 transition-colors">
            TRUSTIA
          </span>
          <span className="font-syncopate font-black text-base md:text-lg tracking-[0.2em] text-[#C8FF00] drop-shadow-[0_0_15px_rgba(200,255,0,0.8)]">
            AI
          </span>
        </Link>

        {/* Center Navigation Links (100% Frameless & Transparent) */}
        <nav className="hidden lg:flex items-center gap-1 sm:gap-2 bg-transparent border-none p-0 shadow-none">
          {/* 1. HAKKIMIZDA */}
          <Link
            href="/hakkimizda"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            HAKKIMIZDA
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 2. OTONOMİ */}
          <button
            onClick={handleScrollToOtonomi}
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 cursor-pointer drop-shadow-md"
          >
            OTONOMİ
          </button>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 3. TEHDİT TESPİTİ */}
          <Link
            href="/politika/siber"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            TEHDİT TESPİTİ
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 4. SÜRÜ ZEKASI */}
          <Link
            href="/politika/etik"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            SÜRÜ ZEKASI
          </Link>

          <span className="text-white/30 text-xs font-mono">•</span>

          {/* 5. SERTİFİKASYON */}
          <Link
            href="/politika/yerlilik"
            className="px-3 py-1 text-xs font-mono font-bold tracking-widest text-slate-200 hover:text-[#C8FF00] uppercase transition-all duration-300 drop-shadow-md"
          >
            SERTİFİKASYON
          </Link>
        </nav>

        {/* Right CTA Button */}
        <Link
          href="/iletisim"
          className="px-5 py-2.5 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all duration-300 group cursor-pointer"
        >
          <span>İLETİŞİM</span>
          <ChevronRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
        </Link>
      </div>
    </header>
  );
}
