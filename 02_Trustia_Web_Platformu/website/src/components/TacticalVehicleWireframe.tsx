"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { getMifa7WireframeModel, Mifa7WireframeModel } from "./mifa7Model";

export interface TacticalCallout {
  id: string;
  name: string;
  at: [number, number, number];
  size: [number, number, number];
  dir: [number, number, number];
  spec: string;
}

export const MIFA7_CALLOUTS: TacticalCallout[] = [
  {
    id: "lidar",
    name: "OUSTER OS2-128 3D LIDAR",
    at: [0, 1900, 250],
    size: [320, 140, 300],
    dir: [0, 1.2, 0.3],
    spec: "240m Menzil • 3D NDT SLAM • 2.62M Nokta/sn",
  },
  {
    id: "livox",
    name: "2x LIVOX MID-360 KÖR NOKTA",
    at: [-740, 650, 2410],
    size: [180, 140, 140],
    dir: [-0.9, 0.4, 1.1],
    spec: "360° x 59° FOV • Ön Tampon Yakın Mesafe Yaya & Bordür",
  },
  {
    id: "canfd",
    name: "100Hz CAN-FD DRIVE-BY-WIRE",
    at: [0, 500, 1480],
    size: [300, 160, 240],
    dir: [0, -0.6, 1.2],
    spec: "Tripy EPS & i-Booster • 1.4 ms Gecikme • 5 ms Devralma Kesmesi",
  },
  {
    id: "compute",
    name: "560 TOPS MERKEZİ OTONOM BEYİN",
    at: [0, 420, -150],
    size: [440, 180, 420],
    dir: [0.9, -0.7, -0.6],
    spec: "NVIDIA Orin & Horizon BPU • 4TB NVMe Kara Kutu (EDR)",
  },
  {
    id: "vision",
    name: "4x SONY IMX390 HDR KAMERA",
    at: [0, 1550, 950],
    size: [480, 120, 380],
    dir: [0, 1.1, 0.8],
    spec: "120 dB Dinamik Aralık • 60 FPS Senkronize FSYNC",
  },
  {
    id: "safety",
    name: "ISO 26262 ASIL-D WATCHDOG",
    at: [-380, 750, 400],
    size: [280, 140, 260],
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

  // Initialize MIFA 7 model instantly
  useEffect(() => {
    modelRef.current = getMifa7WireframeModel();
  }, []);

  // 3D Bounding Box Edge Generator
  const getBoxEdges = useCallback(
    (
      cx: number,
      cy: number,
      cz: number,
      sx: number,
      sy: number,
      sz: number
    ): Array<[[number, number, number], [number, number, number]]> => {
      const hx = sx / 2,
        hy = sy / 2,
        hz = sz / 2;
      const c = [
        [cx - hx, cy - hy, cz - hz],
        [cx + hx, cy - hy, cz - hz],
        [cx + hx, cy + hy, cz - hz],
        [cx - hx, cy + hy, cz - hz],
        [cx - hx, cy - hy, cz + hz],
        [cx + hx, cy - hy, cz + hz],
        [cx + hx, cy + hy, cz + hz],
        [cx - hx, cy + hy, cz + hz],
      ];
      return [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7],
      ].map(([i1, i2]) => [
        c[i1] as [number, number, number],
        c[i2] as [number, number, number],
      ]);
    },
    []
  );

  // Main Render Loop (100% frameless, hardware accelerated)
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number | null = null;
    let lastTime = performance.now();

    const pitch = -0.25; // ~14 deg isometric top-angle view
    const bucketsCount = 10;
    const depthBuckets: number[][] = Array.from({ length: bucketsCount }, () => []);

    function render(now: number) {
      if (!canvas || !ctx) return;
      const model = modelRef.current || getMifa7WireframeModel();

      const dt = Math.min(0.05, (now - lastTime) / 1000 || 0);
      lastTime = now;

      // Auto inertia spin when user is not dragging
      if (!isDraggingRef.current) {
        yawRef.current += spinSpeedRef.current * dt * 0.9;
        spinSpeedRef.current += (0.07 - spinSpeedRef.current) * 0.05;
      }

      const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;

      if (canvas.width !== Math.round(width * dpr) || canvas.height !== Math.round(height * dpr)) {
        canvas.width = Math.round(width * dpr);
        canvas.height = Math.round(height * dpr);
      }

      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, width, height);

      const yaw = yawRef.current;
      const cosY = Math.cos(yaw),
        sinY = Math.sin(yaw);
      const cosP = Math.cos(pitch),
        sinP = Math.sin(pitch);

      const center = model.M;
      const projectedRadius = model.RY * cosP + model.R * Math.abs(sinP);
      const fit = width < 768 ? 0.98 : 0.88;
      const scale = Math.min(width / 2 / model.R, height / 2 / projectedRadius) * fit;

      const screenCenterX = width / 2;
      const screenCenterY = height / 2 + (width < 768 ? 15 : 25);

      // Project point [px, py, pz] to screen [sx, sy, depth]
      const project = (px: number, py: number, pz: number): [number, number, number] => {
        const dx = px - center[0];
        const dy = py - center[1];
        const dz = pz - center[2];
        const rotY = -dx * sinY + dz * cosY;
        const sx = screenCenterX + (dx * cosY + dz * sinY) * scale;
        const sy = screenCenterY - (dy * cosP - rotY * sinP) * scale;
        const depth = dy * sinP + rotY * cosP;
        return [sx, sy, depth];
      };

      // Clear depth buckets
      for (let i = 0; i < bucketsCount; i++) depthBuckets[i].length = 0;

      const { PXYZ, start, npoly } = model;
      const depthSpan = 2600;

      // Group wireframe segments into depth buckets for realistic 3D depth cueing
      for (let i = 0; i < npoly; i++) {
        const pStart = start[i];
        const pEnd = start[i + 1];
        let prevX = 0,
          prevY = 0,
          prevZ = 0,
          hasPrev = false;

        for (let p = pStart; p < pEnd; p++) {
          const [sx, sy, sz] = project(PXYZ[3 * p], PXYZ[3 * p + 1], PXYZ[3 * p + 2]);
          if (hasPrev) {
            const avgDepth = (prevZ + sz) / 2;
            const normDepth = Math.min(1, Math.max(0, (avgDepth + depthSpan) / (2 * depthSpan)));
            const bucketIdx = Math.min(bucketsCount - 1, (normDepth * bucketsCount) | 0);
            depthBuckets[bucketIdx].push(prevX, prevY, sx, sy);
          }
          prevX = sx;
          prevY = sy;
          prevZ = sz;
          hasPrev = true;
        }
      }

      // 1. Draw Maxus MIFA 7 Vehicle Wireframe with Depth Fading
      ctx.lineWidth = width < 768 ? 0.6 : 0.5;
      for (let b = 0; b < bucketsCount; b++) {
        const lines = depthBuckets[b];
        if (!lines.length) continue;
        const alpha = Math.max(0.18, 0.65 - (0.45 * b) / bucketsCount);
        ctx.strokeStyle = `rgba(242, 238, 230, ${alpha.toFixed(3)})`;
        ctx.beginPath();
        for (let j = 0; j < lines.length; j += 4) {
          ctx.moveTo(lines[j], lines[j + 1]);
          ctx.lineTo(lines[j + 2], lines[j + 3]);
        }
        ctx.stroke();
      }

      // 2. Draw 3D Tactical Bounding Boxes & Anchors on Maxus MIFA 7
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
        const edges = getBoxEdges(
          callout.at[0],
          callout.at[1],
          callout.at[2],
          callout.size[0],
          callout.size[1],
          callout.size[2]
        );

        const [anchorX, anchorY] = project(callout.at[0], callout.at[1], callout.at[2]);

        ctx.beginPath();
        edges.forEach(([p1, p2]) => {
          const [x1, y1] = project(p1[0], p1[1], p1[2]);
          const [x2, y2] = project(p2[0], p2[1], p2[2]);
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
        });

        if (isSelected) {
          // Tactical Volt Yellow Highlight (#E4F80D)
          ctx.lineWidth = 1.8;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.98)";
          ctx.stroke();

          // Subtle outer glow
          ctx.lineWidth = 4;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.25)";
          ctx.stroke();

          // 7x7px solid anchor square on mounting point
          ctx.fillStyle = "rgb(228, 248, 13)";
          ctx.fillRect(anchorX - 3.5, anchorY - 3.5, 7, 7);

          // Dashed projection stem to label
          ctx.beginPath();
          ctx.setLineDash([4, 4]);
          ctx.lineWidth = 1;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.65)";
          ctx.moveTo(anchorX, anchorY);
          ctx.lineTo(anchorX, anchorY - 24);
          ctx.stroke();
          ctx.setLineDash([]);
        } else {
          // Passive tactical wireframe box
          ctx.lineWidth = 0.8;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.35)";
          ctx.stroke();
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

      if (isVisibleRef.current) {
        animId = requestAnimationFrame(render);
      }
    }

    // Observer to run RAF strictly when in viewport
    const observer = new IntersectionObserver(
      (entries) => {
        isVisibleRef.current = entries[0].isIntersecting;
        if (isVisibleRef.current && !animId) {
          lastTime = performance.now();
          animId = requestAnimationFrame(render);
        } else if (!isVisibleRef.current && animId) {
          cancelAnimationFrame(animId);
          animId = null;
        }
      },
      { rootMargin: "150px" }
    );
    observer.observe(canvas);

    return () => {
      observer.disconnect();
      if (animId) cancelAnimationFrame(animId);
    };
  }, [activeId, getBoxEdges]);

  // Pointer Interaction (Smooth Drag to Rotate on PC & Mobile)
  const handlePointerDown = (e: React.PointerEvent) => {
    isDraggingRef.current = true;
    dragStartXRef.current = e.clientX;
    (e.target as HTMLElement).setPointerCapture(e.pointerId);
  };

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!isDraggingRef.current) return;
    const dx = e.clientX - dragStartXRef.current;
    dragStartXRef.current = e.clientX;
    yawRef.current += dx * 0.007;
    spinSpeedRef.current = dx * 0.01;
  };

  const handlePointerUp = (e: React.PointerEvent) => {
    isDraggingRef.current = false;
    try {
      (e.target as HTMLElement).releasePointerCapture(e.pointerId);
    } catch {
      // ignore
    }
  };

  return (
    <div
      ref={containerRef}
      className={`relative w-full overflow-hidden select-none touch-none ${className}`}
      style={{
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
                top: `${lbl.y - 18}px`,
              }}
              onClick={() => onSelectCallout?.(lbl.id)}
            >
              {/* Tactical Volt Yellow Badge (0px border-radius, pure black text) */}
              <div className="px-2 py-0.5 bg-[#E4F80D] text-black font-mono text-[10px] sm:text-[11px] font-bold uppercase tracking-wider shadow-[0_0_15px_rgba(228,248,13,0.6)] flex items-center gap-1.5 whitespace-nowrap">
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
          ↔ 3D ÇEVİRMEK İÇİN SÜRÜKLEYİN • SAIC MAXUS MIFA 7 (2.975mm)
        </span>
      </div>
    </div>
  );
}
