"use client";

import { useEffect, useRef, useState, useCallback } from "react";

export interface TacticalCallout {
  id: string;
  name: string;
  at: [number, number, number];
  size: [number, number, number];
  dir: [number, number, number];
  spec: string;
}

export const TACTICAL_CALLOUTS: TacticalCallout[] = [
  {
    id: "lidar",
    name: "OUSTER 128K LIDAR",
    at: [0, 2193, -810],
    size: [326, 112, 204],
    dir: [0, 1.1, 0.4],
    spec: "240m Menzil • 3D NDT SLAM • 2.62M Nokta/sn",
  },
  {
    id: "compute",
    name: "NVIDIA JETSON ORIN",
    at: [-25, 950, -85],
    size: [305, 185, 369],
    dir: [-1.2, 0.6, -0.2],
    spec: "275 TOPS INT8 • 4TB NVMe Kara Kutu Kaydı",
  },
  {
    id: "canfd",
    name: "100Hz CAN-FD DRIVE-BY-WIRE",
    at: [0, 1050, -1900],
    size: [207, 162, 207],
    dir: [-0.9, 0.2, 1.1],
    spec: "100 Hz Senkron Çevrim • 5ms Devralma Kesmesi",
  },
  {
    id: "vision",
    name: "4x GMSL2 HDR KAMERA",
    at: [0, 2078, -250],
    size: [594, 90, 486],
    dir: [0.6, 1.2, -0.5],
    spec: "120 dB Dinamik Aralık • Donanımsal FSYNC",
  },
  {
    id: "radar",
    name: "77GHz DOPPLER RADAR",
    at: [200, 750, -1250],
    size: [168, 144, 144],
    dir: [1.2, 0.5, -0.7],
    spec: "250m Menzil • Radyal Doppler Hız Vektörü",
  },
  {
    id: "safety",
    name: "ASIL-D WATCHDOG & MRM",
    at: [-150, 800, -170],
    size: [280, 110, 221],
    dir: [0.9, 0.7, 0.8],
    spec: "ISO 26262 ASIL-D • 50ms Watchdog • 1.5 m/s² MRM",
  },
];

interface TacticalVehicleWireframeProps {
  activeId?: string;
  onSelectCallout?: (id: string) => void;
  className?: string;
}

interface ModelData {
  PXYZ: Float32Array;
  start: Int32Array;
  npoly: number;
  M: [number, number, number];
  R: number;
  RY: number;
}

export default function TacticalVehicleWireframe({
  activeId,
  onSelectCallout,
  className = "",
}: TacticalVehicleWireframeProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [model, setModel] = useState<ModelData | null>(null);
  const [loading, setLoading] = useState(true);
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
  const yawRef = useRef<number>(-2.35);
  const spinSpeedRef = useRef<number>(0.08);
  const isDraggingRef = useRef<boolean>(false);
  const dragStartXRef = useRef<number>(0);
  const isVisibleRef = useRef<boolean>(false);

  // 1. Fetch & parse wireframe binary model (with fallback procedural chassis)
  useEffect(() => {
    let unmounted = false;

    async function loadWireframe() {
      try {
        let bytes: Uint8Array | null = null;
        // Try gzip stream first if supported
        if (typeof DecompressionStream === "function") {
          try {
            const gzRes = await fetch("/models/vehicle_wire.bin.gz");
            if (gzRes.ok) {
              const raw = new Uint8Array(await gzRes.arrayBuffer());
              if (raw[0] === 31 && raw[1] === 139) {
                const ds = new DecompressionStream("gzip");
                bytes = new Uint8Array(
                  await new Response(new Blob([raw]).stream().pipeThrough(ds)).arrayBuffer()
                );
              }
            }
          } catch {
            bytes = null;
          }
        }

        // Direct binary fetch fallback
        if (!bytes || bytes[0] !== 87 || bytes[1] !== 73) {
          const binRes = await fetch("/models/vehicle_wire.bin");
          if (!binRes.ok) throw new Error("Fallback to CDN");
          bytes = new Uint8Array(await binRes.arrayBuffer());
        }

        if (unmounted) return;

        const dv = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
        if (dv.getUint32(0, false) !== 1464422981) throw new Error("Bad wire magic");

        const npoly = dv.getUint32(4, true);
        const mn: [number, number, number] = [
          dv.getFloat32(8, true),
          dv.getFloat32(12, true),
          dv.getFloat32(16, true),
        ];
        const mx: [number, number, number] = [
          dv.getFloat32(20, true),
          dv.getFloat32(24, true),
          dv.getFloat32(28, true),
        ];
        const span = [mx[0] - mn[0] || 1, mx[1] - mn[1] || 1, mx[2] - mn[2] || 1];

        let offset = 32;
        const polyList: Float32Array[] = [];
        let totalPts = 0;

        for (let i = 0; i < npoly; i++) {
          const ptCount = dv.getUint16(offset, true);
          offset += 2;
          if (ptCount >= 2) {
            const pts = new Float32Array(3 * ptCount);
            for (let p = 0; p < ptCount; p++) {
              pts[3 * p] = mn[0] + (dv.getUint16(offset, true) / 65535) * span[0];
              pts[3 * p + 1] = mn[1] + (dv.getUint16(offset + 2, true) / 65535) * span[1];
              pts[3 * p + 2] = mn[2] + (dv.getUint16(offset + 4, true) / 65535) * span[2];
              offset += 6;
            }
            polyList.push(pts);
            totalPts += ptCount;
          } else {
            offset += ptCount * 6;
          }
        }

        const validPolyCount = polyList.length;
        const PXYZ = new Float32Array(3 * totalPts);
        const start = new Int32Array(validPolyCount + 1);

        let ptr = 0;
        for (let i = 0; i < validPolyCount; i++) {
          start[i] = ptr;
          const poly = polyList[i];
          const n = poly.length / 3;
          for (let p = 0; p < n; p++) {
            PXYZ[3 * ptr] = poly[3 * p];
            PXYZ[3 * ptr + 1] = poly[3 * p + 1];
            PXYZ[3 * ptr + 2] = poly[3 * p + 2];
            ptr++;
          }
        }
        start[validPolyCount] = ptr;

        const center: [number, number, number] = [
          (mn[0] + mx[0]) / 2,
          (mn[1] + mx[1]) / 2,
          (mn[2] + mx[2]) / 2,
        ];
        const radiusXZ = Math.hypot(mx[0] - mn[0], mx[2] - mn[2]) / 2;
        const radiusY = (mx[1] - mn[1]) / 2;

        setModel({
          PXYZ,
          start,
          npoly: validPolyCount,
          M: center,
          R: radiusXZ,
          RY: radiusY,
        });
        setLoading(false);
      } catch (err) {
        console.warn("Wireframe load failed, generating tactical procedural fallback", err);
        // Fallback procedural tactical chassis
        if (!unmounted) {
          generateProceduralChassis();
          setLoading(false);
        }
      }
    }

    function generateProceduralChassis() {
      // Procedural tactical chassis lines if binary fails
      const mn: [number, number, number] = [-1100, 300, -2500];
      const mx: [number, number, number] = [1100, 2200, 2500];
      const center: [number, number, number] = [0, 1250, 0];
      const radiusXZ = 2700;
      const radiusY = 950;

      const lines: number[][] = [];
      // Wheels
      for (const [wx, wz] of [
        [-900, -1600],
        [900, -1600],
        [-900, 1600],
        [900, 1600],
      ]) {
        for (let a = 0; a < 16; a++) {
          const t1 = (a / 16) * Math.PI * 2;
          const t2 = ((a + 1) / 16) * Math.PI * 2;
          lines.push([
            wx, 450 + 400 * Math.cos(t1), wz + 400 * Math.sin(t1),
            wx, 450 + 400 * Math.cos(t2), wz + 400 * Math.sin(t2)
          ]);
        }
      }
      // Frame rails
      lines.push([-700, 500, -2400, -700, 500, 2400]);
      lines.push([700, 500, -2400, 700, 500, 2400]);
      lines.push([-900, 950, -1400, 900, 950, -1400]);
      lines.push([-900, 950, 1400, 900, 950, 1400]);
      // Cabin roof
      lines.push([-750, 2100, -800, 750, 2100, -800]);
      lines.push([-750, 2100, 600, 750, 2100, 600]);
      lines.push([-750, 2100, -800, -750, 2100, 600]);
      lines.push([750, 2100, -800, 750, 2100, 600]);

      const totalPts = lines.length * 2;
      const PXYZ = new Float32Array(totalPts * 3);
      const start = new Int32Array(lines.length + 1);
      let ptr = 0;
      for (let i = 0; i < lines.length; i++) {
        start[i] = ptr;
        PXYZ[3 * ptr] = lines[i][0];
        PXYZ[3 * ptr + 1] = lines[i][1];
        PXYZ[3 * ptr + 2] = lines[i][2];
        ptr++;
        PXYZ[3 * ptr] = lines[i][3];
        PXYZ[3 * ptr + 1] = lines[i][4];
        PXYZ[3 * ptr + 2] = lines[i][5];
        ptr++;
      }
      start[lines.length] = ptr;

      setModel({
        PXYZ,
        start,
        npoly: lines.length,
        M: center,
        R: radiusXZ,
        RY: radiusY,
      });
    }

    loadWireframe();

    return () => {
      unmounted = true;
    };
  }, []);

  // 2. 3D Bounding Box helper
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

  // 3. Render Loop with Visibility & Interaction
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || !model) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number | null = null;
    let lastTime = performance.now();

    const pitch = -0.24; // ~14 deg downward isometric perspective
    const bucketsCount = 10;
    const depthBuckets: number[][] = Array.from({ length: bucketsCount }, () => []);

    function render(now: number) {
      if (!canvas || !ctx || !model) return;

      const dt = Math.min(0.05, (now - lastTime) / 1000 || 0);
      lastTime = now;

      // Auto inertia spin when user is not dragging
      if (!isDraggingRef.current) {
        yawRef.current += spinSpeedRef.current * dt * 0.9;
        spinSpeedRef.current += (0.08 - spinSpeedRef.current) * 0.05;
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
      const fit = width < 768 ? 0.95 : 0.88;
      const scale = Math.min(width / 2 / model.R, height / 2 / projectedRadius) * fit;

      const screenCenterX = width / 2;
      const screenCenterY = height / 2 + (width < 768 ? 10 : 20);

      // Project point [px, py, pz]
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
      const depthSpan = 2500;

      // Classify line segments into depth buckets
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

      // 1. Draw vehicle wireframe lines with Overland bone-white depth fading
      ctx.lineWidth = width < 768 ? 0.45 : 0.4;
      for (let b = 0; b < bucketsCount; b++) {
        const lines = depthBuckets[b];
        if (!lines.length) continue;
        const alpha = Math.max(0.12, 0.48 - (0.35 * b) / bucketsCount);
        ctx.strokeStyle = `rgba(242, 238, 230, ${alpha.toFixed(3)})`;
        ctx.beginPath();
        for (let j = 0; j < lines.length; j += 4) {
          ctx.moveTo(lines[j], lines[j + 1]);
          ctx.lineTo(lines[j + 2], lines[j + 3]);
        }
        ctx.stroke();
      }

      // 2. Draw 3D Tactical Bounding Boxes & Callouts
      const updatedLabels: Array<{
        id: string;
        name: string;
        spec: string;
        x: number;
        y: number;
        active: boolean;
      }> = [];

      TACTICAL_CALLOUTS.forEach((callout) => {
        const isSelected = activeId === callout.id || (!activeId && callout.id === "lidar");
        const edges = getBoxEdges(
          callout.at[0],
          callout.at[1],
          callout.at[2],
          callout.size[0],
          callout.size[1],
          callout.size[2]
        );

        // Mounting anchor point
        const [anchorX, anchorY] = project(callout.at[0], callout.at[1], callout.at[2]);

        // Draw 3D box edges
        ctx.beginPath();
        edges.forEach(([p1, p2]) => {
          const [x1, y1] = project(p1[0], p1[1], p1[2]);
          const [x2, y2] = project(p2[0], p2[1], p2[2]);
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
        });

        if (isSelected) {
          // Tactical Volt Yellow highlight (#E4F80D)
          ctx.lineWidth = 1.6;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.95)";
          ctx.stroke();

          // Outer subtle glow
          ctx.lineWidth = 4;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.22)";
          ctx.stroke();

          // Filled 7x7 anchor square
          ctx.fillStyle = "rgb(228, 248, 13)";
          ctx.fillRect(anchorX - 3.5, anchorY - 3.5, 7, 7);

          // Dashed connection line to top indicator
          ctx.beginPath();
          ctx.setLineDash([4, 4]);
          ctx.lineWidth = 1;
          ctx.strokeStyle = "rgba(228, 248, 13, 0.6)";
          ctx.moveTo(anchorX, anchorY);
          ctx.lineTo(anchorX, anchorY - 24);
          ctx.stroke();
          ctx.setLineDash([]);
        } else {
          // Dim passive tactical wire box
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

    // Observer to run RAF only when in viewport (Zero PC CPU waste)
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
  }, [model, activeId, getBoxEdges]);

  // 4. Pointer Interaction (Drag to Rotate)
  const handlePointerDown = (e: React.PointerEvent) => {
    isDraggingRef.current = true;
    dragStartXRef.current = e.clientX;
    (e.target as HTMLElement).setPointerCapture(e.pointerId);
  };

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!isDraggingRef.current) return;
    const dx = e.clientX - dragStartXRef.current;
    dragStartXRef.current = e.clientX;
    yawRef.current += dx * 0.008;
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
      {/* Loading state indicator */}
      {loading && (
        <div className="absolute inset-0 flex flex-col items-center justify-center gap-2 text-xs font-mono text-[#E4F80D] z-20">
          <div className="w-6 h-6 border-2 border-[#E4F80D] border-t-transparent rounded-full animate-spin" />
          <span>INITIALIZING 3D TACTICAL WIREFRAME...</span>
        </div>
      )}

      {/* Main Vector Wireframe Canvas */}
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

      {/* Overland-Style Floating Tactical HUD Labels (Projected onto 3D Coordinates) */}
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
              <div className="px-2 py-0.5 bg-[#E4F80D] text-black font-mono text-[10px] sm:text-[11px] font-bold uppercase tracking-wider shadow-[0_0_12px_rgba(228,248,13,0.5)] flex items-center gap-1.5 whitespace-nowrap">
                <span className="w-1.5 h-1.5 bg-black" />
                <span>{lbl.name}</span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Subtle Drag Rotation Helper Pill at Bottom Center */}
      <div className="absolute bottom-2 inset-x-0 mx-auto text-center pointer-events-none z-10">
        <span className="px-2.5 py-1 rounded bg-[#0E0D09]/80 border border-[#383226] text-[9px] font-mono text-slate-400 tracking-wider uppercase backdrop-blur-sm">
          ↔ 3D ÇEVİRMEK İÇİN SÜRÜKLEYİN
        </span>
      </div>
    </div>
  );
}
