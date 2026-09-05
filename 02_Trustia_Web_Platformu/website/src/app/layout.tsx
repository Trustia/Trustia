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
    "Trustia AI; şehir içi sivil Robotaksi filoları ve GPS sinyalinin bulunmadığı harekat sahalarında görev yapan İnsansız Savunma Robotları için V2X, 3D SLAM, 5 saniyelik yörünge tahmini ve Seviye 4 yerli otonomi yazılım platformudur. (İstanbul, Türkiye).",
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
    "KOSGEB İleri Girişimci",
    "Murat Furkan Bayram",
    "İstanbul",
  ],
  authors: [
    { name: "Trustia AI", url: "https://trustia.com.tr" },
    { name: "Murat Furkan Bayram", url: "https://trustia.com.tr/hakkimizda/" },
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
      "Milli Çift Amaçlı Otonomi Mimarisi: Hyundai Ioniq 5 Seviye 4 Robotaksi, 3D LiDAR SLAM, 5 Saniyelik Yörünge Yapay Zekası ve 1.301 Doğrulanmış Test. İTO BTM & SSB Akreditasyonlu.",
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
      "Dual-use Level 4 sovereign autonomy software featuring Hyundai Ioniq 5 Robotaxi, 3D LiDAR SLAM, and 1,301 verified tests.",
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
        "foundingDate": "2026",
        "founder": {
          "@type": "Person",
          "name": "Murat Furkan Bayram",
          "jobTitle": "Kurucu & Sistem Mimarı / Founder & Autonomous Systems Architect",
          "sameAs": "https://www.linkedin.com/in/trustia"
        },
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Fulya Mah. Yeşilçimen Sok. İTO BTM Kampüsü, Şişli / İstanbul",
          "addressLocality": "Şişli",
          "addressRegion": "İstanbul",
          "addressCountry": "TR"
        },
        "contactPoint": {
          "@type": "ContactPoint",
          "email": "iletisim@trustia.com.tr",
          "contactType": "Corporate Inquiries & Partnerships",
          "availableLanguage": ["Turkish", "English"]
        },
        "sameAs": [
          "https://github.com/Trustia/Trustia",
          "https://trustia.com.tr",
          "https://www.linkedin.com/in/trustia"
        ],
        "knowsAbout": [
          "Level 4 Autonomous Driving",
          "Robotaxi",
          "V2X / C-V2X Communication",
          "3D LiDAR SLAM",
          "GPS-Denied Navigation",
          "Trajectory Prediction AI",
          "STANAG 4586 Level 4",
          "SAE AS6091 JAUS",
          "ROS 2 Humble",
          "CAN FD",
          "Unmanned Ground Vehicles (UGV)"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://trustia.com.tr/#software",
        "name": "TRUSTIA AI Autonomous Core Stack",
        "operatingSystem": "Linux, ROS 2 Humble, Real-Time RTOS, Embedded Linux",
        "applicationCategory": "AutonomousDrivingSoftware",
        "description": "Seviye 4 yerli otonom sürüş, V2X ve askeri robotik otonomi yazılım çekirdeği.",
        "softwareVersion": "2.1.0",
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
        "name": "Trustia AI",
        "description": "Seviye 4 Yerli Robotaksi ve Askeri İKA Otonomi Platformu",
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
