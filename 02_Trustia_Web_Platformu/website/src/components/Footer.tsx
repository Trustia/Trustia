"use client";

import Link from "next/link";
import { ShieldCheck, CheckCircle2, ArrowUpRight, Cpu, Globe } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";
import TopographicCanvas from "@/components/TopographicCanvas";

export default function Footer() {
  const { lang } = useLanguage();

  return (
    <footer id="kurumsal" className="relative w-full bg-[#14120c] text-slate-200 font-sans text-xs pt-16 sm:pt-20 pb-12 px-6 sm:px-12 z-20 overflow-hidden select-none">
      <TopographicCanvas
        className="absolute inset-0 w-full h-full pointer-events-auto opacity-80 sm:opacity-65"
        inkColor="216, 200, 124"
        bands={44}
        step={7}
        freq={0.021}
        interactive={true}
      />

      {/* Top Edge Seamless Gradient Blend */}
      <div className="absolute top-0 inset-x-0 h-16 bg-gradient-to-b from-[#14120c] to-transparent pointer-events-none z-1" />

      {/* Subtle Radial Ambient Center Glow for High Contrast Legibility */}
      <div className="absolute inset-0 bg-radial-[at_50%_50%] from-transparent via-[#14120c]/20 to-[#14120c]/60 pointer-events-none z-1" />

      {/* Footer Content Inner */}
      <div className="max-w-7xl mx-auto space-y-12 sm:space-y-14 relative z-10 pointer-events-none">
        
        {/* ========================================================
            1. DESKTOP VIEW: 4-Column Balanced Architectural Matrix
           ======================================================== */}
        <div className="hidden lg:grid lg:grid-cols-12 gap-10 lg:gap-12 pb-12 border-b border-white/15">
          
          {/* Column 1: Brand & Verified Accreditation (Width: 4 cols) */}
          <div className="lg:col-span-4 space-y-5">
            {/* Logo */}
            <Link href="/" className="inline-flex items-center gap-2.5 group select-none pointer-events-auto">
              <div className="w-8 h-8 rounded-lg overflow-hidden shrink-0 shadow-md">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/logo.png" alt="Trustia AI Logo" className="w-full h-full object-cover" />
              </div>
              <div className="flex items-center gap-1.5 drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
                <span className="font-bold text-xl text-white tracking-tight">Trustia</span>
                <span className="font-bold text-xl text-[#C8FF00] tracking-tight">AI</span>
              </div>
            </Link>

            {/* Tagline */}
            <p className="text-slate-300 text-xs sm:text-[13px] leading-relaxed font-normal max-w-sm drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              {lang === "tr"
                ? "Ticari elektrikli araç filoları ve çift amaçlı otonom sistemler için 29.748+ satırlık deterministik Seviye-4 otonom sürüş yazılım çekirdeği."
                : "Deterministic 29,748+ LOC Level-4 reference autonomy architecture engineered for commercial electric fleets and sovereign autonomous systems."}
            </p>

            {/* Verified Accreditation Tags */}
            <div className="pt-2 space-y-2.5">
              <div className="text-[10px] font-mono tracking-widest text-[#C8FF00] uppercase font-semibold drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                {lang === "tr" ? "// DOĞRULANMIŞ KURUMSAL KÜTÜK" : "// VERIFIED REGISTRY"}
              </div>
              <div className="space-y-2 text-xs font-mono drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                <div className="flex items-center gap-2.5 text-slate-200">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>ASELSAN &amp; STM Savunma</span>
                  <span className="text-slate-400 text-[11px]">#0050569 / SAP</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-200">
                  <ShieldCheck className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span>OIN 2.0 Patent Paktı</span>
                  <span className="text-slate-400 text-[11px]">#f1e44576</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-200">
                  <Globe className="w-3.5 h-3.5 text-sky-400 shrink-0" />
                  <span>AB PIC &amp; EIT Mobility</span>
                  <span className="text-slate-400 text-[11px]">861711529 • CUS15554</span>
                </div>
                <div className="flex items-center gap-2.5 text-slate-200">
                  <Cpu className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
                  <span>198 Dosya / 29.748+ Satır</span>
                  <span className="text-slate-400 text-[11px]">1.307 + 21 Test (%100)</span>
                </div>
              </div>
            </div>
          </div>

          {/* Column 2: Çözümler / Solutions (Width: 3 cols) */}
          <div className="lg:col-span-3 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2 drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              <span className="w-1.5 h-1.5 rounded-full bg-[#C8FF00]" />
              <span>{lang === "tr" ? "OTONOMİ ÇÖZÜMLERİ" : "AUTONOMY SOLUTIONS"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "L4 Robotaksi (Ioniq 5 & MIFA 7)" : "L4 Robotaxi (Ioniq 5 & MIFA 7)"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "3D LiDAR SLAM & PTP Deskewing" : "3D LiDAR SLAM & PTP Deskewing"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "100 Hz CAN-FD & MPC Kontrol" : "100 Hz CAN-FD & MPC Control"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Taktik Savunma İKA Otonomisi" : "Tactical Defense UGV Core"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Kapalı Kutu (.pyc) Enterprise SDK" : "Closed-Box (.pyc) Enterprise SDK"}
                  </span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00] transition-colors" />
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Standartlar ve Güvenlik / Standards & Safety (Width: 3 cols) */}
          <div className="lg:col-span-3 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2 drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              <span className="w-1.5 h-1.5 rounded-full bg-sky-400" />
              <span>{lang === "tr" ? "GÜVENLİK & STANDARTLAR" : "SAFETY & STANDARDS"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    ISO 26262 ASIL-D &amp; SOTIF
                  </span>
                  <span className="text-[10px] font-mono text-slate-400 group-hover:text-slate-200 transition-colors">
                    IEEE 2846 RSS
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    UN R155, R156 &amp; R157
                  </span>
                  <span className="text-[10px] font-mono text-slate-400 group-hover:text-slate-200 transition-colors">
                    AB 2022/1426
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/siber/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    CAN-FD IDPS &amp; SecOC
                  </span>
                  <span className="text-[10px] font-mono text-slate-400 group-hover:text-slate-200 transition-colors">
                    HMAC-SHA256
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/oin-lisans/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    OIN 2.0 Patent Savunma Paktı
                  </span>
                  <span className="text-[10px] font-mono text-slate-400 group-hover:text-slate-200 transition-colors">
                    #f1e44576
                  </span>
                </Link>
              </li>
              <li>
                <Link href="/politika/ihracat/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                  <span className="group-hover:translate-x-0.5 transition-transform">
                    {lang === "tr" ? "Çift Kullanım (Dual-Use)" : "Dual-Use Compliance"}
                  </span>
                  <span className="text-[10px] font-mono text-slate-400 group-hover:text-slate-200 transition-colors">
                    {lang === "tr" ? "İhracat" : "Export"}
                  </span>
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 4: Kurumsal & İletişim (Width: 2 cols) */}
          <div className="lg:col-span-2 space-y-4">
            <h5 className="text-[11px] font-mono font-bold text-white tracking-widest uppercase flex items-center gap-2 drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
              <span>{lang === "tr" ? "KURUMSAL" : "CORPORATE"}</span>
            </h5>
            <ul className="space-y-2.5 text-xs text-slate-300 font-normal drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
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

        {/* ========================================================
            2. MOBILE VIEW: Overland AI-Style Compact 2-Column Grid
           ======================================================== */}
        <div className="flex lg:hidden flex-col space-y-6 pb-8 border-b border-white/15">
          {/* Mobile Brand & Verified Status */}
          <div className="space-y-3.5 text-center flex flex-col items-center justify-center">
            <Link href="/" className="inline-flex items-center gap-2.5 group select-none pointer-events-auto justify-center">
              <div className="w-8 h-8 rounded-lg overflow-hidden shrink-0 shadow-md">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/logo.png" alt="Trustia AI Logo" className="w-full h-full object-cover" />
              </div>
              <div className="flex items-center gap-1.5 drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
                <span className="font-bold text-xl text-white tracking-tight">Trustia</span>
                <span className="font-bold text-xl text-[#C8FF00] tracking-tight">AI</span>
              </div>
            </Link>

            <p className="text-slate-300 text-xs leading-relaxed font-normal max-w-sm mx-auto drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
              {lang === "tr"
                ? "Ticari elektrikli filolar ve otonom sistemler için 29.748+ satırlık deterministik Seviye-4 otonom sürüş yazılım çekirdeği."
                : "Deterministic 29,748+ LOC Level-4 autonomy architecture for commercial fleets and autonomous robotics."}
            </p>

            {/* Symmetrical 2-Row Monospaced Registry Badges */}
            <div className="flex flex-col items-center justify-center gap-1.5 text-[11px] font-mono text-slate-300 drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)] w-full pt-1">
              <div className="flex items-center justify-center gap-2.5">
                <span className="text-[#C8FF00] font-semibold">ASELSAN #0050569 &amp; STM</span>
                <span className="text-slate-600 select-none">/</span>
                <span className="text-slate-200">OIN #f1e44576</span>
              </div>
              <div className="flex items-center justify-center gap-2">
                <span className="text-sky-400">AB PIC: 861711529</span>
                <span className="text-slate-600 select-none">/</span>
                <span className="text-emerald-400">1.307+21 Test (%100)</span>
              </div>
            </div>
          </div>

          {/* Overland AI Style: Symmetric 2-Column Link Grid */}
          <div className="grid grid-cols-2 gap-x-6 gap-y-6 pt-2">
            
            {/* Column 1: Çözümler / Solutions */}
            <div className="space-y-3">
              <h6 className="text-[10px] font-mono font-bold text-[#C8FF00] tracking-widest uppercase drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                {lang === "tr" ? "ÇÖZÜMLER" : "SOLUTIONS"}
              </h6>
              <ul className="space-y-2 text-xs text-slate-200 font-sans drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                <li>
                  <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>L4 Robotaksi</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>3D LiDAR SLAM</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/robotaxi/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>CAN-FD &amp; MPC</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>Savunma İKA</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/politika/lisans/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>Enterprise SDK</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
              </ul>
            </div>

            {/* Column 2: Güvenlik & Kurumsal */}
            <div className="space-y-3">
              <h6 className="text-[10px] font-mono font-bold text-[#C8FF00] tracking-widest uppercase drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                {lang === "tr" ? "GÜVENLİK & ŞİRKET" : "STANDARDS & CORP"}
              </h6>
              <ul className="space-y-2 text-xs text-slate-200 font-sans drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
                <li>
                  <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>ASIL-D &amp; RSS</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/politika/otonom-guvenlik/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>UN R155/156/157</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/hakkimizda/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>{lang === "tr" ? "Hakkımızda" : "About Us"}</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/iletisim/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>{lang === "tr" ? "Kariyer & Ar-Ge" : "Careers"}</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
                <li>
                  <Link href="/iletisim/" className="hover:text-white transition-colors flex items-center justify-between group pointer-events-auto">
                    <span>{lang === "tr" ? "İletişim" : "Contact"}</span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-[#C8FF00]" />
                  </Link>
                </li>
              </ul>
            </div>

          </div>
        </div>

        {/* ========================================================
            3. BOTTOM BAR: Overland AI-Style Monospaced Strip
           ======================================================== */}
        {/* Desktop View */}
        <div className="hidden sm:flex items-center justify-between gap-4 text-[11px] font-mono text-slate-300 font-normal pointer-events-auto drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
          <div className="flex items-center gap-2">
            <span>(C) {new Date().getFullYear()}</span>
            <span className="text-white font-medium">TRUSTIA AI TECHNOLOGIES™</span>
            <span className="text-slate-500">/</span>
            <span className="text-slate-300">EST 2026</span>
            <span className="text-slate-500">/</span>
            <span className="text-slate-300">İSTANBUL / TÜRKİYE</span>
          </div>

          <div className="flex items-center gap-3 text-[11px] text-slate-300 font-mono">
            <Link href="/politika/kvkk/" className="hover:text-[#C8FF00] transition-colors">
              KVKK / GDPR
            </Link>
            <span className="text-slate-500">/</span>
            <Link href="/politika/ihracat/" className="hover:text-[#C8FF00] transition-colors">
              DUAL-USE
            </Link>
            <span className="text-slate-500">/</span>
            <Link href="/politika/oin-lisans/" className="hover:text-[#C8FF00] transition-colors">
              OIN 2.0
            </Link>
            <span className="text-slate-500">/</span>
            <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors">
              SLA / EULA ⤵
            </Link>
          </div>
        </div>

        {/* Mobile View */}
        <div className="flex sm:hidden flex-col items-center gap-3 text-center font-mono text-[11px] pointer-events-auto drop-shadow-[0_1px_2px_rgba(0,0,0,0.9)]">
          <div className="flex flex-col items-center gap-1.5 text-slate-300">
            <div className="flex items-center gap-3">
              <Link href="/politika/kvkk/" className="hover:text-[#C8FF00] transition-colors">
                KVKK / GDPR
              </Link>
              <span className="text-slate-500">/</span>
              <Link href="/politika/ihracat/" className="hover:text-[#C8FF00] transition-colors">
                DUAL-USE
              </Link>
            </div>
            <div className="flex items-center gap-3">
              <Link href="/politika/oin-lisans/" className="hover:text-[#C8FF00] transition-colors">
                OIN 2.0
              </Link>
              <span className="text-slate-500">/</span>
              <Link href="/politika/lisans/" className="hover:text-[#C8FF00] transition-colors">
                SLA / EULA ⤵
              </Link>
            </div>
          </div>

          <div className="text-[10px] text-slate-300 space-y-0.5 pt-1">
            <div>(C) {new Date().getFullYear()} TRUSTIA AI TECHNOLOGIES™ / EST 2026</div>
            <div className="text-slate-400 tracking-wider">İSTANBUL / TÜRKİYE • ALL RIGHTS RESERVED</div>
          </div>
        </div>

      </div>
    </footer>
  );
}
