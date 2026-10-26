"use client";

export default function FeatureVideo() {
  return (
    <section className="relative w-full py-8 sm:py-12 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#090b0e]">
      {/* 
        Responsive Panoramic Container:
        - Mobile: Natural 16:9 cinematic aspect ratio (0% cropping, full vehicle visible)
        - Desktop: 100% UNTOUCHED original sm:h-[460px] panoramic strip
      */}
      <div className="relative w-full h-auto aspect-[16/9] sm:aspect-auto sm:h-[460px] rounded-2xl sm:rounded-3xl overflow-hidden border border-white/15 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.9)] bg-[#07090c]">
        {/* Pure Cinematic Video Element - 100% Clean & Button-Free */}
        <video
          src="/features-video.mp4"
          autoPlay
          loop
          muted
          playsInline
          className="w-full h-full object-cover object-center pointer-events-none select-none"
        />
      </div>
    </section>
  );
}