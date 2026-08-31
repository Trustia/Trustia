"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Car,
  Cpu,
  Eye,
  ShieldCheck,
  Zap,
  Activity,
  Layers,
  Radio,
  Download,
  CheckCircle2,
  ChevronRight,
  Gauge,
  Lock,
  ArrowLeft,
  Share2,
  Maximize2
} from "lucide-react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiPage() {
  const { lang } = useLanguage();
  const [selectedPhoto, setSelectedPhoto] = useState(0);

  const photos = [
    {
      src: "/robotaxi/ioniq5_foto_1.png",
      title: lang === "tr" ? "Ön 3/4 Dış Görünüm" : "Front 3/4 Exterior",
      desc: lang === "tr" ? "Hyundai Ioniq 5 2024 Advance E-GMP Platformu" : "Hyundai Ioniq 5 2024 Advance E-GMP Chassis",
      tag: "GENEL BAKIŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_2.png",
      title: lang === "tr" ? "Ön Tampon & Sensör Podu" : "Front Bumper & Sensor Pod",
      desc: lang === "tr" ? "Livox Mid-360 LiDAR ve 77GHz Radar Görüş Açısı" : "Livox Mid-360 LiDAR & 77GHz Radar Coverage",
      tag: "LİDAR & RADAR"
    },
    {
      src: "/robotaxi/ioniq5_foto_3.png",
      title: lang === "tr" ? "Yan Profil & Dingil Mesafesi" : "Side Profile & Wheelbase",
      desc: lang === "tr" ? "3.000 mm Dingil Mesafesi ve Tavan Barı Hizalaması" : "3,000 mm Wheelbase & Roof Rack Alignment",
      tag: "ŞASİ & MEKANİK"
    },
    {
      src: "/robotaxi/ioniq5_foto_4.png",
      title: lang === "tr" ? "Arka Çapraz Görünüm" : "Rear 3/4 Exterior",
      desc: lang === "tr" ? "Arka Spoyler Altı IP68 Kablo Geçiş Körüğü" : "Rear Spoiler IP68 Tailgate Cable Entry",
      tag: "IP68 YALITIM"
    },
    {
      src: "/robotaxi/ioniq5_foto_5.png",
      title: lang === "tr" ? "Arka Düz Görünüm" : "Rear Straight View",
      desc: lang === "tr" ? "Geri Görüş HDR Kamerası ve Park Sensörleri" : "Rear HDR Vision & Ultrasonic Park Array",
      tag: "360° GÖRÜŞ"
    },
    {
      src: "/robotaxi/ioniq5_foto_6.png",
      title: lang === "tr" ? "Ön Kokpit & Taktik C2" : "Front Cockpit & C2 Display",
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
      sub: "120 dB Dinamik Aralık • IP67 • Sıfır Gecikme"
    },
    {
      icon: Gauge,
      title: lang === "tr" ? "Kötü Hava Radarı" : "All-Weather Radar",
      val: "2x Continental ARS 408-21 77GHz",
      sub: "250m Menzil • Sis, Şiddetli Yağmur & Kar Kalkanı"
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

  return (
    <main className="relative min-h-screen bg-[#07090d] text-white font-sans selection:bg-[#C8FF00] selection:text-black overflow-x-hidden pt-20 sm:pt-24 pb-16">
      <Navbar />

      {/* Background Ambience */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-[600px] bg-radial from-[#0284C7]/15 via-transparent to-transparent pointer-events-none blur-3xl -z-10" />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-12 sm:space-y-16">

        {/* 1. TOP BREADCRUMB & HEADER */}
        <div className="space-y-4">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-[#C8FF00] flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-[#C8FF00] font-bold">ROBOTAXI</span>
          </div>

          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-white/10">
            <div className="space-y-2 max-w-3xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-xs font-mono font-bold tracking-wider uppercase">
                <span className="w-2 h-2 rounded-full bg-[#C8FF00] animate-ping" />
                <span>{lang === "tr" ? "SEVİYE 4 YERLİ ROBOTAKSİ PLATFORMU" : "LEVEL 4 SOVEREIGN ROBOTAXI PLATFORM"}</span>
              </div>
              <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-[1.15]">
                Hyundai Ioniq 5 (E-GMP) <br />
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-[#C8FF00]">
                  {lang === "tr" ? "Seviye-4 Otonom Sürüş Mimarisi" : "Level-4 Autonomous Mobility Core"}
                </span>
              </h1>
              <p className="text-slate-400 text-sm sm:text-base leading-relaxed">
                {lang === "tr"
                  ? "128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış, 16.000 satır deterministik yerli otonomi çekirdeği."
                  : "Engineered with 128-channel 3D LiDAR, 4x GMSL2 HDR vision, 77GHz radar, and 100 Hz CAN-FD drive-by-wire over 16,000 lines of deterministic autonomy software."}
              </p>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <a
                href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
                download
                className="px-4 py-2.5 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_20px_rgba(200,255,0,0.5)] transition-all cursor-pointer"
              >
                <Download className="w-4 h-4" />
                <span>{lang === "tr" ? "PDF ŞARTNAMEYİ İNDİR (5 SAYFA)" : "DOWNLOAD MASTER PDF (5 PAGES)"}</span>
              </a>
              <Link
                href="/iletisim/"
                className="px-4 py-2.5 rounded-xl bg-white/5 border border-white/15 text-white font-mono font-bold text-xs tracking-wider uppercase hover:bg-white/10 transition-all flex items-center gap-2"
              >
                <span>{lang === "tr" ? "İŞ BİRLİĞİ TALEBİ" : "PARTNERSHIP"}</span>
                <ChevronRight className="w-4 h-4" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. FOUR KPI STATS CARDS */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <div className="p-5 sm:p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1 relative overflow-hidden group hover:border-[#C8FF00]/40 transition-colors">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "OTONOMİ ÇEKİRDEĞİ" : "AUTONOMY STACK"}</div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">16.000+</div>
            <div className="text-xs text-[#C8FF00] font-mono font-medium">{lang === "tr" ? "%100 Özgün C++/Python" : "100% Sovereign Codebase"}</div>
          </div>

          <div className="p-5 sm:p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1 relative overflow-hidden group hover:border-[#C8FF00]/40 transition-colors">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "BİRİM & SİSTEM TESTİ" : "AUTOMATED TESTS"}</div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">1.301 / 1.301</div>
            <div className="text-xs text-emerald-400 font-mono font-medium">{lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate (0 Errors)"}</div>
          </div>

          <div className="p-5 sm:p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1 relative overflow-hidden group hover:border-[#C8FF00]/40 transition-colors">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "MERKEZİ HESAPLAMA" : "COMPUTE POWER"}</div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">275 TOPS</div>
            <div className="text-xs text-sky-400 font-mono font-medium">NVIDIA Jetson AGX Orin</div>
          </div>

          <div className="p-5 sm:p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-1 relative overflow-hidden group hover:border-[#C8FF00]/40 transition-colors">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">{lang === "tr" ? "ALGILAMA MENZİLİ" : "PERCEPTION RANGE"}</div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white">240 Metre</div>
            <div className="text-xs text-purple-400 font-mono font-medium">128 Kanal 3D LiDAR SLAM</div>
          </div>
        </div>

        {/* 3. INTERACTIVE 7-PHOTO CAROUSEL & SHOWCASE */}
        <div className="space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2">
            <div>
              <div className="text-xs font-mono text-[#C8FF00] font-bold tracking-wider uppercase">
                {lang === "tr" ? "FİZİKSEL TEST ARACI" : "PHYSICAL TEST PLATFORM"}
              </div>
              <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                {lang === "tr" ? "Hyundai Ioniq 5 Test Aracı Galerisi" : "Hyundai Ioniq 5 Fleet Gallery"}
              </h2>
            </div>
            <div className="text-xs font-mono text-slate-400">
              {lang === "tr" ? "Görsel seçmek için aşağıdaki küçük resimlere tıklayın" : "Click thumbnails to inspect sensor locations"}
            </div>
          </div>

          {/* Main Large Photo Display */}
          <div className="relative rounded-3xl overflow-hidden border border-white/15 bg-[#0a0d13] shadow-2xl aspect-[16/9] sm:aspect-[21/9] max-h-[560px] group">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={photos[selectedPhoto].src}
              alt={photos[selectedPhoto].title}
              className="w-full h-full object-cover transition-all duration-700 group-hover:scale-[1.02]"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent pointer-events-none" />

            {/* Photo Metadata Overlay */}
            <div className="absolute bottom-6 left-6 right-6 flex flex-col sm:flex-row sm:items-end justify-between gap-4">
              <div className="space-y-1">
                <span className="px-2.5 py-0.5 rounded bg-[#C8FF00] text-black font-mono font-black text-[10px] uppercase tracking-wider inline-block">
                  {photos[selectedPhoto].tag}
                </span>
                <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
                  {photos[selectedPhoto].title}
                </h3>
                <p className="text-slate-300 text-xs sm:text-sm max-w-xl">
                  {photos[selectedPhoto].desc}
                </p>
              </div>

              <div className="text-xs font-mono text-slate-400 shrink-0">
                {selectedPhoto + 1} / {photos.length}
              </div>
            </div>
          </div>

          {/* Thumbnails Row */}
          <div className="grid grid-cols-4 sm:grid-cols-7 gap-2.5 sm:gap-3">
            {photos.map((p, i) => (
              <button
                key={i}
                onClick={() => setSelectedPhoto(i)}
                className={`relative rounded-xl overflow-hidden aspect-[4/3] border transition-all duration-300 cursor-pointer ${
                  selectedPhoto === i
                    ? "border-[#C8FF00] ring-2 ring-[#C8FF00]/50 scale-[1.03] shadow-lg"
                    : "border-white/10 opacity-60 hover:opacity-100 hover:border-white/30"
                }`}
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={p.src} alt={p.title} className="w-full h-full object-cover" />
                <span className="absolute bottom-1 right-1 px-1.5 py-0.5 rounded bg-black/80 text-[8px] font-mono text-white font-bold">
                  0{i + 1}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* 4. TURNKEY HARDWARE & SENSOR MATRIX */}
        <div className="space-y-6">
          <div>
            <div className="text-xs font-mono text-[#C8FF00] font-bold tracking-wider uppercase">
              {lang === "tr" ? "DONANIM VE SENSÖR FÜZYONU" : "HARDWARE & SENSOR FUSION"}
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              {lang === "tr" ? "27 Parçalık Tam Teşekküllü Seviye 4 Kiti" : "27-Item Level-4 Turnkey Sensor Suite"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
            {specs.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div
                  key={idx}
                  className="p-5 rounded-2xl bg-[#0b0e14] border border-white/10 hover:border-[#0284C7]/50 transition-all duration-300 space-y-3 group"
                >
                  <div className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 group-hover:text-[#C8FF00] group-hover:border-[#C8FF00]/40 transition-colors">
                    <Icon className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                      {item.title}
                    </div>
                    <div className="text-sm font-bold text-white mt-0.5 leading-snug">
                      {item.val}
                    </div>
                    <div className="text-[11px] text-slate-400 font-light mt-1">
                      {item.sub}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. ARCHITECTURE & SAFETY PROTOCOLS */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          {/* E-GMP & CAN-FD Integration */}
          <div className="p-7 sm:p-8 rounded-3xl bg-[#0a0d13] border border-white/10 space-y-5">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-sky-400 text-xs font-mono font-bold tracking-wider uppercase">
              <Zap className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "E-GMP CAN-FD MİMARİSİ" : "E-GMP CAN-FD ARCHITECTURE"}</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Sıfır Delme & Tak-Çalıştır Entegrasyon" : "Zero-Drill & Plug-and-Play Integration"}
            </h3>
            <ul className="space-y-3.5 text-xs sm:text-sm text-slate-300 font-normal">
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "Dikiz Aynası ADAS Y-Harness:" : "Rearview ADAS Y-Harness:"}</b>{" "}
                  {lang === "tr"
                    ? "OBD-II gateway engeline takılmadan, doğrudan şasi CAN-FD hattına 100 Hz direksiyon (LKAS11) ve 50 Hz fren/gaz (SCC_FD) sinyali enjekte edilir."
                    : "Injects 100 Hz steering (LKAS11) and 50 Hz brake/accel (SCC_FD) directly into the chassis CAN-FD bus without gateway interference."}
                </span>
              </li>
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "57 Litrelik Sub-Trunk Hesaplama Havuzu:" : "57-Liter Sub-Trunk Compute Hub:"}</b>{" "}
                  {lang === "tr"
                    ? "Jetson Orin, sigorta panosu, 5G router ve regülatör bagaj altı havuzuna yerleştirilir; dışarıdan araç %100 orijinal görünür."
                    : "Jetson Orin, fuse box, 5G router, and DC-DC regulator fit discreetly in the sub-trunk under the stock cargo floor."}
                </span>
              </li>
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "IP68 No-Drill Tavan Geçişi:" : "IP68 Zero-Penetration Roof Routing:"}</b>{" "}
                  {lang === "tr"
                    ? "Araç kaportası delinmez; kablo demeti arka spoyler altındaki fabrikasyon kauçuk körükten sub-trunk'a iner."
                    : "Zero sheet-metal drilling; cables route through OEM tailgate rubber boots sealed with IP68 waterproof junction units."}
                </span>
              </li>
            </ul>
          </div>

          {/* Safety & Takeover Standards */}
          <div className="p-7 sm:p-8 rounded-3xl bg-[#0a0d13] border border-white/10 space-y-5">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono font-bold tracking-wider uppercase">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "GÜVENLİK & SÜRÜCÜ MÜDAHALESİ" : "SAFETY & TAKEOVER PROTOCOLS"}</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "5ms Sürücü Devralma & 5G GPS Çit" : "5ms Driver Override & 5G Geofencing"}
            </h3>
            <ul className="space-y-3.5 text-xs sm:text-sm text-slate-300 font-normal">
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "Anlık Sürücü Müdahalesi (5ms):" : "Instant Human Takeover (5ms):"}</b>{" "}
                  {lang === "tr"
                    ? "Direksiyon 2.0 Nm torkla çevrildiğinde veya frene 1mm basıldığında otonomi 5 milisaniyede kontrolü insana bırakır (ISO 26262 ASIL-D)."
                    : "Steering torque >2.0 Nm or brake pedal depression instantly disengages autonomy within 5ms under ISO 26262 ASIL-D."}
                </span>
              </li>
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "200ms Watchdog & Minimum Risk Manevrası (MRM):" : "200ms Watchdog & MRM Fail-Safe:"}</b>{" "}
                  {lang === "tr"
                    ? "Sensör veya bilgisayar takılırsa flaşörler yanar, araç şeridinde yumuşakça durur ve Samsung 4TB SSD kara kutu kaydı tutar."
                    : "In event of sensor stall, hazard lights activate, the vehicle softly stops within lane, and 4TB NVMe SSD logs black-box telemetry."}
                </span>
              </li>
              <li className="flex items-start gap-3">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span>
                  <b>{lang === "tr" ? "5G GPS Sanal Çit & Uzaktan İmmobilizer:" : "5G GPS Geofencing & Remote Kill:"}</b>{" "}
                  {lang === "tr"
                    ? "Test sahası (BTM veya Bilişim Vadisi) dışına çıkılırsa motor uzaktan kilitlenir; 7/24 teleoperasyon C2 ile yönetilir."
                    : "Vehicle locks motor if exiting authorized proving ground perimeter; managed 24/7 via tactical desktop C2."}
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* 6. FOUR STAGE FIELD TRIAL ROADMAP */}
        <div className="p-8 sm:p-10 rounded-3xl bg-[#0c1017] border border-white/10 space-y-6">
          <div className="text-center max-w-2xl mx-auto space-y-2">
            <div className="text-xs font-mono text-[#C8FF00] font-bold tracking-wider uppercase">
              {lang === "tr" ? "SAHA TEST YOL HARİTASI" : "PROVING GROUND TESTING ROADMAP"}
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              {lang === "tr" ? "4 Kademeli Güvenlik ve İzin Süreci" : "4-Stage Safe Deployment Process"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 pt-4">
            <div className="p-5 rounded-2xl bg-black/40 border border-white/10 space-y-2">
              <div className="text-[10px] font-mono text-[#C8FF00] font-bold uppercase">AŞAMA 1 // SİMÜLASYON</div>
              <div className="text-sm font-bold text-white">Webots 3D Dijital İkiz</div>
              <div className="text-xs text-slate-400 font-light leading-relaxed">
                1.301 birim test, SLAM haritalama, Pure Pursuit rota takibi.
              </div>
              <div className="text-[10px] font-mono text-emerald-400 font-bold pt-1">✅ %100 TAMAMLANDI</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/10 space-y-2">
              <div className="text-[10px] font-mono text-sky-400 font-bold uppercase">AŞAMA 2 // KAPALI PİST</div>
              <div className="text-sm font-bold text-white">Bilişim Vadisi Gebze</div>
              <div className="text-xs text-slate-400 font-light leading-relaxed">
                1.5 km asfalt parkur, cansız mankenler, yapay kavşaklar, dur-kalk akışı.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-bold pt-1">Sıfır Riskli Parkur</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/10 space-y-2">
              <div className="text-[10px] font-mono text-purple-400 font-bold uppercase">AŞAMA 3 // KAMPÜS</div>
              <div className="text-sm font-bold text-white">İTO BTM Fulya Kampüs</div>
              <div className="text-xs text-slate-400 font-light leading-relaxed">
                Kapalı yerleşkede 20-30 km/s hızla otonom yolcu alma ve bırakma.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-bold pt-1">BTM Özel Alan İzni</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/10 space-y-2">
              <div className="text-[10px] font-mono text-amber-400 font-bold uppercase">AŞAMA 4 // AÇIK YOL</div>
              <div className="text-sm font-bold text-white">Şehir İçi Pilot Hat</div>
              <div className="text-xs text-slate-400 font-light leading-relaxed">
                Koltukta emniyet sürücüsü eşliğinde karma trafikte Seviye 4 sürüş.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-bold pt-1">Sanayi Bak. & T Plaka</div>
            </div>
          </div>
        </div>

        {/* 7. BOTTOM CTA & OFFICIAL PDF DOWNLOAD CARD */}
        <div className="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-[#0a192f] via-[#0d1f38] to-[#070b12] border border-[#0284C7]/40 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="space-y-3 text-center md:text-left max-w-2xl">
            <span className="px-3 py-1 rounded-full bg-[#C8FF00]/15 text-[#C8FF00] border border-[#C8FF00]/30 font-mono text-xs font-bold uppercase tracking-wider inline-block">
              {lang === "tr" ? "RESMİ YATIRIMCI VE MÜHENDİSLİK DOKÜMANI" : "OFFICIAL INVESTOR & ENGINEERING DOCUMENT"}
            </span>
            <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              {lang === "tr" ? "5 Sayfalık Master Dönüşüm Şartnamesini İnceleyin" : "Download the 5-Page Turnkey Engineering Specification"}
            </h3>
            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed">
              {lang === "tr"
                ? "27 parçalık doğrulanmış parça listesi, tavan barı montajı, dikiz aynası CAN-FD kablo bağlantıları, CharuCo kalibrasyonu ve güvenlik protokollerini içeren resmi PDF şartname."
                : "Complete 27-item verified BOM table, roof rack mounting geometry, CAN-FD wire harness pins, CharuCo extrinsic calibration, and safety watchdog protocols."}
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-3 shrink-0">
            <a
              href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
              download
              className="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center justify-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.6)] transition-all cursor-pointer"
            >
              <Download className="w-4 h-4" />
              <span>{lang === "tr" ? "PDF'İ İNDİR (A4 ÇIKTI UYUMLU)" : "DOWNLOAD PDF"}</span>
            </a>
          </div>
        </div>

      </div>

      <Footer />
    </main>
  );
}
