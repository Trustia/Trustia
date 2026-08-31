"use client";

import Navbar from "@/components/Navbar";
import HeroVideo from "@/components/HeroVideo";
import InstitutionalAccreditations from "@/components/InstitutionalAccreditations";
import RobotaxiShowcase from "@/components/RobotaxiShowcase";
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

      {/* Hero Content Section - Compact Executive Corner Placement */}
      <section className="relative w-full h-screen min-h-[560px] flex items-end justify-start px-4 sm:px-10 md:px-14 pb-10 sm:pb-14 z-10 pointer-events-none">
        <div className="max-w-sm sm:max-w-md text-left space-y-2 pointer-events-auto">
          {/* Corporate Badge */}
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-black/60 border border-white/15 text-slate-300 text-[10px] font-mono font-medium tracking-wider uppercase backdrop-blur-md">
            <span>{t("hero_badge")}</span>
          </div>

          {/* Clean 2-Line Headline */}
          <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug drop-shadow-xl">
            {t("hero_title_1")} <br />
            <span className="text-slate-200">{t("hero_title_2")}</span>
          </h1>

          {/* Responsive Compact Subtitle */}
          <p className="text-slate-300 text-xs font-normal leading-relaxed drop-shadow-md">
            {t("hero_desc")}
          </p>

          {/* Clean Executive Action Button */}
          <div className="pt-2">
            <a
              href="#otonomi"
              className="px-4 py-2 rounded-lg bg-white text-slate-950 font-semibold text-xs tracking-wider uppercase hover:bg-slate-200 transition-colors inline-flex items-center gap-2 shadow-lg"
            >
              <span>{t("hero_btn_explore")}</span>
            </a>
          </div>
        </div>
      </section>

      {/* 3. Official Institutional Accreditations & Incubator Ecosystem (BTM, Teknopark Istanbul, YC, SSB) */}
      <InstitutionalAccreditations />

      {/* 4. Sovereign Level 4 Robotaxi Platform Showcase (Hyundai Ioniq 5 E-GMP) */}
      <RobotaxiShowcase />

      {/* 5. 5 Real Photos Gallery Showcase */}
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
