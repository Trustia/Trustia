import type { Metadata, Viewport } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";

export const viewport: Viewport = {
  themeColor: "#090b0e",
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
    "Trustia AI; şehir içi sivil Robotaksi filoları ve GPS sinyalinin bulunmadığı harekat sahalarında görev yapan İnsansız Savunma Robotları için V2X, 3D SLAM, 5 saniyelik yörünge tahmini ve Seviye 4 yerli otonomi yazılım platformudur. Open Invention Network (OIN 2.0 Lisansı: #f1e44576), NATO NCAGE (TR26258467723), ASELSAN tedarikçi (#0050569), Avrupa Komisyonu (PIC: 861711529), EIT Urban Mobility (CUS15554), Malta Enterprise ve İTO BTM tescilli. (İstanbul, Türkiye).",
  keywords: [
    "TRUSTIA AI",
    "Trustia",
    "Trustia Teknoloji",
    "otonomi yazılımı",
    "robotaksi",
    "yerli robotaksi",
    "seviye 4 otonom sürüş",
    "insansız kara aracı",
    "İKA otonomi",
    "V2X",
    "C-V2X",
    "GPS-denied navigation",
    "3D SLAM",
    "yörünge tahmini",
    "Hybrid A*",
    "STANAG 4586",
    "SAE JAUS AS6091",
    "ROS 2 Humble",
    "CAN FD bridge",
    "savunma sanayii",
    "İTO BTM",
    "Teknopark İstanbul",
    "Teknopark İstanbul HASAT 2026",
    "KOSGEB İleri Girişimci",
    "İstanbul",
    "Avrupa Komisyonu PIC 861711529",
    "EIT Urban Mobility CUS15554",
    "Singapore Startup SG #57428",
    "Singapore Global Innovation Alliance GIA",
    "B2Match Singapore Joint Innovation",
    "Enterprise Singapore",
    "EntrePass Singapore",
    "QSTP Doha Sprint",
    "BAYKAR Teknoloji",
    "ASELSAN Tedarikçi",
    "DEİK Dijital Teknolojiler",
    "Z Fellows",
    "fonbulucu W1MV5K",
    "Crunchbase Trustia AI",
  ],
  authors: [
    { name: "Trustia AI", url: "https://trustia.com.tr" },
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
    title: "TRUSTIA AI — Seviye 4 Yerli Robotaksi & Askeri Otonomi Platformu",
    description:
      "Milli Çift Amaçlı Otonomi Mimarisi: Hyundai Ioniq 5 Seviye 4 Robotaksi, 3D LiDAR SLAM ve 1.301 Doğrulanmış Test. AB PIC: 861711529, EITUM: CUS15554, Singapur Startup SG: #57428, İTO BTM & ASELSAN Akreditasyonlu.",
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
    title: "TRUSTIA AI — Level 4 Autonomous Driving & Defense Robotics Core",
    description:
      "Dual-use Level 4 sovereign autonomy software featuring Hyundai Ioniq 5 Robotaxi, 3D LiDAR SLAM, and 1,301 verified tests. EU PIC: 861711529 • SG Startup SG: #57428.",
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
        "description": "Milli Çift Amaçlı Seviye 4 Otonom Sürüş, V2X Akıllı Şehir ve Askeri İnsansız Kara Aracı (İKA) Otonomi Yazılım Platformu.",
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
          "https://www.linkedin.com/in/trustia",
          "https://www.crunchbase.com/organization/trustia-ai",
          "https://www.startupsg.gov.sg/profiles/57428",
          "https://www.b2match.com/e/joint-innovation-with-singapore-2024"
        ],
        "identifier": [
          {
            "@type": "PropertyValue",
            "name": "Open Invention Network (OIN 2.0) Executed License Document ID",
            "value": "f1e445769a9934114db095c4f5430a0e749d8201"
          },
          {
            "@type": "PropertyValue",
            "name": "NATO Allied NCAGE Military Supplier Reference",
            "value": "TR26258467723"
          },
          {
            "@type": "PropertyValue",
            "name": "Malta Enterprise 1.5M Euro Grant Application",
            "value": "100062411"
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
            "name": "Singapore Government Startup SG Profile ID",
            "value": "57428"
          },
          {
            "@type": "PropertyValue",
            "name": "Enterprise Singapore GIA Application Response ID",
            "value": "6aa85fa93dc42d7feef1bc57"
          },
          {
            "@type": "PropertyValue",
            "name": "ASELSAN Approved Potential Supplier ID",
            "value": "0050569CCE941FD1A49FCEFB9B7BE7D6"
          },
          {
            "@type": "PropertyValue",
            "name": "Teknopark Istanbul HASAT 2026 Submission",
            "value": "CONFIRMED"
          },
          {
            "@type": "PropertyValue",
            "name": "SPK fonbulucu Campaign Code",
            "value": "W1MV5K"
          },
          {
            "@type": "PropertyValue",
            "name": "SSB SAYZEK Simulation ID",
            "value": "170"
          }
        ],
        "knowsAbout": [
          "Level 4 Autonomous Driving",
          "Open Invention Network (OIN 2.0)",
          "Cross-License Patent Immunity",
          "Robotaxi Fleet Management",
          "V2X / C-V2X Communication",
          "3D LiDAR SLAM",
          "GPS-Denied Navigation",
          "Trajectory Prediction AI",
          "STANAG 4586 Level 4",
          "SAE AS6091 JAUS",
          "ROS 2 Humble",
          "CAN-FD Integration",
          "Hyundai Ioniq 5 E-GMP Platform",
          "Unmanned Ground Vehicles (UGV)",
          "1301 Automated Unit Tests",
          "Global Innovation Alliance (GIA)",
          "Enterprise Singapore Deep Tech Network",
          "EntrePass Framework"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://trustia.com.tr/#software",
        "name": "TRUSTIA AI Autonomous Core Stack",
        "operatingSystem": "Linux, ROS 2 Humble, Real-Time RTOS, Embedded Linux",
        "applicationCategory": "AutonomousDrivingSoftware",
        "description": "Seviye 4 yerli deterministik otonom sürüş, V2X ve askeri robotik otonomi yazılım çekirdeği. 16.000+ satır C++/Python, 1.301 doğrulanmış test, OIN 2.0 patent korumalı.",
        "softwareVersion": "3.0.0",
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
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="bg-[#090b0e] text-[#e1e7ec] antialiased selection:bg-[#C8FF00] selection:text-black font-sans min-h-screen overflow-x-hidden">
        <LanguageProvider>
          {children}
        </LanguageProvider>
      </body>
    </html>
  );
}
