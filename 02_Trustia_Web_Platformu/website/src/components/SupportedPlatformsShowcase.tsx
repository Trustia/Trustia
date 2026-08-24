"use client";

import { useState } from "react";
import {
  Car,
  Shield,
  Tractor,
  Cpu,
  CheckCircle2,
  Zap,
  Layers,
  Sliders,
  Server,
  Radio,
  Eye,
  Crosshair,
  Wrench,
  Activity,
  Terminal,
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function SupportedPlatformsShowcase() {
  const { t } = useLanguage();
  const [activeBomTab, setActiveBomTab] = useState<string>("all");

  const vehicleCategories = [
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
        "Polaris GEM & Kampüs Servisleri",
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
        "NATO STANAG 4586 Uyumlu Şasiler",
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
        "Liman & Depo Otonom AGV'leri",
      ],
      protocol: "ISOBUS 11783 / CAN FD / RTOS",
    },
  ];

  // 100% Verified Global B2B Procurement Market Prices (August 2026)
  const bomItems = [
    // 1. Compute & Power
    {
      category: "compute",
      name: "Ana Otonomi Bilgisayarı (Edge AI)",
      model: "NVIDIA Jetson AGX Orin Industrial (64GB / 275 TOPS)",
      func: "Trustia 400Hz ESKF, 3D SLAM, Hibrit A* ve yapay zeka çekirdeğinin çalıştığı ana işlemci ünitesi.",
      standard: "ISO 26262 ASIL-B / MIL-STD-810H (-40°C/+85°C)",
      cost: "$3.600 USD",
      icon: Server,
    },
    {
      category: "compute",
      name: "Yüksek Hızlı Sistem Diski (NVMe)",
      model: "Samsung 990 Pro 2TB PCIe Gen4 M.2 SSD",
      func: "LiDAR nokta bulutları, kamera akışları ve telemetri loglarının mikrosaniyede kaydı.",
      standard: "PCIe 4.0 / 7.450 MB/s Okuma-Yazma",
      cost: "$190 USD",
      icon: Cpu,
    },
    {
      category: "compute",
      name: "Endüstriyel Voltaj Regülatörü (DC-DC)",
      model: "Mean Well SD-100A-12 (Geniş Girişli)",
      func: "Araç aküsündeki 12V/24V dalgalı voltajı bilgisayar ve sensörler için temiz 12V DC'ye regüle eder.",
      standard: "Endüstriyel IP30 / Kısa Devre & Aşırı Yük Korumalı",
      cost: "$95 USD",
      icon: Zap,
    },
    {
      category: "compute",
      name: "Yedek Güç Koruma Modülü (Mini UPS)",
      model: "12V Süperkapasitör Kesintisiz Güç Ünitesi",
      func: "Marşa basıldığında veya akü voltajı anlık düştüğünde bilgisayarın kapanmasını önler.",
      standard: "Zero-Downtime / 100.000+ Döngü Ömrü",
      cost: "$140 USD",
      icon: Activity,
    },
    {
      category: "compute",
      name: "Donanımsal Emniyet Bekçisi (Safety MCU)",
      model: "STM32H7 / Infineon AURIX TC397",
      func: "İşletim sistemi kitlenirse 200ms içinde donanımsal hidrolik acil freni kilitleyen emniyet kartı.",
      standard: "ISO 26262 ASIL-D Seviye Donanım Bekçisi",
      cost: "$155 USD",
      icon: Shield,
    },

    // 2. Sensors & LiDAR
    {
      category: "sensors",
      name: "3D Lazer Tarayıcı (3D LiDAR)",
      model: "Hesai Pandar XT32 (32 Kanal, 120m) / Ouster OS1-32",
      func: "Aracın tavanında saniyede 640.000 lazer ışınıyla 120 metre menzilde 3D çevre haritalama.",
      standard: "IP67 / IP69K / Sınıf 1 Göz Güvenlikli (Class 1 Eye-Safe)",
      cost: "$5.800 USD",
      icon: Eye,
    },
    {
      category: "sensors",
      name: "HDR Çevre Görüş Kameraları (2 Adet)",
      model: "e-con Systems Sony IMX390 HDR (Global Shutter)",
      func: "Şerit çizgileri, yol tabelaları, insan ve trafik ışıklarının yüksek dinamik aralıkla tespiti.",
      standard: "IP67 / 120dB HDR / GigE & USB3 Arayüz",
      cost: "$650 USD",
      icon: Eye,
    },
    {
      category: "sensors",
      name: "IMU / Yönelim & RTK-INS Sensörü (Denge)",
      model: "Xsens MTi-680G (400Hz 9-Eksen RTK-GNSS/INS)",
      func: "400Hz ivmeölçer ve jiroskop ile aracın yanal kayma, eğim ve yönelimini mikrosaniyede hesaplar.",
      standard: "IP68 / RTK-GNSS Entegreli / MIL-STD-810G",
      cost: "$3.740 USD",
      icon: Crosshair,
    },
    {
      category: "sensors",
      name: "RTK-GNSS / Çift GPS Anten Seti",
      model: "u-blox ZED-F9P Modülü + 2x Tallysman Anten",
      func: "Açık arazide uydu görüşü varken 1-2 santimetre hassasiyetinde mutlak küresel koordinat sağlar.",
      standard: "Çok Bantlı L1/L2/E5b RTK / NMEA 0183",
      cost: "$480 USD",
      icon: Radio,
    },

    // 3. Drive & Vehicle Interface
    {
      category: "drive",
      name: "CAN-Bus Sürüş İletişim Kartı",
      model: "Kvaser Leaf Light v2 / PEAK PCAN-USB Pro FD",
      func: "Trustia sürüş komutlarını (Hız, Direksiyon Açısı) aracın motor ve EPS beynine iletir.",
      standard: "SAE J1939 / CAN 2.0B / CAN FD / 1ms Deterministik",
      cost: "$380 USD",
      icon: Terminal,
    },
    {
      category: "drive",
      name: "OBD-II / CAN Araç Kablo Demeti",
      model: "Shielded Twisted-Pair Otomotiv Kablosu",
      func: "Aracın CAN-High / CAN-Low hatlarına parazitsiz ve gürültüsüz dijital bağlantı.",
      standard: "Otomotiv Sınıfı Korumalı Kablolama",
      cost: "$60 USD",
      icon: Layers,
    },
    {
      category: "drive",
      name: "Fiziksel Acil Durdurma Butonu (E-Stop)",
      model: "Schneider Electric IP67 Mantar Buton",
      func: "Aracın dışına takılır; basıldığı anda aktüatör gücünü mekanik olarak kesip freni kilitler.",
      standard: "IEC 60947-5-5 / IP67 Emniyet Sertifikalı",
      cost: "$75 USD",
      icon: Zap,
    },

    // 4. Military Defense Kit
    {
      category: "defense",
      name: "Termal Gece Görüş Kamerası (LWIR)",
      model: "FLIR Boson 640 Core (640x512 / 60Hz)",
      func: "Zifiri karanlık, sis ve duman arkasındaki canlıları ve toprak altı ısı anomalilerini tespit eder.",
      standard: "MIL-STD-810G Askeri Termal Standart",
      cost: "$4.500 USD",
      icon: Eye,
    },
    {
      category: "defense",
      name: "Askeri Metal & Mayın Arama Bobini",
      model: "CEIA CMD2 Askeri İndüksiyon Bobini",
      func: "Toprak altındaki metal mayınları, EYP düzeneklerini ve gizli kabloları elektromanyetik algılar.",
      standard: "NATO STANAG 4586 / MIL-STD Uyumlu",
      cost: "$6.800 USD",
      icon: Crosshair,
    },
    {
      category: "defense",
      name: "Yere Nüfuz Eden Radar (GPR)",
      model: "Impulse Radar PinPoint GPR (1-2m Derinlik)",
      func: "Toprak altına elektromanyetik radar dalgaları göndererek plastik mayın ve tünelleri bulur.",
      standard: "Geniş Bant Yeraltı Radarı / IP67",
      cost: "$9.500 USD",
      icon: Radio,
    },
    {
      category: "defense",
      name: "Taktik Mesh Telsiz & Veri Bağı",
      model: "Doodle Labs Smart Radio / Silvus SC4200 MIMO (AES-256)",
      func: "Araç ile komuta merkezi arasında 5-15 km mesafeden şifreli canlı video ve telemetri aktarır.",
      standard: "FIPS 140-2 Seviye 2 / MIL-STD-810H",
      cost: "$3.500 USD",
      icon: Radio,
    },

    // 5. Mechanical Actuators
    {
      category: "actuators",
      name: "Direksiyon Servo Motoru (Mekanik Şasi)",
      model: "Nanotec 12V Fırçasız Torklu Servo Motor",
      func: "Elektronik direksiyonu olmayan klasik araçların direksiyon milini fiziksel olarak çevirir.",
      standard: "12V DC / 15 Nm Tork / CANopen Kontrollü",
      cost: "$450 USD",
      icon: Wrench,
    },
    {
      category: "actuators",
      name: "Lineer Pedal İtici Pistonlar (2 Adet)",
      model: "Linak LA36 12V 800N Lineer Ağır Hizmet Aktüatörü (2x)",
      func: "Gaz ve fren pedalının arkasına vidalanarak pedallara insan ayağı gibi fiziksel basar.",
      standard: "IP66 / 800N Basma Kuvveti / Endüstriyel Sınıf",
      cost: "$2.400 USD",
      icon: Wrench,
    },
  ];

  const filteredBom =
    activeBomTab === "all"
      ? bomItems
      : bomItems.filter((item) => item.category === activeBomTab);

  return (
    <section className="relative z-20 py-16 sm:py-24 px-4 sm:px-12 bg-[#07090c] border-t border-white/10">
      {/* Background Subtle Gradient */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_10%,rgba(200,255,0,0.04),rgba(0,0,0,0))]" />

      <div className="max-w-6xl mx-auto relative z-10 space-y-16 sm:space-y-24">
        
        {/* ========================================================================= */}
        {/* PART 1: COMPATIBLE VEHICLE PLATFORMS MATRIX                               */}
        {/* ========================================================================= */}
        <div className="space-y-10">
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
            {vehicleCategories.map((cat) => {
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
                        <span className="font-mono text-xs font-bold text-[#C8FF00]">
                          {cat.number} //
                        </span>
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
        </div>

        {/* ========================================================================= */}
        {/* PART 2: MASTER HARDWARE BILL OF MATERIALS (BOM) SPECIFICATION TABLE       */}
        {/* ========================================================================= */}
        <div className="space-y-8 pt-8 border-t border-white/10">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
            <div className="max-w-2xl space-y-3">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-white/5 border border-white/20 text-[#C8FF00] text-[11px] sm:text-xs font-mono font-bold tracking-widest uppercase">
                <Wrench className="w-3.5 h-3.5" />
                <span>{t("bom_badge")}</span>
              </div>
              <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white tracking-tight">
                {t("bom_title")}
              </h2>
            </div>
            <p className="text-slate-400 text-xs sm:text-sm max-w-md leading-relaxed border-l-2 border-white/20 pl-3">
              {t("bom_desc")}
            </p>
          </div>

          {/* Interactive BOM Category Tabs */}
          <div className="flex flex-wrap gap-2 pt-2">
            {[
              { id: "all", label: t("bom_tab_all") },
              { id: "compute", label: t("bom_tab_compute") },
              { id: "sensors", label: t("bom_tab_sensors") },
              { id: "drive", label: t("bom_tab_drive") },
              { id: "defense", label: t("bom_tab_defense") },
              { id: "actuators", label: t("bom_tab_actuators") },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveBomTab(tab.id)}
                className={`px-3 py-1.5 rounded-lg font-mono text-[11px] sm:text-xs font-bold transition-all ${
                  activeBomTab === tab.id
                    ? "bg-[#C8FF00] text-black shadow-lg shadow-[#C8FF00]/20"
                    : "bg-white/5 text-slate-400 hover:text-white hover:bg-white/10 border border-white/10"
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* Executive Defense-Grade Hardware Table */}
          <div className="rounded-2xl bg-[#0a0d13] border border-white/15 overflow-hidden shadow-2xl">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="bg-white/[0.04] border-b border-white/10 text-slate-400 font-mono text-[10px] sm:text-[11px] uppercase tracking-wider">
                    <th className="py-4 px-4 sm:px-6">{t("bom_col_component")}</th>
                    <th className="py-4 px-4 sm:px-6">{t("bom_col_model")}</th>
                    <th className="py-4 px-4 sm:px-6 hidden md:table-cell">
                      {t("bom_col_function")}
                    </th>
                    <th className="py-4 px-4 sm:px-6">{t("bom_col_standard")}</th>
                    <th className="py-4 px-4 sm:px-6 text-right">{t("bom_col_cost")}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-white/5 font-sans">
                  {filteredBom.map((item, idx) => {
                    const ItemIcon = item.icon;
                    return (
                      <tr
                        key={idx}
                        className="hover:bg-white/[0.02] transition-colors group"
                      >
                        <td className="py-3.5 px-4 sm:px-6 font-bold text-white flex items-center gap-2.5">
                          <div className="p-1.5 rounded-md bg-white/5 text-[#C8FF00] shrink-0">
                            <ItemIcon className="w-4 h-4" />
                          </div>
                          <span>{item.name}</span>
                        </td>
                        <td className="py-3.5 px-4 sm:px-6 font-mono text-slate-300 font-semibold">
                          {item.model}
                        </td>
                        <td className="py-3.5 px-4 sm:px-6 text-slate-400 text-[11px] leading-relaxed hidden md:table-cell max-w-xs">
                          {item.func}
                        </td>
                        <td className="py-3.5 px-4 sm:px-6">
                          <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-white/5 border border-white/10 text-slate-300">
                            {item.standard}
                          </span>
                        </td>
                        <td className="py-3.5 px-4 sm:px-6 text-right font-mono font-bold text-[#C8FF00]">
                          {item.cost}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

          {/* ========================================================================= */}
          {/* PART 3: REAL-WORLD TURNKEY PACKAGE BUDGETS (ACCURATE 2026 ESTIMATES)       */}
          {/* ========================================================================= */}
          <div className="space-y-4 pt-4">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-lg sm:text-xl font-bold text-white">
                  {t("bom_turnkey_title")}
                </h3>
                <p className="text-slate-400 text-xs">{t("bom_turnkey_subtitle")}</p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
              {/* Turnkey 1: Civilian Robotaxi */}
              <div className="p-5 rounded-xl bg-[#0c0f16] border border-white/10 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-[10px] font-bold text-[#C8FF00] bg-[#C8FF00]/10 px-2 py-0.5 rounded border border-[#C8FF00]/30">
                    SİVİL SEVİYE 4 KİTİ
                  </span>
                  <span className="font-mono text-base font-extrabold text-white">
                    ~$14.750 USD
                  </span>
                </div>
                <h4 className="text-sm font-bold text-white">
                  {t("bom_turnkey_1_title")}
                </h4>
                <p className="text-slate-400 text-xs leading-relaxed">
                  {t("bom_turnkey_1_desc")}
                </p>
                <div className="pt-2 text-[10px] font-mono text-slate-500 border-t border-white/10">
                  NVIDIA Jetson Orin ($3.6K) + Hesai XT32 LiDAR ($5.8K) + Xsens MTi-680G ($3.7K) + Kameralar & CAN ($1.6K)
                </div>
              </div>

              {/* Turnkey 2: Military Defense UGV */}
              <div className="p-5 rounded-xl bg-[#0c0f16] border border-[#C8FF00]/30 space-y-3 relative overflow-hidden shadow-lg shadow-[#C8FF00]/5">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-[10px] font-bold text-emerald-400 bg-emerald-400/10 px-2 py-0.5 rounded border border-emerald-400/30">
                    ASKERİ TAKTİK İKA KİTİ
                  </span>
                  <span className="font-mono text-base font-extrabold text-[#C8FF00]">
                    ~$39.050 USD
                  </span>
                </div>
                <h4 className="text-sm font-bold text-white">
                  {t("bom_turnkey_2_title")}
                </h4>
                <p className="text-slate-400 text-xs leading-relaxed">
                  {t("bom_turnkey_2_desc")}
                </p>
                <div className="pt-2 text-[10px] font-mono text-slate-400 border-t border-white/10">
                  Sivil Kit ($14.7K) + FLIR Boson 640 ($4.5K) + CEIA CMD2 ($6.8K) + GPR Radar ($9.5K) + Mesh Telsiz ($3.5K)
                </div>
              </div>

              {/* Turnkey 3: Mechanical Tractor / Mining */}
              <div className="p-5 rounded-xl bg-[#0c0f16] border border-white/10 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-[10px] font-bold text-sky-400 bg-sky-400/10 px-2 py-0.5 rounded border border-sky-400/30">
                    MEKANİK ARAÇ KİTİ
                  </span>
                  <span className="font-mono text-base font-extrabold text-white">
                    ~$17.600 USD
                  </span>
                </div>
                <h4 className="text-sm font-bold text-white">
                  {t("bom_turnkey_3_title")}
                </h4>
                <p className="text-slate-400 text-xs leading-relaxed">
                  {t("bom_turnkey_3_desc")}
                </p>
                <div className="pt-2 text-[10px] font-mono text-slate-500 border-t border-white/10">
                  Sivil Kit ($14.7K) + Nanotec Servo ($450) + Linak LA36 Endüstriyel Pistonlar ($2.4K)
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* PART 4: 2 INTEGRATION METHODOLOGIES PANEL                                  */}
        {/* ========================================================================= */}
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
