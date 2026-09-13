"use client";

import Image from "next/image";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { lang } = useLanguage();

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-8 bg-[#06080b] border-t border-b border-white/10">
      <div className="max-w-5xl mx-auto space-y-6">
        
        {/* Subtle, Minimalist Header */}
        <div className="text-center">
          <span className="text-[11px] sm:text-xs font-mono font-bold tracking-[0.25em] text-slate-400 uppercase">
            {lang === "tr" ? "DESTEKLEYEN KURUMLAR & EKOSİSTEM" : "SUPPORTING INSTITUTIONS & ECOSYSTEM"}
          </span>
        </div>

        {/* 3D Official Institutional Showcase */}
        <div className="relative w-full rounded-2xl overflow-hidden border border-white/10 shadow-[0_20px_50px_rgba(0,0,0,0.8)] bg-[#07090c] group">
          <Image
            src="/accreditations-showcase.jpg"
            alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
            width={1280}
            height={720}
            className="w-full h-auto object-cover object-center group-hover:scale-[1.01] transition-transform duration-700 filter contrast-105 brightness-100"
            priority
          />
        </div>

        {/* High-End Enterprise Accreditation Badges Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2.5 pt-2">
          {[
            {
              flag: "🇪🇺",
              name: "Avrupa Komisyonu",
              code: "PIC: 861711529",
              desc: "ec.europa.eu Tescilli Katılımcı",
              status: "Onaylandı"
            },
            {
              flag: "🇪🇺",
              name: "EIT Urban Mobility",
              code: "Partner: CUS15554",
              desc: "100k€ Hibe Başvuru #3.1.02-1206-3732.3",
              status: "Canlıda"
            },
            {
              flag: "🇶🇦",
              name: "Katar QSTP (Doha)",
              code: "30M$ Fon + Sprint",
              desc: "Qatar Foundation 4 Hafta Doha Rezidansı",
              status: "Alındı"
            },
            {
              flag: "🇹🇷",
              name: "BAYKAR Teknoloji",
              code: "Tedarikçi Portalı",
              desc: "Seviye-4 GNSS-denied 3D SLAM & İKA",
              status: "Kayıt Alındı"
            },
            {
              flag: "🇹🇷",
              name: "ASELSAN Portalı",
              code: "#0050569CCE941FD1",
              desc: "Yazılım & Kara Platform Entegrasyonu",
              status: "Değerlendirmede"
            },
            {
              flag: "🇹🇷",
              name: "SSB SAYZEK",
              code: "Başvuru #170",
              desc: "Simport Otonomi Simülasyon Yöneticisi",
              status: "Onay Bekliyor"
            },
            {
              flag: "🇺🇸",
              name: "Z Fellows (San Francisco)",
              code: "$10k Hibe Mülakatı",
              desc: "Grace Kasten (Pace Capital) Canlı Zoom",
              status: "17 Eylül"
            },
            {
              flag: "🇹🇷",
              name: "DEİK İş Konseyi",
              code: "Dijital Teknolojiler",
              desc: "Ticari Diplomasi & Global Otonomi İhracatı",
              status: "Onaylandı"
            },
            {
              flag: "🇦🇪",
              name: "Dubai RTA World Challenge",
              code: "$1.200.000 Ödül",
              desc: "Global Seviye-4 Robotaksi Yarışması",
              status: "İncelemede"
            },
            {
              flag: "🇸🇦",
              name: "NEOM Otonom Mobilite",
              code: "$500B Mega Şehir",
              desc: "Seviye-4 Sürücüsüz Filo PoC Teklifi",
              status: "Alındı"
            },
            {
              flag: "🇹🇷",
              name: "İTO BTM Fulya Kampüsü",
              code: "2026-II Sözleşmeli",
              desc: "İstanbul Ticaret Odası Ön Kuluçka",
              status: "Yerleşik"
            },
            {
              flag: "🇹🇷",
              name: "SPK fonbulucu",
              code: "Kampanya: W1MV5K",
              desc: "15.000.000 TL Hedef (150M TL Val.)",
              status: "Ön İncelemede"
            }
          ].map((item, idx) => (
            <div
              key={idx}
              className="p-3 rounded-xl bg-[#0a0d13] border border-white/10 hover:border-[#C8FF00]/40 transition-colors flex flex-col justify-between space-y-1 group"
            >
              <div className="flex items-center justify-between gap-1.5">
                <div className="flex items-center gap-1.5 min-w-0">
                  <span className="text-xs shrink-0">{item.flag}</span>
                  <span className="text-[11px] font-bold text-white truncate group-hover:text-[#C8FF00] transition-colors">
                    {item.name}
                  </span>
                </div>
                <span className="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white/5 text-[#C8FF00] border border-white/10 shrink-0">
                  {item.status}
                </span>
              </div>
              <div className="font-mono text-[10px] font-semibold text-slate-300">
                {item.code}
              </div>
              <div className="text-[9.5px] text-slate-400 line-clamp-1">
                {item.desc}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
