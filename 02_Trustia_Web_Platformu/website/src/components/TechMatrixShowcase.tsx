"use client";

import { useLanguage } from "@/context/LanguageContext";
import { Terminal, ShieldCheck, CheckCircle2, Cpu, Activity, Lock, Compass, Wifi } from "lucide-react";

export default function TechMatrixShowcase() {
  const { lang } = useLanguage();

  const specs = [
    {
      num: "01",
      icon: Compass,
      tag: "SPATIAL SLAM",
      metric: "400 Hz ESKF • ±4.2 cm / 60s",
      title: lang === "tr" ? "GNSS-Denied 3D LiDAR SLAM ve NDT Haritalama" : "GNSS-Denied 3D LiDAR SLAM & NDT Mapping",
      desc: lang === "tr"
        ? "Uydu ve GPS sinyalinin tamamen kesildiği tüneller, kapalı otoparklar ve kentsel kanyonlarda; araç üzerindeki çoklu 3D LiDAR ve 400 Hz ESKF IMU sensör füzyonu ile santimetre hassasiyetinde kesintisiz yerel seyrüsefer icra eder."
        : "Maintains centimeter-accurate spatial navigation independent of satellite GNSS signals across tunnels, indoor structures, and dense urban corridors via multi-3D LiDAR NDT matching and 400 Hz ESKF IMU fusion.",
      details: [
        { label: lang === "tr" ? "Sensör Mimarisi" : "Sensor Array", val: "Livox Mid-360 / Ouster OS2" },
        { label: lang === "tr" ? "Drift Toleransı" : "Drift Ceiling", val: "±4.2 cm / 60s" },
        { label: lang === "tr" ? "Uydu Bağımlılığı" : "GNSS Dependency", val: "%0 (Tam Bağımsız)" },
      ],
    },
    {
      num: "02",
      icon: Activity,
      tag: "TRAJECTORY CORE",
      metric: "5.0s Horizon • Voronoi Corridor",
      title: lang === "tr" ? "Deterministik Yörünge ve Güvenlik Koridoru Planlama" : "Deterministic Trajectory & Voronoi Planning",
      desc: lang === "tr"
        ? "Kestirilemez kara kutu modeller yerine; her senaryoda önceden doğrulanabilir Hybrid A*, Voronoi geometri koridorları ve Stanley kinematik kontrolcü mimarisiyle 5 saniyelik zaman ufkunda matematiksel olarak kazasız rota üretir."
        : "Eliminates heuristic hallucinations through mathematically verifiable Hybrid A* search, dynamic Voronoi spatial clearance corridors, and Stanley steering tracking controllers over a 5-second lookahead horizon.",
      details: [
        { label: lang === "tr" ? "Planlama Ufku" : "Lookahead Horizon", val: "5.0 saniye (Dinamik)" },
        { label: lang === "tr" ? "Kontrol Algoritması" : "Tracking Controller", val: "Stanley & MPC Kinematik" },
        { label: lang === "tr" ? "Yaya Güvenliği" : "VRU Compliance", val: "EU AI Act Standart" },
      ],
    },
    {
      num: "03",
      icon: ShieldCheck,
      tag: "FUNCTIONAL SAFETY",
      metric: "ISO 26262 ASIL-D • < 5.0 ms",
      title: lang === "tr" ? "ISO 26262 ASIL-D Emniyet Mimarisi ve Donanımsal Kesme" : "ISO 26262 ASIL-D Safety & Hardware Interrupt",
      desc: lang === "tr"
        ? "Fiziksel emniyet sürücüsünün direksiyon veya fren pedalına uygulayacağı en ufak müdahalede (2.5 Nm üzeri tork), donanımsal kesme rölesi 5 milisaniye içinde kontrolü sürücüye devreder. 200ms telemetri kesintisinde otomatik kontrollü duruş (MRM) başlatılır."
        : "An isolated hardware safety relay yields vehicle control to the human safety operator within 5 milliseconds upon detecting manual steering torque (>2.5 Nm). Communication latency exceeding 200ms triggers an automated Minimum Risk Maneuver (MRM).",
      details: [
        { label: lang === "tr" ? "Devralma Gecikmesi" : "Override Latency", val: "< 5.0 ms (Donanımsal)" },
        { label: lang === "tr" ? "Acil Durum Zamanlayıcı" : "Watchdog Timeout", val: "200 ms MRM Güvenli Duruş" },
        { label: lang === "tr" ? "Emniyet Seviyesi" : "Safety Integrity", val: "ISO 26262 ASIL-D Sertifikasyon" },
      ],
    },
    {
      num: "04",
      icon: Lock,
      tag: "CYBER SECURITY",
      metric: "ISO 21434 • HMAC-SHA256",
      title: lang === "tr" ? "SecOC Kriptografik Araç İçi İletişim Güvenliği" : "SecOC Cryptographic CAN-FD Security",
      desc: lang === "tr"
        ? "Gaz, fren ve direksiyon aktüatör komutları donanımsal HSM üzerinde HMAC-SHA256 ve dinamik sayaç rotasyonu ile şifrelenir. Araya girme (MitM) ve sahte paket tekrarı (Replay) siber saldırılarını mikro saniyede engeller."
        : "Actuation commands across steering, throttle, and braking are cryptographically signed using hardware HSMs, HMAC-SHA256 message authentication codes, and monotonic freshness counters to stop frame injection and replay attacks.",
      details: [
        { label: lang === "tr" ? "Kriptografik Algoritma" : "Cipher Standard", val: "HMAC-SHA256 / AES-128" },
        { label: lang === "tr" ? "Uluslararası Norm" : "Automotive Norms", val: "ISO 21434 & UN ECE R155" },
        { label: lang === "tr" ? "Donanım Koruması" : "Hardware Protection", val: "Secure Boot & HSM Entegre" },
      ],
    },
    {
      num: "05",
      icon: Wifi,
      tag: "CONNECTED V2X",
      metric: "C-V2X / SPaT • < 10 ms",
      title: lang === "tr" ? "C-V2X ve Akıllı Şehir Altyapı Senkronizasyonu" : "C-V2X Smart Infrastructure Synchronization",
      desc: lang === "tr"
        ? "Akıllı trafik ışıklarından (SPaT/GLOSA) milisaniye seviyesinde sinyal sürelerini alarak yeşil dalga hız optimizasyonu yapar; acil durum araçları ve diğer otonom filolarla güvenli telemetri köprüsü kurar."
        : "Interfaces directly with municipal traffic signal controllers (SPaT/GLOSA) for green-wave corridor speed optimization and broadcasts secure telemetry to emergency fleets with sub-10ms latency.",
      details: [
        { label: lang === "tr" ? "Protokol Standardı" : "Datalink Protocol", val: "ETSI ITS-G5 / 3GPP C-V2X" },
        { label: lang === "tr" ? "Haberleşme Gecikmesi" : "Network Latency", val: "< 10 ms Uçtan Uca" },
        { label: lang === "tr" ? "Trafik Optimizasyonu" : "Corridor Sync", val: "SPaT / GLOSA Yeşil Dalga" },
      ],
    },
    {
      num: "06",
      icon: Terminal,
      tag: "HIL VERIFICATION",
      metric: "1,307 Tests • %100 Success",
      title: lang === "tr" ? "1.307 Testli Otomatik Doğrulama ve HIL Test Hattı" : "1,307-Suite Automated HIL Verification Pipeline",
      desc: lang === "tr"
        ? "Sıfır yabancı kapalı kütüphane bağımlılığıyla derlenen 16.000 satırlık C++20 çekirdeği; her derlemede donanım döngülü (HIL) ve matematiksel simülasyon testlerinden %100 başarıyla geçmektedir."
        : "Over 16,000 lines of sovereign C++20 kernel code validated across continuous automated Hardware-in-the-Loop (HIL) test suites with zero regression and 100% test pass rate prior to production vehicle deployment.",
      details: [
        { label: lang === "tr" ? "Doğrulama Kapsamı" : "Test Suites", val: "1.307 / 1.307 (%100 Geçti)" },
        { label: lang === "tr" ? "Test Metodolojisi" : "Bench Methodology", val: "HIL (Hardware-in-the-Loop)" },
        { label: lang === "tr" ? "Kod Bütünlüğü" : "Kernel Integrity", val: "Regresyonsuz C++20 Çekirdek" },
      ],
    },
  ];

  return (
    <section id="teknoloji" className="relative z-20 py-20 sm:py-28 px-4 sm:px-8 lg:px-12 bg-[#07090d] border-b border-white/10">
      <div className="max-w-7xl mx-auto space-y-12 sm:space-y-16">
        
        {/* Executive Split Header */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start pb-10 border-b border-white/10">
          
          {/* Left Title & Vision */}
          <div className="lg:col-span-7 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
              <span>{lang === "tr" ? "TEKNOLOJİ ÇEKİRDEĞİ // MİMARİ ŞARTNAME" : "CORE ARCHITECTURE // SPECIFICATIONS"}</span>
            </div>

            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-snug">
              {lang === "tr" ? (
                <>
                  Deterministik Seviye 4 <br />
                  <span className="text-slate-300 font-semibold">
                    Otonom Karar, Seyrüsefer ve Güvenlik Motoru
                  </span>
                </>
              ) : (
                <>
                  Deterministic Level-4 <br />
                  <span className="text-slate-300 font-semibold">
                    Autonomous Decision, Navigation & Safety Core
                  </span>
                </>
              )}
            </h2>

            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal">
              {lang === "tr"
                ? "Dışa bağımlı kara kutu kütüphaneler yerine; her adımı önceden simüle edilebilen, matematiksel sınırları tanımlı ve otomotiv fonksiyonel emniyet normlarıyla mühürlenmiş yerli otonomi omurgası."
                : "A deterministic autonomy backbone engineered with mathematically provable safety envelopes, zero foreign black-box dependencies, and strict compliance with automotive functional safety standards."}
            </p>
          </div>

          {/* Right Executive Architecture Summary Dossier */}
          <div className="lg:col-span-5 p-5 sm:p-6 rounded-2xl bg-[#0c0f15] border border-white/10 space-y-3 font-mono text-xs">
            <div className="flex items-center justify-between border-b border-white/10 pb-2.5">
              <span className="text-white font-semibold uppercase tracking-wider text-[11px]">
                {lang === "tr" ? "MİMARİ PERFORMANS GÖSTERGELERİ" : "ARCHITECTURE SPECIFICATIONS"}
              </span>
              <span className="text-emerald-400 font-semibold text-[10px] px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-800">
                v4.0 KERNEL
              </span>
            </div>

            <div className="space-y-2 text-[11px] divide-y divide-white/5">
              <div className="pt-2 first:pt-0 flex items-center justify-between">
                <span className="text-slate-400">{lang === "tr" ? "Yazılım Dili & Standart" : "Core Stack & Standard"}</span>
                <span className="text-slate-200 font-semibold">C++20 • ROS 2 Humble</span>
              </div>
              <div className="pt-2 flex items-center justify-between">
                <span className="text-slate-400">{lang === "tr" ? "Çevrim Frekansı (HAL)" : "Cycle Frequency"}</span>
                <span className="text-slate-200 font-semibold">100 Hz Senkron CAN-FD</span>
              </div>
              <div className="pt-2 flex items-center justify-between">
                <span className="text-slate-400">{lang === "tr" ? "Donanımsal Kesme Süresi" : "Interrupt Override Latency"}</span>
                <span className="text-slate-200 font-semibold">&lt; 5.0 ms (ASIL-D)</span>
              </div>
              <div className="pt-2 flex items-center justify-between">
                <span className="text-slate-400">{lang === "tr" ? "Otomatik Doğrulama Testi" : "Automated Verification"}</span>
                <span className="text-emerald-400 font-semibold">1.307 / 1.307 (%100 Başarı)</span>
              </div>
            </div>
          </div>

        </div>

        {/* Hairline Separated Engineering Architecture List (No Clunky Boxes!) */}
        <div className="divide-y divide-white/10">
          {specs.map((item, idx) => (
            <div key={idx} className="py-8 first:pt-0 last:pb-0 space-y-4">
              
              {/* Row Header: Number, Title, Metric Tag */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div className="flex items-center gap-3">
                  <span className="font-mono text-xs text-slate-500 font-bold">{item.num} //</span>
                  <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                    {item.title}
                  </h3>
                </div>

                <div className="flex items-center gap-2 self-start sm:self-auto">
                  <span className="text-[10px] font-mono text-slate-400 px-2.5 py-1 rounded bg-white/5 border border-white/10">
                    {item.metric}
                  </span>
                </div>
              </div>

              {/* Row Description */}
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed font-sans max-w-4xl sm:pl-8">
                {item.desc}
              </p>

              {/* 3-Point Technical Specifications Strip (Subtle & Monospaced) */}
              <div className="sm:pl-8 grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
                {item.details.map((detail, dIdx) => (
                  <div key={dIdx} className="p-3 rounded-lg bg-white/[0.02] border border-white/5 font-mono text-xs space-y-0.5">
                    <span className="text-[10px] text-slate-500 uppercase tracking-wider block">
                      {detail.label}:
                    </span>
                    <span className="text-slate-200 font-medium text-[11px] block">
                      {detail.val}
                    </span>
                  </div>
                ))}
              </div>

            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
