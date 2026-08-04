import PolicyDocumentView from "@/components/PolicyDocumentView";
import { notFound } from "next/navigation";

export const policyData: Record<string, {
  title: string;
  badge: string;
  subBadge: string;
  category: string;
  iconName: string;
  content: {
    summary: string;
    sections: {
      heading: string;
      items: string[];
    }[];
  };
}> = {
  lisans: {
    title: "Otonomi Yazılım Lisanslama ve Kullanım Şartları (EULA / SLA)",
    badge: "SOFTWARE-ONLY SLA",
    subBadge: "LİSANS v2.0",
    category: "YAZILIM LİSANSLAMA",
    iconName: "FileText",
    content: {
      summary: "Bu lisans sözleşmesi, TRUSTIA TEKNOLOJİ tarafından geliştirilen TRUSTIA otonomi yazılım çekirdeğinin, İnsansız Kara Aracı (İKA) donanım üreticileri ve entegratörleri tarafından kullanım şartlarını düzenler. TRUSTIA, araç fiziki donanımı üretmeyip sadece otonomi yazılım beynini lisanslar.",
      sections: [
        {
          heading: "1. Lisans Kapsamı ve Münhasırlık",
          items: [
            "TRUSTIA yazılım çekirdeği, üretici firmanın İnsansız Kara Aracı (İKA) platformu için gayri-münhasır (non-exclusive), devredilemez ve gayri-kabill-i rücu otonom kullanım lisansı olarak tahsis edilir.",
            "Tüm yazılım kaynak kodları, otonomi algoritmaları, 3D SLAM kütüphaneleri ve sürü zekası modelleri TRUSTIA TEKNOLOJİ mülkiyetindedir.",
            "Lisans alan entegratör firma, yazılımı tersine mühendislik (reverse engineering) işlemine tabi tutamaz, kopyalayamaz veya üçüncü taraflara alt lisans olarak devredemez."
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
            "Kritik güvenlik güncellemeleri ve siber yamalar lisans süresince 7/24 kesintisiz olarak yayınlanır.",
            "Saha görevlerinde karşılaşılan algoritmik istisnalar için 48 saat içerisinde teknik destek ve kütük (log) analizi sağlanır."
          ]
        }
      ]
    }
  },
  yerlilik: {
    title: "%100 Yerli Katkı ve Sertifikasyon Taahhüdü",
    badge: "5746 SAYILI KANUN UNVANLI",
    subBadge: "SERTİFİKA v2.0",
    category: "MİLLİ TEKNOLOJİ",
    iconName: "Award",
    content: {
      summary: "TRUSTIA TEKNOLOJİ, geliştirdiği tüm otonomi algoritmaları ve karar destek sistemlerinde %100 yerli katkı oranına uymayı ve Türk Savunma Sanayii standartlarında bağımsız çalışmayı taahhüt eder.",
      sections: [
        {
          heading: "1. Sıfır Dış Bağımlılık ve Algoritma Bağımsızlığı",
          items: [
            "Yazılım mimarimiz, açık kaynak kodlu veya yabancı menşeili hazır kütüphanelere doğrudan bağımlı olmadan Türk mühendislerince geliştirilmiştir.",
            "GPS kısıtlaması veya yabancı uydu bağımlılığı olan harekat sahalarında tamamen yerel sensör füzyonu (LiDAR, Termal Kameralar, IMU) ile görev icra eder.",
            "Yurtdışı ambargolarından veya lisans iptallerinden etkilenmeyecek yerli kaynak kod mimarisine sahiptir."
          ]
        },
        {
          heading: "2. Savunma Sanayii Sertifikasyon Uyumları",
          items: [
            "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı (SSB) yerlilik kriterlerine tam uyumludur.",
            "SAE AS9100 Havacılık ve Savunma Kalite Yönetimi standartları esas alınarak kodlanmıştır.",
            "STANAG 4586 Level 4 ve SAE AS6091 JAUS (Joint Architecture for Unmanned Systems) haberleşme standartlarına sahiptir."
          ]
        }
      ]
    }
  },
  siber: {
    title: "Askeri Siber Güvenlik ve Veri Muhafazası",
    badge: "HMAC-SHA256 ENCRYPTED",
    subBadge: "GÜVENLİK v2.0",
    category: "SİBER GÜVENLİK",
    iconName: "Lock",
    content: {
      summary: "TRUSTIA otonom karar mekanizmaları, askeri düzeyde kriptografik şifreleme ve sahadaki sinyal kesintilerine (Jamming/Spoofing) karşı yüksek dirençli Fail-Safe protokolleri ile korunur.",
      sections: [
        {
          heading: "1. Kriptografik Komut Doğrulama ve E-Stop",
          items: [
            "Yer Kontrol İstasyonundan (GCS) araca iletilen tüm otonomi ve rota komutları HMAC-SHA256 algoritması ile anlık imzalanır.",
            "Yetkisiz araya girme (Man-in-the-Middle) veya sahte komut paketleri sistem tarafından anında reddedilir ve araç güvenli moda geçer.",
            "Donanımsal ve yazılımsal Acil Durdurma (E-Stop) sinyali en yüksek öncelikli kesme (interrupt) olarak işlenir."
          ]
        },
        {
          heading: "2. LinkLoss ve Eve Dönüş (RTH) Protokolü",
          items: [
            "Telsiz haberleşmesinin veya veri bağının koptuğu durumlarda araç 3 saniye içerisinde otomatik LinkLoss durumuna geçer.",
            "Araç, 3D SLAM haritasındaki geçmiş pozitif rotasını izleyerek otonom olarak kalkış noktasına (Home Base) geri döner."
          ]
        }
      ]
    }
  },
  etik: {
    title: "Otonom Silah Sistemleri ve Yapay Zeka Etik Bildirgesi",
    badge: "HUMAN-IN-THE-LOOP",
    subBadge: "ETİK v2.0",
    category: "SİSTEM ETİĞİ",
    iconName: "ShieldCheck",
    content: {
      summary: "TRUSTIA TEKNOLOJİ, geliştirdiği otonom yazılımlarda İnsan Denetiminde Harekat (Human-in-the-Loop) prensibini kesin kural olarak uygular.",
      sections: [
        {
          heading: "1. İnsani Denetim ve Hedef Angajman Sınırı",
          items: [
            "TRUSTIA otonomi yazılımı; rotalama, engel kaçınma, haritalama ve tehdit tespiti işlevlerini otonom icra eder.",
            "Kinetik etki veya silah angajmanı gerektiren hiçbir karar yapay zeka tarafından otonom olarak verilemez; yetki tamamen insan komutandadır.",
            "Cenevre Sözleşmesi ve Uluslararası İnsani Hukuk kurallarına uygun olarak geliştirilmiştir."
          ]
        },
        {
          heading: "2. Sürü Zekası Güvenlik Çerçevesi",
          items: [
            "Sürü halindeki araçlar birbirlerinin konumlarını anlık doğrular ve dost unsur çatışmasını (Fratricide) engelleyen çarpışma önleme algoritmaları çalıştırır."
          ]
        }
      ]
    }
  },
  mulkiyet: {
    title: "Fikri ve Sınai Mülkiyet Hakları & Telif Bildirimi",
    badge: "5846 SAYILI KANUN UNVANLI",
    subBadge: "MÜLKİYET v2.0",
    category: "FİKRİ MÜLKİYET",
    iconName: "Scale",
    content: {
      summary: "TRUSTIA web sitesi, markası, yazılım kodları, 3D SLAM algoritmaları ve görsel materyalleri 5846 sayılı Fikir ve Sanat Eserleri Kanunu ile koruma altındadır.",
      sections: [
        {
          heading: "1. Telif Hakları ve Marka Tescili",
          items: [
            "TRUSTIA ve TRUSTIA AI markaları, logosu, web sitesi tasarımı ve yazılım mimarisi TRUSTIA TEKNOLOJİ'nin tescilli mülküdür.",
            "İzinsiz kopyalanamaz, çoğaltılamaz, dağıtılamaz veya başka bir ticari marka altında sunulamaz.",
            "Sitede yer alan askeri İKA görselleri, videoları ve teknik dokümanlar izinsiz kaynak gösterilerek dahi kullanılamaz."
          ]
        },
        {
          heading: "2. Yasal Yaptırımlar ve İhlal Bildirimi",
          items: [
            "Fikri mülkiyet ihlallerinde T.C. Fikri ve Sınai Haklar Hukuk Mahkemeleri nezdinde cezai ve hukuki süreç başlatılır."
          ]
        }
      ]
    }
  },
  ihracat: {
    title: "Savunma Sanayii İhracat ve Teknoloji Transferi (Yasal Uyum)",
    badge: "5201 SAYILI KANUN UNVANLI",
    subBadge: "İHRACAT v2.0",
    category: "YASAL UYUM",
    iconName: "Globe",
    content: {
      summary: "TRUSTIA yazılım ürünlerinin yurt dışına ihracatı ve teknoloji transferi T.C. Milli Savunma Bakanlığı (MSB) ve Savunma Sanayii Başkanlığı (SSB) izinlerine tabidir.",
      sections: [
        {
          heading: "1. İhracat Kontrolü ve MSB İzinleri",
          items: [
            "5201 sayılı Harp Araç ve Gereçleri ile Silah, Mühimmat ve Patlayıcı Madde Üreten Sanayi Kuruluşlarının Denetimi Hakkında Kanun uyarınca hareket edilir.",
            "Yurt dışı donanım üreticilerine veya yabancı askeri kurumlara yapılacak yazılım satışları T.C. resmi makamlarının onayına bağlıdır.",
            "Ambargolu veya yaptırım listesindeki ülkelere hiçbir koşulda teknoloji transferi yapılmaz."
          ]
        }
      ]
    }
  },
  kvkk: {
    title: "KVKK ve Gizlilik Bildirimi (6698 Sayılı Kanun Uyumlu)",
    badge: "6698 SAYILI KVKK UNVANLI",
    subBadge: "GİZLİLİK v2.0",
    category: "VERİ GİZLİLİĞİ",
    iconName: "Shield",
    content: {
      summary: "TRUSTIA platformunda toplanan kurumsal iletişim verileri ve saha araç logları 6698 sayılı KVKK kapsamında işlenir ve saklanır.",
      sections: [
        {
          heading: "1. Veri Sorumlusu ve Veri Güvenliği",
          items: [
            "TRUSTIA TEKNOLOJİ, KVKK kapsamında Veri Sorumlusu sıfatıyla hareket eder.",
            "Web sitesi üzerinden iletilen kurumsal e-posta ve iletişim talepleri 3. şahıslarla asla paylaşılmaz.",
            "Saha araç telemetry ve görev log verileri yerel kara kontrol istasyonunda şifreli tutulur, buluta aktarılmaz."
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
