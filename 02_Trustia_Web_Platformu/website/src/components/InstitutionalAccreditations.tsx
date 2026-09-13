"use client";

import { useState } from "react";
import Image from "next/image";
import { ShieldCheck, CheckCircle2, Award, ChevronDown, Building2 } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { lang } = useLanguage();
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleAccordion = (idx: number) => {
    setOpenIndex(openIndex === idx ? null : idx);
  };

  const faqItems = [
    {
      flag: "🇪🇺",
      institutionTr: "Avrupa Komisyonu",
      institutionEn: "European Commission",
      badgeTr: "PIC: 861711529",
      badgeEn: "PIC: 861711529",
      badgeColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
      questionTr: "Trustia projesi Avrupa Birliği tarafından resmi olarak tanınıyor mu?",
      questionEn: "Is Trustia officially recognized by the European Union?",
      answerTr: "Evet. Trustia Teknoloji A.Ş., Avrupa Komisyonu Katılımcı Kayıt Defteri'ne (Participant Register) resmi olarak tescil edilmiş olup 9 haneli Avrupa Birliği Katılımcı Kimlik Kodu (PIC: 861711529) kalıcı olarak tahsis edilmiştir. Bu akreditasyon, Trustia'nın Horizon Europe ve EIC hibe/ihale konsorsiyumlarına doğrudan lider tüzel kişilik olarak katılımını yasal güvenceye bağlamıştır.",
      answerEn: "Yes. Trustia Technology has been officially registered in the European Commission's Participant Register with an assigned 9-digit EU Participant Identification Code (PIC: 861711529). This legal accreditation qualifies Trustia as an eligible lead entity for Horizon Europe and European Innovation Council (EIC) deep-tech research and grant consortiums.",
      authority: "ec.europa.eu",
      typeTr: "Resmi AB Tüzel Kişilik Tescili",
      typeEn: "Official EU Legal Entity Registration"
    },
    {
      flag: "🇪🇺",
      institutionTr: "EIT Urban Mobility",
      institutionEn: "EIT Urban Mobility",
      badgeTr: "Partner: CUS15554",
      badgeEn: "Partner: CUS15554",
      badgeColor: "text-[#C8FF00] bg-[#C8FF00]/10 border-[#C8FF00]/30",
      questionTr: "EIT Urban Mobility ortaklığı ve 100.000 € hibe süreci ne durumdadır?",
      questionEn: "What is the status of the EIT Urban Mobility partnership and €100k grant?",
      answerTr: "Trustia, Avrupa İnovasyon ve Teknoloji Enstitüsü (EIT) resmi NetSuite PIF portalında onaylanarak CUS15554 resmi Partner ID'sini almıştır. 'Girişimcilere Mali Destek 26-28' çağrısı kapsamında 100.000 € doğrudan finansman ve Avrupa otonomi test pisti hibesi (Başvuru No: 3.1.02-1206-3732.3) resmi onay ve değerlendirme aşamasındadır.",
      answerEn: "Trustia has been officially approved on the European Institute of Innovation & Technology (EIT) NetSuite PIF portal under Partner ID CUS15554. Trustia's €100,000 equity-free grant and European autonomous test track deployment application (Application ID: 3.1.02-1206-3732.3) under the 'Financial Support for Entrepreneurs 26-28' call is actively in evaluation.",
      authority: "eiturbanmobility.eu",
      typeTr: "Hibe & Test Pisti Finansmanı",
      typeEn: "Grant & Proving Ground Funding"
    },
    {
      flag: "🇶🇦",
      institutionTr: "Katar QSTP (Qatar Foundation)",
      institutionEn: "Qatar QSTP (Qatar Foundation)",
      badgeTr: "30M$ Fon + Sprint",
      badgeEn: "$30M Fund + Sprint",
      badgeColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
      questionTr: "Katar Bilim ve Teknoloji Parkı (QSTP) ile hangi programlar yürütülüyor?",
      questionEn: "What programs are being conducted with Qatar Science & Technology Park (QSTP)?",
      answerTr: "Katar Vakfı (Qatar Foundation) bünyesindeki QSTP'ye iki yönlü resmi müracaat yapılmıştır: 30 Milyon Dolar bütçeli QSTP Tech Venture Fonu kapsamında 500.000 $ Pre-Seed yatırım başvurusu (9 sayfa) ve 4 haftalık yerinde Doha Sprint kuluçka rezidansı (8 sayfa, fiziki ofis, executive konaklama ve Katar şirket tescili desteği). Dosyalar resmi kabul alarak incelemeye girmiştir.",
      answerEn: "A two-tier official application has been submitted to QSTP under Qatar Foundation: a $500,000 Pre-Seed SAFE investment under the $30M Tech Venture Fund (9-page form), and the 4-week in-person Doha Sprint incubation residency (8-page form), providing enterprise office facilities, executive accommodations, and Qatari corporate entity establishment.",
      authority: "qstp.org.qa",
      typeTr: "Venture Fon & Doha Rezidansı",
      typeEn: "Venture Fund & Doha Residency"
    },
    {
      flag: "🇹🇷",
      institutionTr: "BAYKAR Teknoloji",
      institutionEn: "BAYKAR Technology",
      badgeTr: "Tedarikçi Kaydı",
      badgeEn: "Supplier Registry",
      badgeColor: "text-cyan-400 bg-cyan-500/10 border-cyan-500/30",
      questionTr: "BAYKAR Teknoloji tedarikçi ve alt yüklenici değerlendirmesi ne aşamadadır?",
      questionEn: "What is the status of the BAYKAR Tech defense supplier evaluation?",
      answerTr: "BAYKAR Teknoloji Resmi Alt Yüklenici ve Tedarikçi Portalı'na Trustia Seviye-4 otonom seyrüsefer çekirdeği, GNSS-denied (uydu sinyalsiz) 3D LiDAR SLAM haritalama motoru ve taktik İKA (İnsansız Kara Aracı) alt sistemleri ile resmi tedarikçi kaydı eksiksiz yapılmış; teknik dosya onaylanarak savunma tedarikçi havuzuna alınmıştır.",
      answerEn: "Trustia's Level-4 deterministic autonomy core, GNSS-denied 3D LiDAR SLAM localization engine, and tactical UGV algorithmic subsystems have been officially registered and verified in the BAYKAR Technology Supplier Portal for defense robotics subcontracting.",
      authority: "baykartech.com",
      typeTr: "Savunma Sanayii Alt Yüklenici",
      typeEn: "Defense Robotics Subcontractor"
    },
    {
      flag: "🇹🇷",
      institutionTr: "ASELSAN Portalı",
      institutionEn: "ASELSAN Portal",
      badgeTr: "#0050569CCE941FD1",
      badgeEn: "#0050569CCE941FD1",
      badgeColor: "text-amber-400 bg-amber-500/10 border-amber-500/30",
      questionTr: "ASELSAN Tedarikçi Portalı'ndaki resmi kayıt ve kapsam nedir?",
      questionEn: "What is the scope of Trustia's ASELSAN defense supplier candidacy?",
      answerTr: "ASELSAN Tedarikçi Portalı üzerinden 0050569CCE941FD1A49FCEFB9B7BE7D6 resmi takip numarası ile; 'Yazılım Geliştirme', 'Sistem Platform Entegrasyonu' ve 'Kara Platform Entegrasyonu' kategorilerinde ön değerlendirme ve kurumsal tedarikçi denetim süreci yürütülmektedir.",
      answerEn: "Registered under official evaluation reference 0050569CCE941FD1A49FCEFB9B7BE7D6 on the ASELSAN Supplier Portal, spanning three critical capability codes: Software Engineering, Autonomous System Integration, and Land Platform Combat Integration.",
      authority: "partner.aselsan.com.tr",
      typeTr: "Kara Platformu & Otonomi Entegrasyonu",
      typeEn: "Land Platform & Autonomy Integration"
    },
    {
      flag: "🇹🇷",
      institutionTr: "SSB SAYZEK",
      institutionEn: "SSB SAYZEK",
      badgeTr: "Başvuru #170",
      badgeEn: "Application #170",
      badgeColor: "text-amber-400 bg-amber-500/10 border-amber-500/30",
      questionTr: "Savunma Sanayii Başkanlığı SAYZEK Yapay Zekâ Platformu entegrasyonu nedir?",
      questionEn: "What is the SSB SAYZEK Artificial Intelligence Platform integration?",
      answerTr: "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı Yapay Zekâ Platformu (SAYZEK) Simport Simülasyon Altyapısı'na 170 numaralı resmi başvuru ile katılım sağlanmıştır. Trustia'nın 16.000+ satırlık deterministik otonomi mimarisi ve askeri tehdit algılama modelleri, savunma sanayii süper bilgisayar kümesinde onay aşamasındadır.",
      answerEn: "Officially registered under Application #170 on the Presidency of Defense Industries (SSB) Artificial Intelligence Platform (SAYZEK) Simport simulation infrastructure, qualifying Trustia's deterministic autonomy architecture for defense supercomputing clusters.",
      authority: "sayzek.ssb.gov.tr",
      typeTr: "Milli Otonomi Simülasyonu",
      typeEn: "National Autonomy Simulation"
    },
    {
      flag: "🇺🇸",
      institutionTr: "Z Fellows (San Francisco)",
      institutionEn: "Z Fellows (San Francisco)",
      badgeTr: "Mülakat: 17 Eylül",
      badgeEn: "Interview: Sep 17",
      badgeColor: "text-purple-400 bg-purple-500/10 border-purple-500/30",
      questionTr: "Silikon Vadisi Z Fellows programı ve Pace Capital mülakatı nedir?",
      questionEn: "What is the Silicon Valley Z Fellows fellowship and Pace Capital interview?",
      answerTr: "Dünyanın en seçkin genç teknoloji kurucularını Silikon Vadisi'ne taşıyan Z Fellows programında Trustia, Pace Capital Partneri Grace Kasten ile 17 Eylül 2026 tarihinde 10 dakikalık canlı Zoom partner mülakatı aşamasına seçilmiştir. Program 10.000 $ hissesiz hibe ve San Francisco hızlandırma rezidansı sunmaktadır.",
      answerEn: "Trustia was selected for the final live Zoom partner interview on September 17, 2026, with Grace Kasten (Partner at Pace Capital) for Z Fellows in San Francisco, providing an equity-free $10,000 grant and an intensive Silicon Valley founder residency.",
      authority: "zfellows.com",
      typeTr: "Silikon Vadisi Hibe & Hızlandırma",
      typeEn: "Silicon Valley Grant & Acceleration"
    },
    {
      flag: "🇹🇷",
      institutionTr: "DEİK İş Konseyi",
      institutionEn: "DEİK Business Council",
      badgeTr: "Onaylandı",
      badgeEn: "Approved",
      badgeColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
      questionTr: "DEİK bünyesindeki kurumsal temsil ve otonomi ihracat misyonu nedir?",
      questionEn: "What is Trustia's corporate engagement with DEİK?",
      answerTr: "T.C. Ticaret Bakanlığı koordinasyonunda faaliyet gösteren Dış Ekonomik İlişkiler Kurulu (DEİK) 'Dijital Teknolojiler İş Konseyi' bünyesine resmi başvuru tamamlanmıştır. Trustia, Türkiye'nin yerli otonom mobilite ve robotaksi yazılım ihracatını Körfez, Avrupa ve Asya pazarlarında temsil etme misyonunu üstlenmiştir.",
      answerEn: "Trustia has completed official registration with the Foreign Economic Relations Board of Turkey (DEİK) Digital Technologies Business Council under the Ministry of Trade, driving international deployment and commercial export of Turkish autonomous mobility software.",
      authority: "deik.org.tr",
      typeTr: "Ticari Diplomasi & Teknoloji İhracatı",
      typeEn: "Commercial Diplomacy & Tech Export"
    },
    {
      flag: "🇦🇪",
      institutionTr: "Dubai RTA World Challenge",
      institutionEn: "Dubai RTA World Challenge",
      badgeTr: "1.2M$ Yarışma",
      badgeEn: "$1.2M Challenge",
      badgeColor: "text-cyan-400 bg-cyan-500/10 border-cyan-500/30",
      questionTr: "Dubai RTA 1.2 Milyon Dolarlık Robotaksi yarışması ne durumdadır?",
      questionEn: "What is the status of the $1.2M Dubai RTA Self-Driving Transport Challenge?",
      answerTr: "Dubai Yollar ve Ulaşım Otoritesi (RTA) tarafından düzenlenen 1.200.000 $ nakit ödüllü küresel Seviye-4 Robotaksi yarışmasına Hyundai Ioniq 5 retrofit mimarisi ve deterministik otonomi çekirdeği ile başvuru yapılmış; Kasım 2026 küresel finalist adaylığı resmiyet kazanmıştır.",
      answerEn: "Official application submitted to the Dubai Roads and Transport Authority (RTA) $1,200,000 global Level-4 Robotaxi competition utilizing the Hyundai Ioniq 5 drive-by-wire platform, slated for November 2026 international finalist demonstration.",
      authority: "rta.ae",
      typeTr: "Seviye-4 Küresel Robotaksi Ödülü",
      typeEn: "Level-4 Global Robotaxi Prize"
    },
    {
      flag: "🇸🇦",
      institutionTr: "NEOM Otonom Mobilite",
      institutionEn: "NEOM Autonomous Mobility",
      badgeTr: "$500B Mega Şehir",
      badgeEn: "$500B Mega City",
      badgeColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
      questionTr: "Suudi Arabistan NEOM mega kenti ile yürütülen temas nedir?",
      questionEn: "What is the engagement with Saudi Arabia's NEOM mega-city project?",
      answerTr: "Suudi Arabistan'ın 500 Milyar Dolarlık sıfır emisyonlu geleceğin şehri NEOM Otonom Mobilite ve Yatırım Fonu birimine; aşırı sıcak çöl iklimi ve GNSS-denied kentsel kanyonlarda çalışabilen Seviye-4 sürücüsüz filo test ve PoC (Proof of Concept) teklifi resmi olarak sunulmuştur.",
      answerEn: "Trustia has officially submitted an autonomous fleet PoC proposal to the $500B NEOM Investment Fund and Autonomous Mobility division, engineered for Level-4 passenger shuttles operating in harsh thermal and GNSS-denied urban canyons.",
      authority: "neom.com",
      typeTr: "Filo Dağıtım & PoC Teklifi",
      typeEn: "Fleet Deployment & PoC Proposal"
    },
    {
      flag: "🇹🇷",
      institutionTr: "İTO BTM Fulya Kampüsü",
      institutionEn: "ITO BTM Fulya Campus",
      badgeTr: "Sözleşmeli Kuluçka",
      badgeEn: "Contracted Incubator",
      badgeColor: "text-[#C8FF00] bg-[#C8FF00]/10 border-[#C8FF00]/30",
      questionTr: "Trustia'nın fiziki yerleşkesi ve kuluçka akreditasyonu neresidir?",
      questionEn: "Where is Trustia's physical operational base and incubation center?",
      answerTr: "Trustia Teknoloji, İstanbul Ticaret Odası (İTO) bünyesindeki Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Yerleşkesi'nde 2026-II. Dönem Sözleşmeli Girişimi olarak faaliyet göstermektedir. Ofis, Ar-Ge atölyesi, test laboratuvarı ve küresel yatırımcı ağı desteğinden bilfiil yararlanmaktadır.",
      answerEn: "Trustia operates as a contracted enterprise in the 2026-II Cohort at the Information Commercialization Center (BTM) Fulya Campus, backed by the Istanbul Chamber of Commerce (İTO), providing physical office infrastructure, R&D laboratories, and global venture networks.",
      authority: "btm.istanbul",
      typeTr: "Fiziki Merkez & Ön Kuluçka",
      typeEn: "Physical HQ & Incubation Base"
    },
    {
      flag: "🇹🇷",
      institutionTr: "SPK Lisanslı fonbulucu",
      institutionEn: "CMB-Licensed fonbulucu",
      badgeTr: "Kampanya: W1MV5K",
      badgeEn: "Campaign: W1MV5K",
      badgeColor: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
      questionTr: "fonbulucu üzerindeki kitle fonlama kampanyasının kapsamı nedir?",
      questionEn: "What are the terms of the equity crowdfunding campaign on fonbulucu?",
      answerTr: "Sermaye Piyasası Kurulu (SPK) lisanslı fonbulucu platformunda Kampanya Kodu: W1MV5K ile; 150.000.000 TL şirket değerlemesi üzerinden %10 hisse ihracıyla 15.000.000 TL hedefli (18.000.000 TL fonlama tavanı) Seviye-4 Robotaksi Seri Üretim & Test Kampanyası resmi ön inceleme aşamasındadır.",
      answerEn: "Registered under campaign reference W1MV5K on the CMB-licensed (SPK) fonbulucu investment platform, seeking 15,000,000 TRY (18,000,000 TRY ceiling) at a pre-money valuation of 150,000,000 TRY for 10% equity to scale Level-4 Robotaxi vehicle conversions.",
      authority: "fonbulucu.com",
      typeTr: "SPK Paya Dayalı Kitle Fonlama",
      typeEn: "Equity Crowdfunding Round"
    }
  ];

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-8 bg-[#05070a] border-t border-b border-white/10">
      {/* Background Grid Pattern */}
      <div className="absolute inset-0 bg-tactical-grid opacity-10 pointer-events-none" />

      <div className="max-w-7xl mx-auto space-y-6 relative z-10">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 pb-3 border-b border-white/10">
          <div>
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-slate-400 text-[10px] font-mono tracking-wider uppercase mb-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-[#C8FF00]" />
              <span>{lang === "tr" ? "RESMİ AKREDİTASYON VE KURUMSAL KÜTÜK" : "OFFICIAL ACCREDITATIONS & CORPORATE REGISTRY"}</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {lang === "tr" ? "Kurumsal Doğrulama ve Akreditasyon Konsorsiyumu" : "Institutional Verification & Accreditation Consortium"}
            </h2>
          </div>
          <div className="text-left sm:text-right">
            <span className="text-[11px] font-mono text-slate-400 inline-flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00]" />
              {lang === "tr" ? "12 Resmi Program / Savunma & Küresel Fonlar" : "12 Verified Programs / Defense & Global Funds"}
            </span>
          </div>
        </div>

        {/* 2-Column Balanced Master Grid (Left: Clean Official Seal, Right: 12-Item Enterprise Accordion) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          {/* LEFT COLUMN: Clean Static Official Seal Card (4 Cols on lg) */}
          <div className="lg:col-span-4 flex flex-col p-4 rounded-2xl bg-[#080b10] border border-white/15 shadow-xl relative lg:sticky lg:top-24 space-y-3">
            
            {/* Top Header */}
            <div className="flex items-center justify-between gap-2 pb-2.5 border-b border-white/10">
              <div className="flex items-center gap-2">
                <Award className="w-4 h-4 text-[#C8FF00]" />
                <span className="text-xs font-bold text-white tracking-wide">
                  {lang === "tr" ? "T.C. SSB & İTO BTM Mührü" : "SSB Defense & ITO BTM Seal"}
                </span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/30 font-semibold">
                {lang === "tr" ? "Tescilli Konsorsiyum" : "Verified Consortium"}
              </span>
            </div>

            {/* Static Clean Image Container */}
            <div className="relative w-full aspect-[4/3] rounded-xl overflow-hidden border border-white/10 bg-black/60 shadow-inner">
              <Image
                src="/accreditations-showcase.jpg"
                alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
                fill
                className="object-cover object-center filter contrast-105"
                sizes="(max-width: 768px) 100vw, 33vw"
                priority
              />
            </div>

            {/* Entity Verification List */}
            <div className="space-y-2 pt-1 border-t border-white/10 text-xs">
              <div className="text-[10px] font-mono uppercase tracking-wider text-slate-400">
                {lang === "tr" ? "Konsorsiyum Ortakları ve Tesciller:" : "Consortium Entities & Proofs:"}
              </div>
              <div className="grid grid-cols-1 gap-1.5 font-mono text-[11px] text-slate-300">
                <div className="flex items-center gap-2 p-1.5 rounded bg-white/[0.03] border border-white/5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span className="truncate">T.C. SSB SAYZEK Platformu (#170)</span>
                </div>
                <div className="flex items-center gap-2 p-1.5 rounded bg-white/[0.03] border border-white/5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span className="truncate">İTO BTM Fulya 2026-II Kuluçka</span>
                </div>
                <div className="flex items-center gap-2 p-1.5 rounded bg-white/[0.03] border border-white/5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span className="truncate">KOSGEB İleri Girişimci (#01UGE0115)</span>
                </div>
                <div className="flex items-center gap-2 p-1.5 rounded bg-white/[0.03] border border-white/5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#C8FF00] shrink-0" />
                  <span className="truncate">Avrupa Komisyonu (PIC: 861711529)</span>
                </div>
              </div>
            </div>

            {/* Bottom Note */}
            <div className="pt-2 border-t border-white/10 text-[10px] font-mono text-slate-400 text-center">
              {lang === "tr" 
                ? "Tüm resmi evrak ve tesciller bağımsız teftişe ve denetime açıktır."
                : "All official certifications are available for independent corporate audit."}
            </div>
          </div>

          {/* RIGHT COLUMN: 12-Item Enterprise Accordion / Q&A Disclosure (8 Cols on lg) */}
          <div className="lg:col-span-8 space-y-2.5">
            {faqItems.map((item, idx) => {
              const isOpen = openIndex === idx;
              return (
                <div
                  key={idx}
                  className={`rounded-xl border transition-all duration-200 overflow-hidden ${
                    isOpen 
                      ? "bg-[#0d121c] border-[#C8FF00]/40 shadow-lg shadow-[#C8FF00]/5" 
                      : "bg-[#080b10] border-white/10 hover:border-white/20 hover:bg-[#0c1017]"
                  }`}
                >
                  {/* Accordion Trigger Header */}
                  <button
                    onClick={() => toggleAccordion(idx)}
                    className="w-full text-left p-3.5 sm:p-4 flex items-center justify-between gap-3 focus:outline-none"
                  >
                    <div className="flex items-center gap-3 min-w-0">
                      <span className="text-base sm:text-lg shrink-0 p-1.5 rounded-lg bg-white/5 border border-white/10">
                        {item.flag}
                      </span>
                      <div className="min-w-0">
                        <div className="flex items-center gap-2 mb-0.5">
                          <span className="text-[10px] font-mono uppercase tracking-wider text-slate-400 font-semibold">
                            {lang === "tr" ? item.institutionTr : item.institutionEn}
                          </span>
                          <span className="text-slate-600 text-[10px]">•</span>
                          <span className="text-[10px] font-mono text-[#C8FF00]">
                            {lang === "tr" ? item.typeTr : item.typeEn}
                          </span>
                        </div>
                        <h3 className={`text-xs sm:text-sm font-semibold tracking-tight transition-colors ${
                          isOpen ? "text-white" : "text-slate-200"
                        }`}>
                          {lang === "tr" ? item.questionTr : item.questionEn}
                        </h3>
                      </div>
                    </div>

                    <div className="flex items-center gap-2 shrink-0 ml-2">
                      <span className={`hidden sm:inline-block text-[9.5px] font-mono px-2 py-0.5 rounded border font-semibold ${item.badgeColor}`}>
                        {lang === "tr" ? item.badgeTr : item.badgeEn}
                      </span>
                      <div className={`p-1 rounded-md bg-white/5 border border-white/10 text-slate-400 transition-transform duration-200 ${
                        isOpen ? "rotate-180 text-[#C8FF00] bg-[#C8FF00]/10 border-[#C8FF00]/30" : ""
                      }`}>
                        <ChevronDown className="w-4 h-4" />
                      </div>
                    </div>
                  </button>

                  {/* Accordion Content Body */}
                  {isOpen && (
                    <div className="px-3.5 sm:px-4 pb-4 pt-1 border-t border-white/10 space-y-3 animate-in fade-in-50 duration-200">
                      <p className="text-xs sm:text-[13px] text-slate-300 leading-relaxed">
                        {lang === "tr" ? item.answerTr : item.answerEn}
                      </p>

                      {/* Detail Footer Inside Content */}
                      <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-white/5 text-[10px] font-mono text-slate-400">
                        <div className="flex items-center gap-3">
                          <span className="inline-flex items-center gap-1 text-slate-300">
                            <Building2 className="w-3 h-3 text-[#C8FF00]" />
                            <span>{item.authority}</span>
                          </span>
                          <span>•</span>
                          <span className="text-emerald-400 inline-flex items-center gap-1 font-semibold">
                            <CheckCircle2 className="w-3 h-3" />
                            {lang === "tr" ? "Doğrulanmış Tescil" : "Verified Record"}
                          </span>
                        </div>
                        <span className={`sm:hidden text-[9px] font-mono px-1.5 py-0.5 rounded border font-semibold ${item.badgeColor}`}>
                          {lang === "tr" ? item.badgeTr : item.badgeEn}
                        </span>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>

        </div>

      </div>
    </section>
  );
}

