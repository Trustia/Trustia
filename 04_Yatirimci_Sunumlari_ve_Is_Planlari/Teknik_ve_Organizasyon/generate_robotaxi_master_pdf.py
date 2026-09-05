import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image as RLImage
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import shutil

# Register TrueType Fonts with Turkish character support
font_regular = 'C:/Windows/Fonts/arial.ttf'
font_bold = 'C:/Windows/Fonts/arialbd.ttf'
font_italic = 'C:/Windows/Fonts/ariali.ttf'

pdfmetrics.registerFont(TTFont('Arial', font_regular))
pdfmetrics.registerFont(TTFont('Arial-Bold', font_bold))
pdfmetrics.registerFont(TTFont('Arial-Italic', font_italic))

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
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFillColor(colors.HexColor('#0F172A'))
            self.setFont('Arial-Bold', 8)
            self.drawString(14*mm, 285*mm, "TRUSTIA AI")
            self.setFont('Arial', 8)
            self.setFillColor(colors.HexColor('#64748B'))
            self.drawString(32*mm, 285*mm, "|  Hyundai Ioniq 5 Seviye-4 Robotaksi Entegrasyon & Donanım Master Planı")
            
            self.setStrokeColor(colors.HexColor('#CBD5E1'))
            self.setLineWidth(0.75)
            self.line(14*mm, 282*mm, 196*mm, 282*mm)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.75)
        self.line(14*mm, 14*mm, 196*mm, 14*mm)
        
        self.setFont('Arial', 7.5)
        self.setFillColor(colors.HexColor('#64748B'))
        self.drawString(14*mm, 10*mm, "TRUSTIA AI  •  Otonom Mobilite Teknolojileri  •  İTO BTM Fulya Kampüsü  •  Kod: TRUSTIA-IONIQ5-L4-2026")
        
        page_str = f"Sayfa {self._pageNumber} / {page_count}"
        self.drawRightString(196*mm, 10*mm, page_str)
        self.restoreState()

def create_master_pdf_with_photos(output_paths):
    # Image Paths
    img_base = r"c:\Users\Murat\Desktop\Trustia\06_Medya_Gorsel_ve_Tanitim_Videolari\Hyundai_Ioniq_5_Test_Araci"
    img1 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_1.png") # Front 3/4
    img2 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_2.png") # Front Left
    img3 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_3.png") # Side Profile
    img4 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_4.png") # Rear 3/4
    img5 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_5.png") # Rear Straight
    img6 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_6.png") # Front Cockpit
    img7 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_7.png") # Rear Passenger

    doc = SimpleDocTemplate(
        output_paths[0],
        pagesize=A4,
        leftMargin=14*mm,
        rightMargin=14*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )

    styles = getSampleStyleSheet()
    
    c_primary = colors.HexColor('#0A192F')   # Deep Navy
    c_accent = colors.HexColor('#0284C7')    # Electric Blue
    c_dark = colors.HexColor('#0F172A')      # Slate 900
    c_gray = colors.HexColor('#475569')      # Slate 600
    c_light_bg = colors.HexColor('#F8FAFC')  # Slate 50
    c_border = colors.HexColor('#CBD5E1')    # Slate 300
    c_success = colors.HexColor('#059669')   # Emerald 600

    title_style = ParagraphStyle('DocTitle', fontName='Arial-Bold', fontSize=15, leading=19, textColor=c_primary)
    subtitle_style = ParagraphStyle('DocSubTitle', fontName='Arial', fontSize=8.5, leading=11.5, textColor=c_accent)
    h1_style = ParagraphStyle('H1', fontName='Arial-Bold', fontSize=10.5, leading=13, textColor=c_primary, spaceBefore=5, spaceAfter=3)
    h2_style = ParagraphStyle('H2', fontName='Arial-Bold', fontSize=9, leading=11, textColor=c_accent, spaceBefore=4, spaceAfter=2)
    body_style = ParagraphStyle('Body', fontName='Arial', fontSize=7.6, leading=10.5, textColor=c_dark)
    img_caption = ParagraphStyle('ImgCaption', fontName='Arial-Bold', fontSize=6.5, leading=8.5, textColor=c_primary, alignment=1)
    
    table_cell = ParagraphStyle('TableCell', fontName='Arial', fontSize=6.5, leading=8.2, textColor=c_dark)
    table_cell_bold = ParagraphStyle('TableCellBold', fontName='Arial-Bold', fontSize=6.5, leading=8.2, textColor=c_dark)
    table_cell_right = ParagraphStyle('TableCellRight', fontName='Arial', fontSize=6.5, leading=8.2, textColor=c_dark, alignment=2)
    table_cell_right_bold = ParagraphStyle('TableCellRightBold', fontName='Arial-Bold', fontSize=6.5, leading=8.2, textColor=c_primary, alignment=2)
    table_cell_success = ParagraphStyle('TableCellSuccess', fontName='Arial-Bold', fontSize=6.5, leading=8.2, textColor=c_success, alignment=2)

    story = []

    # ================= PAGE 1: COVER, EXECUTIVE SUMMARY & VEHICLE HERO =================
    header_data = [
        [
            Paragraph("<b>TRUSTIA AI</b><br/><font size=6.5 color='#0284C7'>OTONOM SİSTEMLER & DERİN TEKNOLOJİ</font>", body_style),
            Paragraph("<b>DOKÜMAN NO:</b> TRUSTIA-ENG-IONIQ5-L4-V1<br/><b>TARİH:</b> 5 Eylül 2026<br/><b>GİZLİLİK:</b> YATIRIMCI & AR-GE ÖZEL", ParagraphStyle('MetaH', fontName='Arial', fontSize=6.5, leading=9, alignment=2, textColor=c_gray))
        ]
    ]
    t_head = Table(header_data, colWidths=[100*mm, 82*mm])
    t_head.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_head)
    story.append(Spacer(1, 1.5*mm))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_accent, spaceBefore=0, spaceAfter=3*mm))

    story.append(Paragraph("HYUNDAI IONIQ 5 SEVİYE-4 ROBOTAKSİ MASTER PLANI", title_style))
    story.append(Spacer(1, 0.5*mm))
    story.append(Paragraph("E-GMP Şasi Entegrasyonu, 27 Parçalık Doğrulanmış Donanım Kiti, CAN-FD Drive-by-Wire ve Saha Operasyon Rehberi", subtitle_style))
    story.append(Spacer(1, 2.5*mm))

    # Executive Highlights (4 Cards)
    kpi_data = [
        [
            Paragraph("<font size=5.5 color='#64748B'>OTONOMİ ÇEKİRDEĞİ</font><br/><b>16.000 Satır</b><br/><font size=5.5 color='#059669'>%100 Özgün C++/Python</font>", body_style),
            Paragraph("<font size=5.5 color='#64748B'>BİRİM & SİSTEM TESTİ</font><br/><b>1.301 / 1.301</b><br/><font size=5.5 color='#059669'>%100 Sıfır Hata Başarı</font>", body_style),
            Paragraph("<font size=5.5 color='#64748B'>DONANIM KİTİ (27 PARÇA)</font><br/><b>₺ 1.148.829,43</b><br/><font size=5.5 color='#0284C7'>Canlı Sepet Doğrulamalı</font>", body_style),
            Paragraph("<font size=5.5 color='#64748B'>ANAHTAR TESLİM ROBOTAKSİ</font><br/><b>₺ 3.088.829,43</b><br/><font size=5.5 color='#0A192F'>Araç + Tüm Donanım</font>", body_style)
        ]
    ]
    t_kpi = Table(kpi_data, colWidths=[45.5*mm, 45.5*mm, 45.5*mm, 45.5*mm])
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 0.6, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
    ]))
    story.append(t_kpi)
    story.append(Spacer(1, 2.5*mm))

    # Two column: Left text summary, Right Hero Image of Ioniq 5!
    hero_img = RLImage(img1, width=72*mm, height=53*mm)
    
    summary_text = Paragraph(
        "<b>1. YÖNETİCİ ÖZETİ VE MİSYON</b><br/>"
        "Bu master plan; <b>Trustia AI</b> Seviye-4 deterministik otonomi yazılımının, Türkiye'nin ve dünyanın en elverişli 800V elektrikli araç mimarisi olan <b>Hyundai Ioniq 5 (E-GMP)</b> platformuna fiziksel entegrasyon şartnamesidir.<br/><br/>"
        "<b>Küresel Uyumluluk:</b> Hyundai Ioniq 5, dünyanın en büyük iki otonomi devi olan <b>Motional (Hyundai & Aptiv)</b> ve <b>Google Waymo</b> tarafından birincil ticari robotaksi platformu seçilmiştir. Trustia mimarisi, Motional ve Waymo'nun Las Vegas'ta kullandığı algılama ve CAN-FD aktüatör standartlarıyla birebir örtüşmektedir.",
        body_style
    )
    
    hero_col_right = [
        hero_img,
        Paragraph("Şekil 1: Hyundai Ioniq 5 2024 Advance Mat Gri Test Aracı", img_caption)
    ]
    
    hero_table = Table([[summary_text, hero_col_right]], colWidths=[106*mm, 76*mm])
    hero_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(hero_table)
    story.append(Spacer(1, 2.5*mm))

    # Core Specs Table
    spec_data = [
        [Paragraph("<b>Mimari Katman</b>", table_cell_bold), Paragraph("<b>Seçilen Donanım & Teknoloji</b>", table_cell_bold), Paragraph("<b>Temel Fonksiyon & Standart</b>", table_cell_bold)],
        [Paragraph("Merkezi AI İşlemci", table_cell), Paragraph("NVIDIA Jetson AGX Orin 64GB + Seeed J501", table_cell), Paragraph("275 TOPS INT8, 100 Hz Deterministik Kontrol, PoC GMSL2", table_cell)],
        [Paragraph("Yüksek Hızlı Depolama", table_cell), Paragraph("Samsung 990 PRO 4TB M.2 NVMe SSD", table_cell), Paragraph("7.450 MB/s Okuma, Saniyede 350 MB Rosbag/Kara Kutu Kaydı", table_cell)],
        [Paragraph("Birincil 3D SLAM", table_cell), Paragraph("Ouster OS2-128 Rev 7 3D LiDAR (128 Kanal)", table_cell), Paragraph("240m Menzil, 2.62M Nokta/sn, 3D Pose Graph & NDT SLAM", table_cell)],
        [Paragraph("Kör Nokta & Yaya Algılama", table_cell), Paragraph("2x Livox Mid-360 3D LiDAR (Ön Tampon)", table_cell), Paragraph("360°x59° Ultra Geniş Açı, Sıfır Kör Nokta, Kaldırım/Çukur", table_cell)],
        [Paragraph("360° Görsel Algılama", table_cell), Paragraph("4x Leopard Sony IMX390 GMSL2 HDR Kamera", table_cell), Paragraph("120dB Dinamik Aralık, LED Flicker Önleme, IP67 Su Geçirmez", table_cell)],
        [Paragraph("Kötü Hava Koşulu", table_cell), Paragraph("2x Continental ARS 408-21 77GHz FMCW Radar", table_cell), Paragraph("250m Menzil, Yoğun Sis/Yağmur/Kar Altında Kesintisiz Takip", table_cell)],
        [Paragraph("Santimetre Konumlandırma", table_cell), Paragraph("Septentrio mosaic-go Heading + 2x TOP500", table_cell), Paragraph("Santimetre RTK + Durağan Halde Pusula Açısı (Heading)", table_cell)],
        [Paragraph("Araç CAN-FD Köprüsü", table_cell), Paragraph("Kvaser U100 CAN-FD + 120Ω Sonlandırıcı", table_cell), Paragraph("100 Hz LKAS_FD Açı & 50 Hz SCC_FD İvme/Fren Enjeksiyonu", table_cell)],
        [Paragraph("Donanımsal E-Stop", table_cell), Paragraph("Schneider Buton + ELO 80A Güç Rölesi", table_cell), Paragraph("10ms İçinde Mekanik Güç Kesme, ASIL-D Emniyet Kalkanı", table_cell)],
    ]
    t_spec = Table(spec_data, colWidths=[38*mm, 72*mm, 72*mm])
    t_spec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.4, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 1.2*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2*mm),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_spec)

    story.append(PageBreak())

    # ================= PAGE 2: 27-ITEM VERIFIED HARDWARE BOM =================
    story.append(Paragraph("2. %100 DOĞRULANMIŞ VE CANLI SEPETLİ DONANIM TEDARİK LİSTESİ (BOM)", h1_style))
    story.append(Paragraph(
        "Aşağıdaki liste; Trustia AI Hyundai Ioniq 5 test aracının fiziksel entegrasyonu için doğrudan Türkiye distribütörleri ve yetkili global kanallardan sepet teyidi alınmış <b>27 parçalık anahtar teslim donanım listesidir.</b> Fiyatlar canlı döviz kurları ($1 = 48,26 TL, €1 = 56,04 - 56,09 TL) ve KDV/Gümrük dahil net tutarlardır.",
        body_style
    ))
    story.append(Spacer(1, 1.5*mm))

    bom_table_data = [
        [Paragraph("<b>#</b>", table_cell_bold), Paragraph("<b>Sistem & Parça Tanımı</b>", table_cell_bold), Paragraph("<b>Üretici Kodu / Model</b>", table_cell_bold), Paragraph("<b>Tedarikçi & Satıcı</b>", table_cell_bold), Paragraph("<b>Ad.</b>", table_cell_bold), Paragraph("<b>Tutar (TL)</b>", table_cell_right_bold)],
        
        [Paragraph("1", table_cell), Paragraph("Ouster OS2-128 Rev 7 3D LiDAR (Tavan)", table_cell_bold), Paragraph("OS2-128 (240m, 128ch)", table_cell), Paragraph("Leo Drive (İstanbul)", table_cell), Paragraph("1", table_cell), Paragraph("351.258,60 TL", table_cell_right)],
        [Paragraph("2", table_cell), Paragraph("Livox Mid-360 3D LiDAR (Ön Tampon)", table_cell_bold), Paragraph("Mid-360 (360°x59°)", table_cell), Paragraph("Orbi Elektronik (TR)", table_cell), Paragraph("2", table_cell), Paragraph("232.730,40 TL", table_cell_right)],
        [Paragraph("3", table_cell), Paragraph("Seeed reServer J501 + Jetson Orin 64GB", table_cell_bold), Paragraph("E2025112603 (275 TOPS)", table_cell), Paragraph("Seeed Studio ($3.760,26)", table_cell), Paragraph("1", table_cell), Paragraph("181.470,15 TL", table_cell_right)],
        [Paragraph("4", table_cell), Paragraph("Samsung 990 PRO 4TB M.2 NVMe SSD", table_cell_bold), Paragraph("MZ-V9P4T0BW (7.450 MB/s)", table_cell), Paragraph("PTTAVM (tulparlife)", table_cell), Paragraph("1", table_cell), Paragraph("50.220,00 TL", table_cell_right)],
        [Paragraph("5", table_cell), Paragraph("Leopard Sony IMX390 120H GMSL2 Kamera", table_cell_bold), Paragraph("LI-IMX390-GMSL2-120H", table_cell), Paragraph("Mouser TR (1.755,48 €)", table_cell), Paragraph("4", table_cell), Paragraph("98.351,32 TL", table_cell_right)],
        [Paragraph("6", table_cell), Paragraph("Basler GMSL2 FAKRA-Z 3m Kamera Kablosu", table_cell), Paragraph("FAKRA-Z F/F (50Ω Coax)", table_cell), Paragraph("Basler AG (138,04 €)", table_cell), Paragraph("4", table_cell), Paragraph("7.740,18 TL", table_cell_right)],
        [Paragraph("7", table_cell), Paragraph("Continental ARS 408-21 77GHz Radar", table_cell_bold), Paragraph("ARS408-21 (250m FMCW)", table_cell), Paragraph("Alibaba ($1.180,27)", table_cell), Paragraph("2", table_cell), Paragraph("59.345,46 TL", table_cell_right)],
        [Paragraph("8", table_cell), Paragraph("Septentrio mosaic-go Heading RTK Modülü", table_cell_bold), Paragraph("410397 (Dual Antenna)", table_cell), Paragraph("e-komponent (Digi-Key)", table_cell), Paragraph("1", table_cell), Paragraph("52.084,82 TL", table_cell_right)],
        [Paragraph("9", table_cell), Paragraph("TOPGNSS TOP500 Tam Bant RTK Mantar Anten", table_cell), Paragraph("TOP500 (L1/L2/L5 IP67)", table_cell), Paragraph("Alibaba ($211,14)", table_cell), Paragraph("2", table_cell), Paragraph("10.616,38 TL", table_cell_right)],
        [Paragraph("10", table_cell), Paragraph("Elecbee LMR195 Düşük Kayıplı SMA Anten Kablosu", table_cell), Paragraph("EB-101-0112 (1m LMR195)", table_cell), Paragraph("Elecbee.com TR", table_cell), Paragraph("2", table_cell), Paragraph("531,38 TL", table_cell_right)],
        [Paragraph("11", table_cell), Paragraph("Teltonika RUTX50 Endüstriyel 5G Router", table_cell_bold), Paragraph("HBC0000B0MZK3 (Dual SIM)", table_cell), Paragraph("Hepsiburada (ESET TR)", table_cell), Paragraph("1", table_cell), Paragraph("35.349,00 TL", table_cell_right)],
        [Paragraph("12", table_cell), Paragraph("WaveShare 5-Port Gigabit DIN Ray Switch", table_cell), Paragraph("WS-10/100/1000M DIN", table_cell), Paragraph("Robotistan TR", table_cell), Paragraph("1", table_cell), Paragraph("1.583,59 TL", table_cell_right)],
        [Paragraph("13", table_cell), Paragraph("Digitus CAT 6A S-FTP Çift Zırhlı Kablo (10m)", table_cell), Paragraph("DK-1644-A-100 (LSZH)", table_cell), Paragraph("Trendyol (NetworkTek.)", table_cell), Paragraph("2", table_cell), Paragraph("1.378,00 TL", table_cell_right)],
        [Paragraph("14", table_cell), Paragraph("Interkom 12'li Kapaklı & Baralı Sigorta Bloğu", table_cell_bold), Paragraph("IC-276C-12 (Marin/Oto)", table_cell), Paragraph("Interkom Elektronik", table_cell), Paragraph("1", table_cell), Paragraph("1.708,45 TL", table_cell_right)],
        [Paragraph("15", table_cell), Paragraph("Mean Well DCW08A-12 İzoleli DC-DC Konverter", table_cell), Paragraph("DCW08A-12 (9..18V -> 12V)", table_cell), Paragraph("Hepsiburada (Endelkon)", table_cell), Paragraph("1", table_cell), Paragraph("1.403,86 TL", table_cell_right)],
        [Paragraph("16", table_cell), Paragraph("SIEGEN 300A Metal Akü Kesici Şalter (Kill Switch)", table_cell), Paragraph("12V/24V 300A Master", table_cell), Paragraph("Trendyol (incirOto)", table_cell), Paragraph("1", table_cell), Paragraph("519,00 TL", table_cell_right)],
        [Paragraph("17", table_cell), Paragraph("ELO Büyük Kasa 80A DC Ağır Hizmet Güç Rölesi", table_cell), Paragraph("201.005.001 (Toz Korumalı)", table_cell), Paragraph("ELO Ticaret (Resmi)", table_cell), Paragraph("1", table_cell), Paragraph("1.252,80 TL", table_cell_right)],
        [Paragraph("18", table_cell), Paragraph("Schneider Electric Mantar E-Stop Acil Buton", table_cell), Paragraph("XA2EA4342 (22.5mm NC)", table_cell), Paragraph("Activ Elektrik TR", table_cell), Paragraph("1", table_cell), Paragraph("128,72 TL", table_cell_right)],
        [Paragraph("19", table_cell), Paragraph("Kvaser U100 CAN / CAN-FD to USB Dönüştürücü", table_cell_bold), Paragraph("01284-4 (5000V Galvanik)", table_cell), Paragraph("Elektronomi.com TR", table_cell), Paragraph("1", table_cell), Paragraph("24.213,51 TL", table_cell_right)],
        [Paragraph("20", table_cell), Paragraph("Kvaser 00801-4 120Ω CAN Sonlandırma Adaptörü", table_cell), Paragraph("00801-4 (DSUB-9 120 Ohm)", table_cell), Paragraph("Farnell TR (25,42 €)", table_cell), Paragraph("1", table_cell), Paragraph("1.710,96 TL", table_cell_right)],
        [Paragraph("21", table_cell), Paragraph("Drs Tuning Hyundai Ioniq 5 Siyah Tavan Barı", table_cell_bold), Paragraph("Ace-4 Kilitli Ara Atkı Seti", table_cell), Paragraph("Hepsiburada (DrsTuning)", table_cell), Paragraph("1", table_cell), Paragraph("7.086,63 TL", table_cell_right)],
        [Paragraph("22", table_cell), Paragraph("M6 Kauçuk Titreşim Sönümleyici Takoz (4'lü Set)", table_cell), Paragraph("25x20mm M6 Tip-B", table_cell), Paragraph("Trendyol (Tedarik Odası)", table_cell), Paragraph("1", table_cell), Paragraph("709,00 TL", table_cell_right)],
        [Paragraph("23", table_cell), Paragraph("IP68 Su Geçirmez Tavan Buat Jel Kutusu", table_cell), Paragraph("CNP-3103 (52x38x26mm)", table_cell), Paragraph("Trendyol (ERANOVA)", table_cell), Paragraph("1", table_cell), Paragraph("499,00 TL", table_cell_right)],
        [Paragraph("24", table_cell), Paragraph("Coroplast 8551 Siyah Otomotiv Tüylü Bez Bant", table_cell), Paragraph("8551 (19mm x 15m)", table_cell), Paragraph("Trendyol (PATEX)", table_cell), Paragraph("1", table_cell), Paragraph("113,85 TL", table_cell_right)],
        [Paragraph("25", table_cell), Paragraph("WaveShare 10.1\" Dokunmatik HDMI IPS Ekran", table_cell_bold), Paragraph("1024x600 IPS Panel (E)", table_cell), Paragraph("Trendyol (ERNPAZAR)", table_cell), Paragraph("1", table_cell), Paragraph("21.118,35 TL", table_cell_right)],
        [Paragraph("26", table_cell), Paragraph("Deyatech 2.8m Ağır Hizmet Kalibrasyon Ayağı", table_cell), Paragraph("HB00000GKU69 (2.8m Stand)", table_cell), Paragraph("Hepsiburada (Deyatech)", table_cell), Paragraph("1", table_cell), Paragraph("1.299,00 TL", table_cell_right)],
        [Paragraph("27", table_cell), Paragraph("100x80cm Mat CharuCo Kalibrasyon Levhası", table_cell), Paragraph("3mm Dibond + Mat UV Baskı", table_cell), Paragraph("Yerel UV Dijital İmalat", table_cell), Paragraph("1", table_cell), Paragraph("2.400,00 TL", table_cell_right)],
        
        [Paragraph("<b>A</b>", table_cell_bold), Paragraph("<b>TÜM AR-GE DONANIM VE SENSÖR KİTİ TOPLAMI (27 KALEM)</b>", table_cell_bold), Paragraph("<b>Eksiksiz Full Kit</b>", table_cell_bold), Paragraph("<b>27 Parça Doğrulandı</b>", table_cell_bold), Paragraph("<b>27</b>", table_cell_bold), Paragraph("<b>₺ 1.148.829,43</b>", table_cell_success)],
        [Paragraph("<b>B</b>", table_cell_bold), Paragraph("<b>HYUNDAI IONIQ 5 TEST ARACI (2024 ADVANCE MAT GRİ)</b>", table_cell_bold), Paragraph("<b>E-GMP 800V EV</b>", table_cell_bold), Paragraph("<b>Sahibinden (Doğrulandı)</b>", table_cell_bold), Paragraph("<b>1</b>", table_cell_bold), Paragraph("<b>₺ 1.940.000,00</b>", table_cell_right_bold)],
        [Paragraph("<b>C</b>", table_cell_bold), Paragraph("<b>ANAHTAR TESLİM SEVİYE-4 ÇALIŞIR ROBOTAKSİ GENEL TOPLAM</b>", table_cell_bold), Paragraph("<b>Araç + Donanım</b>", table_cell_bold), Paragraph("<b>%100 Turnkey Proje</b>", table_cell_bold), Paragraph("<b>-</b>", table_cell_bold), Paragraph("<b>₺ 3.088.829,43</b>", table_cell_success)],
    ]

    t_bom = Table(bom_table_data, colWidths=[5*mm, 52*mm, 41*mm, 42*mm, 7*mm, 35*mm])
    t_bom.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.4, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-4), [colors.white, c_light_bg]),
        ('BACKGROUND', (0,-3), (-1,-3), colors.HexColor('#F1F5F9')),
        ('BACKGROUND', (0,-2), (-1,-2), colors.HexColor('#F1F5F9')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E0F2FE')),
        ('LINEBELOW', (0,-1), (-1,-1), 1.2, c_accent),
        ('TOPPADDING', (0,0), (-1,-1), 0.85*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.85*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 1.5*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 1.5*mm),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_bom)

    story.append(PageBreak())

    # ================= PAGE 3: PHYSICAL INSTALLATION WITH 2 VEHICLE PHOTOS =================
    story.append(Paragraph("3. HYUNDAI IONIQ 5 FİZİKSEL MEKANİK VE KABLO MONTAJ PLANI", h1_style))
    story.append(Paragraph(
        "Hyundai Ioniq 5, modern monokok gövdesi ve çıtasız tavan raylarıyla delme/kesme işlemi gerektirmeden tam modüler dönüşüme uygundur. Dönüşüm 4 ana fiziksel bölgede 48 saatte tamamlanır:",
        body_style
    ))
    story.append(Spacer(1, 1.5*mm))

    phases_data = [
        [
            Paragraph("<b>BÖLGE 1: TAVAN PLATFORMU (NO-DRILL)</b><br/>"
                      "• <b>Drs Tuning Ace-4 Bar:</b> Kapı üstü fabrikasyon pres fitil yuvalarına 6.5 Nm torkla kilitlenir.<br/>"
                      "• <b>Ouster OS2-128 LiDAR:</b> 4 adet M6 kauçuk titreşim takozuyla ön barın tam merkezine sabitlenir.<br/>"
                      "• <b>2x TOPGNSS Anten:</b> Ön ve arka bar uçlarına monte edilerek aralarında 1.2m True Heading açıklığı sağlanır.<br/>"
                      "• <b>Kablo Geçişi:</b> Tavan sağ oluğundan arka spoyler altındaki fabrikasyon kauçuk körüğe girer. `IP68 CNP-3103 Jel Buat` ile %100 su sızdırmaz şekilde D-sütunundan alt bagaja indirilir.", body_style),
            Paragraph("<b>BÖLGE 2: ÖN TAMPON & IZGARA</b><br/>"
                      "• <b>2x Livox Mid-360 LiDAR:</b> Ön sağ ve sol hava perdesi (air curtain) yuvalarına özel 3D ABS braketlerle yerleştirilir.<br/>"
                      "• <b>Look-down Açılandırma:</b> 45° dışa, 12° aşağıya eğimli açılandırılır; tekerlek dipleri, kaldırımlar ve yayalar 0.1m - 40m arasında kör noktasız taranır.<br/>"
                      "• <b>Continental ARS 408-21:</b> Plakalık altı ızgara arkasındaki darbe demirine M8 paslanmaz çelik braketle sabitlenir (Sis/yağmur filtresi).<br/>"
                      "• <b>Kablo Yolu:</b> Ön çamurluk içinden motor bölmesi ana kauçuk körüğünden kabine alınır.", body_style)
        ],
        [
            Paragraph("<b>BÖLGE 3: 4x GMSL2 HDR KAMERALAR</b><br/>"
                      "• <b>Ön Kamera (CAM_FRONT):</b> Dikiz aynası arkasındaki OEM ADAS kamera kutusu içine ön cama sıfır yerleştirilir.<br/>"
                      "• <b>Yan Kameralar (CAM_L/R):</b> Sağ ve sol yan ayna alt gövdelerine gömme 3D polimer yuvalarla takılır (Şerit ve kör nokta takibi).<br/>"
                      "• <b>Arka Kamera (CAM_REAR):</b> Bagaj kapağı spoyleri altındaki geri görüş kamerası yanına monte edilir.<br/>"
                      "• <b>Kablo Tipi:</b> 4 adet Basler 3m FAKRA-Z çift blendajlı zırhlı koaksiyel kablo ile doğrudan Seeed J501 kartına girer.", body_style),
            Paragraph("<b>BÖLGE 4: ALT BAGAJ (SUB-TRUNK) MERKEZİ</b><br/>"
                      "• <b>57 Litrelik Gizli Hazne:</b> Bagaj taban kapağının altındaki derin havuz içine 4mm CNC alüminyum montaj şasisi yerleştirilir.<br/>"
                      "• <b>İçerik:</b> Seeed J501 (Jetson Orin), Samsung 4TB SSD, Interkom Sigorta Panosu, Teltonika 5G Router, WaveShare Gigabit Switch, Mean Well Regülatör, ELO Röle ve Kvaser CAN-FD.<br/>"
                      "• <b>Termal Yönetim:</b> 2 adet 12V sessiz PWM fan ile sıcaklık sürekli <35°C tutulur. Dışarıdan araç %100 fabrikasyon görünür.", body_style)
        ]
    ]
    t_phase = Table(phases_data, colWidths=[91*mm, 91*mm])
    t_phase.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 0.6, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
    ]))
    story.append(t_phase)
    story.append(Spacer(1, 2*mm))

    # Two Vehicle Photos embedded on Page 3: Side Profile & Rear View
    img_p3_1 = RLImage(img3, width=88*mm, height=52*mm)
    img_p3_2 = RLImage(img4, width=88*mm, height=52*mm)
    
    photo_table_p3 = Table([
        [img_p3_1, img_p3_2],
        [Paragraph("Şekil 2: Yan Profil Sensör Eksenleri & Tavan Barı Hizalaması", img_caption),
         Paragraph("Şekil 3: Arka Gövde & Spoyler Altı Kablo Giriş Körüğü", img_caption)]
    ], colWidths=[91*mm, 91*mm])
    photo_table_p3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1*mm),
    ]))
    story.append(photo_table_p3)
    story.append(Spacer(1, 2*mm))

    story.append(Paragraph("4. ELEKTRİK, GÜÇ DAĞITIMI VE E-STOP EMNİYET ZİNCİRİ", h1_style))
    elec_data = [
        [Paragraph("<b>Kademe</b>", table_cell_bold), Paragraph("<b>Bileşen & İşlev</b>", table_cell_bold), Paragraph("<b>Emniyet Parametresi</b>", table_cell_bold)],
        [Paragraph("1. Ana Hat", table_cell), Paragraph("Ioniq 5 12V Akü -> 4 AWG Marin Bakır Kablo -> 100A ANL Bıçak Sigorta", table_cell), Paragraph("Aşırı akım ve kısa devreye karşı 100A ana hat koruması", table_cell)],
        [Paragraph("2. Kill Switch", table_cell), Paragraph("SIEGEN 300A Metal Akü Şalteri (Kırmızı Çıkarılabilir Anahtar)", table_cell), Paragraph("Park ve bakım halinde tüm elektroniği tek hamlede aküden izole eder", table_cell)],
        [Paragraph("3. E-Stop Röle", table_cell), Paragraph("ELO 80A Ağır Hizmet Güç Rölesi + Schneider Mantar E-Stop Butonu", table_cell), Paragraph("Butona basıldığı an 10 milisaniyede tüm sensör elektriği mekanik kesilir", table_cell)],
        [Paragraph("4. Voltaj Filtresi", table_cell), Paragraph("Mean Well DCW08A-12 İzoleli DC-DC Güç Regülatörü", table_cell), Paragraph("Araç alternatör dalgalanmalarını süzer, sensörlere saf 12.0V DC sağlar", table_cell)],
        [Paragraph("5. Dağıtım Panosu", table_cell), Paragraph("Interkom IC-276C-12 12'li Bıçak Sigortalı Güç Dağıtım Bloğu", table_cell), Paragraph("Jetson (15A), LiDAR (5A), Radar (3A), Router (3A), Switch (2A), Ekran (3A)", table_cell)],
    ]
    t_elec = Table(elec_data, colWidths=[28*mm, 90*mm, 64*mm])
    t_elec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.4, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 1.1*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.1*mm),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_elec)

    story.append(PageBreak())

    # ================= PAGE 4: CAN-FD, SOFTWARE & COCKPIT PHOTOS =================
    story.append(Paragraph("5. CAN-FD DRIVE-BY-WIRE VE YAZILIM ENTEGRASYONU", h1_style))
    story.append(Paragraph(
        "Hyundai Ioniq 5, aktüatör seviyesinde yüksek hızlı <b>CAN-FD (500 kbps Nominal / 2 Mbps Veri Fazı)</b> protokolü kullanır. Trustia AI kontrol motoru, araca fabrikasyon dikiz aynası arkasındaki ADAS kamera soketinden Y-Harness ile bağlanır:",
        body_style
    ))
    story.append(Spacer(1, 1.5*mm))

    can_data = [
        [Paragraph("<b>Kontrol Ekseni</b>", table_cell_bold), Paragraph("<b>CAN-FD Mesajı & ID</b>", table_cell_bold), Paragraph("<b>Frekans</b>", table_cell_bold), Paragraph("<b>Enjekte Edilen Sinyaller & Algoritma</b>", table_cell_bold)],
        [
            Paragraph("<b>Yanal Kontrol (Direksiyon)</b>", table_cell),
            Paragraph("<code>LKAS_FD / LFA_FD</code><br/>ID: <code>0x12A</code>", table_cell),
            Paragraph("100 Hz<br/>(10 ms)", table_cell),
            Paragraph("• Hedef Direksiyon Açısı (0.1° Çözünürlük)<br/>• 100 Hz Pure Pursuit & Stanley Kontrolcü<br/>• 4-bit Periyodik Watchdog Sayıcı + AUTOSAR CRC-8", table_cell)
        ],
        [
            Paragraph("<b>Boylamsal Kontrol (Gaz/Fren)</b>", table_cell),
            Paragraph("<code>SCC_FD / ACC_Control</code><br/>ID: <code>0x1A0</code>", table_cell),
            Paragraph("50 Hz<br/>(20 ms)", table_cell),
            Paragraph("• Hedef İvmelenme / Yavaşlama (+2.0m/s² ... -6.0m/s²)<br/>• iEB 2.0 Elektronik Fren Ön Basınçlandırma<br/>• Tam Durma & Auto-Hold Serbest Bırakma", table_cell)
        ],
        [
            Paragraph("<b>Telemetri & Geri Bildirim</b>", table_cell),
            Paragraph("<code>WHL_SPD11 (0x386)</code><br/><code>SAS11 (0x2B0)</code>", table_cell),
            Paragraph("100 Hz", table_cell),
            Paragraph("• 4 Tekerlek Bağımsız Hız Sensörü (0.03 km/h Hassasiyet)<br/>• Direksiyon Gerçek Açı & Tork Geri Bildirimi<br/>• ESKF Odometri & SLAM Füzyon Beslemesi", table_cell)
        ]
    ]
    t_can = Table(can_data, colWidths=[38*mm, 38*mm, 20*mm, 86*mm])
    t_can.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.4, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 1.4*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.4*mm),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_can)
    story.append(Spacer(1, 2*mm))

    # Two Cockpit/Interior Photos embedded on Page 4: Cockpit & Rear Seating
    img_p4_1 = RLImage(img6, width=88*mm, height=52*mm)
    img_p4_2 = RLImage(img7, width=88*mm, height=52*mm)
    
    photo_table_p4 = Table([
        [img_p4_1, img_p4_2],
        [Paragraph("Şekil 4: Ön Kokpit, 10.1\" Dokunmatik C2 Ekranı & E-Stop Yerleşimi", img_caption),
         Paragraph("Şekil 5: Arka Yolcu Bölümü & E-GMP Geniş Yaşam Alanı", img_caption)]
    ], colWidths=[91*mm, 91*mm])
    photo_table_p4.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1*mm),
    ]))
    story.append(photo_table_p4)
    story.append(Spacer(1, 2*mm))

    story.append(Paragraph("6. SÜRÜCÜ MÜDAHALESİ (OVERRIDE) VE GÜVENLİK PROTOKOLLERİ", h1_style))
    safety_points = [
        [
            Paragraph("<b>İNSAN MÜDAHALESİ (OVERRIDE)</b><br/>"
                      "• <b>Direksiyona Dokunulduğunda:</b> Şoför direksiyonu hafifçe tutup çevirdiği an (>2.0 Nm tork), sistem <b>5 milisaniye içinde</b> kontrolü insana bırakır.<br/>"
                      "• <b>Frene Basıldığında:</b> Fren pedalına 1mm dahi basıldığında CAN-FD otonom freni anında devreden çıkar, hidrolik fren sürücüye geçer.<br/>"
                      "• <b>ISO 26262 ASIL-D Kuralı:</b> İnsan müdahalesi daima otonominin üzerindedir.", body_style),
            Paragraph("<b>ARIZA & ACİL DURUM (FAIL-SAFE)</b><br/>"
                      "• <b>200ms Emniyet Bekçisi:</b> Sensör veya bilgisayar takılırsa 0.2 saniyede arıza algılanır.<br/>"
                      "• <b>Minimum Risk Manevrası (MRM):</b> 4'lü flaşörler yanar, korna çalar, araç şeridinde yumuşakça yavaşlayıp durur ve el frenini (EPB) çeker.<br/>"
                      "• <b>Kara Kutu (Black Box):</b> Samsung 4TB SSD saniyede 350 MB hızla adli kaza telemetrisini kaydeder.", body_style)
        ],
        [
            Paragraph("<b>HIRSIZLIK & KAÇIRILMA KORUMASI</b><br/>"
                      "• <b>5G GPS Sanal Çit (Geofencing):</b> Araç izinli test sahasının (BTM veya Bilişim Vadisi) 5 metre dışına çıkarsa <b>uzaktan motor ve tekerlekler kilitlenir (Remote Immobilizer).</b><br/>"
                      "• <b>Uzaktan Teleoperasyon:</b> Masaüstü C2 konsolundan tek tuşla araç acil durdurulabilir.<br/>"
                      "• <b>7/24 Kabin & Çevre Kaydı:</b> 4 dış + 1 iç kamera 5G ile buluta aktarılır.", body_style),
            Paragraph("<b>GARAJ & PARK ÜSLERİ</b><br/>"
                      "• <b>Ana Merkez: İTO BTM Fulya Kampüsü, Şişli / İstanbul:</b> 7/24 Güvenlikli kapalı otopark, AC elektrikli araç şarj istasyonları.<br/>"
                      "• <b>Test Üssü: Bilişim Vadisi Otonom Test Merkezi (Gebze):</b> Sanayi Bakanlığı resmi kapalı otonomi garajı ve test hangarları.<br/>"
                      "• <b>Özel Kasko:</b> Sensörler aksiyoner bedelleriyle kaskoya işlenir.", body_style)
        ]
    ]
    t_safe = Table(safety_points, colWidths=[91*mm, 91*mm])
    t_safe.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 0.6, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
    ]))
    story.append(t_safe)

    story.append(PageBreak())

    # ================= PAGE 5: CALIBRATION, TESTING, 2 EXTERIOR PHOTOS & SIGN-OFF =================
    story.append(Paragraph("7. KALİBRASYON, 4 KADEMELİ TEST PLANI VE DEVLET İZİNLERİ", h1_style))
    story.append(Paragraph(
        "Araç montajı tamamlandıktan sonra uzaysal sensör kalibrasyonu yapılır ve 4 kademeli güvenlik protokolüyle sahaya çıkarılır:",
        body_style
    ))
    story.append(Spacer(1, 1.5*mm))

    calib_data = [
        [
            Paragraph("<b>SPATIAL EXTRINSIC KALİBRASYON</b><br/>"
                      "• <b>Ekipman:</b> `Deyatech 2.8m Tripod` üzerine `100x80cm Mat CharuCo Levhası` takılır.<br/>"
                      "• <b>İstasyonlar:</b> Aracın önünde 5 farklı uzaysal noktaya (3m, 5m, Sol 45°, Sağ 45°, Arka 4m) yerleştirilir.<br/>"
                      "• <b>Matematiksel Eşleme:</b> Kamera pikselleri ($u,v$) ile LiDAR 3D noktaları ($X,Y,Z$) Levenberg-Marquardt optimizasyonu ile eşleştirilir:<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;<b>P_kamera = R • P_lidar + t</b><br/>"
                      "• Çıkan dönme ve öteleme matrisleri `calibration.py` çekirdeğine işlenir.", body_style),
            Paragraph("<b>MONTAJ VE İCRA EKİBİ</b><br/>"
                      "• <b>👑 Murat Furkan Bayram (Sistem Mimarı & CEO):</b> Yazılım mimarisi, SLAM/Rota motoru, C2 konsolu, test koordinasyonu.<br/>"
                      "• <b>⚡ Denizcan Özcan (Donanım & Test Lideri):</b> ASELSAN & TEKNOFEST Robotaksi tecrübesiyle CAN-Bus, elektrik panosu, kablolama ve kalibrasyon ölçümü.<br/>"
                      "• <b>🛠️ BTM / Bilişim Vadisi Teknisyeni:</b> Mekanik montaj, 3D ABS braket baskıları, el aletleri ve tavan montajı.", body_style)
        ]
    ]
    t_cal = Table(calib_data, colWidths=[91*mm, 91*mm])
    t_cal.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 0.6, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
    ]))
    story.append(t_cal)
    story.append(Spacer(1, 1.5*mm))

    # Two Exterior Photos embedded on Page 5: Front-Left & Rear-Center
    img_p5_1 = RLImage(img2, width=88*mm, height=48*mm)
    img_p5_2 = RLImage(img5, width=88*mm, height=48*mm)
    
    photo_table_p5 = Table([
        [img_p5_1, img_p5_2],
        [Paragraph("Şekil 6: Ön Sol Tampon Livox LiDAR & Radar Tarama Alanı", img_caption),
         Paragraph("Şekil 7: Arka Düz Görünüm & Geri Görüş Otonomi Kamerası", img_caption)]
    ], colWidths=[91*mm, 91*mm])
    photo_table_p5.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0.8*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8*mm),
    ]))
    story.append(photo_table_p5)
    story.append(Spacer(1, 1.5*mm))

    story.append(Paragraph("4 KADEMELİ SAHA TEST YOL HARİTASI VE DEVLET İZİNLERİ", h2_style))
    test_roadmap_data = [
        [Paragraph("<b>Aşama</b>", table_cell_bold), Paragraph("<b>Test Sahası & Lokasyon</b>", table_cell_bold), Paragraph("<b>Test Edilen Senaryolar & Emniyet</b>", table_cell_bold), Paragraph("<b>Yasal İzin & Durum</b>", table_cell_bold)],
        [
            Paragraph("<b>Aşama 1</b> (Simülasyon)", table_cell),
            Paragraph("Webots 3D & CARLA Dijital İkiz", table_cell),
            Paragraph("1.301 Birim/Entegrasyon Testi, SLAM haritalama, Pure Pursuit rota takibi, acil kaçınma", table_cell),
            Paragraph("<font color='#059669'><b>%100 TAMAMLANDI ✅</b></font>", table_cell)
        ],
        [
            Paragraph("<b>Aşama 2</b> (Kapalı Pist)", table_cell),
            Paragraph("Bilişim Vadisi Otonom Pisti (Gebze)", table_cell),
            Paragraph("Trafiğe kapalı 1.5 km asfalt parkur, cansız mankenler, yapay kavşaklar, dur-kalk akışı", table_cell),
            Paragraph("Bilişim Vadisi Protokolü", table_cell)
        ],
        [
            Paragraph("<b>Aşama 3</b> (Kampüs İçi)", table_cell),
            Paragraph("İTO BTM Fulya & Teknopark İst.", table_cell),
            Paragraph("Kapalı kampüs yollarında 20-30 km/s hızla yolcu alma/bırakma, park etme manevraları", table_cell),
            Paragraph("BTM Özel Alan İzni", table_cell)
        ],
        [
            Paragraph("<b>Aşama 4</b> (Açık Yol)", table_cell),
            Paragraph("Şişli / Fulya / Gebze Pilot Hattı", table_cell),
            Paragraph("Koltukta emniyet sürücüsü hazır beklerken şehir içi karma trafikte Seviye 4 sürüş", table_cell),
            Paragraph("Sanayi Bak. + T Plaka", table_cell)
        ]
    ]
    test_table = Table(test_roadmap_data, colWidths=[28*mm, 44*mm, 76*mm, 34*mm])
    test_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.4, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 1.1*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.1*mm),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(test_table)
    story.append(Spacer(1, 2.5*mm))

    # Sign-off Box
    sign_data = [
        [
            Paragraph("<b>HAZIRLAYAN & SİSTEM MİMARI</b><br/>Murat Furkan Bayram<br/><font size=5.5 color='#64748B'>Kurucu & CEO / Sistem Mimarı<br/>Trustia AI</font>", body_style),
            Paragraph("<b>DONANIM & TEST LİDERİ</b><br/>Denizcan Özcan<br/><font size=5.5 color='#64748B'>Donanım & Entegrasyon Mühendisi<br/>ASELSAN & TEKNOFEST Robotaksi Finalisti</font>", body_style),
            Paragraph("<b>KURUMSAL ONAY & AKREDİTASYON</b><br/>İTO BTM & SSB Akredite<br/><font size=5.5 color='#64748B'>SSB 100/100 • KOSGEB İleri Girişimci<br/>TÜBİTAK ARBİS Milli Araştırmacı</font>", body_style)
        ]
    ]
    t_sign = Table(sign_data, colWidths=[60.6*mm, 60.6*mm, 60.6*mm])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_primary),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master PDF with Photos created successfully: {output_paths[0]}")
    
    for extra_path in output_paths[1:]:
        os.makedirs(os.path.dirname(extra_path), exist_ok=True)
        shutil.copy2(output_paths[0], extra_path)
        print(f"Copied to: {extra_path}")

if __name__ == '__main__':
    dest1 = r"C:\Users\Murat\Desktop\Çıktı\Trustia_AI_Hyundai_Ioniq5_Seviye4_Fotografli_Master_Plan.pdf"
    dest2 = r"C:\Users\Murat\Desktop\Çıktı\08_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
    dest3 = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Teknik_ve_Organizasyon\06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
    dest4 = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Pitch_Decks\Trustia_AI_Hyundai_Ioniq5_Fotografli_Master_Plan.pdf"
    
    create_master_pdf_with_photos([dest1, dest2, dest3, dest4])
