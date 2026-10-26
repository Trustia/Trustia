"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Cpu,
  Eye,
  Layers,
  Radio,
  CheckCircle2,
  ChevronRight,
  Gauge,
  Lock,
  ArrowLeft,
  Zap,
  ShieldCheck,
  Activity,
  Crosshair
} from "lucide-react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiPage() {
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
      icon: Cpu,
      title: lang === "tr" ? "Merkezi AI İşlemci" : "Central AI Compute",
      val: "NVIDIA Jetson AGX Orin 64GB",
      sub: "275 TOPS INT8 • Seeed J501 Taşıyıcı Kart"
    },
    {
      icon: Eye,
      title: lang === "tr" ? "Birincil 3D SLAM" : "Primary 3D SLAM",
      val: "Ouster OS2-128 Rev 7 LiDAR",
      sub: "128 Kanal • 240m Menzil • 2.62M Nokta/sn"
    },
    {
      icon: Layers,
      title: lang === "tr" ? "Kör Nokta & Yaya LiDAR" : "Blindspot & Pedestrian LiDAR",
      val: "2x Livox Mid-360 LiDAR",
      sub: "360°x59° Ultra Geniş Açı • 45°/12° Eğimli Pod"
    },
    {
      icon: Radio,
      title: lang === "tr" ? "360° Görsel Algılama" : "360° HDR Vision",
      val: "4x Leopard Sony IMX390 GMSL2",
      sub: "120 dB Dinamik Aralık • IP67 • Donanımsal Senkron"
    },
    {
      icon: Gauge,
      title: lang === "tr" ? "Kötü Hava Radarı" : "All-Weather Radar",
      val: "2x Continental ARS 408-21 77GHz",
      sub: "250m Menzil • Sis, Şiddetli Yağmur ve Kar Filtresi"
    },
    {
      icon: Activity,
      title: lang === "tr" ? "Santimetre Konumlandırma" : "Centimeter Positioning",
      val: "Septentrio mosaic-go Heading RTK",
      sub: "Çift Mantar Anten • Durağan Pusula Açısı (Heading)"
    },
    {
      icon: Zap,
      title: lang === "tr" ? "CAN-FD Aktüatör Köprüsü" : "CAN-FD Drive-by-Wire",
      val: "Kvaser U100 CAN-FD DB9",
      sub: "100 Hz LKAS11 Direksiyon & 50 Hz SCC_FD Fren/Gaz"
    },
    {
      icon: Lock,
      title: lang === "tr" ? "Donanımsal E-Stop" : "Hardware E-Stop Shield",
      val: "Schneider Mantar Buton + ELO 80A Röle",
      sub: "10ms Mekanik Güç Kesme • ASIL-D Güvenlik"
    }
  ];

  const current = sensorDetails[activeSensor];

  return (
    <main className="relative min-h-screen bg-gradient-to-b from-[#1c1813] via-[#28221a] to-[#1c1813] text-[#f5efe6] font-sans selection:bg-[#E4F80D] selection:text-black overflow-x-hidden pt-20 sm:pt-28 pb-12">
      <Navbar />

      {/* Ambient Tactical Sand/Gold Glow */}
      <div className="absolute top-0 inset-x-0 h-[600px] bg-[radial-gradient(ellipse_at_top,rgba(229,214,188,0.10),transparent_70%)] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-6 sm:space-y-8">

        {/* 1. Breadcrumb & Header */}
        <div className="space-y-2.5">
          <div className="flex items-center gap-2 text-xs font-mono text-[#E5D6BC]/70">
            <Link href="/" className="hover:text-[#E5D6BC] flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-[#E5D6BC] font-semibold">ROBOTAXI</span>
          </div>

          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-4 pb-4 border-b border-[#E5D6BC]/15">
            <div className="space-y-1.5 max-w-3xl">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-[#E5D6BC]/10 border border-[#E5D6BC]/25 text-[#E5D6BC] text-[10px] font-mono tracking-wider uppercase">
                <span>{lang === "tr" ? "REFERANS OTONOMİ MİMARİSİ (RAD) // E-GMP" : "REFERENCE AUTONOMY ARCHITECTURE // E-GMP"}</span>
              </div>
              
              <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug">
                Hyundai Ioniq 5 (E-GMP){" "}
                <span className="text-[#E5D6BC] font-normal block sm:inline">
                  {lang === "tr" ? "— Seviye 4 Donanım ve Sensör Mimarisi" : "— Level 4 Hardware & Sensor Blueprint"}
                </span>
              </h1>
              
              <p className="text-[#d6cebf] text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
                {lang === "tr"
                  ? "Kurumsal filolar ve OEM entegrasyonu için 128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsüyle yapılandırılmış; 16.400+ satır özgün deterministik otonomi şartnamesi."
                  : "Configured with 128-channel 3D LiDAR, 4x GMSL2 HDR cameras, 77GHz radar, and 100 Hz CAN-FD drive-by-wire across 16,400+ lines of sovereign autonomy software."}
              </p>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <Link
                href="/iletisim/"
                className="px-4 py-2 rounded-lg bg-[#E5D6BC] text-[#14120c] hover:bg-white font-bold text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-1.5 shadow-md"
              >
                <span>{lang === "tr" ? "Şartname ve Talep" : "Enterprise Spec"}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. Integrated 4-Metric Architectural Bar (KUTUSUZ & KOMPAKT) */}
        <div className="grid grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-[#E5D6BC]/15 py-3.5 border-y border-[#E5D6BC]/20 font-mono">
          <div className="py-1 px-3 first:pl-0 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "YAZILIM ÇEKİRDEĞİ" : "AUTONOMY STACK"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">16.400+</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              {lang === "tr" ? "Satır C++20 / ROS 2" : "Lines of Code (C++20)"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "OTOMATİK TEST" : "AUTOMATED TESTS"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">1.307 / 1.307</div>
            <span className="text-[10px] text-emerald-400 block font-sans font-medium">
              {lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "MERKEZİ HESAPLAMA" : "COMPUTE POWER"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">275 TOPS</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              Jetson AGX Orin 64GB
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "LİDAR MENZİLİ" : "LIDAR RANGE"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">240 Metre</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              128 Kanal Ouster OS2
            </span>
          </div>
        </div>

        {/* 3. Interactive Sensor Fusion Blueprint Visualizer */}
        <div className="space-y-3 pt-2">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-[#E5D6BC]/15">
            <div>
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "DONANIM VE SENSÖR YERLEŞİM ŞARTNAMESİ" : "HARDWARE & SENSOR PLACEMENT BLUEPRINT"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "360° Sensör Kapsama ve CAN-FD Veri Yolu Mimarisi" : "360° Sensor Coverage & CAN-FD Topology"}
              </h2>
            </div>
            
            {/* Filter Pills */}
            <div className="flex flex-wrap items-center gap-1.5">
              {[
                { id: "all" as const, label: lang === "tr" ? "TÜMÜ (360°)" : "ALL (360°)" },
                { id: "lidar" as const, label: "OUSTER 128K LİDAR" },
                { id: "radar" as const, label: "77GHz RADAR" },
                { id: "camera" as const, label: "4x HDR KAMERA" },
                { id: "compute" as const, label: "ORIN & CAN-FD" }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveSensor(tab.id)}
                  className={`px-2.5 py-1 rounded text-[11px] font-mono transition-all duration-200 cursor-pointer ${
                    activeSensor === tab.id
                      ? "bg-[#E5D6BC] text-[#14120c] font-bold shadow-md"
                      : "bg-[#251f18] hover:bg-[#2e261e] text-[#E5D6BC]/80 hover:text-white border border-[#E5D6BC]/20"
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          </div>

          {/* Technical Vector Canvas (360° FOV Blueprint) */}
          <div className="relative rounded-xl overflow-hidden border border-[#E5D6BC]/25 bg-[#18140e] aspect-[16/9] sm:aspect-[21/9] max-h-[480px] flex items-center justify-center p-4 shadow-inner">
            
            {/* Coordinate Grid Header */}
            <div className="absolute top-3 left-3 right-3 flex items-center justify-between text-[10px] font-mono text-slate-400 pointer-events-none">
              <span className="px-2 py-0.5 rounded bg-black/60 border border-[#E5D6BC]/15">
                TOP-DOWN // 360° SENSÖR KAPSAMA GEOMETRİSİ
              </span>
              <span className="text-slate-400">
                ÖLÇEK: 1:100 (240m ÇAP) • E-GMP ŞASİ
              </span>
            </div>

            {/* High-Precision SVG Sensor Topology */}
            <svg viewBox="0 0 600 340" className="w-full h-full" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="archGridPage" width="30" height="30" patternUnits="userSpaceOnUse">
                  <path d="M 30 0 L 0 0 0 30" fill="none" stroke="rgba(255,255,255,0.03)" strokeWidth="1" />
                </pattern>
                <radialGradient id="lidarGlowPage" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.25" />
                  <stop offset="70%" stopColor="#38bdf8" stopOpacity="0.06" />
                  <stop offset="100%" stopColor="#38bdf8" stopOpacity="0" />
                </radialGradient>
                <linearGradient id="radarBeamPage" x1="0%" y1="100%" x2="0%" y2="0%">
                  <stop offset="0%" stopColor="#34d399" stopOpacity="0.35" />
                  <stop offset="100%" stopColor="#34d399" stopOpacity="0.02" />
                </linearGradient>
              </defs>

              <rect width="600" height="340" fill="url(#archGridPage)" />

              {/* Range Rings (50m, 100m, 180m, 240m) */}
              <circle cx="300" cy="170" r="45" stroke="rgba(229,214,188,0.15)" strokeDasharray="3 3" />
              <circle cx="300" cy="170" r="90" stroke="rgba(229,214,188,0.15)" strokeDasharray="3 3" />
              <circle cx="300" cy="170" r="140" stroke="rgba(229,214,188,0.12)" strokeDasharray="3 3" />

              {/* Range Labels */}
              <text x="304" y="122" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">50m</text>
              <text x="304" y="77" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">100m</text>
              <text x="304" y="28" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">200m (LiDAR)</text>

              {/* --- 1. LiDAR 360° Zone --- */}
              {(activeSensor === "all" || activeSensor === "lidar") && (
                <g className="transition-opacity duration-300">
                  <circle cx="300" cy="170" r="145" fill="url(#lidarGlowPage)" />
                  <circle cx="300" cy="170" r="145" stroke="#38bdf8" strokeWidth="1" strokeDasharray="4 4" opacity="0.4" />
                  <line x1="300" y1="170" x2="300" y2="25" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.4" />
                  <line x1="300" y1="170" x2="445" y2="170" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                  <line x1="300" y1="170" x2="155" y2="170" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                </g>
              )}

              {/* --- 2. Radar Forward Long-Range Cone (250m, 77GHz) --- */}
              {(activeSensor === "all" || activeSensor === "radar") && (
                <g className="transition-opacity duration-300">
                  <path
                    d="M 300 135 L 210 15 A 180 180 0 0 1 390 15 Z"
                    fill="url(#radarBeamPage)"
                    stroke="#34d399"
                    strokeWidth="1.2"
                    opacity="0.8"
                  />
                  <path d="M 240 55 A 140 140 0 0 1 360 55" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                  <path d="M 265 95 A 90 90 0 0 1 335 95" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                  <text x="300" y="22" textAnchor="middle" fill="#34d399" fontSize="9" fontFamily="monospace" fontWeight="bold">
                    77GHz DOPPLER RADAR // 250m MENZİL
                  </text>
                </g>
              )}

              {/* --- 3. 4x Surround HDR Cameras (120° FOV Each) --- */}
              {(activeSensor === "all" || activeSensor === "camera") && (
                <g className="transition-opacity duration-300" opacity="0.75">
                  <polygon points="300,140 200,45 400,45" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="280,170 170,95 170,245" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="320,170 430,95 430,245" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="300,205 210,295 390,295" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                </g>
              )}

              {/* --- 4. Vehicle Chassis Silhouette (Hyundai E-GMP 3.000 mm Wheelbase) --- */}
              <g>
                <rect x="281" y="132" width="38" height="78" rx="8" fill="#0f172a" stroke="#475569" strokeWidth="1.5" />
                <rect x="284" y="148" width="32" height="46" rx="4" fill="#1e293b" stroke="#334155" strokeWidth="1" />
                
                <rect x="277" y="140" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="319" y="140" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="277" y="190" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="319" y="190" width="4" height="12" rx="1.5" fill="#64748b" />

                <line x1="272" y1="146" x2="272" y2="196" stroke="rgba(148,163,184,0.4)" strokeWidth="0.8" />
                <text x="268" y="173" textAnchor="end" fill="rgba(148,163,184,0.7)" fontSize="7" fontFamily="monospace">3.000mm</text>

                {/* Bumper Pods */}
                <circle cx="286" cy="134" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />
                <circle cx="314" cy="134" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />

                {/* Roof LiDAR */}
                <circle cx="300" cy="168" r="5" fill="#0284c7" stroke="#38bdf8" strokeWidth="1.5" />
                <circle cx="300" cy="168" r="2" fill="#ffffff" />

                {/* Sub-Trunk Compute Hub */}
                <rect x="288" y="196" width="24" height="10" rx="2" fill="#047857" stroke="#34d399" strokeWidth="1" />
                <text x="300" y="203" textAnchor="middle" fill="#ffffff" fontSize="6" fontFamily="monospace" fontWeight="bold">ORIN</text>

                {/* CAN-FD Bus Backbone Line */}
                {(activeSensor === "all" || activeSensor === "compute") && (
                  <line x1="300" y1="136" x2="300" y2="196" stroke="#10b981" strokeWidth="1.5" strokeDasharray="3 2" />
                )}
              </g>

              {/* Callout Labels with Connecting Hairlines */}
              <g fontFamily="monospace" fontSize="8" fill="#94a3b8">
                <path d="M 305 168 L 380 145 L 440 145" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                <text x="445" y="148" fill="#38bdf8" fontWeight="bold">OUSTER OS2-128 (TAVAN)</text>

                <path d="M 283 134 L 210 120 L 150 120" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                <text x="145" y="123" textAnchor="end" fill="#38bdf8">2x LIVOX MID-360 (TAMPON)</text>

                <path d="M 312 201 L 380 215 L 440 215" stroke="rgba(52,211,153,0.5)" strokeWidth="0.8" />
                <text x="445" y="218" fill="#34d399" fontWeight="bold">JETSON ORIN + 100Hz CAN-FD</text>

                <path d="M 277 170 L 210 190 L 150 190" stroke="rgba(245,158,11,0.5)" strokeWidth="0.8" />
                <text x="145" y="193" textAnchor="end" fill="#f59e0b">4x SONY IMX390 GMSL2 HDR</text>
              </g>
            </svg>

            {/* Bottom Right Homologation Tag */}
            <div className="absolute bottom-3 right-3 flex items-center gap-2 text-[9px] font-mono text-slate-400">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>ISO 26262 ASIL-D & UN ECE R157 UYUMLU</span>
            </div>
          </div>

          {/* Dynamic Specification Bar of Selected Sensor */}
          <div className="p-4 rounded-xl bg-[#251f18] border border-[#E5D6BC]/25 space-y-1 shadow-md">
            <div className="flex items-center justify-between text-[10px] font-mono">
              <span className="text-[#E5D6BC] font-semibold">{current.tag}</span>
              <span className="text-[#E5D6BC]/75">{current.metric}</span>
            </div>
            <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
              {current.title}
            </div>
            <p className="text-[11px] text-[#d6cebf] leading-relaxed font-sans">
              {current.desc}
            </p>
          </div>
        </div>

        {/* 4. Turnkey Sensor & Hardware Matrix (KUTUSUZ EDİTORYAL MİMARİ) */}
        <div className="space-y-4 pt-4 border-t border-[#E5D6BC]/15">
          <div className="pb-2 border-b border-[#E5D6BC]/15">
            <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
              // {lang === "tr" ? "DONANIM VE SENSÖR MİMARİSİ" : "HARDWARE & SENSOR FUSION"}
            </div>
            <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
              {lang === "tr" ? "27 Parçalık Seviye 4 Donanım Seti" : "27-Item Level-4 Turnkey Sensor Suite"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 divide-y divide-white/10">
            {specs.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div key={idx} className="py-3 flex items-start gap-3">
                  <div className="w-7 h-7 rounded bg-[#251f18] border border-[#E5D6BC]/25 flex items-center justify-center text-[#E5D6BC] shrink-0 mt-0.5">
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div className="space-y-0.5 min-w-0">
                    <div className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
                      {item.title}
                    </div>
                    <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
                      {item.val}
                    </div>
                    <div className="text-[11px] text-[#d6cebf]/80 font-sans">
                      {item.sub}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. Architecture & Safety Protocols (KUTUSUZ EDİTORYAL ÇİFT SÜTUN) */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 pt-6 border-t border-[#E5D6BC]/15">
          
          {/* E-GMP & CAN-FD Integration */}
          <div className="space-y-3">
            <div className="border-b border-[#E5D6BC]/15 pb-2">
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "E-GMP CAN-FD ENTEGRASYONU" : "E-GMP CAN-FD ARCHITECTURE"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "Sıfır Delme & Tak-Çalıştır Şasi Uyumu" : "Zero-Drill & Plug-and-Play Integration"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-[#d6cebf] divide-y divide-[#E5D6BC]/10">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Dikiz Aynası ADAS Y-Harness:" : "Rearview ADAS Y-Harness:"}</b>{" "}
                  {lang === "tr"
                    ? "OBD-II gateway kısıtlamasına takılmadan şasi CAN-FD hattına 100 Hz direksiyon (LKAS11) ve 50 Hz fren/gaz (SCC_FD) sinyali iletilir."
                    : "Transmits 100 Hz steering (LKAS11) and 50 Hz brake/accel (SCC_FD) directly into chassis CAN-FD without gateway latency."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "57 Litrelik Sub-Trunk Hesaplama Havuzu:" : "57-Liter Sub-Trunk Compute Hub:"}</b>{" "}
                  {lang === "tr"
                    ? "Jetson Orin, sigorta panosu, 5G router ve DC-DC regülatör bagaj altı havuzuna yerleştirilir; iç mekan düzeni korunur."
                    : "Jetson Orin, fuse box, 5G router, and DC-DC regulator fit discreetly in the sub-trunk compartment."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "IP68 No-Drill Tavan Geçişi:" : "IP68 Zero-Penetration Roof Routing:"}</b>{" "}
                  {lang === "tr"
                    ? "Araç kaportası delinmez; kablo demeti arka spoyler altındaki fabrikasyon kauçuk körükten sub-trunk'a iner."
                    : "Zero sheet-metal drilling; cables route through OEM tailgate rubber boots sealed with IP68 junction hardware."}
                </span>
              </li>
            </ul>
          </div>

          {/* Safety & Human Takeover */}
          <div className="space-y-3">
            <div className="border-b border-[#E5D6BC]/15 pb-2">
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "GÜVENLİK VE DEVİR PROTOKOLLERİ" : "SAFETY & TAKEOVER PROTOCOLS"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "5ms Sürücü Devralma ve Güvenli Durma" : "5ms Driver Override & Fail-Safe"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-[#d6cebf] divide-y divide-[#E5D6BC]/10">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Anlık Sürücü Müdahalesi (5ms):" : "Instant Human Takeover (5ms):"}</b>{" "}
                  {lang === "tr"
                    ? "Direksiyona tork uygulandığında veya fren pedalına basıldığında otonomi 5 milisaniyede kontrolü sürücüye bırakır (ISO 26262 ASIL-D)."
                    : "Manual steering torque or brake depression instantly disengages autonomy within 5ms under ISO 26262 ASIL-D."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "200ms Watchdog & MRM Fail-Safe:" : "200ms Watchdog & MRM Fail-Safe:"}</b>{" "}
                  {lang === "tr"
                    ? "Herhangi bir donanım gecikmesinde flaşörler açılır, araç şeridinde kontrollü durur ve 4TB SSD kara kutu kaydı alır."
                    : "On sensor stall, hazard lights engage, the vehicle safely stops within lane, and 4TB NVMe SSD logs telemetry."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "5G GPS Coğrafi Çit (Geofence):" : "5G GPS Geofencing & Remote Kill:"}</b>{" "}
                  {lang === "tr"
                    ? "Tanımlı Operasyonel Tasarım Alanı (ODD) ve coğrafi koridor dışına çıkış halinde motor kilitlenir; 7/24 teleoperasyon C2 ile yönetilir."
                    : "Vehicle locks drive if exiting authorized Operational Design Domain (ODD) corridor; monitored 24/7 via tactical desktop C2."}
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* 6. Authentic Enterprise Integration & Validation Model */}
        <div className="space-y-3 pt-6 border-t border-[#E5D6BC]/15">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-[#E5D6BC]/15">
            <div>
              <div className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
                // {lang === "tr" ? "KURUMSAL ENTEGRASYON VE DOĞRULAMA MODELİ" : "ENTERPRISE INTEGRATION & VALIDATION PROTOCOL"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "4 Kademeli Otonomi Entegrasyon ve Dağıtım Modeli" : "4-Stage Autonomous Deployment Model"}
              </h2>
            </div>
            <div className="text-[10px] font-mono text-emerald-400 font-semibold">
              ISO 26262 ASIL-D & UN ECE R157 UYUMLU
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-white/10 py-3 border-y border-[#E5D6BC]/15 font-mono">
            <div className="py-2 px-3 first:pl-0 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 01 // YAZILIM ÇEKİRDEĞİ</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">SIL & 3D Dijital İkiz</div>
              <div className="text-[11px] text-[#d6cebf]/90 leading-relaxed font-sans">
                Webots simülasyonu, 1.307 birim test, NDT SLAM haritalama, Pure Pursuit rota takibi.
              </div>
              <div className="text-[10px] text-emerald-400 font-semibold pt-0.5">%100 Doğrulandı</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 02 // CAN-FD HIL TESTİ</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">Aktüatör Bench Doğrulama</div>
              <div className="text-[11px] text-[#d6cebf]/90 leading-relaxed font-sans">
                100 Hz LKAS11 direksiyon torku ve 50 Hz SCC_FD fren/gaz donanımsal bench testi.
              </div>
              <div className="text-[10px] text-slate-400 font-medium pt-0.5">5ms Emniyet Kesmesi</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 03 // SENSÖR FÜZYONU</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">Zamansal Kalibrasyon</div>
              <div className="text-[11px] text-[#d6cebf]/90 leading-relaxed font-sans">
                128 kanal LiDAR + 77GHz Radar + Sony HDR kamera uzaysal matris ve FSYNC kalibrasyonu.
              </div>
              <div className="text-[10px] text-slate-400 font-medium pt-0.5">Santimetre Hassasiyet</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 04 // FİLO ENTEGRASYONU</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">ODD Saha Validasyonu</div>
              <div className="text-[11px] text-[#d6cebf]/90 leading-relaxed font-sans">
                Kurumsal filo operatörleri ile tanımlı operasyonel koridorda ortak pilot validasyon.
              </div>
              <div className="text-[10px] text-emerald-400 font-semibold pt-0.5">Filo İş Birliği Modeli</div>
            </div>
          </div>
        </div>

        {/* 7. Institutional NDA Technical Cooperation Bar */}
        <div className="py-6 px-6 sm:px-8 rounded-2xl bg-gradient-to-r from-[#282017] via-[#352a1e] to-[#282017] border border-[#E5D6BC]/30 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="space-y-1 text-center md:text-left max-w-2xl">
            <div className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
              // {lang === "tr" ? "KURUMSAL TEKNİK İŞBİRLİĞİ" : "INSTITUTIONAL TECHNICAL COOPERATION"}
            </div>
            <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
              {lang === "tr" ? "Mühendislik Şartnamesi ve Entegrasyon Protokolü" : "Engineering Specification & Integration Protocol"}
            </h3>
            <p className="text-[#d6cebf] text-xs leading-relaxed">
              {lang === "tr"
                ? "Donanım mimarisi, sensör yerleşim geometrisi, CAN-FD sinyal protokolleri ve platform güvenlik standartları kurumsal gizlilik sözleşmesi (NDA) kapsamında OEM ve savunma sanayii ortaklarıyla paylaşılmaktadır."
                : "Detailed hardware schematics, sensor mounting geometry, CAN-FD bus protocols, and functional safety architecture are available to qualified OEM and defense partners under institutional NDA."}
            </p>
          </div>

          <Link
            href="/iletisim"
            className="w-full sm:w-auto px-5 py-2.5 rounded-lg bg-[#E5D6BC] text-[#14120c] hover:bg-white font-bold text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-1.5 shrink-0 shadow-lg"
          >
            <Lock className="w-3.5 h-3.5" />
            <span>{lang === "tr" ? "NDA İLE TALEP ET" : "REQUEST VIA NDA"}</span>
          </Link>
        </div>

      </div>

      <Footer />
    </main>
  );
}
