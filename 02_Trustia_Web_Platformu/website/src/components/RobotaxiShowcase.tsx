"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Cpu,
  Eye,
  Layers,
  Radio,
  ArrowRight,
  ShieldCheck,
  ChevronRight,
  Zap,
  Gauge,
  Activity,
  Crosshair
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiShowcase() {
  const { lang } = useLanguage();
  const [activeSensor, setActiveSensor] = useState<"all" | "lidar" | "radar" | "camera" | "compute">("all");

  const sensorDetails = {
    all: {
      tag: lang === "tr" ? "360° ÇOKLU SENSÖR FÜZYONU" : "360° MULTI-SENSOR FUSION",
      title: lang === "tr" ? "Erken ve Geç Füzyonlu Birleşik Algılama Çekirdeği" : "Early & Late Multi-Modal Perception Core",
      desc: lang === "tr"
        ? "LiDAR 3D nokta bulutları, 77GHz Doppler radar kinematik vektörleri ve 4x GMSL2 HDR kamera akışları EKF ve derin öznitelik düzeyinde birleştirilir. Sıfır kör nokta ile deterministik çevre modeli oluşturulur."
        : "LiDAR 3D point clouds, 77GHz Doppler radar kinematic vectors, and 4x GMSL2 HDR camera streams fused via EKF and feature-level fusion for zero-blindspot deterministic world modeling.",
      metric: "240m Menzil • 0.05m Hassasiyet • <15ms Uçtan Uca Gecikme"
    },
    lidar: {
      tag: lang === "tr" ? "BİRİNCİL 3D SLAM VE DERİNLİK" : "PRIMARY 3D SLAM & DEPTH",
      title: lang === "tr" ? "Ouster OS2-128 Rev 7 3D LiDAR (Tavan Montaj)" : "Ouster OS2-128 Rev 7 3D LiDAR (Roof Mount)",
      desc: lang === "tr"
        ? "Tavan merkezine entegre 128 kanal ile saniyede 2.62 milyon nokta üretir. GPS'siz tünel, yer altı ve kanyon alanlarında 3D NDT SLAM santimetre hassasiyetinde uzaysal haritalama icra eder."
        : "Roof-mounted 128-channel solid-state spinning LiDAR generating 2.62M points/sec for GPS-denied 3D NDT SLAM spatial localization.",
      metric: "240 Metre • 128 Kanal • 0.1° Açısal Çözünürlük • UDP Gbit Ethernet"
    },
    radar: {
      tag: lang === "tr" ? "TÜM HAVA KOŞULLARI VE DOPPLER HIZ" : "ALL-WEATHER DOPPLER VELOCITY",
      title: lang === "tr" ? "Continental ARS 408-21 77GHz Otomotiv Radarı" : "Continental ARS 408-21 77GHz Automotive Radar",
      desc: lang === "tr"
        ? "Yoğun sis, sağanak yağmur, kar ve toza tam nüfuz eden doğrudan Doppler radyal hız tespiti. 250 metreye kadar öndeki araç ve hareketli cisimlerin hız vektörlerini anlık çıkarır."
        : "Penetrates dense fog, heavy rain, snow, and dust with direct Doppler radial velocity measurements up to 250 meters.",
      metric: "250 Metre Menzil • ±0.1 km/s Hız Hassasiyeti • CAN-FD Veri Yolu"
    },
    camera: {
      tag: lang === "tr" ? "360° ÇEVRESEL GÖRSEL ALGILAMA" : "360° SURROUND VISION",
      title: lang === "tr" ? "4x Leopard Sony IMX390 HDR GMSL2 Kamera" : "4x Leopard Sony IMX390 HDR GMSL2 Camera Array",
      desc: lang === "tr"
        ? "Ön, sol, sağ ve arka hatlara konumlandırılmış 120° FOV lensler ile 120 dB süper dinamik aralık. Doğrudan güneş parlaması ve tünel çıkışlarında LED titreşim (LFM) sönümleme."
        : "Synchronized 120° FOV surround cameras with 120 dB dynamic range, mitigating extreme lighting flares and tunnel transitions.",
      metric: "120 dB HDR • 60 FPS Senkron • IP67 Muhafaza • Donanımsal FSYNC"
    },
    compute: {
      tag: lang === "tr" ? "MERKEZİ HESAPLAMA VE AKTÜATÖR KÖPRÜSÜ" : "AI COMPUTE & ACTUATION BRIDGE",
      title: lang === "tr" ? "NVIDIA Jetson AGX Orin 64GB + CAN-FD Köprüsü" : "NVIDIA Jetson AGX Orin 64GB + CAN-FD Bridge",
      desc: lang === "tr"
        ? "275 TOPS merkezi otonom yapay zeka gücü. LKAS11 direksiyon torku ve SCC_FD fren/gaz komutlarını şasi CAN-FD hattına 100 Hz frekansta deterministik olarak aktarır. 5ms donanımsal devralma kesmesi."
        : "275 TOPS central AI compute interfacing directly with vehicle CAN-FD at 100 Hz cyclic rate with 5ms hard-interrupt safety fallback.",
      metric: "275 TOPS INT8 • 100 Hz Senkron Çevrim • 5ms Devralma • 4TB NVMe"
    }
  };

  const specs = [
    {
      num: "01",
      icon: Eye,
      id: "lidar" as const,
      title: "Ouster OS2-128 Rev 7 3D LiDAR",
      metric: "128 Kanal • 240m Menzil",
      desc: lang === "tr"
        ? "Saniyede 2.62 milyon nokta taraması ile 3D NDT SLAM ve santimetre hassasiyetinde uzaysal haritalama icra eder."
        : "Captures 2.62M points/sec for primary 3D NDT SLAM and spatial localization independent of GPS."
    },
    {
      num: "02",
      icon: Layers,
      id: "lidar" as const,
      title: "2x Livox Mid-360 LiDAR",
      metric: "360° x 59° • Kör Noktasız",
      desc: lang === "tr"
        ? "Ön tampon podlarına entegre çift LiDAR ile yakın mesafe yaya, bordür ve alçak engel taraması."
        : "Dual bumper-integrated LiDARs delivering comprehensive ultra-wide pedestrian and near-field obstacle tracking."
    },
    {
      num: "03",
      icon: Radio,
      id: "camera" as const,
      title: "4x Sony IMX390 GMSL2 HDR",
      metric: "120 dB Dinamik Aralık • IP67",
      desc: lang === "tr"
        ? "Tünel çıkışları ve doğrudan güneş parlamasında donanımsal senkronize 360° çevre görüş."
        : "Hardware-synchronized 360-degree vision mitigating extreme lighting transitions and dynamic flares."
    },
    {
      num: "04",
      icon: Cpu,
      id: "compute" as const,
      title: "NVIDIA Jetson AGX Orin 64GB",
      metric: "275 TOPS INT8 • 4TB NVMe",
      desc: lang === "tr"
        ? "275 TOPS merkezi AI hesaplama gücü ve kara kutu (DSSAD/EDR) sürekli telemetri kayıt kapasitesi."
        : "275 TOPS automotive AI compute running deterministic planning and high-speed telemetry black-box storage."
    },
    {
      num: "05",
      icon: Zap,
      id: "compute" as const,
      title: "100 Hz Senkron CAN-FD Aktüatör",
      metric: "LKAS11 & SCC_FD • 5ms Devralma",
      desc: lang === "tr"
        ? "Direksiyon, gaz ve fren sistemlerine 100 Hz senkron komut iletimi ve 5ms donanımsal devralma kesmesi."
        : "100 Hz cyclic actuation with 5 millisecond hard-interrupt safety fallback over CAN-FD gateways."
    }
  ];

  const current = sensorDetails[activeSensor];

  return (
    <section id="robotaxi" className="relative z-20 py-10 sm:py-16 px-4 sm:px-8 lg:px-12 bg-[#06080c] border-b border-white/10">
      <div className="max-w-7xl mx-auto space-y-6 sm:space-y-8">
        
        {/* 1. Executive Split Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-8 items-end pb-5 border-b border-white/10">
          <div className="lg:col-span-8 space-y-2">
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[10px] font-mono tracking-wider uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
              <span>{lang === "tr" ? "REFERANS OTONOMİ MİMARİSİ (RAD) // E-GMP" : "REFERENCE AUTONOMY ARCHITECTURE // E-GMP"}</span>
            </div>

            <h2 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug">
              Hyundai Ioniq 5 E-GMP{" "}
              <span className="text-slate-300 font-normal">
                {lang === "tr" ? "— Seviye 4 Donanım ve Sensör Mimarisi" : "— Level 4 Hardware & Sensor Blueprint"}
              </span>
            </h2>

            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Elektrikli araç filoları ve OEM entegrasyonu için geliştirilmiş; 128 kanallı 3D LiDAR, 77GHz radar ve 4x HDR kamera füzyonunu 100 Hz senkron CAN-FD köprüsüyle birleştiren deterministik Seviye-4 referans donanım şartnamesi."
                : "Deterministic Level-4 reference hardware architecture interfacing natively with Hyundai E-GMP via 100 Hz CAN-FD drive-by-wire, 128-channel 3D LiDAR, and multi-modal sensor fusion."}
            </p>
          </div>

          {/* Right Action Link */}
          <div className="lg:col-span-4 flex lg:justify-end">
            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-1.5 text-xs font-mono font-semibold text-white hover:text-slate-200 uppercase tracking-wider pb-0.5 border-b border-white/30 hover:border-white transition-colors"
            >
              <span>{lang === "tr" ? "Mühendislik Şartnamesi (NDA)" : "Engineering Blueprint (NDA)"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>

        {/* 2. Integrated 4-Metric Architectural Bar (KUTUSUZ & KOMPAKT) */}
        <div className="grid grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-white/10 py-3.5 border-y border-white/10 font-mono">
          <div className="py-1 px-3 first:pl-0 space-y-0.5">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "YAZILIM ÇEKİRDEĞİ" : "AUTONOMY STACK"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">16.000+</div>
            <span className="text-[10px] text-slate-400 block font-sans">
              {lang === "tr" ? "Satır C++20 / ROS 2" : "Lines of Code (C++20)"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "OTOMATİK TEST" : "AUTOMATED TESTS"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">1.301 / 1.301</div>
            <span className="text-[10px] text-emerald-400 block font-sans font-medium">
              {lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "HESAPLAMA GÜCÜ" : "AI COMPUTE"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">275 TOPS</div>
            <span className="text-[10px] text-slate-400 block font-sans">
              Jetson AGX Orin 64GB
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "LİDAR MENZİLİ" : "LIDAR RANGE"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">240 Metre</div>
            <span className="text-[10px] text-slate-400 block font-sans">
              128 Kanal Ouster OS2
            </span>
          </div>
        </div>

        {/* 3. Main Split Showcase: Interactive Sensor Fusion Schematic + Hardware Spec List */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
          
          {/* Left Column (7 Cols): Interactive Vector Sensor Coverage Blueprint */}
          <div className="lg:col-span-7 space-y-4">
            
            {/* Sensor Selection Monospaced Filter Strip */}
            <div className="flex flex-wrap items-center gap-1.5 pb-1">
              {[
                { id: "all" as const, label: lang === "tr" ? "TÜM SENSÖRLER (360°)" : "ALL SENSORS (360°)" },
                { id: "lidar" as const, label: "OUSTER 128K LİDAR" },
                { id: "radar" as const, label: "77GHz RADAR" },
                { id: "camera" as const, label: "4x HDR KAMERA" },
                { id: "compute" as const, label: "ORIN & CAN-FD" }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveSensor(tab.id)}
                  className={`px-3 py-1.5 rounded text-xs font-mono transition-all duration-200 cursor-pointer ${
                    activeSensor === tab.id
                      ? "bg-white text-slate-950 font-bold shadow-md"
                      : "bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white border border-white/10"
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>

            {/* Technical Vector Canvas (360° FOV Blueprint) */}
            <div className="relative rounded-xl overflow-hidden border border-white/10 bg-[#080b11] aspect-[16/10] flex items-center justify-center p-4">
              
              {/* Coordinate Grid Header */}
              <div className="absolute top-3 left-3 right-3 flex items-center justify-between text-[10px] font-mono text-slate-400 pointer-events-none">
                <span className="px-2 py-0.5 rounded bg-black/60 border border-white/10">
                  TOP-DOWN // 360° SENSÖR KAPSAMA GEOMETRİSİ
                </span>
                <span className="text-slate-400">
                  ÖLÇEK: 1:100 (240m ÇAP)
                </span>
              </div>

              {/* High-Precision SVG Sensor Topology */}
              <svg viewBox="0 0 600 380" className="w-full h-full max-h-[360px]" fill="none" xmlns="http://www.w3.org/2000/svg">
                {/* Background Grid Lines */}
                <defs>
                  <pattern id="archGrid" width="30" height="30" patternUnits="userSpaceOnUse">
                    <path d="M 30 0 L 0 0 0 30" fill="none" stroke="rgba(255,255,255,0.03)" strokeWidth="1" />
                  </pattern>
                  <radialGradient id="lidarGlow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.25" />
                    <stop offset="70%" stopColor="#38bdf8" stopOpacity="0.06" />
                    <stop offset="100%" stopColor="#38bdf8" stopOpacity="0" />
                  </radialGradient>
                  <linearGradient id="radarBeam" x1="0%" y1="100%" x2="0%" y2="0%">
                    <stop offset="0%" stopColor="#34d399" stopOpacity="0.35" />
                    <stop offset="100%" stopColor="#34d399" stopOpacity="0.02" />
                  </linearGradient>
                </defs>

                <rect width="600" height="380" fill="url(#archGrid)" />

                {/* Range Rings (50m, 100m, 180m, 240m) */}
                <circle cx="300" cy="190" r="45" stroke="rgba(255,255,255,0.08)" strokeDasharray="3 3" />
                <circle cx="300" cy="190" r="90" stroke="rgba(255,255,255,0.08)" strokeDasharray="3 3" />
                <circle cx="300" cy="190" r="140" stroke="rgba(255,255,255,0.06)" strokeDasharray="3 3" />

                {/* Range Labels */}
                <text x="304" y="142" fill="rgba(148,163,184,0.5)" fontSize="8" fontFamily="monospace">50m</text>
                <text x="304" y="97" fill="rgba(148,163,184,0.5)" fontSize="8" fontFamily="monospace">100m</text>
                <text x="304" y="48" fill="rgba(148,163,184,0.5)" fontSize="8" fontFamily="monospace">200m (LiDAR)</text>

                {/* --- 1. LiDAR 360° Zone --- */}
                {(activeSensor === "all" || activeSensor === "lidar") && (
                  <g className="transition-opacity duration-300">
                    <circle cx="300" cy="190" r="155" fill="url(#lidarGlow)" />
                    <circle cx="300" cy="190" r="155" stroke="#38bdf8" strokeWidth="1" strokeDasharray="4 4" opacity="0.4" />
                    {/* LiDAR 360 Degree Radial Rays */}
                    <line x1="300" y1="190" x2="300" y2="35" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.4" />
                    <line x1="300" y1="190" x2="455" y2="190" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                    <line x1="300" y1="190" x2="145" y2="190" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                  </g>
                )}

                {/* --- 2. Radar Forward Long-Range Cone (250m, 77GHz) --- */}
                {(activeSensor === "all" || activeSensor === "radar") && (
                  <g className="transition-opacity duration-300">
                    <path
                      d="M 300 155 L 210 20 A 180 180 0 0 1 390 20 Z"
                      fill="url(#radarBeam)"
                      stroke="#34d399"
                      strokeWidth="1.2"
                      opacity="0.8"
                    />
                    <path d="M 240 60 A 140 140 0 0 1 360 60" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                    <path d="M 265 105 A 90 90 0 0 1 335 105" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                    <text x="300" y="28" textAnchor="middle" fill="#34d399" fontSize="9" fontFamily="monospace" fontWeight="bold">
                      77GHz DOPPLER RADAR // 250m
                    </text>
                  </g>
                )}

                {/* --- 3. 4x Surround HDR Cameras (120° FOV Each) --- */}
                {(activeSensor === "all" || activeSensor === "camera") && (
                  <g className="transition-opacity duration-300" opacity="0.75">
                    {/* Front Camera 120° */}
                    <polygon points="300,160 200,60 400,60" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                    {/* Left Camera 120° */}
                    <polygon points="280,190 170,110 170,270" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                    {/* Right Camera 120° */}
                    <polygon points="320,190 430,110 430,270" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                    {/* Rear Camera 120° */}
                    <polygon points="300,225 210,320 390,320" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  </g>
                )}

                {/* --- 4. Vehicle Chassis Silhouette (Hyundai E-GMP 3.000 mm Wheelbase) --- */}
                <g>
                  {/* Outer Chassis */}
                  <rect x="281" y="152" width="38" height="78" rx="8" fill="#0f172a" stroke="#475569" strokeWidth="1.5" />
                  {/* Cabin Windshield & Glass */}
                  <rect x="284" y="168" width="32" height="46" rx="4" fill="#1e293b" stroke="#334155" strokeWidth="1" />
                  
                  {/* Wheels (4x) */}
                  <rect x="277" y="160" width="4" height="12" rx="1.5" fill="#64748b" />
                  <rect x="319" y="160" width="4" height="12" rx="1.5" fill="#64748b" />
                  <rect x="277" y="210" width="4" height="12" rx="1.5" fill="#64748b" />
                  <rect x="319" y="210" width="4" height="12" rx="1.5" fill="#64748b" />

                  {/* Wheelbase Dimension Line */}
                  <line x1="272" y1="166" x2="272" y2="216" stroke="rgba(148,163,184,0.4)" strokeWidth="0.8" />
                  <text x="268" y="193" textAnchor="end" fill="rgba(148,163,184,0.7)" fontSize="7" fontFamily="monospace">3.000mm</text>

                  {/* Front Bumper Sensor Pods (Livox Mid-360) */}
                  <circle cx="286" cy="154" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />
                  <circle cx="314" cy="154" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />

                  {/* Roof LiDAR Unit (Ouster OS2-128) */}
                  <circle cx="300" cy="188" r="5" fill="#0284c7" stroke="#38bdf8" strokeWidth="1.5" />
                  <circle cx="300" cy="188" r="2" fill="#ffffff" />

                  {/* Sub-Trunk Compute Hub (Jetson Orin) */}
                  <rect x="288" y="216" width="24" height="10" rx="2" fill="#047857" stroke="#34d399" strokeWidth="1" />
                  <text x="300" y="223" textAnchor="middle" fill="#ffffff" fontSize="6" fontFamily="monospace" fontWeight="bold">ORIN</text>

                  {/* CAN-FD Bus Backbone Line */}
                  {(activeSensor === "all" || activeSensor === "compute") && (
                    <line x1="300" y1="156" x2="300" y2="216" stroke="#10b981" strokeWidth="1.5" strokeDasharray="3 2" />
                  )}
                </g>

                {/* Callout Labels with Connecting Hairlines */}
                <g fontFamily="monospace" fontSize="8" fill="#94a3b8">
                  {/* Roof LiDAR Label */}
                  <path d="M 305 188 L 380 160 L 440 160" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                  <text x="445" y="163" fill="#38bdf8" fontWeight="bold">OUSTER OS2-128 (TAVAN)</text>

                  {/* Front Bumper LiDAR Label */}
                  <path d="M 283 154 L 210 140 L 150 140" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                  <text x="145" y="143" textAnchor="end" fill="#38bdf8">2x LIVOX MID-360 (TAMPON)</text>

                  {/* Sub-Trunk Compute Hub Label */}
                  <path d="M 312 221 L 380 235 L 440 235" stroke="rgba(52,211,153,0.5)" strokeWidth="0.8" />
                  <text x="445" y="238" fill="#34d399" fontWeight="bold">JETSON ORIN + 100Hz CAN-FD</text>

                  {/* Surround Cameras Label */}
                  <path d="M 277 190 L 210 210 L 150 210" stroke="rgba(245,158,11,0.5)" strokeWidth="0.8" />
                  <text x="145" y="213" textAnchor="end" fill="#f59e0b">4x SONY IMX390 GMSL2 HDR</text>
                </g>
              </svg>

              {/* Bottom Right Homologation Tag */}
              <div className="absolute bottom-3 right-3 flex items-center gap-2 text-[9px] font-mono text-slate-400">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span>ISO 26262 ASIL-D & UN ECE R157 UYUMLU</span>
              </div>
            </div>

            {/* Dynamic Specification Bar of Selected Sensor */}
            <div className="p-3.5 rounded-lg bg-white/5 border border-white/10 space-y-1">
              <div className="flex items-center justify-between text-[10px] font-mono">
                <span className="text-slate-300 font-semibold">{current.tag}</span>
                <span className="text-slate-400">{current.metric}</span>
              </div>
              <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
                {current.title}
              </div>
              <p className="text-[11px] text-slate-300 leading-relaxed font-sans">
                {current.desc}
              </p>
            </div>

          </div>

          {/* Right Column (5 Cols): Hairline Separated Hardware Architecture List (KUTUSUZ) */}
          <div className="lg:col-span-5 space-y-4">
            <div className="border-b border-white/10 pb-3">
              <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
                // REFERANS DONANIM MİMARİSİ
              </span>
              <h3 className="text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "Temel Sensör ve İşlemci Paketi" : "Core Sensor & Compute Suite"}
              </h3>
            </div>

            <div className="divide-y divide-white/10">
              {specs.map((item, idx) => {
                const Icon = item.icon;
                return (
                  <button
                    key={idx}
                    onClick={() => setActiveSensor(item.id)}
                    className="w-full text-left py-3 first:pt-0 last:pb-0 space-y-1 group hover:bg-white/[0.02] transition-colors rounded-sm cursor-pointer"
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2.5">
                        <span className="font-mono text-xs text-slate-500 font-bold">{item.num} //</span>
                        <h4 className="text-xs sm:text-sm font-bold text-white tracking-tight group-hover:text-slate-200">
                          {item.title}
                        </h4>
                      </div>
                      <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/10">
                        {item.metric}
                      </span>
                    </div>

                    <p className="text-xs text-slate-300 leading-relaxed font-sans sm:pl-7">
                      {item.desc}
                    </p>
                  </button>
                );
              })}
            </div>

            {/* Bottom Regulatory Homologation Note */}
            <div className="pt-3 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>UN ECE R157 & 1 ARALIK 2024 ADS</span>
              <span className="text-emerald-400 font-semibold">%100 UYUMLU</span>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
