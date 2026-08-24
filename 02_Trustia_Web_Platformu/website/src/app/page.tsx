"use client";

import Navbar from "@/components/Navbar";
import HeroVideo from "@/components/HeroVideo";
import GalleryShowcase from "@/components/GalleryShowcase";
import SupportedPlatformsShowcase from "@/components/SupportedPlatformsShowcase";
import FeatureVideo from "@/components/FeatureVideo";
import TechMatrixShowcase from "@/components/TechMatrixShowcase";
import Footer from "@/components/Footer";
import ConsoleBranding from "@/components/ConsoleBranding";
import { useLanguage } from "@/context/LanguageContext";

export default function Home() {
  const { t } = useLanguage();

  return (
    <main className="relative w-full bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black overflow-x-hidden">
      {/* DevTools Browser Console Corporate Branding */}
      <ConsoleBranding />

      {/* 1. 100% Frameless Transparent Glass Navbar with Language Toggle */}
      <Navbar />

      {/* 2. Fullscreen Video Background */}
      <HeroVideo />

      {/* Hero Content Section - Mobile Optimized, Desktop 100% Preserved */}
      <section className="relative w-full h-screen min-h-[580px] sm:min-h-[600px] flex items-end justify-start px-4 sm:px-12 md:px-16 pb-14 sm:pb-16 z-10 pointer-events-none">
        <div className="max-w-md text-left space-y-2 sm:space-y-2.5 pointer-events-auto">
          {/* Corporate Badge */}
          <div className="inline-flex items-center gap-2 px-2.5 sm:px-3 py-0.5 rounded bg-black/50 border border-white/20 text-slate-300 text-[9px] sm:text-[10px] font-mono font-bold tracking-wider uppercase backdrop-blur-md">
            <span>{t("hero_badge")}</span>
          </div>

          {/* Responsive Headline (Cleanly formatted on mobile, bold on desktop) */}
          <h1 className="text-lg sm:text-2xl md:text-3xl font-extrabold text-white tracking-tight leading-[1.25] sm:leading-[1.2] drop-shadow-2xl">
            {t("hero_title_1")} <br />
            {t("hero_title_2")}
          </h1>

          {/* Responsive Subtitle */}
          <p className="text-slate-300 text-[11px] sm:text-xs font-normal leading-relaxed max-w-[320px] sm:max-w-sm drop-shadow-md">
            {t("hero_desc")}
          </p>

          {/* Slanted CTA Button */}
          <div className="pt-0.5 sm:pt-1">
            <a
              href="#otonomi"
              className="btn-overland-slanted cursor-pointer text-[11px] sm:text-xs"
            >
              {t("hero_btn_explore")}
            </a>
          </div>
        </div>
      </section>

      {/* 3. 5 Real Photos Gallery Showcase */}
      <GalleryShowcase />

      {/* 4. Supported Vehicles & Integration Platforms Matrix */}
      <SupportedPlatformsShowcase />

      {/* 5. Pure Panoramic Cinematic Video Strip */}
      <FeatureVideo />

      {/* 5. Complete 6-Grid Executive Defense Tech Matrix (SLAM, Hybrid A*, EYP/CBRN, Swarm, HMAC-SHA256, ROS 2) */}
      <TechMatrixShowcase />

      {/* 6. Comprehensive Corporate Footer */}
      <Footer />
    </main>
  );
}
