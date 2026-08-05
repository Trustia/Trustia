import type { Metadata } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";

export const metadata: Metadata = {
  metadataBase: new URL("https://trustia.com.tr"),
  title: {
    default: "TRUSTIA AI — Milli Askeri Otonomi Yazılım Çekirdeği | %100 Yerli İKA Yazılımı",
    template: "%s | TRUSTIA AI",
  },
  description:
    "TRUSTIA AI; GPS'siz ortamlarda insansız kara araçları (İKA) için 3D Poz Grafı SLAM, Görsel Odometri, EYP/CBRN tehdit algılama ve hava-kara hibrit sürü zekası sunan %100 yerli yazılım mimarisidir. İstanbul, Türkiye.",
  keywords: [
    "otonomi yazılımı",
    "insansız kara aracı",
    "İKA otonomi",
    "3D SLAM",
    "GPS-denied navigation",
    "STANAG 4586",
    "ROS 2",
    "CAN FD",
    "askeri yapay zeka",
    "yerli savunma sanayii",
    "TRUSTIA AI",
    "İstanbul",
  ],
  authors: [{ name: "Trustia Teknoloji", url: "https://trustia.com.tr" }],
  creator: "Trustia Teknoloji",
  publisher: "Trustia Teknoloji",
  alternates: {
    canonical: "https://trustia.com.tr/",
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
    title: "TRUSTIA AI — Milli Askeri Otonomi Yazılım Çekirdeği",
    description:
      "GPS'siz ortamlarda insansız kara araçları için 3D SLAM, tehdit füzyonu ve hava-kara hibrit sürü zekası sunan %100 yerli askeri yazılım mimarisi.",
    url: "https://trustia.com.tr",
    siteName: "TRUSTIA AI",
    locale: "tr_TR",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/logo.png",
        width: 1200,
        height: 630,
        alt: "TRUSTIA AI Milli Otonomi Platformu Logo",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "TRUSTIA AI — Milli Askeri Otonomi Yazılım Çekirdeği",
    description:
      "GPS'siz ortamlarda insansız kara araçları için 3D SLAM ve sürü zekası sunan %100 yerli yazılım mimarisi.",
    images: ["https://trustia.com.tr/logo.png"],
  },
  icons: {
    icon: "/logo.png",
    shortcut: "/logo.png",
    apple: "/logo.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Schema.org Structured Data (JSON-LD) for Google Search Console & Rich Snippets
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://trustia.com.tr/#organization",
        "name": "Trustia Teknoloji",
        "url": "https://trustia.com.tr",
        "logo": "https://trustia.com.tr/logo.png",
        "description": "Milli Askeri Otonomi Yazılım Çekirdeği ve İnsansız Kara Araçları (İKA) Yapay Zeka Mimarisi",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "İstanbul",
          "addressCountry": "TR"
        },
        "knowsAbout": [
          "STANAG 4586",
          "3D SLAM",
          "ROS 2",
          "Autonomous Ground Vehicles",
          "Military Artificial Intelligence"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://trustia.com.tr/#software",
        "name": "TRUSTIA AI Autonomy Core",
        "operatingSystem": "Linux, ROS 2, Embedded RTOS",
        "applicationCategory": "DefenseApplication",
        "description": "GPS'siz ortamlarda 3D Poz Grafı SLAM ve engel kaçınma sağlayan askeri sınıflı otonom sürüş yazılım çekirdeği."
      }
    ]
  };

  return (
    <html lang="tr" className="dark scroll-smooth">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap"
          rel="stylesheet"
        />
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
