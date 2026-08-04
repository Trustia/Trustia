"use client";

import { useEffect, useRef, useState } from "react";
import { Volume2, VolumeX } from "lucide-react";

export default function HeroVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isMuted, setIsMuted] = useState(true);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.volume = 0.3; // 30% sound level
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {});
      }
    }
  }, []);

  const handleTimeUpdate = () => {
    if (videoRef.current) {
      // Loop back to 0 at 108s (1:48) to trim the last 6s showing Overland AI logo
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

  return (
    <div className="fixed inset-0 w-full h-full z-0 pointer-events-none">
      {/* Fullscreen Video Background */}
      <video
        ref={videoRef}
        autoPlay
        loop
        muted
        playsInline
        onTimeUpdate={handleTimeUpdate}
        className="w-full h-full object-cover filter brightness-[0.85] contrast-105 pointer-events-auto"
      >
        <source src="/hero-video.mp4" type="video/mp4" />
      </video>

      {/* Subtle Dark Vignette & Gradient Overlays */}
      <div className="absolute inset-0 bg-gradient-to-t from-[#090b0e] via-black/40 to-[#090b0e]/70 pointer-events-none z-1" />
      <div className="absolute inset-0 bg-gradient-to-r from-[#090b0e]/80 via-transparent to-transparent pointer-events-none z-1" />

      {/* Minimal Transparent Sound Control Button (Bottom Right) */}
      <button
        onClick={toggleSound}
        className="absolute bottom-8 right-8 z-30 px-3.5 py-2 rounded-full bg-black/40 border border-white/20 text-slate-200 hover:text-[#C8FF00] hover:border-[#C8FF00]/60 transition-all backdrop-blur-md pointer-events-auto flex items-center gap-2 text-[11px] font-mono select-none cursor-pointer shadow-lg group"
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
  );
}
