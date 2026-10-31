import type { Metadata, Viewport } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";

export const viewport: Viewport = {
  themeColor: "#1c1813",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
};

export const metadata: Metadata = {
  metadataBase: new URL("https://trustia.com.tr"),
  title: {
    default: "TRUSTIA AI — Seviye 4 Yerli Robotaksi ve Askeri İKA Otonomi Platformu",
    template: "%s | TRUSTIA AI",
  },
  description:
    "Trustia AI; şehir içi ticari Robotaksi filoları (SAIC Maxus MIFA 7, Hyundai Ioniq 5 E-GMP) ve kritik otonom platformlar için ISO 26262 ASIL-D, IEEE 2846 RSS, UN R155/R156/R157, 3D LiDAR SLAM ve 1.329 + 21 testle (1.350 test %100 yeşil) doğrulanmış Seviye-4 yerli otonomi yazılım platformudur. ASELSAN (#0050569) & STM Tedarikçi Kütüğü, OIN 2.0 (#f1e44576), AB Komisyonu (PIC: 861711529), EIT Urban Mobility (CUS15554), Teknopark İstanbul HASAT 2026 ve İTO BTM tescilli.",
  keywords: [
    "TRUSTIA AI",
    "Trustia",
    "Trustia Teknoloji",
    "Murat Furkan Bayram",
    "otonomi yazılımı",
    "robotaksi",
    "yerli robotaksi",
    "SAIC Maxus MIFA 7 Robotaksi",
    "Hyundai Ioniq 5 Robotaksi",
    "seviye 4 otonom sürüş",
    "insansız kara aracı",
    "İKA otonomi",
    "IEEE 2846 RSS",
    "ISO 21448 SOTIF",
    "UN ECE R155 R156 R157",
    "AB 2022/1426 Otonom Araç Yönetmeliği",
    "Frenet Lattice Planner",
    "Model Predictive Control MPC",
    "Lanelet2 HD Map",
    "IEEE 1588 PTP LiDAR Deskewing",
    "CARLA 0.9.15 Simülasyon Köprüsü",
    "V2X",
    "C-V2X",
    "GPS-denied navigation",
    "3D NDT SLAM",
    "400 Hz ESKF",
    "Hybrid A*",
    "SAE J3016 Seviye 4",
    "ISO 26262 ASIL-D",
    "SAE JAUS AS6091",
    "ROS 2 Humble",
    "CAN FD bridge",
    "ASELSAN Onaylı Tedarikçi #0050569",
    "STM Savunma Teknolojileri Tedarikçi",
    "İTO BTM Fulya",
    "Teknopark İstanbul Cube Incubation",
    "Teknopark İstanbul HASAT 2026",
    "YTÜ Yıldız Teknopark",
    "KOSGEB İleri Girişimci KSB01UGE0115153370",
    "BTK L2zPtN4X1ZJ",
    "Avrupa Komisyonu PIC 861711529",
    "EIT Urban Mobility CUS15554",
    "Open Invention Network OIN #f1e44576",
  ],
  authors: [
    { name: "Murat Furkan Bayram — Trustia AI", url: "https://trustia.com.tr" },
  ],
  creator: "Trustia AI",
  publisher: "Trustia AI",
  alternates: {
    canonical: "https://trustia.com.tr/",
    languages: {
      "tr-TR": "https://trustia.com.tr/",
      "en-US": "https://trustia.com.tr/",
    },
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  openGraph: {
    title: "TRUSTIA AI — Seviye 4 Yerli Robotaksi & Çift Amaçlı Otonomi Platformu",
    description:
      "SAIC Maxus MIFA 7 & Hyundai Ioniq 5 Seviye-4 Robotaksi, 31.400+ Satır Kod, 205 Dosya, 21 Alt Sistem ve 1.350 Doğrulanmış Test (%100 Yeşil). ASELSAN (#0050569), STM, OIN 2.0 (#f1e44576), AB PIC: 861711529, EITUM: CUS15554, Teknopark İstanbul & İTO BTM.",
    url: "https://trustia.com.tr",
    siteName: "TRUSTIA AI",
    locale: "tr_TR",
    alternateLocale: ["en_US"],
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/og-image.jpg?v=2026",
        width: 1200,
        height: 630,
        alt: "TRUSTIA AI — Level 4 Autonomous Robotaxi & Defense Robotics",
        type: "image/jpeg",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "TRUSTIA AI — Level 4 Autonomous Driving & Robotaxi SDK Core",
    description:
      "Sovereign Level-4 autonomy stack (31,400+ LOC, 203 files, 21 subsystems, 1,350 verified tests (100% Green)) for SAIC Maxus MIFA 7 & Hyundai Ioniq 5. ASELSAN (#0050569), STM, OIN 2.0 & EU PIC: 861711529.",
    images: ["https://trustia.com.tr/og-image.jpg?v=2026"],
    creator: "@trustia_ai",
  },
  icons: {
    icon: [
      { url: "/logo.png", sizes: "32x32", type: "image/png" },
      { url: "/icon.png", sizes: "192x192", type: "image/png" },
    ],
    shortcut: "/logo.png",
    apple: "/logo.png",
  },
  category: "Autonomous Systems & Defense Technology",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Schema.org Structured Data (JSON-LD) for Google Search Console, Rich Snippets & Knowledge Graph
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://trustia.com.tr/#organization",
        "name": "Trustia AI",
        "alternateName": ["TRUSTIA AI", "Trustia Teknoloji", "Trustia Autonomous Systems"],
        "url": "https://trustia.com.tr",
        "logo": "https://trustia.com.tr/logo.png",
        "image": "https://trustia.com.tr/og-image.jpg",
        "description": "Milli Çift Amaçlı Seviye 4 Otonom Sürüş, Ticari Robotaksi SDK, V2X Akıllı Şehir ve İnsansız Kara Aracı (İKA) Otonomi Yazılım Platformu.",
        "founder": {
          "@type": "Person",
          "name": "Murat Furkan Bayram",
          "jobTitle": "Kurucu, Tek Pay Sahibi & Sistem Mimarı",
          "nationality": "TR",
          "sameAs": "https://www.linkedin.com/in/trustia"
        },
        "foundingLocation": {
          "@type": "Place",
          "name": "İstanbul, Türkiye"
        },
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Fulya Mah. Yeşilçimen Sok. İTO BTM Kampüsü, Şişli / İstanbul",
          "addressLocality": "Şişli",
          "addressRegion": "İstanbul",
          "postalCode": "34394",
          "addressCountry": "TR"
        },
        "contactPoint": {
          "@type": "ContactPoint",
          "email": "kariyer@trustia.com.tr",
          "telephone": "+90-537-064-0460",
          "contactType": "Corporate Inquiries & Partnerships",
          "availableLanguage": ["Turkish", "English"]
        },
        "sameAs": [
          "https://github.com/Trustia/Trustia",
          "https://trustia.com.tr",
          "https://www.linkedin.com/in/trustia"
        ],
        "identifier": [
          {
            "@type": "PropertyValue",
            "name": "Open Invention Network (OIN 2.0) Executed License Document ID",
            "value": "f1e445769a9934114db095c4f5430a0e749d8201"
          },
          {
            "@type": "PropertyValue",
            "name": "ASELSAN Approved Supplier Registry ID & SAP Code",
            "value": "0050569 / FZQHEXGFMTJU / 0050569CCE941FD1A49FCEFB9B7BE7D6"
          },
          {
            "@type": "PropertyValue",
            "name": "STM Savunma Teknolojileri Defense Supplier Registry",
            "value": "REGISTERED_CANDIDATE_SUPPLIER_2026"
          },
          {
            "@type": "PropertyValue",
            "name": "European Commission PIC Number",
            "value": "861711529"
          },
          {
            "@type": "PropertyValue",
            "name": "EIT Urban Mobility Partner ID",
            "value": "CUS15554"
          },
          {
            "@type": "PropertyValue",
            "name": "Teknopark Istanbul Cube Incubation & HASAT 2026 Protocol",
            "value": "CONFIRMED_6_MONTH_INCUBATION"
          },
          {
            "@type": "PropertyValue",
            "name": "ITO BTM Fulya Deep-Tech Campus Residency",
            "value": "RESIDENT_ENTREPRENEUR"
          },
          {
            "@type": "PropertyValue",
            "name": "YTU Yildiz Teknopark Incubation Ecosystem",
            "value": "REGISTERED_APPLICANT"
          },
          {
            "@type": "PropertyValue",
            "name": "KOSGEB Advanced Entrepreneur Certificate & BTK AI Certificate",
            "value": "KSB01UGE0115153370 / L2zPtN4X1ZJ"
          }
        ],
        "knowsAbout": [
          "Level 4 Autonomous Driving",
          "SAIC Maxus MIFA 7 Robotaxi Architecture",
          "Hyundai Ioniq 5 E-GMP Platform",
          "ISO 26262 ASIL-D Functional Safety",
          "IEEE 2846 Responsibility-Sensitive Safety (RSS)",
          "ISO 21448 SOTIF Safety of the Intended Functionality",
          "UN ECE R155 CSMS CAN-FD Intrusion Detection",
          "UN ECE R156 SUMS RXSWIN & Atomic Rollback",
          "UN ECE R157 DSSAD SHA-256 Blackbox",
          "EU 2022/1426 Automated Driving System Type Approval",
          "Frenet (s, d) Jerk-Optimal Lattice Trajectory Planning",
          "Receding-Horizon Model Predictive Control (MPC)",
          "Lanelet2 HD Map & Traffic Rule Engine",
          "IEEE 1588v2 PTP & 3D LiDAR Motion Deskewing",
          "ISO/TR 23049 External HMI (eHMI) & Siren Detection",
          "3D LiDAR NDT SLAM & 400 Hz ESKF",
          "CARLA 0.9.15+ Synchronous Simulation Bridge",
          "1324 Core Tests and 21 Robotaxi SDK Tests (1350 Tests Total - 100% Green)",
          "CenterPoint 3D BEV Deep Perception & nuScenes Catalog",
          "7-DOF Extended Kalman Filter (EKF) Multi-Object Tracking",
          "3-Second Kinematic Trajectory Prediction & Intent Forecaster",
          "ISO 21448 SOTIF Runtime Plausibility & Phantom Brake Arbiter"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://trustia.com.tr/#software",
        "name": "TRUSTIA AI Autonomous Core & Robotaxi Enterprise SDK",
        "operatingSystem": "Linux, ROS 2 Humble, Real-Time RTOS, Embedded Linux",
        "applicationCategory": "AutonomousDrivingSoftware",
        "description": "Seviye 4 yerli deterministik otonom sürüş, SAIC Maxus MIFA 7 / Hyundai Ioniq 5 Robotaksi SDK ve askeri robotik otonomi yazılım çekirdeği. 205 Dosya, 31.400+ satır kod, 21 uluslararası L4 alt sistemi, 1.350 doğrulanmış test (%100 yeşil), OIN 2.0 patent korumalı.",
        "softwareVersion": "4.4.0-enterprise",
        "offers": {
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock"
        }
      },
      {
        "@type": "WebSite",
        "@id": "https://trustia.com.tr/#website",
        "url": "https://trustia.com.tr",
        "name": "TRUSTIA AI",
        "description": "Milli Seviye 4 Yerli Robotaksi ve Askeri İKA Otonomi Platformu",
        "publisher": {
          "@id": "https://trustia.com.tr/#organization"
        },
        "inLanguage": ["tr-TR", "en-US"]
      },
      {
        "@type": "VideoObject",
        "@id": "https://trustia.com.tr/#hero-video",
        "name": "TRUSTIA AI — Seviye 4 Yerli Otonomi ve Robotaksi Platformu",
        "description": "Trustia AI; şehir içi sivil Robotaksi filoları ve GPS sinyalinin bulunmadığı sahalarda görev yapan İnsansız Savunma Robotları için geliştirilen Seviye 4 otonom sürüş yazılım çekirdeği.",
        "thumbnailUrl": "https://trustia.com.tr/og-image.jpg",
        "uploadDate": "2026-08-30T23:00:00+03:00",
        "contentUrl": "https://trustia.com.tr/hero-video.mp4",
        "embedUrl": "https://trustia.com.tr/",
        "duration": "PT30S"
      }
    ]
  };

  return (
    <html lang="tr" className="dark scroll-smooth">
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){window.addEventListener('error',function(e){var m=(e&&e.message)?e.message:'';if(m.indexOf('chunk')!==-1||m.indexOf('Loading chunk')!==-1||m.indexOf('Failed to fetch')!==-1){if(!sessionStorage.getItem('chunk_retry')){sessionStorage.setItem('chunk_retry','1');window.location.reload();}}});window.addEventListener('unhandledrejection',function(e){var r=(e&&e.reason)?(e.reason.message||e.reason.name||''):'';if(r.indexOf('chunk')!==-1||r.indexOf('ChunkLoadError')!==-1||r.indexOf('Failed to fetch')!==-1){if(!sessionStorage.getItem('chunk_retry')){sessionStorage.setItem('chunk_retry','1');window.location.reload();}}});})();`
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="bg-[#1c1813] text-[#f5efe6] antialiased selection:bg-[#E4F80D] selection:text-black font-sans min-h-screen overflow-x-hidden">
        <LanguageProvider>
          {children}
        </LanguageProvider>
      </body>
    </html>
  );
}
