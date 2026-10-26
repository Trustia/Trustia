"use client";

import { useEffect, useRef } from "react";

interface TopographicCanvasProps {
  className?: string;
  inkColor?: string; // RGB string like "216, 200, 124"
  bands?: number;
  step?: number;
  freq?: number;
  interactive?: boolean;
}

export default function TopographicCanvas({
  className = "absolute inset-0 w-full h-full",
  inkColor = "216, 200, 124",
  bands = 44,
  step = 8,
  freq = 0.021,
  interactive = true,
}: TopographicCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    // 1. Mulberry32 PRNG (Pseudo-Random Generator)
    function mulberry32(seed: number) {
      return function () {
        seed = (seed |= 0) + 1831565813 | 0;
        let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
        t = t + Math.imul(t ^ (t >>> 7), 61 | t) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      };
    }

    // 2. 2D Perlin / Value Noise with smoothstep interpolation
    function createNoise(seed: number) {
      const rng = mulberry32(seed);
      const perm = new Uint8Array(512);
      const randTable = new Float32Array(256);

      for (let i = 0; i < 256; i++) {
        perm[i] = i;
        randTable[i] = rng();
      }
      for (let i = 255; i > 0; i--) {
        const j = (rng() * (i + 1)) | 0;
        const tmp = perm[i];
        perm[i] = perm[j];
        perm[j] = tmp;
      }
      for (let i = 0; i < 256; i++) {
        perm[256 + i] = perm[i];
      }

      const sample = (x: number, y: number) => randTable[perm[perm[255 & x] + (255 & y)]];
      const smooth = (t: number) => t * t * (3 - 2 * t);

      return (x: number, y: number) => {
        const fx = Math.floor(x);
        const fy = Math.floor(y);
        const rx = x - fx;
        const ry = y - fy;
        const sx = smooth(rx);
        const sy = smooth(ry);

        const s00 = sample(fx, fy);
        const s10 = sample(fx + 1, fy);
        const s01 = sample(fx, fy + 1);
        const s11 = sample(fx + 1, fy + 1);

        return s00 + (s10 - s00) * sx + (s01 - s00) * sy + (s00 - s10 - s01 + s11) * sx * sy;
      };
    }

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let noiseGen = createNoise((1e9 * Math.random()) | 0);
    const ripples: Array<{ x: number; y: number; r: number; amp: number }> = [];

    const majorEvery = 8;
    const bumpAmp = 0.55;
    const bumpRadius = 140;

    let width = 0;
    let height = 0;
    let dpr = 1;
    let isMobile = false;

    // Cache precomputed base fBm heightfield to guarantee 0% lag on PC
    let cols = 0;
    let rows = 0;
    let effectiveStep = step;
    let baseFbmGrid: Float32Array | null = null;

    // 4-octave Fractal Brownian Motion (fBm)
    function fbm(x: number, y: number) {
      let amp = 1;
      let f = freq;
      let val = 0;
      let sum = 0;
      for (let oct = 0; oct < 4; oct++) {
        val += amp * noiseGen(x * f, y * f);
        sum += amp;
        amp *= 0.5;
        f *= 2;
      }
      const norm = 0.5 + 1.9 * (val / sum - 0.48);
      return norm < 0 ? 0 : norm > 1 ? 1 : norm;
    }

    function computeBaseGrid() {
      if (width <= 0 || height <= 0) return;
      effectiveStep = isMobile ? 7 : Math.max(step, 8);
      cols = Math.ceil(width / effectiveStep) + 2;
      rows = Math.ceil(height / effectiveStep) + 2;
      baseFbmGrid = new Float32Array(cols * rows);

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          baseFbmGrid[r * cols + c] = fbm(c, r);
        }
      }
    }

    function renderContours() {
      if (!ctx || width <= 0 || height <= 0 || !baseFbmGrid) return;

      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, width, height);

      const grid = new Int16Array(cols * rows);
      const hasRipples = ripples.length > 0;

      for (let r = 0; r < rows; r++) {
        const py = r * effectiveStep;
        for (let c = 0; c < cols; c++) {
          const px = c * effectiveStep;
          let h = baseFbmGrid[r * cols + c];

          if (hasRipples) {
            for (const rip of ripples) {
              const dSq = (px - rip.x) ** 2 + (py - rip.y) ** 2;
              const rSq = rip.r * rip.r;
              if (dSq < rSq) {
                const factor = 1 - dSq / rSq;
                h += rip.amp * factor * factor;
              }
            }
            if (h > 1.6) h = 1.6;
          }

          const val = (h * bands) | 0;
          grid[r * cols + c] = val > bands - 1 ? bands - 1 : val;
        }
      }

      const minorPath = new Path2D();
      const majorPath = new Path2D();

      for (let r = 0; r < rows - 1; r++) {
        for (let c = 0; c < cols - 1; c++) {
          const v00 = grid[r * cols + c];
          const v10 = grid[r * cols + c + 1];
          const v11 = grid[(r + 1) * cols + c + 1];
          const v01 = grid[(r + 1) * cols + c];

          const minVal = Math.min(v00, v10, v11, v01);
          const maxVal = Math.max(v00, v10, v11, v01);
          if (maxVal <= minVal) continue;

          const px = c * effectiveStep;
          const py = r * effectiveStep;

          const top: [number, number] = [px + effectiveStep / 2, py];
          const right: [number, number] = [px + effectiveStep, py + effectiveStep / 2];
          const bottom: [number, number] = [px + effectiveStep / 2, py + effectiveStep];
          const left: [number, number] = [px, py + effectiveStep / 2];

          for (let level = minVal + 1; level <= maxVal; level++) {
            const targetPath = level % majorEvery === 0 ? majorPath : minorPath;
            const drawLine = (p1: [number, number], p2: [number, number]) => {
              targetPath.moveTo(p1[0], p1[1]);
              targetPath.lineTo(p2[0], p2[1]);
            };

            const bitmask =
              (v00 >= level ? 8 : 0) |
              (v10 >= level ? 4 : 0) |
              (v11 >= level ? 2 : 0) |
              (v01 >= level ? 1 : 0);

            switch (bitmask) {
              case 8:
              case 7:
                drawLine(left, top);
                break;
              case 4:
              case 11:
                drawLine(top, right);
                break;
              case 2:
              case 13:
                drawLine(right, bottom);
                break;
              case 1:
              case 14:
                drawLine(bottom, left);
                break;
              case 12:
              case 3:
                drawLine(left, right);
                break;
              case 9:
              case 6:
                drawLine(top, bottom);
                break;
              case 10:
                drawLine(left, top);
                drawLine(right, bottom);
                break;
              case 5:
                drawLine(top, right);
                drawLine(bottom, left);
                break;
            }
          }
        }
      }

      const minorAlpha = isMobile ? 0.45 : 0.38;
      const majorAlpha = isMobile ? 0.88 : 0.78;
      const minorWidth = isMobile ? 0.95 : 0.85;
      const majorWidth = isMobile ? 1.5 : 1.35;

      ctx.lineWidth = minorWidth;
      ctx.strokeStyle = `rgba(${inkColor}, ${minorAlpha})`;
      ctx.stroke(minorPath);

      ctx.lineWidth = majorWidth;
      ctx.strokeStyle = `rgba(${inkColor}, ${majorAlpha})`;
      ctx.stroke(majorPath);
    }

    function resize() {
      if (!canvas) return;
      // Cap DPR to 1.5 on desktop to eliminate fill-rate stutter while maintaining crisp lines
      dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      const newWidth = canvas.clientWidth;
      const newHeight = canvas.clientHeight;

      if (newWidth === width && newHeight === height && baseFbmGrid) {
        return;
      }

      width = newWidth;
      height = newHeight;
      isMobile = width < 768;

      if (width > 0 && height > 0) {
        canvas.width = Math.round(width * dpr);
        canvas.height = Math.round(height * dpr);
        computeBaseGrid();
        renderContours();
      }
    }

    let animId: number | null = null;
    const handleInteract = (e: MouseEvent | TouchEvent) => {
      if (!interactive || !canvas) return;
      const rect = canvas.getBoundingClientRect();
      const clientX = "touches" in e ? e.touches[0].clientX : e.clientX;
      const clientY = "touches" in e ? e.touches[0].clientY : e.clientY;

      const rip = {
        x: clientX - rect.left,
        y: clientY - rect.top,
        r: 10,
        amp: bumpAmp,
      };

      ripples.push(rip);
      if (ripples.length > 8) ripples.shift();

      const startTime = performance.now();
      const animDuration = 450;

      if (animId) cancelAnimationFrame(animId);

      function anim(now: number) {
        const progress = Math.min(1, (now - startTime) / animDuration);
        rip.r = 10 + (bumpRadius - 10) * (1 - (1 - progress) ** 3);
        renderContours();
        if (progress < 1) {
          animId = requestAnimationFrame(anim);
        } else {
          ripples.length = 0;
          renderContours();
        }
      }
      animId = requestAnimationFrame(anim);
    };

    const handleDblClick = () => {
      if (!interactive) return;
      noiseGen = createNoise((1e9 * Math.random()) | 0);
      ripples.length = 0;
      computeBaseGrid();
      renderContours();
    };

    // Use IntersectionObserver only — NO SCROLL LISTENER! (Guarantees zero scroll lag on PC)
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          resize();
        }
      },
      { rootMargin: "200px" }
    );
    observer.observe(canvas);

    let resizeTimeout: NodeJS.Timeout | null = null;
    const handleDebouncedResize = () => {
      if (resizeTimeout) clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(resize, 100);
    };

    window.addEventListener("resize", handleDebouncedResize, { passive: true });

    if (interactive) {
      canvas.addEventListener("click", handleInteract as EventListener);
      canvas.addEventListener("dblclick", handleDblClick);
      canvas.addEventListener("touchstart", handleInteract as EventListener, { passive: true });
    }

    resize();

    return () => {
      observer.disconnect();
      window.removeEventListener("resize", handleDebouncedResize);
      if (resizeTimeout) clearTimeout(resizeTimeout);
      if (animId) cancelAnimationFrame(animId);
      if (interactive) {
        canvas.removeEventListener("click", handleInteract as EventListener);
        canvas.removeEventListener("dblclick", handleDblClick);
        canvas.removeEventListener("touchstart", handleInteract as EventListener);
      }
    };
  }, [inkColor, bands, step, freq, interactive]);

  return (
    <canvas
      ref={canvasRef}
      className={className}
      style={{
        display: "block",
        willChange: "transform",
      }}
    />
  );
}
