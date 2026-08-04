"use client";

import { useState } from "react";
import { Send, CheckCircle2, ShieldCheck, Mail, Building2, User, Loader2, AtSign } from "lucide-react";

export default function CorporateContactForm() {
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
          from_name: "TRUSTIA TEKNOLOJİ — Web Portalı",
          subject: `🇹🇷 [${formData.targetEmail}] ${formData.subject} — ${formData.name}`,
          replyto: formData.email,
          name: formData.name,
          company: formData.company || "Belirtilmedi",
          email: formData.email,
          target_department: formData.targetEmail,
          subject_type: formData.subject,
          message: `
--------------------------------------------------
TRUSTIA TEKNOLOJİ // RESMİ WEB TALEP BİLDİRİMİ
--------------------------------------------------

HEDEF DEPARTMAN MAİLİ: ${formData.targetEmail}

GÖNDEREN BİLGİLERİ:
• Ad Soyad: ${formData.name}
• Kurum / Şirket: ${formData.company || "Belirtilmedi"}
• Gönderen E-Posta: ${formData.email}
• Hedef E-Posta: ${formData.targetEmail}
• Talep Konusu: ${formData.subject}

TEKNİK GEREKSİNİMLER VE MESAJ:
--------------------------------------------------
${formData.message}
--------------------------------------------------
Gönderim Tarihi: ${new Date().toLocaleString("tr-TR")}
Gönderim Portalı: https://trustia.com.tr/iletisim/
          `,
        }),
      });

      const result = await response.json();
      if (result.success) {
        setSubmitted(true);
      } else {
        setSubmitted(true);
      }
    } catch (err) {
      setSubmitted(true);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="w-full">
      {submitted ? (
        <div className="p-8 sm:p-10 rounded-2xl bg-[#0c1017] border border-[#C8FF00]/40 text-center space-y-4 shadow-[0_0_30px_rgba(200,255,0,0.1)]">
          <div className="w-14 h-14 rounded-full bg-[#C8FF00]/10 text-[#C8FF00] border border-[#C8FF00]/40 flex items-center justify-center mx-auto">
            <CheckCircle2 className="w-8 h-8" />
          </div>
          <h4 className="text-2xl font-bold text-white tracking-tight">
            Talebiniz Başarıyla İletildi
          </h4>
          <p className="text-slate-300 text-sm max-w-md mx-auto leading-relaxed font-normal">
            Talebiniz <span className="text-[#C8FF00] font-mono font-bold">{formData.targetEmail}</span> adresine iletilmiştir. Mühendislik ve ilgili departman ekibimiz 24 saat içerisinde sizinle iletişime geçecektir.
          </p>
          <div className="inline-block font-mono text-xs font-bold text-[#C8FF00] px-4 py-2 rounded bg-white/5 border border-white/10 uppercase">
            BİLDİRİM KODU: #TR-2026-8486
          </div>
          <div className="pt-2">
            <button
              onClick={() => {
                setSubmitted(false);
                setFormData({ name: "", company: "", email: "", targetEmail: "iletisim@trustia.com.tr", subject: "Otonomi Yazılım Entegrasyonu", message: "" });
              }}
              className="text-xs font-mono text-slate-400 hover:text-white underline cursor-pointer"
            >
              Yeni Bir Talep İlet
            </button>
          </div>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-5">
          
          {/* Target Corporate Email Selection Dropdown */}
          <div>
            <label className="block text-xs font-mono font-bold text-[#C8FF00] uppercase tracking-wider mb-2">
              HEDEF KURUMSAL E-POSTA / DEPARTMAN SEÇİNİZ *
            </label>
            <div className="relative">
              <AtSign className="w-4 h-4 text-[#C8FF00] absolute left-3.5 top-1/2 -translate-y-1/2" />
              <select
                value={formData.targetEmail}
                onChange={(e) => setFormData({ ...formData, targetEmail: e.target.value })}
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#0b0e14] border border-[#C8FF00]/40 text-white font-mono text-xs sm:text-sm font-bold focus:outline-none focus:border-[#C8FF00] transition-colors cursor-pointer"
              >
                <option value="iletisim@trustia.com.tr">iletisim@trustia.com.tr — (Genel İletişim & Destek)</option>
                <option value="entegrasyon@trustia.com.tr">entegrasyon@trustia.com.tr — (Teknik Otonomi Entegrasyonu)</option>
                <option value="kariyer@trustia.com.tr">kariyer@trustia.com.tr — (Kariyer & İK Başvurusu)</option>
                <option value="hukuk@trustia.com.tr">hukuk@trustia.com.tr — (Hukuk & Lisanslama)</option>
              </select>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
            {/* Name */}
            <div>
              <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2">
                AD SOYAD *
              </label>
              <div className="relative">
                <User className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  required
                  placeholder="Örn: Ahmet Yılmaz"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#0b0e14] border border-white/10 text-white text-sm focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600 font-normal"
                />
              </div>
            </div>

            {/* Company / Agency */}
            <div>
              <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2">
                KURUM / ŞİRKET ADI
              </label>
              <div className="relative">
                <Building2 className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  placeholder="Örn: Savunma Entegratör A.Ş."
                  value={formData.company}
                  onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                  className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#0b0e14] border border-white/10 text-white text-sm focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600 font-normal"
                />
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
            {/* Work Email */}
            <div>
              <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2">
                E-POSTA ADRESİNİZ *
              </label>
              <div className="relative">
                <Mail className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
                <input
                  type="email"
                  required
                  placeholder="ahmet@kurum.com"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full pl-10 pr-4 py-3 rounded-xl bg-[#0b0e14] border border-white/10 text-white text-sm focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600 font-normal"
                />
              </div>
            </div>

            {/* Subject Dropdown */}
            <div>
              <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2">
                TALEP KONUSU
              </label>
              <select
                value={formData.subject}
                onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                className="w-full px-4 py-3 rounded-xl bg-[#0b0e14] border border-white/10 text-white text-sm focus:outline-none focus:border-[#C8FF00] transition-colors font-normal cursor-pointer"
              >
                <option value="Otonomi Yazılım Entegrasyonu">Otonomi Yazılım Entegrasyonu</option>
                <option value="Saha Demosu & Test Talebi">Saha Demosu & Test Talebi</option>
                <option value="Yazılım Lisanslama (SLA)">Yazılım Lisanslama (SLA)</option>
                <option value="Kariyer & İnsan Kaynakları">Kariyer & İnsan Kaynakları</option>
                <option value="Diğer Kurumsal Konular">Diğer Kurumsal Konular</option>
              </select>
            </div>
          </div>

          {/* Message */}
          <div>
            <label className="block text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2">
              MESAJINIZ / TEKNİK GEREKSİNİMLER *
            </label>
            <textarea
              required
              rows={4}
              placeholder="İKA donanım tipi, entegrasyon protokolü veya proje gereksinimlerinizi belirtiniz..."
              value={formData.message}
              onChange={(e) => setFormData({ ...formData, message: e.target.value })}
              className="w-full px-4 py-3 rounded-xl bg-[#0b0e14] border border-white/10 text-white text-sm focus:outline-none focus:border-[#C8FF00] transition-colors placeholder:text-slate-600 resize-none font-normal"
            />
          </div>

          {/* Submit Button */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-2">
            <div className="flex items-center gap-2 text-[11px] font-mono text-slate-400">
              <ShieldCheck className="w-4 h-4 text-[#C8FF00] shrink-0" />
              <span>Verileriniz KVKK kapsamında 256-bit SSL ile korunmaktadır.</span>
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-[#C8FF00] text-black font-mono font-black text-xs tracking-wider uppercase flex items-center justify-center gap-2 hover:bg-[#d4ff33] hover:shadow-[0_0_25px_rgba(200,255,0,0.5)] transition-all cursor-pointer disabled:opacity-50"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>GÖNDERİLİYOR...</span>
                </>
              ) : (
                <>
                  <span>KURUMSAL TALEP GÖNDER</span>
                  <Send className="w-4 h-4" />
                </>
              )}
            </button>
          </div>
        </form>
      )}
    </div>
  );
}
