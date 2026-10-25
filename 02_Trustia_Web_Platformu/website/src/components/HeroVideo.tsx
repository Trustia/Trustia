"use client";

import { useEffect, useRef } from "react";

export default function HeroVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.muted = true;
      videoRef.current.volume = 0;
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {});
      }
    }
  }, []);

  return (
    <div className="relative w-full h-screen min-h-[580px] sm:min-h-[600px] overflow-hidden bg-[#07090c]">
      {/* Fullscreen Video Background - 100% Permanently Muted Ambient Atmosphere */}
      <video
        ref={videoRef}
        autoPlay
        loop
        muted
        playsInline
        className="w-full h-full object-cover object-center filter brightness-[0.92] contrast-105 pointer-events-none select-none"
      >
        <source src="/hero-video.mp4" type="video/mp4" />
      </video>

      {/* Subtle Dark Vignette & Ambient Gradient Overlays */}
      <div className="absolute inset-0 bg-gradient-to-t from-[#090b0e] via-black/20 to-black/40 pointer-events-none z-1" />
      <div className="absolute inset-0 bg-gradient-to-r from-[#090b0e]/60 via-transparent to-transparent pointer-events-none z-1" />
    </div>
  );
}
