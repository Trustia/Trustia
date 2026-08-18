"use client";

import { useState, useEffect, useRef } from "react";
import { X, Radio, Activity, ShieldAlert, Compass, Cpu, Power, AlertTriangle, CheckCircle2, Lock, Terminal, Navigation } from "lucide-react";

interface TacticalConsoleModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function TacticalConsoleModal({ isOpen, onClose }: TacticalConsoleModalProps) {
  const [eStopActive, setEStopActive] = useState(false);
  const [activeMode, setActiveMode] = useState<string>("OTONOM DEVRİYE");
  const [rthStatus, setRthStatus] = useState(false);

  // Live Dynamic Telemetry State (Gerçek Zamanlı Canlı Değişen Değerler)
  const [speed, setSpeed] = useState(14.2);
  const [heading, setHeading] = useState(284);
  const [latency, setLatency] = useState(0.8);
  const [battery, setBattery] = useState(94);
  const [posY, setPosY] = useState(128.4);
  const [posX, setPosX] = useState(412.9);

  // Terminal Log Lines (Akan ROS 2 Terminal Kayıtları)
  const [logs, setLogs] = useState<string[]>([
    "[17:56:01] [INFO] [trustia_slam]: 3D Pose Graph Optimization converged (err: 0.0012m)",
    "[17:56:02] [INFO] [can_fd_bridge]: HMAC-SHA256 Packet ACK received (seq: 10482)",
    "[17:56:02] [INFO] [threat_fusion]: LiDAR + Thermal fusion scan clear (0 IED detected)",
    "[17:56:03] [INFO] [path_planner]: Hybrid A* trajectory calculated (nodes: 1420, time: 1.8ms)",
  ]);

  const canvasRef = useRef<HTMLCanvasElement>(null);

  // Live Telemetry Tick Effect (Her 800ms'de bir canlı veri güncellemesi)
  useEffect(() => {
    if (!isOpen) return;

    const interval = setInterval(() => {
      if (!eStopActive) {
        setSpeed((prev) => parseFloat((14.0 + Math.random() * 0.6).toFixed(1)));
        setHeading((prev) => Math.floor(283 + Math.random() * 3));
        setLatency((prev) => parseFloat((0.7 + Math.random() * 0.3).toFixed(1)));
        setPosX((prev) => parseFloat((prev + (Math.random() * 0.2 - 0.1)).toFixed(1)));
        setPosY((prev) => parseFloat((prev + (Math.random() * 0.2 - 0.1)).toFixed(1)));

        // Push new live ROS 2 log
        const timestamp = new Date().toLocaleTimeString('tr-TR');
        const logTypes = [
          `[${timestamp}] [INFO] [trustia_slam]: 3D Scan Match ICP delta < 0.002m`,
          `[${timestamp}] [INFO] [can_fd_bridge]: Heartbeat pulse OK (tx_rate: 1000Hz)`,
          `[${timestamp}] [INFO] [obstacle_avoidance]: Costmap updated (free_space: 99.4%)`,
          `[${timestamp}] [INFO] [threat_fusion]: Metal induction zero anomaly`,
        ];
        const randomLog = logTypes[Math.floor(Math.random() * logTypes.length)];
        setLogs((prevLogs) => [...prevLogs.slice(-5), randomLog]);
      } else {
        setSpeed(0.0);
        setLatency(0.0);
      }
    }, 800);

    return () => clearInterval(interval);
  }, [isOpen, eStopActive]);

  // Live Radar & Point Cloud Canvas Animation
  useEffect(() => {
    if (!isOpen || !canvasRef.current) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let angle = 0;
    let animId: number;

    const render = () => {
      ctx.fillStyle = "#070a0e";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const radius = Math.min(cx, cy) - 15;

      // Draw Grid Rings
      ctx.strokeStyle = "rgba(200, 255, 0, 0.15)";
      ctx.lineWidth = 1;
      for (let r = radius / 3; r <= radius; r += radius / 3) {
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Draw Axis Crosshair
      ctx.beginPath();
      ctx.moveTo(cx - radius, cy); ctx.lineTo(cx + radius, cy);
      ctx.moveTo(cx, cy - radius); ctx.lineTo(cx, cy + radius);
      ctx.stroke();

      // Radar Sweep Line
      angle += 0.03;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(angle);
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(radius, 0);
      ctx.strokeStyle = "#C8FF00";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Radar Sweep Fade Sector
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.arc(0, 0, radius, 0, -0.4, true);
      ctx.fillStyle = "rgba(200, 255, 0, 0.08)";
      ctx.fill();
      ctx.restore();

      // Simulated Simulated Target Points (Waypoints)
      const points = [
        { x: cx + 45, y: cy - 30 },
        { x: cx - 60, y: cy + 40 },
        { x: cx + 80, y: cy + 50 },
      ];
      points.forEach((p) => {
        ctx.fillStyle = "#C8FF00";
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "rgba(200, 255, 0, 0.4)";
        ctx.beginPath();
        ctx.arc(p.x, p.y, 8, 0, Math.PI * 2);
        ctx.stroke();
      });

      // Center UGV Marker
      ctx.fillStyle = eStopActive ? "#ef4444" : "#10b981";
      ctx.beginPath();
      ctx.arc(cx, cy, 5, 0, Math.PI * 2);
      ctx.fill();

      animId = requestAnimationFrame(render);
    };

    render();
    return () => cancelAnimationFrame(animId);
  }, [isOpen, eStopActive]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/90 backdrop-blur-xl animate-fade-in font-sans selection:bg-[#C8FF00] selection:text-black">
      <div className="relative w-full max-w-5xl max-h-[92vh] bg-[#07090d] border border-white/20 rounded-3xl shadow-[0_0_80px_rgba(0,0,0,0.95)] flex flex-col overflow-hidden text-slate-200">
        
        {/* Top Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 bg-[#040608] border-b border-white/10 shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] flex items-center justify-center">
              <Radio className="w-5 h-5 animate-pulse" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-orbitron font-extrabold text-white text-base tracking-wider">TRUSTIA GCS</span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 font-bold flex items-center gap-1">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  STANAG 4586 LEVEL 4
                </span>
              </div>
              <p className="text-[11px] font-mono text-slate-400">
                GERÇEK ZAMANLI İKA TELEMETRİ VE HARİTALAMA KONSOLU
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl bg-white/5 border border-white/10 text-slate-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
            aria-label="Konsolu Kapat"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Console Body */}
        <div className="p-6 overflow-y-auto space-y-6">
          
          {/* E-STOP Alert Banner */}
          {eStopActive && (
            <div className="p-4 rounded-2xl bg-red-500/15 border border-red-500/40 text-red-400 font-mono text-xs flex items-center justify-between animate-pulse">
              <div className="flex items-center gap-2 font-bold">
                <AlertTriangle className="w-5 h-5 shrink-0" />
                <span>DONANIMSAL ACİL DURUM (E-STOP) AKTİF! TÜM MOTOR AKTÜATÖRLERİ KİLİTLENDİ.</span>
              </div>
              <button
                onClick={() => setEStopActive(false)}
                className="px-3 py-1 rounded bg-red-500 text-white font-bold hover:bg-red-600 transition-colors"
              >
                SİSTEMİ YENİDEN BAŞLAT
              </button>
            </div>
          )}

          {/* Main Visualizer Row: Live Radar Canvas + Live Dynamic Telemetry Stream */}
          <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-stretch">
            
            {/* Left Column: Live Radar / 3D Point Cloud Canvas */}
            <div className="md:col-span-5 p-4 rounded-2xl bg-[#090d14] border border-white/10 flex flex-col justify-between items-center text-center space-y-3">
              <div className="w-full flex items-center justify-between text-xs font-mono text-slate-400 border-b border-white/10 pb-2">
                <span className="font-bold text-white flex items-center gap-1.5">
                  <Navigation className="w-3.5 h-3.5 text-[#C8FF00]" />
                  CANLI 3D RADAR & TARA
                </span>
                <span className="text-[#C8FF00]">RANGE: 150m</span>
              </div>

              {/* Animated Canvas */}
              <div className="relative w-full aspect-square max-w-[240px] rounded-full overflow-hidden border border-[#C8FF00]/30 shadow-[0_0_20px_rgba(200,255,0,0.1)]">
                <canvas ref={canvasRef} width={240} height={240} className="w-full h-full" />
              </div>

              <div className="w-full flex items-center justify-between text-[11px] font-mono text-slate-400 pt-2 border-t border-white/10">
                <span>X: <strong className="text-white">{posX}m</strong></span>
                <span>Y: <strong className="text-white">{posY}m</strong></span>
                <span>MOD: <strong className="text-[#C8FF00]">{activeMode}</strong></span>
              </div>
            </div>

            {/* Right Column: Dynamic Live Telemetry Cards */}
            <div className="md:col-span-7 grid grid-cols-2 gap-4">
              
              {/* Stat 1 */}
              <div className="p-4 rounded-2xl bg-[#090d14] border border-white/10 flex flex-col justify-between">
                <div className="text-[11px] font-mono text-slate-400 font-semibold mb-1 flex items-center justify-between">
                  <span className="flex items-center gap-1.5">
                    <Compass className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>KONUMLANMA</span>
                  </span>
                  <span className="text-[10px] text-emerald-400 font-mono">LIVE</span>
                </div>
                <div className="font-orbitron font-extrabold text-2xl text-white">3D SLAM</div>
                <div className="text-[10px] font-mono text-emerald-400 mt-2 flex items-center gap-1">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>GPS Sinyalsiz Sürüş Ok</span>
                </div>
              </div>

              {/* Stat 2 */}
              <div className="p-4 rounded-2xl bg-[#090d14] border border-white/10 flex flex-col justify-between">
                <div className="text-[11px] font-mono text-slate-400 font-semibold mb-1 flex items-center justify-between">
                  <span className="flex items-center gap-1.5">
                    <Activity className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>CANLI HIZ</span>
                  </span>
                  <span className="text-[10px] text-[#C8FF00] font-mono animate-pulse">STREAM</span>
                </div>
                <div className="font-orbitron font-extrabold text-2xl text-white">
                  {speed} <span className="text-xs font-mono text-slate-400">km/s</span>
                </div>
                <div className="text-[10px] font-mono text-slate-400 mt-2">
                  Pusula Açı: <strong className="text-white">{heading}° KD</strong>
                </div>
              </div>

              {/* Stat 3 */}
              <div className="p-4 rounded-2xl bg-[#090d14] border border-white/10 flex flex-col justify-between">
                <div className="text-[11px] font-mono text-slate-400 font-semibold mb-1 flex items-center justify-between">
                  <span className="flex items-center gap-1.5">
                    <Cpu className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>CAN BUS GECİKME</span>
                  </span>
                  <span className="text-[10px] text-emerald-400 font-mono">1000Hz</span>
                </div>
                <div className="font-orbitron font-extrabold text-2xl text-[#C8FF00]">
                  {latency} <span className="text-xs font-mono text-slate-400">ms</span>
                </div>
                <div className="text-[10px] font-mono text-slate-400 mt-2">
                  CAN FD & ROS 2 Köprü
                </div>
              </div>

              {/* Stat 4 */}
              <div className="p-4 rounded-2xl bg-[#090d14] border border-white/10 flex flex-col justify-between">
                <div className="text-[11px] font-mono text-slate-400 font-semibold mb-1 flex items-center justify-between">
                  <span className="flex items-center gap-1.5">
                    <Lock className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>KORUMALI LINK</span>
                  </span>
                  <span className="text-[10px] text-emerald-400 font-mono">OK</span>
                </div>
                <div className="font-orbitron font-extrabold text-2xl text-white">HMAC-256</div>
                <div className="text-[10px] font-mono text-emerald-400 mt-2">
                  STANAG 4586 Doğrulandı
                </div>
              </div>

            </div>

          </div>

          {/* Live ROS 2 Terminal Stream Output Box */}
          <div className="p-4 rounded-2xl bg-black border border-white/10 font-mono text-xs text-slate-300 space-y-2 shadow-inner">
            <div className="flex items-center justify-between border-b border-white/10 pb-2 text-[11px] text-slate-400">
              <span className="flex items-center gap-2 font-bold text-[#C8FF00]">
                <Terminal className="w-3.5 h-3.5" />
                CANLI ROS 2 ÇEKİRDEK LOG AKIŞI (PROD_ENGINE)
              </span>
              <span className="text-[10px] text-emerald-400">STATUS: RUNNING</span>
            </div>
            
            <div className="space-y-1 font-mono text-[11px] text-emerald-400/90 max-h-28 overflow-y-auto">
              {logs.map((log, index) => (
                <div key={index} className="leading-tight">
                  {log}
                </div>
              ))}
            </div>
          </div>

          {/* Interactive Mission Control Actions */}
          <div className="p-5 rounded-2xl bg-[#090d14] border border-white/10 space-y-3">
            <h4 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">
              TAKTİK OPERASYON MOD SEÇİMİ
            </h4>
            
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <button
                onClick={() => { setActiveMode("OTONOM DEVRİYE"); setRthStatus(false); }}
                className={`p-3.5 rounded-xl border text-left font-mono text-xs transition-all cursor-pointer ${
                  activeMode === "OTONOM DEVRİYE" && !rthStatus
                    ? "bg-[#C8FF00]/15 border-[#C8FF00] text-[#C8FF00] font-bold"
                    : "bg-white/5 border-white/10 text-slate-300 hover:bg-white/10"
                }`}
              >
                <div className="font-bold mb-1">01. OTONOM DEVRİYE</div>
                <div className="text-[10px] text-slate-400">3D SLAM Rota Takibi</div>
              </button>

              <button
                onClick={() => { setActiveMode("SÜRÜ FORMASYONU"); setRthStatus(false); }}
                className={`p-3.5 rounded-xl border text-left font-mono text-xs transition-all cursor-pointer ${
                  activeMode === "SÜRÜ FORMASYONU" && !rthStatus
                    ? "bg-[#C8FF00]/15 border-[#C8FF00] text-[#C8FF00] font-bold"
                    : "bg-white/5 border-white/10 text-slate-300 hover:bg-white/10"
                }`}
              >
                <div className="font-bold mb-1">02. SÜRÜ FORMASYONU</div>
                <div className="text-[10px] text-slate-400">Kama / Baklava Düzeni</div>
              </button>

              <button
                onClick={() => { setRthStatus(true); setActiveMode("LINKLOSS RTH"); }}
                className={`p-3.5 rounded-xl border text-left font-mono text-xs transition-all cursor-pointer ${
                  rthStatus
                    ? "bg-amber-500/20 border-amber-500 text-amber-400 font-bold"
                    : "bg-white/5 border-white/10 text-slate-300 hover:bg-white/10"
                }`}
              >
                <div className="font-bold mb-1">03. LINKLOSS EVE DÖNÜŞ (RTH)</div>
                <div className="text-[10px] text-slate-400">Otonom Güvenli Nokta Dönüşü</div>
              </button>
            </div>
          </div>

          {/* Big Red E-STOP Hardware Trigger Button */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-5 rounded-2xl bg-red-950/30 border border-red-900/50">
            <div>
              <h4 className="font-mono text-xs font-bold text-red-400 uppercase">DONANIMSAL ACİL DURDURMA (HARDWARE E-STOP)</h4>
              <p className="text-slate-400 text-xs mt-0.5 font-normal">
                10ms içinde tüm motor sürücü ve aktüatör güçlerini keserek aracı anında kilitler.
              </p>
            </div>

            <button
              onClick={() => setEStopActive(true)}
              className="px-5 py-2.5 rounded-xl bg-red-600 hover:bg-red-700 text-white font-mono font-extrabold text-xs uppercase tracking-wider flex items-center gap-2 shadow-[0_0_20px_rgba(220,38,38,0.5)] transition-all cursor-pointer shrink-0"
            >
              <Power className="w-4 h-4" />
              <span>ACİL DURDUR (E-STOP)</span>
            </button>
          </div>

        </div>

        {/* Modal Footer Note */}
        <div className="px-6 py-3 bg-[#040608] border-t border-white/10 flex justify-between items-center text-xs font-mono text-slate-400 shrink-0">
          <span className="flex items-center gap-2 text-emerald-400 font-semibold">
            <CheckCircle2 className="w-4 h-4" /> CANLI İKA TELEMETRİ AKIŞI AKTİF (1000Hz)
          </span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-white font-bold cursor-pointer transition-colors"
          >
            KAPAT
          </button>
        </div>
      </div>
    </div>
  );
}
