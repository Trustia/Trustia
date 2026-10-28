"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TacticalVehicleWireframe from "@/components/TacticalVehicleWireframe";

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
      titleTr: "3D LiDAR Nokta Bulutu Arayüzü (Hesai / Ouster / Robosense 128-Kanal)",
      titleEn: "3D LiDAR Point-Cloud HAL Interface (Hesai / Ouster / Robosense 128-Ch)",
      tagTr: "BİRİNCİL 3D SLAM & IEEE 1588v2 PTP DESKEWING YAZILIM KATMANI",
      tagEn: "PRIMARY 3D SLAM & IEEE 1588v2 PTP DESKEWING SOFTWARE LAYER",
      descTr:
        "Araç üzerindeki 3D LiDAR sensöründen gelen nokta bulutlarını UDP/Ethernet üzerinden okur; IEEE 1588v2 PTP zaman senkronizasyonu ve 400 Hz IMU ego-motion deskewing ile GPS'siz tünel ve kanyonlarda 3D NDT SLAM konumlandırma icra eder.",
      descEn:
        "Ingests 3D LiDAR streams over UDP/Ethernet with IEEE 1588v2 PTP motion deskewing for GPS-denied 3D NDT SLAM spatial localization.",
      spec: "Hesai / Ouster Uyumu • PTP < 1 µs • 4.2 cm SLAM Hassasiyeti",
      badge: "3D LIDAR HAL SÜRÜCÜSÜ",
    },
    livox: {
      titleTr: "Yakın Çevre, Kör Nokta & 3D Kaldırım Taşı (Curb) Algılama Modülü",
      titleEn: "Near-Field Blindspot & 3D Curb Boundary Detection Module",
      tagTr: "KÖR NOKTASIZ YAKIN ÇEVRE & KALDIRIM KORİDORU YAZILIMI",
      tagEn: "ZERO-BLINDSPOT PERIMETER & CURB CORRIDOR SOFTWARE",
      descTr:
        "Tampon/yan kör nokta LiDAR verilerini işleyerek şehir içi operasyonda yaya, bisikletli ve kavşak kör noktalarını tarar; şerit çizgilerinin silindiği yollarda 8-28 cm kaldırım taşı basamağından sürüş koridoru çıkarır.",
      descEn:
        "Processes perimeter LiDAR streams for vulnerable road user (VRU) tracking and extracts drivable road corridors from 8-28 cm 3D curb height steps.",
      spec: "8-28 cm Bordür Kilidi • RANSAC + DBSCAN • VRU Yaya Takibi",
      badge: "KÖR NOKTA & BORDÜR ALGISI",
    },
    canfd: {
      titleTr: "100 Hz Senkron CAN-FD & UN R155 IDPS Köprüsü (EPS & i-Booster)",
      titleEn: "100 Hz Synchronous CAN-FD & UN R155 IDPS Bridge (EPS & i-Booster)",
      tagTr: "FAIL-OPERATIONAL AKTÜASYON & DBC SÜRÜŞ KÖPRÜSÜ",
      tagEn: "FAIL-OPERATIONAL DRIVE-BY-WIRE & CHASSIS ACTUATION",
      descTr:
        "SAIC Maxus MIFA 7 (0x1A0 EPS, 0x1A1 IPB Fren) ve Hyundai Ioniq 5 şasilerine doğrudan 100 Hz senkron tork, çift yedekli fren (i-Booster + ESC/EPB) ve hız komut iletimi. UN R155 CAN-FD siber saldırı tespiti ve <=5 ms sürücü devralma kesmesi.",
      descEn:
        "Native 100 Hz cyclic torque, fail-operational brake (i-Booster + ESC/EPB), and throttle actuation with UN R155 CAN-FD IDPS, 1.4ms latency, and <=5ms human override.",
      spec: "100 Hz CAN-FD • 0x1A0/0x1A1 DBC • 1.4 ms Gecikme • 5 ms Devir",
      badge: "CAN-FD DRIVE-BY-WIRE",
    },
    compute: {
      titleTr: "Donanımdan Bağımsız Otonom Karar Çekirdeği (Horizon J6P / NVIDIA Orin / x86)",
      titleEn: "Hardware-Agnostic Autonomy Core (Horizon J6P / NVIDIA Orin / x86)",
      tagTr: "FRENET LATTICE, MPC, LANELET2 & UN R157 KARA KUTU YAZILIMI",
      tagEn: "FRENET LATTICE, MPC, LANELET2 & UN R157 BLACK-BOX SOFTWARE",
      descTr:
        "Müşteri aracındaki mevcut işlemci (CalmCar Horizon Journey 6P 560 TOPS, NVIDIA Jetson Orin veya endüstriyel x86_64) üzerinde çalışır. Frenet 5. derece kafes planlama, Kayan Ufuklu MPC, Lanelet2 kural motoru ve UN R157 DSSAD kara kutu kaydını yürütür.",
      descEn:
        "Executes on host vehicle compute (CalmCar Horizon J6P, NVIDIA Orin, or x86_64), running Frenet Quintic Lattice planning, Receding-Horizon MPC, Lanelet2 rules, and UN R157 DSSAD logging.",
      spec: "Horizon J6P & Orin Uyumu • Kapalı Kutu (.pyc) SDK • UN R156 SUMS",
      badge: "OTONOM KARAR & KONTROL",
    },
    vision: {
      titleTr: "Çift-Sensör Çapraz Doğrulama (CalmCar + 3D LiDAR) & KVKK Veri Kalkanı",
      titleEn: "Cross-Sensor Validation (CalmCar + 3D LiDAR) & KVKK Data Shield",
      tagTr: "ISO 21448 SOTIF HAKEMİ, eHMI & ACİL DURUM SİREN KORİDORU",
      tagEn: "ISO 21448 SOTIF ARBITER, eHMI & EMERGENCY SIREN CORRIDOR",
      descTr:
        "Araç üzerindeki kamera algı çıktısını (CalmDrive / GMSL2) 3D LiDAR mesafe verisiyle çapraz doğrulayarak gölge/yansıma kaynaklı hayalet frenlemeyi önler. KVKK m.9 yurt dışı veri kalkanı ve ambulans sireni fermuar koridoru içerir.",
      descEn:
        "Cross-validates camera perception with 3D LiDAR depth under ISO 21448 SOTIF to eliminate phantom braking, while enforcing KVKK Art. 9 data isolation and siren corridor formation.",
      spec: "0 Hayalet Frenleme • KVKK m.9 Kalkanı • ISO/TR 23049 eHMI",
      badge: "SOTIF & KVKK HAKEMİ",
    },
    safety: {
      titleTr: "ISO 26262 ASIL-D, IEEE 2846 RSS & ISO 21448 SOTIF Emniyet Hakemi",
      titleEn: "ISO 26262 ASIL-D, IEEE 2846 RSS & ISO 21448 SOTIF Safety Arbiter",
      tagTr: "FONKSİYONEL GÜVENLİK, MRM VE KABİN / BMS EMNİYETİ",
      tagEn: "FUNCTIONAL SAFETY, MRM & CABIN / BMS INTERLOCK",
      descTr:
        "IEEE 2846 RSS matematiksel takip mesafesi, ODD/SOTIF sınır denetçisi, yolcu kapı/kemer/SOS kilidi ve 50 ms Watchdog. İhlal anında 1.5 m/s² kontrollü sağa çekme (MRM), dörtlü flaşör ve 5G/WebRTC Teleoperasyon devri.",
      descEn:
        "IEEE 2846 RSS mathematical safety envelope, ODD/SOTIF supervisor, passenger cabin interlock, and 50ms watchdog triggering 1.5 m/s² MRM pullover and 5G/WebRTC teleoperation.",
      spec: "ISO 26262 ASIL-D • IEEE 2846 RSS • 50 ms Watchdog • 1.5 m/s² MRM",
      badge: "FAILSAFE GÜVENLİK HAKEMİ",
    },
  };

  const current = calloutDetails[activeCalloutId] || calloutDetails.lidar;

  return (
    <section
      id="robotaxi"
      className="hidden md:block relative z-20 pt-20 sm:pt-28 pb-14 sm:pb-20 px-4 sm:px-8 lg:px-12 bg-gradient-to-b from-[#221d16] via-[#2f281f] to-[#252018] text-white select-none overflow-hidden scroll-mt-20 sm:scroll-mt-28 border-b border-[#E5D6BC]/20"
    >
      {/* Soft Ambient Spotlight directly behind 3D MIFA 7 Vehicle */}
      <div className="absolute top-[52%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-[85vw] max-w-[1000px] h-[500px] bg-[radial-gradient(ellipse_at_center,rgba(228,248,13,0.08),transparent_70%)] pointer-events-none blur-3xl z-0" />

      <div className="max-w-7xl mx-auto space-y-6 sm:space-y-8 relative z-10">
        
        {/* ========================================================
            1. PUNCHY EXECUTIVE HEADER (SIFIR KUTU)
           ======================================================== */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-[#E5D6BC]/20">
          <div className="space-y-2.5 max-w-3xl">
            {/* Taktik HUD Başlığı */}
            <div className="inline-flex items-center gap-2 font-mono text-[11px] uppercase tracking-widest text-[#E5D6BC]/80">
              <span className="text-white font-semibold">
                {lang === "tr" ? "SEVİYE-4 ROBOTAKSİ MİMARİSİ" : "LEVEL-4 ROBOTAXI ARCHITECTURE"}
              </span>
              <span className="text-[#E5D6BC]/40">/</span>
              <span className="text-[#E4F80D] font-bold">SAIC MAXUS MIFA 7 &amp; HYUNDAI IONIQ 5</span>
              <span className="text-[#E5D6BC]/40">/</span>
              <span className="text-[#E5D6BC]/70">{lang === "tr" ? "AB 2022/1426 TAM UYUMLU" : "EU 2022/1426 COMPLIANT"}</span>
            </div>

            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-white leading-tight font-sans">
              <span className="block text-white">SAIC Maxus MIFA 7</span>
              <span className="block text-[#E5D6BC] font-light text-lg sm:text-2xl lg:text-3xl mt-1">
                {lang === "tr" ? "Seviye-4 Ticari Robotaksi Mimarisi" : "Level-4 Commercial Robotaxi Architecture"}
              </span>
            </h2>

            <p className="text-[#E5D6BC]/80 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal pt-0.5">
              {lang === "tr"
                ? "Ticari elektrikli yolcu filoları ve kentsel robotaksi operasyonları için geliştirilmiş; 20 uluslararası L4 modülü, 100 Hz senkron CAN-FD aktüatör kontrolü (EPS & i-Booster), 3D LiDAR SLAM, IEEE 2846 RSS ve ISO 26262 ASIL-D deterministik seyrüsefer referans mimarisi."
                : "Deterministic Level-4 autonomy architecture engineered for commercial electric fleets across 20 international L4 modules via 100 Hz CAN-FD drive-by-wire, 3D LiDAR SLAM, and IEEE 2846 RSS."}
            </p>
          </div>

          {/* Action Link (Kutudan arındırılmış temiz buton) */}
          <div className="shrink-0 flex items-center">
            <Link
              href="/robotaxi/"
              className="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-wider px-4 py-2.5 bg-[#E4F80D] text-black font-bold hover:bg-white transition-all shadow-[0_2px_12px_rgba(228,248,13,0.3)] cursor-pointer"
            >
              <span>{lang === "tr" ? "Mühendislik Şartnamesi (20 Modül)" : "Engineering Blueprint (20 Modules)"}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>

        {/* ========================================================
            2. 3D TACTICAL VEHICLE WIREFRAME (100% KUTUSUZ / FRAMELESS)
           ======================================================== */}
        <div className="space-y-4">
          
          {/* Frameless Top Bar: Coordinate Readout & Component Switcher */}
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 pb-3 border-b border-[#E5D6BC]/20">
            <div className="flex items-center gap-2 text-[10px] font-mono tracking-wider text-[#E5D6BC]/80">
              <span className="w-2 h-2 bg-[#E4F80D] animate-pulse" />
              <span className="text-white font-bold">SAIC MAXUS MIFA 7 // 3D ŞASİ TOPOLOJİSİ</span>
              <span className="text-[#E5D6BC]/40 hidden sm:inline">/</span>
              <span className="text-[#E5D6BC]/60 hidden sm:inline">DİNGİL: 2.975mm • UZUNLUK: 4.907mm</span>
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
                        : "text-[#E5D6BC]/60 hover:text-white border-transparent"
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
          <div className="relative w-full h-[360px] xs:h-[420px] sm:h-[500px] lg:h-[580px]">
            <TacticalVehicleWireframe
              activeId={activeCalloutId}
              onSelectCallout={setActiveCalloutId}
              className="w-full h-full"
            />
          </div>

          {/* Frameless Active Specification HUD (Sıfır Kutu, Saf Tipografi) */}
          <div className="pt-4 border-t border-[#E5D6BC]/20 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="space-y-1.5 max-w-2xl">
              <div className="flex items-center gap-2 font-mono text-[10px]">
                <span className="text-[#E4F80D] font-bold">
                  [ {current.badge} ]
                </span>
                <span className="text-[#E5D6BC]/40">/</span>
                <span className="text-[#E5D6BC]/80 uppercase tracking-wider">
                  {lang === "tr" ? current.tagTr : current.tagEn}
                </span>
              </div>
              <div className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? current.titleTr : current.titleEn}
              </div>
              <p className="text-xs text-[#E5D6BC]/85 leading-relaxed font-sans font-normal">
                {lang === "tr" ? current.descTr : current.descEn}
              </p>
            </div>

            <div className="shrink-0 text-left md:text-right font-mono space-y-1 md:pl-6 md:border-l border-[#E5D6BC]/20">
              <span className="text-[10px] text-[#E5D6BC]/60 uppercase tracking-widest block font-medium">
                // DONANIM &amp; EMNİYET METRİĞİ
              </span>
              <div className="text-xs sm:text-[13px] font-bold text-[#E4F80D] tracking-tight">
                {current.spec}
              </div>
              <div className="text-[10px] text-[#E5D6BC]/60">
                UN R155/R156/R157 • IEEE 2846 • ISO 26262 ASIL-D
              </div>
            </div>
          </div>

        </div>

        {/* ========================================================
            3. VERIFIED BENCHMARKS (100% KUTUSUZ / PURE TYPOGRAPHY)
            - 31.400+ LOC (203 Files), 1.324 + 21 Tests, 100 Hz CAN-FD, 5 ms Interrupt
           ======================================================== */}
        <div className="pt-6 border-t border-[#E5D6BC]/20 space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 font-mono text-[11px] text-[#E5D6BC]/70 uppercase tracking-wider">
            <div className="flex items-center gap-2">
              <span className="text-[#E4F80D] font-bold">//</span>
              <span className="text-white font-semibold">{lang === "tr" ? "L4 ROBOTAKSİ SAHA ENTEGRASYON VE DOĞRULAMA KÜTÜĞÜ" : "L4 ROBOTAXI DEPLOYMENT & VERIFICATION LOG"}</span>
            </div>
            <span className="text-[#E4F80D] font-semibold">%100 MİLLİ SEVİYE-4 ÇEKİRDEK &amp; KAPALI KUTU SDK</span>
          </div>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8 font-mono">
            {/* Stat 1 */}
            <div className="space-y-1">
              <span className="text-[10px] text-[#E5D6BC]/60 uppercase tracking-wider block font-semibold">
                YAZILIM ENVANTERİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                31.400+
              </div>
              <span className="text-[11px] text-[#E5D6BC]/70 font-sans block">
                Satır Kod (203 Dosya • 20 L4 Modül)
              </span>
            </div>

            {/* Stat 2 */}
            <div className="space-y-1 sm:border-l border-[#E5D6BC]/20 sm:pl-6">
              <span className="text-[10px] text-[#E5D6BC]/60 uppercase tracking-wider block font-semibold">
                DOĞRULAMA KÜTÜPHANESİ
              </span>
              <div className="text-2xl sm:text-3xl font-black text-[#E4F80D] tracking-tight">
                1.324 + 21
              </div>
              <span className="text-[11px] text-emerald-400 font-sans font-medium block">
                %100 Yeşil Test (0 Hata / 0 Fail)
              </span>
            </div>

            {/* Stat 3 */}
            <div className="space-y-1 border-t sm:border-t-0 sm:border-l border-[#E5D6BC]/20 pt-4 sm:pt-0 sm:pl-6">
              <span className="text-[10px] text-[#E5D6BC]/60 uppercase tracking-wider block font-semibold">
                CAN-FD &amp; UN R155 IDPS
              </span>
              <div className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                100 Hz
              </div>
              <span className="text-[11px] text-[#E5D6BC]/70 font-sans block">
                {lang === "tr" ? "1.4 ms Gecikme (EPS & i-Booster)" : "1.4 ms Latency (EPS & i-Booster)"}
              </span>
            </div>

            {/* Stat 4 */}
            <div className="space-y-1 border-t sm:border-t-0 sm:border-l border-[#E5D6BC]/20 pt-4 sm:pt-0 sm:pl-6">
              <span className="text-[10px] text-[#E5D6BC]/60 uppercase tracking-wider block font-semibold">
                DONANIMSAL KESME
              </span>
              <div className="text-2xl sm:text-3xl font-black text-[#E4F80D] tracking-tight">
                5 ms
              </div>
              <span className="text-[11px] text-[#E5D6BC]/70 font-sans block">
                ASIL-D Devralma &amp; 50 ms Watchdog
              </span>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
