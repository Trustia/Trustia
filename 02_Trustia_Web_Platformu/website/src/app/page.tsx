"use client";

import Navbar from "@/components/Navbar";
import HeroVideo from "@/components/HeroVideo";
import RobotaxiShowcase from "@/components/RobotaxiShowcase";
import SupportedPlatformsShowcase from "@/components/SupportedPlatformsShowcase";
import FeatureVideo from "@/components/FeatureVideo";
import TechMatrixShowcase from "@/components/TechMatrixShowcase";
import Footer from "@/components/Footer";
import ConsoleBranding from "@/components/ConsoleBranding";
import { useLanguage } from "@/context/LanguageContext";

export default function Home() {
  const { lang } = useLanguage();

  return (
    <main className="relative w-full bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black overflow-x-hidden">
      {/* DevTools Browser Console Corporate Branding */}
      <ConsoleBranding />

      {/* 1. 100% Frameless Transparent Glass Navbar with Language Toggle */}
      <Navbar />

      {/* 2. Fullscreen Video Background */}
      <HeroVideo />

      {/* 3. Pure Cinematic Video Viewport - 100% Unobstructed Autonomous Cockpit */}
      <section className="relative w-full h-screen min-h-[580px] flex items-end justify-center pb-8 z-10 pointer-events-none">
        {/* Subtle Luxury Scroll Pill */}
        <a
          href="#otonomi"
          className="pointer-events-auto flex flex-col items-center gap-2 text-slate-400/70 hover:text-white transition-colors cursor-pointer group select-none"
          aria-label={lang === "tr" ? "Mimariyi İncele" : "Explore Architecture"}
        >
          <span className="text-[10px] font-mono tracking-widest uppercase text-slate-400 group-hover:text-[#C8FF00] transition-colors">
            {lang === "tr" ? "MİMARİ" : "ARCHITECTURE"}
          </span>
          <div className="w-5 h-8 rounded-full border border-white/20 group-hover:border-[#C8FF00]/50 flex items-start justify-center p-1.5 backdrop-blur-sm bg-black/30 transition-colors shadow-lg">
            <div className="w-1 h-2 rounded-full bg-white/70 group-hover:bg-[#C8FF00] animate-bounce transition-colors" />
          </div>
        </a>
      </section>

      {/* Sovereign Level 4 Robotaxi Platform Showcase (Hyundai Ioniq 5 E-GMP) */}
      <RobotaxiShowcase />

      {/* 4. Supported Vehicles & Integration Platforms Matrix */}
      <SupportedPlatformsShowcase />

      {/* 5. Pure Panoramic Cinematic Video Strip */}
      <FeatureVideo />

      {/* 6. Complete Executive Defense & Automotive Tech Matrix */}
      <TechMatrixShowcase />

      {/* 7. Comprehensive Corporate Footer */}
      <Footer />
    </main>
  );
}
