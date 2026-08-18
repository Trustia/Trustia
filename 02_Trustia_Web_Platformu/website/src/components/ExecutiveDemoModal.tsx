"use client";

import { useState } from "react";
import { X, ShieldCheck, Lock, Building, Mail, User, Send, CheckCircle2, UploadCloud, Download, FileText } from "lucide-react";
import { useLanguage } from "@/context/LanguageContext";

interface ExecutiveDemoModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function ExecutiveDemoModal({ isOpen, onClose }: ExecutiveDemoModalProps) {
  const { lang, t } = useLanguage();
  const [submitted, setSubmitted] = useState(false);
  const [attachedFile, setAttachedFile] = useState<File | null>(null);
  const [formData, setFormData] = useState({
    institution: "",
    title: "",
    email: "",
    scope: "İKA Entegrasyonu & 3D SLAM SDK",
  });

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setAttachedFile(e.target.files[0]);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/85 backdrop-blur-md animate-fade-in font-sans selection:bg-[#C8FF00] selection:text-black">
      <div className="relative w-full max-w-xl bg-[#0a0d12] border border-white/15 rounded-3xl shadow-[0_20px_60px_rgba(0,0,0,0.9)] flex flex-col overflow-hidden text-slate-200">
        
        {/* Top Executive Header */}
        <div className="flex items-center justify-between px-6 py-5 bg-[#06080b] border-b border-white/10 shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] flex items-center justify-center">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-orbitron font-extrabold text-white text-base tracking-wider">TRUSTIA AI</span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] font-bold">
                  {t("demo_nda_badge")}
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-normal">
                {t("demo_header_title")}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl bg-white/5 border border-white/10 text-slate-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
            aria-label="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Form Body */}
        <div className="p-6 sm:p-8 space-y-6">
          {submitted ? (
            <div className="py-6 text-center space-y-5">
              <div className="w-14 h-14 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 flex items-center justify-center mx-auto">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <div className="space-y-1">
                <h3 className="text-xl font-bold text-white tracking-tight">{t("demo_success_title")}</h3>
                <p className="text-slate-300 text-xs sm:text-sm max-w-md mx-auto leading-relaxed">
                  {t("demo_success_desc")}
                </p>
              </div>

              {/* Instant Executive SDK Document Download Button */}
              <div className="p-4 rounded-2xl bg-[#06080b] border border-white/10 text-left space-y-3 max-w-md mx-auto">
                <div className="flex items-center gap-2 text-xs font-mono text-[#C8FF00] font-bold">
                  <FileText className="w-4 h-4" />
                  <span>{t("demo_download_title")}</span>
                </div>
                <p className="text-[11px] text-slate-400 leading-relaxed font-normal">
                  {t("demo_download_desc")}
                </p>
                <a
                  href="/politika/lisans"
                  target="_blank"
                  className="w-full py-2.5 px-4 rounded-xl bg-white/10 hover:bg-white/20 border border-white/15 text-white font-mono font-bold text-xs flex items-center justify-center gap-2 transition-all cursor-pointer"
                >
                  <Download className="w-4 h-4 text-[#C8FF00]" />
                  <span>{t("demo_download_btn")}</span>
                </a>
              </div>

              <button
                onClick={() => { setSubmitted(false); setAttachedFile(null); onClose(); }}
                className="px-6 py-2.5 rounded-xl bg-[#C8FF00] text-black font-mono font-bold text-xs uppercase tracking-wider hover:bg-[#d4ff33] transition-colors cursor-pointer"
              >
                {t("demo_btn_close")}
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5">
              
              {/* Institution / Company */}
              <div className="space-y-2">
                <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <Building className="w-3.5 h-3.5 text-[#C8FF00]" />
                  <span>{t("demo_label_institution")}</span>
                </label>
                <input
                  type="text"
                  required
                  placeholder={t("demo_ph_institution")}
                  value={formData.institution}
                  onChange={(e) => setFormData({ ...formData, institution: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
                />
              </div>

              {/* Title / Role & Email Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                    <User className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>{t("demo_label_title")}</span>
                  </label>
                  <input
                    type="text"
                    required
                    placeholder={t("demo_ph_title")}
                    value={formData.title}
                    onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                    className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
                  />
                </div>

                <div className="space-y-2">
                  <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                    <Mail className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>{t("demo_label_email")}</span>
                  </label>
                  <input
                    type="email"
                    required
                    placeholder={t("demo_ph_email")}
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
                  />
                </div>
              </div>

              {/* Scope Selection */}
              <div className="space-y-2">
                <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider">
                  {t("demo_label_scope")}
                </label>
                <select
                  value={formData.scope}
                  onChange={(e) => setFormData({ ...formData, scope: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/15 text-white font-mono text-xs focus:outline-none focus:border-[#C8FF00] transition-colors"
                >
                  <option value="İKA Entegrasyonu & 3D SLAM SDK">
                    {lang === "tr" ? "İKA Entegrasyonu & 3D SLAM Otonomi SDK" : "UGV Integration & 3D SLAM Autonomy SDK"}
                  </option>
                  <option value="Saha Demosu ve Canlı Test Talebi">
                    {lang === "tr" ? "Saha Demosu ve Canlı Araç Test Talebi" : "Live Field Demo & Physical Vehicle Trials"}
                  </option>
                  <option value="EYP/Mayın & KHKN Tehdit Füzyon Modülü">
                    {lang === "tr" ? "EYP/Mayın & KHKN Tehdit Füzyon Modülü" : "IED/Mine & CBRN Threat Fusion Module"}
                  </option>
                  <option value="Hava-Kara Hibrit Sürü Mimarisi">
                    {lang === "tr" ? "Hava-Kara Hibrit Sürü Mimarisi & C2" : "Air-Ground Hybrid Swarm Architecture & C2"}
                  </option>
                </select>
              </div>

              {/* Optional File Upload Dropzone */}
              <div className="space-y-2">
                <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider flex items-center justify-between">
                  <span>{t("demo_label_upload")}</span>
                  {attachedFile && (
                    <span className="text-[#C8FF00] font-normal normal-case">{attachedFile.name}</span>
                  )}
                </label>
                <label className="border border-dashed border-white/20 hover:border-[#C8FF00]/50 rounded-2xl p-4 flex flex-col items-center justify-center gap-2 cursor-pointer bg-white/[0.02] hover:bg-white/[0.04] transition-all group">
                  <input
                    type="file"
                    accept=".pdf,.docx,.zip,.rar"
                    onChange={handleFileChange}
                    className="hidden"
                  />
                  <UploadCloud className="w-6 h-6 text-slate-400 group-hover:text-[#C8FF00] transition-colors" />
                  <div className="text-center">
                    <span className="text-xs font-mono font-bold text-slate-300 group-hover:text-white">
                      {attachedFile ? attachedFile.name : t("demo_upload_drag")}
                    </span>
                    <p className="text-[10px] text-slate-500 mt-0.5">
                      {t("demo_upload_hint")}
                    </p>
                  </div>
                </label>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                className="w-full py-3 px-6 rounded-xl bg-[#C8FF00] hover:bg-[#d4ff33] text-black font-mono font-black text-xs uppercase tracking-wider flex items-center justify-center gap-2 hover:shadow-[0_0_20px_rgba(200,255,0,0.4)] transition-all cursor-pointer"
              >
                <Send className="w-4 h-4" />
                <span>{t("demo_btn_submit")}</span>
              </button>

              <div className="flex items-center justify-center gap-2 text-[10px] font-mono text-slate-400 text-center">
                <Lock className="w-3 h-3 text-[#C8FF00]" />
                <span>{t("demo_footer_note")}</span>
              </div>
            </form>
          )}
        </div>

      </div>
    </div>
  );
}
