"use client";

import { useState } from "react";
import {
  Compass,
  Layers,
  Radio,
  Lock,
  Cpu,
  CloudRain,
  Wifi,
  Activity,
  ShieldCheck,
  Zap,
  Terminal,
  Crosshair,
  Shield,
  Eye,
  CheckCircle2,
  Sparkles,
  ArrowUpRight
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function TechMatrixShowcase() {
  const { lang } = useLanguage();
  const [activeTab, setActiveTab] = useState<"all" | "core" | "safety" | "v2x">("all");

  return (
    <section id="teknoloji" className="relative z-20 py-20 sm:py-28 px-4 sm:px-8 lg:px-12 bg-[#05070a] border-b border-white/10 overflow-hidden">
      
      {/* 2027 Ambient Cyber Mesh Glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-[radial-gradient(ellipse_at_top,_rgba(200,255,0,0.06)_0%,_rgba(0,0,0,0)_70%)] pointer-events-none"></div>
      <div className="absolute -top-32 right-10 w-96 h-96 bg-[radial-gradient(circle,_rgba(16,185,129,0.05)_0%,_rgba(0,0,0,0)_70%)] pointer-events-none"></div>

      <div className="max-w-7xl mx-auto space-y-12 sm:space-y-16 relative">
        
        {/* Executive 2027 Futuristic Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-12 items-end pb-8 border-b border-white/10">
          <div className="lg:col-span-8 space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-[11px] font-mono tracking-wider uppercase backdrop-blur-md">
              <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00] animate-pulse"></span>
              <span>{lang === "tr" ? "TEKNOLOJİ ÇEKİRDEĞİ // v4.0 MİMARİ" : "CORE ARCHITECTURE // v4.0 TELEMETRY"}</span>
            </div>

            <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-[1.1]">
              {lang === "tr" ? (
                <>
                  Deterministik Seviye 4 <br />
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-200 via-white to-slate-400">
                    Otonom Karar ve Güvenlik Motoru
                  </span>
                </>
              ) : (
                <>
                  Deterministic Level-4 <br />
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-200 via-white to-slate-400">
                    Autonomous Decision & Safety Core
                  </span>
                </>
              )}
            </h2>
          </div>

          {/* Right Live Telemetry Status Readout */}
          <div className="lg:col-span-4 p-4 rounded-xl bg-black/60 border border-white/10 font-mono text-[11px] space-y-2 backdrop-blur-md">
            <div className="flex items-center justify-between text-slate-400 border-b border-white/5 pb-1.5">
              <span className="flex items-center gap-1.5">
                <Activity className="w-3.5 h-3.5 text-emerald-400 animate-pulse" />
                <span>TELEMETRY_ENGINE</span>
              </span>
              <span className="text-emerald-400 font-bold">100 Hz SYNC</span>
            </div>
            <div className="grid grid-cols-2 gap-2 text-[10px]">
              <div>
                <span className="text-slate-500 block">DETERMINISM:</span>
                <span className="text-slate-200 font-bold">100% MATHEMATICAL</span>
              </div>
              <div>
                <span className="text-slate-500 block">FAIL-SAFE:</span>
                <span className="text-[#C8FF00] font-bold">5ms ASIL-D OVERRIDE</span>
              </div>
            </div>
          </div>
        </div>

        {/* 2027 Bento Grid Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 sm:gap-6">
          
          {/* BENTO HERO CARD 1: 3D LiDAR SLAM & GNSS-Denied Radar Center (8 COLS) */}
          <div className="lg:col-span-8 p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-[#0c1017] via-[#090c12] to-[#07090e] border border-white/10 hover:border-[#C8FF00]/40 transition-all duration-500 flex flex-col justify-between space-y-6 relative group overflow-hidden shadow-2xl">
            
            {/* Background Radar Sweep Animation */}
            <div className="absolute -right-16 -top-16 w-80 h-80 rounded-full border border-white/5 pointer-events-none hidden sm:block">
              <div className="absolute inset-4 rounded-full border border-white/5"></div>
              <div className="absolute inset-12 rounded-full border border-white/5"></div>
              <div className="absolute inset-20 rounded-full border border-emerald-500/10"></div>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-32 h-32 rounded-full bg-emerald-500/5 animate-pulse"></div>
            </div>

            <div className="space-y-4 relative z-10">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <div className="w-9 h-9 rounded-lg bg-[#C8FF00]/10 border border-[#C8FF00]/30 flex items-center justify-center text-[#C8FF00]">
                    <Compass className="w-5 h-5" />
                  </div>
                  <div>
                    <span className="text-[10px] font-mono text-slate-400 uppercase tracking-wider block font-semibold">
                      {lang === "tr" ? "UZAYSAL SEYRÜSEFER MERKEZİ" : "SPATIAL NAVIGATION ENGINE"}
                    </span>
                    <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
                      {lang === "tr" ? "GNSS-Denied 3D LiDAR SLAM & NDT Haritalama" : "GNSS-Denied 3D LiDAR SLAM & NDT Mapping"}
                    </h3>
                  </div>
                </div>

                <span className="px-2.5 py-1 rounded bg-black/60 border border-emerald-500/30 text-emerald-400 text-[10px] font-mono font-bold shrink-0">
                  ±4.2 cm / 60s
                </span>
              </div>

              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-2xl font-sans">
                {lang === "tr"
                  ? "Uydu ve GPS sinyalinin tamamen kesildiği tüneller, kapalı otoparklar veya elektronik harp karartma alanlarında; araç üzerindeki çoklu 3D LiDAR (Livox Mid-360 / Ouster OS2) ve 400Hz ESKF IMU sensör füzyonu ile santimetre hassasiyetinde seyrüsefer ve yerel haritalama icra eder."
                  : "Continuous centimeter-level localization operating independently of satellite GNSS signals across tunnels, dense urban canyons, and electronic countermeasure theaters via Livox/Ouster 3D LiDAR NDT matching and 400Hz ESKF IMU fusion."}
              </p>
            </div>

            {/* Live Visual Telemetry HUD Strip */}
            <div className="pt-4 border-t border-white/10 grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-xs relative z-10">
              <div className="p-3 rounded-xl bg-black/50 border border-white/5 space-y-0.5">
                <span className="text-[9px] text-slate-500 block">LOCALIZATION:</span>
                <span className="text-white font-bold text-[11px]">3D NDT MATCH</span>
              </div>
              <div className="p-3 rounded-xl bg-black/50 border border-white/5 space-y-0.5">
                <span className="text-[9px] text-slate-500 block">IMU FREQUENCY:</span>
                <span className="text-emerald-400 font-bold text-[11px]">400 Hz ESKF</span>
              </div>
              <div className="p-3 rounded-xl bg-black/50 border border-white/5 space-y-0.5">
                <span className="text-[9px] text-slate-500 block">DEGENERACY:</span>
                <span className="text-slate-200 font-bold text-[11px]">AUTO-RECOVER</span>
              </div>
              <div className="p-3 rounded-xl bg-black/50 border border-white/5 space-y-0.5">
                <span className="text-[9px] text-slate-500 block">GPS DEPENDENCY:</span>
                <span className="text-[#C8FF00] font-bold text-[11px]">0% (ZERO)</span>
              </div>
            </div>
          </div>

          {/* BENTO CARD 2: ISO 26262 ASIL-D & 5ms Hardware Override (4 COLS) */}
          <div className="lg:col-span-4 p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-[#0e121a] to-[#07090e] border border-white/10 hover:border-emerald-500/40 transition-all duration-500 flex flex-col justify-between space-y-6 shadow-2xl">
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className="w-9 h-9 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <ShieldCheck className="w-5 h-5" />
                </div>
                <span className="px-2.5 py-0.5 rounded bg-emerald-950/60 border border-emerald-800 text-emerald-400 text-[10px] font-mono font-bold">
                  ASIL-D LOCK
                </span>
              </div>

              <div>
                <span className="text-[10px] font-mono text-slate-400 uppercase tracking-wider block font-semibold">
                  {lang === "tr" ? "FONKSİYONEL EMNİYET MİMARİSİ" : "FUNCTIONAL SAFETY PROTOCOL"}
                </span>
                <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                  {lang === "tr" ? "5ms Acil Devralma & Watchdog" : "5ms Hardware Takeover Override"}
                </h3>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed font-sans">
                {lang === "tr"
                  ? "Fiziksel emniyet sürücüsünün direksiyona veya frene en ufak müdahalesinde (2.5 Nm tork), sistem 5 milisaniyede donanımsal kesme rölesiyle kontrolü sürücüye devreder. 200ms paket kesintisinde otomatik Minimum Risk Manevrası (MRM) ile kontrollü duruş sağlanır."
                  : "Hard-interrupt safety relay relinquishes chassis control within 5 milliseconds upon detecting manual human steering torque (>2.5 Nm). 200ms telemetry interruptions initiate emergency Minimum Risk Maneuver (MRM) safe halt."}
              </p>
            </div>

            <div className="pt-4 border-t border-white/10 space-y-2 font-mono text-[11px]">
              <div className="flex items-center justify-between text-slate-400">
                <span>INTERRUPT LATENCY:</span>
                <span className="text-emerald-400 font-bold">&lt; 5.0 ms</span>
              </div>
              <div className="w-full bg-slate-900 rounded-full h-1.5 overflow-hidden">
                <div className="bg-emerald-400 h-1.5 rounded-full w-[96%]"></div>
              </div>
              <div className="flex items-center justify-between text-[10px] text-slate-500 pt-0.5">
                <span>FAIL-SAFE TIMEOUT:</span>
                <span className="text-white font-semibold">200ms WATCHDOG</span>
              </div>
            </div>
          </div>

          {/* BENTO CARD 3: 5s Trajectory AI & Voronoi Planning (4 COLS) */}
          <div className="lg:col-span-4 p-6 sm:p-7 rounded-3xl bg-[#0a0d13] border border-white/10 hover:border-white/20 transition-all duration-300 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-300">
                  <Activity className="w-4 h-4 text-[#C8FF00]" />
                </div>
                <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/10">
                  HYBRID A*
                </span>
              </div>

              <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "5s Yörünge & VRU Tahmini" : "5s Predictive Trajectory AI"}
              </h3>

              <p className="text-xs text-slate-400 leading-relaxed font-sans">
                {lang === "tr"
                  ? "Trafikteki yayaların ve diğer araçların hareketlerini 5 saniyelik zaman ufkunda çoklu olasılık modelleriyle simüle eder; Voronoi güvenli koridorları oluşturarak kaza riskini matematiksel olarak sıfırlar."
                  : "Simulates pedestrian and vehicular motion vectors across a 5-second prediction horizon, generating deterministic Voronoi clearance corridors under strict EU AI Act VRU guidelines."}
              </p>
            </div>

            <div className="pt-3 border-t border-white/5 flex items-center justify-between text-[10px] font-mono text-slate-400">
              <span>HORIZON: 5.0 SECONDS</span>
              <span className="text-emerald-400 font-semibold">ZERO COLLISION</span>
            </div>
          </div>

          {/* BENTO CARD 4: SecOC & HMAC-SHA256 CAN-FD Protection (4 COLS) */}
          <div className="lg:col-span-4 p-6 sm:p-7 rounded-3xl bg-[#0a0d13] border border-white/10 hover:border-white/20 transition-all duration-300 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-300">
                  <Lock className="w-4 h-4 text-emerald-400" />
                </div>
                <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/10">
                  ISO 21434 & R155
                </span>
              </div>

              <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "SecOC Kriptografik CAN-FD" : "SecOC Cryptographic CAN-FD"}
              </h3>

              <p className="text-xs text-slate-400 leading-relaxed font-sans">
                {lang === "tr"
                  ? "Direksiyon, gaz ve fren aktüatör komutları HMAC-SHA256 ve dinamik sayaç rotasyonu ile şifrelenir. Araya girme (Man-in-the-Middle) ve sahte paket tekrarı (Replay) siber saldırılarını mikro saniyede engeller."
                  : "All actuation frames are cryptographically authenticated using HMAC-SHA256 signatures with monotonic rolling counters, blocking frame injection and replay attacks at the hardware CAN-FD gateway."}
              </p>
            </div>

            <div className="pt-3 border-t border-white/5 flex items-center justify-between text-[10px] font-mono text-slate-400">
              <span>CIPHER: HMAC-SHA256</span>
              <span className="text-emerald-400 font-semibold">SECURE BOOT HSM</span>
            </div>
          </div>

          {/* BENTO CARD 5: Connected V2X & SPaT Infrastructure (4 COLS) */}
          <div className="lg:col-span-4 p-6 sm:p-7 rounded-3xl bg-[#0a0d13] border border-white/10 hover:border-white/20 transition-all duration-300 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <div className="w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-300">
                  <Wifi className="w-4 h-4 text-blue-400" />
                </div>
                <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/10">
                  C-V2X / SPaT
                </span>
              </div>

              <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "C-V2X & Akıllı Şehir Entegrasyonu" : "C-V2X Smart Infrastructure"}
              </h3>

              <p className="text-xs text-slate-400 leading-relaxed font-sans">
                {lang === "tr"
                  ? "Akıllı trafik ışıklarından (SPaT/GLOSA) anlık sinyal sürelerini alarak yeşil dalga hız optimizasyonu yapar; acil durum araçları ve diğer otonom filolarla güvenli telemetri köprüsü kurar."
                  : "Real-time communication with smart municipal signal controllers (SPaT/GLOSA) for green-wave corridor speed optimization and emergency vehicle telemetry broadcast."}
              </p>
            </div>

            <div className="pt-3 border-t border-white/5 flex items-center justify-between text-[10px] font-mono text-slate-400">
              <span>LATENCY: &lt; 10ms</span>
              <span className="text-blue-400 font-semibold">GREEN WAVE SYNC</span>
            </div>
          </div>

          {/* BENTO BOTTOM ROW 6: 1.301 Automated Verification Test Suite Terminal (12 COLS FULL WIDTH) */}
          <div className="lg:col-span-12 p-6 sm:p-8 rounded-3xl bg-[#07090d] border border-white/10 space-y-4 font-mono text-xs">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/10 pb-4">
              <div className="flex items-center gap-2">
                <Terminal className="w-4 h-4 text-emerald-400" />
                <span className="text-white font-bold tracking-wider uppercase text-xs sm:text-sm">
                  {lang === "tr" ? "OTOMATİK DOĞRULAMA & TEST HATTI (HIL BENCH)" : "AUTOMATED VERIFICATION & HIL TEST BENCH"}
                </span>
              </div>
              <div className="flex items-center gap-3 text-[11px]">
                <span className="text-slate-400">TOTAL SUITES: <strong className="text-white">1,301</strong></span>
                <span className="px-2.5 py-0.5 rounded-full bg-emerald-950/80 border border-emerald-800 text-emerald-400 font-bold">
                  %100 PASS (0 FAILURES)
                </span>
              </div>
            </div>

            {/* Simulated Real-Time Automated Verification Log Streams */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3 text-[11px] text-slate-400">
              <div className="p-3 rounded-xl bg-black/60 border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-semibold">
                  <span>[SLAM_NDT_BENCH]</span>
                  <span className="text-emerald-400">PASS</span>
                </div>
                <div className="text-[10px] text-slate-500">
                  Convergence within 8.4ms (mean drift: 0.038m over 10km synthetic loop).
                </div>
              </div>

              <div className="p-3 rounded-xl bg-black/60 border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-semibold">
                  <span>[CAN_FD_LATENCY]</span>
                  <span className="text-emerald-400">PASS</span>
                </div>
                <div className="text-[10px] text-slate-500">
                  100 Hz cyclic heartbeat with zero packet drop under 80% bus load.
                </div>
              </div>

              <div className="p-3 rounded-xl bg-black/60 border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-semibold">
                  <span>[ASIL_D_OVERRIDE]</span>
                  <span className="text-emerald-400">PASS</span>
                </div>
                <div className="text-[10px] text-slate-500">
                  Mechanical actuator disengagement measured at 4.2ms (&lt; 5.0ms ceiling).
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
