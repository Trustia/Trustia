import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { ArrowLeft, Shield, Cpu, Target, Award, CheckCircle2, Lock, Terminal, Radio } from "lucide-react";

export const metadata = {
  title: "Hakkımızda | TRUSTIA AI — Savunma Sanayii Otonomi Yazılım Çekirdeği",
  description: "TRUSTIA TEKNOLOJİ kurumsal profil, askeri otonomi yazılımı mimarisi, STANAG 4586 uyumluluğu ve yerli Ar-Ge vizyonu. İstanbul, Türkiye.",
};

export default function AboutPage() {
  return (
    <main className="min-h-screen bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black">
      <Navbar />

      {/* Hero Header */}
      <section className="pt-32 pb-16 px-6 bg-[#0b0e14] border-b border-white/10 relative overflow-hidden">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none" />

        <div className="max-w-6xl mx-auto relative z-10">
          <div className="flex flex-col items-start gap-3 mb-6">
            <Link
              href="/"
              className="inline-flex items-center gap-2 text-xs font-mono text-slate-400 hover:text-[#C8FF00] transition-colors group"
            >
              <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
              <span>← ANA SAYFAYA DÖN</span>
            </Link>

            <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 text-xs font-mono font-bold tracking-wider uppercase">
              <span>KURUMSAL PROFİL & MİMARİ VİZYON</span>
            </div>
          </div>

          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight mb-4">
            Trustia Teknoloji Otonomi Çekirdeği
          </h1>
          <p className="text-slate-400 text-sm sm:text-base max-w-3xl font-normal leading-relaxed">
            İnsansız Kara Araçları (İKA) için askeri standartlarda %100 yerli ve özgün otonomi yazılım altyapısı geliştiren yüksek teknoloji mühendislik kuruluşu.
          </p>
        </div>
      </section>

      {/* Executive Summary Grid */}
      <section className="py-16 px-6 max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
          <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
            <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
              <Shield className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white tracking-tight">
              Stratejik Bağımsızlık
            </h3>
            <p className="text-slate-400 text-xs leading-relaxed">
              Yabancı bağımlılığı sıfır olan kütüphane altyapısı ve %100 özgün kaynak kod mülkiyeti ile milli savunma gereksinimlerine tam uyum.
            </p>
          </div>

          <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
            <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
              <Cpu className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white tracking-tight">
              Donanımdan Bağımsız RTOS
            </h3>
            <p className="text-slate-400 text-xs leading-relaxed">
              ROS2 ve CAN-Bus mimarileri üzerinde çalışan, paletli ve tekerlekli tüm kara platformlarına modüler entegrasyon yeteneği.
            </p>
          </div>

          <div className="p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/30 transition-colors">
            <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 w-fit">
              <Award className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white tracking-tight">
              STANAG & JAUS Standartları
            </h3>
            <p className="text-slate-400 text-xs leading-relaxed">
              STANAG 4586 Level 4 ve SAE AS6091 JAUS protokolleri ile NATO standartlarında komuta kontrol entegrasyonu.
            </p>
          </div>
        </div>

        {/* Corporate Profile Narrative */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start mb-16">
          <div className="lg:col-span-7 space-y-6 text-slate-300 text-sm leading-relaxed">
            <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mb-4 border-l-2 border-[#C8FF00] pl-4">
              Milli Savunma İçin Derin Mühendislik
            </h2>

            <p>
              <strong className="text-white">TRUSTIA TEKNOLOJİ</strong>, savunma sanayii ve otonom kara sistemleri alanında kritik yazılım katmanları geliştirmek amacıyla kurulmuştur. Odak noktamız, GPS sinyallerinin engellendiği, elektronik harp koşullarının hüküm sürdüğü zorlu saha ortamlarında kara araçlarının kendi kararlarını güvenle alabilmesini sağlamaktır.
            </p>

            <p>
              Geliştirdiğimiz otonomi mimarisi, donanım üreticilerinden bağımsız bir yazılım katmanı (Core Middleware) olarak çalışır. Görsel Odometri, LiDAR tabanlı 3D SLAM ve Tehdit Algılama algoritmalarımız; 1.200 saatin üzerindeki zorlu saha ve iklim testleriyle doğrulanmıştır.
            </p>

            <div className="p-6 rounded-xl bg-[#0c1017] border border-white/10 space-y-3 font-mono text-xs text-slate-400 my-6">
              <div className="flex items-center gap-2 text-[#C8FF00] font-bold uppercase">
                <Terminal className="w-4 h-4" />
                <span>MÜHENDİSLİK İLKELERİMİZ</span>
              </div>
              <ul className="space-y-2 list-disc list-inside text-slate-300">
                <li>Dış Bağımsızlık: Üçüncü taraf yabancı kütüphanelere sıfır bağımlılık.</li>
                <li>Gerçek Zamanlı Determinizma: RTOS üzerinde mikro saniye hassasiyetli döngüler.</li>
                <li>Siber Dayanıklılık: Donanım düzeyinde HSM kütüphaneleri ve 256-bit şifreleme.</li>
              </ul>
            </div>
          </div>

          {/* Technical Certifications Sidebar */}
          <div className="lg:col-span-5 p-8 rounded-2xl bg-[#0c1017] border border-white/10 space-y-6">
            <h3 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider border-b border-white/10 pb-3">
              STANDARTLAR & SERTİFİKASYONLAR
            </h3>

            <div className="space-y-4 font-mono text-xs">
              <div className="p-4 rounded-xl bg-white/[0.02] border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-bold">
                  <span>STANAG 4586 Level 4</span>
                  <span className="text-[#C8FF00]">Uyumlu</span>
                </div>
                <p className="text-slate-500 text-[11px]">NATO İnsansız Sistem Komuta Kontrol Protokolü</p>
              </div>

              <div className="p-4 rounded-xl bg-white/[0.02] border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-bold">
                  <span>SAE AS6091 JAUS</span>
                  <span className="text-[#C8FF00]">Uyumlu</span>
                </div>
                <p className="text-slate-500 text-[11px]">Açık Mimari İnsansız Kara Aracı Mimarisi</p>
              </div>

              <div className="p-4 rounded-xl bg-white/[0.02] border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-bold">
                  <span>ISO 26262 ASIL-D</span>
                  <span className="text-[#C8FF00]">Sertifikalı</span>
                </div>
                <p className="text-slate-500 text-[11px]">Fonksiyonel Güvenlik ve Hata Tolerans Mimari</p>
              </div>

              <div className="p-4 rounded-xl bg-white/[0.02] border border-white/5 space-y-1">
                <div className="flex items-center justify-between text-white font-bold">
                  <span>5746 & 5846 Kanunları</span>
                  <span className="text-[#C8FF00]">T.C. Lisanslı</span>
                </div>
                <p className="text-slate-500 text-[11px]">Yerli Ar-Ge ve Özgün Telif Hakları Koruması</p>
              </div>
            </div>
          </div>
        </div>

        {/* Corporate CTA Banner */}
        <div className="p-8 sm:p-12 rounded-2xl bg-[linear-gradient(135deg,#0c1017_0%,#131a26_100%)] border border-white/10 flex flex-col sm:flex-row items-center justify-between gap-6">
          <div className="space-y-2">
            <h4 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              Saha Testleri & Entegrasyon İşbirliği
            </h4>
            <p className="text-slate-400 text-xs sm:text-sm max-w-xl">
              Platformunuza yerli otonomi çekirdeği entegre etmek veya ortak Ar-Ge projesi yürütmek için doğrudan iletişim ekibimize ulaşın.
            </p>
          </div>
          <Link
            href="/iletisim"
            className="px-6 py-3 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase hover:bg-[#d4ff33] transition-colors shrink-0"
          >
            İLETİŞİME GEÇİN
          </Link>
        </div>
      </section>

      <Footer />
    </main>
  );
}
