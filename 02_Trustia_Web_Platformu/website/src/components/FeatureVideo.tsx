"use client";

import { useLanguage } from "@/context/LanguageContext";

export default function FeatureVideo() {
  const { lang } = useLanguage();

  return (
    <section className="relative w-full overflow-hidden bg-[#14120c] z-20">
      {/* 
        Full-Bleed Panoramic Cinematic Video:
        - 100% Edge-to-edge full width (no boxes, no borders, no padding/margin gaps)
        - Native 1920x1038 / 16:9 cinematic aspect ratio (zero digital zoom distortion, full frame visibility)
        - Hardware GPU acceleration and enhanced contrast/clarity filters
      */}
      <div className="relative w-full aspect-[16/9] sm:aspect-[1920/1038] max-h-[88vh] overflow-hidden bg-black flex items-center justify-center">
        {/* Subtle Edge Ambient Blend (Merges video seamlessly into sand above and footer below) */}
        <div className="absolute top-0 inset-x-0 h-12 sm:h-20 bg-gradient-to-b from-[#14120c] via-[#14120c]/40 to-transparent pointer-events-none z-10" />
        <div className="absolute bottom-0 inset-x-0 h-12 sm:h-20 bg-gradient-to-t from-[#14120c] via-[#14120c]/50 to-transparent pointer-events-none z-10" />

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

        {/* 100% KUTUSUZ & ÇERÇEVESİZ SAF TİPOGRAFİK GÖSTERGE */}
        <div className="absolute bottom-3 inset-x-0 mx-auto text-center sm:inset-x-auto sm:left-auto sm:right-8 sm:bottom-5 sm:text-right z-20 pointer-events-none select-none px-4 sm:px-0">
          <span className="text-[10px] sm:text-[11px] font-mono tracking-wider text-white/50 drop-shadow-[0_1px_3px_rgba(0,0,0,0.9)]">
            {lang === "tr" ? "* Temsili Gösterim / Alıntı Video" : "* Representative Footage / Reference"}
          </span>
        </div>
      </div>
    </section>
  );
}
