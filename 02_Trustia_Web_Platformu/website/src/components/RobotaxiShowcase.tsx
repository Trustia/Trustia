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
  ChevronRight,
  Shield,
  Gauge,
  CheckCircle2
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiShowcase() {
  const { lang } = useLanguage();
  const [selectedPhoto, setSelectedPhoto] = useState(0);

  const photos = [
    {
      src: "/robotaxi/ioniq5_foto_1.png",
      title: lang === "tr" ? "Ön Çeyrek Dış Görünüm" : "Front 3/4 Exterior",
      desc: lang === "tr" ? "Hyundai Ioniq 5 E-GMP Otonomi Platformu" : "Hyundai Ioniq 5 E-GMP Autonomy Platform",
      tag: "DIŞ GÖRÜNÜM"
    },
    {
      src: "/robotaxi/ioniq5_foto_2.png",
      title: lang === "tr" ? "Ön Tampon & Sensör Podu" : "Front Bumper & Sensor Pod",
      desc: lang === "tr" ? "Livox Mid-360 LiDAR ve 77GHz Radar Entegrasyonu" : "Livox Mid-360 LiDAR & 77GHz Radar Integration",
      tag: "SENSÖR PODU"
    },
    {
      src: "/robotaxi/ioniq5_foto_3.png",
      title: lang === "tr" ? "Yan Profil & Tavan Barı" : "Side Profile & Roof Rack",
      desc: lang === "tr" ? "Tavan Barı ve 128 Kanal Ouster OS2 LiDAR Montaj Hattı" : "Roof Bar & 128-Channel Ouster OS2 LiDAR Alignment",
      tag: "TAVAN HATTI"
    },
    {
      src: "/robotaxi/ioniq5_foto_4.png",
      title: lang === "tr" ? "Arka Çeyrek Görünüm" : "Rear 3/4 Exterior",
      desc: lang === "tr" ? "IP68 Yalıtımlı Kablo Geçiş Hattı ve Arka Spoyler" : "IP68 Sealed Cable Entry & Rear Spoiler",
      tag: "KABLO YALITIMI"
    },
    {
      src: "/robotaxi/ioniq5_foto_5.png",
      title: lang === "tr" ? "Arka Düz Görünüm" : "Rear Straight View",
      desc: lang === "tr" ? "Geri Görüş HDR Kamera ve Ultrasonik Sensör Dizilimi" : "Rear HDR Camera & Ultrasonic Sensor Suite",
      tag: "ARKA GÖRÜŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_6.png",
      title: lang === "tr" ? "Ön Kokpit & Yönetim Ekranı" : "Cockpit & Telemetry Console",
      desc: lang === "tr" ? "10.1\" Taktik Dokunmatik Ekran ve Acil Durum E-Stop Butonu" : "10.1\" Touch Console & Emergency E-Stop Button",
      tag: "KOKPİT C2"
    },
    {
      src: "/robotaxi/ioniq5_foto_7.png",
      title: lang === "tr" ? "Arka Yolcu Alanı" : "Rear Cabin",
      desc: lang === "tr" ? "E-GMP Düz Zemin ve Yolcu Konfor Odaklı İç Mimari" : "E-GMP Flat Floor & Passenger Comfort Ergonomics",
      tag: "YOLCU KABİNİ"
    }
  ];

  const specs = [
    {
      icon: Eye,
      title: "Ouster OS2-128 LiDAR",
      desc: lang === "tr" ? "128 Kanal, 240m Menzil, 2.62M Nokta/sn Birincil 3D SLAM" : "128 Channels, 240m Range, Primary 3D SLAM"
    },
    {
      icon: Layers,
      title: "2x Livox Mid-360 LiDAR",
      desc: lang === "tr" ? "Ön Tampon 360°x59° Kör Noktasız Yaya ve Engel Taraması" : "Front Bumper 360°x59° Blindspot & Pedestrian Coverage"
    },
    {
      icon: Radio,
      title: "4x Sony IMX390 GMSL2 HDR",
      desc: lang === "tr" ? "120 dB Dinamik Aralık, 360° Çevre Görüş, Donanımsal Senkron" : "120 dB Dynamic Range, 360° Surround Vision, Hardware Sync"
    },
    {
      icon: Cpu,
      title: "NVIDIA Jetson AGX Orin 64GB",
      desc: lang === "tr" ? "275 TOPS AI Hesaplama, 4TB Samsung 990 PRO NVMe Kayıt" : "275 TOPS AI Compute, 4TB Samsung 990 PRO NVMe Storage"
    }
  ];

  return (
    <section id="robotaxi" className="relative w-full py-16 sm:py-20 px-4 sm:px-8 bg-[#090b0e] border-b border-white/10 relative z-20">
      <div className="max-w-7xl mx-auto space-y-10 sm:space-y-12">
        
        {/* Header: Corporate Clean & Confident */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-white/10">
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-slate-800/80 border border-slate-700 text-slate-300 text-xs font-mono font-medium tracking-wider uppercase">
              <span>{lang === "tr" ? "SEVİYE 4 OTONOM SÜRÜŞ PLATFORMU" : "LEVEL 4 AUTONOMOUS DRIVING PLATFORM"}</span>
            </div>
            
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-white tracking-tight">
              Hyundai Ioniq 5 (E-GMP) <br className="hidden sm:inline" />
              <span className="text-slate-300 font-semibold">
                {lang === "tr" ? "Seviye-4 Otonom Test Filosu" : "Level-4 Autonomous Fleet Architecture"}
              </span>
            </h2>

            <p className="text-slate-400 text-sm leading-relaxed">
              {lang === "tr"
                ? "128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış; 16.000 satır özgün deterministik otonomi yazılımı."
                : "Configured with 128-channel 3D LiDAR, 4x GMSL2 HDR cameras, 77GHz radar, and 100 Hz CAN-FD drive-by-wire across 16,000 lines of sovereign autonomy software."}
            </p>
          </div>

          {/* Action Buttons: Solid Executive Style */}
          <div className="flex flex-wrap items-center gap-3 shrink-0">
            <Link
              href="/robotaxi/"
              className="px-5 py-2.5 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-2"
            >
              <span>{lang === "tr" ? "TEKNİK DOKÜMANI İNCELE" : "VIEW TECHNICAL SPEC"}</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <a
              href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
              download
              className="px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 hover:bg-slate-800 font-medium text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-2"
            >
              <Download className="w-4 h-4 text-slate-400" />
              <span>{lang === "tr" ? "PDF ŞARTNAME (5 SAYFA)" : "DOWNLOAD SPEC PDF"}</span>
            </a>
          </div>
        </div>

        {/* 4 Executive Metric Cards */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "YAZILIM ÇEKİRDEĞİ" : "AUTONOMY CORE"}
            </div>
            <div className="text-2xl font-bold text-white">16.000+</div>
            <div className="text-xs text-slate-400">
              {lang === "tr" ? "Satır Özgün C++ / Python" : "Lines of Sovereign Code"}
            </div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "OTOMATİK TEST" : "AUTOMATED TESTS"}
            </div>
            <div className="text-2xl font-bold text-white">1.301 / 1.301</div>
            <div className="text-xs text-slate-400">
              {lang === "tr" ? "%100 Başarı (Sıfır Hata)" : "100% Pass Rate (0 Errors)"}
            </div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "HESAPLAMA GÜCÜ" : "AI COMPUTE"}
            </div>
            <div className="text-2xl font-bold text-white">275 TOPS</div>
            <div className="text-xs text-slate-400">NVIDIA Jetson AGX Orin</div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "LİDAR MENZİLİ" : "LIDAR RANGE"}
            </div>
            <div className="text-2xl font-bold text-white">240 Metre</div>
            <div className="text-xs text-slate-400">128 Kanal 3D SLAM</div>
          </div>
        </div>

        {/* Gallery + Engineering Specs Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          
          {/* 16:10 Automotive Media Frame (7 Cols) */}
          <div className="lg:col-span-7 space-y-3">
            <div className="relative rounded-2xl overflow-hidden border border-slate-800 bg-[#0c1017] aspect-[16/10] group">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={photos[selectedPhoto].src}
                alt={photos[selectedPhoto].title}
                className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.01]"
              />
              
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent pointer-events-none" />

              <div className="absolute bottom-4 left-4 right-4 flex items-end justify-between">
                <div className="space-y-0.5">
                  <span className="px-2 py-0.5 rounded bg-slate-900/90 border border-slate-700 text-slate-300 font-mono text-[10px] uppercase tracking-wider inline-block">
                    {photos[selectedPhoto].tag}
                  </span>
                  <h4 className="text-base sm:text-lg font-bold text-white">
                    {photos[selectedPhoto].title}
                  </h4>
                  <p className="text-slate-400 text-xs max-w-md">
                    {photos[selectedPhoto].desc}
                  </p>
                </div>
                <div className="text-xs font-mono text-slate-400">
                  {selectedPhoto + 1} / {photos.length}
                </div>
              </div>
            </div>

            {/* Thumbnail Pills */}
            <div className="grid grid-cols-7 gap-2">
              {photos.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedPhoto(idx)}
                  className={`relative rounded-lg overflow-hidden aspect-[4/3] border transition-all duration-200 cursor-pointer ${
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
          <div className="lg:col-span-5 space-y-3">
            <div className="text-xs font-mono text-slate-400 uppercase tracking-wider font-semibold">
              {lang === "tr" ? "TEMEL DONANIM BİLEŞENLERİ" : "CORE HARDWARE SUITE"}
            </div>

            <div className="space-y-2.5">
              {specs.map((item, i) => {
                const Icon = item.icon;
                return (
                  <div
                    key={i}
                    className="p-3.5 rounded-xl bg-[#0f131a] border border-slate-800 flex items-start gap-3 hover:border-slate-700 transition-colors"
                  >
                    <div className="w-8 h-8 rounded-lg bg-slate-800/60 border border-slate-700 flex items-center justify-center text-slate-300 shrink-0 mt-0.5">
                      <Icon className="w-4 h-4" />
                    </div>
                    <div className="space-y-0.5">
                      <div className="text-sm font-semibold text-white">
                        {item.title}
                      </div>
                      <div className="text-xs text-slate-400 leading-snug">
                        {item.desc}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Bottom Info Pill */}
            <div className="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 flex items-center justify-between gap-3 text-xs text-slate-300">
              <div>
                <span className="font-semibold text-white">CAN-FD Aktüatör Köprüsü:</span>{" "}
                {lang === "tr" ? "100 Hz LKAS11 & SCC_FD, 5ms acil devralma." : "100 Hz LKAS11 & SCC_FD, 5ms takeover."}
              </div>
              <Link
                href="/robotaxi/"
                className="shrink-0 font-medium text-white hover:underline flex items-center gap-1 text-xs"
              >
                <span>{lang === "tr" ? "Detay" : "More"}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
