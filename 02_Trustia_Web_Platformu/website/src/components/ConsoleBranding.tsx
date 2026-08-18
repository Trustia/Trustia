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
      "%c TRUSTIA AUTONOMOUS SYSTEMS INC. %c DEFENSE UGV AUTONOMY PLATFORM v2.0 ",
      "background: #C8FF00; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 10px; border-radius: 4px 0 0 4px;",
      "background: #10b981; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 10px; border-radius: 0 4px 4px 0;"
    );

    console.log(
      "%c\n[SİSTEM MİMARİSİ]: %cSTANAG 4586 Level 4 • SAE AS6091 JAUS • ROS 2 Humble Core\n[GÜVENLİK PROTOKOLÜ]: %cHMAC-SHA256 Şifrelenmiş Telemetri & Otonom Eve Dönüş (RTH) Aktif\n[KORUMA BİLDİRİMİ]: %cBu konsol alanı kurumsal savunma protokollerince kayıt altına alınmaktadır.",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #ffffff; font-family: monospace; font-size: 11px;",
      "color: #10b981; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;"
    );

    console.log(
      "%c\n📩 İletişim & Tedarik: %ciletisim@trustia.com.tr %c| 🇺🇸 Dover, Delaware, USA • 🇹🇷 İstanbul, Türkiye\n",
      "color: #94a3b8; font-family: monospace; font-size: 11px;",
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 11px;",
      "color: #94a3b8; font-family: monospace; font-size: 11px;"
    );
  }, []);

  return null;
}
