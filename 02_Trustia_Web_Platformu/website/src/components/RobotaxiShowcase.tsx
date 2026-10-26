"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ShieldCheck, Cpu, Eye, Radio, Zap, Layers, Activity } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TacticalVehicleWireframe, { MIFA7_CALLOUTS } from "@/components/TacticalVehicleWireframe";

const COMPONENT_TABS = [
  { id: "lidar", labelTr: "3D LİDAR", labelEn: "3D LIDAR" },
  { id: "livox", labelTr: "KÖR NOKTA", labelEn: "BLIND SPOT" },
  { id: "canfd", labelTr: "CAN-FD SÜRÜŞ", labelEn: "CAN-FD DRIVE" },
  { id: "compute", labelTr: "OTONOM BEYİN", labelEn: "AI COMPUTE" },
  { id: "vision", labelTr: "360° KAMERA", labelEn: "360° VISION" },
  { id: "safety", labelTr: "EMNİYET HAKEMİ", labelEn: "SAFETY ARBITER" },
];

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
      titleTr: "Ouster OS2-128 Rev 7 3D LiDAR (Tavan Otonom Pod)",
      titleEn: "Ouster OS2-128 Rev 7 3D LiDAR (Roof Mount)",
      tagTr: "BİRİNCİL 3D SLAM & UZAYSAL HARİTALAMA",
      tagEn: "PRIMARY 3D SLAM & SPATIAL MAPPING",
      descTr:
        "Tavan merkezine entegre 128 kanal ile saniyede 2.62 milyon nokta üretir. GPS'siz tünel, yer altı otoparkı ve kanyonlarda 3D NDT SLAM santimetre hassasiyetinde uzaysal konumlandırma icra eder.",
      descEn:
        "Roof-mounted 128-channel solid-state LiDAR generating 2.62M pts/sec for GPS-denied 3D NDT SLAM spatial localization in tunnels and urban canyons.",
      spec: "240m Menzil • 128 Kanal • 0.1° Açısal Çözünürlük • UDP Gbit Ethernet",
      badge: "TAVAN SENSÖR PODU",
    },
    livox: {
      titleTr: "2x Livox Mid-360 LiDAR (Ön Tampon Podları)",
      titleEn: "2x Livox Mid-360 LiDAR (Front Bumper Pods)",
      tagTr: "KÖR NOKTASIZ YAKIN ÇEVRE ALGISI",
      tagEn: "ZERO-BLINDSPOT PERIMETER SENSING",
      descTr:
        "Ön sağ ve sol tampon köşelerine entegre çift LiDAR ile 360° x 59° ultra geniş açı. Şehir içi operasyonda yaya, bordür, düşük kotlu engel ve kavşak kör noktalarını sıfırlar.",
      descEn:
        "Dual bumper-integrated LiDARs delivering comprehensive 360° x 59° ultra-wide pedestrian and near-field obstacle tracking.",
      spec: "360° x 59° FOV • 40m Menzil • Santimetre Hassasiyet",
      badge: "ÖN TAMPON KÖR NOKTA",
    },
    canfd: {
      titleTr: "100 Hz Senkron CAN-FD Aktüatör Köprüsü (Tripy EPS & i-Booster)",
      titleEn: "100 Hz Synchronous CAN-FD Bridge (Tripy EPS & i-Booster)",
      tagTr: "DONANIMSAL AKTÜASYON & SÜRÜŞ KÖPRÜSÜ",
      tagEn: "DRIVE-BY-WIRE & CHASSIS ACTUATION",
      descTr:
        "SAIC Maxus MIFA 7 şasisine doğrudan 100 Hz senkron tork, fren ve gaz komut iletimi. 1.4 ms mesaj gecikmesi ve 5 ms donanımsal devralma kesmesi (hardware override) güvencesi.",
      descEn:
        "Native 100 Hz cyclic torque, brake, and throttle actuation over Maxus MIFA 7 CAN-FD gateways with 1.4ms latency and 5ms hardware override.",
      spec: "100 Hz Senkron Çevrim • 1.4 ms Gecikme • 5 ms Devralma Kesmesi",
      badge: "CAN-FD DRIVE-BY-WIRE",
    },
    compute: {
      titleTr: "560 TOPS Merkezi Otonom Beyin (Horizon Nash BPU / NVIDIA Orin)",
      titleEn: "560 TOPS Central Autonomy Compute (Horizon / NVIDIA Orin)",
      tagTr: "MERKEZİ OTONOM YAPAY ZEKA BİLGİSAYARI",
      tagEn: "CENTRAL AUTONOMY AI COMPUTE",
      descTr:
        "560 TOPS merkezi yapay zeka işlem gücü. Hibrit A* kinematik yörünge planlama, çoklu sensör füzyonu ve sürekli telemetri kara kutu (DSSAD/EDR) kayıtlarını deterministik yürütür.",
      descEn:
        "560 TOPS central AI compute executing Hybrid A* path planning, multi-sensor fusion, and continuous EDR black-box telemetry.",
      spec: "560 TOPS INT8 • 64GB LPDDR5 • 4TB NVMe Kara Kutu",
      badge: "ZEMİN ALTI OTONOM BEYİN",
    },
    vision: {
      titleTr: "4x Sony IMX390 GMSL2 HDR Kamera Paketi",
      titleEn: "4x Sony IMX390 GMSL2 HDR Surround Vision",
      tagTr: "360° ÇEVRESEL GÖRSEL ALGILAMA",
      tagEn: "360° SURROUND VISUAL PERCEPTION",
      descTr:
        "Ön cam, yan aynalar ve arka spoyler hatlarında 120° FOV lenslerle 120 dB süper dinamik aralık. Doğrudan güneş parlaması ve tünel çıkışlarında donanımsal FSYNC senkron çevre görüş.",
      descEn:
        "Synchronized 120° FOV surround cameras with 120 dB dynamic range, mitigating extreme lighting flares and tunnel transitions.",
      spec: "120 dB Dinamik Aralık • 60 FPS Senkron • IP67 Donanım FSYNC",
      badge: "360° GÖRSEL FÜZYON",
    },
    safety: {
      titleTr: "ISO 26262 ASIL-D Emniyet Hakemi & Watchdog",
      titleEn: "ISO 26262 ASIL-D Safety Arbiter & Watchdog",
      tagTr: "FONKSİYONEL GÜVENLİK VE ACİL DEVRE KESME",
      tagEn: "FUNCTIONAL SAFETY & FAILSAFE INTERRUPT",
      descTr:
        "50 ms kontrol zaman aşımı durumunda devreye giren Minimal Risk Maneuver (MRM). 1.5 m/s² kontrollü sağa çekme, acil durum frenleme ve E-Stop donanımsal koruma kalkanı.",
      descEn:
        "50ms watchdog hardware interrupt triggering Minimal Risk Maneuver (MRM) with 1.5 m/s² controlled pullover deceleration and E-Stop.",
      spec: "ISO 26262 ASIL-D • 50 ms Watchdog • 1.5 m/s² MRM Sağa Çekme",
      badge: "FAILSAFE GÜVENLİK HAKEMİ",
    },
  };

  const current = calloutDetails[activeCalloutId] || calloutDetails.lidar;

  return (
    <section
      id="robotaxi"
      className="relative z-20 pt-20 sm:pt-28 pb-14 sm:pb-20 px-4 sm:px-8 lg:px-12 bg-[#090b0e] text-white select-none overflow-hidden scroll-mt-20 sm:scroll-mt-28"
    >
      {/* Soft Ambient Spotlight directly behind 3D MIFA 7 Vehicle */}
      <div className="absolute top-[52%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-[85vw] max-w-[1000px] h-[500px] bg-[radial-gradient(ellipse_at_center,rgba(228,248,13,0.06),transparent_70%)] pointer-events-none blur-3xl z-0" />

      <div className="max-w-7xl mx-auto space-y-6 sm:space-y-8 relative z-10">
        
        {/* ========================================================
            1. PUNCHY EXECUTIVE HEADER (SIFIR KUTU)
           ======================================================== */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-white/10">
          <div className="space-y-2.5 max-w-3xl">
            {/* Taktik HUD Başlığı */}
            <div className="inline-flex items-center gap-2 font-mono text-[11px] uppercase tracking-widest text-slate-300">
              <span className="text-[#E4F80D] font-bold">[+]</span>
              <span className="text-white font-semibold">
                {lang === "tr" ? "SEVİYE-4 ROBOTAKSİ MİMARİSİ" : "LEVEL-4 ROBOTAXI ARCHITECTURE"}
              </span>
              <span className="text-slate-600">/</span>
              <span className="text-[#E4F80D] font-bold">SAIC MAXUS MIFA 7</span>
              <span className="text-slate-600">/</span>
              <span className="text-slate-400">TRIPY MOBILITY</span>
            </div>

            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-white leading-tight font-sans">
              <span className="block text-white">Tripy SAIC Maxus MIFA 7</span>
              <span className="block text-slate-300 font-light text-lg sm:text-2xl lg:text-3xl mt-1">
                {lang === "tr" ? "Seviye-4 Otonom Sürüş Mimarisi" : "Level-4 Autonomous Driving Architecture"}
              </span>
            </h2>

            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal pt-0.5">
              {lang === "tr"
                ? "Tripy Mobility ticari elektrikli filoları için geliştirilmiş; 100 Hz senkron CAN-FD aktüatör kontrolü (EPS & i-Booster), 3D LiDAR SLAM ve ISO 26262 ASIL-D deterministik seyrüsefer referans yazılım mimarisi."
                : "Deterministic Level-4 autonomy architecture engineered for Tripy Mobility commercial electric fleets via 100 Hz CAN-FD drive-by-wire and 3D LiDAR SLAM."}
            </p>
          </div>

          {/* Action Link (Kutudan arındırılmış temiz buton) */}
          <div className="shrink-0 flex items-center">
            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-wider px-4 py-2.5 bg-[#E4F80D] text-black font-bold hover:bg-white transition-all shadow-[0_2px_12px_rgba(228,248,13,0.3)] cursor-pointer"
            >
              <span>{lang === "tr" ? "Mühendislik Şartnamesi (NDA)" : "Engineering Blueprint (NDA)"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>

        {/* ========================================================
            2. 3D TACTICAL VEHICLE WIREFRAME (100% KUTUSUZ / FRAMELESS)
            - Saf Maxus MIFA 7 Şasisi (2.975mm Dingil Mesafesi)
            - Arka plan zifiri karanlığa doğrudan gömülü (Kutu yok!)
            - Kullanıcı fareyle ve mobilde parmağıyla 3D çevirebilir
           ======================================================== */}
        <div className="space-y-4">
          
          {/* Frameless Top Bar: Coordinate Readout & Component Switcher */}
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 pb-3 border-b border-white/10">
            <div className="flex items-center gap-2 text-[10px] font-mono tracking-wider text-slate-300">
              <span className="w-2 h-2 bg-[#E4F80D] animate-pulse" />
              <span className="text-white font-bold">SAIC MAXUS MIFA 7 // 3D ŞASİ TOPOLOJİSİ</span>
              <span className="text-slate-600 hidden sm:inline">/</span>
              <span className="text-slate-400 hidden sm:inline">DİNGİL: 2.975mm • UZUNLUK: 4.907mm</span>
            </div>

            {/* Frameless Tactical Selector Strip (100% SIFIR KUTU, PURE UNDERLINE TABS) */}
            <div className="flex items-center gap-2 sm:gap-4 overflow-x-auto no-scrollbar py-1 -mx-2 px-2 sm:mx-0 sm:px-0">
              {COMPONENT_TABS.map((tab) => {
                const isActive = activeCalloutId === tab.id;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveCalloutId(tab.id)}
                    className={`shrink-0 pb-1.5 pt-1 px-1 text-[10px] sm:text-[11px] font-mono tracking-wider uppercase transition-all duration-150 cursor-pointer flex items-center gap-1.5 border-b-2 ${
                      isActive
                        ? "text-[#E4F80D] font-bold border-[#E4F80D] drop-shadow-[0_0_8px_rgba(228,248,13,0.6)]"
                        : "text-slate-400 hover:text-white border-transparent"
                    }`}
                  >
                    {isActive && <span className="w-1.5 h-1.5 bg-[#E4F80D]" />}
                    <span>{lang === "tr" ? tab.labelTr : tab.labelEn}</span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Full-Bleed 100% Frameless 3D Wireframe Canvas */}
          <div className="relative w-full h-[340px] xs:h-[400px] sm:h-[480px] lg:h-[560px]">
            <TacticalVehicleWireframe
              activeId={activeCalloutId}
              onSelectCallout={setActiveCalloutId}
              className="w-full h-full"
            />
          </div>

          {/* Frameless Active Specification HUD (Sıfır Kutu, Saf Tipografi) */}
          <div className="pt-4 border-t border-white/10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="space-y-1.5 max-w-2xl">
              <div className="flex items-center gap-2 font-mono text-[10px]">
                <span className="text-[#E4F80D] font-bold">
                  [ {current.badge} ]
                </span>
                <span className="text-slate-500">/</span>
                <span className="text-slate-400 uppercase tracking-wider">
                  {lang === "tr" ? current.tagTr : current.tagEn}
                </span>
              </div>
              <div className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? current.titleTr : current.titleEn}
              </div>
              <p className="text-xs text-slate-300 leading-relaxed font-sans font-normal">
                {lang === "tr" ? current.descTr : current.descEn}
              </p>
            </div>

            <div className="shrink-0 text-left md:text-right font-mono space-y-1 md:pl-6 md:border-l border-white/10">
              <span className="text-[10px] text-slate-400 uppercase tracking-widest block font-medium">
                // DONANIM METRİĞİ
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
            3. VERIFIED BENCHMARKS (100% KUTUSUZ / PURE TYPOGRAPHY)
            - 16.400+ LOC, 1.307 Tests, 100 Hz CAN-FD, 560 TOPS
            - Sıfır kutu, sıfır kart sınırı!
           ======================================================== */}
        <div className="pt-6 border-t border-white/10 space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 font-mono text-[11px] text-slate-400 uppercase tracking-wider">
            <div className="flex items-center gap-2">
              <span className="text-[#E4F80D] font-bold">//</span>
              <span className="text-white font-semibold">TRİPY SAHA ENTEGRASYON VE DOĞRULAMA KÜTÜĞÜ</span>
            </div>
            <span className="text-[#E4F80D] font-semibold">%100 MİLLİ SEVİYE-4 ÇEKİRDEK</span>
          </div>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8 font-mono">
            {/* Stat 1 */}
            <div className="space-y-1">
              <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
                YAZILIM ÇEKİRDEĞİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                16.400+
              </div>
              <span className="text-[11px] text-slate-400 font-sans block">
                Satır C++20 / ROS 2 Çekirdek
              </span>
            </div>

            {/* Stat 2 */}
            <div className="space-y-1 sm:border-l border-white/10 sm:pl-6">
              <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
                DOĞRULAMA KÜTÜPHANESİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-[#C8FF00] tracking-tight">
                1.307 / 1.307
              </div>
              <span className="text-[11px] text-emerald-400 font-sans font-medium block">
                %100 Yeşil Test (0 Hata / 0 Fail)
              </span>
            </div>

            {/* Stat 3 */}
            <div className="space-y-1 border-t sm:border-t-0 sm:border-l border-white/10 pt-4 sm:pt-0 sm:pl-6">
              <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
                CAN-FD ÇEVRİMİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                100 Hz
              </div>
              <span className="text-[11px] text-slate-400 font-sans block">
                Tripy EPS &amp; i-Booster Senkron
              </span>
            </div>

            {/* Stat 4 */}
            <div className="space-y-1 border-t sm:border-t-0 sm:border-l border-white/10 pt-4 sm:pt-0 sm:pl-6">
              <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-semibold">
                DONANIMSAL KESME
              </span>
              <div className="text-2xl sm:text-3xl font-black text-[#E4F80D] tracking-tight">
                5 ms
              </div>
              <span className="text-[11px] text-slate-400 font-sans block">
                Acil Durum Devralma Güvencesi
              </span>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
