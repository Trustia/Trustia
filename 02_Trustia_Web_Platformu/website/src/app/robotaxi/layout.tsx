import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Hyundai Ioniq 5 Seviye 4 Yerli Robotaksi Platformu",
  description:
    "Trustia AI; Hyundai Ioniq 5 (E-GMP) platformunda 128 kanallı LiDAR, 4x GMSL2 HDR kamera, 77GHz radar ve 100 Hz CAN-FD aktüatör mimarisiyle çalışan Seviye 4 yerli Robotaksi otonomi mimarisidir. (İstanbul, Türkiye).",
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
    "Trustia AI",
    "Murat Furkan Bayram",
    "İTO BTM",
    "Bilişim Vadisi"
  ],
  alternates: {
    canonical: "https://trustia.com.tr/robotaxi/",
  },
  openGraph: {
    title: "Hyundai Ioniq 5 Seviye 4 Yerli Robotaksi Platformu | TRUSTIA AI",
    description:
      "27 parçalık doğrulanmış donanım kiti, 128 kanallı 3D LiDAR, 4x GMSL2 HDR kamera, 77GHz radar ve 16.000 satır deterministik yerli otonomi çekirdeği.",
    url: "https://trustia.com.tr/robotaxi/",
    siteName: "TRUSTIA AI",
    type: "website",
    images: [
      {
        url: "https://trustia.com.tr/robotaxi/ioniq5_foto_1.png",
        width: 1200,
        height: 675,
        alt: "Hyundai Ioniq 5 Level 4 Autonomous Robotaxi Test Vehicle",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Hyundai Ioniq 5 Seviye 4 Yerli Robotaksi Platformu | TRUSTIA AI",
    description:
      "128ch LiDAR, 4x GMSL2 HDR Vision, 77GHz Radar and 100 Hz CAN-FD Drive-by-Wire on Hyundai Ioniq 5 E-GMP Platform.",
    images: ["https://trustia.com.tr/robotaxi/ioniq5_foto_1.png"],
  },
};

export default function RobotaxiLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
