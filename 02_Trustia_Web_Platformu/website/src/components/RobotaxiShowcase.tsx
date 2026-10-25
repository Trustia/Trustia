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
  Gauge
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
      tag: "DIŞ GÖRÜNÜM",
      label: lang === "tr" ? "01 Genel Görünüm" : "01 Exterior"
    },
    {
      src: "/robotaxi/ioniq5_foto_2.png",
      title: lang === "tr" ? "Ön Tampon & Sensör Podu" : "Front Bumper & Sensor Pod",
      desc: lang === "tr" ? "Livox Mid-360 LiDAR ve 77GHz Radar Entegrasyonu" : "Livox Mid-360 LiDAR & Radar",
      tag: "SENSÖR PODU",
      label: lang === "tr" ? "02 Ön Sensör Podu" : "02 Sensor Pod"
    },
    {
      src: "/robotaxi/ioniq5_foto_3.png",
      title: lang === "tr" ? "Yan Profil & Tavan Barı" : "Side Profile & Roof Rack",
      desc: lang === "tr" ? "Tavan Barı ve 128 Kanal Ouster OS2 LiDAR Montaj Hattı" : "Roof Bar & Ouster OS2 LiDAR",
      tag: "TAVAN HATTI",
      label: lang === "tr" ? "03 Tavan LiDAR" : "03 Roof LiDAR"
    },
    {
      src: "/robotaxi/ioniq5_foto_4.png",
      title: lang === "tr" ? "Arka Çeyrek & Kablo Girişi" : "Rear 3/4 & Cable Entry",
      desc: lang === "tr" ? "IP68 Yalıtımlı Kablo Geçiş Hattı ve Arka Spoyler" : "IP68 Cable Entry",
      tag: "KABLO YALITIMI",
      label: lang === "tr" ? "04 Arka Profil" : "04 Rear Profile"
    },
    {
      src: "/robotaxi/ioniq5_foto_6.png",
      title: lang === "tr" ? "Ön Kokpit & Telemetri Konsolu" : "Cockpit & Telemetry Console",
      desc: lang === "tr" ? "10.1\" Taktik Dokunmatik Ekran ve Acil Durum Butonu" : "10.1\" Touch Console & E-Stop",
      tag: "KOKPİT C2",
      label: lang === "tr" ? "05 Kokpit C2" : "05 Cockpit"
    },
    {
      src: "/robotaxi/ioniq5_foto_7.png",
      title: lang === "tr" ? "Arka Yolcu Alanı" : "Rear Cabin",
      desc: lang === "tr" ? "E-GMP Düz Zemin ve Yolcu Konfor Odaklı İç Mimari" : "E-GMP Flat Floor Comfort",
      tag: "YOLCU KABİNİ",
      label: lang === "tr" ? "06 Yolcu Kabini" : "06 Cabin"
    }
  ];

  const specs = [
    {
      num: "01",
      icon: Eye,
      title: "Ouster OS2-128 Rev 7 3D LiDAR",
      metric: "128 Kanal • 240m Menzil",
      desc: lang === "tr"
        ? "Saniyede 2.62 milyon nokta taraması ile 3D NDT SLAM ve santimetre hassasiyetinde uzaysal haritalama icra eder."
        : "Captures 2.62M points/sec for primary 3D NDT SLAM and spatial localization independent of GPS."
    },
    {
      num: "02",
      icon: Layers,
      title: "2x Livox Mid-360 LiDAR",
      metric: "360° x 59° • Kör Noktasız",
      desc: lang === "tr"
        ? "Ön tampon podlarına entegre çift LiDAR ile yakın mesafe yaya, bordür ve alçak engel taraması."
        : "Dual bumper-integrated LiDARs delivering comprehensive ultra-wide pedestrian and near-field obstacle tracking."
    },
    {
      num: "03",
      icon: Radio,
      title: "4x Sony IMX390 GMSL2 HDR",
      metric: "120 dB Dinamik Aralık • IP67",
      desc: lang === "tr"
        ? "Tünel çıkışları ve doğrudan güneş parlamasında donanımsal senkronize 360° çevre görüş."
        : "Hardware-synchronized 360-degree vision mitigating extreme lighting transitions and dynamic flares."
    },
    {
      num: "04",
      icon: Cpu,
      title: "NVIDIA Jetson AGX Orin 64GB",
      metric: "275 TOPS INT8 • 4TB NVMe",
      desc: lang === "tr"
        ? "275 TOPS merkezi AI hesaplama gücü ve kara kutu (DSSAD/EDR) sürekli telemetri kayıt kapasitesi."
        : "275 TOPS automotive AI compute running deterministic planning and high-speed telemetry black-box storage."
    },
    {
      num: "05",
      icon: Zap,
      title: "100 Hz Senkron CAN-FD Aktüatör",
      metric: "LKAS11 & SCC_FD • 5ms Devralma",
      desc: lang === "tr"
        ? "Direksiyon, gaz ve fren sistemlerine 100 Hz senkron komut iletimi ve 5ms donanımsal devralma kesmesi."
        : "100 Hz cyclic actuation with 5 millisecond hard-interrupt safety fallback over CAN-FD gateways."
    }
  ];

  return (
    <section id="robotaxi" className="relative z-20 py-10 sm:py-16 px-4 sm:px-8 lg:px-12 bg-[#06080c] border-b border-white/10">
      <div className="max-w-7xl mx-auto space-y-6 sm:space-y-8">
        
        {/* 1. Executive Split Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-8 items-end pb-5 border-b border-white/10">
          <div className="lg:col-span-8 space-y-2">
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[10px] font-mono tracking-wider uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
              <span>{lang === "tr" ? "SEVİYE 4 OTONOM SÜRÜŞ PLATFORMU // E-GMP" : "LEVEL 4 AUTONOMY STACK // E-GMP"}</span>
            </div>

            <h2 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug">
              Hyundai Ioniq 5{" "}
              <span className="text-slate-300 font-normal">
                {lang === "tr" ? "— Seviye-4 Otonom Filo Mimarisi" : "— Level-4 Fleet Architecture"}
              </span>
            </h2>

            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Elektrikli E-GMP şasisi üzerinde 100 Hz senkron CAN-FD aktüatör köprüsü, 128 kanallı 3D LiDAR ve çoklu sensör füzyonu ile donatılmış deterministik yerli otonom sürüş yazılım çekirdeği."
                : "Deterministic Level-4 autonomy stack interfacing natively with Hyundai E-GMP via 100 Hz CAN-FD drive-by-wire, 128-channel 3D LiDAR, and multi-modal sensor fusion."}
            </p>
          </div>

          {/* Right Action Link */}
          <div className="lg:col-span-4 flex lg:justify-end">
            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-1.5 text-xs font-mono font-semibold text-white hover:text-slate-200 uppercase tracking-wider pb-0.5 border-b border-white/30 hover:border-white transition-colors"
            >
              <span>{lang === "tr" ? "Şartname ve Donanım Yerleşimi" : "View Hardware Architecture"}</span>
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
              {lang === "tr" ? "Satır C++20 / Python" : "Lines of Code"}
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

        {/* 3. Main Split Showcase (Vehicle Presentation + Hardware Specifications) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
          
          {/* Left Column (7 Cols): Clean Panoramic Visual Showcase */}
          <div className="lg:col-span-7 space-y-4">
            
            {/* Visual Frame */}
            <div className="relative rounded-2xl overflow-hidden border border-white/10 bg-[#0a0d13] aspect-[16/10] group">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={photos[selectedPhoto].src}
                alt={photos[selectedPhoto].title}
                className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.01]"
              />

              {/* Gradient Vignette obscuring dealership text at the very top */}
              <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-black/60 pointer-events-none"></div>

              {/* Top Architecture Pill */}
              <div className="absolute top-4 left-4 right-4 flex items-center justify-between text-[10px] font-mono">
                <span className="px-2.5 py-1 rounded bg-black/70 border border-white/15 text-slate-300 backdrop-blur-md">
                  HYUNDAI E-GMP // 3.000 mm DİNGİL MESAFESİ
                </span>
                <span className="px-2 py-0.5 rounded bg-black/70 border border-white/10 text-slate-400">
                  {selectedPhoto + 1} / {photos.length}
                </span>
              </div>

              {/* Bottom Caption Overlay */}
              <div className="absolute bottom-4 left-4 right-4 space-y-1">
                <div className="inline-block px-2 py-0.5 rounded bg-white/10 border border-white/20 text-white font-mono text-[9px] uppercase tracking-wider">
                  {photos[selectedPhoto].tag}
                </div>
                <h4 className="text-base sm:text-lg font-bold text-white tracking-tight">
                  {photos[selectedPhoto].title}
                </h4>
                <p className="text-slate-300 text-xs font-sans line-clamp-1 sm:line-clamp-none">
                  {photos[selectedPhoto].desc}
                </p>
              </div>
            </div>

            {/* Clean Monospaced Text Pills Selector (NO CLASSIFIED AD THUMBNAIL BOXES!) */}
            <div className="flex flex-wrap items-center gap-2 pt-1">
              {photos.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedPhoto(idx)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-mono transition-all duration-200 cursor-pointer ${
                    selectedPhoto === idx
                      ? "bg-white text-slate-950 font-bold shadow-md"
                      : "bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white border border-white/10"
                  }`}
                >
                  {p.label}
                </button>
              ))}
            </div>

          </div>

          {/* Right Column (5 Cols): Hairline Separated Hardware Architecture List (KUTUSUZ) */}
          <div className="lg:col-span-5 space-y-4">
            <div className="border-b border-white/10 pb-3">
              <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold block">
                // DONANIM ENTEGRASYON MİMARİSİ
              </span>
              <h3 className="text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "Temel Sensör ve İşlemci Paketi" : "Core Sensor & Compute Suite"}
              </h3>
            </div>

            <div className="divide-y divide-white/10">
              {specs.map((item, idx) => {
                const Icon = item.icon;
                return (
                  <div key={idx} className="py-4 first:pt-0 last:pb-0 space-y-1.5">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2.5">
                        <span className="font-mono text-xs text-slate-500 font-bold">{item.num} //</span>
                        <h4 className="text-xs sm:text-sm font-bold text-white tracking-tight">
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
                  </div>
                );
              })}
            </div>

            {/* Bottom Regulatory Homologation Note */}
            <div className="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>UN ECE R157 & 1 ARALIK 2024 ADS</span>
              <span className="text-emerald-400 font-semibold">%100 UYUMLU</span>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
