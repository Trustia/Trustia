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
    <div className="relative w-full h-screen min-h-[580px] sm:min-h-[600px] overflow-hidden bg-black">
      {/* Fullscreen Video Background - 100% Permanently Muted Ambient Atmosphere (Zero Color Tint) */}
      <video
        ref={videoRef}
        autoPlay
        loop
        muted
        playsInline
        className="w-full h-full object-cover object-center pointer-events-none select-none"
      >
        <source src="/hero-video.mp4" type="video/mp4" />
      </video>

      {/* Subtle Pure Dark Top Vignette for Navbar Contrast (Zero Color Alteration) */}
      <div className="absolute top-0 inset-x-0 h-28 bg-gradient-to-b from-black/60 via-black/20 to-transparent pointer-events-none z-1" />

      {/* Subtle Pure Dark Bottom Fade for Natural Section Transition */}
      <div className="absolute bottom-0 inset-x-0 h-20 bg-gradient-to-t from-black/60 to-transparent pointer-events-none z-1" />
    </div>
  );
}
