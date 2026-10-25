"use client";

import { useEffect, useRef, useState } from "react";
import { Volume2, VolumeX } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function HeroVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isMuted, setIsMuted] = useState(true);
  const [scrollProgress, setScrollProgress] = useState(0);
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

  useEffect(() => {
    let ticking = false;
    const handleScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const currentY = window.scrollY;
          // Progress from 0 to 1 over 360px of scroll
          const progress = Math.min(1, Math.max(0, currentY / 360));
          setScrollProgress(progress);
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
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

  // Interpolated values for Apple / Console Shrink
  const scale = 1 - scrollProgress * 0.08; // 1.0 -> 0.92
  const borderRadius = scrollProgress * 28; // 0px -> 28px
  const borderOpacity = scrollProgress * 0.18; // 0 -> 0.18
  const indicatorOpacity = Math.max(0, 1 - scrollProgress * 2.5);

  return (
    <div className="relative w-full h-[125vh]">
      {/* Sticky Fullscreen Wrapper */}
      <div className="sticky top-0 w-full h-screen flex items-center justify-center p-0 overflow-hidden pointer-events-none">
        
        {/* Dynamic Shrinking Console Frame */}
        <div
          style={{
            transform: `scale(${scale})`,
            borderRadius: `${borderRadius}px`,
            borderColor: `rgba(255, 255, 255, ${borderOpacity})`,
            boxShadow:
              scrollProgress > 0.05
                ? `0 ${scrollProgress * 30}px ${scrollProgress * 70}px -15px rgba(0, 0, 0, 0.95)`
                : "none",
            willChange: "transform, border-radius",
          }}
          className="relative w-full h-full overflow-hidden border transition-[border-color,box-shadow] duration-150 ease-out pointer-events-auto bg-[#07090c]"
        >
          {/* Video Player */}
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
          <div className="absolute inset-0 bg-gradient-to-t from-[#090b0e] via-black/25 to-[#090b0e]/50 pointer-events-none z-1" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#090b0e]/60 via-transparent to-transparent pointer-events-none z-1" />

          {/* Responsive Touch-Friendly Sound Control Button */}
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

          {/* Subtle Luxury Scroll Pill (Fades out smoothly on scroll) */}
          <div
            style={{
              opacity: indicatorOpacity,
              transform: `translateY(${scrollProgress * 25}px)`,
              pointerEvents: indicatorOpacity > 0.1 ? "auto" : "none",
            }}
            className="absolute bottom-6 left-1/2 -translate-x-1/2 z-20 flex flex-col items-center gap-2 text-slate-400/80 hover:text-white transition-opacity select-none"
          >
            <a
              href="#otonomi"
              className="flex flex-col items-center gap-2 group cursor-pointer"
              aria-label={lang === "tr" ? "Mimariyi İncele" : "Explore Architecture"}
            >
              <span className="text-[10px] font-mono tracking-widest uppercase text-slate-400 group-hover:text-[#C8FF00] transition-colors">
                {lang === "tr" ? "MİMARİ" : "ARCHITECTURE"}
              </span>
              <div className="w-5 h-8 rounded-full border border-white/20 group-hover:border-[#C8FF00]/50 flex items-start justify-center p-1.5 backdrop-blur-sm bg-black/40 transition-colors shadow-lg">
                <div className="w-1 h-2 rounded-full bg-white/70 group-hover:bg-[#C8FF00] animate-bounce transition-colors" />
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
