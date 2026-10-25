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
    <main className="relative min-h-screen bg-[#07090d] text-white font-sans selection:bg-slate-700 selection:text-white overflow-x-hidden pt-20 sm:pt-28 pb-12">
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-6 sm:space-y-8">

        {/* 1. Breadcrumb & Header */}
        <div className="space-y-2.5">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-white flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-slate-200 font-semibold">ROBOTAXI</span>
          </div>

          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-4 pb-4 border-b border-white/10">
            <div className="space-y-1.5 max-w-3xl">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-slate-300 text-[10px] font-mono tracking-wider uppercase">
                <span>{lang === "tr" ? "SEVİYE 4 OTONOM SÜRÜŞ PLATFORMU" : "LEVEL 4 AUTONOMOUS PLATFORM"}</span>
              </div>
              
              <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug">
                Hyundai Ioniq 5 (E-GMP){" "}
                <span className="text-slate-300 font-normal">
                  {lang === "tr" ? "— Seviye-4 Otonom Sürüş Mimarisi" : "— Level-4 Autonomous Fleet Architecture"}
                </span>
              </h1>
              
              <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
                {lang === "tr"
                  ? "128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar ve 100 Hz CAN-FD aktüatör köprüsü ile donatılmış; 16.000 satır özgün deterministik otonomi çekirdeği."
                  : "Configured with 128-channel 3D LiDAR, 4x GMSL2 HDR cameras, 77GHz radar, and 100 Hz CAN-FD drive-by-wire across 16,000 lines of sovereign autonomy software."}
              </p>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <Link
                href="/iletisim/"
                className="px-4 py-2 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-1.5"
              >
                <span>{lang === "tr" ? "Şartname ve Talep" : "Enterprise Spec"}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
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
              {lang === "tr" ? "MERKEZİ HESAPLAMA" : "COMPUTE POWER"}
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

        {/* 3. Photo Gallery */}
        <div className="space-y-3 pt-2">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-white/10">
            <div>
              <div className="text-[10px] font-mono text-slate-400 font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "FİZİKSEL TEST PLATFORMU" : "PHYSICAL TEST PLATFORM"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "Hyundai Ioniq 5 Donanım Yerleşimi" : "Hyundai Ioniq 5 Hardware Layout"}
              </h2>
            </div>
            <div className="text-[10px] font-mono text-slate-400">
              {lang === "tr" ? "Detayları görmek için panellere tıklayın" : "Click labels to inspect locations"}
            </div>
          </div>

          {/* Main Photo Frame */}
          <div className="relative rounded-xl overflow-hidden border border-white/10 bg-[#0a0d13] aspect-[16/9] sm:aspect-[21/9] max-h-[500px] group">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={photos[selectedPhoto].src}
              alt={photos[selectedPhoto].title}
              className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.01]"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-black/60 pointer-events-none" />

            {/* Top Tag */}
            <div className="absolute top-3 left-3 right-3 flex items-center justify-between text-[10px] font-mono">
              <span className="px-2 py-0.5 rounded bg-black/70 border border-white/15 text-slate-300 backdrop-blur-md">
                E-GMP // 3.000 mm DİNGİL MESAFESİ
              </span>
              <span className="px-2 py-0.5 rounded bg-black/70 border border-white/10 text-slate-400">
                {selectedPhoto + 1} / {photos.length}
              </span>
            </div>

            {/* Photo Caption Overlay */}
            <div className="absolute bottom-3 left-3 right-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
              <div className="space-y-0.5">
                <span className="px-1.5 py-0.5 rounded bg-white/10 border border-white/20 text-white font-mono text-[9px] uppercase tracking-wider inline-block">
                  {photos[selectedPhoto].tag}
                </span>
                <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                  {photos[selectedPhoto].title}
                </h3>
                <p className="text-slate-300 text-xs max-w-xl font-sans">
                  {photos[selectedPhoto].desc}
                </p>
              </div>
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
                0{idx + 1} // {p.title}
              </button>
            ))}
          </div>
        </div>

        {/* 4. Turnkey Sensor & Hardware Matrix (KUTUSUZ EDİTORYAL MİMARİ) */}
        <div className="space-y-4 pt-4 border-t border-white/10">
          <div className="pb-2 border-b border-white/10">
            <div className="text-[10px] font-mono text-slate-400 font-semibold tracking-wider uppercase">
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
                  <div className="w-7 h-7 rounded bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 shrink-0 mt-0.5">
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div className="space-y-0.5 min-w-0">
                    <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                      {item.title}
                    </div>
                    <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
                      {item.val}
                    </div>
                    <div className="text-[11px] text-slate-400 font-sans">
                      {item.sub}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. Architecture & Safety Protocols (KUTUSUZ EDİTORYAL ÇİFT SÜTUN) */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 pt-6 border-t border-white/10">
          
          {/* E-GMP & CAN-FD Integration */}
          <div className="space-y-3">
            <div className="border-b border-white/10 pb-2">
              <div className="text-[10px] font-mono text-slate-400 font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "E-GMP CAN-FD ENTEGRASYONU" : "E-GMP CAN-FD ARCHITECTURE"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "Sıfır Delme & Tak-Çalıştır Şasi Uyumu" : "Zero-Drill & Plug-and-Play Integration"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-slate-300 divide-y divide-white/5">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Dikiz Aynası ADAS Y-Harness:" : "Rearview ADAS Y-Harness:"}</b>{" "}
                  {lang === "tr"
                    ? "OBD-II gateway kısıtlamasına takılmadan şasi CAN-FD hattına 100 Hz direksiyon (LKAS11) ve 50 Hz fren/gaz (SCC_FD) sinyali iletilir."
                    : "Transmits 100 Hz steering (LKAS11) and 50 Hz brake/accel (SCC_FD) directly into chassis CAN-FD without gateway latency."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "57 Litrelik Sub-Trunk Hesaplama Havuzu:" : "57-Liter Sub-Trunk Compute Hub:"}</b>{" "}
                  {lang === "tr"
                    ? "Jetson Orin, sigorta panosu, 5G router ve DC-DC regülatör bagaj altı havuzuna yerleştirilir; iç mekan düzeni korunur."
                    : "Jetson Orin, fuse box, 5G router, and DC-DC regulator fit discreetly in the sub-trunk compartment."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
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
            <div className="border-b border-white/10 pb-2">
              <div className="text-[10px] font-mono text-slate-400 font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "GÜVENLİK VE DEVİR PROTOKOLLERİ" : "SAFETY & TAKEOVER PROTOCOLS"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "5ms Sürücü Devralma ve Güvenli Durma" : "5ms Driver Override & Fail-Safe"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-slate-300 divide-y divide-white/5">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Anlık Sürücü Müdahalesi (5ms):" : "Instant Human Takeover (5ms):"}</b>{" "}
                  {lang === "tr"
                    ? "Direksiyona tork uygulandığında veya fren pedalına basıldığında otonomi 5 milisaniyede kontrolü sürücüye bırakır (ISO 26262 ASIL-D)."
                    : "Manual steering torque or brake depression instantly disengages autonomy within 5ms under ISO 26262 ASIL-D."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "200ms Watchdog & MRM Fail-Safe:" : "200ms Watchdog & MRM Fail-Safe:"}</b>{" "}
                  {lang === "tr"
                    ? "Herhangi bir donanım gecikmesinde flaşörler açılır, araç şeridinde kontrollü durur ve 4TB SSD kara kutu kaydı alır."
                    : "On sensor stall, hazard lights engage, the vehicle safely stops within lane, and 4TB NVMe SSD logs telemetry."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "5G GPS Coğrafi Çit (Geofence):" : "5G GPS Geofencing & Remote Kill:"}</b>{" "}
                  {lang === "tr"
                    ? "Test sahası (BTM veya Bilişim Vadisi) dışına çıkış halinde motor kilitlenir; 7/24 teleoperasyon C2 ile yönetilir."
                    : "Vehicle locks drive if exiting authorized test perimeter; monitored 24/7 via tactical desktop C2."}
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* 6. Four-Stage Proving Ground Plan (KUTUSUZ ENTEGRE ÇİZGİLİ ŞERİT) */}
        <div className="space-y-3 pt-6 border-t border-white/10">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-white/10">
            <div>
              <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                // {lang === "tr" ? "SAHA TEST YOL HARİTASI" : "DEPLOYMENT ROADMAP"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "4 Kademeli Test ve İzin Protokolü" : "4-Stage Safe Deployment Process"}
              </h2>
            </div>
            <div className="text-[10px] font-mono text-emerald-400 font-semibold">
              UN ECE R157 & ADS UYUMLU
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-white/10 py-3 border-y border-white/10 font-mono">
            <div className="py-2 px-3 first:pl-0 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 01 // SİMÜLASYON</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">Webots 3D Dijital İkiz</div>
              <div className="text-[11px] text-slate-400 leading-relaxed font-sans">
                1.301 birim test, SLAM haritalama, Pure Pursuit rota takibi.
              </div>
              <div className="text-[10px] text-emerald-400 font-semibold pt-0.5">%100 Doğrulandı</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 02 // KAPALI PİST</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">Bilişim Vadisi Gebze</div>
              <div className="text-[11px] text-slate-400 leading-relaxed font-sans">
                1.5 km asfalt parkur, cansız mankenler, yapay kavşak ve dur-kalk akışı.
              </div>
              <div className="text-[10px] text-slate-400 font-medium pt-0.5">Sıfır Riskli Parkur</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 03 // KAMPÜS</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">İTO BTM Fulya Kampüs</div>
              <div className="text-[11px] text-slate-400 leading-relaxed font-sans">
                Kapalı yerleşkede 20-30 km/s hızla otonom yolcu alma ve bırakma.
              </div>
              <div className="text-[10px] text-slate-400 font-medium pt-0.5">BTM Özel Alan İzni</div>
            </div>

            <div className="py-2 px-3 sm:pl-6 space-y-1">
              <div className="text-[10px] text-slate-400 font-bold uppercase">AŞAMA 04 // AÇIK YOL</div>
              <div className="text-xs sm:text-sm font-bold text-white font-sans">Şehir İçi Pilot Hat</div>
              <div className="text-[11px] text-slate-400 leading-relaxed font-sans">
                Koltukta emniyet sürücüsü eşliğinde karma trafikte Seviye 4 sürüş.
              </div>
              <div className="text-[10px] text-slate-400 font-medium pt-0.5">Sanayi Bak. & T Plaka</div>
            </div>
          </div>
        </div>

        {/* 7. Institutional NDA Technical Cooperation Bar */}
        <div className="py-4 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="space-y-1 text-center md:text-left max-w-2xl">
            <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
              // {lang === "tr" ? "KURUMSAL TEKNİK İŞBİRLİĞİ" : "INSTITUTIONAL TECHNICAL COOPERATION"}
            </div>
            <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
              {lang === "tr" ? "Mühendislik Şartnamesi ve Entegrasyon Protokolü" : "Engineering Specification & Integration Protocol"}
            </h3>
            <p className="text-slate-400 text-xs leading-relaxed">
              {lang === "tr"
                ? "Donanım mimarisi, sensör yerleşim geometrisi, CAN-FD sinyal protokolleri ve platform güvenlik standartları kurumsal gizlilik sözleşmesi (NDA) kapsamında OEM ve savunma sanayii ortaklarıyla paylaşılmaktadır."
                : "Detailed hardware schematics, sensor mounting geometry, CAN-FD bus protocols, and functional safety architecture are available to qualified OEM and defense partners under institutional NDA."}
            </p>
          </div>

          <Link
            href="/iletisim"
            className="w-full sm:w-auto px-4 py-2 rounded-lg bg-white text-slate-950 hover:bg-slate-200 font-semibold text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-1.5 shrink-0"
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
