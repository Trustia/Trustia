"use client";

import { useState } from "react";
import { X, ShieldCheck, Lock, Building, Mail, User, Send, CheckCircle2, UploadCloud, Download, FileText } from "lucide-react";

interface ExecutiveDemoModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function ExecutiveDemoModal({ isOpen, onClose }: ExecutiveDemoModalProps) {
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
                  NDA KORUMALI
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-normal">
                Kurumsal Platform Erişimi & Çift Yönlü Dosya Paylaşımı
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl bg-white/5 border border-white/10 text-slate-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
            aria-label="Kapat"
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
                <h3 className="text-xl font-bold text-white tracking-tight">Talebiniz Kaydedildi ve Dosyanız Alındı</h3>
                <p className="text-slate-300 text-xs sm:text-sm max-w-md mx-auto leading-relaxed">
                  Kurumsal güvenlik protokolü gereğince, temsilcimiz 24 saat içinde tarafınızla iletişime geçerek Gizlilik Anlaşmasını (NDA) başlatacaktır.
                </p>
              </div>

              {/* Instant Executive SDK Document Download Button */}
              <div className="p-4 rounded-2xl bg-[#06080b] border border-white/10 text-left space-y-3 max-w-md mx-auto">
                <div className="flex items-center gap-2 text-xs font-mono text-[#C8FF00] font-bold">
                  <FileText className="w-4 h-4" />
                  <span>DOKÜMAN İNDİRME MERKEZİ</span>
                </div>
                <p className="text-[11px] text-slate-400 leading-relaxed font-normal">
                  Sözleşme öncesi incelemeniz için hazırlanan Otonomi Yazılım Mimarisi SDK Özet Şartnamesini hemen indirebilirsiniz.
                </p>
                <a
                  href="/politika/lisans"
                  target="_blank"
                  className="w-full py-2.5 px-4 rounded-xl bg-white/10 hover:bg-white/20 border border-white/15 text-white font-mono font-bold text-xs flex items-center justify-center gap-2 transition-all cursor-pointer"
                >
                  <Download className="w-4 h-4 text-[#C8FF00]" />
                  <span>SDK & ŞARTNAME DOKÜMANINI GÖRÜNTÜLE (PDF/WEB)</span>
                </a>
              </div>

              <button
                onClick={() => { setSubmitted(false); setAttachedFile(null); onClose(); }}
                className="mt-2 px-6 py-2 rounded-xl bg-[#C8FF00] text-black font-mono font-bold text-xs uppercase tracking-wider hover:bg-[#d4ff33] transition-all cursor-pointer"
              >
                TAMAM
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <p className="text-xs text-slate-300 leading-relaxed border-l-2 border-[#C8FF00] pl-3 py-0.5 font-normal">
                Savunma entegratörleri için araç şasisi entegrasyon dosyalarını yükleyebilir, SDK şartname paketlerini talep edebilirsiniz.
              </p>

              {/* Input 1: Kurum Adı */}
              <div className="space-y-1.5">
                <label className="text-[11px] font-mono font-bold text-slate-300 uppercase flex items-center gap-1.5">
                  <Building className="w-3.5 h-3.5 text-[#C8FF00]" />
                  <span>KURUM / ŞİRKET ADI</span>
                </label>
                <input
                  type="text"
                  required
                  placeholder="Örn: HAVELSAN A.Ş. / OTOKAR / Savunma Sanayii Başkanlığı"
                  value={formData.institution}
                  onChange={(e) => setFormData({ ...formData, institution: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/10 text-white text-xs placeholder:text-slate-500 focus:outline-none focus:border-[#C8FF00] transition-colors"
                />
              </div>

              {/* Input 2: Unvan & E-Posta Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <label className="text-[11px] font-mono font-bold text-slate-300 uppercase flex items-center gap-1.5">
                    <User className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>YETKİLİ UNVANI</span>
                  </label>
                  <input
                    type="text"
                    required
                    placeholder="Örn: Otonomi Mühendisi"
                    value={formData.title}
                    onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                    className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/10 text-white text-xs placeholder:text-slate-500 focus:outline-none focus:border-[#C8FF00] transition-colors"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-[11px] font-mono font-bold text-slate-300 uppercase flex items-center gap-1.5">
                    <Mail className="w-3.5 h-3.5 text-[#C8FF00]" />
                    <span>KURUMSAL E-POSTA</span>
                  </label>
                  <input
                    type="email"
                    required
                    placeholder="ad.soyad@kurum.com.tr"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    className="w-full px-4 py-2.5 rounded-xl bg-[#06080b] border border-white/10 text-white text-xs placeholder:text-slate-500 focus:outline-none focus:border-[#C8FF00] transition-colors"
                  />
                </div>
              </div>

              {/* Input 3: File Upload Box (Müşterinin Araç Şasisi / Şartname Dosyasını Yüklemesi İçin) */}
              <div className="space-y-1.5">
                <label className="text-[11px] font-mono font-bold text-slate-300 uppercase flex items-center gap-1.5">
                  <UploadCloud className="w-3.5 h-3.5 text-[#C8FF00]" />
                  <span>ŞASİ & SENSÖR ŞARTNAME DOSYASI YÜKLE (OPSİYONEL)</span>
                </label>
                <div className="relative border-2 border-dashed border-white/15 rounded-xl p-3 text-center bg-[#06080b] hover:border-[#C8FF00]/50 transition-colors group cursor-pointer">
                  <input
                    type="file"
                    onChange={handleFileChange}
                    accept=".pdf,.zip,.docx,.png,.jpg"
                    className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                  />
                  <div className="flex items-center justify-center gap-2 text-xs font-mono text-slate-300">
                    <UploadCloud className="w-4 h-4 text-[#C8FF00] group-hover:scale-110 transition-transform" />
                    {attachedFile ? (
                      <span className="text-[#C8FF00] font-bold">{attachedFile.name} (Yüklendi)</span>
                    ) : (
                      <span>Dosya Sürükleyin veya Seçin (.pdf, .zip, .docx)</span>
                    )}
                  </div>
                </div>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                className="w-full mt-2 py-3.5 rounded-xl bg-[#C8FF00] hover:bg-[#d4ff33] text-black font-mono font-black text-xs uppercase tracking-wider flex items-center justify-center gap-2 shadow-[0_0_20px_rgba(200,255,0,0.3)] transition-all cursor-pointer"
              >
                <Send className="w-4 h-4" />
                <span>DEMO & DOSYA GÖNDER</span>
              </button>
            </form>
          )}
        </div>

        {/* Footer Note */}
        <div className="px-6 py-3 bg-[#06080b] border-t border-white/10 flex items-center justify-between text-[11px] font-mono text-slate-400 shrink-0">
          <span className="flex items-center gap-1.5 text-slate-300">
            <Lock className="w-3.5 h-3.5 text-[#C8FF00]" />
            Dosya transferiniz HMAC-256 şifrelemeyle korunur.
          </span>
          <span>TRUSTIA TEKNOLOJİ</span>
        </div>
      </div>
    </div>
  );
}
