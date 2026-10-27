import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "SAIC Maxus MIFA 7 & Hyundai Ioniq 5 Seviye 4 Referans Robotaksi Mimarisi",
  description:
    "Trustia AI; SAIC Maxus MIFA 7 ve Hyundai Ioniq 5 (E-GMP) platformlarında 128 kanallı 3D LiDAR, 4x GMSL2 HDR kamera, 77GHz radar, 100 Hz CAN-FD aktüatör köprüsü, IEEE 2846 RSS, UN R155/R156/R157, Frenet Lattice, MPC ve 1.307 + 21 testle doğrulanmış Seviye-4 Robotaksi mimarisidir.",
  keywords: [
    "Robotaksi",
    "Yerli Robotaksi",
    "SAIC Maxus MIFA 7 Robotaksi",
    "Hyundai Ioniq 5 Robotaksi",
    "Seviye 4 Otonom Sürüş",
    "AB 2022/1426 Tip Onayı",
    "IEEE 2846 RSS",
    "ISO 21448 SOTIF",
    "UN ECE R155 R156 R157",
    "Frenet Lattice Planner",
    "Model Predictive Control MPC",
    "Lanelet2 HD Harita",
    "IEEE 1588 PTP LiDAR Deskewing",
    "CARLA 0.9.15 Simülasyon",
    "CAN-FD Drive-by-Wire",
    "Ouster OS2-128 LiDAR",
    "Livox Mid-360",
    "Jetson AGX Orin",
    "Trustia AI"
  ],
  alternates: {
    canonical: "https://trustia.com.tr/robotaxi/",
  },
  openGraph: {
    title: "SAIC Maxus MIFA 7 & Hyundai Ioniq 5 Seviye 4 Robotaksi Mimarisi | TRUSTIA AI",
    description:
      "20 uluslararası Seviye-4 otonomi modülü, 29.748+ satır kod, 1.307 + 21 doğrulanmış test, 100 Hz CAN-FD Drive-by-Wire ve AB 2022/1426 (1 Aralık 2024 Resmî Gazete) tam uyumluluk matrisi.",
    url: "https://trustia.com.tr/robotaxi/",
    siteName: "TRUSTIA AI",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/logo.png",
        width: 1200,
        height: 630,
        alt: "Trustia AI Seviye 4 Robotaksi Mimarisi",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "SAIC Maxus MIFA 7 & Hyundai Ioniq 5 Seviye 4 Robotaksi Mimarisi | TRUSTIA AI",
    description:
      "20 Level-4 modules, 29,748+ LOC, 1,307 + 21 verified tests, IEEE 2846 RSS, Frenet, MPC, UN R155/R156/R157 and 100 Hz CAN-FD Drive-by-Wire.",
    images: ["https://trustia.com.tr/logo.png"],
  },
};

export default function RobotaxiLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
