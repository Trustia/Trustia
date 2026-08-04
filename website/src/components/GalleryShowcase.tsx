"use client";

import { ShieldCheck, Cpu, Radio, Eye } from "lucide-react";

export default function GalleryShowcase() {
  return (
    <section className="relative w-full py-16 px-4 sm:px-8 max-w-[1440px] mx-auto z-20 bg-[#090c10] border-t border-b border-white/10">
      
      {/* Section Header */}
      <div className="text-center max-w-2xl mx-auto mb-12 space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#C8FF00]/10 border border-[#C8FF00]/30 text-[#C8FF00] text-xs font-mono font-bold tracking-widest uppercase">
          <Eye className="w-3.5 h-3.5" />
          <span>SAHA OPERASYON FOTO GALERİSİ</span>
        </div>
        <h3 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          Saha Testleri ve İKA Entegrasyon Kataloğu
        </h3>
        <p className="text-slate-400 text-xs sm:text-sm font-normal">
          Farklı şasi ve sensör konfigürasyonlarında çalışan otonom yazılım beyni görselleri
        </p>
      </div>

      <div className="max-w-6xl mx-auto space-y-6">
        
        {/* ROW 1: 3 Rectangular 16:9 Photos Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          
          {/* Photo 1: HAVELSAN BARKAN UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/1.webp"
              alt="HAVELSAN BARKAN Otonom İKA Saha Arazi Testi"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">01 // SAHA ARAZİ TESTİ</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">BARKAN İKA</span>
            </div>
          </div>

          {/* Photo 2: OTOKAR ALPAR Heavy UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/2.jpg"
              alt="OTOKAR ALPAR Sensör Kulesi ve Radar Füzyonu"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">02 // SENSÖR FÜZYONU</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">ALPAR İKA</span>
            </div>
          </div>

          {/* Photo 3: Tactical Offroad High Mobility UGV Chassis */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/3.jpeg"
              alt="Taktik Otonom Sürüş Şasisi Engel Kaçınma Testi"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">03 // ENGEL KAÇINMA</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">HYBRID A*</span>
            </div>
          </div>

        </div>

        {/* ROW 2: 2 Center Photos (Exact 16:9 Aspect Ratio) + Left & Right Flanking Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 items-center">
          
          {/* LEFT BOŞLUK DOLGUSU: Tactical Telemetry Card 1 */}
          <div className="p-5 rounded-2xl bg-[#0e121a] border border-white/10 flex flex-col justify-between aspect-video shadow-2xl">
            <div className="space-y-1.5">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Cpu className="w-3.5 h-3.5" />
                <span>CAN FD & ROS 2 TELEMETRİ</span>
              </div>
              <h4 className="text-xs font-bold text-white">Donanım Sürücü Köprüsü</h4>
              <p className="text-slate-400 text-[11px] leading-relaxed font-normal line-clamp-2">
                Araç aktüatörleri ve motor sürücüleri ile 1ms altında kesintisiz veri alışverişi.
              </p>
            </div>
            <div className="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono text-emerald-400">
              <span>DURUM: AKTİF</span>
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            </div>
          </div>

          {/* CENTER Photo 4: HAVELSAN KAPGAN 8x8 Heavy UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/4.jpg"
              alt="HAVELSAN KAPGAN 8x8 Ağır İKA Tehdit Füzyonu Testi"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">04 // TEHDİT FÜZYONU</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">KAPGAN 8x8</span>
            </div>
          </div>

          {/* CENTER Photo 5: ENGA 6x6 Tactical UGV */}
          <div className="relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl aspect-video bg-[#07090c]">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="/gallery/5.jpg"
              alt="ENGA 6x6 Taktik İKA Çoklu Sürü Harekatı"
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
            <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs font-mono text-slate-200">
              <span className="font-bold text-white text-[11px]">05 // SÜRÜ FORMASYONU</span>
              <span className="text-[#C8FF00] text-[9px] bg-black/60 px-1.5 py-0.5 rounded border border-white/10 font-bold">ENGA 6x6</span>
            </div>
          </div>

          {/* RIGHT BOŞLUK DOLGUSU: Tactical Cyber Security Card 2 */}
          <div className="p-5 rounded-2xl bg-[#0e121a] border border-white/10 flex flex-col justify-between aspect-video shadow-2xl">
            <div className="space-y-1.5">
              <div className="flex items-center gap-1.5 text-[10px] font-mono text-[#C8FF00] font-bold uppercase">
                <Radio className="w-3.5 h-3.5" />
                <span>HMAC-SHA256 ŞİFRELEME</span>
              </div>
              <h4 className="text-xs font-bold text-white">Telsiz & LinkLoss Güvenliği</h4>
              <p className="text-slate-400 text-[11px] leading-relaxed font-normal line-clamp-2">
                Sinyal kesintisinde otonom eve dönüş (RTH) ve şifreli komut doğrulama.
              </p>
            </div>
            <div className="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono text-[#C8FF00]">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>STANAG 4586</span>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
