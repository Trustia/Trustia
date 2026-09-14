"use client";

import { useState } from "react";
import Image from "next/image";
import { ShieldCheck, ChevronDown, Building2 } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function InstitutionalAccreditations() {
  const { lang } = useLanguage();
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleAccordion = (idx: number) => {
    setOpenIndex(openIndex === idx ? null : idx);
  };

  const faqItems = [
    {
      id: "01",
      categoryTr: "Avrupa Komisyonu",
      categoryEn: "European Commission",
      scopeTr: "Horizon Europe",
      scopeEn: "Horizon Europe",
      badge: "PIC: 861711529",
      questionTr: "Trustia Avrupa Birliği tarafından resmi olarak tanınıyor mu?",
      questionEn: "Is Trustia officially recognized by the European Commission?",
      answerTr: "Trustia, Avrupa Komisyonu Katılımcı Kayıt Defteri'ne (ec.europa.eu Participant Register) resmi olarak tescil edilmiş olup 9 haneli Avrupa Birliği Katılımcı Kimlik Kodu (PIC: 861711529) tahsis edilmiştir. Bu kayıt, Trustia'nın Horizon Europe ve EIC hibe programlarına doğrudan katılımını sağlamaktadır.",
      answerEn: "Trustia is officially registered in the European Commission Participant Register (ec.europa.eu) with an assigned 9-digit EU Participant Identification Code (PIC: 861711529), qualifying for direct participation in Horizon Europe and European Innovation Council (EIC) deep-tech research consortiums.",
      authority: "ec.europa.eu",
      recordTypeTr: "Resmi Katılımcı Tescili",
      recordTypeEn: "Official Participant Registry"
    },
    {
      id: "02",
      categoryTr: "EIT Urban Mobility",
      categoryEn: "EIT Urban Mobility",
      scopeTr: "Hibe & Test Pisti",
      scopeEn: "Grant & Proving Ground",
      badge: "Partner: CUS15554",
      questionTr: "EIT Urban Mobility ortaklığı ve 100.000 € hibe süreci ne aşamadadır?",
      questionEn: "What is the status of the EIT Urban Mobility partnership and €100k grant?",
      answerTr: "Trustia, Avrupa İnovasyon ve Teknoloji Enstitüsü (EIT) resmi kurumsal portalında onaylanarak CUS15554 Partner ID'sini almıştır. Girişimcilere Mali Destek çağrısı kapsamında 100.000 € tutarındaki doğrudan finansman ve otonomi test pisti başvurusu (Başvuru No: 3.1.02-1206-3732.3) resmi değerlendirme aşamasındadır.",
      answerEn: "Trustia is approved on the European Institute of Innovation & Technology (EIT) institutional portal under Partner ID CUS15554. An equity-free €100,000 grant and proving ground deployment application (Application ID: 3.1.02-1206-3732.3) under the Financial Support for Entrepreneurs call is in formal review.",
      authority: "eiturbanmobility.eu",
      recordTypeTr: "Hibe & Test Pisti",
      recordTypeEn: "Grant & Proving Ground"
    },
    {
      id: "03",
      categoryTr: "Katar QSTP",
      categoryEn: "Qatar QSTP",
      scopeTr: "30M$ Fon & Doha Sprint",
      scopeEn: "$30M Fund & Doha Sprint",
      badge: "Pre-Seed & Kuluçka",
      questionTr: "Katar Bilim ve Teknoloji Parkı (QSTP) ile yürütülen süreç nedir?",
      questionEn: "What is the engagement with Qatar Science & Technology Park (QSTP)?",
      answerTr: "Katar Vakfı bünyesindeki QSTP'ye iki yönlü resmi başvuru tamamlanmıştır: 30 Milyon Dolar bütçeli QSTP Tech Venture Fonu kapsamında 500.000 $ Pre-Seed yatırım başvurusu ve 4 haftalık yerinde Doha Sprint kuluçka rezidansı (fiziki ofis, konaklama ve Katar şirket kurulum desteği). Başvurular resmi inceleme kütüğündedir.",
      answerEn: "A dual-track application has been submitted to QSTP under Qatar Foundation: a $500,000 Pre-Seed investment proposal under the $30M Tech Venture Fund and the 4-week in-person Doha Sprint incubation residency, including enterprise office facilities, executive accommodations, and Qatari corporate establishment.",
      authority: "qstp.org.qa",
      recordTypeTr: "Venture Fon & Rezidans",
      recordTypeEn: "Venture Fund & Residency"
    },
    {
      id: "04",
      categoryTr: "BAYKAR Teknoloji",
      categoryEn: "BAYKAR Technology",
      scopeTr: "Savunma Alt Yüklenici",
      scopeEn: "Defense Subcontractor",
      badge: "Tedarikçi Havuzu",
      questionTr: "BAYKAR Teknoloji tedarikçi ve alt yüklenici değerlendirmesi ne durumdadır?",
      questionEn: "What is the status of the BAYKAR Tech defense supplier evaluation?",
      answerTr: "BAYKAR Teknoloji Tedarikçi Portalı'na Trustia Seviye-4 otonom seyrüsefer çekirdeği, GNSS-denied 3D LiDAR SLAM haritalama motoru ve taktik İKA alt sistemleri ile resmi tedarikçi kaydı yapılmış; teknik dosya onaylanarak savunma tedarikçi havuzuna dahil edilmiştir.",
      answerEn: "Trustia's Level-4 deterministic autonomy core, GNSS-denied 3D LiDAR SLAM localization engine, and tactical UGV algorithmic subsystems are officially registered in the BAYKAR Technology Supplier Portal for defense robotics subcontracting.",
      authority: "baykartech.com",
      recordTypeTr: "Savunma Tedarikçi Portalı",
      recordTypeEn: "Defense Supplier Portal"
    },
    {
      id: "05",
      categoryTr: "ASELSAN",
      categoryEn: "ASELSAN",
      scopeTr: "Yazılım Geliştirme & Potansiyel Tedarikçi",
      scopeEn: "Software Engineering & Potential Supplier",
      badge: "Ön Değerlendirme Onaylandı",
      questionTr: "ASELSAN Tedarikçi Portalı'ndaki resmi kayıt ve onay durumu nedir?",
      questionEn: "What is the official approval status on the ASELSAN Supplier Portal?",
      answerTr: "ASELSAN Tedarikçi Portalı (Başvuru No: 0050569CCE941FD1A49FCEFB9B7BE7D6) 'Yazılım Geliştirme' faaliyet alanındaki kurumsal ön değerlendirme OLUMLU SONUÇLANMIŞTIR. Trustia AI Otonom Sistemleri resmi olarak ASELSAN Potansiyel Tedarikçi Kütüğü'ne kaydedilmiş, SAP kurumsal portal erişim yetkisi tahsis edilmiş ve Kurul Toplantısı aşamasına geçilmiştir.",
      answerEn: "Official pre-evaluation for the 'Software Engineering' domain on the ASELSAN Supplier Portal (Ref: 0050569CCE941FD1A49FCEFB9B7BE7D6) has concluded with OFFICIAL APPROVAL. Trustia AI Autonomous Systems is formally registered in the ASELSAN Potential Supplier Registry with enterprise SAP access credentials provisioned, advancing to the Executive Board review stage.",
      authority: "partner.aselsan.com.tr",
      recordTypeTr: "Ön Değerlendirme Onaylandı • Potansiyel Tedarikçi",
      recordTypeEn: "Pre-Evaluation Approved • Potential Supplier"
    },
    {
      id: "06",
      categoryTr: "SSB SAYZEK",
      categoryEn: "SSB SAYZEK",
      scopeTr: "Yapay Zekâ & Simülasyon",
      scopeEn: "AI & Simulation",
      badge: "Başvuru #170",
      questionTr: "Savunma Sanayii Başkanlığı SAYZEK Yapay Zekâ Platformu entegrasyonu nedir?",
      questionEn: "What is the SSB SAYZEK Artificial Intelligence Platform integration?",
      answerTr: "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı Yapay Zekâ Platformu (SAYZEK) Simport Simülasyon Altyapısı'na 170 numaralı resmi başvuru ile katılım sağlanmıştır. Deterministik otonomi mimarisi ve askeri tehdit tespit modelleri savunma süper bilgisayar kümesinde onay sürecindedir.",
      answerEn: "Officially registered under Application #170 on the Presidency of Defense Industries (SSB) Artificial Intelligence Platform (SAYZEK) Simport simulation infrastructure, qualifying Trustia's deterministic autonomy architecture for defense computing resources.",
      authority: "sayzek.ssb.gov.tr",
      recordTypeTr: "Simport Simülasyon Portalı",
      recordTypeEn: "Simport Simulation Portal"
    },
    {
      id: "07",
      categoryTr: "Z Fellows",
      categoryEn: "Z Fellows",
      scopeTr: "Silikon Vadisi & Pace Capital",
      scopeEn: "Silicon Valley & Pace Capital",
      badge: "Mülakat: 17 Eylül",
      questionTr: "Silikon Vadisi Z Fellows programı ve Pace Capital mülakatı nedir?",
      questionEn: "What is the Silicon Valley Z Fellows fellowship and Pace Capital interview?",
      answerTr: "Uluslararası teknoloji kurucularını Silikon Vadisi'ne taşıyan Z Fellows programında Trustia, Pace Capital Partneri Grace Kasten ile 17 Eylül 2026 tarihinde canlı Zoom partner mülakatı aşamasına seçilmiştir. Program 10.000 $ hissesiz hibe ve San Francisco hızlandırma rezidansı sunmaktadır.",
      answerEn: "Trustia was selected for the live Zoom partner interview on September 17, 2026, with Grace Kasten (Partner at Pace Capital) for Z Fellows in San Francisco, providing an equity-free $10,000 grant and an intensive founder residency.",
      authority: "zfellows.com",
      recordTypeTr: "Silikon Vadisi Hızlandırma",
      recordTypeEn: "Silicon Valley Acceleration"
    },
    {
      id: "08",
      categoryTr: "DEİK",
      categoryEn: "DEİK",
      scopeTr: "İş Konseyi Üyelik Daveti",
      scopeEn: "Business Council Official Invitation",
      badge: "Resmi Üyelik Daveti",
      questionTr: "DEİK bünyesindeki kurumsal temsil ve üyelik daveti süreci nedir?",
      questionEn: "What is the status of DEİK business diplomacy and membership invitation?",
      answerTr: "T.C. Ticaret Bakanlığı koordinasyonundaki Dış Ekonomik İlişkiler Kurulu (DEİK) Üye İlişkileri Dairesi tarafından Trustia'ya DEİK ve Dijital Teknolojiler İş Konseyi resmi üyelik daveti iletilmiştir. Türkiye'nin yerli Seviye-4 otonom mobilite ve savunma teknolojileri ihracatı bu diplomatik hat üzerinden küresel pazarlara taşınmaktadır.",
      answerEn: "Trustia has received an official corporate membership invitation from the Foreign Economic Relations Board of Turkey (DEİK) Membership & Business Councils department under the Ministry of Trade, anchoring Trustia's sovereign Level-4 autonomous driving technologies into global commercial diplomacy pipelines.",
      authority: "deik.org.tr",
      recordTypeTr: "Resmi Üyelik Daveti",
      recordTypeEn: "Official Membership Invitation"
    },
    {
      id: "09",
      categoryTr: "Dubai RTA",
      categoryEn: "Dubai RTA",
      scopeTr: "1.2M$ Küresel Challenge",
      scopeEn: "$1.2M Global Challenge",
      badge: "Finalist Adayı",
      questionTr: "Dubai RTA 1.2 Milyon Dolarlık Robotaksi yarışması ne durumdadır?",
      questionEn: "What is the status of the $1.2M Dubai RTA Self-Driving Transport Challenge?",
      answerTr: "Dubai Yollar ve Ulaşım Otoritesi (RTA) tarafından düzenlenen 1.200.000 $ nakit ödüllü küresel Seviye-4 Robotaksi yarışmasına Hyundai Ioniq 5 retrofit mimarisi ve deterministik otonomi çekirdeği ile başvuru yapılmış; Kasım 2026 küresel finalist adaylığı tescil edilmiştir.",
      answerEn: "Official application submitted to the Dubai Roads and Transport Authority (RTA) $1,200,000 global Level-4 Robotaxi competition utilizing the Hyundai Ioniq 5 drive-by-wire platform, slated for November 2026 international finalist demonstration.",
      authority: "rta.ae",
      recordTypeTr: "Seviye-4 Robotaksi Ödülü",
      recordTypeEn: "Level-4 Robotaxi Prize"
    },
    {
      id: "10",
      categoryTr: "NEOM Mobilite",
      categoryEn: "NEOM Mobility",
      scopeTr: "$500B Mega Şehir",
      scopeEn: "$500B Mega City",
      badge: "PoC Başvurusu",
      questionTr: "Suudi Arabistan NEOM mega kenti ile yürütülen temas nedir?",
      questionEn: "What is the engagement with Saudi Arabia's NEOM mega-city project?",
      answerTr: "Suudi Arabistan'ın 500 Milyar Dolarlık sıfır emisyonlu mega kenti NEOM Otonom Mobilite ve Yatırım Fonu birimine; aşırı sıcak çöl iklimi ve GNSS-denied kentsel kanyonlarda çalışabilen Seviye-4 sürücüsüz filo test ve PoC (Proof of Concept) teklifi sunulmuştur.",
      answerEn: "Trustia has submitted an autonomous fleet PoC proposal to the $500B NEOM Investment Fund and Autonomous Mobility division, engineered for Level-4 passenger shuttles operating in harsh thermal and GNSS-denied urban canyons.",
      authority: "neom.com",
      recordTypeTr: "Filo PoC Teklifi",
      recordTypeEn: "Fleet PoC Proposal"
    },
    {
      id: "11",
      categoryTr: "İTO BTM Fulya",
      categoryEn: "ITO BTM Fulya",
      scopeTr: "Sözleşmeli Kuluçka",
      scopeEn: "Contracted Incubation",
      badge: "2026-II Dönemi",
      questionTr: "Trustia'nın fiziki yerleşkesi ve kuluçka akreditasyonu neresidir?",
      questionEn: "Where is Trustia's physical operational base and incubation center?",
      answerTr: "Trustia, İstanbul Ticaret Odası (İTO) bünyesindeki Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Yerleşkesi'nde 2026-II. Dönem Sözleşmeli Girişimi olarak faaliyet göstermektedir. Ofis, Ar-Ge atölyesi ve test altyapısı imkanlarından bilfiil yararlanmaktadır.",
      answerEn: "Trustia operates as a contracted enterprise in the 2026-II Cohort at the Information Commercialization Center (BTM) Fulya Campus, backed by the Istanbul Chamber of Commerce (İTO), providing physical office infrastructure, R&D laboratories, and venture networks.",
      authority: "btm.istanbul",
      recordTypeTr: "Sözleşmeli Ön Kuluçka",
      recordTypeEn: "Contracted Incubator"
    },
    {
      id: "12",
      categoryTr: "SPK fonbulucu",
      categoryEn: "CMB fonbulucu",
      scopeTr: "Paya Dayalı Fonlama",
      scopeEn: "Equity Crowdfunding",
      badge: "Kampanya: W1MV5K",
      questionTr: "fonbulucu üzerindeki kitle fonlama kampanyasının kapsamı nedir?",
      questionEn: "What are the terms of the equity crowdfunding campaign on fonbulucu?",
      answerTr: "Sermaye Piyasası Kurulu (SPK) lisanslı fonbulucu platformunda Kampanya Kodu: W1MV5K ile; 150.000.000 TL şirket değerlemesi üzerinden %10 hisse ihracıyla 15.000.000 TL hedefli (18.000.000 TL fonlama tavanı) Seviye-4 Robotaksi Seri Üretim & Test Kampanyası resmi ön inceleme aşamasındadır.",
      answerEn: "Registered under campaign reference W1MV5K on the CMB-licensed (SPK) fonbulucu investment platform, seeking 15,000,000 TRY (18,000,000 TRY ceiling) at a pre-money valuation of 150,000,000 TRY for 10% equity to scale Level-4 Robotaxi vehicle conversions.",
      authority: "fonbulucu.com",
      recordTypeTr: "SPK Paya Dayalı Fonlama",
      recordTypeEn: "Equity Crowdfunding Round"
    },
    {
      id: "13",
      categoryTr: "Teknopark İstanbul",
      categoryEn: "Teknopark Istanbul",
      scopeTr: "HASAT 2026 Teknoloji Sahnesi",
      scopeEn: "HASAT 2026 Deep Tech Stage",
      badge: "100M TL Destek & Ofis",
      questionTr: "Teknopark İstanbul HASAT 2026 ve Cube Incubation başvuru süreci nedir?",
      questionEn: "What is the status of the Teknopark Istanbul HASAT 2026 and Cube Incubation application?",
      answerTr: "T.C. Cumhurbaşkanlığı Savunma Sanayii Başkanlığı (SSB) ve İstanbul Ticaret Odası (İTO) çatı ortaklığındaki Teknopark İstanbul tarafından düzenlenen HASAT 2026 yarışmasına Seviye-4 deterministik otonomi platformumuzla resmi yarışma başvurusu başarıyla tamamlanmıştır. 100 Milyon TL'lik yatırım ve destek havuzu kapsamında Cube Incubation bünyesinde Ar-Ge ofisi, prototipleme atölyesi ve sahne sunumu hedeflenmektedir.",
      answerEn: "Trustia has formally submitted its application to HASAT 2026, hosted by Teknopark Istanbul under the co-founding auspices of the Presidency of Defense Industries (SSB) and Istanbul Chamber of Commerce (İTO). Selected startups gain access to a 100M TRY investment and support pool, dedicated R&D office space at Cube Incubation, and live stage pitching to defense and deep-tech venture capital funds.",
      authority: "hasat.eventiqs.com",
      recordTypeTr: "SSB & İTO Destekli Teknoloji Sahnesi",
      recordTypeEn: "SSB & İTO Deep Tech Stage"
    }
  ];

  return (
    <section className="relative z-20 py-12 sm:py-16 px-4 sm:px-8 bg-[#07090e] border-t border-b border-zinc-800/80">
      <div className="max-w-7xl mx-auto space-y-6 relative z-10">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 pb-3 border-b border-zinc-800">
          <div>
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-zinc-900 border border-zinc-800 text-zinc-400 text-[10px] font-mono tracking-wider uppercase mb-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-zinc-300" />
              <span>{lang === "tr" ? "RESMİ AKREDİTASYON VE TESCİLLER" : "OFFICIAL ACCREDITATIONS & REGISTRY"}</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-semibold text-white tracking-tight">
              {lang === "tr" ? "Kurumsal Doğrulama ve Tescil Kütüğü" : "Institutional Verification & Regulatory Registry"}
            </h2>
          </div>
          <div className="text-left sm:text-right">
            <span className="text-[11px] font-mono text-zinc-400">
              {lang === "tr" ? "13 Doğrulanmış Kayıt / Savunma & Küresel Fonlar" : "13 Verified Records / Defense & Global Funds"}
            </span>
          </div>
        </div>

        {/* 2-Column Balanced Master Grid (Left: Official Dossier, Right: 12-Item Corporate Accordion) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          {/* LEFT COLUMN: Clean Corporate Verification Dossier (4 Cols on lg) */}
          <div className="lg:col-span-4 flex flex-col p-5 rounded-2xl bg-[#0b0e14] border border-zinc-800/80 shadow-xl relative lg:sticky lg:top-24 space-y-4">
            
            {/* Dossier Header */}
            <div className="flex items-center justify-between gap-2 pb-2.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <Building2 className="w-4 h-4 text-zinc-300" />
                <span className="text-xs font-semibold text-zinc-200 tracking-wide">
                  {lang === "tr" ? "Kamu & Savunma Tescili" : "Public & Defense Registry"}
                </span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-zinc-900 text-zinc-300 border border-zinc-700 font-medium">
                {lang === "tr" ? "Tescilli" : "Verified"}
              </span>
            </div>

            {/* Static Clean Image Container */}
            <div className="relative w-full aspect-[16/10] rounded-xl overflow-hidden border border-zinc-800 bg-black shadow-inner">
              <Image
                src="/accreditations-showcase.jpg"
                alt="T.C. Savunma Sanayii Başkanlığı, İTO, BTM, KOSGEB, Teknopark İstanbul Resmi Akreditasyonları"
                fill
                className="object-cover object-center filter contrast-105"
                sizes="(max-width: 768px) 100vw, 33vw"
                priority
              />
            </div>

            {/* Structured Executive Metadata Breakdown */}
            <div className="space-y-2 pt-2 border-t border-zinc-800/80 text-xs">
              <div className="text-[10px] font-mono uppercase tracking-wider text-zinc-400 font-medium">
                {lang === "tr" ? "Doğrulanmış Ekosistem Kütüğü" : "Verified Ecosystem Registry"}
              </div>
              <div className="space-y-1.5 font-mono text-[11px]">
                <div className="flex items-center justify-between py-1.5 px-2.5 rounded bg-zinc-900/50 border border-zinc-800/60">
                  <span className="text-zinc-400">ASELSAN Tedarikçi</span>
                  <span className="text-zinc-200 font-semibold">{lang === "tr" ? "Ön Onaylı (SAP)" : "Pre-Approved (SAP)"}</span>
                </div>
                <div className="flex items-center justify-between py-1.5 px-2.5 rounded bg-zinc-900/50 border border-zinc-800/60">
                  <span className="text-zinc-400">T.C. SSB SAYZEK</span>
                  <span className="text-zinc-200 font-semibold">Başvuru #170</span>
                </div>
                <div className="flex items-center justify-between py-1.5 px-2.5 rounded bg-zinc-900/50 border border-zinc-800/60">
                  <span className="text-zinc-400">İTO BTM Fulya</span>
                  <span className="text-zinc-200 font-semibold">2026-II Kuluçka</span>
                </div>
                <div className="flex items-center justify-between py-1.5 px-2.5 rounded bg-zinc-900/50 border border-zinc-800/60">
                  <span className="text-zinc-400">KOSGEB Başkanlığı</span>
                  <span className="text-zinc-200 font-semibold">#01UGE0115</span>
                </div>
                <div className="flex items-center justify-between py-1.5 px-2.5 rounded bg-zinc-900/50 border border-zinc-800/60">
                  <span className="text-zinc-400">Avrupa Komisyonu</span>
                  <span className="text-zinc-200 font-semibold">PIC: 861711529</span>
                </div>
              </div>
            </div>

            {/* Dossier Footer */}
            <div className="pt-2 border-t border-zinc-800/80 text-[10px] font-mono text-zinc-500 text-center">
              {lang === "tr" 
                ? "Tüm tesciller ilgili resmi kurum kayıt defterlerinde onaylıdır." 
                : "All records are officially certified in respective institutional registers."}
            </div>
          </div>

          {/* RIGHT COLUMN: 12-Item Corporate Accordion (8 Cols on lg) */}
          <div className="lg:col-span-8 space-y-2">
            {faqItems.map((item, idx) => {
              const isOpen = openIndex === idx;
              return (
                <div
                  key={idx}
                  className={`rounded-xl border transition-colors overflow-hidden ${
                    isOpen 
                      ? "bg-[#0d1017] border-zinc-700 shadow-md" 
                      : "bg-[#090c12] border-zinc-800/80 hover:border-zinc-700 hover:bg-[#0c0f16]"
                  }`}
                >
                  {/* Accordion Trigger Header */}
                  <button
                    onClick={() => toggleAccordion(idx)}
                    className="w-full text-left p-3.5 sm:p-4 flex items-center justify-between gap-3 focus:outline-none"
                  >
                    <div className="flex items-center gap-3 min-w-0">
                      <span className="font-mono text-xs font-semibold text-zinc-400 w-5 shrink-0">
                        {item.id}
                      </span>
                      <div className="min-w-0">
                        <div className="flex items-center gap-2 mb-0.5">
                          <span className="text-[10px] font-mono uppercase tracking-wider text-zinc-400 font-semibold">
                            {lang === "tr" ? item.categoryTr : item.categoryEn}
                          </span>
                          <span className="text-zinc-600 text-[10px]">•</span>
                          <span className="text-[10px] font-mono text-zinc-400">
                            {lang === "tr" ? item.scopeTr : item.scopeEn}
                          </span>
                        </div>
                        <h3 className={`text-xs sm:text-sm font-medium tracking-tight transition-colors ${
                          isOpen ? "text-white" : "text-zinc-200"
                        }`}>
                          {lang === "tr" ? item.questionTr : item.questionEn}
                        </h3>
                      </div>
                    </div>

                    <div className="flex items-center gap-2 shrink-0 ml-2">
                      <span className="hidden sm:inline-block text-[9.5px] font-mono px-2 py-0.5 rounded border font-medium bg-zinc-900 text-zinc-300 border-zinc-700/80">
                        {item.badge}
                      </span>
                      <div className={`p-1 rounded bg-zinc-900 border border-zinc-800 text-zinc-400 transition-transform duration-200 ${
                        isOpen ? "rotate-180 text-zinc-200 border-zinc-700" : ""
                      }`}>
                        <ChevronDown className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </button>

                  {/* Accordion Content Body */}
                  {isOpen && (
                    <div className="px-3.5 sm:px-4 pb-4 pt-1 border-t border-zinc-800/80 space-y-3">
                      <p className="text-xs sm:text-[13px] text-zinc-300 leading-relaxed font-normal">
                        {lang === "tr" ? item.answerTr : item.answerEn}
                      </p>

                      {/* Detail Footer Inside Content */}
                      <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-zinc-800/40 text-[10px] font-mono text-zinc-400">
                        <div className="flex items-center gap-3">
                          <span className="text-zinc-400">
                            {item.authority}
                          </span>
                          <span>•</span>
                          <span className="text-zinc-300 font-medium">
                            {lang === "tr" ? item.recordTypeTr : item.recordTypeEn}
                          </span>
                        </div>
                        <span className="sm:hidden text-[9px] font-mono px-1.5 py-0.5 rounded border font-medium bg-zinc-900 text-zinc-300 border-zinc-800">
                          {item.badge}
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

