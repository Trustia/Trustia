import PolicyDocumentView from "@/components/PolicyDocumentView";
import { notFound } from "next/navigation";

export interface PolicyContent {
  tr: {
    title: string;
    badge: string;
    subBadge: string;
    category: string;
    summary: string;
    sections: {
      heading: string;
      items: string[];
    }[];
  };
  en: {
    title: string;
    badge: string;
    subBadge: string;
    category: string;
    summary: string;
    sections: {
      heading: string;
      items: string[];
    }[];
  };
  iconName: string;
}

export const policyData: Record<string, PolicyContent> = {
  lisans: {
    iconName: "FileText",
    tr: {
      title: "Otonomi Yazılım Lisanslama ve Kullanım Şartları (EULA / SLA)",
      badge: "SOFTWARE-ONLY SLA",
      subBadge: "LİSANS v2.0",
      category: "YAZILIM LİSANSLAMA",
      summary: "Bu lisans sözleşmesi, TRUSTIA TEKNOLOJİ tarafından geliştirilen TRUSTIA otonomi yazılım çekirdeğinin, İnsansız Kara Aracı (İKA) donanım üreticileri ve entegratörleri tarafından kullanım şartlarını düzenler. TRUSTIA, araç fiziki donanımı üretmeyip sadece otonomi yazılım beynini lisanslar.",
      sections: [
        {
          heading: "1. Lisans Kapsamı ve Münhasırlık",
          items: [
            "TRUSTIA yazılım çekirdeği, üretici firmanın İnsansız Kara Aracı (İKA) platformu için gayri-münhasır (non-exclusive), devredilemez otonom kullanım lisansı olarak tahsis edilir.",
            "Tüm yazılım kaynak kodları, otonomi algoritmaları, 3D SLAM kütüphaneleri ve sürü zekası modelleri TRUSTIA TEKNOLOJİ mülkiyetindedir.",
            "Lisans alan entegratör firma, yazılımı tersine mühendislik (reverse engineering) işlemine tabi tutamaz veya yetkisiz kopyalayamaz."
          ]
        },
        {
          heading: "2. Donanım Bağımsızlığı ve Entegrasyon Sorumluluğu",
          items: [
            "TRUSTIA yazılımı; CAN-BUS, ROS2 ve UDP/TCP socket protokolleri üzerinden donanım aktüatörlerine komut iletir.",
            "Fiziksel aracın mekanik aksamı, motor sürücüleri, fren sistemleri ve şasi emniyeti donanım üreticisinin veya entegratörün sorumluluğundadır.",
            "TRUSTIA, donanım kaynaklı mekanik kırıma veya fiziksel donanım arızalarına karşı sorumluluk kabul etmez."
          ]
        },
        {
          heading: "3. Servis Seviyesi Taahhüdü (SLA) ve Güncelleme",
          items: [
            "Kritik güvenlik güncellemeleri ve siber yamalar lisans süresince kesintisiz olarak yayınlanır.",
            "Saha görevlerinde karşılaşılan algoritmik istisnalar için 48 saat içerisinde teknik destek ve kütük (log) analizi sağlanır."
          ]
        }
      ]
    },
    en: {
      title: "Autonomy Software Licensing & Terms of Use (EULA / SLA)",
      badge: "SOFTWARE-ONLY SLA",
      subBadge: "LICENSE v2.0",
      category: "SOFTWARE LICENSING",
      summary: "This license agreement governs the terms and conditions under which UGV manufacturers and defense integrators deploy the TRUSTIA Autonomy Software Core. TRUSTIA operates as a pure-play software intelligence provider and licenses its autonomous cognitive stack.",
      sections: [
        {
          heading: "1. Scope of License & Non-Exclusivity",
          items: [
            "The TRUSTIA core software is licensed on a non-exclusive, non-transferable basis for integration into authorized UGV platforms.",
            "All algorithms, 3D SLAM architectures, and neural threat fusion models remain the sole intellectual property of TRUSTIA Autonomous Systems.",
            "Reverse engineering, unauthorized decompilation, or third-party sublicensing is strictly prohibited under international IP treaties."
          ]
        },
        {
          heading: "2. Hardware Agnostic Interface & Integrator Scope",
          items: [
            "TRUSTIA interfaces via standardized CAN-FD, ROS 2, and UDP socket layers to command low-level motor drivers and steering actuators.",
            "Chassis mechanical integrity, electrical powertrain safety, and emergency braking hardware remain the integrator's responsibility.",
            "TRUSTIA disclaims liability for mechanical structural failure originating from physical hardware defects."
          ]
        },
        {
          heading: "3. Service Level Agreement (SLA) & Field Support",
          items: [
            "Continuous deployment of critical security patches and anti-jamming updates throughout active mission contracts.",
            "Comprehensive 48-hour telemetry log review and root-cause analysis for field trial anomalies."
          ]
        }
      ]
    }
  },
  yerlilik: {
    iconName: "Award",
    tr: {
      title: "%100 Yerli Katkı ve Savunma Sanayii Sertifikasyon Taahhüdü",
      badge: "MİLLİ TEKNOLOJİ",
      subBadge: "SERTİFİKA v2.0",
      category: "MİLLİ TEKNOLOJİ",
      summary: "TRUSTIA TEKNOLOJİ, geliştirdiği tüm otonomi algoritmaları ve karar destek sistemlerinde %100 yerli katkı oranına uymayı ve Türk Savunma Sanayii standartlarında bağımsız çalışmayı taahhüt eder.",
      sections: [
        {
          heading: "1. Sıfır Dış Bağımlılık ve Algoritma Bağımsızlığı",
          items: [
            "Yazılım mimarimiz, açık kaynak kodlu veya yabancı menşeili hazır kütüphanelere doğrudan bağımlı olmadan geliştirilmiştir.",
            "GPS kısıtlaması veya yabancı uydu bağımlılığı olan harekat sahalarında tamamen yerel sensör füzyonu (LiDAR, Termal Kameralar, IMU) ile görev icra eder.",
            "Yurtdışı ambargolarından veya lisans iptallerinden etkilenmeyecek yerli kaynak kod mimarisine sahiptir."
          ]
        },
        {
          heading: "2. Savunma Sanayii Sertifikasyon Uyumları",
          items: [
            "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı (SSB) yerlilik kriterlerine tam uyumludur.",
            "SAE AS9100 Havacılık ve Savunma Kalite Yönetimi standartları esas alınarak kodlanmıştır.",
            "STANAG 4586 Level 4 ve SAE AS6091 JAUS haberleşme standartlarına sahiptir."
          ]
        }
      ]
    },
    en: {
      title: "100% Indigenous IP & Defense Certification Compliance",
      badge: "SOVEREIGN DEFENSE IP",
      subBadge: "CERTIFICATION v2.0",
      category: "INDIGENOUS TECH",
      summary: "TRUSTIA Autonomous Systems commits to zero foreign ITAR dependency across its core algorithmic stack, delivering sovereign mission autonomy resilient against international embargoes.",
      sections: [
        {
          heading: "1. Zero Foreign Dependency & Algorithmic Sovereignty",
          items: [
            "Full proprietary codebase developed without reliance on export-restricted foreign libraries or black-box third-party binaries.",
            "Continuous mission execution in electronic warfare and GPS-denied theaters via local onboard multi-sensor fusion (LiDAR, VO, IMU).",
            "Immune to foreign export bans, remote license revocations, or satellite jamming."
          ]
        },
        {
          heading: "2. Defense Industry Standards Compliance",
          items: [
            "Fully compatible with NATO STANAG 4586 Level 4 Command & Control standards.",
            "Engineered following SAE AS9100 aerospace and defense quality guidelines.",
            "Native SAE AS6091 JAUS (Joint Architecture for Unmanned Systems) interoperability."
          ]
        }
      ]
    }
  },
  siber: {
    iconName: "Lock",
    tr: {
      title: "Askeri Siber Güvenlik ve Veri Muhafazası",
      badge: "HMAC-SHA256 ENCRYPTED",
      subBadge: "GÜVENLİK v2.0",
      category: "SİBER GÜVENLİK",
      summary: "TRUSTIA otonom karar mekanizmaları, askeri düzeyde kriptografik şifreleme ve sahadaki sinyal kesintilerine (Jamming/Spoofing) karşı yüksek dirençli Fail-Safe protokolleri ile korunur.",
      sections: [
        {
          heading: "1. Kriptografik Komut Doğrulama ve E-Stop",
          items: [
            "Yer Kontrol İstasyonundan (GCS) araca iletilen tüm otonomi ve rota komutları HMAC-SHA256 algoritması ile anlık imzalanır.",
            "Yetkisiz araya girme (Man-in-the-Middle) veya sahte komut paketleri sistem tarafından anında reddedilir.",
            "Donanımsal ve yazılımsal Acil Durdurma (E-Stop) sinyali en yüksek öncelikli kesme olarak işlenir."
          ]
        },
        {
          heading: "2. LinkLoss ve Eve Dönüş (RTH) Protokolü",
          items: [
            "Telsiz haberleşmesinin veya veri bağının koptuğu durumlarda araç 3 saniye içerisinde otomatik LinkLoss durumuna geçer.",
            "Araç, 3D SLAM haritasındaki geçmiş rotasını izleyerek otonom olarak kalkış noktasına (Home Base) geri döner."
          ]
        }
      ]
    },
    en: {
      title: "Military-Grade Cyber Defense & Data Security",
      badge: "HMAC-SHA256 ENCRYPTED",
      subBadge: "CYBERSEC v2.0",
      category: "CYBER DEFENSE",
      summary: "TRUSTIA autonomous control architectures are fortified with cryptographic telemetry authentication and electronic warfare fail-safe protocols designed for contested battlefields.",
      sections: [
        {
          heading: "1. Cryptographic Command Signing & E-Stop",
          items: [
            "All GCS command frames and trajectory waypoints are authenticated using HMAC-SHA256 signatures with dynamic nonce rotation.",
            "Man-in-the-middle packet injection or spoofed telemetry is rejected instantaneously.",
            "Deterministic hardware and software E-Stop execution via high-priority RTOS interrupts."
          ]
        },
        {
          heading: "2. Electronic Warfare LinkLoss & Autonomous Return-To-Home",
          items: [
            "Automated transition to LinkLoss fail-safe mode within 3 seconds of RF signal severance.",
            "Autonomous backtrack to home base using onboard 3D SLAM topological waypoint history without satellite dependency."
          ]
        }
      ]
    }
  },
  etik: {
    iconName: "ShieldCheck",
    tr: {
      title: "Otonom Sistemler ve Yapay Zeka Etik Bildirgesi",
      badge: "HUMAN-IN-THE-LOOP",
      subBadge: "ETİK v2.0",
      category: "SİSTEM ETİĞİ",
      summary: "TRUSTIA TEKNOLOJİ, geliştirdiği otonom yazılımlarda İnsan Denetiminde Harekat (Human-in-the-Loop) prensibini kesin kural olarak uygular.",
      sections: [
        {
          heading: "1. İnsani Denetim ve Hedef Angajman Sınırı",
          items: [
            "TRUSTIA otonomi yazılımı; rotalama, engel kaçınma, haritalama ve tehdit tespiti işlevlerini icra eder.",
            "Kinetik etki veya silah angajmanı gerektiren kararlar otonom verilemez; yetki daima insan komutandadır.",
            "Cenevre Sözleşmesi ve Uluslararası İnsani Hukuk kurallarına tam uyumludur."
          ]
        },
        {
          heading: "2. Sürü Zekası Güvenlik Çerçevesi",
          items: [
            "Sürü halindeki araçlar birbirlerinin konumlarını anlık doğrular ve dost unsur çatışmasını engelleyen çarpışma önleme algoritmaları çalıştırır."
          ]
        }
      ]
    },
    en: {
      title: "Autonomous Systems & Ethical AI Charter",
      badge: "HUMAN-IN-THE-LOOP",
      subBadge: "ETHICS v2.0",
      category: "SYSTEM ETHICS",
      summary: "TRUSTIA Autonomous Systems strictly implements a mandatory Human-in-the-Loop (HITL) doctrine for all autonomous cognitive and decision architectures.",
      sections: [
        {
          heading: "1. Human-in-the-Loop & Engagement Boundaries",
          items: [
            "TRUSTIA handles navigation, 3D SLAM mapping, obstacle negotiation, and hazardous object detection.",
            "Zero autonomous kinetic weapon authorization: all weapon engagement remains exclusively under authorized human command.",
            "Strict adherence to the Geneva Conventions and International Humanitarian Law (IHL)."
          ]
        },
        {
          heading: "2. Swarm Safety & Deconfliction",
          items: [
            "Continuous inter-agent consensus and mutual position verification to eliminate fratricide and mid-mission trajectory clashes."
          ]
        }
      ]
    }
  },
  mulkiyet: {
    iconName: "Scale",
    tr: {
      title: "Fikri ve Sınai Mülkiyet Hakları & Telif Bildirimi",
      badge: "FİKRİ MÜLKİYET",
      subBadge: "MÜLKİYET v2.0",
      category: "FİKRİ MÜLKİYET",
      summary: "TRUSTIA web sitesi, markası, yazılım kodları, 3D SLAM algoritmaları ve görsel materyalleri uluslararası fikri mülkiyet kanunları ile koruma altındadır.",
      sections: [
        {
          heading: "1. Telif Hakları ve Marka Tescili",
          items: [
            "TRUSTIA markası, logosu, web sitesi tasarımı ve yazılım mimarisi TRUSTIA Autonomous Systems Inc. mülkiyetindedir.",
            "İzinsiz kopyalanamaz, çoğaltılamaz veya başka bir ticari unvan altında sunulamaz."
          ]
        }
      ]
    },
    en: {
      title: "Intellectual Property, Copyright & Trademarks",
      badge: "INTELLECTUAL PROPERTY",
      subBadge: "IP v2.0",
      category: "INTELLECTUAL PROPERTY",
      summary: "The TRUSTIA brand, software stack, mathematical SLAM formulations, and digital assets are protected under global patent and intellectual property conventions.",
      sections: [
        {
          heading: "1. Copyright Ownership & Trademark Registration",
          items: [
            "TRUSTIA, the logo, platform codebase, and digital media are proprietary assets of TRUSTIA Autonomous Systems Inc. (Delaware, USA).",
            "Unauthorized replication, distribution, or decompilation is strictly prohibited."
          ]
        }
      ]
    }
  },
  ihracat: {
    iconName: "Globe",
    tr: {
      title: "Savunma Sanayii İhracat ve Teknoloji Transferi",
      badge: "YASAL UYUM",
      subBadge: "İHRACAT v2.0",
      category: "YASAL UYUM",
      summary: "TRUSTIA yazılım ürünlerinin yurt dışına ihracatı ve lisanslanması resmi savunma sanayii ihracat kontrol mevzuatlarına tabidir.",
      sections: [
        {
          heading: "1. İhracat Kontrolü ve Yasal İzinler",
          items: [
            "5201 sayılı Kanun ve ilgili uluslararası savunma tedarik mevzuatlarına uygun hareket edilir.",
            "Yurt dışı donanım üreticilerine yapılacak yazılım satışları yetkili devlet makamlarının onayına bağlıdır."
          ]
        }
      ]
    },
    en: {
      title: "Defense Export Controls & Technology Transfer Compliance",
      badge: "EXPORT COMPLIANCE",
      subBadge: "EXPORT v2.0",
      category: "LEGAL COMPLIANCE",
      summary: "International licensing and technology transfer of TRUSTIA autonomous software are conducted in full compliance with defense export control regimes.",
      sections: [
        {
          heading: "1. Export Authorization & Compliance",
          items: [
            "Software transfers adhere to national defense industry regulations and dual-use export control guidelines.",
            "Zero transfer of sensitive algorithmic stacks to sanctioned entities or embargoed jurisdictions."
          ]
        }
      ]
    }
  },
  kvkk: {
    iconName: "Shield",
    tr: {
      title: "KVKK, GDPR ve Veri Gizliliği Politikası",
      badge: "KVKK & GDPR COMPLIANT",
      subBadge: "GİZLİLİK v2.0",
      category: "VERİ GİZLİLİĞİ",
      summary: "TRUSTIA platformunda toplanan kurumsal iletişim verileri KVKK ve GDPR kapsamında en yüksek güvenlik standartlarında işlenir.",
      sections: [
        {
          heading: "1. Veri Sorumlusu ve Gizlilik İlkeleri",
          items: [
            "Web sitemiz üzerinden iletilen kurumsal talepler 3. şahıslarla asla ticari amaçla paylaşılmaz.",
            "Saha araç telemetry verileri yerel yer kontrol istasyonunda şifreli tutulur, izinsiz buluta aktarılmaz."
          ]
        }
      ]
    },
    en: {
      title: "Data Privacy Policy (KVKK & GDPR Compliance)",
      badge: "KVKK & GDPR COMPLIANT",
      subBadge: "PRIVACY v2.0",
      category: "DATA PRIVACY",
      summary: "Institutional inquiries and partner telemetry submitted to TRUSTIA Autonomous Systems are processed under rigorous KVKK and GDPR data protection frameworks.",
      sections: [
        {
          heading: "1. Data Controller & Protection Principles",
          items: [
            "Corporate contact information is utilized solely for technical evaluation and NDA partnership communication.",
            "Field telemetry and mission logs remain encrypted on local ground control hardware with zero unauthorized cloud egress."
          ]
        }
      ]
    }
  },
  gizlilik: {
    iconName: "Shield",
    tr: {
      title: "KVKK, GDPR ve Veri Gizliliği Politikası",
      badge: "KVKK & GDPR COMPLIANT",
      subBadge: "GİZLİLİK v2.0",
      category: "VERİ GİZLİLİĞİ",
      summary: "TRUSTIA platformunda toplanan kurumsal iletişim verileri KVKK ve GDPR kapsamında en yüksek güvenlik standartlarında işlenir.",
      sections: [
        {
          heading: "1. Veri Sorumlusu ve Gizlilik İlkeleri",
          items: [
            "Web sitemiz üzerinden iletilen kurumsal talepler 3. şahıslarla asla ticari amaçla paylaşılmaz.",
            "Saha araç telemetry verileri yerel yer kontrol istasyonunda şifreli tutulur, izinsiz buluta aktarılmaz."
          ]
        }
      ]
    },
    en: {
      title: "Data Privacy Policy (KVKK & GDPR Compliance)",
      badge: "KVKK & GDPR COMPLIANT",
      subBadge: "PRIVACY v2.0",
      category: "DATA PRIVACY",
      summary: "Institutional inquiries and partner telemetry submitted to TRUSTIA Autonomous Systems are processed under rigorous KVKK and GDPR data protection frameworks.",
      sections: [
        {
          heading: "1. Data Controller & Protection Principles",
          items: [
            "Corporate contact information is utilized solely for technical evaluation and NDA partnership communication.",
            "Field telemetry and mission logs remain encrypted on local ground control hardware with zero unauthorized cloud egress."
          ]
        }
      ]
    }
  }
};

export function generateStaticParams() {
  return Object.keys(policyData).map((slug) => ({ slug }));
}

export default async function PolicyPage({ params }: { params: Promise<{ slug: string }> }) {
  const resolvedParams = await params;
  const currentSlug = resolvedParams.slug;
  const policy = policyData[currentSlug];

  if (!policy) {
    notFound();
  }

  return (
    <PolicyDocumentView
      currentSlug={currentSlug}
      policy={policy}
      policyData={policyData}
    />
  );
}
