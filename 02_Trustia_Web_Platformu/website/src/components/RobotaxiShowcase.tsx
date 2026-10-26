"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ShieldCheck, Cpu, Eye, Radio, Zap, Layers, Activity } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TacticalVehicleWireframe, { TACTICAL_CALLOUTS } from "@/components/TacticalVehicleWireframe";

export default function RobotaxiShowcase() {
  const { lang } = useLanguage();
  const [activeCalloutId, setActiveCalloutId] = useState<string>("lidar");

  const calloutDetails: Record<
    string,
    {
      titleTr: string;
      titleEn: string;
      tagTr: string;
      tagEn: string;
      descTr: string;
      descEn: string;
      spec: string;
      badge: string;
    }
  > = {
    lidar: {
      titleTr: "Ouster OS2-128 Rev 7 3D LiDAR",
      titleEn: "Ouster OS2-128 Rev 7 3D LiDAR",
      tagTr: "BİRİNCİL 3D SLAM & UZAYSAL HARİTALAMA",
      tagEn: "PRIMARY 3D SLAM & SPATIAL MAPPING",
      descTr:
        "Tavan merkezine entegre 128 kanal ile saniyede 2.62 milyon nokta üretir. GPS'siz tünel, yer altı ve kanyonlarda 3D NDT SLAM santimetre hassasiyetinde uzaysal konumlandırma icra eder.",
      descEn:
        "Roof-mounted 128-channel solid-state LiDAR generating 2.62M pts/sec for GPS-denied 3D NDT SLAM spatial localization.",
      spec: "240m Menzil • 128 Kanal • 0.1° Açısal Çözünürlük • Gbit Ethernet",
      badge: "ROOF SENSOR POD",
    },
    compute: {
      titleTr: "NVIDIA Jetson AGX Orin 64GB",
      titleEn: "NVIDIA Jetson AGX Orin 64GB",
      tagTr: "MERKEZİ OTONOM YAPAY ZEKA BİLGİSAYARI",
      tagEn: "CENTRAL AUTONOMY AI COMPUTE",
      descTr:
        "275 TOPS INT8 yapay zeka işlem gücü. Hibrit A* yol planlama, engelden kaçınma ve sürekli telemetri kara kutu (DSSAD/EDR) kayıtlarını 100 Hz çevrimde deterministik icra eder.",
      descEn:
        "275 TOPS INT8 central AI compute executing Hybrid A* path planning, obstacle avoidance, and continuous EDR black-box telemetry.",
      spec: "275 TOPS INT8 • 64GB LPDDR5 • 4TB NVMe Telemetri",
      badge: "CENTRAL CHASSIS HUB",
    },
    canfd: {
      titleTr: "100 Hz Senkron CAN-FD Aktüatör Köprüsü",
      titleEn: "100 Hz Synchronous CAN-FD Actuation Bridge",
      tagTr: "DONANIMSAL AKTÜASYON & SÜRÜŞ KÖPRÜSÜ",
      tagEn: "DRIVE-BY-WIRE & CHASSIS ACTUATION",
      descTr:
        "Hyundai Ioniq 5 ve taktik platform şasilerine 100 Hz senkron tork, fren ve gaz komut iletimi. 1.4 ms mesaj gecikmesi ve 5 ms donanımsal devralma kesmesi güvencesi.",
      descEn:
        "100 Hz cyclic torque, brake, and throttle actuation over CAN-FD gateways with 1.4ms latency and 5ms hardware takeover override.",
      spec: "100 Hz Çevrim • 1.4 ms Gecikme • 5 ms Donanımsal Devralma",
      badge: "STEERING & DRIVE-BY-WIRE",
    },
    vision: {
      titleTr: "4x Sony IMX390 GMSL2 HDR Kamera Paketi",
      titleEn: "4x Sony IMX390 GMSL2 HDR Surround Vision",
      tagTr: "360° ÇEVRESEL GÖRSEL ALGILAMA",
      tagEn: "360° SURROUND VISUAL PERCEPTION",
      descTr:
        "Ön, arka ve yan hatlarda 120° FOV lenslerle 120 dB süper dinamik aralık. Doğrudan güneş parlaması ve tünel geçişlerinde donanımsal FSYNC senkronize çevre görüş.",
      descEn:
        "Synchronized 120° FOV surround cameras with 120 dB dynamic range, mitigating extreme lighting flares and tunnel transitions.",
      spec: "120 dB Dinamik Aralık • 60 FPS Senkron • IP67 Donanım FSYNC",
      badge: "360° SURROUND VISION",
    },
    radar: {
      titleTr: "Continental ARS 408 77GHz Otomotiv Radarı",
      titleEn: "Continental ARS 408 77GHz Automotive Radar",
      tagTr: "TÜM HAVA KOŞULLARINDA DOPPLER HIZ",
      tagEn: "ALL-WEATHER DOPPLER VELOCITY",
      descTr:
        "Yoğun sis, sağanak yağmur, kar ve toz fırtınasında doğrudan Doppler radyal hız tespiti. 250 metreye kadar hareketli cisimlerin bağıl hız vektörlerini sıfır kör noktayla çıkarır.",
      descEn:
        "Direct Doppler radial velocity measurements penetrating dense fog, rain, snow, and dust up to 250 meters.",
      spec: "250m Menzil • ±0.1 km/s Hız Hassasiyeti • CAN-FD Veri Yolu",
      badge: "FRONT RADAR BUMPER",
    },
    safety: {
      titleTr: "ISO 26262 ASIL-D MRM & Watchdog Modülü",
      titleEn: "ISO 26262 ASIL-D MRM & Safety Watchdog",
      tagTr: "FONKSİYONEL GÜVENLİK VE ACİL DEVRE KESME",
      tagEn: "FUNCTIONAL SAFETY & FAILSAFE INTERRUPT",
      descTr:
        "50 ms kontrol zaman aşımı durumunda devreye giren Minimal Risk Maneuver (MRM). 1.5 m/s² kontrollü sağa çekme, acil durum frenleme ve E-Stop donanımsal koruma kalkanı.",
      descEn:
        "50ms watchdog hardware interrupt triggering Minimal Risk Maneuver (MRM) with 1.5 m/s² controlled pullover deceleration and E-Stop.",
      spec: "ISO 26262 ASIL-D • 50 ms Watchdog • 1.5 m/s² MRM Sağa Çekme",
      badge: "FAILSAFE CONTROLLER",
    },
  };

  const current = calloutDetails[activeCalloutId] || calloutDetails.lidar;

  const platforms = [
    {
      badge: "AUTONOMY ENABLED",
      titleTr: "Hyundai Ioniq 5 Robotaksi",
      titleEn: "Hyundai Ioniq 5 Robotaxi",
      descTr:
        "Ticari elektrikli yolcu filoları için 100 Hz senkron CAN-FD direksiyon ve hız kontrolü.",
      descEn:
        "Deterministic Level-4 autonomy for commercial electric passenger fleets over native CAN-FD.",
      spec: "100 Hz CAN-FD • 50 km/s Seviye-4",
    },
    {
      badge: "DUAL-USE CAPABLE",
      titleTr: "Taktik İnsansız Kara Aracı (İKA)",
      titleEn: "Tactical Unmanned Ground Vehicle (UGV)",
      descTr:
        "GPS karartmalı muharebe sahalarında 3D NDT SLAM ve arazi şartlarında tam otonom seyrüsefer.",
      descEn:
        "GPS-denied 3D NDT SLAM maneuver engineered for sovereign defense and off-road rugged robotics.",
      spec: "GPS-Denied 3D SLAM • MIL-STD-810H",
    },
    {
      badge: "INDUSTRIAL FLEET",
      titleTr: "Ağır Hizmet ve Liman AGV'si",
      titleEn: "Heavy-Duty Industrial & Port AGV",
      descTr:
        "Maden ocakları ve konteyner terminallerinde 7/24 deterministik otonom yük ve ring taşımacılığı.",
      descEn:
        "Continuous 24/7 deterministic ring transport for mining hubs and logistics container yards.",
      spec: "15 km/s Fabrika İçi • Ağır Tonaj",
    },
  ];

  return (
    <section
      id="robotaxi"
      className="relative z-20 py-12 sm:py-20 px-4 sm:px-8 lg:px-12 bg-[#26221B] border-y border-[#383226] text-white select-none overflow-hidden"
    >
      {/* Overland-Style Subtle Background Watermark Typography */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-[14vw] sm:text-[16vw] font-mono font-black text-white/[0.02] tracking-tighter uppercase pointer-events-none select-none whitespace-nowrap z-0">
        IONIQ 5 E-GMP™
      </div>

      <div className="max-w-7xl mx-auto space-y-8 sm:space-y-12 relative z-10">
        
        {/* ========================================================
            1. OVERLAND TOPLINE & MINIMAL PUNCHY HEADER
           ======================================================== */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-[#383226]">
          <div className="space-y-3 max-w-3xl">
            {/* Overland Tactical Eyebrow */}
            <div className="inline-flex items-center gap-2 font-mono text-[11px] uppercase tracking-widest text-slate-300">
              <span className="text-[#E4F80D] font-bold">[+]</span>
              <span className="text-white font-semibold">
                {lang === "tr" ? "REFERANS OTONOMİ MİMARİSİ (RAD)" : "REFERENCE AUTONOMY ARCHITECTURE"}
              </span>
              <span className="text-slate-500">/</span>
              <span className="text-[#E4F80D]">E-GMP // DUAL-USE</span>
            </div>

            <h2 className="text-2xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight font-sans">
              Hyundai Ioniq 5 &amp;{" "}
              <span className="text-slate-300 font-light">
                {lang === "tr" ? "Çift Amaçlı Otonomi Mimarisi" : "Dual-Use Autonomy Stack"}
              </span>
            </h2>

            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Şehir içi elektrikli robotaksi filoları ve kritik insansız kara araçları (İKA) için 100 Hz senkron CAN-FD ve 3D LiDAR SLAM referans donanım mimarisi."
                : "Deterministic Level-4 reference hardware architecture interfacing natively via 100 Hz CAN-FD drive-by-wire and 3D LiDAR SLAM."}
            </p>
          </div>

          {/* Action Blueprint Link */}
          <div className="shrink-0 flex items-center">
            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-wider px-3.5 py-2 bg-[#E4F80D] text-black font-bold hover:bg-white transition-all shadow-[0_2px_10px_rgba(228,248,13,0.3)] cursor-pointer"
            >
              <span>{lang === "tr" ? "Mühendislik Şartnamesi (NDA)" : "Engineering Blueprint (NDA)"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>

        {/* ========================================================
            2. 3D TACTICAL VEHICLE WIREFRAME STAGE (CENTERPIECE)
            - Overland AI Vector Wireframe Engine
            - Real-time 3D rotation, mouse drag & touch friendly
            - Projected neon volt yellow HUD callouts
           ======================================================== */}
        <div className="rounded-xl border border-[#383226] bg-[#1A1712] overflow-hidden shadow-2xl relative">
          
          {/* Stage Top Bar: Coordinate Readout & Tactical Selector Strip */}
          <div className="p-3 sm:p-4 border-b border-[#383226] bg-[#0E0D09]/80 backdrop-blur-md flex flex-col md:flex-row md:items-center justify-between gap-3">
            <div className="flex items-center gap-2 text-[10px] font-mono tracking-wider text-slate-300">
              <span className="w-2 h-2 bg-[#E4F80D] animate-pulse" />
              <span className="text-white font-bold">3D CHASSIS // SENSÖR VE AKTÜATÖR DÜZENİ</span>
              <span className="text-slate-600 hidden sm:inline">|</span>
              <span className="text-slate-400 hidden sm:inline">ÖLÇEK: 1:1 CAN-FD VE SLAM TOPOLOJİSİ</span>
            </div>

            {/* Tactical Selector Tabs */}
            <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-0.5 -mx-1 px-1">
              {TACTICAL_CALLOUTS.map((callout) => {
                const isActive = activeCalloutId === callout.id;
                return (
                  <button
                    key={callout.id}
                    onClick={() => setActiveCalloutId(callout.id)}
                    className={`shrink-0 px-2.5 py-1 text-[10px] font-mono uppercase tracking-wider transition-all duration-150 cursor-pointer ${
                      isActive
                        ? "bg-[#E4F80D] text-black font-bold shadow-[0_0_8px_rgba(228,248,13,0.4)]"
                        : "bg-white/[0.04] hover:bg-white/[0.08] text-slate-300 border border-white/10"
                    }`}
                  >
                    {callout.name.split(" ")[0]}
                  </button>
                );
              })}
            </div>
          </div>

          {/* 3D Wireframe Canvas Container */}
          <div className="relative w-full h-[320px] xs:h-[370px] sm:h-[460px] lg:h-[520px]">
            <TacticalVehicleWireframe
              activeId={activeCalloutId}
              onSelectCallout={setActiveCalloutId}
              className="w-full h-full"
            />
          </div>

          {/* Active Component Specification HUD Readout */}
          <div className="p-4 sm:p-5 border-t border-[#383226] bg-[#0E0D09]/95 backdrop-blur-md flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="space-y-1 max-w-2xl">
              <div className="flex items-center gap-2 font-mono text-[10px]">
                <span className="px-1.5 py-0.5 bg-[#E4F80D]/15 text-[#E4F80D] font-bold border border-[#E4F80D]/30">
                  {current.badge}
                </span>
                <span className="text-slate-400 uppercase tracking-wider">
                  {lang === "tr" ? current.tagTr : current.tagEn}
                </span>
              </div>
              <div className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? current.titleTr : current.titleEn}
              </div>
              <p className="text-xs text-slate-300 leading-relaxed font-sans font-normal">
                {lang === "tr" ? current.descTr : current.descEn}
              </p>
            </div>

            <div className="shrink-0 text-left sm:text-right font-mono space-y-1 sm:pl-4 sm:border-l border-[#383226]">
              <span className="text-[10px] text-slate-400 uppercase tracking-widest block font-medium">
                DONANIM ÖZELLİKLERİ
              </span>
              <div className="text-xs sm:text-[13px] font-bold text-[#E4F80D] tracking-tight">
                {current.spec}
              </div>
              <div className="text-[10px] text-slate-400">
                UN ECE R157 &amp; ISO 26262 ASIL-D
              </div>
            </div>
          </div>

        </div>

        {/* ========================================================
            3. OVERLAND-STYLE VEHICLE FLEET CARDS (AUTONOMY ENABLED)
            - 3-Column Tactical Platform Architecture
            - Zero text clutter, punchy mission capability
           ======================================================== */}
        <div className="space-y-4">
          <div className="flex items-center justify-between font-mono text-[11px] text-slate-400 uppercase tracking-wider border-b border-[#383226] pb-2">
            <span className="text-slate-200 font-semibold">// DESTEKLENEN ARAÇ PLATFORMLARI</span>
            <span className="text-[#E4F80D]">EVRENSEL L4 ÇEKİRDEK</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {platforms.map((plat, idx) => (
              <div
                key={idx}
                className="p-4 sm:p-5 rounded-lg border border-[#383226] bg-[#1A1712] hover:border-[#E4F80D]/40 transition-colors space-y-3 group"
              >
                <div className="flex items-center justify-between font-mono text-[10px]">
                  <span className="px-1.5 py-0.5 bg-[#E4F80D] text-black font-bold uppercase">
                    [{plat.badge}]
                  </span>
                  <span className="text-slate-400">0{idx + 1} //</span>
                </div>

                <h4 className="text-base font-bold text-white tracking-tight group-hover:text-[#E4F80D] transition-colors">
                  {lang === "tr" ? plat.titleTr : plat.titleEn}
                </h4>

                <p className="text-xs text-slate-300 leading-relaxed font-sans font-normal">
                  {lang === "tr" ? plat.descTr : plat.descEn}
                </p>

                <div className="pt-2 border-t border-[#383226] font-mono text-[10px] text-slate-400 flex items-center justify-between">
                  <span>METRİK:</span>
                  <span className="text-white font-medium">{plat.spec}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ========================================================
            4. OVERLAND "BUILT BY OVERLAND" STYLE COYOTE TAN BANNER
            - Desert Sand (#E5D6BC) High-Contrast Engineering Block
            - Verified Benchmarks: 16.400+ LOC, 1.307 Tests, 275 TOPS
           ======================================================== */}
        <div className="rounded-xl bg-[#E5D6BC] text-black p-6 sm:p-8 lg:p-10 shadow-xl space-y-6">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6 border-b border-black/15 pb-6">
            <div className="space-y-1.5">
              <div className="font-mono text-[11px] font-bold uppercase tracking-widest text-black/70 flex items-center gap-1.5">
                <span className="w-2 h-2 bg-black" />
                <span>BUILT BY TRUSTIA AI TECHNOLOGIES</span>
              </div>
              <h3 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-black font-sans">
                {lang === "tr"
                  ? "Sovereign Seviye-4 Referans Otonomi Çekirdeği"
                  : "Sovereign Level-4 Reference Autonomy Core"}
              </h3>
            </div>

            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-2 px-4 py-2.5 bg-black text-[#E4F80D] font-mono text-xs font-bold uppercase tracking-wider hover:bg-slate-900 transition-colors self-start lg:self-auto cursor-pointer"
            >
              <span>{lang === "tr" ? "TEKNOLOJİYİ İNCELE" : "EXPLORE ARCHITECTURE"}</span>
              <span className="text-[#E4F80D]">↵</span>
            </Link>
          </div>

          {/* 3-Metric Clean Monospaced Readout */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 font-mono">
            <div className="space-y-0.5">
              <span className="text-[10px] font-bold text-black/60 uppercase tracking-wider block">
                YAZILIM ÇEKİRDEĞİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-black tracking-tight">
                16.400+
              </div>
              <span className="text-xs text-black/80 font-sans block">
                Satır Deterministik C++20 / ROS 2
              </span>
            </div>

            <div className="space-y-0.5 sm:border-l sm:border-black/15 sm:pl-6">
              <span className="text-[10px] font-bold text-black/60 uppercase tracking-wider block">
                DOĞRULAMA KÜTÜPHANESİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-black tracking-tight">
                1.307 / 1.307
              </div>
              <span className="text-xs text-emerald-800 font-sans font-bold block">
                %100 Yeşil Test (0 Hata / 0 Fail)
              </span>
            </div>

            <div className="space-y-0.5 sm:border-l sm:border-black/15 sm:pl-6">
              <span className="text-[10px] font-bold text-black/60 uppercase tracking-wider block">
                MERKEZİ HESAPLAMA GÜCÜ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-black tracking-tight">
                275 TOPS
              </div>
              <span className="text-xs text-black/80 font-sans block">
                Jetson AGX Orin &amp; 100 Hz CAN-FD
              </span>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
