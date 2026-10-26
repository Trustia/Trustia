"use client";

import { useLanguage } from "@/context/LanguageContext";

export default function FeatureVideo() {
  const { lang } = useLanguage();

  return (
    <section className="relative w-full overflow-hidden bg-[#090b0e] z-20">
      {/* 
        Full-Bleed Panoramic Cinematic Video:
        - 100% Edge-to-edge full width (no boxes, no borders, no padding/margin gaps)
        - Native 1920x1038 / 16:9 cinematic aspect ratio (zero digital zoom distortion, full frame visibility)
        - Hardware GPU acceleration and enhanced contrast/clarity filters
      */}
      <div className="relative w-full aspect-[16/9] sm:aspect-[1920/1038] max-h-[88vh] overflow-hidden bg-black flex items-center justify-center">
        {/* Subtle Edge Ambient Blend (Merges video seamlessly into dark sections above and below) */}
        <div className="absolute top-0 inset-x-0 h-12 sm:h-20 bg-gradient-to-b from-[#090b0e] via-[#090b0e]/40 to-transparent pointer-events-none z-10" />
        <div className="absolute bottom-0 inset-x-0 h-12 sm:h-20 bg-gradient-to-t from-[#090b0e] via-[#090b0e]/40 to-transparent pointer-events-none z-10" />

        <video
          src="/features-video.mp4"
          autoPlay
          loop
          muted
          playsInline
          preload="auto"
          disablePictureInPicture
          className="w-full h-full object-cover object-center filter contrast-[1.06] brightness-[1.02] saturate-[1.04] pointer-events-none select-none transform-gpu will-change-transform"
          style={{ imageRendering: "-webkit-optimize-contrast" }}
        />

        {/* Tactical Reference / Representative Video Watermark */}
        <div className="absolute bottom-3 right-3 sm:bottom-5 sm:right-6 z-20 pointer-events-none select-none">
          <div className="flex items-center gap-2 px-2.5 py-1 rounded bg-black/60 backdrop-blur-md text-[10px] sm:text-[11px] font-mono tracking-wider text-slate-300 border border-white/10">
            <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00]/80" />
            <span>
              {lang === "tr" ? "Temsili Gösterim / Alıntı Video" : "Representative Footage / Reference"}
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}
