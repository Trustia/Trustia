"use client";

import React, { createContext, useContext, useState, useEffect } from "react";

type Language = "tr" | "en";

interface LanguageContextType {
  lang: Language;
  setLang: (lang: Language) => void;
  toggleLang: () => void;
  t: (key: string) => string;
}

const translations: Record<Language, Record<string, string>> = {
  tr: {
    // Navbar
    nav_about: "HAKKIMIZDA",
    nav_autonomy: "OTONOMİ",
    nav_threat: "TEHDİT TESPİTİ",
    nav_swarm: "SÜRÜ ZEKASI",
    nav_cert: "SERTİFİKASYON",
    nav_contact: "İLETİŞİM",

    // Hero
    hero_badge: "%100 YERLİ KATKI SERTİFİKASYON UYUMLU",
    hero_title_1: "Zorlu Operasyon Sahalarında",
    hero_title_2: "Tam Otonom Milli İrade",
    hero_desc: "GPS sinyalinin bulunmadığı veya engellendiği harekat alanlarında İnsansız Kara Araçları (İKA) için geliştirilmiş sıfır dış bağımlılıklı askeri otonomi platformu.",
    hero_btn_explore: "SİSTEMİ İNCELE",
    hero_btn_demo: "DEMO TALEP ET",
    hero_sound_mute: "Sessiz",
    hero_sound_unmute: "Sesi Aç",

    // Tech Matrix
    matrix_badge: "MİLLİ OTONOMİ MİMARİSİ",
    matrix_title: "GPS Olmayan Sahalarda Yüksek Hassasiyetli Otonom İntikal",
    matrix_desc: "Düşman karıştırması veya coğrafi engeller nedeniyle küresel konumlama (GPS) sinyali alınamayan kritik harekat alanlarında tam güvenilirlikle çalışan otonom sürüş çekirdeği.",
    card_1_title: "GPS-Denied Görsel SLAM",
    card_1_desc: "Kameralar ve LiDAR ile 3D haritalama. GPS bağımlılığı sıfır.",
    card_2_title: "Heterojen Sürü Zekası",
    card_2_desc: "Çoklu İKA sistemleri arasında anlık karar paylaşımı ve formasyon.",
    card_3_title: "Yapay Zeka Tehdit Tespiti",
    card_3_desc: "YOLOV8 tabanlı anlık mayın, EYP ve hedef tespit algoritması.",
    card_4_title: "STANAG 4586 Uyumlu Kontrol",
    card_4_desc: "NATO standartlarında veri bağı ve komuta kontrol mimarisi.",

    // Gallery
    gallery_title: "Saha Testleri ve Yerli Donanım Entegrasyonu",
    gallery_subtitle: "Farklı arazi ve hava koşullarında %100 doğrulukla doğrulanan sürü otonomisi.",

    // Contact
    contact_title: "Savunma ve Entegrasyon Talebi",
    contact_desc: "Askeri platform entegrasyonu, teknik sunum ve saha demosu talepleri için kurumsal ekibimizle iletişime geçin.",

    // Footer
    footer_tagline: "GPS-Denied Sahalar İçin İnsansız Kara Araçları Otonomi Platformu.",
    footer_rights: "Tüm hakları saklıdır."
  },
  en: {
    // Navbar
    nav_about: "ABOUT US",
    nav_autonomy: "AUTONOMY",
    nav_threat: "THREAT DETECTION",
    nav_swarm: "SWARM INTELLIGENCE",
    nav_cert: "CERTIFICATION",
    nav_contact: "CONTACT",

    // Hero
    hero_badge: "100% INDIGENOUS & CERTIFIED DEFENSE PLATFORM",
    hero_title_1: "In GPS-Denied Operating Theatres",
    hero_title_2: "Fully Autonomous Defense Autonomy",
    hero_desc: "Zero-dependency military autonomy platform developed for Unmanned Ground Vehicles (UGVs) operating in jammed and GPS-denied environments.",
    hero_btn_explore: "EXPLORE PLATFORM",
    hero_btn_demo: "REQUEST DEMO",
    hero_sound_mute: "Mute",
    hero_sound_unmute: "Unmute",

    // Tech Matrix
    matrix_badge: "NATIONAL AUTONOMY ARCHITECTURE",
    matrix_title: "High-Precision Autonomous Navigation in GPS-Denied Environments",
    matrix_desc: "Autonomous driving core operating with absolute reliability in critical operating theatres where global positioning (GPS) is jammed or unavailable.",
    card_1_title: "GPS-Denied Visual SLAM",
    card_1_desc: "3D mapping via Cameras and LiDAR. Zero GPS dependency.",
    card_2_title: "Heterogeneous Swarm Intelligence",
    card_2_desc: "Instant decision-sharing and tactical formation between multiple UGVs.",
    card_3_title: "AI Threat Detection",
    card_3_desc: "YOLOv8-based real-time mine, IED and target detection algorithm.",
    card_4_title: "STANAG 4586 Compliant Control",
    card_4_desc: "NATO-standard data link and command-control architecture.",

    // Gallery
    gallery_title: "Field Tests and Native Hardware Integration",
    gallery_subtitle: "Swarm autonomy validated with 100% accuracy across extreme terrains and weather conditions.",

    // Contact
    contact_title: "Defense & Integration Request",
    contact_desc: "Contact our executive team for military platform integration, technical briefings, and live field demonstration requests.",

    // Footer
    footer_tagline: "Unmanned Ground Vehicle Autonomy Platform for GPS-Denied Operating Theatres.",
    footer_rights: "All rights reserved."
  }
};

const LanguageContext = createContext<LanguageContextType>({
  lang: "tr",
  setLang: () => {},
  toggleLang: () => {},
  t: (key: string) => key
});

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [lang, setLangState] = useState<Language>("tr");

  useEffect(() => {
    const saved = localStorage.getItem("trustia_lang") as Language;
    if (saved === "tr" || saved === "en") {
      setLangState(saved);
    }
  }, []);

  const setLang = (newLang: Language) => {
    setLangState(newLang);
    localStorage.setItem("trustia_lang", newLang);
  };

  const toggleLang = () => {
    setLang(lang === "tr" ? "en" : "tr");
  };

  const t = (key: string): string => {
    return translations[lang]?.[key] || translations["tr"]?.[key] || key;
  };

  return (
    <LanguageContext.Provider value={{ lang, setLang, toggleLang, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  return useContext(LanguageContext);
}
