"use client";

import Navbar from "@/components/Navbar";
import HeroVideo from "@/components/HeroVideo";
import RobotaxiShowcase from "@/components/RobotaxiShowcase";
import SupportedPlatformsShowcase from "@/components/SupportedPlatformsShowcase";
import FeatureVideo from "@/components/FeatureVideo";
import TechMatrixShowcase from "@/components/TechMatrixShowcase";
import Footer from "@/components/Footer";
import ConsoleBranding from "@/components/ConsoleBranding";

export default function Home() {
  return (
    <main className="relative w-full bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black overflow-x-hidden">
      {/* DevTools Browser Console Corporate Branding */}
      <ConsoleBranding />

      {/* 1. 100% Frameless Transparent Glass Navbar with Language Toggle */}
      <Navbar />

      {/* 2. Apple / Console Scroll-Driven Shrink Hero Video */}
      <HeroVideo />

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
