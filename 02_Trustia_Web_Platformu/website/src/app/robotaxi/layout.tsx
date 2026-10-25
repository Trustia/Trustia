import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Hyundai Ioniq 5 Seviye 4 Referans Otonomi Mimarisi (RAD)",
  description:
    "Trustia AI; Hyundai Ioniq 5 (E-GMP) platformunda 128 kanallı 3D LiDAR, 4x GMSL2 HDR kamera, 77GHz radar ve 100 Hz CAN-FD aktüatör mimarisiyle çalışan Seviye 4 referans otonomi mimarisidir.",
  keywords: [
    "Robotaksi",
    "Yerli Robotaksi",
    "Hyundai Ioniq 5 Robotaksi",
    "Seviye 4 Otonom Sürüş",
    "Autonomous Robotaxi",
    "Level 4 Autonomy",
    "E-GMP Autonomy",
    "CAN-FD Drive-by-Wire",
    "Ouster OS2-128 LiDAR",
    "Livox Mid-360",
    "Jetson AGX Orin",
    "Sony IMX390 GMSL2",
    "Trustia AI"
  ],
  alternates: {
    canonical: "https://trustia.com.tr/robotaxi/",
  },
  openGraph: {
    title: "Hyundai Ioniq 5 Seviye 4 Referans Otonomi Mimarisi | TRUSTIA AI",
    description:
      "27 parçalık doğrulanmış donanım kiti, 128 kanallı 3D LiDAR, 4x GMSL2 HDR kamera, 77GHz radar ve 16.400+ satır deterministik yerli otonomi çekirdeği.",
    url: "https://trustia.com.tr/robotaxi/",
    siteName: "TRUSTIA AI",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/logo.png",
        width: 1200,
        height: 630,
        alt: "Trustia AI Seviye 4 Otonomi Mimarisi",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Hyundai Ioniq 5 Seviye 4 Referans Otonomi Mimarisi | TRUSTIA AI",
    description:
      "128ch LiDAR, 4x GMSL2 HDR Vision, 77GHz Radar and 100 Hz CAN-FD Drive-by-Wire on Hyundai Ioniq 5 E-GMP Platform.",
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
