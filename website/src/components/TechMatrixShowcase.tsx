"use client";

import { useState } from "react";
import { Compass, Radar, Radio, Lock, Cpu, Activity, CheckCircle2, ShieldCheck, Zap, Terminal, Layers, Crosshair } from "lucide-react";

export default function TechMatrixShowcase() {
  const [activeTab, setActiveTab] = useState<"all" | "otonomi" | "tehdit" | "suru" | "siber" | "test">("all");

  const techFeatures = [
    {
      id: "slam",
      category: "otonomi",
      number: "01",
      badge: "KONUMLANMA & NAVİGASYON",
      title: "GPS'siz 3D SLAM & Görsel Odometri",
      desc: "LiDAR, Stereoskopik Kameralar ve IMU sensör füzyonu ile GPS uydularının engellendiği harekat sahalarında santimetre hassasiyetinde 3D haritalama ve poz tahmini.",
      tags: ["ICP 3D Scan Matching", "Poz Grafı Optimizasyonu", "Görsel Odometri (VO)", "NDT Haritalama"],
      metric: "99.94%",
      metricLabel: "Konum Doğruluğu",
      icon: Compass,
    },
    {
      id: "planning",
      category: "otonomi",
      number: "02",
      badge: "ROTA PLANLAMA",
      title: "Kinematik Hybrid A* & RRT* Rota Algoritması",
      desc: "Araç fiziki dönüş yarıçapı, arazi eğimi ve engebeyi dikkate alan dinamik kinematik rota planlama ve canlı engel engelleme mekanizması.",
      tags: ["Hybrid A*", "RRT* Pathfinding", "DWA Lokal Kaçınma", "Dinamik Costmap"],
      metric: "<15ms",
      metricLabel: "Yeniden Hesaplama",
      icon: Layers,
    },
    {
      id: "threat",
      category: "tehdit",
      number: "03",
      badge: "SAHA TEHDİT FÜZYONU",
      title: "EYP, Mayın & KHKN Gaz Tespiti",
      desc: "GPR radar, metal indüksiyonu ve termal anomali verileriyle patlayıcı tuzak algılama ve Rüzgar Altı Gaz Yayılım (Plume) modellemesiyle 30m emniyet çemberi.",
      tags: ["GPR Radar Verisi", "Termal Anomali", "Plume Dispersion", "Otomatik Karantina"],
      metric: "30m",
      metricLabel: "Tehdit Çemberi",
      icon: Radar,
    },
    {
      id: "swarm",
      category: "suru",
      number: "04",
      badge: "ÇOKLU KOORDİNASYON",
      title: "Hava-Kara Hibrit Sürü Zekası",
      desc: "İHA keşif verileri ile İKA harekatını senkronize eden, Kama, Saf, Kolon ve Baklava formasyonlarında taktik çoklu araç koordinasyon algoritması.",
      tags: ["İHA-İKA Senkronizasyonu", "Mesh Ad-Hoc Ağ", "Çoklu Araç Konsensüsü", "Taktik Formasyon"],
      metric: "16 İKA",
      metricLabel: "Eşzamanlı Sürü",
      icon: Radio,
    },
    {
      id: "cyber",
      category: "siber",
      number: "05",
      badge: "KORUMA & FAIL-SAFE",
      title: "HMAC-SHA256 Kripto & LinkLoss RTH",
      desc: "Şifrelenmiş komut paketi doğrulaması, Jamming/Spoofing koruması ve telsiz kesintilerinde 3D SLAM geçmiş rotasıyla otonom eve dönüş (RTH) emniyeti.",
      tags: ["HMAC-SHA256", "Anti-Jamming Direnci", "LinkLoss RTH", "Donanımsal E-Stop"],
      metric: "3sn",
      metricLabel: "Fail-Safe Tetikleme",
      icon: Lock,
    },
    {
      id: "ros2",
      category: "test",
      number: "06",
      badge: "MİMARİ VE SAHA TESTLERİ",
      title: "ROS 2 Humble / CAN FD & Saha Metrikleri",
      desc: "Yerli C++20 çekirdeği üzerinde mikro-saniye gecikmeli RTOS gerçek zamanlı çalıştırıcı ve 1.200 saatin üzerinde kesintisiz saha ve iklim stres testleri.",
      tags: ["ROS 2 Humble Core", "CAN FD Bus", "Zero-Copy IPC", "STANAG 4586 L4"],
      metric: "1,200+ Saat",
      metricLabel: "Saha Stres Testi",
      icon: Cpu,
    },
  ];

  const filteredFeatures = activeTab === "all" ? techFeatures : techFeatures.filter(f => f.category === activeTab);

  return (
    <section id="otonomi" className="relative z-20 py-24 px-6 sm:px-12 bg-[#090b0e] border-t border-white/10">
      {/* Background Subtle Radar Lines */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(200,255,0,0.05),rgba(255,255,255,0))]" />

      <div className="max-w-6xl mx-auto relative z-10">
        
        {/* Section Title & Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-xs font-mono font-bold tracking-widest uppercase mb-3">
              <Crosshair className="w-3.5 h-3.5" />
              <span>MİLLİ OTONOMİ MİMARİSİ VE TEKNİK KAPASİTE MATRIXI</span>
            </div>
            <h3 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight">
              Tüm Askeri Alt Sistem & Algoritma Katmanları
            </h3>
          </div>
          <p className="text-slate-400 text-xs sm:text-sm font-normal max-w-md leading-relaxed border-l-2 border-[#C8FF00] pl-4">
            GPS sinyalinin olmadığı harekat ortamlarında sıfır dış bağımlılıkla çalışan 6 ana teknoloji katmanı ve 1,200+ saatlik saha doğrulama metrikleri.
          </p>
        </div>

        {/* Filter Tabs */}
        <div className="flex flex-wrap items-center gap-2 mb-10 border-b border-white/10 pb-4">
          <button
            onClick={() => setActiveTab("all")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "all"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            TÜM SİSTEMLER (6 KATMAN)
          </button>
          <button
            onClick={() => setActiveTab("otonomi")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "otonomi"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            OTONOMİ & SLAM
          </button>
          <button
            onClick={() => setActiveTab("tehdit")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "tehdit"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            TEHDİT FÜZYONU
          </button>
          <button
            onClick={() => setActiveTab("suru")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "suru"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            SÜRÜ ZEKASI
          </button>
          <button
            onClick={() => setActiveTab("siber")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "siber"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            SİBER KORUMA
          </button>
          <button
            onClick={() => setActiveTab("test")}
            className={`px-4 py-2 rounded-xl text-xs font-mono font-bold tracking-wider transition-all cursor-pointer ${
              activeTab === "test"
                ? "bg-[#C8FF00] text-black shadow-[0_0_20px_rgba(200,255,0,0.3)]"
                : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
            }`}
          >
            SAHA & RTOS
          </button>
        </div>

        {/* 6 Grid Technology Matrix */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredFeatures.map((item) => {
            const ItemIcon = item.icon;
            return (
              <div
                key={item.id}
                className="p-7 rounded-2xl bg-[#0c0f16] border border-white/10 hover:border-[#C8FF00]/50 transition-all duration-300 group flex flex-col justify-between hover:shadow-[0_10px_30px_rgba(200,255,0,0.1)] relative overflow-hidden"
              >
                {/* Background Number Accent */}
                <div className="absolute top-2 right-4 font-mono font-black text-6xl text-white/[0.03] select-none pointer-events-none group-hover:text-[#C8FF00]/10 transition-colors">
                  {item.number}
                </div>

                <div>
                  {/* Top Badge & Metric Card */}
                  <div className="flex items-center justify-between mb-5">
                    <div className="w-12 h-12 rounded-xl bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] flex items-center justify-center group-hover:bg-[#C8FF00] group-hover:text-black transition-all">
                      <ItemIcon className="w-6 h-6" />
                    </div>

                    <div className="text-right">
                      <div className="font-mono text-base font-extrabold text-[#C8FF00]">
                        {item.metric}
                      </div>
                      <div className="font-mono text-[10px] text-slate-400 uppercase tracking-wider">
                        {item.metricLabel}
                      </div>
                    </div>
                  </div>

                  {/* Sub-Title Badge */}
                  <div className="font-mono text-[11px] font-bold text-[#C8FF00] uppercase tracking-wider mb-2">
                    {item.number} // {item.badge}
                  </div>

                  {/* Feature Title */}
                  <h4 className="text-xl font-extrabold text-white mb-3 tracking-tight group-hover:text-[#C8FF00] transition-colors leading-snug">
                    {item.title}
                  </h4>

                  {/* Feature Description */}
                  <p className="text-slate-300 text-xs sm:text-sm leading-relaxed mb-6 font-normal">
                    {item.desc}
                  </p>
                </div>

                {/* Sub-system Tags & Compliance Badges */}
                <div className="space-y-3 border-t border-white/10 pt-4">
                  <div className="flex flex-wrap gap-1.5">
                    {item.tags.map((tag, idx) => (
                      <span
                        key={idx}
                        className="px-2.5 py-1 rounded bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono font-medium flex items-center gap-1.5"
                      >
                        <CheckCircle2 className="w-3 h-3 text-[#C8FF00]" />
                        <span>{tag}</span>
                      </span>
                    ))}
                  </div>
                </div>

              </div>
            );
          })}
        </div>

        {/* Bottom Total Capability Summary Bar */}
        <div className="mt-12 p-6 sm:p-8 rounded-2xl bg-white/[0.02] border border-white/10 flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="flex items-center gap-4">
            <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 shrink-0">
              <ShieldCheck className="w-6 h-6" />
            </div>
            <div>
              <h5 className="font-bold text-white text-base tracking-tight mb-1">
                %100 Yerli ve Savunma Sanayii Başkanlığı Kriterlerine Tam Uyumlu
              </h5>
              <p className="text-slate-400 text-xs font-normal max-w-xl leading-relaxed">
                STANAG 4586 Level 4, SAE AS6091 JAUS, ROS 2 Humble ve CAN FD haberleşme protokollerine tam uyumlu yerli yazılım çekirdeği.
              </p>
            </div>
          </div>

          <a
            href="#iletisim"
            className="px-6 py-3 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all shrink-0 cursor-pointer"
          >
            ENTEGRASYON TALEBİ GÖNDER
          </a>
        </div>

      </div>
    </section>
  );
}
