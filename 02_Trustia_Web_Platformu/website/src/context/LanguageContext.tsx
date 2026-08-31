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
    // Top Ticker
    top_ticker_btm: "🏛️ İTO BTM (Bilgiyi Ticarileştirme Merkezi) Ön Kuluçka Kabulü",
    top_ticker_teknopark: "🏢 Teknopark İstanbul Girişimcilik Ekosistemi",
    top_ticker_yc: "🇺🇸 Seviye 4 Yerli Robotaksi ve Çift Amaçlı Otonomi",
    top_ticker_ssb: "🎖️ T.C. Savunma Sanayii Başkanlığı 100/100 Tam Puan Tescili",

    // Institutional Ecosystem
    eco_badge: "RESMİ KURUMLAR & AKREDİTASYONLAR",
    eco_title: "Devlet ve Ekosistem Onaylarımız",
    eco_desc: "Savunma Sanayii Başkanlığı, İstanbul Ticaret Odası, BTM, KOSGEB ve Teknopark İstanbul tarafından tescillenen resmi süreçlerimiz.",

    // Navbar
    nav_about: "HAKKIMIZDA",
    nav_robotaxi: "ROBOTAKSİ",
    nav_autonomy: "ÇÖZÜMLER",
    nav_threat: "TEKNOLOJİ",
    nav_swarm: "GÜVENLİK",
    nav_cert: "AKREDİTASYON",
    nav_contact: "İLETİŞİM",

    // Hero Section
    hero_badge: "MİLLİ OTONOM SİSTEMLER PLATFORMU",
    hero_title_1: "Sürücüsüz Ulaşım ve Savunma İçin",
    hero_title_2: "Seviye 4 Yerli Otonomi",
    hero_desc: "Trustia AI; şehir içi yerli Robotaksi filoları ve GPS sinyalinin kesildiği sahalarda görev yapan İnsansız Savunma Robotları için tam bağımsız otonomi yazılımı geliştirir.",
    hero_btn_explore: "ÇÖZÜMLERİ İNCELE",
    hero_btn_demo: "DEMO TALEP ET",
    hero_sound_mute: "Sessiz",
    hero_sound_unmute: "Ses Açık",

    // Gallery
    gallery_badge: "SAHA VE PLATFORM KATALOĞU",
    gallery_title: "Saha Testleri ve Platform Entegrasyonları",
    gallery_desc: "Farklı araç ve robot konfigürasyonlarında çalışan yerli otonomi yazılım beyni",
    gallery_p1_title: "01 // ARAZİ VE SAHA TESTİ",
    gallery_p1_badge: "BARKAN İKA",
    gallery_p2_title: "02 // SENSÖR FÜZYONU",
    gallery_p2_badge: "ALPAR İKA",
    gallery_p3_title: "03 // ENGEL KAÇINMA",
    gallery_p3_badge: "HİBRİT ROTA",
    gallery_p4_title: "04 // ÇEVRE ALGILAMA",
    gallery_p4_badge: "KAPGAN 8x8",
    gallery_p5_title: "05 // SÜRÜ ZEKASI",
    gallery_p5_badge: "ENGA 6x6",

    // About Page
    about_back: "← ANA SAYFAYA DÖN",
    about_badge: "KURUMSAL BİLGİ & VİZYON",
    about_title: "Trustia AI — Milli Otonomi Mimarisi",
    about_desc: "Trustia AI (İstanbul, Türkiye); şehir içi sivil Robotaksi filoları ve GPS sinyalinin bulunmadığı harekat sahalarında görev yapan İnsansız Kara Araçları (İKA) için Seviye 4 yerli otonomi yazılımı geliştiren yeni nesil teknoloji şirketidir.",
    about_c1_title: "Tam Bağımsız Yerli Yazılım",
    about_c1_desc: "Yabancı kapalı kutu sistemlere bağımlılığı sıfıra indiren, %100 özgün kaynak kod mülkiyetine sahip yerli otonomi çekirdeği.",
    about_c2_title: "1.301 Otomatik Doğrulama Testi",
    about_c2_desc: "16.000+ satır özgün deterministik mimari; 1.301 otomatik birim ve simülasyon testinden %100 başarıyla geçerek sahada doğrulanmıştır.",
    about_c3_title: "Evrensel Donanım Bağımsızlığı",
    about_c3_desc: "Standart CAN-Bus ve ROS 2 protokolleri sayesinde binek otomobillerden askeri zırhlı araçlara kadar her şasiye kolayca entegre olur.",
    about_founder_badge: "KURUCU & SİSTEM MİMARI",
    about_founder_title: "Murat Furkan Bayram",
    about_founder_role: "Kurucu & Sistem Mimarı",
    about_founder_bio: "KOSGEB İleri Girişimci ve T.C. Savunma Sanayii Başkanlığı 100/100 tam puan sertifikalı otonomi mühendisi. GPS'siz 3D SLAM, sürü zekası ve Seviye 4 yerli otonom sürüş mimarisini geliştirmiş olup şirketin teknoloji ve Ar-Ge yapılanmasını yönetmektedir.",

    // Contact
    contact_page_badge: "İLETİŞİM KANALLARI",
    contact_page_title: "Kurumsal İletişim & İş Birliği",
    contact_page_desc: "Robotaksi filoları, İKA otonomi yazılımı lisanslama ve yatırım süreçlerimiz için doğrudan ekibimizle iletişime geçin.",

    // Footer
    footer_tagline: "Sivil Robotaksi filoları ve zorlu harekat alanları için geliştirilmiş Seviye 4 yerli otonomi yazılım platformu.",
    footer_made_in: "İstanbul, Türkiye'de geliştirildi.",
    footer_locations: "İTO BTM Fulya & Teknopark İstanbul",
    footer_col_platform: "ÇÖZÜMLER",
    footer_link_arch: "Otonomi Mimarisi",
    footer_link_engine: "Robotaksi Platformu",
    footer_link_perception: "3D SLAM Haritalama",
    footer_link_ros: "Sürü Zekası",
    footer_link_api: "API & Entegrasyon",
    footer_col_cert: "AKREDİTASYON",
    footer_cert_indigenous: "%100 Yerli Katkı",
    footer_cert_crypto: "Savunma Sanayii Başkanlığı",
    footer_cert_as9100: "İTO BTM Ön Kuluçka",
    footer_cert_iso: "Teknopark İstanbul",
    footer_cert_ros: "KOSGEB İleri Girişimci",
    footer_col_corporate: "KURUMSAL",
    footer_link_about: "Hakkımızda",
    footer_link_career: "Kariyer",
    footer_badge_join: "BİZE KATILIN",
    footer_link_contact: "İletişim",
    footer_link_press: "Basın Kiti",
    footer_rights: "Tüm hakları saklıdır.",
    footer_entity: "Trustia AI"
  },
  en: {
    // Top Ticker
    top_ticker_btm: "🏛️ Istanbul Chamber of Commerce (BTM) Pre-Incubation Cohort",
    top_ticker_teknopark: "🏢 Teknopark Istanbul Defense & Deep Tech Ecosystem",
    top_ticker_yc: "🇺🇸 Level 4 Sovereign Robotaxi & Dual-Use Autonomy",
    top_ticker_ssb: "🎖️ Turkish Defense Industry Agency 100/100 Certification",

    // Institutional Ecosystem
    eco_badge: "INSTITUTIONAL ACCREDITATIONS",
    eco_title: "State & Ecosystem Accreditations",
    eco_desc: "Officially accredited and supported by the Turkish Defense Industry Agency (SSB), Istanbul Chamber of Commerce (İTO), BTM, KOSGEB, and Teknopark Istanbul.",

    // Navbar
    nav_about: "ABOUT US",
    nav_robotaxi: "ROBOTAXI",
    nav_autonomy: "SOLUTIONS",
    nav_threat: "TECHNOLOGY",
    nav_swarm: "SECURITY",
    nav_cert: "ACCREDITATION",
    nav_contact: "CONTACT",

    // Hero Section
    hero_badge: "SOVEREIGN AUTONOMOUS SYSTEMS",
    hero_title_1: "For Driverless Cities & Defense",
    hero_title_2: "Level 4 Sovereign Autonomy",
    hero_desc: "Trustia AI develops high-reliability Level-4 autonomous driving software for urban Robotaxi fleets and GPS-denied tactical Unmanned Ground Vehicles.",
    hero_btn_explore: "EXPLORE SOLUTIONS",
    hero_btn_demo: "REQUEST DEMO",
    hero_sound_mute: "Muted",
    hero_sound_unmute: "Audio On",

    // Gallery
    gallery_badge: "FIELD & PLATFORM CATALOG",
    gallery_title: "Field Operations & Platform Integrations",
    gallery_desc: "Autonomous software core running seamlessly across diverse vehicle and robot configurations",
    gallery_p1_title: "01 // FIELD OPERATIONS",
    gallery_p1_badge: "BARKAN UGV",
    gallery_p2_title: "02 // SENSOR FUSION",
    gallery_p2_badge: "ALPAR UGV",
    gallery_p3_title: "03 // OBSTACLE AVOIDANCE",
    gallery_p3_badge: "HYBRID PATH",
    gallery_p4_title: "04 // PERCEPTION AI",
    gallery_p4_badge: "KAPGAN 8x8",
    gallery_p5_title: "05 // SWARM INTEL",
    gallery_p5_badge: "ENGA 6x6",

    // About Page
    about_back: "← BACK TO HOME",
    about_badge: "CORPORATE OVERVIEW & VISION",
    about_title: "Trustia AI — Sovereign Autonomy Core",
    about_desc: "Trustia AI (Istanbul, Turkey) is a next-generation deep tech startup engineering Level-4 sovereign autonomy software for urban commercial Robotaxi fleets and GPS-denied defense robotics.",
    about_c1_title: "Complete Algorithmic Sovereignty",
    about_c1_desc: "100% original proprietary codebase eliminating foreign black-box dependencies and supply chain risks.",
    about_c2_title: "1,301 Verified Automated Tests",
    about_c2_desc: "16,000+ lines of deterministic autonomy architecture verified with 100% pass rate across 1,301 rigorous unit and simulation tests.",
    about_c3_title: "Universal Hardware-Agnostic Core",
    about_c3_desc: "Standard CAN-Bus and ROS 2 compliance enables seamless integration across passenger cars, commercial vans, and defense platforms.",
    about_founder_badge: "FOUNDER & SYSTEMS ARCHITECT",
    about_founder_title: "Murat Furkan Bayram",
    about_founder_role: "Founder & Systems Architect",
    about_founder_bio: "KOSGEB Advanced Entrepreneur and Turkish Defense Industry Agency 100/100 certified autonomy engineer. Developed GPS-denied 3D SLAM, swarm intelligence, and Level 4 sovereign autonomy architectures.",

    // Contact
    contact_page_badge: "OFFICIAL CHANNELS",
    contact_page_title: "Corporate Contact & Partnerships",
    contact_page_desc: "Get in touch directly with our engineering and executive team for Robotaxi fleet integration, defense licensing, and investment inquiries.",

    // Footer
    footer_tagline: "Level-4 sovereign autonomy software platform engineered for urban Robotaxi fleets and demanding defense theaters.",
    footer_made_in: "Engineered in Istanbul, Turkey.",
    footer_locations: "İTO BTM Fulya & Teknopark Istanbul",
    footer_col_platform: "SOLUTIONS",
    footer_link_arch: "Autonomy Core",
    footer_link_engine: "Robotaxi Fleet",
    footer_link_perception: "3D SLAM Mapping",
    footer_link_ros: "Swarm Consensus",
    footer_link_api: "API & Integration",
    footer_col_cert: "ACCREDITATION",
    footer_cert_indigenous: "100% Sovereign",
    footer_cert_crypto: "Defense Industry Agency",
    footer_cert_as9100: "İTO BTM Incubation",
    footer_cert_iso: "Teknopark Istanbul",
    footer_cert_ros: "KOSGEB Grant",
    footer_col_corporate: "CORPORATE",
    footer_link_about: "About Us",
    footer_link_career: "Careers",
    footer_badge_join: "JOIN US",
    footer_link_contact: "Contact",
    footer_link_press: "Press Kit",
    footer_rights: "All rights reserved.",
    footer_entity: "Trustia AI"
  }
};

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [lang, setLangState] = useState<Language>("tr");

  useEffect(() => {
    const saved = localStorage.getItem("trustia_lang") as Language;
    if (saved && (saved === "tr" || saved === "en")) {
      setLangState(saved);
    }
  }, []);

  const setLang = (newLang: Language) => {
    setLangState(newLang);
    localStorage.setItem("trustia_lang", newLang);
  };

  const toggleLang = () => {
    const next = lang === "tr" ? "en" : "tr";
    setLang(next);
  };

  const t = (key: string): string => {
    return translations[lang][key] || translations["tr"][key] || key;
  };

  return (
    <LanguageContext.Provider value={{ lang, setLang, toggleLang, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error("useLanguage must be used within a LanguageProvider");
  }
  return context;
}
