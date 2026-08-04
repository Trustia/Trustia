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
    <section className="relative w-full py-12 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#090b0e]">
      {/* Clean Panoramic Cinematic Strip Container (Metinsiz, Saf Sinematik Video Şeridi) */}
      <div className="relative w-full h-[400px] sm:h-[460px] rounded-3xl overflow-hidden border border-white/15 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.9)] bg-[#07090c] group">
        
        {/* Clean Video Element (100% Pure Video, No Text Overlay) */}
        <video
          ref={videoRef}
          src="/features-video.mp4"
          autoPlay
          loop
          muted={isMuted}
          playsInline
          className="w-full h-full object-cover"
        />

        {/* Minimal Bottom-Right Controls (Play/Pause & Sound Only) */}
        <div className="absolute bottom-5 right-5 z-20 flex items-center gap-2 opacity-80 group-hover:opacity-100 transition-opacity">
          {/* Play/Pause Button */}
          <button
            onClick={togglePlay}
            className="p-2.5 rounded-xl bg-black/60 border border-white/20 hover:border-[#C8FF00]/50 text-white hover:text-[#C8FF00] backdrop-blur-md transition-all duration-200 cursor-pointer"
            aria-label="Oynat / Duraklat"
          >
            {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
          </button>

          {/* Sound Toggle Button */}
          <button
            onClick={toggleMute}
            className="p-2.5 rounded-xl bg-black/60 border border-white/20 hover:border-[#C8FF00]/50 text-white hover:text-[#C8FF00] backdrop-blur-md transition-all duration-200 cursor-pointer"
            aria-label="Sesi Aç / Kapat"
          >
            {isMuted ? <VolumeX className="w-4 h-4 text-amber-400" /> : <Volume2 className="w-4 h-4 text-[#C8FF00]" />}
          </button>
        </div>

      </div>
    </section>
  );
}
