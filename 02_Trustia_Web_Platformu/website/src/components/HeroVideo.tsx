"use client";

import { useEffect, useRef, useState } from "react";
import { Volume2, VolumeX } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function HeroVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isMuted, setIsMuted] = useState(true);
  const { lang } = useLanguage();

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.volume = 0.5;
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {});
      }
    }
  }, []);

  const toggleSound = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (videoRef.current) {
      if (isMuted) {
        videoRef.current.muted = false;
        videoRef.current.volume = 0.7;
        setIsMuted(false);
        videoRef.current.play().catch(() => {});
      } else {
        videoRef.current.muted = true;
        setIsMuted(true);
      }
    }
  };

  return (
    <div className="absolute top-0 left-0 w-full h-screen min-h-[580px] sm:min-h-[600px] overflow-hidden z-0 pointer-events-none">
      {/* Fullscreen Video Background - Optimized for Mobile & Desktop */}
      <video
        ref={videoRef}
        autoPlay
        loop
        muted
        playsInline
        className="w-full h-full object-cover object-center filter brightness-[0.88] contrast-105 pointer-events-auto"
      >
        <source src="/hero-video.mp4" type="video/mp4" />
      </video>

      {/* Subtle Dark Vignette & Gradient Overlays */}
      <div className="absolute inset-0 bg-gradient-to-t from-[#090b0e] via-black/30 to-[#090b0e]/60 pointer-events-none z-1" />
      <div className="absolute inset-0 bg-gradient-to-r from-[#090b0e]/70 via-transparent to-transparent pointer-events-none z-1" />

      {/* Responsive Touch-Friendly Sound Control Button (Stays in Hero, never interferes with scrolling) */}
      <button
        type="button"
        onClick={toggleSound}
        className="absolute bottom-5 right-4 sm:bottom-8 sm:right-8 z-30 px-3.5 py-2.5 sm:px-4 sm:py-2 rounded-full bg-black/70 border border-white/25 text-slate-200 hover:text-[#C8FF00] hover:border-[#C8FF00]/60 active:scale-95 transition-all backdrop-blur-md pointer-events-auto flex items-center gap-2 text-xs font-mono select-none cursor-pointer shadow-2xl touch-manipulation min-h-[44px]"
        title={lang === "tr" ? "Ses Kontrolü" : "Audio Control"}
      >
        {isMuted ? (
          <VolumeX className="w-4 h-4 text-slate-400 group-hover:text-red-400 transition-colors" />
        ) : (
          <Volume2 className="w-4 h-4 text-[#C8FF00] animate-pulse" />
        )}
        <span className="font-semibold tracking-wide">
          {isMuted ? (lang === "tr" ? "Sessiz" : "Muted") : (lang === "tr" ? "Ses Açık" : "Audio On")}
        </span>
      </button>
    </div>
  );
}
