"use client";

import Link from "next/link";
import { ShieldCheck, CheckCircle2, ArrowUpRight, Cpu, Globe, Lock, Code2 } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function Footer() {
  const { lang, t } = useLanguage();

  return (
    <footer id="kurumsal" className="relative w-full bg-[#05070a] border-t border-white/10 text-slate-400 font-sans text-xs pt-16 pb-12 px-6 sm:px-12 z-20 overflow-hidden">
      {/* Subtle Ambient Background Glow */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-white/[0.015] rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-[#C8FF00]/[0.015] rounded-full blur-3xl pointer-events-none" />

      <div className="max-w-7xl mx-auto space-y-12 relative z-10">
        
        {/* Main 4-Column Responsive Layout */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 pb-12 border-b border-white/10">
          
          {/* Column 1: Brand & Verified Accreditation (Width: 4 cols) */}
          <div className="lg:col-span-4 space-y-5">
            {/* Logo */}
            <Link href="/" className="inline-flex items-center gap-2.5 group select-none">
              <div className="w-8 h-8 rounded-lg overflow-hidden shrink-0">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/logo.png" alt="Trustia AI Logo" className="w-full h-full object-cover" />
              </div>
              <div className="flex items-center gap-1.5">
                <span className="font-bold text-xl text-white tracking-tight">Trustia</span>
                <span className="font-bold text-xl text-[#C8FF00] tracking-tight">AI</span>
              </div>
            </Link>

            {/* Tagline */}
            <p className="text-slate-300 text-xs sm:text-[13px] leading-relaxed font-normal max-w-sm">
              {lang === "tr"
                ? "Ticari elektrikli araç filoları ve çift amaçlı otonom sistemler için deterministik Seviye-4 otonom sürüş yazılım çekirdeği."
                : "Deterministic Level-4 reference autonomy architecture engineered for commercial electric fleets and sovereign autonomous systems."}
            </p>

            {/* Verified Accreditation Tags - Clean Typographic Readout (No Box/Border) */}
            <div className="pt-2 space-y-2.5">
              <div className="text-[10px] font-mono tracking-widest text-slate-500 uppercase font-semibold">
                {lang === "tr" ? "DOĞRULANMIŞ KURUMSAL KÜTÜK" : "VERIFIED REGISTRY"}
              </div>
              <div className="space-y-2 text-xs font-mono">
                <div className="flex items-center gap-2.5 text-slate-300">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>ASELSAN & STM</span>
                  <span className="text-slate-500 text-[11px]">#{'0050569'}</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-300">
                  <ShieldCheck className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>OIN Patent Paktı</span>
                  <span className="text-slate-500 text-[11px]">#{'f1e44576'}</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-300">
                  <Globe className="w-3.5 h-3.5 text-sky-400 shrink-0" />
                  <span>AB Katılımcı Kimliği</span>
                  <span className="text-slate-500 text-[11px]">PIC: 861711529</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-300">
                  <Cpu className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
                  <span>L4 Doğrulama Kütüphanesi</span>
                  <span className="text-slate-500 text-[11px]">1.307 Test (%100)</span>
                </div>
              </div>
            </div>
          </div>

          {/* Column 2: Çözümler / Solutions (Width: 3 cols) */}
          <div className="lg:col-span-3 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00]" />
              <span>{lang === "tr" ? "OTONOMİ ÇÖZÜMLERİ" : "AUTONOMY SOLUTIONS"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal">
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Hyundai Ioniq 5 Robotaksi" : "Hyundai Ioniq 5 Robotaxi"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "3D LiDAR SLAM & Haritalama" : "3D LiDAR SLAM & Mapping"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "100 Hz CAN-FD Aktüatör Köprüsü" : "100 Hz CAN-FD Actuation"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Taktik Savunma İKA Otonomisi" : "Tactical Defense UGV Core"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Enterprise SDK & Lisanslama" : "Enterprise SDK Licensing"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Standartlar ve Güvenlik / Standards & Safety (Width: 3 cols) */}
          <div className="lg:col-span-3 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-sky-400" />
              <span>{lang === "tr" ? "GÜVENLİK & STANDARTLAR" : "SAFETY & STANDARDS"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal">
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    ISO 26262 ASIL-D
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    {lang === "tr" ? "Emniyet" : "Safety"}
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    UN ECE R157 & R155
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    {lang === "tr" ? "Regülasyon" : "Regulation"}
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/siber/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    SecOC & Kriptografik CAN
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    HMAC-SHA256
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    OIN 2.0 Patent Savunma Paktı
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    #f1e44576
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/ihracat/" className="hover:text-white transition-colors flex items-center justify-between group">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Çift Kullanım (Dual-Use)" : "Dual-Use Compliance"}
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    {lang === "tr" ? "İhracat" : "Export"}
                  </span>
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 4: Kurumsal & İletişim (Width: 2 cols) */}
          <div className="lg:col-span-2 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
              <span>{lang === "tr" ? "KURUMSAL" : "CORPORATE"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal">
              <li>
                <Link href="/hakkimizda/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform">
                  {lang === "tr" ? "Hakkımızda & Vizyon" : "About & Vision"}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform">
                  {lang === "tr" ? "İletişim & Şartname" : "Contact & Specs"}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform">
                  {lang === "tr" ? "Kariyer & Ar-Ge" : "Careers"}
                </Link>
              </li>
              <li>
                <Link href="/politika/mulkiyet/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform">
                  {lang === "tr" ? "Fikri Mülkiyet (IP)" : "Intellectual Property"}
                </Link>
              </li>
              <li>
                <Link href="/politika/kvkk/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform">
                  {lang === "tr" ? "Gizlilik & KVKK" : "Privacy Policy"}
                </Link>
              </li>
            </ul>
          </div>

        </div>

        {/* Bottom Bar: Clean, Balanced Editorial Strip */}
        {/* Desktop View (100% UNTOUCHED ORIGINAL LAYOUT) */}
        <div className="hidden sm:flex items-center justify-between gap-4 text-xs text-slate-400 font-normal">
          <div className="flex items-center gap-2">
            <span>© {new Date().getFullYear()}</span>
            <span className="text-white font-medium">Trustia AI Technologies</span>
            <span className="text-slate-600">•</span>
            <span className="text-slate-500">
              {lang === "tr" ? "İstanbul, Türkiye (Ar-Ge ve Mühendislik)" : "Istanbul, TR • Autonomy Engineering"}
            </span>
          </div>

          <div className="flex items-center gap-4 text-[11px] text-slate-400 font-mono">
            <Link href="/politika/kvkk/" className="hover:text-white transition-colors">
              KVKK / GDPR
            </Link>
            <span className="text-slate-700">•</span>
            <Link href="/politika/ihracat/" className="hover:text-white transition-colors">
              Dual-Use
            </Link>
            <span className="text-slate-700">•</span>
            <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors">
              OIN 2.0
            </Link>
            <span className="text-slate-700">•</span>
            <Link href="/politika/lisans/" className="hover:text-white transition-colors">
              SLA / EULA
            </Link>
          </div>
        </div>

        {/* Mobile View (sm:hidden - Dedicated High-End Ergonomic Layout) */}
        <div className="flex sm:hidden flex-col items-center gap-4 text-center pt-2">
          {/* Symmetrical 2x2 Glass Pill Grid for Compliance & Legal Links */}
          <div className="grid grid-cols-2 gap-2 w-full max-w-xs font-mono text-[11px]">
            <Link
              href="/politika/kvkk/"
              className="py-2.5 px-3 rounded-lg bg-white/[0.04] border border-white/10 text-slate-300 hover:text-white active:bg-white/10 transition-colors flex items-center justify-center font-medium"
            >
              KVKK / GDPR
            </Link>
            <Link
              href="/politika/ihracat/"
              className="py-2.5 px-3 rounded-lg bg-white/[0.04] border border-white/10 text-slate-300 hover:text-white active:bg-white/10 transition-colors flex items-center justify-center font-medium"
            >
              Dual-Use
            </Link>
            <Link
              href="/politika/oin-lisans/"
              className="py-2.5 px-3 rounded-lg bg-white/[0.04] border border-white/10 text-slate-300 hover:text-white active:bg-white/10 transition-colors flex items-center justify-center font-medium"
            >
              OIN 2.0
            </Link>
            <Link
              href="/politika/lisans/"
              className="py-2.5 px-3 rounded-lg bg-white/[0.04] border border-white/10 text-slate-300 hover:text-white active:bg-white/10 transition-colors flex items-center justify-center font-medium"
            >
              SLA / EULA
            </Link>
          </div>

          {/* Symmetrical Centered Copyright & Location */}
          <div className="space-y-1 text-xs text-slate-400">
            <div className="flex items-center justify-center gap-1.5 font-medium text-slate-300">
              <span>© {new Date().getFullYear()}</span>
              <span className="text-white font-semibold">Trustia AI Technologies</span>
            </div>
            <p className="text-[11px] text-slate-400">
              {lang === "tr" ? "İstanbul, Türkiye • Tüm Hakları Saklıdır" : "Istanbul, TR • All Rights Reserved"}
            </p>
          </div>
        </div>

      </div>
    </footer>
  );
}
