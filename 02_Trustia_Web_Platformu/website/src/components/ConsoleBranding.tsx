"use client";

import { useEffect } from "react";

export default function ConsoleBranding() {
  useEffect(() => {
    // Ultra-Premium Corporate Defense Console Banner
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
      "%c TRUSTIA AI %c LEVEL-4 AUTONOMY PLATFORM v4.0 ",
      "background: #C8FF00; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 10px; border-radius: 4px 0 0 4px;",
      "background: #10b981; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 10px; border-radius: 0 4px 4px 0;"
    );

    console.log(
      "%c\n[SİSTEM MİMARİSİ]: %cSAE J3016 Seviye 4 • ISO 26262 ASIL-D • ROS 2 Humble Core\n[GÜVENLİK PROTOKOLÜ]: %cHMAC-SHA256 Şifrelenmiş CAN-FD & 5ms Donanımsal Devralma\n[KORUMA BİLDİRİMİ]: %cTüm hakları Trustia AI mülkiyetindedir.",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #ffffff; font-family: monospace; font-size: 11px;",
      "color: #10b981; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;"
    );

    console.log(
      "%c\n📩 İletişim & Tedarik: %ciletisim@trustia.com.tr %c| 🇹🇷 İstanbul, Türkiye\n",
      "color: #94a3b8; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;"
    );
  }, []);

  return null;
}
