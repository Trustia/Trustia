"use client";

import Link from "next/link";
import { CheckCircle2, MapPin, Globe, Shield, Cpu } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function Footer() {
  const { lang, t } = useLanguage();

  return (
    <footer id="kurumsal" className="w-full bg-[#05070a] border-t border-[#161b22] text-slate-400 font-sans text-xs pt-20 pb-12 px-6 sm:px-12 relative z-20 selection:bg-[#C8FF00] selection:text-black">
      
      {/* Background Subtle Low-Opacity Grid Pattern */}
      <div className="absolute inset-0 bg-tactical-grid opacity-15 pointer-events-none" />

      <div className="max-w-7xl mx-auto relative z-10">
        
        {/* 4 Columns Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-16 mb-16">
          
          {/* Column 1: Şirket / Company */}
          <div className="space-y-5">
            <Link href="/" className="inline-flex items-center gap-2.5 group select-none">
              <div className="w-8 h-8 rounded-lg overflow-hidden border border-[#C8FF00]/40 shadow-[0_0_12px_rgba(200,255,0,0.4)] group-hover:scale-105 transition-transform">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/logo.png" alt="Trustia AI Logo" className="w-full h-full object-cover" />
              </div>
              <div className="flex items-center gap-1">
                <span className="font-orbitron font-extrabold text-2xl text-white tracking-wider">Trustia</span>
                <span className="font-orbitron font-extrabold text-2xl text-[#C8FF00] tracking-wider drop-shadow-[0_0_12px_rgba(200,255,0,0.4)]">AI</span>
              </div>
            </Link>

            <p className="text-slate-400 text-xs leading-relaxed font-light">
              {t("footer_tagline")}
            </p>

            <div className="pt-2 space-y-2.5 font-mono text-[11px] text-slate-300">
              <div className="flex items-center gap-2 text-[#C8FF00] font-medium">
                <Globe className="w-3.5 h-3.5 shrink-0" />
                <span>{t("footer_made_in")}</span>
              </div>
              <div className="flex items-center gap-2 text-slate-400">
                <MapPin className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>{t("footer_locations")}</span>
              </div>
              <div className="flex items-center gap-2 text-slate-400">
                <Shield className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>STANAG 4586 Level 4</span>
              </div>
              <div className="flex items-center gap-2 text-slate-400">
                <Cpu className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>SAE J3016 Level 4</span>
              </div>
            </div>
          </div>

          {/* Column 2: Platform */}
          <div className="space-y-5">
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">{t("footer_col_platform")}</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li>
                <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  {t("footer_link_arch")}
                </Link>
              </li>
              <li>
                <Link href="/politika/etik/" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  {t("footer_link_engine")}
                </Link>
              </li>
              <li>
                <Link href="/politika/siber/" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  {t("footer_link_perception")}
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  {t("footer_link_ros")}
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  {t("footer_link_api")}
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Sertifikasyon / Certification */}
          <div className="space-y-5">
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">{t("footer_col_cert")}</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/yerlilik/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_cert_indigenous")}
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/siber/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_cert_crypto")}
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/ihracat/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_cert_as9100")}
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/siber/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_cert_iso")}
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_cert_ros")}
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 4: Kurumsal / Corporate */}
          <div className="space-y-5">
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">{t("footer_col_corporate")}</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li>
                <Link href="/hakkimizda/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_link_about")}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-[#C8FF00] transition-colors flex items-center gap-2">
                  <span>{t("footer_link_career")}</span>
                  <span className="text-[9px] font-mono px-1.5 py-0.5 bg-[#C8FF00]/15 text-[#C8FF00] border border-[#C8FF00]/30 rounded font-bold">{t("footer_badge_join")}</span>
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-[#C8FF00] transition-colors">
                  {t("footer_link_contact")}
                </Link>
              </li>
              <li>
                <Link href="/politika/mulkiyet/" className="hover:text-[#C8FF00] transition-colors">
                  {lang === "tr" ? "Fikri Mülkiyet & Basın" : "IP & Press Kit"}
                </Link>
              </li>
            </ul>
          </div>

        </div>

        {/* Bottom Bar: Clean Silicon Valley / Defense Standard Corporate Bar */}
        <div className="pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-400">
          <div className="text-center md:text-left text-slate-400">
            © {new Date().getFullYear()} <span className="text-white font-bold tracking-wide">Trustia AI</span> {t("footer_rights")}
          </div>

          <div className="flex flex-wrap items-center justify-center gap-4 sm:gap-6 text-[11px]">
            <Link href="/politika/kvkk/" className="text-slate-400 hover:text-[#C8FF00] transition-colors">
              {lang === "tr" ? "Gizlilik Politikası (KVKK/GDPR)" : "Privacy Policy (GDPR)"}
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/ihracat/" className="text-slate-400 hover:text-[#C8FF00] transition-colors">
              {lang === "tr" ? "İhracat Kontrol (5201/MSB)" : "Export Control"}
            </Link>
            <span className="text-white/20 hidden sm:inline">•</span>
            <Link href="/politika/mulkiyet/" className="text-slate-400 hover:text-[#C8FF00] transition-colors">
              {lang === "tr" ? "Fikri Mülkiyet & Lisans" : "IP & Licensing"}
            </Link>
          </div>
        </div>

      </div>
    </footer>
  );
}
