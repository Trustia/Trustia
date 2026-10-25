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
      "%c TRUSTIA AI %c LEVEL-4 AUTONOMY CORE v4.2.0 %c 1.307 TEST: %100 GEÇTİ ",
      "background: #C8FF00; color: #000; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px; border-radius: 4px 0 0 4px;",
      "background: #0284c7; color: #fff; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px;",
      "background: #10b981; color: #000; font-weight: 800; font-family: monospace; font-size: 11px; padding: 4px 8px; border-radius: 0 4px 4px 0;"
    );

    console.log(
      "%c\n[KURUCU & MİMAR]: %cMurat Furkan Bayram %c(%100 Tek Pay Sahibi, Kurucu & CEO)\n" +
      "%c[SİSTEM MİMARİSİ]: %c16.400+ Satır Deterministik C++20 / ROS 2 Humble • Hyundai Ioniq 5 CAN-FD\n" +
      "%c[DOĞRULAMA SUİTİ]: %c1.307 / 1.307 Birim, Entegrasyon & Simülasyon Testi (%100 Yeşil)\n" +
      "%c[EMNİYET & ASIL-D]: %cISO 26262 ASIL-D MRM Safe Stop • 50ms Watchdog • 1.4ms Gecikme\n" +
      "%c[NAVİGASYON & SLAM]: %cGNSS-Denied 3D NDT SLAM • 400Hz ESKF Sensör Füzyonu (<4.2 cm Drift)\n" +
      "%c[RESMİ TESCİLLER]: %cASELSAN Onaylı Tedarikçi (#0050569) • OIN Küresel Patent Paktı (#f1e44576) • AB PIC (861711529) • İTO BTM Kampüsü",
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
