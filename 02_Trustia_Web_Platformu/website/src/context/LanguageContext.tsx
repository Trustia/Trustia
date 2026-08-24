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

    // Hero Section
    hero_badge: "%100 YERLİ KATKI SERTİFİKASYON UYUMLU",
    hero_title_1: "Zorlu Operasyon Sahalarında",
    hero_title_2: "Tam Otonom Milli İrade",
    hero_desc: "GPS sinyalinin bulunmadığı veya engellendiği harekat alanlarında İnsansız Kara Araçları (İKA) için geliştirilmiş sıfır dış bağımlılıklı askeri otonomi platformu.",
    hero_btn_explore: "SİSTEMİ İNCELE",
    hero_btn_demo: "DEMO TALEP ET",
    hero_sound_mute: "Sessiz",
    hero_sound_unmute: "Sesi Aç",

    // Gallery Showcase
    gallery_badge: "SAHA OPERASYON FOTO GALERİSİ",
    gallery_title: "Saha Testleri ve İKA Entegrasyon Kataloğu",
    gallery_desc: "Farklı şasi ve sensör konfigürasyonlarında çalışan otonom yazılım beyni görselleri",
    gallery_p1_title: "01 // SAHA ARAZİ TESTİ",
    gallery_p1_badge: "BARKAN İKA",
    gallery_p2_title: "02 // SENSÖR FÜZYONU",
    gallery_p2_badge: "ALPAR İKA",
    gallery_p3_title: "03 // ENGEL KAÇINMA",
    gallery_p3_badge: "HYBRID A*",
    gallery_p4_title: "04 // TEHDİT FÜZYONU",
    gallery_p4_badge: "KAPGAN 8x8",
    gallery_p5_title: "05 // SÜRÜ FORMASYONU",
    gallery_p5_badge: "ENGA 6x6",
    gallery_card1_badge: "CAN FD & ROS 2 TELEMETRİ",
    gallery_card1_title: "Donanım Sürücü Köprüsü",
    gallery_card1_desc: "Araç aktüatörleri ve motor sürücüleri ile 1ms altında kesintisiz veri alışverişi.",
    gallery_card1_status: "DURUM: AKTİF",
    gallery_card2_badge: "HMAC-SHA256 ŞİFRELEME",
    gallery_card2_title: "Telsiz & LinkLoss Güvenliği",
    gallery_card2_desc: "Sinyal kesintisinde otonom eve dönüş (RTH) ve şifreli komut doğrulama.",

    // Supported Platforms & Vehicles
    platforms_badge: "DONANIM-BAĞIMSIZ MİMARİ // HARDWARE-AGNOSTIC",
    platforms_title: "Hangi Araç ve Platformlarda Çalışır?",
    platforms_desc: "Trustia, belirli bir üreticiye bağımlı olmayan evrensel bir otonomi beynidir. Standart SAE J1939 CAN-Bus, CAN FD, ROS 2 ve Drive-by-Wire (DbW) haberleşme protokolleri sayesinde mekanik veya elektronik aktüatör bağlantısına sahip her türlü tekerlekli ve paletli platformda çalışır.",
    
    plat_cat1_badge: "SİVİL MOBİLİTE & ROBOTAKSİ",
    plat_cat1_title: "Binek, Ticari & Elektrikli Otomobiller",
    plat_cat1_desc: "Elektronik direksiyon (EPS), gaz ve fren (Drive-by-Wire) altyapısına sahip modern şasilerde doğrudan CAN hattı üzerinden tak-çalıştır otonomi.",
    plat_cat1_list: "TOGG T10X/T10F, Mercedes G-Serisi / Sprinter, Toyota Corolla/RAV4, Lexus RX, BMW 3/5 Serisi, Ford Transit, Hyundai Ioniq, Tesla EV, Polaris GEM",

    plat_cat2_badge: "SAVUNMA & ASKERİ İKA",
    plat_cat2_title: "Taktik İnsansız Kara Araçları (UGV)",
    plat_cat2_desc: "NATO STANAG 4586 ve SAE AS6091 (JAUS) standartlarında, elektronik harp ve GPS'siz muharebe sahalarında görev yapan hafif, orta ve ağır sınıf askeri robotlar.",
    plat_cat2_list: "HAVELSAN BARKAN & BARKAN 2, ASELSAN/FNSS ALPAR, HAVELSAN KAPGAN 8x8, BMC Vuran/Kirpi (Otonom Konvoy), Otokar Enga/Cobra II, Clearpath Husky/Warthog",

    plat_cat3_badge: "AĞIR HİZMET & ENDÜSTRİ",
    plat_cat3_title: "Otonom Tarım, Maden & Şantiye",
    plat_cat3_desc: "Zorlu şantiye ve tarım arazilerinde insan hayatını riske atmadan 7/24 kesintisiz otonom lojistik, hafriyat ve hassas tarım sürüşü.",
    plat_cat3_list: "John Deere, New Holland, TÜMOSAN Otonom Traktörler, CAT & Komatsu Maden Kamyonları ve Ağır İş Makineleri",

    plat_how_title: "Gerçek Dünyada Araca Nasıl Entegre Edilir?",
    plat_how_subtitle: "Endüstriyel Standartlarda 2 Farklı Entegrasyon Metodolojisi",
    plat_how_opt1_badge: "YÖNTEM 1 // ELEKTRONİK (DRIVE-BY-WIRE)",
    plat_how_opt1_title: "Yeni Nesil Elektronik Kontrollü Araçlar",
    plat_how_opt1_desc: "Direksiyonu ve freni kablolu (Drive-by-Wire / EPS) olan tüm yeni nesil araçlarda mekanik hiçbir parça takılmaz. Trustia bilgisayarından çıkan Kvaser/PEAK CAN kablosu aracın OBD-II veya CAN Gateway portuna takılır; yazılım dijital komutlarla aracı anında sürer.",
    plat_how_opt2_badge: "YÖNTEM 2 // MEKANİK VE KLASİK ARAÇLAR",
    plat_how_opt2_title: "Mekanik Direksiyon & Klasik Zırhlı Şasiler",
    plat_how_opt2_desc: "Elektronik direksiyonu olmayan klasik zırhlı araç, kamyon veya traktörlerde direksiyon miline 1 adet kompakt elektrikli servo motor, gaz/fren pedalına ise 1'er adet lineer aktüatör vidalanır. Trustia bu motorları CAN üzerinden yönetir.",

    // Hardware BOM & Master Specifications
    bom_badge: "DONANIM VE TEDARİK ŞARTNAMESİ // HARDWARE BOM SPECIFICATION",
    bom_title: "Fiziksel Entegrasyon İçin Master Donanım Listesi",
    bom_desc: "Trustia otonomi yazılımının gerçek dünyada fiziksel bir araca takılıp sahada çalıştırılması için gereken onaylı, endüstriyel ve askeri sınıf donanım bileşenleri matrisi.",
    bom_tab_all: "TÜM DONANIMLAR (15 BİLEŞEN)",
    bom_tab_compute: "🧠 BİLGİSAYAR & GÜÇ",
    bom_tab_sensors: "👁️ SENSÖRLER & LİDAR",
    bom_tab_drive: "🔌 SÜRÜŞ & CAN-BUS",
    bom_tab_defense: "🎖️ ASKERİ & MAYIN KİTİ",
    bom_tab_actuators: "🚜 MEKANİK AKTÜATÖR",
    bom_col_component: "BİLEŞEN & DONANIM",
    bom_col_model: "ONAYLI MODEL",
    bom_col_function: "TEKNİK FONKSİYON & ENTEGRASYON",
    bom_col_standard: "STANDART / SERTİFİKA",
    bom_col_cost: "TEDARİK & DURUM",
    bom_turnkey_title: "Endüstriyel Entegrasyon Paketleri",
    bom_turnkey_subtitle: "Seviye 4 Otonom Sürüş & Askeri İKA Entegrasyon Mimarisi",
    bom_turnkey_1_title: "Sivil Robotaksi Kiti",
    bom_turnkey_1_desc: "Binek, ticari ve elektrikli modern araçlar (TOGG, Mercedes, Toyota vb.).",
    bom_turnkey_2_title: "Askeri Taktik İKA Kiti",
    bom_turnkey_2_desc: "Zırhlı muharebe araçları, termal gece görüşü, mayın ve EYP tespit donanımları.",
    bom_turnkey_3_title: "Mekanik & Traktör Kiti",
    bom_turnkey_3_desc: "Elektronik direksiyonu olmayan klasik araçlar, şantiye kamyonları ve traktörler.",

    // Tech Matrix Showcase
    matrix_badge: "MİLLİ OTONOMİ MİMARİSİ VE TEKNİK KAPASİTE MATRIXI",
    matrix_title: "Tüm Askeri Alt Sistem & Algoritma Katmanları",
    matrix_desc: "GPS sinyalinin olmadığı harekat ortamlarında sıfır dış bağımlılıkla çalışan 6 ana teknoloji katmanı ve 1,200+ saatlik saha doğrulama metrikleri.",
    tab_all: "TÜM SİSTEMLER (6 KATMAN)",
    tab_otonomi: "OTONOMİ & SLAM",
    tab_tehdit: "TEHDİT FÜZYONU",
    tab_suru: "SÜRÜ ZEKASI",
    tab_siber: "SİBER KORUMA",
    tab_test: "SAHA & RTOS",

    // Tech Cards
    card_1_badge: "KONUMLANMA & NAVİGASYON",
    card_1_title: "GPS'siz 3D SLAM & Görsel Odometri",
    card_1_desc: "LiDAR, Stereoskopik Kameralar ve IMU sensör füzyonu ile GPS uydularının engellendiği harekat sahalarında santimetre hassasiyetinde 3D haritalama ve poz tahmini.",
    card_1_metric: "99.94%",
    card_1_label: "Konum Doğruluğu",

    card_2_badge: "ROTA PLANLAMA",
    card_2_title: "Kinematik Hybrid A* & RRT* Rota Algoritması",
    card_2_desc: "Araç fiziki dönüş yarıçapı, arazi eğimi ve engebeyi dikkate alan dinamik kinematik rota planlama ve canlı engel engelleme mekanizması.",
    card_2_metric: "<15ms",
    card_2_label: "Yeniden Hesaplama",

    card_3_badge: "SAHA TEHDİT FÜZYONU",
    card_3_title: "EYP, Mayın & KHKN Gaz Tespiti",
    card_3_desc: "GPR radar, metal indüksiyonu ve termal anomali verileriyle patlayıcı tuzak algılama ve Rüzgar Altı Gaz Yayılım (Plume) modellemesiyle 30m emniyet çemberi.",
    card_3_metric: "30m",
    card_3_label: "Tehdit Çemberi",

    card_4_badge: "ÇOKLU KOORDİNASYON",
    card_4_title: "Hava-Kara Hibrit Sürü Zekası",
    card_4_desc: "İHA keşif verileri ile İKA harekatını senkronize eden, Kama, Saf, Kolon ve Baklava formasyonlarında taktik çoklu araç koordinasyon algoritması.",
    card_4_metric: "16 İKA",
    card_4_label: "Eşzamanlı Sürü",

    card_5_badge: "KORUMA & FAIL-SAFE",
    card_5_title: "HMAC-SHA256 Kripto & Anti-Spoofing RTH",
    card_5_desc: "Şifrelenmiş komut paketi doğrulaması, Anti-GPS Spoofing/Jamming kalkanı ve telsiz kesintilerinde 3D SLAM geçmiş rotasıyla otonom eve dönüş (RTH) emniyeti.",
    card_5_metric: "3sn",
    card_5_label: "Fail-Safe Tetikleme",

    card_6_badge: "MİMARİ VE SAHA TESTLERİ",
    card_6_title: "ROS 2 Humble, SocketCAN & 400Hz ESKF",
    card_6_desc: "Yerli C++20 ve saf Python çekirdeği üzerinde mikro-saniye gecikmeli RTOS gerçek zamanlı çalıştırıcı, 400Hz ESKF sensör füzyonu ve 1.281 otomatik test ile doğrulanmış saha metrikleri.",
    card_6_metric: "1,281 Test",
    card_6_label: "Otomasyon & HIL",

    // Executive Demo Modal
    demo_nda_badge: "NDA KORUMALI",
    demo_header_title: "Kurumsal Platform Erişimi & Çift Yönlü Dosya Paylaşımı",
    demo_success_title: "Talebiniz Kaydedildi ve Dosyanız Alındı",
    demo_success_desc: "Kurumsal güvenlik protokolü gereğince, temsilcimiz 24 saat içinde tarafınızla iletişime geçerek Gizlilik Anlaşmasını (NDA) başlatacaktır.",
    demo_download_title: "DOKÜMAN İNDİRME MERKEZİ",
    demo_download_desc: "Sözleşme öncesi incelemeniz için hazırlanan Otonomi Yazılım Mimarisi SDK Özet Şartnamesini hemen indirebilirsiniz.",
    demo_download_btn: "SDK & ŞARTNAME DOKÜMANINI GÖRÜNTÜLE (PDF/WEB)",
    demo_btn_close: "Pencereyi Kapat",
    demo_label_institution: "KURUM / FİRMA ADI *",
    demo_ph_institution: "Örn: ASELSAN, ROKETSAN, FNSS veya SSB",
    demo_label_title: "ÜNVAN / GÖREV *",
    demo_ph_title: "Örn: Otonomi Proje Yöneticisi / Başmühendis",
    demo_label_email: "KURUMSAL E-POSTA ADRESİ *",
    demo_ph_email: "ad.soyad@kurum.com.tr",
    demo_label_scope: "TALEP KAPSAMI VE SİSTEM TERCİHİ",
    demo_label_upload: "KURUMSAL GEREKSİNİM VEYA TEKNİK ŞARTNAME DOSYASI (OPSİYONEL)",
    demo_upload_drag: "Teknik şartname veya gereksinim dokümanınızı buraya sürükleyin",
    demo_upload_hint: "PDF, DOCX veya ZIP formatında teknik şartname (Maks. 25MB)",
    demo_btn_submit: "GÜVENLİ DEMO & ENTEGRASYON TALEBİ GÖNDER",
    demo_submitting: "Güvenli Protokol ile İletiliyor...",
    demo_footer_note: "Verileriniz 256-bit TLS şifreleme ile korunmakta olup yalnızca savunma sanayii yetkilileri ile paylaşılır.",

    // Corporate Contact Form
    contact_success_title: "Talebiniz Başarıyla İletildi",
    contact_success_desc: "Talebiniz adresine iletilmiştir. Mühendislik ve ilgili departman ekibimiz 24 saat içerisinde sizinle iletişime geçecektir.",
    contact_code: "BİLDİRİM KODU: #TR-2026-8486",
    contact_btn_new: "Yeni Talep Oluştur",
    contact_label_dept: "HEDEF DEPARTMAN VE E-POSTA *",
    contact_label_name: "AD SOYAD / YETKİLİ *",
    contact_ph_name: "Örn: Ahmet Yılmaz",
    contact_label_company: "KURUM / FİRMA (OPSİYONEL)",
    contact_ph_company: "Örn: Savunma Sanayii Başkanlığı / ASELSAN / Üniversite",
    contact_label_email: "E-POSTA ADRESİNİZ *",
    contact_ph_email: "iletisim@kurum.com.tr",
    contact_label_subject: "TALEP KONUSU *",
    contact_label_message: "TEKNİK DETAYLAR VE MESAJINIZ *",
    contact_label_msg: "TEKNİK DETAYLAR VE MESAJINIZ *",
    contact_ph_message: "İKA platformunuz, entegrasyon takviminiz, donanım gereksinimleriniz veya sormak istediğiniz tüm teknik detayları belirtiniz...",
    contact_btn_submit: "RESMİ TALEBİ İLET",
    contact_btn_send: "RESMİ TALEBİ İLET",
    contact_submitting: "İletiliyor...",
    contact_btn_sending: "İletiliyor...",
    contact_direct_note: "Bu form üzerinden gönderilen mesajlar doğrudan kurumsal e-posta gelen kutusuna anında düşer.",
    contact_footer_note: "Bu form üzerinden gönderilen mesajlar doğrudan kurumsal e-posta gelen kutusuna anında düşer.",

    // Contact Page
    contact_back: "← ANA SAYFAYA DÖN",
    contact_page_badge: "RESMİ İLETİŞİM KANALLARI",
    contact_page_title: "Kurumsal İletişim & Entegrasyon",
    contact_page_desc: "İnsansız Kara Aracı (İKA) otonomi yazılımı lisanslama, donanım entegrasyonu ve saha demo talepleriniz için doğrudan teknik ekibimizle iletişime geçin.",
    contact_gen_badge: "GENEL İLETİŞİM",
    contact_gen_note: "Cloudflare kurumsal e-posta altyapısı ile tüm iletiler doğrudan nöbetçi mühendislik ekibimize ulaşır.",
    contact_dept_title: "DEPARTMAN E-POSTA ADRESLERİ",
    contact_dept_tech: "Teknik Entegrasyon:",
    contact_dept_hr: "Kariyer & İK:",
    contact_dept_legal: "Hukuk & Lisanslama:",
    contact_dept_invest: "Yatırımcı İlişkileri:",
    contact_loc_title: "OPERASYON VE AR-GE MERKEZİ",
    contact_loc_hq: "Trustia Autonomous Systems Inc. — Delaware, ABD & İstanbul, Türkiye",
    contact_hours_title: "YANIT SÜRESİ",
    contact_hours_desc: "Hafta içi 08:30 - 18:30 (Resmi taleplere 24 saat içinde yanıt verilir).",

    // About Page
    about_back: "← ANA SAYFAYA DÖN",
    about_badge: "KURUMSAL PROFİL & ASKERİ VİZYON",
    about_title: "Trustia Autonomous Systems Inc. — Milli Otonomi Çekirdeği",
    about_desc: "Trustia Autonomous Systems Inc. (Delaware, ABD & İstanbul, Türkiye), GPS sinyalinin bulunmadığı veya elektronik harp ile karartıldığı zorlu muharebe sahalarında İnsansız Kara Araçları (İKA) için 3D SLAM, kinematik Hybrid A* rota planlama, EYP/Mayın füzyonu ve hava-kara hibrit sürü zekası geliştiren yeni nesil savunma teknolojileri kuruluşudur.",
    about_c1_title: "Algoritmik Tam Bağımsızlık",
    about_c1_desc: "Yabancı kapalı kutu (black-box) yazılımlara bağımlılığı sıfıra indiren %100 özgün C++20 kaynak kod mülkiyeti ile ambargo risklerini ortadan kaldıran milli yazılım beyni.",
    about_c2_title: "1.281 Otomatik Test & HIL Doğrulama",
    about_c2_desc: "1.281 birim, entegrasyon ve matematiksel simülasyon testi %100 başarıyla tamamlanmış; donanım seviyesi döngü (HIL), Linux SocketCAN ve 1.200 saatin üzerinde kesintisiz saha iklim testleriyle onaylanmıştır.",
    about_c3_title: "NATO STANAG 4586 Seviye 4 & Çift Şirket Mimarisi",
    about_c3_desc: "Delaware C-Corp tüzel kişiliğiyle global yatırım ve NATO müttefik veri bağını sağlarken; İstanbul Ar-Ge merkeziyle Türk savunma sanayiine yerli ve milli çözümler sunar.",
    about_founder_badge: "KURUCU & MÜHENDİSLİK LİDERLİĞİ",
    about_founder_title: "Murat Furkan Bayram",
    about_founder_role: "Kurucu & Otonomi Sistemleri Başmühendisi",
    about_founder_bio: "KOSGEB İleri Girişimci ve BTK / SSB Savunma Sanayii Akademi sertifikalı otonomi mühendisi. GPS'siz sahalarda 3D Pose Graph SLAM, çoklu ajan sürü zekası ve askeri yapay zeka alanında milli otonomi çekirdeğini geliştirmiş; şirketin Delaware C-Corp ve Türkiye yapılanmasını yönetmektedir.",
    about_arch_title: "Modüler Tak-Çalıştır Savunma Mimarisi",
    about_arch_desc: "Trustia Core, her türlü tekerlekli veya paletli İKA platformuna CAN-Bus ve ROS 2 üzerinden 10 dakikada entegre olabilen tak-çalıştır Donanım Soyutlama Katmanına (HAL) ve SAE AS6091 JAUS protokol köprüsüne sahiptir.",

    // Footer
    footer_tagline: "GPS'in bulunmadığı veya engellendiği zorlu harekat alanlarında İnsansız Kara Araçları (İKA) için geliştirilmiş %100 yerli askeri otonom sürüş ve algılama yazılım platformu.",
    footer_made_in: "Türkiye ve ABD'de geliştirildi.",
    footer_locations: "Delaware, ABD & İstanbul, Türkiye",
    footer_col_platform: "PLATFORM",
    footer_link_arch: "Yazılım Mimarisi",
    footer_link_engine: "Otonomi Motoru",
    footer_link_perception: "Algılama Sistemi",
    footer_link_ros: "ROS 2 & CAN-Bus",
    footer_link_api: "API Dokümantasyonu",
    footer_col_cert: "SERTİFİKASYON",
    footer_cert_indigenous: "%100 Yerli Katkı",
    footer_cert_crypto: "HMAC-SHA256",
    footer_cert_as9100: "SAE AS9100",
    footer_cert_iso: "ISO 27001",
    footer_cert_ros: "ROS2 Uyumlu",
    footer_col_corporate: "KURUMSAL",
    footer_link_about: "Hakkımızda",
    footer_link_career: "Kariyer",
    footer_badge_join: "BİZE KATILIN",
    footer_link_contact: "İletişim",
    footer_link_press: "Basın",
    footer_rights: "Tüm hakları saklıdır.",
    footer_entity: "Trustia Autonomous Systems Inc. (Delaware, USA) & Trustia Teknoloji (Türkiye)"
  },
  en: {
    // Navbar
    nav_about: "ABOUT US",
    nav_autonomy: "AUTONOMY",
    nav_threat: "THREAT DETECTION",
    nav_swarm: "SWARM INTEL",
    nav_cert: "CERTIFICATION",
    nav_contact: "CONTACT",

    // Hero Section
    hero_badge: "100% INDIGENOUS & CERTIFIED DEFENSE PLATFORM",
    hero_title_1: "In GPS-Denied Operating Theatres",
    hero_title_2: "Fully Autonomous Defense Autonomy",
    hero_desc: "Zero-external-dependency military autonomy platform developed for Unmanned Ground Vehicles (UGVs) operating in jammed and GPS-denied combat environments.",
    hero_btn_explore: "EXPLORE PLATFORM",
    hero_btn_demo: "REQUEST DEMO",
    hero_sound_mute: "Mute",
    hero_sound_unmute: "Unmute",

    // Gallery Showcase
    gallery_badge: "FIELD OPERATIONS PHOTO GALLERY",
    gallery_title: "Field Tests and UGV Integration Catalog",
    gallery_desc: "Visual records of the autonomous software core running on diverse chassis and sensor configurations",
    gallery_p1_title: "01 // FIELD TERRAIN TEST",
    gallery_p1_badge: "BARKAN UGV",
    gallery_p2_title: "02 // SENSOR FUSION",
    gallery_p2_badge: "ALPAR UGV",
    gallery_p3_title: "03 // OBSTACLE AVOIDANCE",
    gallery_p3_badge: "HYBRID A*",
    gallery_p4_title: "04 // THREAT FUSION",
    gallery_p4_badge: "KAPGAN 8x8",
    gallery_p5_title: "05 // SWARM FORMATION",
    gallery_p5_badge: "ENGA 6x6",
    gallery_card1_badge: "CAN FD & ROS 2 TELEMETRY",
    gallery_card1_title: "Hardware Driver Bridge",
    gallery_card1_desc: "Sub-1ms seamless deterministic communication with vehicle actuators and motor drivers.",
    gallery_card1_status: "STATUS: ACTIVE",
    gallery_card2_badge: "HMAC-SHA256 ENCRYPTION",
    gallery_card2_title: "Data Link & LinkLoss Security",
    gallery_card2_desc: "Automated Return-To-Home (RTH) upon signal loss and encrypted command validation.",

    // Supported Platforms & Vehicles
    platforms_badge: "HARDWARE-AGNOSTIC ARCHITECTURE",
    platforms_title: "Which Vehicles and Platforms Does It Support?",
    platforms_desc: "Trustia is a hardware-agnostic autonomous operating stack with zero proprietary vendor lock-in. Powered by standard SAE J1939 CAN-Bus, CAN FD, ROS 2, and Drive-by-Wire (DbW) protocols, it integrates into any wheeled or tracked chassis equipped with mechanical or electronic actuators.",

    plat_cat1_badge: "CIVILIAN MOBILITY & ROBOTAXI",
    plat_cat1_title: "Passenger, Commercial & Electric Vehicles",
    plat_cat1_desc: "Plug-and-play autonomy over standard CAN-Bus on modern chassis featuring electronic power steering (EPS), throttle, and brake-by-wire.",
    plat_cat1_list: "TOGG T10X/T10F, Mercedes G-Class / Sprinter, Toyota Corolla/RAV4, Lexus RX, BMW 3/5 Series, Ford Transit, Hyundai Ioniq, Tesla EV, Polaris GEM",

    plat_cat2_badge: "DEFENSE & TACTICAL UGV",
    plat_cat2_title: "Tactical Unmanned Ground Vehicles (UGV)",
    plat_cat2_desc: "NATO STANAG 4586 and SAE AS6091 (JAUS) compliant integration across light, medium, and heavy tracked/wheeled military robotics operating in GPS-denied warfare.",
    plat_cat2_list: "HAVELSAN BARKAN & BARKAN 2, ASELSAN/FNSS ALPAR, HAVELSAN KAPGAN 8x8, BMC Vuran/Kirpi (Convoy DbW), Otokar Enga/Cobra II, Clearpath Husky/Warthog",

    plat_cat3_badge: "HEAVY DUTY & INDUSTRY",
    plat_cat3_title: "Autonomous Agriculture, Mining & Logistics",
    plat_cat3_desc: "24/7 continuous autonomous material hauling, excavation, and precision agriculture without exposing human operators to hazardous sites.",
    plat_cat3_list: "John Deere, New Holland, TÜMOSAN Autonomous Tractors, CAT & Komatsu Mining Trucks and Heavy Machinery",

    plat_how_title: "How Is It Integrated into Physical Vehicles?",
    plat_how_subtitle: "Two Production Integration Methodologies",
    plat_how_opt1_badge: "METHOD 1 // DIGITAL (DRIVE-BY-WIRE)",
    plat_how_opt1_title: "Modern Electronic-Controlled Vehicles",
    plat_how_opt1_desc: "No mechanical hardware is required on vehicles equipped with Drive-by-Wire (EPS/electronic throttle). The CAN-Bus cable from the Trustia edge computer connects directly to the OBD-II or CAN Gateway port, controlling actuation through native digital messages.",
    plat_how_opt2_badge: "METHOD 2 // MECHANICAL & LEGACY CHASSIS",
    plat_how_opt2_title: "Mechanical Steering & Legacy Armored Platforms",
    plat_how_opt2_desc: "For mechanical steering or heavy-duty legacy vehicles, a compact industrial servo motor is fitted to the steering column, and linear actuators are mounted to the pedals. Trustia commands these actuators directly via CAN-Bus.",

    // Hardware BOM & Master Specifications
    bom_badge: "HARDWARE PROCUREMENT SPECIFICATION // BILL OF MATERIALS",
    bom_title: "Master Hardware Bill of Materials for Physical Integration",
    bom_desc: "Validated industrial and military-grade hardware matrix required to flash and operate the Trustia autonomy stack on physical vehicles in real-world environments.",
    bom_tab_all: "ALL HARDWARE (15 COMPONENTS)",
    bom_tab_compute: "🧠 COMPUTE & POWER",
    bom_tab_sensors: "👁️ SENSORS & LIDAR",
    bom_tab_drive: "🔌 DRIVE & CAN-BUS",
    bom_tab_defense: "🎖️ DEFENSE & MINE KIT",
    bom_tab_actuators: "🚜 MECHANICAL ACTUATORS",
    bom_col_component: "COMPONENT / HARDWARE",
    bom_col_model: "QUALIFIED MODEL",
    bom_col_function: "TECHNICAL FUNCTION & INTEGRATION",
    bom_col_standard: "STANDARD / RATING",
    bom_col_cost: "PROCUREMENT & STATUS",
    bom_turnkey_title: "Industrial Integration Packages",
    bom_turnkey_subtitle: "Level 4 Autonomous Driving & Military UGV Architecture",
    bom_turnkey_1_title: "Civilian Robotaxi Kit",
    bom_turnkey_1_desc: "Modern passenger, commercial, and EV platforms (TOGG, Mercedes, Toyota, etc.).",
    bom_turnkey_2_title: "Military Tactical UGV Kit",
    bom_turnkey_2_desc: "Armored combat vehicles with FLIR thermal night vision, mine & IED detection payloads.",
    bom_turnkey_3_title: "Mechanical & Tractor Kit",
    bom_turnkey_3_desc: "Legacy mechanical steering platforms, heavy mining trucks, and autonomous tractors.",

    // Tech Matrix Showcase
    matrix_badge: "NATIONAL AUTONOMY ARCHITECTURE & TECHNICAL CAPACITY MATRIX",
    matrix_title: "Complete Military Subsystems & Algorithm Stack",
    matrix_desc: "6 core technology layers operating with zero external dependency in GPS-denied operational theatres, validated across 1,200+ field hours.",
    tab_all: "ALL SYSTEMS (6 LAYERS)",
    tab_otonomi: "AUTONOMY & SLAM",
    tab_tehdit: "THREAT FUSION",
    tab_suru: "SWARM INTEL",
    tab_siber: "CYBER DEFENSE",
    tab_test: "FIELD & RTOS",

    // Tech Cards
    card_1_badge: "POSITIONING & NAVIGATION",
    card_1_title: "GPS-Denied 3D SLAM & Visual Odometry",
    card_1_desc: "Centimeter-accurate 3D mapping and pose estimation via LiDAR, Stereoscopic Cameras, and IMU sensor fusion under active satellite jamming.",
    card_1_metric: "99.94%",
    card_1_label: "Position Accuracy",

    card_2_badge: "TRAJECTORY PLANNING",
    card_2_title: "Kinematic Hybrid A* & RRT* Pathfinding",
    card_2_desc: "Dynamic kinematic route planning and real-time obstacle avoidance respecting turning radius, vehicle inertia, and terrain gradients.",
    card_2_metric: "<15ms",
    card_2_label: "Re-computation",

    card_3_badge: "BATTLEFIELD THREAT FUSION",
    card_3_title: "IED, Mine & CBRN Gas Plume Detection",
    card_3_desc: "Multi-modal explosive trap detection with GPR radar, induction, and thermal anomaly data, projecting automated 30m safety quarantine buffers.",
    card_3_metric: "30m",
    card_3_label: "Threat Buffer",

    card_4_badge: "MULTI-AGENT COORDINATION",
    card_4_title: "Air-Ground Hybrid Swarm Intelligence",
    card_4_desc: "Synchronizing UAV aerial reconnaissance with UGV maneuvers in tactical Wedge, Line, Column, and Diamond multi-robot formations.",
    card_4_metric: "16 UGVs",
    card_4_label: "Concurrent Swarm",

    card_5_badge: "PROTECTION & FAIL-SAFE",
    card_5_title: "HMAC-SHA256 Crypto & Anti-Spoofing RTH",
    card_5_desc: "Cryptographic command validation, Anti-GPS Spoofing / Electronic Warfare defense, and automatic Return-To-Home via recorded 3D SLAM trajectories upon link drop.",
    card_5_metric: "3s",
    card_5_label: "Fail-Safe Trigger",

    card_6_badge: "ARCHITECTURE & FIELD TRIALS",
    card_6_title: "ROS 2 Humble, SocketCAN & 400Hz ESKF",
    card_6_desc: "Native deterministic RTOS loops with 400Hz Error-State Kalman Filter (ESKF) sensor fusion, Linux SocketCAN, and 1,281 automated verification tests.",
    card_6_metric: "1,281 Tests",
    card_6_label: "Automation & HIL",

    // Executive Demo Modal
    demo_nda_badge: "NDA PROTECTED",
    demo_header_title: "Enterprise Platform Access & Secure File Exchange",
    demo_success_title: "Your Request and Document Have Been Received",
    demo_success_desc: "Under defense security protocols, our executive team will contact you within 24 hours to initiate the Non-Disclosure Agreement (NDA).",
    demo_download_title: "DOCUMENT DOWNLOAD CENTER",
    demo_download_desc: "Download the Autonomy Architecture SDK Summary Specification prepared for pre-contract institutional review.",
    demo_download_btn: "VIEW SDK & SPECIFICATION DOCUMENT (PDF/WEB)",
    demo_btn_close: "Close Window",
    demo_label_institution: "INSTITUTION / COMPANY NAME *",
    demo_ph_institution: "e.g. Lockheed Martin, Rheinmetall, ASELSAN, or MoD",
    demo_label_title: "JOB TITLE / ROLE *",
    demo_ph_title: "e.g. Lead Autonomy Engineer / Program Manager",
    demo_label_email: "CORPORATE EMAIL ADDRESS *",
    demo_ph_email: "first.last@company.com",
    demo_label_scope: "REQUEST SCOPE & SYSTEM SELECTION",
    demo_label_upload: "REQUIREMENTS OR TECHNICAL SPECIFICATION FILE (OPTIONAL)",
    demo_upload_drag: "Drag and drop your technical requirements document here",
    demo_upload_hint: "PDF, DOCX or ZIP technical specification (Max 25MB)",
    demo_btn_submit: "SUBMIT SECURE DEMO & INTEGRATION REQUEST",
    demo_submitting: "Transmitting via Secure Protocol...",
    demo_footer_note: "Your data is encrypted with 256-bit TLS and shared exclusively with defense industry representatives.",

    // Corporate Contact Form
    contact_success_title: "Your Request Has Been Transmitted",
    contact_success_desc: "Your request has been routed to our engineering and executive team. We will respond within 24 hours.",
    contact_code: "REFERENCE CODE: #TR-2026-8486",
    contact_btn_new: "Submit Another Request",
    contact_label_dept: "TARGET DEPARTMENT & INBOX *",
    contact_label_name: "FULL NAME / OFFICER *",
    contact_ph_name: "e.g. John Doe",
    contact_label_company: "INSTITUTION / COMPANY (OPTIONAL)",
    contact_ph_company: "e.g. Ministry of Defense / Defense Contractor / University",
    contact_label_email: "YOUR EMAIL ADDRESS *",
    contact_ph_email: "contact@company.com",
    contact_label_subject: "REQUEST SUBJECT *",
    contact_label_message: "TECHNICAL DETAILS & MESSAGE *",
    contact_label_msg: "TECHNICAL DETAILS & MESSAGE *",
    contact_ph_message: "Please state your UGV platform specifications, integration timeline, hardware constraints, or questions...",
    contact_btn_submit: "TRANSMIT OFFICIAL REQUEST",
    contact_btn_send: "TRANSMIT OFFICIAL REQUEST",
    contact_submitting: "Transmitting...",
    contact_btn_sending: "Transmitting...",
    contact_direct_note: "Messages submitted through this portal are instantly routed to our executive engineering inbox.",
    contact_footer_note: "Messages submitted through this portal are instantly routed to our executive engineering inbox.",

    // Contact Page
    contact_back: "← BACK TO HOMEPAGE",
    contact_page_badge: "OFFICIAL COMMUNICATIONS PORTAL",
    contact_page_title: "Corporate Inquiries & Integration",
    contact_page_desc: "Contact our technical team for Unmanned Ground Vehicle (UGV) autonomy software licensing, hardware integration, and field demonstration inquiries.",
    contact_gen_badge: "GENERAL INQUIRIES",
    contact_gen_note: "Powered by enterprise Cloudflare routing, all inquiries reach our on-duty engineering desk directly.",
    contact_dept_title: "DEPARTMENT DIRECTORY",
    contact_dept_tech: "Technical Integration:",
    contact_dept_hr: "Careers & HR:",
    contact_dept_legal: "Legal & Licensing:",
    contact_dept_invest: "Investor Relations:",
    contact_loc_title: "OPERATIONS & R&D CENTERS",
    contact_loc_hq: "Trustia Autonomous Systems Inc. — Delaware, USA & Istanbul, Turkey",
    contact_hours_title: "RESPONSE TIME",
    contact_hours_desc: "Mon - Fri 08:30 - 18:30 (Official inquiries answered within 24 hours).",

    // About Page
    about_back: "← BACK TO HOMEPAGE",
    about_badge: "CORPORATE PROFILE & DEFENSE ARCHITECTURE",
    about_title: "Trustia Autonomous Systems Inc. — Sovereign Autonomy Core",
    about_desc: "Trustia Autonomous Systems Inc. (Delaware, USA & Istanbul, Turkey) is a next-generation defense technology enterprise developing sovereign, military-grade autonomy software for Unmanned Ground Vehicles (UGVs) operating in GPS-denied and electronic warfare contested operational environments.",
    about_c1_title: "Complete Algorithmic Sovereignty",
    about_c1_desc: "100% proprietary C++20 algorithmic ownership with zero black-box foreign dependencies, ensuring total operational immunity against foreign licensing restrictions and embargoes.",
    about_c2_title: "1,281 Automated Tests & HIL Verification",
    about_c2_desc: "1,281 automated unit, integration, and mathematical simulation tests verified with 100% pass rate, backed by Hardware-In-The-Loop (HIL) and over 1,200 continuous all-weather field trial hours.",
    about_c3_title: "STANAG 4586 Level 4 & Dual-Entity Structure",
    about_c3_desc: "Dual-entity structure combining a Delaware C-Corp for global venture capital and NATO interoperability with an Istanbul R&D engineering hub for sovereign defense manufacturing.",
    about_founder_badge: "FOUNDER & LEADERSHIP",
    about_founder_title: "Murat Furkan Bayram",
    about_founder_role: "Founder & Lead Autonomous Systems Engineer",
    about_founder_bio: "KOSGEB Advanced Entrepreneur, BTK and Defense Industry Academy certified autonomous systems engineer. Architected Trustia's sovereign autonomy core specializing in GPS-denied 3D LiDAR SLAM, multi-robot swarm consensus, and defense AI.",
    about_arch_title: "Modular Plug-and-Play Defense Stack",
    about_arch_desc: "Trustia Core features a universal Hardware Abstraction Layer (HAL) and SAE AS6091 (JAUS) protocol bridge, enabling seamless integration into any wheeled or tracked UGV platform via CAN FD and ROS 2 in under 10 minutes.",

    // Footer
    footer_tagline: "100% proprietary military autonomous driving and perception software platform developed for Unmanned Ground Vehicles (UGVs) operating in contested, GPS-denied environments.",
    footer_made_in: "Engineered in Turkey & USA.",
    footer_locations: "Delaware, USA & Istanbul, Turkey",
    footer_col_platform: "PLATFORM",
    footer_link_arch: "Software Architecture",
    footer_link_engine: "Autonomy Core",
    footer_link_perception: "Perception Stack",
    footer_link_ros: "ROS 2 & CAN-Bus",
    footer_link_api: "API Documentation",
    footer_col_cert: "CERTIFICATION",
    footer_cert_indigenous: "100% Proprietary Core",
    footer_cert_crypto: "HMAC-SHA256",
    footer_cert_as9100: "SAE AS9100",
    footer_cert_iso: "ISO 27001",
    footer_cert_ros: "ROS 2 Compliant",
    footer_col_corporate: "CORPORATE",
    footer_link_about: "About Us",
    footer_link_career: "Careers",
    footer_badge_join: "JOIN US",
    footer_link_contact: "Contact",
    footer_link_press: "Press",
    footer_rights: "All rights reserved.",
    footer_entity: "Trustia Autonomous Systems Inc. (Delaware, USA) & Trustia Teknoloji (Turkey)"
  }
};

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

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
    if (translations[lang] && translations[lang][key]) {
      return translations[lang][key];
    }
    if (translations.tr[key]) {
      return translations.tr[key];
    }
    return key;
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
