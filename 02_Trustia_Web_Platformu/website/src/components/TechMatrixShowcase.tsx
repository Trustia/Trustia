"use client";

import { Compass, Layers, Radar, Radio, Lock, Cpu, CloudRain, Wifi, Activity, ShieldCheck, Zap } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function TechMatrixShowcase() {
  const { lang } = useLanguage();

  const capabilities = [
    {
      id: "slam",
      icon: Compass,
      title: lang === "tr" ? "GPS'siz 3D Haritalama (SLAM)" : "GPS-Denied 3D SLAM",
      desc: lang === "tr"
        ? "Uydu sinyali veya internet olmasa dahi 3D LiDAR ve kameralarla santimetre hassasiyetinde haritalama ve anlık konum tayini."
        : "Centimeter-accurate real-time 3D mapping and localization using LiDAR and vision, operating independently of satellite GPS.",
      badge: lang === "tr" ? "0 Dış Bağımlılık" : "Zero Satellite Dependency"
    },
    {
      id: "prediction",
      icon: Activity,
      title: lang === "tr" ? "5 Saniyelik Yörünge & Niyet Tahmini" : "5-Second Trajectory & Intent AI",
      desc: lang === "tr"
        ? "Yayaların, bisikletlilerin ve araçların gelecekteki 5 saniyelik hareket yörüngesini ve niyetini önceden kestirerek sıfır kaza güvenliği sağlar."
        : "Multimodal probabilistic intent prediction modeling pedestrian and vehicle paths 5 seconds ahead for proactive collision avoidance.",
      badge: lang === "tr" ? "Öngörülü Güvenlik" : "Predictive Safety"
    },
    {
      id: "v2x",
      icon: Wifi,
      title: lang === "tr" ? "V2X Akıllı Şehir & Trafik Işığı Ağı" : "V2X Smart Infrastructure Engine",
      desc: lang === "tr"
        ? "Akıllı trafik ışıklarından (SPaT/GLOSA) anlık sinyal sürelerini alır, acil araçlara (ambulans/polis) yol verir ve araçlar arası acil frenleme paylaşır."
        : "C-V2X & DSRC engine communicating directly with smart traffic lights, optimizing green waves and broadcasting emergency braking alerts.",
      badge: lang === "tr" ? "C-V2X / SPaT / GLOSA" : "Connected V2X"
    },
    {
      id: "weather",
      icon: CloudRain,
      title: lang === "tr" ? "Zorlu Hava & Çamur Telafi Filtresi" : "Adverse Weather & Lens Compensation",
      desc: lang === "tr"
        ? "Yoğun sis, sağanak yağmur ve kamera lensine sıçrayan çamurda sensör körleşmesini anında algılayıp 77 GHz Radar ve LiDAR ağırlıklarını artırır."
        : "Dynamic sensor degradation adaptation compensating for dense fog, heavy rain, and lens occlusion with adaptive radar/LiDAR gain.",
      badge: lang === "tr" ? "Sis / Yağmur / Çamur" : "All-Weather Robust"
    },
    {
      id: "teleop",
      icon: Radio,
      title: lang === "tr" ? "Uzaktan Müdahale & Filo Teleoperasyonu" : "Remote Teleoperation & Fleet C2",
      desc: lang === "tr"
        ? "Karmaşık yol çalışmalarında merkezdeki operatörün araca uzaktan alternatif yol çizmesini veya güvenle kontrolü devralmasını sağlayan düşük gecikmeli köprü."
        : "Low-latency WebRTC teleoperation bridge enabling remote human-in-the-loop path guidance and hardware-level safety watchdog intervention.",
      badge: lang === "tr" ? "Düşük Gecikmeli C2" : "Low-Latency Teleop"
    },
    {
      id: "tested",
      icon: ShieldCheck,
      title: lang === "tr" ? "1.301 Doğrulanmış Test & Siber Güvenlik" : "1,301 Verified Tests & Security",
      desc: lang === "tr"
        ? "16.000+ satır özgün deterministik otonomi mimarisi, HMAC-SHA256 şifreli komut doğrulama ve %100 başarı oranına sahip 1.301 otomatik test."
        : "16,000+ lines of original deterministic code, cryptographic command validation, and 100% pass rate across 1,301 automated test suites.",
      badge: lang === "tr" ? "%100 Test Başarısı" : "100% Pass Rate"
    }
  ];

  return (
    <section id="teknoloji" className="relative z-20 py-16 sm:py-20 px-4 sm:px-8 bg-[#07090c] border-b border-white/10">
      <div className="max-w-6xl mx-auto space-y-12">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto space-y-3">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
            <span>{lang === "tr" ? "TEKNOLOJİK ÇEKİRDEK & MODÜLLER" : "CORE TECHNOLOGY & MODULES"}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            {lang === "tr" ? "Güvenilir, Deterministik Otonomi Mimarisi" : "Deterministic, Battle-Tested Autonomy Core"}
          </h2>
          <p className="text-sm text-slate-400 font-normal leading-relaxed">
            {lang === "tr"
              ? "Her türlü hava, trafik ve harekat koşulunda hatasız çalışan Seviye 4 yerli yazılım katmanlarımız."
              : "Level-4 sovereign autonomy software layers designed for flawless operation across all traffic, tactical, and weather conditions."}
          </p>
        </div>

        {/* 6 Clean Corporate Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {capabilities.map((item) => {
            const Icon = item.icon;
            return (
              <div
                key={item.id}
                className="p-6 rounded-xl bg-[#0c0f14] border border-white/10 hover:border-white/20 transition-all duration-300 flex flex-col justify-between space-y-4 group"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <div className="w-10 h-10 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-300 group-hover:text-white transition-colors">
                      <Icon className="w-5 h-5" />
                    </div>
                    <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-white/5 border border-white/5">
                      {item.badge}
                    </span>
                  </div>

                  <h3 className="text-base font-bold text-white tracking-tight">
                    {item.title}
                  </h3>

                  <p className="text-xs text-slate-400 font-normal leading-relaxed">
                    {item.desc}
                  </p>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
