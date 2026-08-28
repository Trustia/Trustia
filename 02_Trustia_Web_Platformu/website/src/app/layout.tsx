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
    default: "TRUSTIA AI — GPS-Denied Defense UGV Autonomy Platform | Milli Askeri Otonomi",
    template: "%s | TRUSTIA AI",
  },
  description:
    "TRUSTIA Autonomous Systems; GPS sinyalinin bulunmadığı operasyon sahalarında İnsansız Kara Araçları (İKA) için 3D Poz Grafı SLAM, Hybrid A* rota planlama, EYP/Mayın tespiti ve hava-kara sürü zekası sunan milli askeri otonomi yazılım platformudur. (İstanbul, Türkiye).",
  keywords: [
    "TRUSTIA AI",
    "Trustia Autonomous Systems",
    "otonomi yazılımı",
    "insansız kara aracı",
    "İKA otonomi",
    "GPS-denied navigation",
    "3D SLAM",
    "Hybrid A* pathfinding",
    "STANAG 4586",
    "SAE JAUS AS6091",
    "ROS 2 Humble",
    "CAN FD bridge",
    "askeri yapay zeka",
    "milli savunma sanayii",
    "EYP tespiti",
    "hava-kara sürü zekası",
    "defense tech startup",
    "UGV autonomy software",
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
    title: "TRUSTIA AI — GPS-Denied Defense UGV Autonomy Platform",
    description:
      "Milli Askeri Otonomi Yazılım Platformu: 3D SLAM, Hybrid A* rota, EYP/Mayın tehdit füzyonu ve hava-kara hibrit sürü zekası. STANAG 4586 Level 4 uyumlu.",
    url: "https://trustia.com.tr",
    siteName: "TRUSTIA AI",
    locale: "tr_TR",
    alternateLocale: ["en_US"],
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "TRUSTIA AI — Military UGV Autonomy Platform (1200x630)",
        type: "image/jpeg",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "TRUSTIA AI — GPS-Denied Defense UGV Autonomy Platform",
    description:
      "Military-grade UGV autonomy software core featuring 3D SLAM, kinematic pathfinding, IED detection & multi-agent swarm intelligence.",
    images: ["https://trustia.com.tr/og-image.jpg"],
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
  category: "Defense Technology",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Schema.org Structured Data (JSON-LD) for Google Search Console, Knowledge Graph & Defense Entities
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Corporation",
        "@id": "https://trustia.com.tr/#organization",
        "name": "Trustia AI",
        "alternateName": ["TRUSTIA AI", "Trustia Teknoloji", "Trustia Autonomous Systems"],
        "url": "https://trustia.com.tr",
        "logo": "https://trustia.com.tr/logo.png",
        "image": "https://trustia.com.tr/og-image.jpg",
        "description": "GPS-Denied Military UGV Autonomy Software Core, 3D Pose Graph SLAM & Swarm Intelligence Platform.",
        "foundingDate": "2026",
        "founder": {
          "@type": "Person",
          "name": "Murat Furkan Bayram",
          "jobTitle": "Founder & Autonomous Systems Lead Engineer"
        },
        "address": [
          {
            "@type": "PostalAddress",
            "addressLocality": "İstanbul",
            "addressCountry": "TR"
          }
        ],
        "contactPoint": {
          "@type": "ContactPoint",
          "email": "iletisim@trustia.com.tr",
          "contactType": "corporate inquiries",
          "availableLanguage": ["Turkish", "English"]
        },
        "sameAs": [
          "https://github.com/Trustia/Trustia",
          "https://trustia.com.tr"
        ],
        "knowsAbout": [
          "STANAG 4586 Level 4",
          "SAE AS6091 JAUS",
          "3D LiDAR SLAM",
          "Hybrid A* Kinematic Path Planning",
          "ROS 2 Humble",
          "CAN FD",
          "Unmanned Ground Vehicles (UGV)",
          "Military Artificial Intelligence"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://trustia.com.tr/#software",
        "name": "TRUSTIA AI Autonomy Core",
        "operatingSystem": "Linux, ROS 2, Embedded RTOS",
        "applicationCategory": "DefenseApplication",
        "description": "Sovereign, GPS-denied autonomous navigation and threat fusion engine for defense unmanned ground vehicles.",
        "offers": {
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock"
        }
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
