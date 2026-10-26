"use client";

import Link from "next/link";
import { ShieldCheck, CheckCircle2, ArrowUpRight, Cpu, Globe } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TopographicCanvas from "@/components/TopographicCanvas";

export default function Footer() {
  const { lang } = useLanguage();

  return (
    <footer id="kurumsal" className="relative w-full bg-[#080a0c] text-slate-300 font-sans text-xs pt-20 pb-12 px-6 sm:px-12 z-20 overflow-hidden select-none">
      {/* 
        1. Overland AI-Style Procedural 2D Marching Squares Topographic Elevation Canvas:
        - 44-band Fractal Brownian Motion (fBm) elevation contour lines
        - Overland military gold tone (rgb(216, 200, 124))
        - Real-time interactive mouse ripple & elevation deform on click / touch
        - Double-click to randomly generate a new mountain topography
      */}
      <TopographicCanvas
        className="absolute inset-0 w-full h-full pointer-events-auto opacity-75"
        inkColor="216, 200, 124"
        bands={44}
        step={8}
        freq={0.021}
        interactive={true}
      />

      {/* Subtle Tactical Vignette & Legibility Dark Fade Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-[#090b0e] via-[#080a0c]/80 to-[#05070a]/92 pointer-events-none" />

      {/* Footer Content Inner (Pointer events pass through to canvas except on interactive links) */}
      <div className="max-w-7xl mx-auto space-y-14 relative z-10 pointer-events-none">
        
        {/* Main 4-Column Responsive Layout (100% KUTUSUZ & ÇERÇEVESİZ SAF TİPOGRAFİ) */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 pb-12 border-b border-white/10">
          
          {/* Column 1: Brand & Verified Accreditation (Width: 4 cols) */}
          <div className="lg:col-span-4 space-y-5">
            {/* Logo */}
            <Link href="/" className="inline-flex items-center gap-2.5 group select-none pointer-events-auto">
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
              <div className="text-[10px] font-mono tracking-widest text-[#C8FF00]/80 uppercase font-semibold">
                {lang === "tr" ? "// DOĞRULANMIŞ KURUMSAL KÜTÜK" : "// VERIFIED REGISTRY"}
              </div>
              <div className="space-y-2 text-xs font-mono">
                <div className="flex items-center gap-2.5 text-slate-300">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>ASELSAN & STM</span>
                  <span className="text-slate-500 text-[11px]">#{'0050569'}</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-300">
                  <ShieldCheck className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>NATO NCAGE Kodu</span>
                  <span className="text-slate-500 text-[11px]">TR26258467723</span>
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
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Hyundai Ioniq 5 Robotaksi" : "Hyundai Ioniq 5 Robotaxi"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "3D LiDAR SLAM & Haritalama" : "3D LiDAR SLAM & Mapping"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "100 Hz CAN-FD Aktüatör Köprüsü" : "100 Hz CAN-FD Actuation"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Taktik Savunma İKA Otonomisi" : "Tactical Defense UGV Core"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-600 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
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
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    ISO 26262 ASIL-D
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    {lang === "tr" ? "Emniyet" : "Safety"}
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    UN ECE R157 & R155
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    {lang === "tr" ? "Regülasyon" : "Regulation"}
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/siber/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    SecOC & Kriptografik CAN
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    HMAC-SHA256
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    OIN 2.0 Patent Savunma Paktı
                  </span>
                  <span className="text-[10px] font-mono text-slate-500 group-hover:text-slate-300 transition-colors">
                    #f1e44576
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/ihracat/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
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
                <Link href="/hakkimizda/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform pointer-events-auto">
                  {lang === "tr" ? "Hakkımızda & Vizyon" : "About & Vision"}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform pointer-events-auto">
                  {lang === "tr" ? "İletişim & Şartname" : "Contact & Specs"}
                </Link>
              </li>
              <li>
                <Link href="/iletisim/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform pointer-events-auto">
                  {lang === "tr" ? "Kariyer & Ar-Ge" : "Careers"}
                </Link>
              </li>
              <li>
                <Link href="/politika/mulkiyet/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform pointer-events-auto">
                  {lang === "tr" ? "Fikri Mülkiyet (IP)" : "Intellectual Property"}
                </Link>
              </li>
              <li>
                <Link href="/politika/kvkk/" className="hover:text-white transition-colors inline-block hover:translate-x-0.5 transition-transform pointer-events-auto">
                  {lang === "tr" ? "Gizlilik & KVKK" : "Privacy Policy"}
                </Link>
              </li>
            </ul>
          </div>

        </div>

        {/* Bottom Bar: Overland AI-Style Monospaced Tactical Metadata Strip (Sıfır Kutu, Sadece Tipografi) */}
        {/* Desktop View */}
        <div className="hidden sm:flex items-center justify-between gap-4 text-[11px] font-mono text-slate-400 font-normal pointer-events-auto">
          <div className="flex items-center gap-2">
            <span>(C) {new Date().getFullYear()}</span>
            <span className="text-white font-medium">TRUSTIA AI TECHNOLOGIES™</span>
            <span className="text-slate-600">/</span>
            <span className="text-slate-500">EST 2026</span>
            <span className="text-slate-600">/</span>
            <span className="text-slate-500">İSTANBUL / TÜRKİYE</span>
          </div>

          <div className="flex items-center gap-3 text-[11px] text-slate-400 font-mono">
            <Link href="/politika/kvkk/" className="hover:text-[#C8FF00] transition-colors">
              KVKK / GDPR
            </Link>
            <span className="text-slate-600">/</span>
            <Link href="/politika/ihracat/" className="hover:text-[#C8FF00] transition-colors">
              DUAL-USE
            </Link>
            <span className="text-slate-600">/</span>
            <Link href="/politika/oin-lisans/" className="hover:text-[#C8FF00] transition-colors">
              OIN 2.0
            </Link>
            <span className="text-slate-600">/</span>
            <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors">
              SLA / EULA ⤵
            </Link>
          </div>
        </div>

        {/* Mobile View: Overland AI-Style Monospaced Centered Strip */}
        <div className="flex sm:hidden flex-col items-center gap-3.5 text-center font-mono text-[11px] pointer-events-auto">
          {/* Pure Typographic Legal Links (Sıfır Kutu, Slash Delimiters) */}
          <div className="flex flex-col items-center gap-1.5 text-slate-400">
            <div className="flex items-center gap-3">
              <Link href="/politika/kvkk/" className="hover:text-[#C8FF00] transition-colors">
                KVKK / GDPR
              </Link>
              <span className="text-slate-600">/</span>
              <Link href="/politika/ihracat/" className="hover:text-[#C8FF00] transition-colors">
                DUAL-USE
              </Link>
            </div>
            <div className="flex items-center gap-3">
              <Link href="/politika/oin-lisans/" className="hover:text-[#C8FF00] transition-colors">
                OIN 2.0
              </Link>
              <span className="text-slate-600">/</span>
              <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors">
                SLA / EULA ⤵
              </Link>
            </div>
          </div>

          {/* Copyright Metadata */}
          <div className="text-[10px] text-slate-500 space-y-1 pt-1">
            <div>(C) {new Date().getFullYear()} TRUSTIA AI TECHNOLOGIES™ / EST 2026</div>
            <div className="text-slate-600 tracking-wider">İSTANBUL / TÜRKİYE • ALL RIGHTS RESERVED</div>
          </div>
        </div>

      </div>
    </footer>
  );
}
