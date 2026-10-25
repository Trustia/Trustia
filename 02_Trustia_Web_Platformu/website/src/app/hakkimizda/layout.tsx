import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Hakkımızda & Milli Otonomi Vizyonu",
  description:
    "Trustia AI; kurucusu ve tek pay sahibi Murat Furkan Bayram liderliğinde geliştirilen, 16.400+ satırlık deterministik Seviye-4 otonom sürüş yazılım çekirdeği ve 1.307 doğrulanmış test teminatıyla çalışan yerli derin teknoloji girişimidir.",
  keywords: [
    "Trustia Hakkımızda",
    "Murat Furkan Bayram",
    "Milli Otonom Sürüş",
    "Yerli Seviye 4 Otonomi",
    "Robotaksi Yazılımı",
    "ASELSAN Tedarikçi #0050569",
    "OIN Patent Lisansı #f1e44576",
    "Avrupa Komisyonu PIC 861711529",
    "EIT Urban Mobility CUS15554",
    "İTO BTM Fulya Kampüsü",
    "Teknopark İstanbul HASAT 2026"
  ],
  alternates: {
    canonical: "https://trustia.com.tr/hakkimizda/",
  },
  openGraph: {
    title: "Hakkımızda & Milli Otonomi Vizyonu | TRUSTIA AI",
    description:
      "Kurucu ve Tek Pay Sahibi Murat Furkan Bayram liderliğinde 16.400+ satır L4 çekirdek ve 1.307 doğrulanmış test ile inşa edilen bağımsız otonomi platformu.",
    url: "https://trustia.com.tr/hakkimizda/",
    siteName: "TRUSTIA AI",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/og-image.jpg?v=2026",
        width: 1200,
        height: 630,
        alt: "Trustia AI Kurumsal ve Mühendislik Vizyonu",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Hakkımızda & Milli Otonomi Vizyonu | TRUSTIA AI",
    description:
      "16.400+ lines of sovereign Level-4 autonomy core verified across 1,307 automated tests. Founded by Murat Furkan Bayram.",
    images: ["https://trustia.com.tr/og-image.jpg?v=2026"],
  },
};

export default function AboutLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
