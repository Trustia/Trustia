"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Car,
  Cpu,
  Eye,
  Layers,
  Radio,
  Download,
  CheckCircle2,
  ChevronRight,
  Gauge,
  Lock,
  Zap,
  ArrowRight,
  ShieldCheck
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiShowcase() {
  const { lang } = useLanguage();
  const [selectedPhoto, setSelectedPhoto] = useState(0);

  const photos = [
    {
      src: "/robotaxi/ioniq5_foto_1.png",
      title: lang === "tr" ? "Ön 3/4 Dış Görünüm" : "Front 3/4 Exterior",
      desc: lang === "tr" ? "Hyundai Ioniq 5 E-GMP Seviye 4 Otonom Test Aracı" : "Hyundai Ioniq 5 E-GMP Level 4 Autonomous Test Platform",
      tag: "GENEL BAKIŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_2.png",
      title: lang === "tr" ? "Ön Tampon & LiDAR Podu" : "Front Bumper & LiDAR Pod",
      desc: lang === "tr" ? "Livox Mid-360 LiDAR & 77GHz Radar Kör Noktasız Tarama" : "Livox Mid-360 LiDAR & 77GHz Radar Blindspot Coverage",
      tag: "LİDAR & RADAR"
    },
    {
      src: "/robotaxi/ioniq5_foto_3.png",
      title: lang === "tr" ? "Yan Profil & Tavan Barı" : "Side Profile & Roof Bar",
      desc: lang === "tr" ? "Drs Tuning Ace-4 Tavan Barı & Ouster OS2-128 LiDAR Hizalaması" : "Ace-4 Roof Bar & Ouster OS2-128 LiDAR Alignment",
      tag: "TAVAN MİMARİSİ"
    },
    {
      src: "/robotaxi/ioniq5_foto_4.png",
      title: lang === "tr" ? "Arka Çapraz Görünüm" : "Rear 3/4 Exterior",
      desc: lang === "tr" ? "Arka Spoyler Altı IP68 Su Geçirmez Kablo Giriş Körüğü" : "Rear Spoiler IP68 Tailgate Cable Entry",
      tag: "IP68 YALITIM"
    },
    {
      src: "/robotaxi/ioniq5_foto_5.png",
      title: lang === "tr" ? "Arka Düz Görünüm" : "Rear Straight View",
      desc: lang === "tr" ? "Geri Görüş HDR Kamerası & Ultrasonik Park Dizilimi" : "Rear HDR Vision & Ultrasonic Array",
      tag: "360° GÖRÜŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_6.png",
      title: lang === "tr" ? "Ön Kokpit & Taktik C2" : "Front Cockpit & C2 Map",
      desc: lang === "tr" ? "10.1\" IPS Dokunmatik Harita ve Schneider E-Stop Butonu" : "10.1\" Touch C2 Map & Schneider E-Stop",
      tag: "KOKPİT & C2"
    },
    {
      src: "/robotaxi/ioniq5_foto_7.png",
      title: lang === "tr" ? "VIP Arka Yolcu Alanı" : "VIP Passenger Cabin",
      desc: lang === "tr" ? "E-GMP Düz Zemin ve Otonom Yolcu Konforu" : "E-GMP Flat Floor & Autonomous Ride Comfort",
      tag: "YOLCU KONFORU"
    }
  ];

  const highlights = [
    {
      icon: Eye,
      title: lang === "tr" ? "Ouster OS2-128 LiDAR" : "Ouster OS2-128 LiDAR",
      sub: lang === "tr" ? "128 Kanal • 240m Menzil • 2.62M Nokta/sn" : "128ch • 240m Range • 2.62M pts/s"
    },
    {
      icon: Layers,
      title: lang === "tr" ? "2x Livox Mid-360" : "2x Livox Mid-360",
      sub: lang === "tr" ? "Ön Tampon 360°x59° Kör Noktasız Yaya Algılama" : "Front Bumper 360°x59° Blindspot Coverage"
    },
    {
      icon: Radio,
      title: lang === "tr" ? "4x Sony IMX390 HDR" : "4x Sony IMX390 HDR",
      sub: lang === "tr" ? "120 dB Dinamik Aralık • GMSL2 Sıfır Gecikme" : "120 dB Dynamic Range • GMSL2 Zero-Latency"
    },
    {
      icon: Cpu,
      title: lang === "tr" ? "NVIDIA Jetson AGX Orin" : "NVIDIA Jetson AGX Orin",
      sub: lang === "tr" ? "275 TOPS AI • 4TB Samsung 990 PRO NVMe SSD" : "275 TOPS AI • 4TB Samsung 990 PRO NVMe"
    }
  ];

  return (
    <section id="robotaxi" className="relative w-full py-16 sm:py-24 px-4 sm:px-8 bg-gradient-to-b from-[#07090d] via-[#0b0e14] to-[#07090d] border-y border-white/10 relative z-20 overflow-hidden">
      
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-5xl h-[400px] bg-radial from-[#0284C7]/15 via-transparent to-transparent pointer-events-none blur-3xl -z-10" />

      <div className="max-w-7xl mx-auto space-y-12 sm:space-y-16">
        
        {/* Section Header */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-white/10">
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-xs font-mono font-bold tracking-wider uppercase">
              <span className="w-2 h-2 rounded-full bg-[#C8FF00] animate-ping" />
              <span>{lang === "tr" ? "MİLLİ SEVİYE 4 ROBOTAKSİ PLATFORMU" : "SOVEREIGN LEVEL 4 ROBOTAXI PLATFORM"}</span>
            </div>
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-[1.15]">
              Hyundai Ioniq 5 (E-GMP) <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-[#C8FF00]">
                {lang === "tr" ? "Seviye-4 Otonom Test Filosu" : "Level-4 Autonomous Fleet Platform"}
              </span>
            </h2>
            <p className="text-slate-400 text-sm sm:text-base leading-relaxed">
              {lang === "tr"
                ? "128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış, 16.000 satır özgün deterministik yerli otonomi çekirdeği."
                : "Equipped with 128-channel 3D LiDAR, 4x GMSL2 HDR vision, 77GHz radar, and 100 Hz CAN-FD drive-by-wire over 16,000 lines of deterministic autonomy software."}
            </p>
          </div>

          {/* Quick Action Buttons */}
          <div className="flex flex-wrap items-center gap-3 shrink-0">
            <Link
              href="/robotaxi/"
              className="px-5 py-3 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.6)] transition-all cursor-pointer group"
            >
              <span>{lang === "tr" ? "TÜM ROBOTAKSİ MİMARİSİNİ AÇ" : "EXPLORE FULL ARCHITECTURE"}</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            
            <a
              href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
              download
              className="px-4 py-3 rounded-xl bg-white/5 border border-white/15 text-white font-mono font-bold text-xs tracking-wider uppercase hover:bg-white/10 transition-all flex items-center gap-2"
            >
              <Download className="w-4 h-4 text-slate-300" />
              <span>{lang === "tr" ? "PDF ŞARTNAME (5 SAYFA)" : "DOWNLOAD PDF"}</span>
            </a>
          </div>
        </div>

        {/* 4 Quick Stat Badges */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1">
            <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "KOD TABANI" : "CODEBASE"}</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">16.000+ Satır</div>
            <div className="text-[11px] text-[#C8FF00] font-mono font-medium">{lang === "tr" ? "%100 Özgün C++/Python" : "100% Sovereign"}</div>
          </div>
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1">
            <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "OTOMATİK TEST" : "TEST SUITE"}</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">1.301 / 1.301</div>
            <div className="text-[11px] text-emerald-400 font-mono font-medium">{lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate"}</div>
          </div>
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1">
            <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "AI İŞLEMCİ" : "AI COMPUTE"}</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">275 TOPS</div>
            <div className="text-[11px] text-sky-400 font-mono font-medium">Jetson AGX Orin 64GB</div>
          </div>
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1">
            <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "LİDAR MENZİLİ" : "LIDAR RANGE"}</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">240 Metre</div>
            <div className="text-[11px] text-purple-400 font-mono font-medium">128 Kanal 3D SLAM</div>
          </div>
        </div>

        {/* Interactive Photo Showcase + Metadata */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          {/* Main Photo (7 Cols) */}
          <div className="lg:col-span-7 space-y-4">
            <div className="relative rounded-3xl overflow-hidden border border-white/15 bg-[#0a0d13] shadow-2xl aspect-[16/10] group">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={photos[selectedPhoto].src}
                alt={photos[selectedPhoto].title}
                className="w-full h-full object-cover transition-all duration-500 group-hover:scale-[1.02]"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/10 to-transparent pointer-events-none" />

              <div className="absolute bottom-5 left-5 right-5 flex items-end justify-between">
                <div className="space-y-1">
                  <span className="px-2.5 py-0.5 rounded bg-[#C8FF00] text-black font-mono font-black text-[9px] uppercase tracking-wider inline-block">
                    {photos[selectedPhoto].tag}
                  </span>
                  <h4 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                    {photos[selectedPhoto].title}
                  </h4>
                  <p className="text-slate-300 text-xs max-w-md">
                    {photos[selectedPhoto].desc}
                  </p>
                </div>
                <div className="text-xs font-mono text-slate-400">
                  {selectedPhoto + 1} / {photos.length}
                </div>
              </div>
            </div>

            {/* Thumbnail Row */}
            <div className="grid grid-cols-7 gap-2">
              {photos.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedPhoto(idx)}
                  className={`relative rounded-xl overflow-hidden aspect-[4/3] border transition-all duration-300 cursor-pointer ${
                    selectedPhoto === idx
                      ? "border-[#C8FF00] ring-2 ring-[#C8FF00]/50 scale-[1.04]"
                      : "border-white/10 opacity-60 hover:opacity-100"
                  }`}
                >
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={p.src} alt={p.title} className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
          </div>

          {/* Key Engineering Highlights (5 Cols) */}
          <div className="lg:col-span-5 space-y-4">
            <div className="text-xs font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "TEMEL SENSÖR VE KONTROL DÖNGÜSÜ" : "PRIMARY SENSOR & CONTROL SUITE"}
            </div>

            <div className="space-y-3">
              {highlights.map((h, i) => {
                const Icon = h.icon;
                return (
                  <div
                    key={i}
                    className="p-4 rounded-2xl bg-[#0c1017] border border-white/10 hover:border-[#C8FF00]/40 transition-colors flex items-start gap-3.5 group"
                  >
                    <div className="w-9 h-9 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 group-hover:text-[#C8FF00] shrink-0 transition-colors">
                      <Icon className="w-4 h-4" />
                    </div>
                    <div>
                      <div className="text-sm font-bold text-white tracking-tight">
                        {h.title}
                      </div>
                      <div className="text-xs text-slate-400 font-light mt-0.5">
                        {h.sub}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Bottom Integration Note */}
            <div className="p-4 rounded-2xl bg-[#0284C7]/10 border border-[#0284C7]/30 flex items-center justify-between gap-3">
              <div className="text-xs text-slate-200">
                <span className="font-bold text-white">E-GMP CAN-FD 100 Hz:</span>{" "}
                {lang === "tr"
                  ? "Dikiz aynası Y-harness ile LKAS11 & SCC_FD enjeksiyonu, 5ms insan müdahalesi."
                  : "LKAS11 & SCC_FD injection via ADAS Y-harness, 5ms human takeover."}
              </div>
              <Link
                href="/robotaxi/"
                className="shrink-0 text-xs font-mono font-bold text-[#C8FF00] hover:underline flex items-center gap-1"
              >
                <span>{lang === "tr" ? "Detay" : "Details"}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
