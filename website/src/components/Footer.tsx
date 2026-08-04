"use client";

import Link from "next/link";
import { CheckCircle2, MapPin, Globe, Shield, Cpu } from "lucide-react";

export default function Footer() {
  return (
    <footer id="iletisim" className="w-full bg-[#050505] border-t border-[#1a1a1a] text-slate-400 font-sans text-xs pt-20 pb-12 px-6 sm:px-12 relative z-20 selection:bg-[#C8FF00] selection:text-black">
      
      {/* Background Subtle Low-Opacity Grid Pattern */}
      <div className="absolute inset-0 bg-tactical-grid opacity-15 pointer-events-none"></div>

      <div className="max-w-7xl mx-auto relative z-10">
        {/* 4 Columns Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-16 mb-20">
          
          {/* Column 1: Şirket */}
          <div className="space-y-5">
            {/* Logo */}
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

            {/* Description */}
            <p className="text-slate-400 text-xs leading-relaxed font-light">
              GPS&apos;in bulunmadığı veya engellendiği zorlu harekat alanlarında İnsansız Kara Araçları (İKA) için geliştirilmiş %100 yerli askeri otonom sürüş ve algılama yazılım platformu.
            </p>

            {/* Location & Military Badges */}
            <div className="pt-2 space-y-2.5 font-mono text-[11px] text-slate-300">
              <div className="flex items-center gap-2 text-[#C8FF00] font-medium">
                <Globe className="w-3.5 h-3.5 shrink-0" />
                <span>Türkiye&apos;de geliştirildi.</span>
              </div>
              <div className="flex items-center gap-2 text-slate-400">
                <MapPin className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>İstanbul, Türkiye</span>
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
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">PLATFORM</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li>
                <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  Yazılım Mimarisi
                </Link>
              </li>
              <li>
                <Link href="/politika/etik" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  Otonomi Motoru
                </Link>
              </li>
              <li>
                <Link href="/politika/etik" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  Algılama Sistemi
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  ROS2
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors duration-200 hover:translate-x-0.5 inline-block">
                  API Dokümantasyonu
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Sertifikasyon */}
          <div className="space-y-5">
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">SERTİFİKASYON</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/yerlilik" className="hover:text-[#C8FF00] transition-colors">
                  %100 Yerli Katkı
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/siber" className="hover:text-[#C8FF00] transition-colors">
                  HMAC-SHA256
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/ihracat" className="hover:text-[#C8FF00] transition-colors">
                  SAE AS9100
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/siber" className="hover:text-[#C8FF00] transition-colors">
                  ISO 27001
                </Link>
              </li>
              <li className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors">
                  ROS2 Uyumlu
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 4: Kurumsal */}
          <div className="space-y-5">
            <h5 className="font-mono text-xs font-bold text-white tracking-widest uppercase">KURUMSAL</h5>
            <ul className="space-y-3 font-normal text-slate-300">
              <li>
                <Link href="/hakkimizda" className="hover:text-[#C8FF00] transition-colors">
                  Hakkımızda
                </Link>
              </li>
              <li>
                <Link href="/iletisim" className="hover:text-[#C8FF00] transition-colors flex items-center gap-2">
                  <span>Kariyer</span>
                  <span className="text-[9px] font-mono px-1.5 py-0.5 bg-[#C8FF00]/15 text-[#C8FF00] border border-[#C8FF00]/30 rounded font-bold">BİZE KATILIN</span>
                </Link>
              </li>
              <li>
                <Link href="/iletisim" className="hover:text-[#C8FF00] transition-colors">
                  İletişim
                </Link>
              </li>
              <li>
                <Link href="/#kurumsal" className="hover:text-[#C8FF00] transition-colors">
                  Basın
                </Link>
              </li>
              <li>
                <Link href="/politika/kvkk" className="hover:text-[#C8FF00] transition-colors">
                  Gizlilik Politikası
                </Link>
              </li>
              <li>
                <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors">
                  Kullanım Koşulları
                </Link>
              </li>
            </ul>
          </div>

        </div>

        {/* Thin Divider Line */}
        <div className="w-full h-[1px] bg-[#1a1a1a] mb-8"></div>

        {/* Bottom Satır */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-6 text-[11px] font-normal text-slate-500">
          {/* Left Copyright */}
          <div>
            © 2026 Trustia Teknoloji. Tüm hakları saklıdır.
          </div>

          {/* Center Links */}
          <div className="flex flex-wrap items-center justify-center gap-4 text-slate-400 font-sans">
            <Link href="/politika/kvkk" className="hover:text-[#C8FF00] transition-colors duration-200">
              KVKK & Gizlilik
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/lisans" className="hover:text-[#C8FF00] transition-colors duration-200">
              Lisans & SLA
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/mulkiyet" className="hover:text-[#C8FF00] transition-colors duration-200">
              Fikri Mülkiyet & Telif
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/yerlilik" className="hover:text-[#C8FF00] transition-colors duration-200">
              %100 Yerlilik
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/siber" className="hover:text-[#C8FF00] transition-colors duration-200">
              Siber Güvenlik
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/etik" className="hover:text-[#C8FF00] transition-colors duration-200">
              Yapay Zeka Etiği
            </Link>
            <span className="text-white/10">•</span>
            <Link href="/politika/ihracat" className="hover:text-[#C8FF00] transition-colors duration-200">
              İhracat Uyum
            </Link>
          </div>

          {/* Right Modern Line Social Icons */}
          <div className="flex items-center gap-4">
            {/* LinkedIn */}
            <a
              href="https://linkedin.com"
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 rounded-lg bg-white/5 border border-white/10 text-slate-400 hover:text-[#C8FF00] hover:border-[#C8FF00]/40 transition-all duration-200"
              aria-label="LinkedIn"
            >
              <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24z"/>
              </svg>
            </a>

            {/* GitHub */}
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 rounded-lg bg-white/5 border border-white/10 text-slate-400 hover:text-[#C8FF00] hover:border-[#C8FF00]/40 transition-all duration-200"
              aria-label="GitHub"
            >
              <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/>
              </svg>
            </a>

            {/* X (Twitter) */}
            <a
              href="https://twitter.com"
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 rounded-lg bg-white/5 border border-white/10 text-slate-400 hover:text-[#C8FF00] hover:border-[#C8FF00]/40 transition-all duration-200"
              aria-label="X (Twitter)"
            >
              <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
            </a>
          </div>

        </div>

      </div>
    </footer>
  );
}
