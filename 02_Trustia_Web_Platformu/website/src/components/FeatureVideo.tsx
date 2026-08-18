"use client";

import { useRef, useState } from "react";
import { Play, Pause, Volume2, VolumeX } from "lucide-react";

export default function FeatureVideo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isPlaying, setIsPlaying] = useState(true);
  const [isMuted, setIsMuted] = useState(true);

  const togglePlay = () => {
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.pause();
      } else {
        videoRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const toggleMute = () => {
    if (videoRef.current) {
      videoRef.current.muted = !isMuted;
      setIsMuted(!isMuted);
    }
  };

  return (
    <section className="relative w-full py-8 sm:py-12 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#090b0e]">
      {/* 
        Responsive Panoramic Container:
        - Mobile: Natural 16:9 cinematic aspect ratio (0% cropping, full vehicle visible)
        - Desktop: 100% UNTOUCHED original sm:h-[460px] panoramic strip
      */}
      <div className="relative w-full h-auto aspect-[16/9] sm:aspect-auto sm:h-[460px] rounded-2xl sm:rounded-3xl overflow-hidden border border-white/15 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.9)] bg-[#07090c] group">
        
        {/* Clean Video Element */}
        <video
          ref={videoRef}
          src="/features-video.mp4"
          autoPlay
          loop
          muted={isMuted}
          playsInline
          className="w-full h-full object-cover object-center"
        />

        {/* Minimal Bottom-Right Controls (Play/Pause & Sound Only) */}
        <div className="absolute bottom-3 right-3 sm:bottom-5 sm:right-5 z-20 flex items-center gap-1.5 sm:gap-2 opacity-90 sm:opacity-80 group-hover:opacity-100 transition-opacity">
          {/* Play/Pause Button */}
          <button
            onClick={togglePlay}
            className="p-2 sm:p-2.5 rounded-lg sm:rounded-xl bg-black/60 border border-white/20 hover:border-[#C8FF00]/50 text-white hover:text-[#C8FF00] backdrop-blur-md transition-all duration-200 cursor-pointer shadow-md"
            aria-label="Oynat / Duraklat"
          >
            {isPlaying ? <Pause className="w-3.5 h-3.5 sm:w-4 sm:h-4" /> : <Play className="w-3.5 h-3.5 sm:w-4 sm:h-4" />}
          </button>

          {/* Sound Toggle Button */}
          <button
            onClick={toggleMute}
            className="p-2 sm:p-2.5 rounded-lg sm:rounded-xl bg-black/60 border border-white/20 hover:border-[#C8FF00]/50 text-white hover:text-[#C8FF00] backdrop-blur-md transition-all duration-200 cursor-pointer shadow-md"
            aria-label="Sesi Aç / Kapat"
          >
            {isMuted ? <VolumeX className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-amber-400" /> : <Volume2 className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[#C8FF00]" />}
          </button>
        </div>

      </div>
    </section>
  );
}
