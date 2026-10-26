"use client";

import { useEffect, useRef, useState } from "react";
import { getMifa7WireframeModel, Mifa7WireframeModel } from "./mifa7Model";

export interface TacticalCallout {
  id: string;
  name: string;
  at: [number, number, number];
  dir: [number, number, number];
  spec: string;
}

export const MIFA7_CALLOUTS: TacticalCallout[] = [
  {
    id: "lidar",
    name: "OUSTER OS2-128 3D LIDAR",
    at: [0, 1950, 800], // Center of Tripy aerodynamic roof pod
    dir: [0, 1.2, 0.3],
    spec: "240m Menzil • 3D NDT SLAM • 2.62M Nokta/sn",
  },
  {
    id: "livox",
    name: "2x LIVOX MID-360 KÖR NOKTA",
    at: [-740, 520, 2410], // Left front bumper corner intake
    dir: [-0.9, 0.4, 1.1],
    spec: "360° x 59° FOV • Ön Tampon Yakın Mesafe Yaya & Bordür",
  },
  {
    id: "canfd",
    name: "100Hz CAN-FD DRIVE-BY-WIRE",
    at: [-420, 650, 1200], // EPS steering rack & i-Booster
    dir: [0, -0.6, 1.2],
    spec: "Tripy EPS & i-Booster • 1.4 ms Gecikme • 5 ms Devralma Kesmesi",
  },
  {
    id: "compute",
    name: "560 TOPS MERKEZİ OTONOM BEYİN",
    at: [0, 320, 400], // Underfloor electronics hub
    dir: [0.9, -0.7, -0.6],
    spec: "NVIDIA Orin & Horizon BPU • 4TB NVMe Kara Kutu (EDR)",
  },
  {
    id: "vision",
    name: "4x SONY IMX390 HDR KAMERA",
    at: [0, 1860, 1220], // Roof pod front twin camera cowlings
    dir: [0, 1.1, 0.8],
    spec: "120 dB Dinamik Aralık • 60 FPS Senkronize FSYNC",
  },
  {
    id: "safety",
    name: "ISO 26262 ASIL-D WATCHDOG",
    at: [0, 450, -200], // Central ASIL-D safety arbiter
    dir: [-1.1, 0.5, 0.3],
    spec: "50 ms Donanımsal Watchdog • 1.5 m/s² Kontrollü MRM Sağa Çekme",
  },
];

interface TacticalVehicleWireframeProps {
  activeId?: string;
  onSelectCallout?: (id: string) => void;
  className?: string;
}

export default function TacticalVehicleWireframe({
  activeId = "lidar",
  onSelectCallout,
  className = "",
}: TacticalVehicleWireframeProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const containerRef = useRef<HTMLDivElement | null>(null);
  const modelRef = useRef<Mifa7WireframeModel | null>(null);

  const [labelCoords, setLabelCoords] = useState<
    Array<{
      id: string;
      name: string;
      spec: string;
      x: number;
      y: number;
      active: boolean;
    }>
  >([]);

  // State refs for animation & interaction
  const yawRef = useRef<number>(-2.45);
  const spinSpeedRef = useRef<number>(0.07);
  const isDraggingRef = useRef<boolean>(false);
  const dragStartXRef = useRef<number>(0);
  const isVisibleRef = useRef<boolean>(false);
  const pulseRef = useRef<number>(0);

  // Initialize MIFA 7 model instantly
  useEffect(() => {
    modelRef.current = getMifa7WireframeModel();
  }, []);

  // Main 3D Canvas Rendering Loop
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number;
    let lastTime = performance.now();

    function render() {
      if (!ctx || !canvas) return;

      const now = performance.now();
      const dt = Math.min((now - lastTime) / 1000, 0.1);
      lastTime = now;
      pulseRef.current += dt * 3;

      const m = modelRef.current;
      if (!m) {
        if (isVisibleRef.current) animId = requestAnimationFrame(render);
        return;
      }

      // 1. Inertial Rotation Decay & Auto-Orbit
      if (!isDraggingRef.current) {
        yawRef.current += spinSpeedRef.current * dt;
        spinSpeedRef.current *= Math.pow(0.85, dt * 60);
        if (Math.abs(spinSpeedRef.current) < 0.04) {
          spinSpeedRef.current = 0.04; // Smooth continuous idle rotation
        }
      }

      // 2. High-DPI Canvas Resizing
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      if (canvas.width !== width * dpr || canvas.height !== height * dpr) {
        canvas.width = width * dpr;
        canvas.height = height * dpr;
      }

      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, width, height);

      // 3. 3D Camera Setup
      const yaw = yawRef.current;
      const pitch = 0.32; // Slight downward isometric perspective
      const cosY = Math.cos(yaw),
        sinY = Math.sin(yaw);
      const cosP = Math.cos(pitch),
        sinP = Math.sin(pitch);

      // Scale model to fit canvas cleanly with comfortable margins
      const scale = Math.min(width / (m.R * 2.35), height / (m.R * 1.65));
      const cx = width / 2;
      const cy = height * 0.52;

      // Project 3D point (X, Y, Z) into 2D Screen Space
      const project = (px: number, py: number, pz: number): [number, number, number] => {
        // Shift relative to center M
        const dx = px - m.M[0];
        const dy = py - m.M[1];
        const dz = pz - m.M[2];

        // Yaw rotation
        const x1 = dx * cosY - dz * sinY;
        const z1 = dx * sinY + dz * cosY;

        // Pitch rotation
        const y2 = dy * cosP - z1 * sinP;
        const z2 = dy * sinP + z1 * cosP;

        // Isometric perspective projection
        const focal = 3200;
        const pFactor = focal / (focal + z2 * 0.45);
        const sx = cx + x1 * scale * pFactor;
        const sy = cy - y2 * scale * pFactor;

        return [sx, sy, z2];
      };

      // 4. Transform & Depth-Sort Lines
      const { PXYZ, start, npoly } = m;
      const bucketsCount = 20;
      const depthBuckets: number[][] = Array.from({ length: bucketsCount }, () => []);

      for (let i = 0; i < npoly; i++) {
        const s = start[i];
        const e = start[i + 1];
        let hasPrev = false;
        let prevX = 0,
          prevY = 0,
          prevZ = 0;

        for (let idx = s; idx < e; idx++) {
          const [sx, sy, sz] = project(PXYZ[idx * 3], PXYZ[idx * 3 + 1], PXYZ[idx * 3 + 2]);
          if (hasPrev) {
            const avgZ = (prevZ + sz) / 2;
            const normZ = Math.max(0, Math.min(1, (avgZ + m.R) / (2 * m.R)));
            const bIdx = Math.min(bucketsCount - 1, Math.floor(normZ * bucketsCount));
            depthBuckets[bIdx].push(prevX, prevY, sx, sy);
          }
          prevX = sx;
          prevY = sy;
          prevZ = sz;
          hasPrev = true;
        }
      }

      // 5. Draw Maxus MIFA 7 Vehicle Wireframe with Depth Fading (NO BOXES!)
      ctx.lineWidth = width < 768 ? 0.7 : 0.6;
      for (let b = 0; b < bucketsCount; b++) {
        const lines = depthBuckets[b];
        if (!lines.length) continue;
        const alpha = Math.max(0.18, 0.68 - (0.45 * b) / bucketsCount);
        ctx.strokeStyle = `rgba(235, 238, 245, ${alpha.toFixed(3)})`;
        ctx.beginPath();
        for (let j = 0; j < lines.length; j += 4) {
          ctx.moveTo(lines[j], lines[j + 1]);
          ctx.lineTo(lines[j + 2], lines[j + 3]);
        }
        ctx.stroke();
      }

      // 6. Draw Tactical Reticle / Waypoint Anchors (SIFIR KUTU - Sadece Taktiksel Nişangah Noktaları)
      const updatedLabels: Array<{
        id: string;
        name: string;
        spec: string;
        x: number;
        y: number;
        active: boolean;
      }> = [];

      MIFA7_CALLOUTS.forEach((callout) => {
        const isSelected = activeId === callout.id || (!activeId && callout.id === "lidar");
        const [anchorX, anchorY] = project(callout.at[0], callout.at[1], callout.at[2]);

        if (isSelected) {
          const pulse = Math.sin(pulseRef.current) * 0.5 + 0.5; // 0..1
          const ringR = 9 + pulse * 4;

          // Outer pulsing ring
          ctx.beginPath();
          ctx.arc(anchorX, anchorY, ringR, 0, Math.PI * 2);
          ctx.lineWidth = 1.2;
          ctx.strokeStyle = `rgba(228, 248, 13, ${0.4 + pulse * 0.4})`;
          ctx.stroke();

          // Subtle glow bloom
          ctx.beginPath();
          ctx.arc(anchorX, anchorY, 18, 0, Math.PI * 2);
          ctx.lineWidth = 4;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.15)";
          ctx.stroke();

          // Solid center core dot
          ctx.beginPath();
          ctx.arc(anchorX, anchorY, 3.5, 0, Math.PI * 2);
          ctx.fillStyle = "#E4F80D";
          ctx.fill();

          // Dashed vertical leader line extending up to the floating HUD label
          ctx.beginPath();
          ctx.setLineDash([3, 3]);
          ctx.lineWidth = 1;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.75)";
          ctx.moveTo(anchorX, anchorY - 6);
          ctx.lineTo(anchorX, anchorY - 26);
          ctx.stroke();
          ctx.setLineDash([]);
        } else {
          // Passive subtle waypoint dot on component
          ctx.beginPath();
          ctx.arc(anchorX, anchorY, 2.5, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(228, 248, 13, 0.4)";
          ctx.fill();
        }

        updatedLabels.push({
          id: callout.id,
          name: callout.name,
          spec: callout.spec,
          x: anchorX,
          y: anchorY,
          active: isSelected,
        });
      });

      setLabelCoords(updatedLabels);
      ctx.restore();

      if (isVisibleRef.current) {
        animId = requestAnimationFrame(render);
      }
    }

    // Observer to run RAF strictly when in viewport
    const observer = new IntersectionObserver(
      (entries) => {
        isVisibleRef.current = entries[0].isIntersecting;
        if (isVisibleRef.current) {
          lastTime = performance.now();
          animId = requestAnimationFrame(render);
        } else if (animId) {
          cancelAnimationFrame(animId);
        }
      },
      { threshold: 0.05 }
    );

    if (containerRef.current) {
      observer.observe(containerRef.current);
    }

    return () => {
      observer.disconnect();
      if (animId) cancelAnimationFrame(animId);
    };
  }, [activeId]);

  // Pointer Interaction (Smooth Drag to Rotate on PC & Mobile)
  const handlePointerDown = (e: React.PointerEvent) => {
    isDraggingRef.current = true;
    dragStartXRef.current = e.clientX;
    spinSpeedRef.current = 0;
  };

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!isDraggingRef.current) return;
    const dx = e.clientX - dragStartXRef.current;
    dragStartXRef.current = e.clientX;
    yawRef.current += dx * 0.007;
    spinSpeedRef.current = dx * 0.01;
  };

  const handlePointerUp = () => {
    isDraggingRef.current = false;
  };

  return (
    <div
      ref={containerRef}
      className={`relative w-full h-full select-none ${className}`}
      style={{
        touchAction: "none",
        backgroundColor: "transparent",
      }}
    >
      {/* 100% Frameless Canvas (No boxes, no cards, no borders!) */}
      <canvas
        ref={canvasRef}
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={handlePointerUp}
        onPointerCancel={handlePointerUp}
        className="w-full h-full block cursor-grab active:cursor-grabbing"
        style={{
          touchAction: "none",
        }}
      />

      {/* Floating Tactical Yellow HUD Badges (Projected onto Maxus MIFA 7) */}
      <div className="absolute inset-0 pointer-events-none">
        {labelCoords.map((lbl) => {
          if (!lbl.active) return null;
          return (
            <div
              key={lbl.id}
              className="absolute z-20 transition-all duration-150 transform -translate-x-1/2 -translate-y-full pointer-events-auto cursor-pointer"
              style={{
                left: `${lbl.x}px`,
                top: `${lbl.y - 24}px`,
              }}
              onClick={() => onSelectCallout?.(lbl.id)}
            >
              {/* Tactical Volt Yellow Badge (0px border-radius, pure black text) */}
              <div className="px-2.5 py-1 bg-[#E4F80D] text-black font-mono text-[10px] sm:text-[11px] font-bold uppercase tracking-wider shadow-[0_0_15px_rgba(228,248,13,0.7)] flex items-center gap-1.5 whitespace-nowrap">
                <span className="w-1.5 h-1.5 bg-black" />
                <span>{lbl.name}</span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Subtle Drag Rotation Helper Text at Bottom */}
      <div className="absolute bottom-2 inset-x-0 mx-auto text-center pointer-events-none z-10">
        <span className="text-[10px] font-mono tracking-widest uppercase text-white/40 drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
          ↔ 3D ÇEVİRMEK İÇİN SÜRÜKLEYİN • SAIC MAXUS MIFA 7 (2.975mm DİNGİL)
        </span>
      </div>
    </div>
  );
}
