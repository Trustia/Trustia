"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import {
  ArrowLeft,
  CheckCircle2,
  ShieldCheck,
  ArrowRight,
  Printer,
  Download,
  FileText,
  Award,
  Lock,
  Scale,
  Globe,
  Shield,
  Clock,
  Building,
  ChevronRight
} from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

const iconMap: Record<string, any> = {
  FileText,
  Award,
  Lock,
  ShieldCheck,
  Scale,
  Globe,
  Shield,
};

export default function PolicyDocumentView({
  currentSlug,
  policy,
  policyData,
}: {
  currentSlug: string;
  policy: any;
  policyData: Record<string, any>;
}) {
  const { lang } = useLanguage();
  const IconComponent = iconMap[policy.iconName] || FileText;
  const activeData = policy[lang] || policy.tr;

  // Filter unique slugs for directory (avoid duplicate gizlilik/kvkk)
  const sidebarEntries = Object.entries(policyData).filter(([slug]) => slug !== "gizlilik");

  return (
    <main className="min-h-screen bg-gradient-to-b from-[#1c1813] via-[#28221a] to-[#1c1813] text-[#f5efe6] font-sans selection:bg-[#E4F80D] selection:text-black pt-28 sm:pt-36 pb-16 relative overflow-hidden">
      <Navbar />

      {/* Ambient Tactical Sand/Gold Glow */}
      <div className="absolute top-0 inset-x-0 h-[600px] bg-[radial-gradient(ellipse_at_top,rgba(229,214,188,0.10),transparent_70%)] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-8 space-y-6 sm:space-y-8">

        {/* 1. Header & Breadcrumb */}
        <div className="space-y-3 pb-6 border-b border-[#E5D6BC]/15">
          <div className="flex items-center gap-2 text-xs font-mono text-[#E5D6BC]/70">
            <Link href="/" className="hover:text-[#E5D6BC] flex items-center gap-1 transition-colors">
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>{lang === "tr" ? "Ana Sayfa" : "Home"}</span>
            </Link>
            <span>/</span>
            <span className="text-[#E5D6BC]/70">{lang === "tr" ? "POLİTİKALAR" : "POLICIES"}</span>
            <span>/</span>
            <span className="text-[#E5D6BC] font-semibold truncate">{activeData.category}</span>
          </div>

          <div className="flex flex-wrap items-center gap-2 pt-1">
            <span className="px-2.5 py-0.5 rounded bg-[#E5D6BC]/10 border border-[#E5D6BC]/25 text-[#E5D6BC] text-[10px] font-mono font-semibold uppercase tracking-wider">
              {activeData.category}
            </span>
            <span className="px-2.5 py-0.5 rounded bg-[#251f18] border border-[#E5D6BC]/20 text-[#E5D6BC] text-[10px] font-mono">
              {activeData.docNo}
            </span>
            <span className="px-2.5 py-0.5 rounded bg-[#251f18] border border-[#E5D6BC]/20 text-[#E5D6BC] text-[10px] font-mono">
              {activeData.subBadge}
            </span>
          </div>

          <h1 className="text-xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-snug">
            {activeData.title}
          </h1>

          <p className="text-[#d6cebf] text-xs sm:text-sm max-w-3xl leading-relaxed">
            {activeData.summary}
          </p>
        </div>

        {/* 
          2. Mobile-Only Horizontal Policy Tabs Strip
          (Allows mobile users to instantly switch policies without scrolling past a huge vertical list!)
        */}
        <div className="block lg:hidden">
          <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider mb-2 font-semibold flex items-center justify-between">
            <span>{lang === "tr" ? "TÜM KURUMSAL POLİTİKALAR" : "ALL CORPORATE POLICIES"}</span>
            <span className="text-[9px] text-slate-400">← {lang === "tr" ? "Kaydır" : "Swipe"} →</span>
          </div>
          <div className="flex overflow-x-auto gap-2 pb-2 no-scrollbar scrollbar-none">
            {sidebarEntries.map(([slug, item]) => {
              const isActive = slug === currentSlug || (slug === "kvkk" && currentSlug === "gizlilik");
              const itemData = item[lang] || item.tr;
              const ItemIcon = iconMap[item.iconName] || FileText;

              return (
                <Link
                  key={slug}
                  href={`/politika/${slug}/`}
                  className={`px-3 py-2 rounded-lg font-mono text-xs whitespace-nowrap shrink-0 flex items-center gap-1.5 transition-all border ${
                    isActive
                      ? "bg-[#E5D6BC] text-[#14120c] font-bold border-[#E5D6BC] shadow-md"
                      : "bg-[#251f18] text-[#E5D6BC]/80 border-[#E5D6BC]/20 hover:text-white"
                  }`}
                >
                  <ItemIcon className={`w-3.5 h-3.5 ${isActive ? "text-[#14120c]" : "text-[#E5D6BC]"}`} />
                  <span>{itemData.category}</span>
                </Link>
              );
            })}
          </div>
        </div>

        {/* 3. Main Document Layout: Left Sidebar (Desktop) + Right Document Content */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left Desktop Sidebar (4 Cols) */}
          <aside className="hidden lg:block lg:col-span-4 space-y-4">
            <div className="sticky top-28 p-5 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/20 space-y-3">
              <div className="flex items-center justify-between border-b border-[#E5D6BC]/20 pb-3">
                <span className="font-mono text-xs font-semibold text-[#E5D6BC] uppercase tracking-wider">
                  {lang === "tr" ? "KURUMSAL POLİTİKALAR" : "CORPORATE POLICIES"}
                </span>
                <span className="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded bg-[#18140e] border border-[#E5D6BC]/20 text-[#E5D6BC]">
                  {sidebarEntries.length} {lang === "tr" ? "DOKÜMAN" : "DOCS"}
                </span>
              </div>

              <nav className="space-y-1.5 font-mono text-xs">
                {sidebarEntries.map(([slug, item]) => {
                  const isActive = slug === currentSlug || (slug === "kvkk" && currentSlug === "gizlilik");
                  const ItemIcon = iconMap[item.iconName] || FileText;
                  const itemData = item[lang] || item.tr;

                  return (
                    <Link
                      key={slug}
                      href={`/politika/${slug}/`}
                      className={`flex items-center justify-between p-2.5 rounded-lg transition-all group ${
                        isActive
                          ? "bg-white text-slate-950 font-bold"
                          : "text-slate-400 hover:text-white hover:bg-slate-900 border border-transparent"
                      }`}
                    >
                      <div className="flex items-center gap-2.5 overflow-hidden">
                        <ItemIcon className={`w-4 h-4 shrink-0 ${isActive ? "text-[#14120c]" : "text-[#E5D6BC]"}`} />
                        <span className="truncate">{itemData.category}</span>
                      </div>
                      <ChevronRight className={`w-3.5 h-3.5 shrink-0 ${isActive ? "text-slate-950" : "opacity-0 group-hover:opacity-100"}`} />
                    </Link>
                  );
                })}
              </nav>

              {/* Official Registry Stamp */}
              <div className="pt-3 border-t border-[#E5D6BC]/20 text-[11px] text-slate-400 font-mono space-y-1.5">
                <div className="text-white font-semibold flex items-center gap-1.5">
                  <ShieldCheck className="w-4 h-4 text-emerald-400" />
                  <span>Resmi Hukuki Geçerlilik</span>
                </div>
                <div className="text-[10px] text-[#d6cebf]/80 leading-tight">
                  T.C. Kanunları, SAE J3016 ve ISO 26262 ASIL-D standartları uyarınca yürürlüktedir.
                </div>
              </div>
            </div>
          </aside>

          {/* Right Main Policy Content (8 Cols) */}
          <div className="lg:col-span-8 space-y-6">
            
            {/* Document Meta Ribbon */}
            <div className="p-4 sm:p-5 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/20 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs font-mono">
              <div className="flex items-center gap-3 text-slate-300">
                <div className="flex items-center gap-1.5">
                  <Building className="w-3.5 h-3.5 text-slate-400" />
                  <span>Trustia AI Legal & Compliance</span>
                </div>
                <span>•</span>
                <div className="flex items-center gap-1.5 text-slate-400">
                  <Clock className="w-3.5 h-3.5" />
                  <span>{lang === "tr" ? "Yürürlük:" : "Effective:"} {activeData.effectiveDate}</span>
                </div>
              </div>

              <div className="flex items-center gap-2">
                {(currentSlug === "oin-lisans" || currentSlug === "lisans" || currentSlug === "mulkiyet") && (
                  <a
                    href="/Trustia_OIN_Lisans_Sozlesmesi_2026.pdf"
                    target="_blank"
                    rel="noopener noreferrer"
                    download
                    className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded bg-[#E5D6BC] hover:bg-white text-[#14120c] font-bold text-[11px] transition-all shadow-md"
                  >
                    <Download className="w-3.5 h-3.5" />
                    <span>{lang === "tr" ? "İmzalı OIN Lisans PDF" : "Signed OIN License PDF"}</span>
                  </a>
                )}

                <button
                  onClick={() => typeof window !== "undefined" && window.print()}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded bg-[#18140e] hover:bg-[#251f18] border border-[#E5D6BC]/20 text-[#E5D6BC] hover:text-white transition-colors cursor-pointer text-[11px]"
                >
                  <Printer className="w-3.5 h-3.5" />
                  <span>{lang === "tr" ? "Yazdır / PDF" : "Print / PDF"}</span>
                </button>
              </div>
            </div>

            {/* Document Articles Sections */}
            <div className="space-y-4">
              {activeData.sections.map((sec: any, index: number) => (
                <div
                  key={index}
                  className="p-5 sm:p-7 rounded-2xl bg-[#251f18] border border-[#E5D6BC]/20 space-y-3.5"
                >
                  <h2 className="text-sm sm:text-base font-bold text-white tracking-tight flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-[#E5D6BC]"></span>
                    <span>{sec.heading}</span>
                  </h2>

                  <div className="space-y-2.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans pl-4 border-l-2 border-[#E5D6BC]/25">
                    {sec.items.map((itemText: string, iIdx: number) => (
                      <p key={iIdx} className="text-[#d6cebf]">
                        {itemText}
                      </p>
                    ))}
                  </div>
                </div>
              ))}
            </div>

            {/* Official Closing Compliance Box */}
            <div className="p-5 rounded-2xl bg-[#1b1610] border border-[#E5D6BC]/20 text-xs text-slate-400 space-y-2">
              <div className="font-semibold text-white flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>{lang === "tr" ? "Resmi Yürürlük ve İletişim" : "Official Notice & Contact"}</span>
              </div>
              <p className="leading-relaxed">
                {lang === "tr"
                  ? "Bu kurumsal politika dokümanı, Trustia AI Yönetim Kurulu ve Hukuk Müşavirliği tarafından onaylanarak yürürlüğe konulmuştur. Sözleşme, lisanslama ve uyumluluk talepleriniz için doğrudan 'hukuk@trustia.com.tr' adresi ile iletişime geçebilirsiniz."
                  : "This institutional policy document is formally certified and enacted by the Trustia AI Executive Board and Legal Directorate. For licensing, OEM compliance, and legal inquiries, contact 'hukuk@trustia.com.tr'."}
              </p>
            </div>

          </div>

        </div>

      </div>

      <Footer />
    </main>
  );
}
