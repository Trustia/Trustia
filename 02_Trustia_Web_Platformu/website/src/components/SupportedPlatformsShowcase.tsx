"use client";

import { Car, Shield, Tractor, ArrowRight, CheckCircle2 } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function SupportedPlatformsShowcase() {
  const { lang } = useLanguage();

  const solutions = [
    {
      id: "civilian",
      icon: Car,
      title: lang === "tr" ? "Sivil Mobilite & Robotaksi" : "Urban Mobility & Robotaxi",
      subtitle: lang === "tr" ? "Şehir İçi Seviye 4 Otonom Filolar" : "Level 4 Autonomous City Fleets",
      desc: lang === "tr"
        ? "Binek ve elektrikli otomobiller için geliştirilen tak-çalıştır otonom sürüş beyni. Şehir içi yolcu taşımacılığı, servis hatları ve otonom taksi operasyonları."
        : "Plug-and-play autonomous driving core for passenger and electric vehicles. Tailored for urban ride-hailing, campus shuttles, and autonomous taxi fleets.",
      highlights: lang === "tr"
        ? ["Elektronik Direksiyon (Drive-by-Wire)", "Trafik Işığı & Yaya Algılama", "Dinamik Rota Planlama"]
        : ["Drive-by-Wire CAN Integration", "Traffic Light & Pedestrian AI", "Dynamic Route Planning"],
      vehicles: "TOGG, Mercedes, Toyota, Hyundai, Tesla"
    },
    {
      id: "defense",
      icon: Shield,
      title: lang === "tr" ? "Savunma & İnsansız Kara Araçları (İKA)" : "Defense & Unmanned Ground Vehicles",
      subtitle: lang === "tr" ? "GPS Olmayan Sahalarda Tam Otonomi" : "Full Autonomy in GPS-Denied Theaters",
      desc: lang === "tr"
        ? "Elektronik harp ve uydu sinyalinin kesildiği çatışma alanlarında; 3D LiDAR SLAM ve sürü zekası ile görev yapan zırhlı savunma robotları."
        : "Designed for electronic warfare and GPS-jammed operational zones; armored defense robots powered by 3D LiDAR SLAM and swarm intelligence.",
      highlights: lang === "tr"
        ? ["GPS-Sinyalsiz 3D SLAM Haritalama", "Sürü Koordinasyonu (Swarm)", "Askeri JAUS & ROS 2 Uyumu"]
        : ["GPS-Denied 3D SLAM Mapping", "Multi-Agent Swarm Consensus", "NATO STANAG & JAUS Compliance"],
      vehicles: "Hafif, Orta ve Ağır Sınıf Taktik İKA'lar"
    },
    {
      id: "industrial",
      icon: Tractor,
      title: lang === "tr" ? "Endüstri, Maden & Tarım" : "Industry, Mining & Agriculture",
      subtitle: lang === "tr" ? "Zorlu Sahalarda 7/24 Sürücüsüz Çalışma" : "24/7 Driverless Heavy Operations",
      desc: lang === "tr"
        ? "Maden ocakları, liman lojistiği ve tarım arazilerinde insan hayatını riske atmadan 7/24 kesintisiz çalışan ağır hizmet otonomi sistemleri."
        : "Heavy-duty autonomous logistics operating 24/7 across open-pit mines, seaport terminals, and large-scale precision agriculture without human risk.",
      highlights: lang === "tr"
        ? ["Ağır Arazi ve Çamur Algılama", "Otonom Konvoy & Yük Taşıma", "Gece / Sisli Görüş Desteği"]
        : ["Off-Road Terrain Navigation", "Autonomous Convoy Logistics", "Thermal Night & Fog Vision"],
      vehicles: "Maden Kamyonları, Otonom Traktörler, AGV"
    }
  ];

  return (
    <section id="otonomi" className="relative z-20 py-16 sm:py-20 px-4 sm:px-8 bg-[#090b0e] border-b border-white/10">
      <div className="max-w-6xl mx-auto space-y-12">
        
        {/* Executive Clean Header */}
        <div className="text-center max-w-3xl mx-auto space-y-3">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-[11px] font-mono tracking-wider uppercase">
            <span>{lang === "tr" ? "UYGULAMA ALANLARI & ÇÖZÜMLER" : "APPLICATIONS & SOLUTIONS"}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            {lang === "tr" ? "Ne Yapıyoruz? Hangi Alanlarda Çalışıyoruz?" : "What We Do & Where We Operate"}
          </h2>
          <p className="text-sm text-slate-400 font-normal leading-relaxed">
            {lang === "tr"
              ? "Trustia AI; donanım bağımsız evrensel bir otonomi beynidir. Standart CAN-Bus ve Drive-by-Wire haberleşmesi ile her türlü aracı tam otonom hale getirir."
              : "Trustia AI is a universal, hardware-agnostic autonomy core. It transforms commercial, defense, and industrial vehicles into fully autonomous systems."}
          </p>
        </div>

        {/* 3 Calm, High-Status Corporate Solution Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {solutions.map((item) => {
            const Icon = item.icon;
            return (
              <div
                key={item.id}
                className="p-6 sm:p-7 rounded-2xl bg-[#0d1017] border border-white/10 hover:border-white/20 transition-all duration-300 flex flex-col justify-between space-y-6 group"
              >
                <div className="space-y-4">
                  {/* Icon & Title */}
                  <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-200 group-hover:text-white transition-colors">
                    <Icon className="w-6 h-6" />
                  </div>

                  <div>
                    <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider block mb-1">
                      {item.subtitle}
                    </span>
                    <h3 className="text-lg font-bold text-white tracking-tight">
                      {item.title}
                    </h3>
                  </div>

                  <p className="text-xs sm:text-sm text-slate-400 font-normal leading-relaxed">
                    {item.desc}
                  </p>

                  {/* Key Highlights */}
                  <div className="pt-2 space-y-2 border-t border-white/5">
                    {item.highlights.map((h, i) => (
                      <div key={i} className="flex items-center gap-2 text-xs text-slate-300">
                        <CheckCircle2 className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                        <span>{h}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Footer Tag */}
                <div className="pt-4 border-t border-white/5 text-[11px] font-mono text-slate-500">
                  <span className="text-slate-400 font-medium">
                    {lang === "tr" ? "Uyumlu: " : "Platforms: "}
                  </span>
                  {item.vehicles}
                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
