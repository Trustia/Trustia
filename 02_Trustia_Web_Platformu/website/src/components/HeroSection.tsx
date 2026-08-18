"use client";

import { useState, useRef, useEffect } from "react";
import { Volume2, VolumeX, ChevronDown, ChevronUp, Shield, ArrowRight } from "lucide-react";

export default function HeroSection() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isMuted, setIsMuted] = useState(true);
  const [isDrawerOpen, setIsDrawerOpen] = useState(true);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.volume = 0.3;
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {});
      }
    }
  }, []);

  const handleTimeUpdate = () => {
    if (videoRef.current) {
      // Loop back to 0 at 1:48 (108 seconds) to trim the last 6 seconds showing 'Overland AI' logo
      if (videoRef.current.currentTime >= 108) {
        videoRef.current.currentTime = 0;
      }
    }
  };

  const toggleSound = () => {
    if (videoRef.current) {
      if (isMuted) {
        videoRef.current.muted = false;
        videoRef.current.volume = 0.3;
        setIsMuted(false);
        videoRef.current.play().catch(() => {});
      } else {
        videoRef.current.muted = true;
        setIsMuted(true);
      }
    }
  };

  const handleScrollToOtonomi = (e: React.MouseEvent) => {
    e.preventDefault();
    const elem = document.getElementById("otonomi");
    if (elem) {
      elem.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section className="relative w-full pt-[96px] sm:pt-[104px] pb-12 px-4 sm:px-8 max-w-[1440px] mx-auto selection:bg-[#C8FF00] selection:text-black">
      {/* Stable, Framed High-End Dashboard Video Container */}
      <div className="relative w-full h-[75vh] sm:h-[82vh] rounded-[28px] overflow-hidden border border-white/15 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.95)] flex items-end justify-between p-5 sm:p-8 bg-[#07090c]">
        
        {/* Video Player */}
        <video
          ref={videoRef}
          autoPlay
          loop
          muted
          playsInline
          onTimeUpdate={handleTimeUpdate}
          className="absolute inset-0 w-full h-full object-cover filter brightness-[0.9] contrast-105"
        >
          <source src="/hero-video.mp4" type="video/mp4" />
        </video>

        {/* Ambient Dark Gradient Overlays */}
        <div className="absolute inset-0 bg-gradient-to-t from-[#07090c] via-transparent to-black/30 pointer-events-none z-1" />
        <div className="absolute inset-0 bg-gradient-to-r from-black/50 via-transparent to-transparent pointer-events-none z-1" />

        {/* Collapsible Tactical Drawer Panel (Bottom-Left) */}
        <div className="relative z-20 max-w-xl w-full pointer-events-auto">
          <div className="rounded-2xl bg-black/75 border border-white/15 backdrop-blur-xl shadow-[0_25px_60px_rgba(0,0,0,0.8)] overflow-hidden transition-all duration-500">
            
            {/* Drawer Header Bar */}
            <button
              onClick={() => setIsDrawerOpen(!isDrawerOpen)}
              className="w-full px-5 py-3 flex items-center justify-between bg-white/[0.04] hover:bg-white/[0.08] transition-colors cursor-pointer border-b border-white/10"
            >
              <div className="flex items-center gap-2.5">
                <span className="w-2 h-2 rounded-full bg-[#C8FF00] animate-ping" />
                <span className="font-mono text-xs font-bold text-[#C8FF00] tracking-wider uppercase">
                  TRUSTIA AI // SİSTEM PANELİ
                </span>
              </div>

              <div className="flex items-center gap-2 text-slate-300 text-xs font-mono">
                <span className="hidden sm:inline text-slate-400">
                  {isDrawerOpen ? "Paneli Gizle" : "Paneli Göster"}
                </span>
                {isDrawerOpen ? (
                  <ChevronDown className="w-4 h-4 text-[#C8FF00]" />
                ) : (
                  <ChevronUp className="w-4 h-4 text-[#C8FF00]" />
                )}
              </div>
            </button>

            {/* Drawer Content */}
            {isDrawerOpen && (
              <div className="p-5 sm:p-7 space-y-4 animate-fadeIn">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-[11px] font-mono font-bold tracking-wider uppercase">
                  <Shield className="w-3.5 h-3.5" />
                  <span>%100 YERLİ KATKI SERTİFİKASYON UYUMLU</span>
                </div>

                <h1 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight leading-tight">
                  Zorlu Operasyon Sahalarında Tam Otonom Milli İrade
                </h1>

                <p className="text-slate-300 text-xs sm:text-sm leading-relaxed font-normal">
                  GPS sinyalinin bulunmadığı veya engellendiği harekat alanlarında İnsansız Kara Araçları (İKA) için geliştirilmiş sıfır dış bağımlılıklı askeri otonomi platformu.
                </p>

                <div className="pt-2 flex items-center gap-4">
                  <button
                    onClick={handleScrollToOtonomi}
                    className="px-6 py-3 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all cursor-pointer"
                  >
                    <span>SİSTEMİ İNCELE</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Minimal Transparent Sound Button (Bottom-Right) */}
        <div className="relative z-20 pointer-events-auto">
          <button
            onClick={toggleSound}
            className="px-3.5 py-2 rounded-full bg-black/40 border border-white/20 text-slate-200 hover:text-[#C8FF00] hover:border-[#C8FF00]/60 transition-all backdrop-blur-md flex items-center gap-2 text-[11px] font-mono select-none cursor-pointer shadow-lg group"
            title="Ses Kontrolü"
          >
            {isMuted ? (
              <VolumeX className="w-3.5 h-3.5 text-slate-400 group-hover:text-red-400 transition-colors" />
            ) : (
              <Volume2 className="w-3.5 h-3.5 text-[#C8FF00] animate-pulse" />
            )}
            <span className="font-medium tracking-wide">
              {isMuted ? "Sessiz" : "Ses %30"}
            </span>
          </button>
        </div>

      </div>
    </section>
  );
}
