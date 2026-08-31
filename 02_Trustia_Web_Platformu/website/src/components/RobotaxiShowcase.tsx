"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Cpu,
  Eye,
  Layers,
  Radio,
  Download,
  ArrowRight,
  ChevronRight
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiShowcase() {
  const { lang } = useLanguage();
  const [selectedPhoto, setSelectedPhoto] = useState(0);

  const photos = [
    {
      src: "/robotaxi/ioniq5_foto_1.png",
      title: lang === "tr" ? "Ön Çeyrek Dış Görünüm" : "Front 3/4 Exterior",
      desc: lang === "tr" ? "Hyundai Ioniq 5 E-GMP Otonomi Platformu" : "Hyundai Ioniq 5 E-GMP Platform",
      tag: "DIŞ GÖRÜNÜM"
    },
    {
      src: "/robotaxi/ioniq5_foto_2.png",
      title: lang === "tr" ? "Ön Tampon & Sensör Podu" : "Front Bumper & Sensor Pod",
      desc: lang === "tr" ? "Livox Mid-360 LiDAR ve 77GHz Radar Entegrasyonu" : "Livox Mid-360 LiDAR & Radar",
      tag: "SENSÖR PODU"
    },
    {
      src: "/robotaxi/ioniq5_foto_3.png",
      title: lang === "tr" ? "Yan Profil & Tavan Barı" : "Side Profile & Roof Rack",
      desc: lang === "tr" ? "Tavan Barı ve 128 Kanal Ouster OS2 LiDAR Montaj Hattı" : "Roof Bar & Ouster OS2 LiDAR",
      tag: "TAVAN HATTI"
    },
    {
      src: "/robotaxi/ioniq5_foto_4.png",
      title: lang === "tr" ? "Arka Çeyrek Görünüm" : "Rear 3/4 Exterior",
      desc: lang === "tr" ? "IP68 Yalıtımlı Kablo Geçiş Hattı ve Arka Spoyler" : "IP68 Cable Entry",
      tag: "KABLO YALITIMI"
    },
    {
      src: "/robotaxi/ioniq5_foto_5.png",
      title: lang === "tr" ? "Arka Düz Görünüm" : "Rear Straight View",
      desc: lang === "tr" ? "Geri Görüş HDR Kamera ve Ultrasonik Sensör Dizilimi" : "Rear HDR Camera Suite",
      tag: "ARKA GÖRÜŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_6.png",
      title: lang === "tr" ? "Ön Kokpit & Telemetri Konsolu" : "Cockpit & Telemetry Console",
      desc: lang === "tr" ? "10.1\" Taktik Dokunmatik Ekran ve Acil Durum Butonu" : "10.1\" Touch Console & E-Stop",
      tag: "KOKPİT C2"
    },
    {
      src: "/robotaxi/ioniq5_foto_7.png",
      title: lang === "tr" ? "Arka Yolcu Alanı" : "Rear Cabin",
      desc: lang === "tr" ? "E-GMP Düz Zemin ve Yolcu Konfor Odaklı İç Mimari" : "E-GMP Flat Floor Comfort",
      tag: "YOLCU KABİNİ"
    }
  ];

  const specs = [
    {
      icon: Eye,
      title: "Ouster OS2-128 LiDAR",
      desc: lang === "tr" ? "128 Kanal, 240m Menzil, 2.62M Nokta/sn 3D SLAM" : "128 Channels, 240m Range, Primary 3D SLAM"
    },
    {
      icon: Layers,
      title: "2x Livox Mid-360 LiDAR",
      desc: lang === "tr" ? "Ön Tampon 360°x59° Kör Noktasız Yaya Taraması" : "Front Bumper 360°x59° Blindspot Coverage"
    },
    {
      icon: Radio,
      title: "4x Sony IMX390 GMSL2 HDR",
      desc: lang === "tr" ? "120 dB Dinamik Aralık, 360° Çevre Görüş" : "120 dB Dynamic Range, 360° Vision"
    },
    {
      icon: Cpu,
      title: "NVIDIA Jetson AGX Orin 64GB",
      desc: lang === "tr" ? "275 TOPS AI Hesaplama, 4TB Samsung NVMe Kayıt" : "275 TOPS AI Compute, 4TB NVMe SSD"
    }
  ];

  return (
    <section id="robotaxi" className="relative w-full py-8 sm:py-14 px-3 sm:px-8 bg-[#090b0e] border-b border-white/10 relative z-20">
      <div className="max-w-6xl mx-auto space-y-6 sm:space-y-8">
        
        {/* Header: Clean & 100% Mobile Optimized */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 pb-4 border-b border-white/10">
          <div className="space-y-1.5 max-w-2xl">
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px] font-mono font-medium uppercase tracking-wider">
              <span>{lang === "tr" ? "SEVİYE 4 OTONOM SÜRÜŞ PLATFORMU" : "LEVEL 4 AUTONOMOUS PLATFORM"}</span>
            </div>
            
            <h2 className="text-lg sm:text-2xl font-bold text-white tracking-tight leading-snug">
              Hyundai Ioniq 5 (E-GMP){" "}
              <span className="text-slate-400 font-normal block sm:inline">
                {lang === "tr" ? "— Seviye-4 Otonom Test Filosu" : "— Level-4 Autonomous Fleet"}
              </span>
            </h2>

            <p className="text-slate-400 text-xs leading-relaxed max-w-xl">
              {lang === "tr"
                ? "128 Kanallı LiDAR, 4x HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış 16.000 satır özgün deterministik otonomi yazılımı."
                : "Equipped with 128-channel LiDAR, 4x HDR vision, 77GHz radar, and 100 Hz CAN-FD drive-by-wire over 16,000 lines of sovereign code."}
            </p>
          </div>

          {/* Action Buttons: Responsive full width on mobile, inline on desktop */}
          <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-2 sm:gap-2.5 shrink-0">
            <Link
              href="/robotaxi/"
              className="px-3.5 py-2 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-1.5 shadow-sm"
            >
              <span>{lang === "tr" ? "TEKNİK DOKÜMAN" : "TECHNICAL SPEC"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>

            <a
              href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
              download
              className="px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 hover:bg-slate-800 font-medium text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-1.5"
            >
              <Download className="w-3.5 h-3.5 text-slate-400" />
              <span>PDF (5 SAYFA)</span>
            </a>
          </div>
        </div>

        {/* 4 Responsive Metric Cards */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-4">
          <div className="p-3 sm:p-4 rounded-xl bg-[#0f131a] border border-slate-800 space-y-0.5">
            <div className="text-[9px] sm:text-[10px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "YAZILIM ÇEKİRDEĞİ" : "AUTONOMY CORE"}
            </div>
            <div className="text-lg sm:text-xl font-bold text-white">16.000+</div>
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">
              {lang === "tr" ? "Satır C++ / Python" : "Lines of Code"}
            </div>
          </div>

          <div className="p-3 sm:p-4 rounded-xl bg-[#0f131a] border border-slate-800 space-y-0.5">
            <div className="text-[9px] sm:text-[10px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "OTOMATİK TEST" : "AUTOMATED TESTS"}
            </div>
            <div className="text-lg sm:text-xl font-bold text-white">1.301 / 1.301</div>
            <div className="text-[10px] sm:text-[11px] text-emerald-400 font-medium truncate">
              {lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate"}
            </div>
          </div>

          <div className="p-3 sm:p-4 rounded-xl bg-[#0f131a] border border-slate-800 space-y-0.5">
            <div className="text-[9px] sm:text-[10px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "HESAPLAMA GÜCÜ" : "AI COMPUTE"}
            </div>
            <div className="text-lg sm:text-xl font-bold text-white">275 TOPS</div>
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">Jetson AGX Orin 64GB</div>
          </div>

          <div className="p-3 sm:p-4 rounded-xl bg-[#0f131a] border border-slate-800 space-y-0.5">
            <div className="text-[9px] sm:text-[10px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "LİDAR MENZİLİ" : "LIDAR RANGE"}
            </div>
            <div className="text-lg sm:text-xl font-bold text-white">240 Metre</div>
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">128 Kanal 3D SLAM</div>
          </div>
        </div>

        {/* Gallery + Engineering Specs Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 items-center">
          
          {/* Media Frame (7 Cols) */}
          <div className="lg:col-span-7 space-y-2.5">
            <div className="relative rounded-xl overflow-hidden border border-slate-800 bg-[#0c1017] aspect-[16/10] max-h-[360px] group">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={photos[selectedPhoto].src}
                alt={photos[selectedPhoto].title}
                className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-[1.01]"
              />
              
              <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent pointer-events-none" />

              <div className="absolute bottom-2.5 left-2.5 right-2.5 sm:bottom-3 sm:left-3 sm:right-3 flex items-end justify-between">
                <div className="space-y-0.5">
                  <span className="px-1.5 py-0.5 rounded bg-slate-900/90 border border-slate-700 text-slate-300 font-mono text-[9px] uppercase tracking-wider inline-block">
                    {photos[selectedPhoto].tag}
                  </span>
                  <h4 className="text-xs sm:text-base font-bold text-white leading-tight">
                    {photos[selectedPhoto].title}
                  </h4>
                  <p className="text-slate-400 text-[10px] sm:text-[11px] max-w-sm line-clamp-1 sm:line-clamp-none">
                    {photos[selectedPhoto].desc}
                  </p>
                </div>
                <div className="text-[10px] sm:text-[11px] font-mono text-slate-400 shrink-0 ml-2">
                  {selectedPhoto + 1} / {photos.length}
                </div>
              </div>
            </div>

            {/* Mobile Scrollable / Desktop Grid Thumbnails */}
            <div className="flex gap-2 overflow-x-auto pb-1 pt-0.5 no-scrollbar scrollbar-none sm:grid sm:grid-cols-7 sm:gap-1.5">
              {photos.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedPhoto(idx)}
                  className={`relative rounded-md overflow-hidden aspect-[4/3] w-14 sm:w-auto shrink-0 border transition-all duration-200 cursor-pointer ${
                    selectedPhoto === idx
                      ? "border-white ring-1 ring-white/60"
                      : "border-slate-800 opacity-60 hover:opacity-100"
                  }`}
                >
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={p.src} alt={p.title} className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
          </div>

          {/* Technical Specifications (5 Cols) */}
          <div className="lg:col-span-5 space-y-2">
            <div className="text-[10px] sm:text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
              {lang === "tr" ? "TEMEL DONANIM BİLEŞENLERİ" : "CORE HARDWARE SUITE"}
            </div>

            <div className="space-y-1.5 sm:space-y-2">
              {specs.map((item, i) => {
                const Icon = item.icon;
                return (
                  <div
                    key={i}
                    className="p-2 sm:p-2.5 rounded-lg bg-[#0f131a] border border-slate-800 flex items-start gap-2.5 hover:border-slate-700 transition-colors"
                  >
                    <div className="w-6 h-6 sm:w-7 sm:h-7 rounded-md bg-slate-800/60 border border-slate-700 flex items-center justify-center text-slate-300 shrink-0 mt-0.5">
                      <Icon className="w-3.5 h-3.5" />
                    </div>
                    <div className="space-y-0.5 min-w-0">
                      <div className="text-xs font-semibold text-white truncate">
                        {item.title}
                      </div>
                      <div className="text-[10px] sm:text-[11px] text-slate-400 leading-tight">
                        {item.desc}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Bottom Info Pill */}
            <div className="p-2 sm:p-2.5 rounded-lg bg-slate-900/90 border border-slate-800 flex items-center justify-between gap-2 text-[10px] sm:text-[11px] text-slate-300">
              <div className="truncate">
                <span className="font-semibold text-white">CAN-FD 100 Hz:</span>{" "}
                {lang === "tr" ? "LKAS11 & SCC_FD (5ms Devralma)" : "100 Hz LKAS & SCC (5ms)"}
              </div>
              <Link
                href="/robotaxi/"
                className="shrink-0 font-medium text-white hover:underline flex items-center gap-0.5 text-[10px] sm:text-[11px]"
              >
                <span>{lang === "tr" ? "Detay" : "More"}</span>
                <ChevronRight className="w-3 h-3" />
              </Link>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
