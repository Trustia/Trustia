"use client";

import React from "react";
import TopographicCanvas from "@/components/TopographicCanvas";

interface TacticalBackgroundLayersProps {
  watermarkText?: string;
  theme?: "robotaxi" | "defense" | "platform";
  showTopo?: boolean;
}

export default function TacticalBackgroundLayers({
  watermarkText = "TRIPY MIFA 7",
  theme = "robotaxi",
  showTopo = true,
}: TacticalBackgroundLayersProps) {
  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none select-none z-0">
      {/* 1. LAYER: Multi-Point Volumetric Radial Lighting Accents */}
      {/* Top-Left Tactical Volt Spotlight */}
      <div
        className="absolute -top-32 -left-32 w-[650px] h-[650px] rounded-full blur-[140px] opacity-25 pointer-events-none"
        style={{
          background:
            theme === "robotaxi"
              ? "radial-gradient(circle, #E4F80D 0%, rgba(228, 248, 13, 0.2) 40%, transparent 70%)"
              : "radial-gradient(circle, #00F0FF 0%, rgba(0, 240, 255, 0.2) 40%, transparent 70%)",
        }}
      />

      {/* Center-Right Warm Tactical Sand Glow (Overland AI Khaki E5D6BC) */}
      <div
        className="absolute top-1/4 -right-36 w-[700px] h-[700px] rounded-full blur-[160px] opacity-20 pointer-events-none"
        style={{
          background: "radial-gradient(circle, #E5D6BC 0%, rgba(216, 200, 124, 0.25) 45%, transparent 70%)",
        }}
      />

      {/* Deep Vehicle Halo (Directly behind 3D MIFA 7 Wireframe) */}
      <div
        className="absolute top-[56%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-[90vw] max-w-[1100px] h-[520px] rounded-full blur-[130px] opacity-25 pointer-events-none"
        style={{
          background: "radial-gradient(ellipse at center, rgba(228, 248, 13, 0.35) 0%, rgba(216, 200, 124, 0.15) 35%, transparent 70%)",
        }}
      />

      {/* Bottom Stealth Navy/Cyan Floor */}
      <div
        className="absolute -bottom-36 left-1/4 w-[850px] h-[600px] rounded-full blur-[180px] opacity-20 pointer-events-none"
        style={{
          background: "radial-gradient(circle, #0B2545 0%, rgba(14, 34, 61, 0.4) 50%, transparent 75%)",
        }}
      />

      {/* 2. LAYER: Procedural 2D Marching Squares Topographic Elevation Contours */}
      {showTopo && (
        <div className="absolute inset-0 opacity-30 sm:opacity-40 mix-blend-screen pointer-events-none">
          <TopographicCanvas
            className="absolute inset-0 w-full h-full pointer-events-none"
            inkColor={theme === "robotaxi" ? "216, 200, 124" : "168, 159, 140"}
            bands={40}
            step={8}
            freq={0.019}
            interactive={false}
          />
        </div>
      )}

      {/* 3. LAYER: Tactical Engineering Grid & Crosshairs '+' Matrix */}
      <svg
        className="absolute inset-0 w-full h-full opacity-25 pointer-events-none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <pattern
            id={`tactical-grid-${theme}`}
            width="80"
            height="80"
            patternUnits="userSpaceOnUse"
          >
            {/* Fine Sub-grid line */}
            <path
              d="M 80 0 L 0 0 0 80"
              fill="none"
              stroke="rgba(255, 255, 255, 0.06)"
              strokeWidth="0.8"
            />
            {/* Center Crosshair '+' */}
            <path
              d="M 40 35 L 40 45 M 35 40 L 45 40"
              stroke="#E4F80D"
              strokeWidth="0.8"
              strokeOpacity="0.45"
            />
            {/* Corner micro-dot */}
            <circle cx="80" cy="80" r="1" fill="rgba(255, 255, 255, 0.15)" />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill={`url(#tactical-grid-${theme})`} />
      </svg>

      {/* 4. LAYER: Concentric Tactical Radar / LiDAR Range Reticle Rings */}
      <div className="absolute top-[56%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-[640px] h-[640px] sm:w-[860px] sm:h-[860px] pointer-events-none select-none opacity-35">
        <svg viewBox="0 0 800 800" className="w-full h-full text-[#E4F80D]">
          {/* Inner 50m Range Ring */}
          <circle
            cx="400"
            cy="400"
            r="140"
            fill="none"
            stroke="currentColor"
            strokeWidth="0.8"
            strokeDasharray="3 6"
            opacity="0.4"
          />
          {/* Mid 120m Range Ring */}
          <circle
            cx="400"
            cy="400"
            r="260"
            fill="none"
            stroke="currentColor"
            strokeWidth="0.8"
            strokeDasharray="4 8"
            opacity="0.6"
          />
          {/* Outer 240m LiDAR Horizon */}
          <circle
            cx="400"
            cy="400"
            r="380"
            fill="none"
            stroke="currentColor"
            strokeWidth="1"
            strokeDasharray="6 12"
            opacity="0.8"
          />
          {/* Crosshair Axes */}
          <line
            x1="20"
            y1="400"
            x2="780"
            y2="400"
            stroke="currentColor"
            strokeWidth="0.6"
            strokeDasharray="2 6"
            opacity="0.35"
          />
          <line
            x1="400"
            y1="20"
            x2="400"
            y2="780"
            stroke="currentColor"
            strokeWidth="0.6"
            strokeDasharray="2 6"
            opacity="0.35"
          />
          {/* Tactical Telemetry Labels */}
          <text x="408" y="38" fill="currentColor" fontSize="10" fontFamily="monospace" opacity="0.6">
            000° N [OUSTER 128 CH]
          </text>
          <text x="735" y="395" fill="currentColor" fontSize="10" fontFamily="monospace" opacity="0.6">
            090° E
          </text>
          <text x="408" y="775" fill="currentColor" fontSize="10" fontFamily="monospace" opacity="0.6">
            180° S
          </text>
          <text x="24" y="395" fill="currentColor" fontSize="10" fontFamily="monospace" opacity="0.6">
            270° W
          </text>
          <text x="408" y="270" fill="currentColor" fontSize="9" fontFamily="monospace" opacity="0.7">
            120m SENSÖR RADYUSU
          </text>
          <text x="408" y="150" fill="currentColor" fontSize="9" fontFamily="monospace" opacity="0.85">
            240m MAKSİMUM MENZİL
          </text>
        </svg>
      </div>

      {/* 5. LAYER: Radiant Illuminated Stencil Watermark (Glows & Pops) */}
      <div className="absolute top-[56%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-full text-center z-0 pointer-events-none select-none">
        <span
          className="text-[9.5vw] sm:text-[11.5vw] font-mono font-black uppercase tracking-tight whitespace-nowrap block drop-shadow-[0_0_55px_rgba(228,248,13,0.22)]"
          style={{
            color: "rgba(255, 255, 255, 0.08)",
            WebkitTextStroke: "1.5px rgba(228, 248, 13, 0.28)",
          }}
        >
          {watermarkText}
        </span>
      </div>

      {/* 6. LAYER: Deep Edge Seamless Vignette (Blends into adjacent sections) */}
      <div className="absolute top-0 inset-x-0 h-32 bg-gradient-to-b from-[#090b0e] via-[#090b0e]/70 to-transparent pointer-events-none" />
      <div className="absolute bottom-0 inset-x-0 h-32 bg-gradient-to-t from-[#090b0e] via-[#090b0e]/70 to-transparent pointer-events-none" />
    </div>
  );
}
