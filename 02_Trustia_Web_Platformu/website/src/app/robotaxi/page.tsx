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
  Activity,
} from "lucide-react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { useLanguage } from "@/context/LanguageContext";

export default function RobotaxiPage() {
  const { lang } = useLanguage();
  const [activeSensor, setActiveSensor] = useState<"all" | "lidar" | "radar" | "camera" | "compute">("all");

  const sensorDetails = {
    all: {
      tag: lang === "tr" ? "360° ÇOKLU SENSÖR FÜZYONU & IEEE 1588v2 PTP" : "360° MULTI-SENSOR FUSION & IEEE 1588v2 PTP",
      title: lang === "tr" ? "Erken ve Geç Füzyonlu Birleşik Algılama Çekirdeği" : "Early & Late Multi-Modal Perception Core",
      desc: lang === "tr"
        ? "LiDAR 3D nokta bulutları (400 Hz IMU hareket bozulması düzeltmeli), 77GHz Doppler radar kinematik vektörleri ve 4x GMSL2 HDR kamera akışları IEEE 1588v2 PTP (<100 µs) senkronizasyonuyla birleştirilir."
        : "LiDAR 3D point clouds (with 400 Hz IMU motion deskewing), 77GHz Doppler radar vectors, and 4x GMSL2 HDR camera streams fused under IEEE 1588v2 PTP (<100 µs) synchronization.",
      metric: "240m Menzil • 0.05m Hassasiyet • <15ms Uçtan Uca Gecikme"
    },
    lidar: {
      tag: lang === "tr" ? "BİRİNCİL 3D SLAM, KALDIRIM TAŞI & DERİNLİK" : "PRIMARY 3D SLAM, CURB DETECTION & DEPTH",
      title: lang === "tr" ? "Ouster OS2-128 Rev 7 3D LiDAR (Tavan Montaj)" : "Ouster OS2-128 Rev 7 3D LiDAR (Roof Mount)",
      desc: lang === "tr"
        ? "Tavan merkezine entegre 128 kanal ile saniyede 2.62 milyon nokta üretir. GPS'siz tünel ve kanyonlarda 3D NDT SLAM ile santimetre hassasiyetinde konumlama ve silinmiş şeritlerde kaldırım taşı (8-28 cm) algılama icra eder."
        : "Roof-mounted 128-channel solid-state LiDAR generating 2.62M points/sec for GPS-denied 3D NDT SLAM localization and 3D curb boundary detection.",
      metric: "240 Metre • 128 Kanal • 0.1° Açısal Çözünürlük • UDP Gbit Ethernet"
    },
    radar: {
      tag: lang === "tr" ? "TÜM HAVA KOŞULLARI VE DOPPLER HIZ" : "ALL-WEATHER DOPPLER VELOCITY",
      title: lang === "tr" ? "Continental ARS 408-21 77GHz Otomotiv Radarı" : "Continental ARS 408-21 77GHz Automotive Radar",
      desc: lang === "tr"
        ? "Yoğun sis, sağanak yağmur, kar ve toza tam nüfuz eden doğrudan Doppler radyal hız tespiti. 250 metreye kadar öndeki araç ve hareketli cisimlerin hız vektörlerini anlık çıkarır."
        : "Penetrates dense fog, heavy rain, snow, and dust with direct Doppler radial velocity measurements up to 250 meters.",
      metric: "250 Metre Menzil • ±0.1 km/s Hız Hassasiyeti • CAN-FD Veri Yolu"
    },
    camera: {
      tag: lang === "tr" ? "360° ÇEVRESEL GÖRSEL ALGILAMA & SOTIF" : "360° SURROUND VISION & SOTIF",
      title: lang === "tr" ? "4x Leopard Sony IMX390 HDR GMSL2 Kamera + CalmCar Hakemi" : "4x Leopard Sony IMX390 HDR GMSL2 Camera + CalmCar Arbiter",
      desc: lang === "tr"
        ? "Ön, sol, sağ ve arka hatlara konumlandırılmış 120° FOV lensler ile 120 dB süper dinamik aralık. ISO 21448 SOTIF gözetmeni kamera algısını 3D LiDAR ile çapraz doğrulayarak hayalet frenlemeyi (Phantom Brake) önler."
        : "Synchronized 120° FOV surround cameras with 120 dB dynamic range, cross-validated by ISO 21448 SOTIF and 3D LiDAR to prevent phantom braking.",
      metric: "120 dB HDR • 60 FPS Senkron • IP67 Muhafaza • KVKK m.9 Veri Kalkanı"
    },
    compute: {
      tag: lang === "tr" ? "MERKEZİ HESAPLAMA VE AKTÜATÖR KÖPRÜSÜ" : "AI COMPUTE & ACTUATION BRIDGE",
      title: lang === "tr" ? "NVIDIA Jetson AGX Orin 64GB + 100 Hz CAN-FD Köprüsü" : "NVIDIA Jetson AGX Orin 64GB + 100 Hz CAN-FD Bridge",
      desc: lang === "tr"
        ? "275/560 TOPS merkezi otonom yapay zeka gücü. Direksiyon (EPS) ve fren/gaz (i-Booster + yedek ESC/EPB) komutlarını şasi CAN-FD hattına 100 Hz (1.4 ms) frekansta deterministik olarak aktarır."
        : "Central AI compute interfacing directly with vehicle CAN-FD at 100 Hz (1.4 ms) cyclic rate with 5ms hard-interrupt safety fallback and redundant braking.",
      metric: "275/560 TOPS INT8 • 100 Hz CAN-FD • 5ms Devralma • UN R157 DSSAD"
    }
  };

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
      sub: "360°x59° Ultra Geniş Açı • 8-28 cm Kaldırım Algılama"
    },
    {
      icon: Radio,
      title: lang === "tr" ? "360° Görsel Algılama" : "360° HDR Vision",
      val: "4x Leopard Sony IMX390 GMSL2",
      sub: "120 dB Dinamik Aralık • ISO 21448 SOTIF & KVKK Kalkanı"
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
      val: "Septentrio mosaic-go + 400Hz ESKF",
      sub: "GNSS-Denied 3D NDT SLAM • ±4.2 cm Yörünge Hassasiyeti"
    },
    {
      icon: Zap,
      title: lang === "tr" ? "CAN-FD & Siber Kalkan" : "CAN-FD & Cyber Shield",
      val: "100 Hz CAN-FD + UN R155 IDPS",
      sub: "1.4 ms Mesaj İletimi • EPS & Çift Yedekli i-Booster/ESC"
    },
    {
      icon: Lock,
      title: lang === "tr" ? "ASIL-D & IEEE 2846 RSS" : "ASIL-D & IEEE 2846 RSS",
      val: "20ms Öz-Denetim • 50ms Watchdog",
      sub: "1.5 m/s² Sağa Çekme (MRM) • 5ms Sürücü Devri"
    }
  ];

  const l4ComplianceMatrix = [
    { code: "01", std: "ISO 26262 ASIL-D & MRM", mod: "safety/asil_d_mrm.py", desc: "20 ms öz-denetim, 50 ms Watchdog, 1.5 m/s² kontrollü sağa çekme (MRM), 6.5 m/s² acil fren ve <=5 ms sürücü devri." },
    { code: "02", std: "IEEE 2846 & Mobileye RSS", mod: "security/rss_ieee2846.py", desc: "Boylamsal ve yanal minimum güvenli takip mesafesi denklemleri ve otomatik 'Proper Response' fren kalkanı." },
    { code: "03", std: "ISO 21448 SOTIF & CalmCar Hakemi", mod: "perception/calmcar_bridge.py", desc: "Kamera algısını 3B LiDAR ile çapraz doğrulayan, güneş parlaması ve hayalet frenlemeyi (Phantom Brake) önleyen hakem." },
    { code: "04", std: "AB 2022/1426 ODD Coğrafi Çit", mod: "security/odd_sotif_dssad.py", desc: "1 Aralık 2024 Resmî Gazete uyumlu coğrafi çit, hız sınırı, eğim ve görüş mesafesi denetleyicisi." },
    { code: "05", std: "UN/ECE R157 DSSAD Kara Kutu", mod: "security/odd_sotif_dssad.py", desc: "SHA-256 kriptografik özet zincirli (Hash-Chained) değiştirilemez adli olay ve otonom devir kayıt sistemi." },
    { code: "06", std: "UN/ECE R155 & ISO 21434 CAN-IDPS", mod: "security/can_ids_r155.py", desc: "CAN-FD veri yolunda sahte mesaj enjeksiyonu (Spoofing), DoS boğma ve yürüyen sayaç (0..15) saldırı tespiti." },
    { code: "07", std: "UN/ECE R156 SUMS & RXSWIN", mod: "security/sums_un_r156.py", desc: "RXSWIN tip onay yazılım sicili, HMAC-SHA256 OTA paket doğrulama, hareket halinde güncelleme kilidi ve atomik Rollback." },
    { code: "08", std: "6698 Sayılı KVKK m.9 Veri Kalkanı", mod: "perception/calmcar_bridge.py", desc: "Kamera ve konum verilerinin yurt dışı bulut sunucularına aktarımını otomatik engelleyen yerel veri kalkanı." },
    { code: "09", std: "IEEE 1588v2 PTP & LiDAR Deskewing", mod: "perception/lidar_deskew_ptp.py", desc: "Mikrosaniye hassasiyetli PTP saat senkronu denetimi ve 400 Hz IMU ile 3B LiDAR hareket bozulması düzeltme." },
    { code: "10", std: "3B LiDAR Kaldırım Taşı (Curb) Algılama", mod: "perception/curb_detector.py", desc: "Şerit çizgilerinin silindiği veya yağışlı yollarda 3B LiDAR basamak farkından (8-28 cm) yol koridoru çıkarma." },
    { code: "11", std: "3B NDT SLAM & 400 Hz ESKF", mod: "slam/eskf.py & pose_graph.py", desc: "Tünel ve GPS'siz (GNSS-Denied) alanlarda 3B LiDAR tarama eşleştirme ve 400 Hz Hata Durumlu Kalman Filtresi." },
    { code: "12", std: "Lanelet2 HD Harita & KTK m.74", mod: "planning/lanelet2_rules.py", desc: "Topolojik şerit kuralları, yaya geçidinde yayaya mutlak duruş önceliği ve kavşak geçiş üstünlüğü karar motoru." },
    { code: "13", std: "Frenet (s, d) Jerk-Optimal Planlayıcı", mod: "planning/frenet_lattice_planner.py", desc: "Yol merkez eğrisine göre 5. dereceden (Quintic) sarsıntısız yerel engel kaçınma ve konforlu şerit değiştirme." },
    { code: "14", std: "Kinematik Hibrit A* Planlayıcı", mod: "planning/hybrid_astar.py", desc: "SAIC Maxus MIFA 7 (2.975 m dingil mesafesi) ve Hyundai Ioniq 5 dönüş çapı kısıtlarına uygun rota planlama." },
    { code: "15", std: "Model Öngörülü Kontrol (MPC) & Stanley", mod: "control/mpc_redundant_control.py", desc: "Ufuk tabanlı kinematik bisiklet modeli optimizasyonu (MPC), Stanley şerit takibi ve Çift Yedekli Fren Dağıtımı." },
    { code: "16", std: "ISO 11898-1 100 Hz CAN-FD & DBC", mod: "canbus/mifa7_canfd.py", desc: "100 Hz (1.4 ms) direksiyon, i-Booster fren, EPB ve yürüyen sayaçlı kalp atışı mesaj kodlama altyapısı." },
    { code: "17", std: "ISO/TR 23049 eHMI & Akustik Siren", mod: "v2x/ehmi_siren_detector.py", desc: "Yayalar için dış iletişim LED paneli (eHMI), V2X GLOSA yeşil dalga ve 600-1550 Hz ambulans/itfaiye siren algılama." },
    { code: "18", std: "Kabin Kapı Kilidi & Batarya BMS", mod: "command/cabin_bms_safety.py", desc: "Kapı/bagaj emniyet kilidi (Door Interlock), kemer kontrolü, yolcu SOS sağa çekme butonu ve batarya SoC/termal yönetimi." },
    { code: "19", std: "Uzaktan Operasyon (Teleoperation)", mod: "fleet/teleoperation.py", desc: "Çağrı merkezi operatörünün <=150 ms ağ gecikmesi ve <=15 km/s güvenli hız sınırı ile uzaktan kurtarma köprüsü." },
    { code: "20", std: "CARLA 0.9.15+ / MetaDrive / Webots SIL", mod: "integration/carla_bridge.py", desc: "CARLA 100 Hz simülasyon köprüsü (2.6M nokta/sn LiDAR) ve 582 senaryoluk deterministik sanal doğrulama." },
  ];

  const simVsFieldRows = [
    { param: "Sistem Öz-Denetim Döngüsü (Self-Check)", mod: "safety/asil_d_mrm.py", sim: "20.0 milisaniye (50 Hz)", field: "20.0 – 22.5 ms (RTOS zamanlayıcı toleransı ile)" },
    { param: "Komut Kesintisi Zaman Aşımı (Watchdog)", mod: "safety/asil_d_mrm.py", sim: "50.0 milisaniye", field: "50.0 – 55.0 ms (Donanım kesme gecikmesi dahil)" },
    { param: "Kontrollü Sağa Çekme Yavaşlaması (MRM)", mod: "odd_sotif_dssad.py", sim: "1.5 m/s²", field: "1.2 – 1.8 m/s² (Yol eğimi ve asfalt tutunmasına göre)" },
    { param: "Kritik Acil Durum Frenlemesi (E-Stop)", mod: "mifa7_canfd.py", sim: "6.5 m/s²", field: "4.5 – 6.5 m/s² (Zemin sürtünme katsayısı µ ve i-Booster basıncına göre)" },
    { param: "CAN-FD Mesaj Paketleme ve İletim Süresi", mod: "mifa7_canfd.py (2 Mbps)", sim: "1.4 milisaniye (100 Hz)", field: "1.4 – 3.5 ms (Şasi CAN hattı anlık mesaj yoğunluğuna göre)" },
    { param: "Sürücü Direksiyon/Fren Müdahalesinde Devir", mod: "carla_bridge.py & asil_d_mrm.py", sim: "5.0 milisaniye (Yazılım kararı)", field: "5.0 – 15.0 ms (Tork sensörü mekanik okuma süresi dahil)" },
  ];

  const current = sensorDetails[activeSensor];

  return (
    <main className="relative min-h-screen bg-gradient-to-b from-[#1c1813] via-[#28221a] to-[#1c1813] text-[#f5efe6] font-sans selection:bg-[#E4F80D] selection:text-black overflow-x-hidden pt-20 sm:pt-28 pb-12">
      <Navbar />

      {/* Ambient Tactical Sand/Gold Glow */}
      <div className="absolute top-0 inset-x-0 h-[600px] bg-[radial-gradient(ellipse_at_top,rgba(229,214,188,0.10),transparent_70%)] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-6 sm:space-y-8">

        {/* 1. Breadcrumb & Header */}
        <div className="space-y-2.5">
          <div className="flex items-center gap-2 text-xs font-mono text-[#E5D6BC]/70">
            <Link href="/" className="hover:text-[#E5D6BC] flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-[#E5D6BC] font-semibold">ROBOTAXI</span>
          </div>

          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-4 pb-4 border-b border-[#E5D6BC]/15">
            <div className="space-y-1.5 max-w-3xl">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-[#E5D6BC]/10 border border-[#E5D6BC]/25 text-[#E5D6BC] text-[10px] font-mono tracking-wider uppercase">
                <span>{lang === "tr" ? "REFERANS OTONOMİ MİMARİSİ // SAIC MAXUS MIFA 7 & HYUNDAI IONIQ 5" : "REFERENCE AUTONOMY ARCHITECTURE // SAIC MAXUS MIFA 7 & HYUNDAI IONIQ 5"}</span>
              </div>
              
              <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight leading-snug">
                SAIC Maxus MIFA 7 &amp; E-GMP{" "}
                <span className="text-[#E5D6BC] font-normal block sm:inline">
                  {lang === "tr" ? "— Seviye 4 Robotaksi Yazılım, Sensör ve Tip Onay Mimarisi" : "— Level 4 Robotaxi Software, Sensor & Homologation Blueprint"}
                </span>
              </h1>
              
              <p className="text-[#d6cebf] text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
                {lang === "tr"
                  ? "Ticari yolcu filoları ve kentsel robotaksi operasyonları için 128 Kanallı 3D LiDAR, 4x GMSL2 HDR Kamera, 77GHz Radar, 100 Hz CAN-FD aktüatör köprüsü ve 20 uluslararası Seviye-4 modülüyle yapılandırılmış; 198 dosya ve 29.748+ satırlık deterministik otonomi şartnamesi."
                  : "Configured with 128-channel 3D LiDAR, 4x GMSL2 HDR cameras, 77GHz radar, 100 Hz CAN-FD drive-by-wire, and 20 international Level-4 modules across 198 files and 29,748+ lines of sovereign autonomy software."}
              </p>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap items-center gap-3 shrink-0">
              <Link
                href="/iletisim/"
                className="px-4 py-2 rounded-lg bg-[#E5D6BC] text-[#14120c] hover:bg-white font-bold text-xs tracking-wider uppercase transition-colors inline-flex items-center gap-1.5 shadow-md"
              >
                <span>{lang === "tr" ? "Kapalı Kutu SDK & NDA Talebi" : "Closed-Box SDK & NDA Request"}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>
        </div>

        {/* 2. Integrated 4-Metric Architectural Bar (KUTUSUZ & KOMPAKT) */}
        <div className="grid grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-[#E5D6BC]/15 py-3.5 border-y border-[#E5D6BC]/20 font-mono">
          <div className="py-1 px-3 first:pl-0 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "TOPLAM MÜHENDİSLİK HACMİ" : "TOTAL CODEBASE VOLUME"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">29.748+ Satır</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              {lang === "tr" ? "198 Dosya (Çekirdek + Robotaksi SDK)" : "198 Files (Core + Robotaxi SDK)"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "OTOMATİK DOĞRULAMA" : "AUTOMATED TESTS"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">1.307 + 21 Test</div>
            <span className="text-[10px] text-emerald-400 block font-sans font-medium">
              {lang === "tr" ? "%100 Başarı (0 Hata / 0 Fail)" : "100% Pass Rate (0 Failures)"}
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "EMNİYET & DEVRALMA" : "SAFETY & OVERRIDE"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">20ms / 50ms / 5ms</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              Öz-Denetim • Watchdog • İnsan Devri
            </span>
          </div>

          <div className="py-1 px-3 sm:pl-6 space-y-0.5">
            <span className="text-[10px] text-[#E5D6BC] uppercase tracking-wider block font-semibold">
              {lang === "tr" ? "TİP ONAY & STANDART" : "HOMOLOGATION"}
            </span>
            <div className="text-lg sm:text-xl font-bold text-white tracking-tight">20 L4 Modülü</div>
            <span className="text-[10px] text-[#d6cebf]/80 block font-sans">
              AB 2022/1426 • R155/R156/R157 • RSS
            </span>
          </div>
        </div>

        {/* 3. Interactive Sensor Fusion Blueprint Visualizer */}
        <div className="space-y-3 pt-2">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-[#E5D6BC]/15">
            <div>
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "DONANIM VE SENSÖR YERLEŞİM ŞARTNAMESİ" : "HARDWARE & SENSOR PLACEMENT BLUEPRINT"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr" ? "360° Sensör Kapsama ve CAN-FD Veri Yolu Mimarisi" : "360° Sensor Coverage & CAN-FD Topology"}
              </h2>
            </div>
            
            {/* Filter Pills */}
            <div className="flex flex-wrap items-center gap-1.5">
              {[
                { id: "all" as const, label: lang === "tr" ? "TÜMÜ (360°)" : "ALL (360°)" },
                { id: "lidar" as const, label: "OUSTER 128K LİDAR" },
                { id: "radar" as const, label: "77GHz RADAR" },
                { id: "camera" as const, label: "4x HDR KAMERA" },
                { id: "compute" as const, label: "ORIN & CAN-FD" }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveSensor(tab.id)}
                  className={`px-2.5 py-1 rounded text-[11px] font-mono transition-all duration-200 cursor-pointer ${
                    activeSensor === tab.id
                      ? "bg-[#E5D6BC] text-[#14120c] font-bold shadow-md"
                      : "bg-[#251f18] hover:bg-[#2e261e] text-[#E5D6BC]/80 hover:text-white border border-[#E5D6BC]/20"
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          </div>

          {/* Technical Vector Canvas (360° FOV Blueprint) */}
          <div className="relative rounded-xl overflow-hidden border border-[#E5D6BC]/25 bg-[#18140e] aspect-[16/9] sm:aspect-[21/9] max-h-[480px] flex items-center justify-center p-4 shadow-inner">
            
            {/* Coordinate Grid Header */}
            <div className="absolute top-3 left-3 right-3 flex items-center justify-between text-[10px] font-mono text-slate-400 pointer-events-none">
              <span className="px-2 py-0.5 rounded bg-black/60 border border-[#E5D6BC]/15">
                TOP-DOWN // 360° SENSÖR KAPSAMA GEOMETRİSİ
              </span>
              <span className="text-slate-400">
                ÖLÇEK: 1:100 (240m ÇAP) • SAIC MAXUS MIFA 7 ŞASİ
              </span>
            </div>

            {/* High-Precision SVG Sensor Topology */}
            <svg viewBox="0 0 600 340" className="w-full h-full" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="archGridPage" width="30" height="30" patternUnits="userSpaceOnUse">
                  <path d="M 30 0 L 0 0 0 30" fill="none" stroke="rgba(255,255,255,0.03)" strokeWidth="1" />
                </pattern>
                <radialGradient id="lidarGlowPage" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.25" />
                  <stop offset="70%" stopColor="#38bdf8" stopOpacity="0.06" />
                  <stop offset="100%" stopColor="#38bdf8" stopOpacity="0" />
                </radialGradient>
                <linearGradient id="radarBeamPage" x1="0%" y1="100%" x2="0%" y2="0%">
                  <stop offset="0%" stopColor="#34d399" stopOpacity="0.35" />
                  <stop offset="100%" stopColor="#34d399" stopOpacity="0.02" />
                </linearGradient>
              </defs>

              <rect width="600" height="340" fill="url(#archGridPage)" />

              {/* Range Rings (50m, 100m, 180m, 240m) */}
              <circle cx="300" cy="170" r="45" stroke="rgba(229,214,188,0.15)" strokeDasharray="3 3" />
              <circle cx="300" cy="170" r="90" stroke="rgba(229,214,188,0.15)" strokeDasharray="3 3" />
              <circle cx="300" cy="170" r="140" stroke="rgba(229,214,188,0.12)" strokeDasharray="3 3" />

              {/* Range Labels */}
              <text x="304" y="122" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">50m</text>
              <text x="304" y="77" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">100m</text>
              <text x="304" y="28" fill="rgba(229,214,188,0.7)" fontSize="8" fontFamily="monospace">200m (LiDAR)</text>

              {/* --- 1. LiDAR 360° Zone --- */}
              {(activeSensor === "all" || activeSensor === "lidar") && (
                <g className="transition-opacity duration-300">
                  <circle cx="300" cy="170" r="145" fill="url(#lidarGlowPage)" />
                  <circle cx="300" cy="170" r="145" stroke="#38bdf8" strokeWidth="1" strokeDasharray="4 4" opacity="0.4" />
                  <line x1="300" y1="170" x2="300" y2="25" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.4" />
                  <line x1="300" y1="170" x2="445" y2="170" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                  <line x1="300" y1="170" x2="155" y2="170" stroke="#38bdf8" strokeWidth="1" strokeDasharray="2 4" opacity="0.3" />
                </g>
              )}

              {/* --- 2. Radar Forward Long-Range Cone (250m, 77GHz) --- */}
              {(activeSensor === "all" || activeSensor === "radar") && (
                <g className="transition-opacity duration-300">
                  <path
                    d="M 300 135 L 210 15 A 180 180 0 0 1 390 15 Z"
                    fill="url(#radarBeamPage)"
                    stroke="#34d399"
                    strokeWidth="1.2"
                    opacity="0.8"
                  />
                  <path d="M 240 55 A 140 140 0 0 1 360 55" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                  <path d="M 265 95 A 90 90 0 0 1 335 95" stroke="#34d399" strokeWidth="1" strokeDasharray="2 3" opacity="0.6" />
                  <text x="300" y="22" textAnchor="middle" fill="#34d399" fontSize="9" fontFamily="monospace" fontWeight="bold">
                    77GHz DOPPLER RADAR // 250m MENZİL
                  </text>
                </g>
              )}

              {/* --- 3. 4x Surround HDR Cameras (120° FOV Each) --- */}
              {(activeSensor === "all" || activeSensor === "camera") && (
                <g className="transition-opacity duration-300" opacity="0.75">
                  <polygon points="300,140 200,45 400,45" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="280,170 170,95 170,245" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="320,170 430,95 430,245" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                  <polygon points="300,205 210,295 390,295" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" strokeWidth="1" strokeDasharray="2 2" />
                </g>
              )}

              {/* --- 4. Vehicle Chassis Silhouette --- */}
              <g>
                <rect x="281" y="132" width="38" height="78" rx="8" fill="#0f172a" stroke="#475569" strokeWidth="1.5" />
                <rect x="284" y="148" width="32" height="46" rx="4" fill="#1e293b" stroke="#334155" strokeWidth="1" />
                
                <rect x="277" y="140" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="319" y="140" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="277" y="190" width="4" height="12" rx="1.5" fill="#64748b" />
                <rect x="319" y="190" width="4" height="12" rx="1.5" fill="#64748b" />

                <line x1="272" y1="146" x2="272" y2="196" stroke="rgba(148,163,184,0.4)" strokeWidth="0.8" />
                <text x="268" y="173" textAnchor="end" fill="rgba(148,163,184,0.7)" fontSize="7" fontFamily="monospace">2.975mm</text>

                {/* Bumper Pods */}
                <circle cx="286" cy="134" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />
                <circle cx="314" cy="134" r="3" fill="#38bdf8" stroke="#ffffff" strokeWidth="1" />

                {/* Roof LiDAR */}
                <circle cx="300" cy="168" r="5" fill="#0284c7" stroke="#38bdf8" strokeWidth="1.5" />
                <circle cx="300" cy="168" r="2" fill="#ffffff" />

                {/* Sub-Trunk Compute Hub */}
                <rect x="288" y="196" width="24" height="10" rx="2" fill="#047857" stroke="#34d399" strokeWidth="1" />
                <text x="300" y="203" textAnchor="middle" fill="#ffffff" fontSize="6" fontFamily="monospace" fontWeight="bold">ORIN</text>

                {/* CAN-FD Bus Backbone Line */}
                {(activeSensor === "all" || activeSensor === "compute") && (
                  <line x1="300" y1="136" x2="300" y2="196" stroke="#10b981" strokeWidth="1.5" strokeDasharray="3 2" />
                )}
              </g>

              {/* Callout Labels with Connecting Hairlines */}
              <g fontFamily="monospace" fontSize="8" fill="#94a3b8">
                <path d="M 305 168 L 380 145 L 440 145" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                <text x="445" y="148" fill="#38bdf8" fontWeight="bold">OUSTER OS2-128 (TAVAN)</text>

                <path d="M 283 134 L 210 120 L 150 120" stroke="rgba(56,189,248,0.5)" strokeWidth="0.8" />
                <text x="145" y="123" textAnchor="end" fill="#38bdf8">2x LIVOX MID-360 (TAMPON)</text>

                <path d="M 312 201 L 380 215 L 440 215" stroke="rgba(52,211,153,0.5)" strokeWidth="0.8" />
                <text x="445" y="218" fill="#34d399" fontWeight="bold">JETSON ORIN + 100Hz CAN-FD</text>

                <path d="M 277 170 L 210 190 L 150 190" stroke="rgba(245,158,11,0.5)" strokeWidth="0.8" />
                <text x="145" y="193" textAnchor="end" fill="#f59e0b">4x SONY IMX390 GMSL2 HDR</text>
              </g>
            </svg>

            {/* Bottom Right Homologation Tag */}
            <div className="absolute bottom-3 right-3 flex items-center gap-2 text-[9px] font-mono text-slate-400">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>ISO 26262 ASIL-D • IEEE 2846 RSS • UN R155/R156/R157</span>
            </div>
          </div>

          {/* Dynamic Specification Bar of Selected Sensor */}
          <div className="p-4 rounded-xl bg-[#251f18] border border-[#E5D6BC]/25 space-y-1 shadow-md">
            <div className="flex items-center justify-between text-[10px] font-mono">
              <span className="text-[#E5D6BC] font-semibold">{current.tag}</span>
              <span className="text-[#E5D6BC]/75">{current.metric}</span>
            </div>
            <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
              {current.title}
            </div>
            <p className="text-[11px] text-[#d6cebf] leading-relaxed font-sans">
              {current.desc}
            </p>
          </div>
        </div>

        {/* 4. Turnkey Sensor & Hardware Matrix */}
        <div className="space-y-4 pt-4 border-t border-[#E5D6BC]/15">
          <div className="pb-2 border-b border-[#E5D6BC]/15">
            <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
              // {lang === "tr" ? "DONANIM VE SENSÖR MİMARİSİ" : "HARDWARE & SENSOR FUSION"}
            </div>
            <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
              {lang === "tr" ? "27 Parçalık Seviye 4 Donanım ve Aktüatör Seti" : "27-Item Level-4 Turnkey Sensor & Actuator Suite"}
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 divide-y divide-white/10">
            {specs.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div key={idx} className="py-3 flex items-start gap-3">
                  <div className="w-7 h-7 rounded bg-[#251f18] border border-[#E5D6BC]/25 flex items-center justify-center text-[#E5D6BC] shrink-0 mt-0.5">
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div className="space-y-0.5 min-w-0">
                    <div className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
                      {item.title}
                    </div>
                    <div className="text-xs sm:text-sm font-bold text-white tracking-tight">
                      {item.val}
                    </div>
                    <div className="text-[11px] text-[#d6cebf]/80 font-sans">
                      {item.sub}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 5. NEW: 20-Item International Level-4 Robotaxi & EU 2022/1426 Compliance Matrix */}
        <div className="space-y-4 pt-6 border-t border-[#E5D6BC]/15">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 pb-2 border-b border-[#E5D6BC]/15">
            <div>
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "ULUSLARARASI SEVİYE-4 VE 1 ARALIK 2024 RESMÎ GAZETE (AB 2022/1426) UYUMLULUK MATRİSİ" : "INTERNATIONAL LEVEL-4 & EU 2022/1426 HOMOLOGATION MATRIX"}
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {lang === "tr"
                  ? "20 Temel Otonomi ve Regülasyon Modülü (%100 Kodlanmış ve Test Edilmiş Mimari)"
                  : "20 Core Autonomy & Regulatory Modules (100% Coded & Verified Architecture)"}
              </h2>
            </div>
            <div className="text-[10px] font-mono text-emerald-400 font-semibold">
              1.307 ÇEKİRDEK TESTİ + 21 SDK TESTİ (%100 YEŞİL)
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {l4ComplianceMatrix.map((row) => (
              <div
                key={row.code}
                className="p-3.5 rounded-xl bg-[#251f18]/90 border border-[#E5D6BC]/20 space-y-1.5 flex flex-col justify-between"
              >
                <div className="space-y-1">
                  <div className="flex items-center justify-between gap-2 font-mono text-[10px]">
                    <span className="text-[#E4F80D] font-bold">#{row.code} // {row.std}</span>
                    <span className="px-1.5 py-0.5 rounded bg-black/50 border border-[#E5D6BC]/20 text-sky-300">
                      {row.mod}
                    </span>
                  </div>
                  <p className="text-[11px] text-[#d6cebf] leading-relaxed font-sans">
                    {row.desc}
                  </p>
                </div>
                <div className="pt-1 flex items-center justify-between text-[10px] font-mono text-emerald-400">
                  <span>DURUM: DOĞRULANDI</span>
                  <span>PASS (%100)</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 6. NEW: Simulation (Nominal) vs. Real Vehicle Field Calibration Tolerances */}
        <div className="space-y-3 pt-6 border-t border-[#E5D6BC]/15">
          <div className="pb-2 border-b border-[#E5D6BC]/15">
            <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
              // {lang === "tr" ? "MÜHENDİSLİK ŞEFFAFLIĞI // SİMÜLASYON VE SAHA KALİBRASYON TOLERANSLARI" : "ENGINEERING TRANSPARENCY // SIMULATION VS. FIELD CALIBRATION TOLERANCES"}
            </div>
            <h2 className="text-base sm:text-lg font-bold text-white tracking-tight">
              {lang === "tr"
                ? "Simülasyon (İdeal / Nominal) Değerleri ile Gerçek Araç Saha Kalibrasyon Aralıkları"
                : "Simulation (Nominal) Benchmarks vs. Physical Vehicle Field Calibration Ranges"}
            </h2>
          </div>

          <div className="overflow-x-auto rounded-xl border border-[#E5D6BC]/20 bg-[#18140e]">
            <table className="w-full text-left border-collapse text-xs">
              <thead>
                <tr className="bg-[#251f18] text-[#E5D6BC] font-mono text-[10px] uppercase border-b border-[#E5D6BC]/20">
                  <th className="py-2.5 px-3">Emniyet ve Kontrol Parametresi</th>
                  <th className="py-2.5 px-3">İlgili Kod Modülü</th>
                  <th className="py-2.5 px-3">Simülasyon (İdeal / Nominal)</th>
                  <th className="py-2.5 px-3">Gerçek Araç Beklenen Saha Aralığı</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#E5D6BC]/10 text-[11px]">
                {simVsFieldRows.map((r, i) => (
                  <tr key={i} className="hover:bg-white/[0.02]">
                    <td className="py-2.5 px-3 font-semibold text-white">{r.param}</td>
                    <td className="py-2.5 px-3 font-mono text-sky-300">{r.mod}</td>
                    <td className="py-2.5 px-3 font-mono text-emerald-400 font-semibold">{r.sim}</td>
                    <td className="py-2.5 px-3 text-[#d6cebf]">{r.field}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* 7. Architecture & Safety Protocols (KUTUSUZ EDİTORYAL ÇİFT SÜTUN) */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 pt-6 border-t border-[#E5D6BC]/15">
          
          {/* CAN-FD Integration */}
          <div className="space-y-3">
            <div className="border-b border-[#E5D6BC]/15 pb-2">
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "SAIC MAXUS MIFA 7 & E-GMP CAN-FD ENTEGRASYONU" : "SAIC MAXUS MIFA 7 & E-GMP CAN-FD ARCHITECTURE"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "Sıfır Delme & Çift Yedekli Şasi Uyumu" : "Zero-Drill & Fail-Operational Integration"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-[#d6cebf] divide-y divide-[#E5D6BC]/10">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "100 Hz CAN-FD & Çift Yedekli Fren:" : "100 Hz CAN-FD & Redundant Braking:"}</b>{" "}
                  {lang === "tr"
                    ? "Şasi CAN-FD hattına 100 Hz direksiyon (EPS) ve birincil i-Booster / ikincil ESC hidrolik pompa + EPB yedekli fren sinyali iletilir."
                    : "Transmits 100 Hz steering (EPS) and fail-operational primary i-Booster / secondary ESC hydraulic pump + EPB brake commands."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Kabin Kapı Kilidi (Door Interlock) & BMS:" : "Cabin Door Interlock & EV BMS:"}</b>{" "}
                  {lang === "tr"
                    ? "Kapı veya bagaj açıkken ya da yolcu kemeri takılı değilken kalkış kilitlenir; batarya SoC <%18 olduğunda araç otomatik şarj istasyonuna yönlendirilir."
                    : "Locks drive if any door/trunk is unlatched or seatbelt unfastened; automatically routes to depot charger when SoC drops below 18%."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Kapalı Kutu (.pyc) Enterprise SDK Dağıtımı:" : "Closed-Box (.pyc) Enterprise SDK Delivery:"}</b>{" "}
                  {lang === "tr"
                    ? "Açık kaynak kodlar paylaşılmaz; OEM ve filo ortaklarına HMAC-SHA256 donanım kilitli kapalı kutu (.pyc) değerlendirme ve üretim paketi sunulur."
                    : "Delivered strictly as HMAC-SHA256 hardware-locked compiled bytecode (.pyc) preserving 100% sovereign intellectual property."}
                </span>
              </li>
            </ul>
          </div>

          {/* Safety & Human Takeover */}
          <div className="space-y-3">
            <div className="border-b border-[#E5D6BC]/15 pb-2">
              <div className="text-[10px] font-mono text-[#E5D6BC] font-semibold tracking-wider uppercase">
                // {lang === "tr" ? "GÜVENLİK VE DEVİR PROTOKOLLERİ" : "SAFETY & TAKEOVER PROTOCOLS"}
              </div>
              <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
                {lang === "tr" ? "5ms Sürücü Devralma, 50ms Watchdog ve MRM" : "5ms Driver Override, 50ms Watchdog & MRM"}
              </h3>
            </div>

            <ul className="space-y-2.5 text-xs text-[#d6cebf] divide-y divide-[#E5D6BC]/10">
              <li className="pt-2 first:pt-0 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "Anlık Sürücü Müdahalesi (<=5ms):" : "Instant Human Takeover (<=5ms):"}</b>{" "}
                  {lang === "tr"
                    ? "Direksiyona 2.0 Nm üzeri tork uygulandığında veya fren pedalına basıldığında otonomi 5 milisaniyede kontrolü sürücüye bırakır (ISO 26262 ASIL-D)."
                    : "Manual steering torque (>2.0 Nm) or brake depression instantly disengages autonomy within 5ms under ISO 26262 ASIL-D."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "20ms Öz-Denetim & 50ms Watchdog MRM:" : "20ms Self-Check & 50ms Watchdog MRM:"}</b>{" "}
                  {lang === "tr"
                    ? "50 ms komut kesintisinde dörtlü flaşörler açılır, araç 1.5 m/s² kontrollü yavaşlama ile sağa çekilir ve UN R157 SHA-256 kara kutu kaydı alır."
                    : "On 50ms heartbeat timeout, hazard lights engage, vehicle executes 1.5 m/s² MRM pullover, and UN R157 SHA-256 blackbox logs the event."}
                </span>
              </li>
              <li className="pt-2 flex items-start gap-2.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#E5D6BC] shrink-0 mt-0.5" />
                <span>
                  <b className="text-white font-medium">{lang === "tr" ? "ODD Coğrafi Çit & Uzaktan Operasyon (Teleop):" : "ODD Geofencing & Remote Teleoperation:"}</b>{" "}
                  {lang === "tr"
                    ? "Tanımlı ODD koridoru dışına çıkışta güvenli duruş başlatılır; çağrı merkezi operatörü <=15 km/s hız ve <=150 ms RTT sınırı ile uzaktan destek verir."
                    : "Enforces ODD geofence limits and supports authenticated remote teleoperation recovery capped at <=15 km/h and <=150 ms RTT."}
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* 8. Institutional NDA Technical Cooperation Bar */}
        <div className="py-6 px-6 sm:px-8 rounded-2xl bg-gradient-to-r from-[#282017] via-[#352a1e] to-[#282017] border border-[#E5D6BC]/30 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="space-y-1 text-center md:text-left max-w-2xl">
            <div className="text-[10px] font-mono text-[#E5D6BC] uppercase tracking-wider font-semibold">
              // {lang === "tr" ? "KURUMSAL TEKNİK İŞBİRLİĞİ & KAPALI KUTU DEĞERLENDİRME SDK'SI" : "INSTITUTIONAL TECHNICAL COOPERATION & CLOSED-BOX EVALUATION SDK"}
            </div>
            <h3 className="text-sm sm:text-base font-bold text-white tracking-tight">
              {lang === "tr" ? "Tam Yazılım Envanteri, 1.307 + 21 Test Kanıt Dosyası ve Kapalı Kutu SDK" : "Full Software Inventory, 1,307 + 21 Test Evidence Dossier & Closed-Box SDK"}
            </h3>
            <p className="text-[#d6cebf] text-xs leading-relaxed">
              {lang === "tr"
                ? "198 dosyalık tam modül çizelgesi, CAN-FD DBC sözlüğü ve 21 alt sistem testini kendi bilgisayarınızda 1 dakikada doğrulayabileceğiniz derlenmiş kapalı kutu (.pyc) Robotaksi SDK paketi karşılıklı Gizlilik Sözleşmesi (NDA) kapsamında sunulmaktadır."
                : "Our 198-file module inventory, CAN-FD DBC dictionary, and compiled closed-box (.pyc) Robotaxi Evaluation SDK with 21 automated subsystem tests are available under mutual NDA."}
            </p>
          </div>

          <Link
            href="/iletisim/"
            className="w-full sm:w-auto px-5 py-2.5 rounded-lg bg-[#E5D6BC] text-[#14120c] hover:bg-white font-bold text-xs tracking-wider uppercase transition-colors inline-flex items-center justify-center gap-1.5 shrink-0 shadow-lg"
          >
            <Lock className="w-3.5 h-3.5" />
            <span>{lang === "tr" ? "NDA İLE SDK TALEP ET" : "REQUEST SDK VIA NDA"}</span>
          </Link>
        </div>

      </div>

      <Footer />
    </main>
  );
}
