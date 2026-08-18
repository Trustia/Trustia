"use client";

import { useState } from "react";
import { Send, CheckCircle2, ShieldCheck, Mail, Building2, User, Loader2, AtSign } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

export default function CorporateContactForm() {
  const { lang, t } = useLanguage();
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    company: "",
    email: "",
    targetEmail: "iletisim@trustia.com.tr",
    subject: "Otonomi Yazılım Entegrasyonu",
    message: "",
  });

  const departmentOptions = [
    { email: "iletisim@trustia.com.tr", label: lang === "tr" ? "Genel İletişim & Santral (iletisim@trustia.com.tr)" : "General Inquiries (iletisim@trustia.com.tr)" },
    { email: "entegrasyon@trustia.com.tr", label: lang === "tr" ? "Teknik Entegrasyon & Otonomi SDK (entegrasyon@trustia.com.tr)" : "Technical Integration & SDK (entegrasyon@trustia.com.tr)" },
    { email: "kariyer@trustia.com.tr", label: lang === "tr" ? "Kariyer & Mühendislik Başvuruları (kariyer@trustia.com.tr)" : "Careers & Engineering Recruitment (kariyer@trustia.com.tr)" },
    { email: "hukuk@trustia.com.tr", label: lang === "tr" ? "Hukuk, Fikri Mülkiyet & Lisanslama (hukuk@trustia.com.tr)" : "Legal, IP & Licensing (hukuk@trustia.com.tr)" },
  ];

  const subjectOptions = [
    { value: "Otonomi Yazılım Entegrasyonu", label: lang === "tr" ? "İKA Otonomi Yazılım Entegrasyonu Talebi" : "UGV Autonomy Software Integration Request" },
    { value: "Saha Demosu ve Teknik Sunum", label: lang === "tr" ? "Saha Demosu ve Teknik Sunum Talebi" : "Live Field Demo & Technical Briefing" },
    { value: "Savunma Tedarik & Lisanslama", label: lang === "tr" ? "Savunma Tedarik ve OEM Lisanslama" : "Defense Procurement & OEM Licensing" },
    { value: "Ar-Ge ve Konsorsiyum Ortaklığı", label: lang === "tr" ? "Milli Ar-Ge ve Konsorsiyum Ortaklığı" : "R&D Consortium & Defense Partnership" },
    { value: "Kariyer ve Staj Başvurusu", label: lang === "tr" ? "Kariyer ve Mühendislik Başvurusu" : "Career & Engineering Application" },
    { value: "Diğer Kurumsal Konular", label: lang === "tr" ? "Diğer Kurumsal Konular" : "Other Corporate Inquiries" },
  ];

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name || !formData.email || !formData.message) return;
    setIsSubmitting(true);

    try {
      const response = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          access_key: "89f9e28d-6a2c-4612-be65-b387ad79b5ab",
          from_name: "TRUSTIA AI — Web Portal",
          subject: `[${formData.targetEmail}] ${formData.subject} — ${formData.name}`,
          replyto: formData.email,
          name: formData.name,
          company: formData.company || "Not Specified",
          email: formData.email,
          target_department: formData.targetEmail,
          subject_type: formData.subject,
          message: `
--------------------------------------------------
TRUSTIA AUTONOMOUS SYSTEMS // OFFICIAL WEB INQUIRY
--------------------------------------------------

TARGET INBOX: ${formData.targetEmail}

SENDER INFORMATION:
• Name: ${formData.name}
• Institution / Company: ${formData.company || "Not Specified"}
• Sender Email: ${formData.email}
• Target Email: ${formData.targetEmail}
• Subject: ${formData.subject}

TECHNICAL REQUIREMENTS & MESSAGE:
--------------------------------------------------
${formData.message}
--------------------------------------------------
Timestamp: ${new Date().toISOString()}
Portal: https://trustia.com.tr/iletisim/
          `,
        }),
      });

      await response.json();
      setSubmitted(true);
    } catch {
      setSubmitted(true);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="w-full">
      {submitted ? (
        <div className="p-6 sm:p-10 rounded-2xl bg-[#0c1017] border border-[#C8FF00]/40 text-center space-y-4 shadow-[0_0_30px_rgba(200,255,0,0.1)]">
          <div className="w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/40 flex items-center justify-center mx-auto">
            <CheckCircle2 className="w-6 h-6 sm:w-8 sm:h-8" />
          </div>
          <h4 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
            {t("contact_success_title")}
          </h4>
          <p className="text-slate-300 text-xs sm:text-sm max-w-md mx-auto leading-relaxed font-normal">
            {t("contact_success_desc")} (<span className="text-[#C8FF00] font-mono font-bold">{formData.targetEmail}</span>)
          </p>
          <div className="inline-block font-mono text-[11px] sm:text-xs font-bold text-[#C8FF00] px-3.5 py-1.5 rounded bg-white/5 border border-white/10 uppercase">
            {t("contact_code")}
          </div>
          <div className="pt-2">
            <button
              onClick={() => {
                setSubmitted(false);
                setFormData({ name: "", company: "", email: "", targetEmail: "iletisim@trustia.com.tr", subject: "Otonomi Yazılım Entegrasyonu", message: "" });
              }}
              className="text-xs font-mono text-slate-400 hover:text-white underline cursor-pointer"
            >
              {t("contact_btn_new")}
            </button>
          </div>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="p-4 sm:p-8 md:p-10 rounded-2xl bg-[#0c1017] border border-white/10 space-y-4 sm:space-y-6 shadow-2xl">
          
          {/* Target Department Selection */}
          <div className="space-y-1.5 sm:space-y-2">
            <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
              <AtSign className="w-3.5 h-3.5 text-[#C8FF00]" />
              <span>{t("contact_label_dept")}</span>
            </label>
            <select
              value={formData.targetEmail}
              onChange={(e) => setFormData({ ...formData, targetEmail: e.target.value })}
              className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
            >
              {departmentOptions.map((opt) => (
                <option key={opt.email} value={opt.email} className="bg-[#0c1017] text-white">
                  {opt.label}
                </option>
              ))}
            </select>
          </div>

          {/* Name & Company Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
            <div className="space-y-1.5 sm:space-y-2">
              <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                <User className="w-3.5 h-3.5 text-[#C8FF00]" />
                <span>{t("contact_label_name")}</span>
              </label>
              <input
                type="text"
                required
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                placeholder={lang === "tr" ? "Örn: Ahmet Yılmaz" : "e.g. John Doe"}
                className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600"
              />
            </div>

            <div className="space-y-1.5 sm:space-y-2">
              <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                <Building2 className="w-3.5 h-3.5 text-[#C8FF00]" />
                <span>{t("contact_label_company")}</span>
              </label>
              <input
                type="text"
                value={formData.company}
                onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                placeholder={lang === "tr" ? "Örn: Savunma Sanayii / ASELSAN" : "e.g. Defense Contractor / Corp"}
                className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600"
              />
            </div>
          </div>

          {/* Email Address */}
          <div className="space-y-1.5 sm:space-y-2">
            <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
              <Mail className="w-3.5 h-3.5 text-[#C8FF00]" />
              <span>{t("contact_label_email")}</span>
            </label>
            <input
              type="email"
              required
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              placeholder="iletisim@kurum.com.tr"
              className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600"
            />
          </div>

          {/* Subject Option */}
          <div className="space-y-1.5 sm:space-y-2">
            <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-[#C8FF00]" />
              <span>{t("contact_label_subject")}</span>
            </label>
            <select
              value={formData.subject}
              onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
              className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
            >
              {subjectOptions.map((subj) => (
                <option key={subj.value} value={subj.value} className="bg-[#0c1017] text-white">
                  {subj.label}
                </option>
              ))}
            </select>
          </div>

          {/* Message Textarea */}
          <div className="space-y-1.5 sm:space-y-2">
            <label className="block text-[11px] sm:text-xs font-mono font-bold text-slate-300 uppercase tracking-wider">
              {t("contact_label_message")}
            </label>
            <textarea
              required
              rows={3}
              value={formData.message}
              onChange={(e) => setFormData({ ...formData, message: e.target.value })}
              placeholder={lang === "tr" ? "İKA platformunuz, entegrasyon takviminiz, donanım gereksinimleriniz veya sormak istediğiniz tüm teknik detayları belirtiniz..." : "Specify your UGV platform, integration timeline, hardware interfaces and technical requirements..."}
              className="w-full px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-xl bg-black/60 border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600 resize-none leading-relaxed"
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full py-3 sm:py-4 rounded-xl bg-[#C8FF00] hover:bg-[#d4ff33] text-black font-mono font-bold text-xs sm:text-sm uppercase tracking-wider flex items-center justify-center gap-2 hover:shadow-[0_0_25px_rgba(200,255,0,0.4)] transition-all cursor-pointer disabled:opacity-50"
          >
            {isSubmitting ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>{t("contact_submitting")}</span>
              </>
            ) : (
              <>
                <Send className="w-4 h-4" />
                <span>{t("contact_btn_submit")}</span>
              </>
            )}
          </button>

          <p className="text-[10px] sm:text-xs text-slate-400 font-mono text-center leading-relaxed">
            {t("contact_direct_note")}
          </p>

        </form>
      )}
    </div>
  );
}
