import os
import sys
import shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register Turkish Fonts
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'C:/Windows/Fonts/ariali.ttf'))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont('Arial', 8)
        self.setFillColor(colors.HexColor('#64748b'))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 810, 'TRUSTIA AI  |  SEVİYE-4 OTONOM ROBOTAKSİ & KİTLE FONLAMASI MASTER PLANI')
            self.drawRightString(559, 810, 'İTO BTM FULYA KAMPÜSÜ  •  EYLÜL 2026')
            self.setStrokeColor(colors.HexColor('#e2e8f0'))
            self.setLineWidth(0.5)
            self.line(36, 804, 559, 804)
        
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor('#e2e8f0'))
        self.setLineWidth(0.5)
        self.line(36, 36, 559, 36)
        self.drawString(36, 24, 'GİZLİ & KURUMSAL  •  Trustia Teknoloji A.Ş.  •  https://trustia.com.tr')
        self.drawRightString(559, 24, f'Sayfa {self._pageNumber} / {page_count}')
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=46
    )
    
    # Custom Palette
    c_primary = colors.HexColor('#0f172a')    # Dark Slate
    c_accent = colors.HexColor('#0284c7')     # Ocean Blue
    c_cyan = colors.HexColor('#0ea5e9')       # Cyan
    c_dark = colors.HexColor('#1e293b')
    c_light = colors.HexColor('#f8fafc')
    c_success = colors.HexColor('#059669')
    
    # Styles
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Arial-Bold',
        fontSize=17,
        leading=21,
        textColor=c_primary,
        alignment=0
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Arial-Bold',
        fontSize=10,
        leading=13,
        textColor=c_accent,
        alignment=0
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        fontName='Arial-Bold',
        fontSize=11,
        leading=15,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=4
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        fontName='Arial-Bold',
        fontSize=9,
        leading=13,
        textColor=c_accent,
        spaceBefore=6,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        fontName='Arial',
        fontSize=8,
        leading=11.5,
        textColor=c_dark,
        spaceAfter=3
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Arial',
        fontSize=7.5,
        leading=9.5,
        textColor=c_dark
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Arial-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=c_primary
    )
    
    table_cell_header = ParagraphStyle(
        'TableCellHeader',
        fontName='Arial-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white
    )
    
    story = []
    
    # ==================== KAPAK / BAŞLIK ====================
    story.append(Paragraph('TRUSTIA AI  |  MİLLİ OTONOM MOBİLİTE PLATFORMU', subtitle_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("TÜRKİYE'NİN İLK SEVİYE-4 OTONOM ROBOTAKSİ & PAYLAŞIMLI MOBİLİTE MASTER PLANI (2026)", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Yönetici Karar Raporu:</b> 15.000.000 TL Kitle Fonlaması Bütçesi, Hyundai Ioniq 5 Retrofit Kiti, 16M İstanbul Operasyonu ve Kuruşu Kuruşuna Fon Kullanım Mimarisi", body_style))
    story.append(Spacer(1, 4))
    
    # Meta Box
    meta_data = [
        [
            Paragraph("<b>Kurucu & CEO:</b> Murat Furkan Bayram (17 Yaşında, Sistem Mimarı, %80 Hisse)", table_cell),
            Paragraph("<b>Resmi Konum:</b> İTO BTM Fulya Kampüsü, Şişli / İstanbul", table_cell)
        ],
        [
            Paragraph("<b>Kurucu Ortak & Operasyon:</b> Doğukan Bayram (%20 Hisse, Reşit Temsilci)", table_cell),
            Paragraph("<b>Resmi Tesciller:</b> BTK Akademi • KOSGEB İleri Girişimci • TÜBİTAK ARBİS", table_cell)
        ],
        [
            Paragraph("<b>Donanım Entegrasyon:</b> Denizcan Özcan (İÜC EEE 3.44 GPA, ASELSAN Havuzu)", table_cell),
            Paragraph("<b>Platform & Hedef:</b> fonbulucu.com • 15M TL Taban (%20 Ek Fonlama ile 18M TL)", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[260, 263])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))
    
    # ==================== BÖLÜM 1: STRATEJİK VİZYON ====================
    story.append(Paragraph("1. STRATEJİK VİZYON VE ETİK DURUŞ (THE NORTH STAR)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    p1 = ("<b>Tek ve Net Odak:</b> Trustia AI; enerjisini askeri ihaleler, tarım veya lisanslar arasında dağıtmayıp, tüm gücünü "
          "<b>Türkiye'nin İlk Sivil Seviye-4 Otonom Yolcu Aracını (Hyundai Ioniq 5) yola çıkarmaya</b> odaklamıştır. Askeri İKA ve tarım "
          "algoritmalarımız hazır durumdadır; ancak ana vitrinimiz ve milyar dolarlık pazarımız sivil otonom mobilitedir.<br/>"
          "<b>Kimsenin Ekmeğiyle Oynamadan Geleceği İnşa Etmek:</b> 16 milyonluk İstanbul'da sadece 19.000 sarı taksi bulunmakta olup "
          "kronik bir araç krizi yaşanmaktadır. Trustia AI, taksicilerin ekmeğini elinden alan bir düşman değil; Oğuz Alper Öktem'in (Martı TAG) "
          "açtığı yolda taksi esnafı ve filo sahiplerinin gelecekte kendi robotaksilerini işletebilmelerini sağlayacak milli otonomi altyapısıdır.")
    story.append(Paragraph(p1, body_style))
    story.append(Spacer(1, 4))
    
    # ==================== BÖLÜM 2: DONANIM & HYUNDAI IONIQ 5 ====================
    story.append(Paragraph("2. DÜNYANIN EN İYİ PLATFORM ARACI VE SEVİYE-4 DONANIM PAKETİ (BOM)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    p3 = ("<b>Neden Hyundai Ioniq 5 (E-GMP)?</b> 800V mimarisiyle <b>18 dakikada</b> şarj olur. Comma.ai tarafından açık CAN-FD steer-by-wire "
          "protokolleri çözülmüş, yazılımla doğrudan direksiyon ve fren kontrolüne izin veren dünyadaki en açık elektrikli platformdur. "
          "Waymo ve Motional'ın da resmi küresel tercihidir.")
    story.append(Paragraph(p3, body_style))
    story.append(Spacer(1, 2))
    
    # BOM Table
    bom_data = [
        [Paragraph("Bileşen / Parça", table_cell_header), Paragraph("Model & Teknik Özellik", table_cell_header), Paragraph("Görev & Fonksiyon", table_cell_header), Paragraph("Maliyet (TL)", table_cell_header)],
        [Paragraph("<b>Ana 3D LiDAR</b>", table_cell_bold), Paragraph("Ouster OS2-128 (128 Kanal, 200m+)", table_cell), Paragraph("Tavan 360° uzun menzilli nokta bulutu & 3D NDT SLAM", table_cell), Paragraph("530.000 TL", table_cell_bold)],
        [Paragraph("<b>Kör Nokta LiDAR</b>", table_cell_bold), Paragraph("2x Livox Mid-360 (Katı Hal)", table_cell), Paragraph("Ön sağ/sol çamurluk kör nokta yaya ve engel algılama", table_cell), Paragraph("65.000 TL", table_cell_bold)],
        [Paragraph("<b>Yapay Zeka Beyin</b>", table_cell_bold), Paragraph("NVIDIA Jetson AGX Orin 64GB (275 TOPS)", table_cell), Paragraph("Gömülü Linux, TensorRT deterministik derin öğrenme", table_cell), Paragraph("95.000 TL", table_cell_bold)],
        [Paragraph("<b>RTK GNSS + IMU</b>", table_cell_bold), Paragraph("Septentrio Dual Anten + Endüstriyel IMU", table_cell), Paragraph("Santimetre hassasiyetinde küresel konum & açısal hız", table_cell), Paragraph("85.000 TL", table_cell_bold)],
        [Paragraph("<b>HDR Kameralar</b>", table_cell_bold), Paragraph("4x GMSL2 Otomotiv Kamerası (Sony Sensör)", table_cell), Paragraph("Trafik ışığı, şerit çizgileri, tabela ve yaya tespiti", table_cell), Paragraph("45.000 TL", table_cell_bold)],
        [Paragraph("<b>CAN-FD Arayüzü</b>", table_cell_bold), Paragraph("Kvaser U100 CAN-FD / Comma Panda", table_cell), Paragraph("Aracın ADAS ve direksiyon kontrol ünitesine doğrudan erişim", table_cell), Paragraph("38.000 TL", table_cell_bold)],
        [Paragraph("<b>Mekanik & Enerji</b>", table_cell_bold), Paragraph("Özel Tavan Barı, PDU Panosu, DC-DC Regülatör", table_cell), Paragraph("Tavan montaj podu, 12V/24V regüle güç dağıtımı", table_cell), Paragraph("122.000 TL", table_cell_bold)],
        [Paragraph("<b>TOPLAM DONANIM</b>", table_cell_bold), Paragraph("<b>27 Parçalık Eksiksiz Seviye-4 Dönüşüm Kiti</b>", table_cell_bold), Paragraph("<b>Anahtar Teslim Modüler Retrofit Mimarisi</b>", table_cell_bold), Paragraph("<b>980.000 TL</b>", table_cell_bold)]
    ]
    bom_table = Table(bom_data, colWidths=[95, 175, 173, 80])
    bom_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#e0f2fe')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(bom_table)
    story.append(Spacer(1, 6))
    
    # ==================== BÖLÜM 3: YAZILIM & GÜVENLİK ====================
    story.append(Paragraph("3. KANITLANMIŞ YAZILIM MİMARİSİ VE TEKNOLOJİK OLGUNLUK (TRL-6)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    p4 = ("• <b>16.000 Satır Özgün Deterministik Motor:</b> Sıfırdan C++17/20 ve Python ile geliştirilen mimarimiz;<br/>"
          "• <b>3D NDT LiDAR SLAM:</b> GPS sinyali kesilse bile (tünel, Maslak gökdelen kanyonu) 5 cm hassasiyetle lokalizasyon sağlar.<br/>"
          "• <b>Kinematik Hybrid A* & Pure Pursuit:</b> <15 ms çevrim süresiyle deterministik güvenli rota çizer ve direksiyon açısını yönetir.<br/>"
          "• <b>1.301 / 1.301 Otomatik Test:</b> %100 başarıyla CI/CD hatlarında doğrulanmıştır.")
    story.append(Paragraph(p4, body_style))
    
    # ==================== BÖLÜM 4: İSTANBUL OPERASYONU ====================
    story.append(PageBreak()) # Sayfa 2
    story.append(Paragraph("4. 16 MİLYONLUK İSTANBUL ROBOTAKSİ OPERASYON PLANI", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    p5 = ("<b>Mobil Uygulama (Trustia Ride):</b> 1. <i>Tarihli & Saatli Rezervasyon:</i> Uçuş veya toplantı öncesi saat seçilir; araç 5 dakika önce biniş cebine yanaşır. 2. <i>Anlık Çağırma (On-Demand):</i> En yakın bekleme noktasındaki araç çağrılır; ücret yolculuk öncesi sabittir.<br/>"
          "<b>Kabin Protokolü & 3 Yolcu:</b> Ön koltuk TAMAMEN BOŞTUR (sürücüsüz). Arkada en fazla 3 yolcu seyahat eder. E-GMP düz tabanı limuzin ferahlığı sunar. Arka tablette klima, Spotify ve canlı 3D LiDAR algı ekranı ile 'Acil Durum Kenara Çek' butonu yer alır.<br/>"
          "<b>3 Pilot Koridor:</b> 1. <i>Havalimanı Express (İST Havalimanı ↔ Maslak / Levent / BTM Fulya).</i> 2. <i>Finans Hattı (BTM Fulya ↔ Levent ↔ Vadistanbul).</i> 3. <i>Banliyö Ringi (Bahçeşehir ↔ Olimpiyat/Mahmutbey Metro).</i><br/>"
          "<b>Filo Lojistiği & Şarj:</b> Staging Hubs (AVM ve BTM otopark cepleri). 18 dakikada Trugo/ZES 350 kW DC hızlı şarj. Gece 01:00-05:00 buharlı antibakteriyel koltuk temizliği, sensör optik bakımı ve telemetri teşhisi. Otonom ticari filo kaskosu ile kara kutu güvencesi.")
    story.append(Paragraph(p5, body_style))
    story.append(Spacer(1, 6))
    
    # ==================== BÖLÜM 5: FİYATLANDIRMA & EKONOMİ ====================
    story.append(Paragraph("5. FİYATLANDIRMA MODELİ VE BİRİM EKONOMİ (SARI TAKSİDEN KAT KAT UCUZ)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    # Price Table
    price_data = [
        [Paragraph("Parametre / Mesafe", table_cell_header), Paragraph("UKOME 2026 Sarı Taksi", table_cell_header), Paragraph("Trustia AI Seviye-4 Robotaksi", table_cell_header), Paragraph("Vatandaşın Kazancı", table_cell_header)],
        [Paragraph("<b>Açılış Ücreti</b>", table_cell_bold), Paragraph("71,94 TL", table_cell), Paragraph("<b>25,00 TL</b>", table_cell_bold), Paragraph("<b>%65 Daha Ucuz</b>", table_cell_bold)],
        [Paragraph("<b>Kilometre Başı</b>", table_cell_bold), Paragraph("47,92 TL", table_cell), Paragraph("<b>18,50 TL</b>", table_cell_bold), Paragraph("<b>%61 Daha Ucuz</b>", table_cell_bold)],
        [Paragraph("<b>İndi-Bindi (Kısa Mesafe)</b>", table_cell_bold), Paragraph("<b>230,00 TL (Zorunlu)</b>", table_cell), Paragraph("<b>YOK (Sıfır İndi-Bindi Cezası)</b>", table_cell_bold), Paragraph("<b>Tam Adalet</b>", table_cell_bold)],
        [Paragraph("<b>1.5 km Kısa Yolculuk</b>", table_cell_bold), Paragraph("230,00 TL", table_cell), Paragraph("<b>52,75 TL</b>", table_cell_bold), Paragraph("<b>4 KAT DAHA UCUZ!</b>", table_cell_bold)],
        [Paragraph("<b>10 km Şehir İçi Yolculuk</b>", table_cell_bold), Paragraph("~700,00 TL (Trafikle)", table_cell), Paragraph("<b>~250,00 TL (Sabit & Şeffaf)</b>", table_cell_bold), Paragraph("<b>%64 Daha Ucuz!</b>", table_cell_bold)],
        [Paragraph("<b>Enerji Maliyeti (100 km)</b>", table_cell_bold), Paragraph("~380 TL (Dizel 8.5L)", table_cell), Paragraph("<b>~64 TL (Elektrik 16 kWh)</b>", table_cell_bold), Paragraph("<b>6 Kat Düşük Enerji</b>", table_cell_bold)]
    ]
    price_table = Table(price_data, colWidths=[125, 135, 145, 118])
    price_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#fef3c7')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(price_table)
    story.append(Spacer(1, 4))
    
    p9 = ("<b>Tek Bir Aracın Günlük & Aylık Nakit Akışı:</b> Günlük 16 Sefer (220 km) = <b>5.040 TL Günlük Ciro</b> (Aylık ~151.200 TL). "
          "Günlük Toplam Gider (Şarj + Temizlik + Kasko/Bakım + Otopark) = <b>590 TL</b>. "
          "<b>Tek Bir Aracın Günlük Net Kârı: 4.450 TL  |  Aylık Net Kârı: 133.500 TL NET NAKİT!</b>")
    story.append(Paragraph(p9, body_style))
    
    # ==================== BÖLÜM 6: KİTLE FONLAMASI ====================
    story.append(PageBreak()) # Sayfa 3
    story.append(Paragraph("6. FONBULUCU.COM KİTLE FONLAMASI VE KURUŞU KURUŞUNA BÜTÇE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    # Campaign Summary Box
    camp_summary = [
        [Paragraph("<b>Taban Hedef Fon:</b> 15.000.000 TL (~400.000 $)", table_cell_bold), Paragraph("<b>Ek Fonlama Tavanı (%20):</b> 18.000.000 TL (~475.000 $)", table_cell_bold)],
        [Paragraph("<b>Şirket Ön Değerlemesi:</b> 150.000.000 TL (~4M $)", table_cell), Paragraph("<b>Yatırımcıya Arz Edilen Pay:</b> %8.5 — %10.0", table_cell_bold)],
        [Paragraph("<b>Kurucularda Kalan Pay:</b> %90.0 — %91.5", table_cell_bold), Paragraph("<b>Platform:</b> fonbulucu.com (SPK Lisanslı)", table_cell)]
    ]
    camp_table = Table(camp_summary, colWidths=[260, 263])
    camp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1, c_success),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bbf7d0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(camp_table)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Kuruşu Kuruşuna Fon Kullanım Raporu (Use of Funds - 15.000.000 TL):</b>", h2_style))
    
    use_data = [
        [Paragraph("Harcama Kalemi", table_cell_header), Paragraph("Bütçe (TL)", table_cell_header), Paragraph("Oran", table_cell_header), Paragraph("Detay ve Gerekçe", table_cell_header)],
        [Paragraph("<b>Hyundai Ioniq 5 Test Aracı</b>", table_cell_bold), Paragraph("2.600.000 TL", table_cell_bold), Paragraph("%17.3", table_cell), Paragraph("Düşük kilometreli, 800V E-GMP elektrikli şasi şirketin tapulu demirbaşı olur.", table_cell)],
        [Paragraph("<b>Seviye-4 Sensör Kiti (BOM)</b>", table_cell_bold), Paragraph("1.150.000 TL", table_cell_bold), Paragraph("%7.7", table_cell), Paragraph("Ouster 128-LiDAR, 2x Livox Mid-360, Jetson Orin 64GB, Septentrio RTK, 4x Kamera.", table_cell)],
        [Paragraph("<b>Mekanik Montaj & Tavan Podu</b>", table_cell_bold), Paragraph("150.000 TL", table_cell_bold), Paragraph("%1.0", table_cell), Paragraph("Alüminyum tavan barı, CNC sensör braketleri, PDU güç panosu ve kablolama.", table_cell)],
        [Paragraph("<b>Çekirdek Mühendislik Ekibi</b>", table_cell_bold), Paragraph("5.200.000 TL", table_cell_bold), Paragraph("%34.7", table_cell), Paragraph("<b>18 Aylık Runway:</b> Murat (Sistem Mimarı), Denizcan (Donanım) ve test mühendisi maaşları.", table_cell)],
        [Paragraph("<b>Pist Testleri, Saha & Kasko</b>", table_cell_bold), Paragraph("2.100.000 TL", table_cell_bold), Paragraph("%14.0", table_cell), Paragraph("Bilişim Vadisi pist kiralama, kapalı alan testleri, ticari otonom kasko ve 18 aylık şarj.", table_cell)],
        [Paragraph("<b>SPK, Şirket Kuruluş & Patent</b>", table_cell_bold), Paragraph("1.800.000 TL", table_cell_bold), Paragraph("%12.0", table_cell), Paragraph("A.Ş. kuruluşu, fonbulucu komisyonu, Takasbank/MKK harçları ve TürkPatent tescili.", table_cell)],
        [Paragraph("<b>Acil Durum Rezervi (%10)</b>", table_cell_bold), Paragraph("1.400.000 TL", table_cell_bold), Paragraph("%9.3", table_cell), Paragraph("Kur dalgalanması, gümrük vergisi ve yedek sensör stoğu için güvence fonu.", table_cell)],
        [Paragraph("<b>Lansman & 4K Video Filmi</b>", table_cell_bold), Paragraph("600.000 TL", table_cell_bold), Paragraph("%4.0", table_cell), Paragraph("Boş koltuklu 4K sinematik video prodüksiyonu, egirişim PR ve BTM Demo Day lansmanı.", table_cell)],
        [Paragraph("<b>TOPLAM HEDEF BÜTÇE</b>", table_cell_bold), Paragraph("<b>15.000.000 TL</b>", table_cell_bold), Paragraph("<b>%100</b>", table_cell_bold), Paragraph("<b>18 Aylık Eksiksiz Anahtar Teslim Robotaksi Operasyonu</b>", table_cell_bold)]
    ]
    use_table = Table(use_data, colWidths=[130, 85, 45, 263])
    use_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#e0f2fe')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(use_table)
    story.append(Spacer(1, 4))
    
    p10 = ("<b>Bütçe Esnekliği ve Şirket İçi Kullanım Serbestisi:</b> Takasbank blokesi çözüldüğünde para doğrudan Trustia A.Ş.'nin banka hesabına geçer. "
           "Tek harcama yetkilisi Yönetim Kurulu'dur (Murat & Doğukan). 'Mühendislik Ekibi' bütçesi zaten Murat ve çekirdek kurucuların yasal maaşıdır; "
           "her ay şahsi hesaplara yatar. Maaş veya operasyondan artan bütçe Yönetim Kurulu Kararı ile doğrudan 2. araç alımına, daha üst LiDAR'lara veya "
           "sunucuya kaydırılabilir. Bu SPK ve bağımsız mali denetim nezdinde tamamen yasaldır.")
    story.append(Paragraph(p10, body_style))
    
    # ==================== BÖLÜM 7: YÖNETİM & MÜHENDİSLİK HEYETİ ====================
    story.append(PageBreak()) # Sayfa 4
    story.append(Paragraph("7. KURUCU YÖNETİM VE MÜHENDİSLİK HEYETİ (EXECUTIVE DOSSIER)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    team_data = [
        [
            Paragraph("<b>MURAT FURKAN BAYRAM</b><br/><i>Kurucu & CEO / Baş Sistem Mimarı (%80 Hisse)</i><br/><br/>"
                      "• <b>Yaş & Yetkinlik:</b> 17 Yaşında sistem mimarı. 16.000 satır deterministik C++/Python otonomi motorunun tek mimarı.<br/>"
                      "• <b>Teknik Derinlik:</b> 3D NDT LiDAR SLAM, Kinematic Hybrid A*, Pure Pursuit, CAN-FD Drive-by-Wire, ROS2 Humble.<br/>"
                      "• <b>Resmi Tesciller:</b> KOSGEB İleri Girişimci (KSB01UGE0115153370), TÜBİTAK ARBİS Milli Araştırmacı, BTK Akademi Savunma Sertifikası.<br/>"
                      "• <b>Kurumsal Temsil:</b> İTO BTM Fulya Kampüsü Yerleşik Girişimcisi, Startups.watch doğrulanmış kurucusu.", table_cell),
            Paragraph("<b>DENİZCAN ÖZCAN</b><br/><i>Donanım & Robotik Entegrasyon Mühendisi</i><br/><br/>"
                      "• <b>Eğitim:</b> İstanbul Üniversitesi-Cerrahpaşa Elektrik-Elektronik Mühendisliği 4. Sınıf (3.44 GPA).<br/>"
                      "• <b>Savunma & Robotaksi:</b> <b>ASELSAN Aday Mühendis Havuzu</b> & <b>TEKNOFEST Robotaksi Finalisti</b>.<br/>"
                      "• <b>Donanım Uzmanlığı:</b> Araç CAN-FD / CAN-Bus hat dinleme, FPGA, sensör kablolama, PDU güç dağıtımı, kalibrasyon.<br/>"
                      "• <b>Rolü:</b> Hyundai Ioniq 5'in fiziksel kablolama, tavan podu ve Jetson Orin donanım entegrasyonundan sorumlu lider.", table_cell)
        ],
        [
            Paragraph("<b>DOĞUKAN BAYRAM</b><br/><i>Kurucu Ortak & Operasyon Direktörü (%20 Hisse)</i><br/><br/>"
                      "• <b>Rol & Yetki:</b> Reşit kurucu ortak ve şirketin resmi imza yetkilisi.<br/>"
                      "• <b>Sorumluluklar:</b> SPK yasal süreçleri, Takasbank/MKK entegrasyonu, İTO BTM ve devlet hibe ilişkileri.<br/>"
                      "• <b>Operasyonel Güç:</b> Filo kiralama, lojistik anlaşmaları ve saha bekleme hub'larının resmi yönetimi.", table_cell),
            Paragraph("<b>GÖMÜLÜ SİSTEM & TEST MÜHENDİSİ</b><br/><i>(Fonlama Sonrası İstihdam Edilecek 3. Mühendis)</i><br/><br/>"
                      "• <b>Rol:</b> Bilişim Vadisi test pistinde 7/24 araç başında telemetri ve acil durum MRM testlerini yürütecek saha mühendisi.<br/>"
                      "• <b>Bütçe:</b> 18 aylık maaşı ve SGK payı fonlama bütçesinde garanti altına alınmıştır.", table_cell)
        ]
    ]
    team_table = Table(team_data, colWidths=[260, 263])
    team_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(team_table)
    story.append(Spacer(1, 6))
    
    # ==================== BÖLÜM 8: YOL HARİTASI & NİHAİ KARAR ====================
    story.append(Paragraph("8. KAMPANYA SONRASI 12 AYLIK KİLOMETRE TAŞLARI (ROADMAP)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_accent, spaceBefore=1, spaceAfter=4))
    
    road_data = [
        [Paragraph("Dönem", table_cell_header), Paragraph("Ulaşılacak Somut Hedef (Milestone)", table_cell_header), Paragraph("Çıktı & Doğrulama", table_cell_header)],
        [Paragraph("<b>Ay 1</b>", table_cell_bold), Paragraph("Takasbank'tan fonun kasaya geçmesi, A.Ş. tescili, Hyundai Ioniq 5 aracının satın alınması.", table_cell), Paragraph("Araç ruhsatı & şirket bilançosu.", table_cell)],
        [Paragraph("<b>Ay 2</b>", table_cell_bold), Paragraph("Ouster 128-LiDAR, Jetson Orin ve sensörlerin Denizcan tarafından araca montajı ve kalibrasyonu.", table_cell), Paragraph("Canlı sensör veri akışı & CAN-FD testi.", table_cell)],
        [Paragraph("<b>Ay 3</b>", table_cell_bold), Paragraph("Bilişim Vadisi Test Pisti'nde kapalı alan ilk boş sürücü koltuklu test sürüşü ve 4K sinematik video çekimi.", table_cell), Paragraph("<b>TÜRKİYE LANSMAN VİDEOSU YAYINI.</b>", table_cell_bold)],
        [Paragraph("<b>Ay 4 - 6</b>", table_cell_bold), Paragraph("Oğuz Alper Öktem (Martı TAG) ile robotaksi pilot protokolü masasına oturulması ve BTM Fulya ringi.", table_cell), Paragraph("Martı Autonomous Pilot Sözleşmesi.", table_cell)],
        [Paragraph("<b>Ay 7 - 12</b>", table_cell_bold), Paragraph("Trustia Ride mobil uygulaması ile ilk 100 davetli yolcunun taşınması ve Seri A turuna hazırlık.", table_cell), Paragraph("Şirket değerlemesinin 500M TL'ye çıkması.", table_cell_bold)]
    ]
    road_table = Table(road_data, colWidths=[65, 310, 148])
    road_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(road_table)
    story.append(Spacer(1, 8))
    
    # Signature Box
    sig_p = ("<b>NİHAİ ONAY VE KURUCU TAAHHÜDÜ:</b> "
             "İşbu belge; Trustia AI'ın Seviye-4 otonom robotaksi operasyonunu, 15.000.000 TL fonbulucu kitle fonlaması başvurusunu ve "
             "kurumsal büyüme stratejisini eksiksiz olarak kayıt altına almaktadır.<br/>"
             "<b>Murat Furkan Bayram</b> (Kurucu & CEO / Sistem Mimarı, %80) • "
             "<b>Doğukan Bayram</b> (Kurucu Ortak & Operasyon, %20) • "
             "<b>Denizcan Özcan</b> (Donanım Lideri) • "
             "<b>İTO Bilgiyi Ticarileştirme Merkezi (BTM) Fulya Kampüsü, Beşiktaş / İstanbul</b>")
    story.append(Paragraph(sig_p, body_style))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated: {filename}")

if __name__ == '__main__':
    out_pdf1 = 'c:/Users/Murat/Desktop/Trustia/04_Yatirimci_Sunumlari_ve_Is_Planlari/Trustia_AI_Seviye4_Robotaksi_ve_Kitle_Fonlamasi_Master_Plan_2026.pdf'
    out_pdf2 = 'C:/Users/Murat/Desktop/Çıktı/Trustia_AI_Seviye4_Robotaksi_ve_Kitle_Fonlamasi_Master_Plan_2026.pdf'
    
    build_pdf(out_pdf1)
    shutil.copy(out_pdf1, out_pdf2)
    print(f"Copied to desktop folder: {out_pdf2}")
