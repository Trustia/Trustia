"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import CorporateContactForm from "@/components/CorporateContactForm";
import Link from "next/link";
import { ArrowLeft, Mail, MapPin, Clock, ShieldCheck, Phone, CheckCircle2 } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function ContactPage() {
  const { lang, t } = useLanguage();

  const channels = [
    { title: "Genel İletişim & Santral", email: "iletisim@trustia.com.tr", desc: "Tüm resmi yazışmalar ve konsorsiyum talepleri" },
    { title: "Teknik Entegrasyon & SDK", email: "entegrasyon@trustia.com.tr", desc: "CAN-FD, ROS 2, JAUS ve donanım sürücüleri" },
    { title: "Kariyer & Mühendislik", email: "kariyer@trustia.com.tr", desc: "Otonomi, kontrol ve gömülü yazılım pozisyonları" },
    { title: "Hukuk & Lisanslama", email: "hukuk@trustia.com.tr", desc: "Fikri mülkiyet, OEM lisanslama ve ihracat izinleri" },
  ];

  return (
    <main className="min-h-screen bg-[#07090d] text-white font-sans selection:bg-slate-700 selection:text-white pt-20 sm:pt-24 pb-16">
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-8 sm:space-y-10">

        {/* 1. Header */}
        <div className="space-y-3 pb-6 border-b border-white/10">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Link href="/" className="hover:text-white flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{t("contact_back")}</span>
            </Link>
            <span>/</span>
            <span className="text-slate-200 font-semibold">{lang === "tr" ? "İLETİŞİM" : "CONTACT"}</span>
          </div>

          <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px] font-mono font-medium tracking-wider uppercase">
            <span>{t("contact_page_badge")}</span>
          </div>

          <h1 className="text-2xl sm:text-4xl font-bold text-white tracking-tight leading-snug">
            {t("contact_page_title")}
          </h1>

          <p className="text-slate-400 text-xs sm:text-sm max-w-2xl leading-relaxed">
            {t("contact_page_desc")}
          </p>
        </div>

        {/* 2. Main 2-Column Grid (Desktop 2-Col, Mobile Compact Grid) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left Column (5 Cols) - Corporate Directory & Headquarters */}
          <div className="lg:col-span-5 space-y-4">
            
            {/* Department Emails Card */}
            <div className="p-5 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-3">
              <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                {t("contact_dept_title")}
              </div>

              {/* 2-Column on Mobile, 1-Column on Desktop */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-2.5">
                {channels.map((ch, idx) => (
                  <a
                    key={idx}
                    href={`mailto:${ch.email}`}
                    className="p-3 rounded-xl bg-[#07090d] border border-slate-800 hover:border-slate-600 transition-colors block group"
                  >
                    <div className="text-xs font-semibold text-white group-hover:text-slate-200">
                      {ch.title}
                    </div>
                    <div className="text-xs font-mono text-slate-300 mt-0.5">
                      {ch.email}
                    </div>
                    <div className="text-[10px] text-slate-500 mt-1">
                      {ch.desc}
                    </div>
                  </a>
                ))}
              </div>
            </div>

            {/* Physical Location Card */}
            <div className="p-5 rounded-2xl bg-[#0f131a] border border-slate-800 space-y-3">
              <div className="text-[11px] font-mono text-slate-400 uppercase tracking-wider font-semibold">
                {t("contact_loc_title")}
              </div>

              <div className="space-y-2.5 text-xs text-slate-300">
                <div className="flex items-start gap-2.5">
                  <MapPin className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                  <div>
                    <div className="font-semibold text-white">İTO BTM Kampüsü</div>
                    <div className="text-slate-400 text-[11px]">Fulya Mah. Yeşilçimen Sok. Polat Tower Rezidans, Şişli / İstanbul</div>
                  </div>
                </div>

                <div className="flex items-start gap-2.5">
                  <Clock className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
                  <div>
                    <div className="font-semibold text-white">{t("contact_hours_title")}</div>
                    <div className="text-slate-400 text-[11px]">{t("contact_hours_desc")}</div>
                  </div>
                </div>
              </div>
            </div>

          </div>

          {/* Right Column (7 Cols) - Contact Form */}
          <div className="lg:col-span-7">
            <CorporateContactForm />
          </div>

        </div>

      </div>

      <Footer />
    </main>
  );
}
