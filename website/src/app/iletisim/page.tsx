import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import CorporateContactForm from "@/components/CorporateContactForm";
import Link from "next/link";
import { ArrowLeft, Mail, MapPin, Clock } from "lucide-react";

export const metadata = {
  title: "İletişim | TRUSTIA AI — Kurumsal İletişim & Entegrasyon",
  description: "TRUSTIA TEKNOLOJİ kurumsal iletişim, otonomi yazılımı entegrasyon talepleri ve saha test koordinasyon kanalları. İstanbul, Türkiye.",
};

export default function ContactPage() {
  return (
    <main className="min-h-screen bg-[#090b0e] text-white font-sans selection:bg-[#C8FF00] selection:text-black">
      <Navbar />

      {/* Hero Header */}
      <section className="pt-32 pb-12 px-6 bg-[#0b0e14] border-b border-white/10 relative overflow-hidden">
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
              <span>RESMİ İLETİŞİM KANALLARI</span>
            </div>
          </div>

          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight leading-tight mb-3">
            Kurumsal İletişim & Entegrasyon
          </h1>
          <p className="text-slate-400 text-sm sm:text-base max-w-2xl font-normal leading-relaxed">
            İnsansız Kara Aracı (İKA) otonomi yazılımı lisanslama, donanım entegrasyonu ve saha demo talepleriniz için doğrudan teknik ekibimizle iletişime geçin.
          </p>
        </div>
      </section>

      {/* Main Content Layout */}
      <section className="py-16 px-6 max-w-6xl mx-auto font-sans">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          {/* Left Column: Contact Cards & Email Addresses */}
          <div className="lg:col-span-5 space-y-6">
            
            {/* Primary Email Card */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 hover:border-[#C8FF00]/40 transition-colors">
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <Mail className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">GENEL İLETİŞİM</h4>
                  <a
                    href="mailto:iletisim@trustia.com.tr"
                    className="text-base sm:text-lg font-bold text-white hover:text-[#C8FF00] transition-colors font-mono"
                  >
                    iletisim@trustia.com.tr
                  </a>
                </div>
              </div>
              <p className="text-slate-400 text-xs leading-relaxed border-t border-white/10 pt-3">
                Cloudflare kurumsal e-posta yönlendirme altyapısı ile tüm iletiler doğrudan nöbetçi mühendislik ekibimize ulaşır.
              </p>
            </div>

            {/* Department Email Addresses */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4">
              <h5 className="font-mono text-xs font-bold text-white uppercase tracking-wider border-b border-white/10 pb-3">
                DEPARTMAN E-POSTA ADRESLERİ
              </h5>

              <div className="space-y-3 font-mono text-xs">
                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">Teknik Entegrasyon:</span>
                  <a href="mailto:entegrasyon@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    entegrasyon@trustia.com.tr
                  </a>
                </div>

                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">Kariyer & İK:</span>
                  <a href="mailto:kariyer@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    kariyer@trustia.com.tr
                  </a>
                </div>

                <div className="flex items-center justify-between p-3 rounded-xl bg-white/[0.02] border border-white/5">
                  <span className="text-slate-400">Hukuk & Lisanslama:</span>
                  <a href="mailto:hukuk@trustia.com.tr" className="text-[#C8FF00] font-bold hover:underline">
                    hukuk@trustia.com.tr
                  </a>
                </div>
              </div>
            </div>

            {/* Location & Working Hours */}
            <div className="p-6 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4">
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-xl bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30">
                  <MapPin className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="font-mono text-xs font-bold text-[#C8FF00] uppercase tracking-wider">GENEL MERKEZ & AR-GE</h4>
                  <div className="text-sm font-bold text-white font-mono">
                    İstanbul, Türkiye
                  </div>
                </div>
              </div>

              <div className="flex items-center gap-3 border-t border-white/10 pt-4 text-xs font-mono text-slate-400">
                <Clock className="w-4 h-4 text-[#C8FF00] shrink-0" />
                <span>Pazartesi — Cuma: 09:00 - 18:00 (TSİ)</span>
              </div>
            </div>

          </div>

          {/* Right Column: Executive Form */}
          <div className="lg:col-span-7">
            <div className="p-8 sm:p-10 rounded-2xl bg-[#0c1017] border border-white/10 shadow-2xl">
              <div className="mb-6">
                <h3 className="text-2xl font-bold text-white tracking-tight mb-2">
                  Entegrasyon & Destek Formu
                </h3>
                <p className="text-slate-400 text-xs sm:text-sm">
                  Projeniz için teknik gereksinimlerinizi iletin, mühendislik ekibimiz 24 saat içinde dönüş yapsın.
                </p>
              </div>

              <CorporateContactForm />
            </div>
          </div>

        </div>
      </section>

      <Footer />
    </main>
  );
}
