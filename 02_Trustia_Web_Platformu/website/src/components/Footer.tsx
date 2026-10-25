"use client";

import Link from "next/link";
import { ShieldCheck, Cpu, Code2, Scale } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function Footer() {
  const { lang, t } = useLanguage();

  return (
    <footer id="kurumsal" className="w-full bg-[#07090d] border-t border-white/10 text-slate-400 font-sans text-xs pt-16 pb-12 px-6 sm:px-12 relative z-20 selection:bg-slate-700 selection:text-white">
      <div className="max-w-7xl mx-auto space-y-12">
        
        {/* 4 Columns Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-12">
          
          {/* Column 1: Şirket & Mühendislik Temeli */}
          <div className="space-y-4">
            <Link href="/" className="inline-flex items-center gap-2 group select-none">
              <div className="w-7 h-7 rounded overflow-hidden border border-white/15 bg-white/5 flex items-center justify-center group-hover:border-white/30 transition-colors">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/logo.png" alt="Trustia AI Logo" className="w-full h-full object-cover" />
              </div>
              <div className="flex items-center gap-1.5">
                <span className="font-bold text-base text-white tracking-tight">Trustia</span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white/5 border border-white/10 text-slate-300 font-semibold">AI</span>
              </div>
            </Link>

            <p className="text-slate-400 text-xs leading-relaxed font-normal">
              {t("footer_tagline")}
            </p>

            <div className="pt-2 space-y-1.5 font-mono text-[11px] text-slate-400 divide-y divide-white/5">
              <div className="pt-1.5 first:pt-0 flex items-center gap-2 text-slate-300">
                <Code2 className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                <span>16.000+ Satır C++20 / ROS 2</span>
              </div>
              <div className="pt-1.5 flex items-center gap-2">
                <Cpu className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>1.301 / 1.301 Doğrulanmış Test</span>
              </div>
              <div className="pt-1.5 flex items-center gap-2">
                <ShieldCheck className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>SAE J3016 Seviye 4 • ISO 26262 ASIL-D</span>
              </div>
              <div className="pt-1.5 flex items-center gap-2">
                <Scale className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>OIN 2.0 Patent Lisansı: #f1e44576</span>
              </div>
            </div>
          </div>

          {/* Column 2: Çözümler / Solutions */}
          <div className="space-y-4">
            <h5 className="font-mono text-[11px] font-bold text-white tracking-widest uppercase">
              // {t("footer_col_platform")}
            </h5>
            <ul className="space-y-2.5 font-normal text-slate-300">
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "Referans Otonomi Mimarisi (RAD)" : "Reference Autonomy Architecture (RAD)"}
                </Link>
              </li>
              <li>
                <Link href="/politika/siber/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "3D NDT SLAM & Haritalama" : "3D NDT SLAM & Mapping"}
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "Çoklu Sensör Füzyonu (LiDAR & Radar)" : "Multi-Sensor Fusion Core"}
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "100 Hz CAN-FD Sürüş Köprüsü" : "100 Hz CAN-FD Drive Bridge"}
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "ASIL-D Güvenlik & Devralma Protokolü" : "ASIL-D Fail-Safe & Override"}
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Standartlar ve Uyumluluk */}
          <div className="space-y-4">
            <h5 className="font-mono text-[11px] font-bold text-white tracking-widest uppercase">
              // {t("footer_col_cert")}
            </h5>
            <ul className="space-y-2.5 font-normal text-slate-300">
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors duration-150 flex items-center justify-between group">
                  <span>ISO 26262 ASIL-D</span>
                  <span className="text-[10px] font-mono text-slate-300">Fonksiyonel Emniyet</span>
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors duration-150 flex items-center justify-between group">
                  <span>UN ECE R157</span>
                  <span className="text-[10px] font-mono text-slate-300">Otonom Regülasyon</span>
                </Link>
              </li>
              <li>
                <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors duration-150 flex items-center justify-between group">
                  <span>OIN 2.0 Patent Paktı</span>
                  <span className="text-[10px] font-mono text-slate-300">#f1e44576</span>
                </Link>
              </li>
              <li>
                <Link href="/politika/yerlilik/" className="hover:text-white transition-colors duration-150 flex items-center justify-between group">
                  <span>ASELSAN & STM Tedarikçi Ağı</span>
                  <span className="text-[10px] font-mono text-slate-300">#0050569</span>
                </Link>
              </li>
              <li>
                <Link href="/politika/ihracat/" className="hover:text-white transition-colors duration-150 flex items-center justify-between group">
                  <span>Çift Kullanım (Dual-Use)</span>
                  <span className="text-[10px] font-mono text-slate-300">İhracat Uyumu</span>
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 4: Kurumsal / Corporate */}
          <div className="space-y-4">
            <h5 className="font-mono text-[11px] font-bold text-white tracking-widest uppercase">
              // {t("footer_col_corporate")}
            </h5>
            <ul className="space-y-2.5 font-normal text-slate-300">
              <li>
                <Link href="/hakkimizda/" className="hover:text-white transition-colors duration-150 inline-block">
                  {t("footer_link_about")}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors duration-150 inline-block">
                  {t("footer_link_career")}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors duration-150 inline-block">
                  {t("footer_link_contact")}
                </Link>
              </li>
              <li>
                <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "OIN 2.0 Patent Lisansı" : "OIN 2.0 Patent License"}
                </Link>
              </li>
              <li>
                <Link href="/politika/mulkiyet/" className="hover:text-white transition-colors duration-150 inline-block">
                  {lang === "tr" ? "Fikri Mülkiyet & Lisanslar" : "IP & Licensing"}
                </Link>
              </li>
            </ul>
          </div>

        </div>

        {/* Bottom Bar: Muted Monochrome Defense Layout */}
        <div className="pt-6 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-400">
          <div className="text-center md:text-left text-slate-400">
            © {new Date().getFullYear()} <span className="text-white font-medium">Trustia AI</span>. {t("footer_rights")}
          </div>

          <div className="flex flex-wrap items-center justify-center gap-3 sm:gap-4 text-[11px] text-slate-400">
            <Link href="/politika/kvkk/" className="hover:text-white transition-colors">
              {lang === "tr" ? "Gizlilik (KVKK/GDPR)" : "Privacy Policy"}
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/ihracat/" className="hover:text-white transition-colors">
              {lang === "tr" ? "İhracat Kontrol" : "Export Control"}
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/mulkiyet/" className="hover:text-white transition-colors">
              {lang === "tr" ? "Fikri Mülkiyet" : "Intellectual Property"}
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors">
              OIN 2.0
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/lisans/" className="hover:text-white transition-colors">
              SLA & EULA
            </Link>
          </div>
        </div>

      </div>
    </footer>
  );
}
