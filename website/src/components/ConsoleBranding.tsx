"use client";

import { useEffect } from "react";

export default function ConsoleBranding() {
  useEffect(() => {
    // Ultra-Premium Corporate Defense Console Banner
    const asciiArt = `
  ████████╗██████╗ ██╗███████╗████████╗██╗ █████╗     █████╗ ██╗
  ╚══██╔══╝██╔══██╗██║██╔════╝╚══██╔══╝██║██╔══██╗   ██╔══██╗██║
     ██║   ██████╔╝██║███████╗   ██║   ██║███████║   ███████║██║
     ██║   ██╔══██╗██║╚════██║   ██║   ██║██╔══██║   ██╔══██║██║
     ██║   ██║  ██║██║███████║   ██║   ██║██║  ██║   ██║  ██║██║
     ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝
    `;

    console.clear();

    console.log(
      `%c${asciiArt}`,
      "color: #C8FF00; font-weight: bold; font-family: monospace; font-size: 10px;"
    );

    console.log(
      "%c TRUSTIA TEKNOLOJİ %c MILLI OTONOMİ YAZILIM ÇEKİRDEĞİ V2.0 ",
      "background: #C8FF00; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 8px; border-radius: 4px 0 0 4px;",
      "background: #10b981; color: #000; font-weight: bold; font-family: monospace; font-size: 12px; padding: 4px 8px; border-radius: 0 4px 4px 0;"
    );

    console.log(
      "%c\n[SİSTEM NİZAMI]: %cSTANAG 4586 Level 4 & SAE AS6091 JAUS Uyumlu %100 Yerli Sürücü Mimarisi\n[GÜVENLİK BİLDİRİMİ]: %cHMAC-SHA256 Şifrelenmiş Sinyal & Sinyal Kesintisinde Eve Dönüş (RTH) Aktif\n[GÜVENLİK UYARISI]: %cBu konsol alanı üzerinden doğrudan kod yürütme girişimleri siber denetim protokollerince kaydedilmektedir.",
      "color: #C8FF00; font-weight: bold; font-family: monospace;",
      "color: #ffffff; font-family: monospace;",
      "color: #10b981; font-family: monospace;",
      "color: #f59e0b; font-family: monospace;"
    );

    console.log(
      "%c\n📩 Kurumsal İletişim & Entegrasyon: %ciletisim@trustia.com.tr %c| 📍 İstanbul, Türkiye\n",
      "color: #94a3b8; font-family: monospace;",
      "color: #C8FF00; font-weight: bold; font-family: monospace;",
      "color: #94a3b8; font-family: monospace;"
    );
  }, []);

  return null;
}
