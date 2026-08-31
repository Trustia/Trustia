"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Cpu,
  Eye,
  Layers,
  Radio,
  Download,
  CheckCircle2,
  ChevronRight,
  Gauge,
  Lock,
  ArrowLeft,
  Zap,
  ShieldCheck,
  Activity
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
      title: lang === "tr" ? "Ön Çeyrek Dış Görünüm" : "Front 3/4 Exterior",
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
      title: lang === "tr" ? "Arka Çeyrek Görünüm" : "Rear 3/4 Exterior",
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
      title: lang === "tr" ? "Ön Kokpit & Telemetri Konsolu" : "Cockpit & Telemetry Console",
      desc: lang === "tr" ? "10.1\" IPS Dokunmatik Harita ve Schneider E-Stop Butonu" : "10.1\" Touch C2 Map & Schneider E-Stop",
      tag: "KOKPİT C2"
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

  return (
    <main className="relative min-h-screen bg-[#07090d] text-white font-sans selection:bg-slate-700 selection:text-white overflow-x-hidden pt-20 sm:pt-24 pb-16">
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-12 sm:space-y-14">

        {/* 1. Breadcrumb & Header */}
        <div className="space-y-4">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-white flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-slate-200 font-semibold">ROBOTAXI</span>
          </div>

          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b border-white/10">
            <div className="space-y-2.5 max-w-3xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-slate-800/80 border border-slate-700 text-slate-300 text-xs font-mono font-medium tracking-wider uppercase">
                <span>{lang === "tr" ? "SEVİYE 4 OTONOM SÜRÜŞ PLATFORMU" : "LEVEL 4 AUTONOMOUS PLATFORM"}</span>
              </div>
              
              <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold text-white tracking-tight leading-[1.15]">
                Hyundai Ioniq 5 (E-GMP) <br />
                <span className="text-slate-300 font-semibold">
                  {lang === "tr" ? "Seviye-4 Otonom Sürüş Mimarisi" : "Level-4 Autonomous Fleet Architecture"}
                </span>
              </h1>
              
              <p className="text-slate-400 text-sm sm:text-base leading-relaxed">
                {lang === "tr"
                  ? "128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış; 16.000 satır özgün deterministik otonomi çekirdeği."
                  : "Configured with 128-channel 3D LiDAR, 4x GMSL2 HDR cameras, 77GHz radar, and 100 Hz CAN-FD drive-by-wire across 16,000 lines of sovereign autonomy software."}
              </p>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <Link
                href="/iletisim/"
                className="px-5 py-2.5 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-2"
              >
                <span>{lang === "tr" ? "RESMİ ŞARTNAME VE İŞ BİRLİĞİ TALEBİ" : "ENTERPRISE SPEC & PARTNERSHIP"}</span>
                <ChevronRight className="w-4 h-4" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. Four KPI Metric Cards */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "YAZILIM ÇEKİRDEĞİ" : "AUTONOMY STACK"}
            </div>
            <div className="text-2xl sm:text-3xl font-bold text-white">16.000+</div>
            <div className="text-xs text-slate-400 font-medium">
              {lang === "tr" ? "Satır Özgün C++ / Python" : "Lines of Sovereign Code"}
            </div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "BİRİM & ENTEGRASYON TESTİ" : "AUTOMATED TESTS"}
            </div>
            <div className="text-2xl sm:text-3xl font-bold text-white">1.301 / 1.301</div>
            <div className="text-xs text-emerald-400 font-medium">
              {lang === "tr" ? "%100 Başarı (0 Hata)" : "100% Pass Rate (0 Errors)"}
            </div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "MERKEZİ HESAPLAMA" : "COMPUTE POWER"}
            </div>
            <div className="text-2xl sm:text-3xl font-bold text-white">275 TOPS</div>
            <div className="text-xs text-slate-400 font-medium">NVIDIA Jetson AGX Orin</div>
          </div>

          <div className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 space-y-1">
            <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider">
              {lang === "tr" ? "ALGILAMA MENZİLİ" : "PERCEPTION RANGE"}
            </div>
            <div className="text-2xl sm:text-3xl font-bold text-white">240 Metre</div>
            <div className="text-xs text-slate-400 font-medium">128 Kanal 3D LiDAR SLAM</div>
          </div>
        </div>

        {/* 3. Photo Gallery */}
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2">
            <div>
              <div className="text-xs font-mono text-slate-400 font-semibold tracking-wider uppercase">
                {lang === "tr" ? "FİZİKSEL TEST PLATFORMU" : "PHYSICAL TEST PLATFORM"}
              </div>
              <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
                {lang === "tr" ? "Hyundai Ioniq 5 Test Aracı Donanım Yerleşimi" : "Hyundai Ioniq 5 Hardware Layout"}
              </h2>
            </div>
            <div className="text-xs font-mono text-slate-400">
              {lang === "tr" ? "Görselleri incelemek için küçük resimlere tıklayın" : "Click thumbnails to inspect sensor locations"}
            </div>
          </div>

          {/* Main Photo Frame */}
          <div className="relative rounded-2xl overflow-hidden border border-slate-800 bg-[#0c1017] aspect-[16/9] sm:aspect-[21/9] max-h-[560px] group">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={photos[selectedPhoto].src}
              alt={photos[selectedPhoto].title}
              className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.01]"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent pointer-events-none" />

            {/* Photo Caption Overlay */}
            <div className="absolute bottom-5 left-5 right-5 flex flex-col sm:flex-row sm:items-end justify-between gap-3">
              <div className="space-y-1">
                <span className="px-2 py-0.5 rounded bg-slate-900/90 border border-slate-700 text-slate-300 font-mono text-[10px] uppercase tracking-wider inline-block">
                  {photos[selectedPhoto].tag}
                </span>
                <h3 className="text-lg sm:text-xl font-bold text-white">
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
          <div className="grid grid-cols-4 sm:grid-cols-7 gap-2.5">
            {photos.map((p, i) => (
              <button
                key={i}
                onClick={() => setSelectedPhoto(i)}
                className={`relative rounded-lg overflow-hidden aspect-[4/3] border transition-all duration-200 cursor-pointer ${
                  selectedPhoto === i
                    ? "border-white ring-1 ring-white/60"
                    : "border-slate-800 opacity-60 hover:opacity-100"
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

        {/* 4. Turnkey Sensor & Hardware Matrix */}
        <div className="space-y-4">
          <div>
            <div className="text-xs font-mono text-slate-400 font-semibold tracking-wider uppercase">
              {lang === "tr" ? "DONANIM VE SENSÖR MİMARİSİ" : "HARDWARE & SENSOR FUSION"}
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "27 Parçalık Tam Teşekküllü Seviye 4 Donanım Seti" : "27-Item Level-4 Turnkey Sensor Suite"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {specs.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div
                  key={idx}
                  className="p-5 rounded-xl bg-[#0f131a] border border-slate-800 hover:border-slate-700 transition-colors space-y-3"
                >
                  <div className="w-9 h-9 rounded-lg bg-slate-800/60 border border-slate-700 flex items-center justify-center text-slate-300">
                    <Icon className="w-4 h-4" />
                  </div>
                  <div>
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                      {item.title}
                    </div>
                    <div className="text-sm font-bold text-white mt-0.5 leading-snug">
                      {item.val}
                    </div>
                    <div className="text-[11px] text-slate-400 mt-1 leading-normal">
                      {item.sub}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. Architecture & Safety Protocols */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* E-GMP & CAN-FD Integration */}
          <div className="p-6 sm:p-7 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-slate-800/80 border border-slate-700 text-slate-300 text-xs font-mono font-medium tracking-wider uppercase">
              <Zap className="w-3.5 h-3.5 text-slate-400" />
              <span>{lang === "tr" ? "E-GMP CAN-FD ENTEGRASYONU" : "E-GMP CAN-FD ARCHITECTURE"}</span>
            </div>
            
            <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Sıfır Delme & Tak-Çalıştır Şasi Uyumu" : "Zero-Drill & Plug-and-Play Integration"}
            </h3>

            <ul className="space-y-3 text-xs sm:text-sm text-slate-300">
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "Dikiz Aynası ADAS Y-Harness:" : "Rearview ADAS Y-Harness:"}</b>{" "}
                  {lang === "tr"
                    ? "OBD-II gateway kısıtlamasına takılmadan şasi CAN-FD hattına 100 Hz direksiyon (LKAS11) ve 50 Hz fren/gaz (SCC_FD) sinyali iletilir."
                    : "Transmits 100 Hz steering (LKAS11) and 50 Hz brake/accel (SCC_FD) directly into chassis CAN-FD without gateway latency."}
                </span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "57 Litrelik Sub-Trunk Hesaplama Havuzu:" : "57-Liter Sub-Trunk Compute Hub:"}</b>{" "}
                  {lang === "tr"
                    ? "Jetson Orin, sigorta panosu, 5G router ve DC-DC regülatör bagaj altı havuzuna yerleştirilir; iç mekan düzeni korunur."
                    : "Jetson Orin, fuse box, 5G router, and DC-DC regulator fit discreetly in the sub-trunk compartment."}
                </span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "IP68 No-Drill Tavan Geçişi:" : "IP68 Zero-Penetration Roof Routing:"}</b>{" "}
                  {lang === "tr"
                    ? "Araç kaportası delinmez; kablo demeti arka spoyler altındaki fabrikasyon kauçuk körükten sub-trunk'a iner."
                    : "Zero sheet-metal drilling; cables route through OEM tailgate rubber boots sealed with IP68 junction hardware."}
                </span>
              </li>
            </ul>
          </div>

          {/* Safety & Human Takeover */}
          <div className="p-6 sm:p-7 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-slate-800/80 border border-slate-700 text-slate-300 text-xs font-mono font-medium tracking-wider uppercase">
              <ShieldCheck className="w-3.5 h-3.5 text-slate-400" />
              <span>{lang === "tr" ? "GÜVENLİK VE DEVİR PROTOKOLLERİ" : "SAFETY & TAKEOVER PROTOCOLS"}</span>
            </div>

            <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight">
              {lang === "tr" ? "5ms Sürücü Devralma ve Güvenli Durma" : "5ms Driver Override & Fail-Safe"}
            </h3>

            <ul className="space-y-3 text-xs sm:text-sm text-slate-300">
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "Anlık Sürücü Müdahalesi (5ms):" : "Instant Human Takeover (5ms):"}</b>{" "}
                  {lang === "tr"
                    ? "Direksiyona tork uygulandığında veya fren pedalına basıldığında otonomi 5 milisaniyede kontrolü sürücüye bırakır (ISO 26262 ASIL-D)."
                    : "Manual steering torque or brake depression instantly disengages autonomy within 5ms under ISO 26262 ASIL-D."}
                </span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "200ms Watchdog & Minimum Risk Manevrası:" : "200ms Watchdog & MRM Fail-Safe:"}</b>{" "}
                  {lang === "tr"
                    ? "Herhangi bir donanım gecikmesinde flaşörler açılır, araç şeridinde kontrollü durur ve 4TB SSD kara kutu kaydı alır."
                    : "On sensor stall, hazard lights engage, the vehicle safely stops within lane, and 4TB NVMe SSD logs telemetry."}
                </span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white">{lang === "tr" ? "5G GPS Coğrafi Çit (Geofence):" : "5G GPS Geofencing & Remote Kill:"}</b>{" "}
                  {lang === "tr"
                    ? "Test sahası (BTM veya Bilişim Vadisi) dışına çıkış halinde motor kilitlenir; 7/24 teleoperasyon C2 ile yönetilir."
                    : "Vehicle locks drive if exiting authorized test perimeter; monitored 24/7 via tactical desktop C2."}
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* 6. Four-Stage Proving Ground Plan */}
        <div className="p-6 sm:p-8 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-5">
          <div className="text-center max-w-2xl mx-auto space-y-1.5">
            <div className="text-xs font-mono text-slate-400 uppercase tracking-wider font-semibold">
              {lang === "tr" ? "SAHA TEST YOL HARİTASI" : "DEPLOYMENT ROADMAP"}
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              {lang === "tr" ? "4 Kademeli Test ve İzin Protokolü" : "4-Stage Safe Deployment Process"}
            </h2>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
            <div className="p-4 rounded-xl bg-[#0b0e14] border border-slate-800 space-y-1.5">
              <div className="text-[10px] font-mono text-slate-400 font-bold uppercase">AŞAMA 1 // SİMÜLASYON</div>
              <div className="text-sm font-bold text-white">Webots 3D Dijital İkiz</div>
              <div className="text-xs text-slate-400 leading-relaxed">
                1.301 birim test, SLAM haritalama, Pure Pursuit rota takibi.
              </div>
              <div className="text-[10px] font-mono text-emerald-400 font-semibold pt-1">✅ %100 Doğrulandı</div>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-slate-800 space-y-1.5">
              <div className="text-[10px] font-mono text-slate-400 font-bold uppercase">AŞAMA 2 // KAPALI PİST</div>
              <div className="text-sm font-bold text-white">Bilişim Vadisi Gebze</div>
              <div className="text-xs text-slate-400 leading-relaxed">
                1.5 km asfalt parkur, cansız mankenler, yapay kavşak ve dur-kalk akışı.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-medium pt-1">Sıfır Riskli Parkur</div>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-slate-800 space-y-1.5">
              <div className="text-[10px] font-mono text-slate-400 font-bold uppercase">AŞAMA 3 // KAMPÜS</div>
              <div className="text-sm font-bold text-white">İTO BTM Fulya Kampüs</div>
              <div className="text-xs text-slate-400 leading-relaxed">
                Kapalı yerleşkede 20-30 km/s hızla otonom yolcu alma ve bırakma.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-medium pt-1">BTM Özel Alan İzni</div>
            </div>

            <div className="p-4 rounded-xl bg-[#0b0e14] border border-slate-800 space-y-1.5">
              <div className="text-[10px] font-mono text-slate-400 font-bold uppercase">AŞAMA 4 // AÇIK YOL</div>
              <div className="text-sm font-bold text-white">Şehir İçi Pilot Hat</div>
              <div className="text-xs text-slate-400 leading-relaxed">
                Koltukta emniyet sürücüsü eşliğinde karma trafikte Seviye 4 sürüş.
              </div>
              <div className="text-[10px] font-mono text-slate-400 font-medium pt-1">Sanayi Bak. & T Plaka</div>
            </div>
          </div>
        </div>

        {/* 7. Bottom Master PDF Download Card */}
        <div className="p-6 sm:p-8 rounded-2xl bg-[#0f131a] border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="space-y-2 text-center md:text-left max-w-2xl">
            <span className="px-2.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300 font-mono text-xs uppercase tracking-wider inline-block">
              {lang === "tr" ? "RESMİ MÜHENDİSLİK DOKÜMANI" : "OFFICIAL ENGINEERING SPECIFICATION"}
            </span>
            <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "5 Sayfalık Master Dönüşüm Şartnamesi" : "5-Page Master Engineering Specification"}
            </h3>
            <p className="text-slate-400 text-xs sm:text-sm leading-relaxed">
              {lang === "tr"
                ? "27 parçalık doğrulanmış donanım listesi, tavan barı montaj geometrisi, dikiz aynası CAN-FD kablo şeması, CharuCo kalibrasyonu ve güvenlik protokolleri."
                : "Complete 27-item verified BOM table, roof rack mounting geometry, CAN-FD wire harness pins, CharuCo extrinsic calibration, and safety watchdog protocols."}
            </p>
          </div>

          <a
            href="/06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
            download
            className="w-full sm:w-auto px-5 py-3 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-2 shrink-0"
          >
            <Download className="w-4 h-4" />
            <span>{lang === "tr" ? "PDF ŞARTNAMEYİ İNDİR" : "DOWNLOAD PDF"}</span>
          </a>
        </div>

      </div>

      <Footer />
    </main>
  );
}
