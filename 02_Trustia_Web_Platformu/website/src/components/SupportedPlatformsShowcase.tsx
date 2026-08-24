"use client";

import { Car, Shield, Tractor, Cpu, CheckCircle2, Zap, ArrowRight, Layers, Sliders } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function SupportedPlatformsShowcase() {
  const { t } = useLanguage();

  const categories = [
    {
      id: "civilian",
      icon: Car,
      number: "01",
      badge: t("plat_cat1_badge"),
      title: t("plat_cat1_title"),
      desc: t("plat_cat1_desc"),
      list: [
        "TOGG T10X / T10F (Yerli EV)",
        "Mercedes-Benz G-Serisi & Sprinter",
        "Toyota Corolla & RAV4 (Robotaxi)",
        "Lexus RX & Camry",
        "BMW 3 & 5 Serisi",
        "Ford Transit & Ranger",
        "Hyundai Ioniq 5/6 & Tesla EV",
        "Polaris GEM & Kampüs Servisleri"
      ],
      protocol: "SAE J1939 / CAN 2.0B / DbW",
    },
    {
      id: "defense",
      icon: Shield,
      number: "02",
      badge: t("plat_cat2_badge"),
      title: t("plat_cat2_title"),
      desc: t("plat_cat2_desc"),
      list: [
        "HAVELSAN BARKAN & BARKAN 2 (İKA)",
        "ASELSAN & FNSS ALPAR (Zırhlı İKA)",
        "HAVELSAN KAPGAN (8x8 Taktik)",
        "BMC Vuran & Kirpi (Otonom Konvoy)",
        "Otokar Enga & Cobra II (Keşif İKA)",
        "Best Grup Korhan & Fedai",
        "Clearpath Husky & Warthog",
        "NATO STANAG 4586 Uyumlu Şasiler"
      ],
      protocol: "NATO STANAG 4586 / SAE AS6091 (JAUS)",
    },
    {
      id: "industrial",
      icon: Tractor,
      number: "03",
      badge: t("plat_cat3_badge"),
      title: t("plat_cat3_title"),
      desc: t("plat_cat3_desc"),
      list: [
        "John Deere Otonom Traktörler",
        "New Holland & TÜMOSAN Tarım Şasileri",
        "CAT (Caterpillar) Maden Kamyonları",
        "Komatsu Otonom Hafriyat Dozerleri",
        "Şantiye İnsansız Malzeme Taşıyıcıları",
        "Liman & Depo Otonom AGV'leri"
      ],
      protocol: "ISOBUS 11783 / CAN FD / RTOS",
    },
  ];

  return (
    <section className="relative z-20 py-16 sm:py-24 px-4 sm:px-12 bg-[#07090c] border-t border-white/10">
      {/* Background Subtle Gradient */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_10%,rgba(200,255,0,0.04),rgba(0,0,0,0))]" />

      <div className="max-w-6xl mx-auto relative z-10 space-y-12 sm:space-y-16">
        
        {/* Header Section */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <div className="max-w-2xl space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-[11px] sm:text-xs font-mono font-bold tracking-widest uppercase">
              <Cpu className="w-3.5 h-3.5" />
              <span>{t("platforms_badge")}</span>
            </div>
            <h2 className="text-2xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight">
              {t("platforms_title")}
            </h2>
          </div>
          <p className="text-slate-400 text-xs sm:text-sm font-normal max-w-md leading-relaxed border-l-2 border-[#C8FF00] pl-3 sm:pl-4">
            {t("platforms_desc")}
          </p>
        </div>

        {/* 3 Main Vehicle Category Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {categories.map((cat) => {
            const IconComponent = cat.icon;
            return (
              <div
                key={cat.id}
                className="p-6 sm:p-7 rounded-2xl bg-[#0c0f16] border border-white/10 hover:border-[#C8FF00]/40 transition-all duration-300 flex flex-col justify-between group relative overflow-hidden shadow-xl"
              >
                <div className="space-y-4">
                  {/* Card Header */}
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold text-[#C8FF00]">{cat.number} //</span>
                      <span className="font-mono text-[10px] uppercase tracking-wider text-slate-300 font-bold bg-white/5 px-2 py-0.5 rounded border border-white/10">
                        {cat.badge}
                      </span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-white/5 text-[#C8FF00] group-hover:bg-[#C8FF00]/10 transition-colors">
                      <IconComponent className="w-5 h-5" />
                    </div>
                  </div>

                  {/* Title & Desc */}
                  <div>
                    <h3 className="text-lg font-bold text-white mb-2 group-hover:text-[#C8FF00] transition-colors leading-snug">
                      {cat.title}
                    </h3>
                    <p className="text-slate-400 text-xs leading-relaxed font-normal">
                      {cat.desc}
                    </p>
                  </div>

                  {/* Vehicle Tag Pills */}
                  <div className="space-y-1.5 pt-2">
                    <div className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
                      Uyumlu Platform Örnekleri:
                    </div>
                    <div className="flex flex-wrap gap-1.5">
                      {cat.list.map((item, idx) => (
                        <span
                          key={idx}
                          className="text-[10px] font-mono px-2 py-1 rounded bg-white/[0.04] border border-white/10 text-slate-300 flex items-center gap-1"
                        >
                          <CheckCircle2 className="w-2.5 h-2.5 text-[#C8FF00] shrink-0" />
                          <span>{item}</span>
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Bottom Protocol Pill */}
                <div className="pt-6 mt-6 border-t border-white/10 flex items-center justify-between">
                  <span className="text-[9px] font-mono text-slate-400 uppercase tracking-wider">
                    Protokol:
                  </span>
                  <span className="text-[10px] font-mono font-bold text-[#C8FF00] bg-[#C8FF00]/10 px-2.5 py-0.5 rounded border border-[#C8FF00]/30">
                    {cat.protocol}
                  </span>
                </div>
              </div>
            );
          })}
        </div>

        {/* Real Engineering Integration Methodologies Panel */}
        <div className="p-6 sm:p-8 rounded-2xl bg-[#0a0d13] border border-white/15 relative overflow-hidden">
          <div className="max-w-2xl mb-6">
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-slate-300 text-[10px] font-mono font-bold tracking-wider uppercase mb-2">
              <Sliders className="w-3 h-3 text-[#C8FF00]" />
              <span>{t("plat_how_subtitle")}</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {t("plat_how_title")}
            </h3>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Method 1: Drive-by-Wire */}
            <div className="p-5 rounded-xl bg-white/[0.02] border border-white/10 space-y-3">
              <div className="flex items-center justify-between">
                <span className="font-mono text-[10px] font-bold text-[#C8FF00] bg-[#C8FF00]/10 px-2 py-0.5 rounded border border-[#C8FF00]/30">
                  {t("plat_how_opt1_badge")}
                </span>
                <Zap className="w-4 h-4 text-[#C8FF00]" />
              </div>
              <h4 className="text-base font-bold text-white">
                {t("plat_how_opt1_title")}
              </h4>
              <p className="text-slate-400 text-xs leading-relaxed">
                {t("plat_how_opt1_desc")}
              </p>
              <div className="pt-2 flex items-center gap-2 text-[11px] font-mono text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00]" />
                <span>Entegrasyon Süresi: &lt; 15 Dakika (Tak-Çalıştır)</span>
              </div>
            </div>

            {/* Method 2: Mechanical Actuators */}
            <div className="p-5 rounded-xl bg-white/[0.02] border border-white/10 space-y-3">
              <div className="flex items-center justify-between">
                <span className="font-mono text-[10px] font-bold text-sky-400 bg-sky-400/10 px-2 py-0.5 rounded border border-sky-400/30">
                  {t("plat_how_opt2_badge")}
                </span>
                <Layers className="w-4 h-4 text-sky-400" />
              </div>
              <h4 className="text-base font-bold text-white">
                {t("plat_how_opt2_title")}
              </h4>
              <p className="text-slate-400 text-xs leading-relaxed">
                {t("plat_how_opt2_desc")}
              </p>
              <div className="pt-2 flex items-center gap-2 text-[11px] font-mono text-slate-300">
                <span className="w-1.5 h-1.5 rounded-full bg-sky-400" />
                <span>Uygulama: Direksiyon Servo Motoru + Lineer Fren Pistonu</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
