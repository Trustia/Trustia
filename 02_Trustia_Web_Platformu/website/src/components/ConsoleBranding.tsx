"use client";

import { useEffect } from "react";

export default function ConsoleBranding() {
  useEffect(() => {
    const asciiArt = `
  ████████╗██████╗ ██╗   ██╗███████╗████████╗██╗ █████╗      █████╗ ██╗
  ╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔══██╗    ██╔══██╗██║
     ██║   ██████╔╝██║   ██║███████╗   ██║   ██║███████║    ███████║██║
     ██║   ██╔══██╗██║   ██║╚════██║   ██║   ██║██╔══██║    ██╔══██║██║
     ██║   ██║  ██║╚██████╔╝███████║   ██║   ██║██║  ██║    ██║  ██║██║
     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
    `;

    console.clear();

    console.log(
      `%c${asciiArt}`,
      "color: #C8FF00; font-weight: 900; font-family: monospace; font-size: 11px; line-height: 1.2;"
    );

    console.log(
      "%c TRUSTIA AI %c LEVEL-4 AUTONOMY CORE v4.4.0 %c 1.329 + 21 TEST: %100 GEÇTİ ",
      "background: #C8FF00; color: #000; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px; border-radius: 4px 0 0 4px;",
      "background: #0284c7; color: #fff; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px;",
      "background: #10b981; color: #000; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px; border-radius: 0 4px 4px 0;"
    );

    console.log(
      "%c\n[KURUCU & MİMAR]: %cMurat Furkan Bayram %c(%100 Tek Pay Sahibi, Kurucu & Sistem Mimarı)\n" +
      "%c[SİSTEM ENVANTERİ]: %c203 Dosya / 31.400+ Satır Deterministik C++20, Python 3.12 & ROS 2 Humble\n" +
      "%c[DOĞRULAMA SUİTİ]: %c1.329 Çekirdek + 21 Kapalı Kutu SDK Testi (%100 Yeşil, 0 Hata / 0 Fail)\n" +
      "%c[EMNİYET & REGÜLASYON]: %cISO 26262 ASIL-D • ISO 21448 SOTIF • IEEE 2846 RSS • UN R155/R156/R157 • AB 2022/1426\n" +
      "%c[NAVİGASYON & KONTROL]: %cGNSS-Denied 3D NDT SLAM • IEEE 1588v2 PTP • Frenet Lattice • Kayan Ufuklu MPC\n" +
      "%c[RESMİ TESCİLLER]: %cASELSAN (#0050569 / SAP: FZQHEXGFMTJU) • STM Savunma • Teknopark İstanbul • İTO BTM • YTÜ Yıldız Teknopark • OIN (#f1e44576) • AB PIC (861711529) • EIT (CUS15554) • KOSGEB (KSB01UGE0115153370) • BTK (L2zPtN4X1ZJ)",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #ffffff; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #e2e8f0; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #10b981; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #e2e8f0; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #e2e8f0; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #38bdf8; font-family: monospace; font-size: 11px;"
    );

    console.log(
      "%c\n📩 İletişim & Kariyer: %ckariyer@trustia.com.tr %c| %ciletisim@trustia.com.tr %c| 🇹🇷 İstanbul, Türkiye\n",
      "color: #94a3b8; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #64748b; font-family: monospace; font-size: 11px;",
      "color: #38bdf8; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;"
    );
  }, []);

  return null;
}
