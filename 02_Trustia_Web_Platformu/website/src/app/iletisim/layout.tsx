import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "İletişim, Ar-Ge Merkezi & Şartname Talebi | TRUSTIA AI",
  description:
    "Trustia AI kurumsal santral, Ar-Ge merkezi (İTO BTM Fulya Yerleşkesi, Şişli / İstanbul), teknik şartname talepleri ve OEM otonomi entegrasyonu başvuru kanalları.",
  keywords: [
    "Trustia İletişim",
    "Trustia Ar-Ge",
    "İTO BTM Fulya Kampüsü",
    "Robotaksi Şartname Talebi",
    "Otonomi SDK Lisanslama",
    "OEM Entegrasyonu",
    "Kariyer Trustia AI"
  ],
  alternates: {
    canonical: "https://trustia.com.tr/iletisim/",
  },
  openGraph: {
    title: "İletişim & Ar-Ge Merkezi | TRUSTIA AI",
    description:
      "İTO BTM Fulya Kampüsü, Şişli / İstanbul. Kurumsal iletişim, teknik şartname ve OEM entegrasyon kanalları.",
    url: "https://trustia.com.tr/iletisim/",
    siteName: "TRUSTIA AI",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/og-image.jpg?v=2026",
        width: 1200,
        height: 630,
        alt: "Trustia AI İletişim ve Ar-Ge Merkezi",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "İletişim & Ar-Ge Merkezi | TRUSTIA AI",
    description:
      "Contact Trustia AI Headquarters (Istanbul, Turkey) for Level-4 engineering specifications and OEM partnership inquiries.",
    images: ["https://trustia.com.tr/og-image.jpg?v=2026"],
  },
};

export default function ContactLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
