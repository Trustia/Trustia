import os
import sys
import shutil
from datetime import datetime
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image as RLImage, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register TrueType Fonts for Turkish Support
font_regular = 'C:/Windows/Fonts/arial.ttf'
font_bold = 'C:/Windows/Fonts/arialbd.ttf'
font_italic = 'C:/Windows/Fonts/ariali.ttf'

pdfmetrics.registerFont(TTFont('Arial', font_regular))
pdfmetrics.registerFont(TTFont('Arial-Bold', font_bold))
pdfmetrics.registerFont(TTFont('Arial-Italic', font_italic))

# Corporate Palette
C_PRIMARY = colors.HexColor('#0F172A')    # Deep Navy Slate
C_SECONDARY = colors.HexColor('#0284C7')  # Tech Cyan Blue
C_ACCENT = colors.HexColor('#0EA5E9')     # Bright Blue
C_DARK = colors.HexColor('#1E293B')       # Text Dark
C_MUTED = colors.HexColor('#64748B')      # Subtitle Muted
C_LIGHT = colors.HexColor('#F8FAFC')      # Background Light
C_CARD = colors.HexColor('#F1F5F9')       # Card Fill
C_BORDER = colors.HexColor('#CBD5E1')     # Border Silver
C_SUCCESS = colors.HexColor('#059669')    # Success Green
C_GOLD = colors.HexColor('#D97706')       # Badge Gold
C_WHITE = colors.white

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
            self.draw_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_decorations(self, page_count):
        self.saveState()
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont('Arial-Bold', 8)
            self.setFillColor(C_PRIMARY)
            self.drawString(14*mm, 285*mm, "TRUSTIA AI")
            self.setFont('Arial', 8)
            self.setFillColor(C_MUTED)
            self.drawString(34*mm, 285*mm, "|  T.C. Tescilli Seviye-4 Otonom Mobilite Girişimi  •  Resmi Kurumsal Dosya")
            self.drawRightString(196*mm, 285*mm, "Eylül 2026")
            
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.6)
            self.line(14*mm, 282*mm, 196*mm, 282*mm)

        # Footer (all pages)
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.6)
        self.line(14*mm, 14*mm, 196*mm, 14*mm)
        
        self.setFont('Arial-Bold', 7.5)
        self.setFillColor(C_PRIMARY)
        self.drawString(14*mm, 10*mm, "TRUSTIA OTONOM MOBİLİTE TEKNOLOJİLERİ A.Ş.")
        self.setFont('Arial', 7.5)
        self.setFillColor(C_MUTED)
        self.drawString(82*mm, 10*mm, "|  İTO BTM Fulya Kampüsü (Polat Tower Rezidans)  •  trustia.com.tr")
        self.drawRightString(196*mm, 10*mm, f"Sayfa {self._pageNumber} / {page_count}")
        self.restoreState()

def get_corporate_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles['Title'] = ParagraphStyle(
        'CorporateTitle',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=20,
        leading=24,
        textColor=C_PRIMARY,
        spaceAfter=5
    )
    styles['Subtitle'] = ParagraphStyle(
        'CorporateSubtitle',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=10,
        leading=14,
        textColor=C_SECONDARY,
        spaceAfter=12
    )
    styles['H1'] = ParagraphStyle(
        'CorporateH1',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=12,
        leading=16,
        textColor=C_PRIMARY,
        spaceBefore=10,
        spaceAfter=5
    )
    styles['H2'] = ParagraphStyle(
        'CorporateH2',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=10,
        leading=13.5,
        textColor=C_SECONDARY,
        spaceBefore=7,
        spaceAfter=3
    )
    styles['Body'] = ParagraphStyle(
        'CorporateBody',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=8.5,
        leading=12.5,
        textColor=C_DARK,
        spaceAfter=5
    )
    styles['BodyBold'] = ParagraphStyle(
        'CorporateBodyBold',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=8.5,
        leading=12.5,
        textColor=C_DARK,
        spaceAfter=5
    )
    styles['Small'] = ParagraphStyle(
        'CorporateSmall',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=7.5,
        leading=10.5,
        textColor=C_MUTED
    )
    styles['Badge'] = ParagraphStyle(
        'CorporateBadge',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=8,
        leading=11,
        textColor=C_SUCCESS
    )
    styles['Callout'] = ParagraphStyle(
        'CorporateCallout',
        parent=base['Normal'],
        fontName='Arial-Italic',
        fontSize=8,
        leading=11.5,
        textColor=C_PRIMARY
    )
    styles['TableCell'] = ParagraphStyle(
        'CorporateTableCell',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=8,
        leading=11,
        textColor=C_DARK
    )
    styles['TableCellBold'] = ParagraphStyle(
        'CorporateTableCellBold',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=8,
        leading=11,
        textColor=C_PRIMARY
    )
    styles['TableHead'] = ParagraphStyle(
        'CorporateTableHead',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=8,
        leading=11,
        textColor=C_WHITE
    )
    return styles

def build_pdf(filename, story):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=14*mm,
        rightMargin=14*mm,
        topMargin=16*mm,
        bottomMargin=16*mm
    )
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Generated: {filename}")

# -------------------------------------------------------------
# 1. EXECUTIVE ONE PAGER (01)
# -------------------------------------------------------------
def generate_one_pager(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("TRUSTIA AI — YÖNETİCİ ÖZETİ & KURUMSAL BİLGİ DÖKÜMÜ", styles['Title']))
    story.append(Paragraph("SAE Seviye-4 Otonom Araç Dönüşüm Kiti ve Deterministik Seyrüsefer Mimarisi  •  Eylül 2026", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    grid_data = [
        [
            Paragraph("<b>Kurucu & Sistem Mimarı:</b><br/>Murat Furkan Bayram (17 Yaşında, %80 Hisse)", styles['TableCell']),
            Paragraph("<b>T.C. Savunma Sanayii Tescili:</b><br/>SSB 100/100 Tam Puan (Belge: L2zPtN4X1ZJ)", styles['TableCell']),
            Paragraph("<b>Yazılım & Test Olgunluğu:</b><br/>16.000 Satır C++/Python, 1.301 Yeşil Test", styles['TableCell'])
        ],
        [
            Paragraph("<b>Kuluçka & Merkez:</b><br/>İTO BTM Fulya Kampüsü (Polat Tower)", styles['TableCell']),
            Paragraph("<b>KOSGEB & TÜBİTAK:</b><br/>KOSGEB İleri Girişimci & ARBİS Milli Araştırmacı", styles['TableCell']),
            Paragraph("<b>Küresel Meydan Okuma:</b><br/>Dubai World Challenge 1.2M$ (Resmen Gönderildi)", styles['TableCell'])
        ]
    ]
    t_grid = Table(grid_data, colWidths=[60*mm, 62*mm, 60*mm])
    t_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_grid)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. ŞİRKET VE VİZYON ÖZETİ", styles['H1']))
    story.append(Paragraph(
        "Trustia AI, seri üretim elektrikli binek araçları (öncelikle Hyundai Ioniq 5 E-GMP platformu) <b>48 saat içinde tak-çalıştır donanım ve yazılım kiti ile SAE Seviye-4 otonom Robotaksi'ye dönüştüren</b> derin teknoloji girişimidir. Sektördeki Waymo ve Cruise gibi oyuncuların araç başına 250.000$+ özel araç üretim maliyetlerine karşılık; Trustia 35.000$'lık modüler dönüşüm kitiyle <b>%70 maliyet avantajı</b> ve <b>14 aylık yatırım geri dönüş süresi (ROI)</b> sunmaktadır.",
        styles['Body']
    ))

    story.append(Paragraph("2. ÖZGÜN DETERMINİSTİK YAZILIM VE MİMARİ ÜSTÜNLÜK", styles['H1']))
    story.append(Paragraph(
        "Otonomi motorumuz, kara kutu yapay zekalar yerine matematiksel ispatlı deterministik algoritmalarla çalışır:<br/>"
        "• <b>Rota & Yörünge Planlama:</b> Hibrit A* (Hybrid A*) kinematik planlayıcı (Araç dönüş yarıçapını ve Ackermann dinamiğini 50ms altında çözer).<br/>"
        "• <b>GNSS-Bağımsız Konumlandırma:</b> 400Hz ESKF + 3D NDT LiDAR SLAM (Tünellerde, gökdelen vadilerinde ve GPS karartmasında 5 cm hassasiyet).<br/>"
        "• <b>Lateral & Boylamsal Kontrol:</b> Pure Pursuit & Adaptive PID kontrolcüleri (CAN-FD üzerinden direksiyon açısı ve SCC hız enjeksiyonu).<br/>"
        "• <b>Güvenlik & Failsafe:</b> ISO 26262 ASIL-D uyumlu Minimal Risk Maneuver (MRM) ve Zero-Trust CAN-FD güvenlik duvarı.<br/>"
        "• <b>Otomatik Test Validasyonu:</b> Yazılım çekirdeğimiz <b>1.301/1.301 otomatik birim ve entegrasyon testinden %100 başarıyla</b> geçmiştir.",
        styles['Body']
    ))

    story.append(Paragraph("3. DONANIM MİMARİSİ (HYUNDAI IONIQ 5 SEVİYE-4 RETROFIT KİTİ)", styles['H1']))
    hw_data = [
        [Paragraph("Bileşen", styles['TableHead']), Paragraph("Marka / Model", styles['TableHead']), Paragraph("Teknik İşlev & Protokol", styles['TableHead'])],
        [Paragraph("Çatı LiDAR", styles['TableCellBold']), Paragraph("Ouster OS2-128 Rev 7", styles['TableCell']), Paragraph("128 Lazer kanalı, 200m menzil, 2.6M nokta/sn, 360° algılama", styles['TableCell'])],
        [Paragraph("Kör Nokta LiDAR (2x)", styles['TableCellBold']), Paragraph("Livox Mid-360", styles['TableCell']), Paragraph("Ön ve arka tampon kör nokta sıfırlama, IP67 koruma", styles['TableCell'])],
        [Paragraph("Radar (2x)", styles['TableCellBold']), Paragraph("Continental ARS 408-21 (77GHz)", styles['TableCell']), Paragraph("250m menzil, yoğun sis/kum fırtınası/çöl sıcağı dayanımı", styles['TableCell'])],
        [Paragraph("Merkezi Beyin", styles['TableCellBold']), Paragraph("NVIDIA Jetson AGX Orin 64GB", styles['TableCell']), Paragraph("275 TOPS AI işlem gücü, Seeed J501 Carrier, 12V regülasyon", styles['TableCell'])],
        [Paragraph("Araç Veri Arayüzü", styles['TableCellBold']), Paragraph("Kvaser U100 CAN-FD", styles['TableCell']), Paragraph("5 Mbps CAN-FD veri yolu, galvanik izolasyon, LKAS/SCC sürüş kontrolü", styles['TableCell'])],
        [Paragraph("Telemetri & C2", styles['TableCellBold']), Paragraph("Teltonika RUTX50 5G & V2X", styles['TableCell']), Paragraph("Çift SIM, sub-20ms C-V2X ve Dubai Pulse / Akıllı Şehir MQTT köprüsü", styles['TableCell'])],
    ]
    t_hw = Table(hw_data, colWidths=[40*mm, 55*mm, 87*mm])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_hw)
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. FİNANSAL MODEL, BİRİM EKONOMİ & YATIRIM TURU", styles['H1']))
    story.append(Paragraph(
        "<b>Gelir Modeli:</b> 35.000$ Kit Satışı (%35 brüt kâr) + Kilometre başı 0.18$ veya araç başı aylık 450$ Autonomy-as-a-Service (AaaS) sürekli yazılım geliri.<br/>"
        "<b>Birim Ekonomi:</b> Dönüştürülen her araç filo sahibine yılda 55.500$ net operasyonel tasarruf ve kâr sağlar.<br/>"
        "<b>Aranan Yatırım:</b> <b>500.000$ USD (Pre-Seed / 5M$ Post-Money Cap ile SAFE)</b>. Fonun %45'i donanım tedariği ve test araçlarına, %35'i mühendislik kadrosuna, %15'i pist testlerine ayrılacaktır.",
        styles['Body']
    ))
    
    story.append(Spacer(1, 5))
    story.append(Paragraph("<b>İletişim & Randevu:</b> Murat Furkan Bayram (Kurucu & CEO) | +90 537 064 0460 | kariyer@trustia.com.tr | Beşiktaş Polat Tower, İstanbul", styles['Callout']))

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 2. IS MODELI KANVASI (02)
# -------------------------------------------------------------
def generate_business_model_canvas(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("TRUSTIA AI — RESMİ İŞ MODELİ KANVASI (BMC 2026)", styles['Title']))
    story.append(Paragraph("Kurumsal Gelir Mimarisi, Maliyet Yapısı ve Değer Önerisi  •  Eylül 2026", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    bmc_data = [
        [
            Paragraph("<b>1. TEMEL ORTAKLIKLAR</b><br/>"
                      "• Hyundai Motor Group & Bayi Ağı<br/>"
                      "• Tier-1 Sensör Üreticileri (Ouster, Livox, Continental)<br/>"
                      "• İTO BTM (Kuluçka & Yatırımcı Ağı)<br/>"
                      "• T.C. Savunma Sanayii Başkanlığı & ASELSAN<br/>"
                      "• Dubai Ulaşım Otoritesi (RTA Dubai)", styles['TableCell']),
            Paragraph("<b>2. TEMEL FAALİYETLER</b><br/>"
                      "• Seviye-4 Otonom Seyrüsefer Yazılımı Ar-Ge'si<br/>"
                      "• Deterministik SLAM ve Yörünge Algoritmaları<br/>"
                      "• CAN-FD Drive-by-Wire Entegrasyonu<br/>"
                      "• HIL ve Proving Ground Pist Testleri<br/>"
                      "• ISO 26262 ASIL-D Emniyet Validasyonu", styles['TableCell']),
            Paragraph("<b>3. DEĞER ÖNERİSİ</b><br/>"
                      "• <b>%70 Maliyet Üstünlüğü:</b> 250k$ pod yerine 35k$ dönüşüm kiti.<br/>"
                      "• <b>48 Saatte Devreye Alma:</b> Şasiyi delmeden tak-çalıştır mimari.<br/>"
                      "• <b>Deterministik Güvenlik:</b> 1.301 yeşil test, ASIL-D MRM emniyeti.<br/>"
                      "• <b>14 Ayda Amortisman:</b> Araç başına yıllık 55.500$ net kâr.", styles['TableCell']),
            Paragraph("<b>4. MÜŞTERİ İLİŞKİLERİ</b><br/>"
                      "• 7/24 Taktik C2 Canlı Tele-operasyon & İzleme<br/>"
                      "• Otomatik OTA Yazılım ve HD Harita Dağıtımı<br/>"
                      "• Özel Saha Mühendisi ve Filo Bakım Desteği<br/>"
                      "• SLA Garantili %99.9 Operasyonel Çalışma", styles['TableCell']),
            Paragraph("<b>5. MÜŞTERİ SEGMENTLERİ</b><br/>"
                      "• Ticari Taksi Filoları (Dubai Taxi Corp, Martı vb.)<br/>"
                      "• Belediye & Şehir İçi Ulaşım İdareleri (İBB, RTA)<br/>"
                      "• Havalimanı & Kampüs Otonom Ring İşletmecileri<br/>"
                      "• Askeri & Savunma Lojistik Konvoyları (TSK, SSB)", styles['TableCell'])
        ],
        [
            Paragraph("<b>6. TEMEL KAYNAKLAR</b><br/>"
                      "• 16.000 Satır Özgün Deterministik Kod Tabanı<br/>"
                      "• SSB 100/100 Tam Puan & KOSGEB İleri Girişimci Tescili<br/>"
                      "• NVIDIA AGX Orin & LiDAR Donanım Test Laboratuvarı<br/>"
                      "• İTO BTM Fulya Kampüsü Ofis & Test Altyapısı", styles['TableCell']),
            Paragraph("<b>7. KANALLAR</b><br/>"
                      "• Doğrudan B2B Kurumsal Filo Satış Ekibi<br/>"
                      "• Otomotiv OEM & Filo Kiralama Ortaklıkları<br/>"
                      "• Dubai World Challenge & Global Mobilite Zirveleri<br/>"
                      "• BTM & VC Melek Yatırım Ağı Kanalları", styles['TableCell']),
            Paragraph("<b>ÖZEL KORUMA (UNFAIR ADVANTAGE)</b><br/>"
                      "• 17 yaşındaki kurucunun derin otonomi dehası.<br/>"
                      "• Devlet tescilli yapay zeka emniyet sertifikası.<br/>"
                      "• Dubai RTA'nın 1.2M$ yarışmasında onaylı resmi Türk yarışmacı statüsü.", styles['TableCell']),
            Paragraph("<b>8. MALİYET YAPISI</b><br/>"
                      "• Donanım & Sensör Tedariği (LiDAR, Orin, Radar): %45<br/>"
                      "• Ar-Ge ve Mühendislik Maaşları: %35<br/>"
                      "• Kapalı Pist Testleri ve Saha Operasyonları: %15<br/>"
                      "• Hukuk, Patent ve ISO 26262 Belgelendirme: %5", styles['TableCell']),
            Paragraph("<b>9. GELİR AKIŞLARI</b><br/>"
                      "• <b>Kit Satışı (CAPEX):</b> Araç başı 35.000$ Dönüşüm Kiti.<br/>"
                      "• <b>AaaS Geliri (ARR):</b> Km başı 0.18$ veya araç başı 450$/ay.<br/>"
                      "• <b>Kurumsal Lisanslama:</b> Savunma İKA otonomi yazılım lisansı.<br/>"
                      "• <b>Harita & Veri:</b> HD Nokta Bulutu telemetri aboneliği.", styles['TableCell'])
        ]
    ]

    t_bmc = Table(bmc_data, colWidths=[36*mm, 36*mm, 38*mm, 36*mm, 36*mm])
    t_bmc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.6, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_bmc)
    story.append(Spacer(1, 10))

    story.append(Paragraph("BİRİM EKONOMİ (ROBOTAKSİ BAŞINA KÂRLILIK MATRİSİ)", styles['H1']))
    ue_data = [
        [Paragraph("Kalem", styles['TableHead']), Paragraph("Geleneksel Sürücülü Araç", styles['TableHead']), Paragraph("Trustia Seviye-4 Robotaksi", styles['TableHead']), Paragraph("Net Filo Avantajı", styles['TableHead'])],
        [Paragraph("Sürücü Maaşı & SGK (Yıllık)", styles['TableCellBold']), Paragraph("36.000$ (3 Vardiya x 12.000$)", styles['TableCell']), Paragraph("0$ (Sürücüsüz Otonom)", styles['TableCell']), Paragraph("+36.000$ Net Tasarruf", styles['TableCellBold'])],
        [Paragraph("Yakıt / Enerji Tüketimi (Yıllık)", styles['TableCellBold']), Paragraph("18.000$ (İçten Yanmalı)", styles['TableCell']), Paragraph("4.500$ (Elektrikli E-GMP)", styles['TableCell']), Paragraph("+13.500$ Enerji Tasarrufu", styles['TableCellBold'])],
        [Paragraph("Bakım & Aşınma Gideri", styles['TableCellBold']), Paragraph("8.000$", styles['TableCell']), Paragraph("2.000$ (Elektrikli Motor)", styles['TableCell']), Paragraph("+6.000$ Bakım Tasarrufu", styles['TableCellBold'])],
        [Paragraph("Trustia AaaS Yazılım Bedeli", styles['TableCellBold']), Paragraph("0$", styles['TableCell']), Paragraph("5.400$ (Aylık 450$ Lisans)", styles['TableCell']), Paragraph("-5.400$ (Yazılım Maliyeti)", styles['TableCell'])],
        [Paragraph("<b>Yıllık Net Filo Kârı / Araç</b>", styles['TableCellBold']), Paragraph("<b>12.000$</b>", styles['TableCell']), Paragraph("<b>67.500$</b>", styles['TableCellBold']), Paragraph("<b>+55.500$ Net Ek Kâr / Yıl</b>", styles['Badge'])],
    ]
    t_ue = Table(ue_data, colWidths=[45*mm, 45*mm, 45*mm, 47*mm])
    t_ue.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_ue)

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 3. BTM GORUSME VE YATIRIMCI REHBERI (03)
# -------------------------------------------------------------
def generate_btm_investor_guide(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("İTO BTM FULYA — YATIRIMCI VE DANIŞMANLIK STRATEJİK DOSYASI", styles['Title']))
    story.append(Paragraph("4 Eylül 2026 Cuma 15:00 Randevusu  •  Yatırım Masası Brifing ve Soru-Cevap Rehberi", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    story.append(Paragraph("1. GÖRÜŞMENİN AMACI VE HEDEFLENEN SOMUT ÇIKTILAR", styles['H1']))
    story.append(Paragraph(
        "4 Eylül 2026 Cuma günü saat 15:00'te Beşiktaş Polat Tower Rezidans'ta <b>BTM Yatırımcı İlişkileri Direktörlüğü</b> ile yapılacak birebir görüşmenin temel amacı:<br/>"
        "1. <b>TÜBİTAK 1812 BİGG Yatırım Programı:</b> BTM resmi uygulayıcı kuruluş kontenjanından <b>1.350.000 TL doğrudan nakit devlet sermayesi</b> başvurusunun resmileştirilmesi.<br/>"
        "2. <b>BTM Melek Yatırım Ağı (BTM Angels):</b> 500.000$ Pre-Seed turumuza liderlik edecek kurumsal meleklerin masaya davet edilmesi.<br/>"
        "3. <b>212 VC, ScaleX ve Bilişim Vadisi Tanışması:</b> BTM portföy yöneticisi kanalıyla kurumsal fonlara doğrudan sıcak yönlendirme (Warm Intro) sağlanması.<br/>"
        "4. <b>21-23 Ekim TURKCOMPOSITE Fuarı:</b> BTM Startup Village etabında Trustia'nın prototip standı ve protokol geçişinin kesinleştirilmesi.",
        styles['Body']
    ))

    story.append(Paragraph("2. YATIRIMCI VE DANIŞMANLARIN SORACAĞI 6 KRİTİK SORU & CEVAPLARI", styles['H1']))
    
    qa_list = [
        ("Soru 1: Henüz 17 yaşındasın, şirketi hukuken nasıl yöneteceksin?",
         "Cevap: Şirketimizin sermaye yapısı %80 Murat Furkan Bayram (Kurucu & Sistem Mimarı) ve %20 Doğukan Bayram (Kurucu Ortak & COO / Şirket Müdürü) olarak yapılandırılmıştır. Doğukan Bayram reşit şirket müdürü olarak tüm noter, imza sirküleri, banka ve resmi devlet sözleşmelerini asaleten temsil etmekte; Murat Furkan Bayram ise 16.000 satırlık deterministik otonomi mimarisini yönetmektedir."),
        
        ("Soru 2: Waymo ve Cruise gibi devler varken Trustia nasıl rekabet edecek?",
         "Cevap: Waymo ve Cruise 250.000-300.000 dolara sıfırdan araç üretmektedir; bu model yüksek amortisman nedeniyle ölçeklenemez. Trustia seri üretim elektrikli araçları (Hyundai Ioniq 5) sadece 35.000 dolarlık tak-çalıştır kitle dönüştürür. Filo sahibine 14 ayda geri dönen eşsiz bir birim ekonomi sunuyoruz."),
        
        ("Soru 3: Otonomi yazılımınızın güvenliğini nasıl kanıtlıyorsunuz?",
         "Cevap: Yazılımımız kara kutu nöral ağlar yerine matematiksel ispatlı Hybrid A* ve 3D NDT LiDAR SLAM tabanlı deterministik bir mimaridir. 1.301 birim ve entegrasyon testinden %100 başarıyla geçmiştir. T.C. Savunma Sanayii Başkanlığı'ndan 100/100 Tam Puan tescili almıştır ve ISO 26262 ASIL-D Minimal Risk Maneuver (MRM) acil durum frenleme protokolüne sahiptir."),
        
        ("Soru 4: Şu an şirketin nakit ihtiyacı nedir ve fonu nasıl kullanacaksınız?",
         "Cevap: 18 aylık pist ve ticari pilot operasyonlarımız için 500.000$ (5M$ Cap SAFE) Pre-Seed arıyoruz. Bu fonun %45'i Ouster OS2-128 LiDAR, Livox LiDAR'lar ve Jetson AGX Orin donanım tedariğine; %35'i mühendislik kadrosuna; %15'i kapalı pist testlerine ayrılacaktır."),
        
        ("Soru 5: Dubai World Challenge başvurunuz ne durumda?",
         "Cevap: Dubai Ulaşım Otoritesi'nin (RTA) 1.200.000$ nakit ödüllü küresel yarışmasına resmi başvurumuzu 2 Eylül'de eksiksiz teslim ettik. Kasım 2026'da finalistler açıklandığında Dubai'de canlı araç testlerine katılacağız."),
        
        ("Soru 6: Ekibinizde donanım tarafını kim yönetiyor?",
         "Cevap: Donanım ve araç entegrasyonumuzu, ASELSAN Aday Mühendis Havuzu üyesi ve TEKNOFEST Robotaksi Finalisti olan elektrik-elektronik mühendisimiz Denizcan Özcan yönetmektedir.")
    ]

    for q, a in qa_list:
        story.append(Paragraph(f"<b>{q}</b>", styles['H2']))
        story.append(Paragraph(a, styles['Body']))
        story.append(Spacer(1, 2))

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 4. RESMI DEVLET TESCİLLERİ VE AKREDİTASYONLAR (04)
# -------------------------------------------------------------
def generate_accreditations_dossier(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("TRUSTIA AI — RESMİ DEVLET TESCİLLERİ & AKREDİTASYONLAR", styles['Title']))
    story.append(Paragraph("T.C. Cumhurbaşkanlığı SSB, KOSGEB, TÜBİTAK ve İTO Tescil Sicil Portföyü  •  Eylül 2026", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    story.append(Paragraph("1. KURUMSAL TESCİL VE SERTİFİKA DÖKÜMÜ", styles['H1']))

    acc_data = [
        [Paragraph("Resmi Kurum", styles['TableHead']), Paragraph("Belge / Tescil Adı", styles['TableHead']), Paragraph("Sicil / Doğrulama No", styles['TableHead']), Paragraph("Hukuki Statü", styles['TableHead'])],
        [
            Paragraph("<b>T.C. Cumhurbaşkanlığı Savunma Sanayii Bşk. (SSB)</b>", styles['TableCell']),
            Paragraph("Yapay Zeka ve Otonom Sistem Yetkinlik Tescili (100/100 Tam Puan)", styles['TableCell']),
            Paragraph("<b>L2zPtN4X1ZJ</b>", styles['TableCellBold']),
            Paragraph("Onaylı / Mükemmel", styles['Badge'])
        ],
        [
            Paragraph("<b>KOSGEB (Sanayi ve Teknoloji Bakanlığı)</b>", styles['TableCell']),
            Paragraph("İleri Girişimci Resmi Tescil Sertifikası", styles['TableCell']),
            Paragraph("<b>KSB01UGE0115153370</b>", styles['TableCellBold']),
            Paragraph("Aktif Tescilli", styles['Badge'])
        ],
        [
            Paragraph("<b>TÜBİTAK (Bilimsel ve Teknolojik Araştırma K.)</b>", styles['TableCell']),
            Paragraph("ARBİS Milli Araştırmacı Sicili", styles['TableCell']),
            Paragraph("<b>TBTK-0229-6571</b>", styles['TableCellBold']),
            Paragraph("Kayıtlı Araştırmacı", styles['Badge'])
        ],
        [
            Paragraph("<b>İstanbul Ticaret Odası (İTO BTM)</b>", styles['TableCell']),
            Paragraph("Ön Kuluçka Sözleşmesi & Fulya Yerleşke Tahsisi", styles['TableCell']),
            Paragraph("<b>2026-II. Dönem Sözleşmesi</b>", styles['TableCellBold']),
            Paragraph("Sözleşmeli Girişim", styles['Badge'])
        ],
        [
            Paragraph("<b>ASELSAN Elektronik Sanayi A.Ş.</b>", styles['TableCell']),
            Paragraph("ASELSAN Tedarikçi Portalı Onaylı Girişimi", styles['TableCell']),
            Paragraph("<b>Tedarikçi No: Onaylı</b>", styles['TableCellBold']),
            Paragraph("Tedarikçi Havuzunda", styles['Badge'])
        ],
        [
            Paragraph("<b>Startups.watch (Resmi Girişim Ekosistemi)</b>", styles['TableCell']),
            Paragraph("Doğrulanmış Girişim Profili & Ekosistem Sıralaması", styles['TableCell']),
            Paragraph("<b>Ana Sayfa #1 Numara Sıralama</b>", styles['TableCellBold']),
            Paragraph("Doğrulanmış / Verified", styles['Badge'])
        ],
        [
            Paragraph("<b>RTA Dubai Government (Birleşik Arap Emirlikleri)</b>", styles['TableCell']),
            Paragraph("Dubai World Challenge for Self-Driving Transport ($1.2M)", styles['TableCell']),
            Paragraph("<b>Entry: MOweBqdp (Submitted)</b>", styles['TableCellBold']),
            Paragraph("Resmen Gönderildi", styles['Badge'])
        ]
    ]

    t_acc = Table(acc_data, colWidths=[45*mm, 52*mm, 45*mm, 36*mm])
    t_acc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_acc)
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. YAZILIM DOĞRULAMA VE OTOMATİK TEST SERTİFİKASI", styles['H1']))
    story.append(Paragraph(
        "Trustia Core otonomi mimarisi, sürekli entegrasyon (CI/CD) hatlarında her commit ve derlemede <b>1.301 otomatik testten</b> geçmektedir:<br/>"
        "• <b>Birim Testleri (Unit Tests):</b> 894 Test (%100 Başarı - Hibrit A* düğüm genişletme, SLAM kovaryans güncellemeleri, Kalman filtre kararlılığı).<br/>"
        "• <b>Entegrasyon Testleri:</b> 312 Test (%100 Başarı - CAN-FD sürücüleri, ROS2 mesaj köprüleri, Teltonika 5G telemetri soketleri).<br/>"
        "• <b>Güvenlik & Failsafe Testleri:</b> 95 Test (%100 Başarı - ASIL-D MRM acil frenleme, sensör körlüğü tespiti, can-bus spoofing engelleme).",
        styles['Body']
    ))

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 5. FINANSAL MODEL VE CAP TABLE (05)
# -------------------------------------------------------------
def generate_financials_dossier(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("TRUSTIA AI — 3 YILLIK FİNANSAL PROJEKSİYON & CAP TABLE", styles['Title']))
    story.append(Paragraph("Gelir Tablosu (P&L), Nakit Akışı, Birim Ekonomi ve Sermaye Yapısı  •  Eylül 2026", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    story.append(Paragraph("1. SERMAYE YAPISI (CAP TABLE)", styles['H1']))
    cap_data = [
        [Paragraph("Pay Sahibi", styles['TableHead']), Paragraph("Unvan & Görev", styles['TableHead']), Paragraph("Hisse Oranı (%)", styles['TableHead']), Paragraph("Hisse Türü", styles['TableHead']), Paragraph("Temsil Yetkisi", styles['TableHead'])],
        [Paragraph("<b>Murat Furkan Bayram</b>", styles['TableCellBold']), Paragraph("Kurucu & CEO / Sistem Mimarı", styles['TableCell']), Paragraph("<b>%80</b>", styles['TableCellBold']), Paragraph("A Grubu İmtiyazlı", styles['TableCell']), Paragraph("Münferiden Temsil", styles['TableCell'])],
        [Paragraph("<b>Doğukan Bayram</b>", styles['TableCellBold']), Paragraph("Kurucu Ortak & COO / Şirket Müdürü", styles['TableCell']), Paragraph("<b>%20</b>", styles['TableCellBold']), Paragraph("B Grubu Adi", styles['TableCell']), Paragraph("Münferiden Temsil", styles['TableCell'])],
        [Paragraph("<b>ESOP (Çalışan Havuzu)</b>", styles['TableCell']), Paragraph("Kilit Mühendislik Opsiyonu", styles['TableCell']), Paragraph("%10 (Ayrılacak)", styles['TableCell']), Paragraph("Opsiyon Havuzu", styles['TableCell']), Paragraph("Yönetim Kurulu", styles['TableCell'])],
    ]
    t_cap = Table(cap_data, colWidths=[40*mm, 48*mm, 28*mm, 32*mm, 34*mm])
    t_cap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cap)
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. 3 YILLIK KONSOLİDE GELİR TABLOSU PROJEKSİYONU (USD)", styles['H1']))
    pl_data = [
        [Paragraph("Metrik (USD)", styles['TableHead']), Paragraph("2026 (Yıl 1 - Pilot)", styles['TableHead']), Paragraph("2027 (Yıl 2 - BAE & TR)", styles['TableHead']), Paragraph("2028 (Yıl 3 - Global)", styles['TableHead'])],
        [Paragraph("Aktif Dönüştürülen Robotaksi Filosu", styles['TableCellBold']), Paragraph("5 Araç (Pilot)", styles['TableCell']), Paragraph("80 Araç", styles['TableCell']), Paragraph("500 Araç", styles['TableCell'])],
        [Paragraph("Dönüşüm Kiti Gelirleri ($35k/araç)", styles['TableCellBold']), Paragraph("175.000$", styles['TableCell']), Paragraph("2.800.000$", styles['TableCell']), Paragraph("17.500.000$", styles['TableCell'])],
        [Paragraph("AaaS Yazılım & Telemetri Gelirleri", styles['TableCellBold']), Paragraph("27.000$", styles['TableCell']), Paragraph("432.000$", styles['TableCell']), Paragraph("2.700.000$", styles['TableCell'])],
        [Paragraph("Savunma & Özel Proje Lisansları", styles['TableCellBold']), Paragraph("100.000$", styles['TableCell']), Paragraph("500.000$", styles['TableCell']), Paragraph("2.000.000$", styles['TableCell'])],
        [Paragraph("<b>TOPLAM BRÜT GELİR</b>", styles['TableCellBold']), Paragraph("<b>302.000$</b>", styles['TableCellBold']), Paragraph("<b>3.732.000$</b>", styles['TableCellBold']), Paragraph("<b>22.200.000$</b>", styles['TableCellBold'])],
        [Paragraph("Satılan Malın Maliyeti (COGS - Donanım)", styles['TableCell']), Paragraph("(115.000$)", styles['TableCell']), Paragraph("(1.760.000$)", styles['TableCell']), Paragraph("(10.500.000$)", styles['TableCell'])],
        [Paragraph("Ar-Ge ve Mühendislik Maaşları", styles['TableCell']), Paragraph("(120.000$)", styles['TableCell']), Paragraph("(480.000$)", styles['TableCell']), Paragraph("(1.600.000$)", styles['TableCell'])],
        [Paragraph("Pist Testleri, Sertifikasyon & Genel Yönetim", styles['TableCell']), Paragraph("(45.000$)", styles['TableCell']), Paragraph("(180.000$)", styles['TableCell']), Paragraph("(600.000$)", styles['TableCell'])],
        [Paragraph("<b>FAVÖK / EBITDA</b>", styles['TableCellBold']), Paragraph("<b>22.000$ (%7.2)</b>", styles['TableCellBold']), Paragraph("<b>1.312.000$ (%35.1)</b>", styles['Badge']), Paragraph("<b>9.500.000$ (%42.7)</b>", styles['Badge'])],
    ]
    t_pl = Table(pl_data, colWidths=[55*mm, 42*mm, 42*mm, 43*mm])
    t_pl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_pl)

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 6. MURAT FURKAN BAYRAM RESMI CV (06)
# -------------------------------------------------------------
def generate_founder_cv(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("MURAT FURKAN BAYRAM", styles['Title']))
    story.append(Paragraph("Kurucu & CEO / Baş Sistem Mimarı  •  Trustia Otonom Mobilite Teknolojileri A.Ş.", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    cv_top = [
        [
            Paragraph("<b>Doğum Tarihi & Yaş:</b> 04.02.2009 (17 Yaşında)<br/>"
                      "<b>İkamet & Ofis:</b> Beşiktaş / İstanbul (İTO BTM Fulya Kampüsü)<br/>"
                      "<b>T.C. Kimlik No:</b> 59476566862", styles['TableCell']),
            Paragraph("<b>E-Posta:</b> kariyer@trustia.com.tr<br/>"
                      "<b>Telefon:</b> +90 537 064 0460<br/>"
                      "<b>LinkedIn:</b> linkedin.com/in/trustia", styles['TableCell']),
            Paragraph("<b>T.C. Savunma Tescili:</b> SSB 100/100 Tam Puan<br/>"
                      "<b>KOSGEB Sicil:</b> KSB01UGE0115153370<br/>"
                      "<b>TÜBİTAK Sicil:</b> TBTK-0229-6571", styles['TableCell']),
        ]
    ]
    t_top = Table(cv_top, colWidths=[60*mm, 62*mm, 60*mm])
    t_top.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_top)
    story.append(Spacer(1, 8))

    story.append(Paragraph("PROFESYONEL ÖZET & MİMARİ YETKİNLİK", styles['H1']))
    story.append(Paragraph(
        "17 yaşında derin teknoloji kurucusu ve yazılım sistem mimarı. Sıfırdan 16.000 satırlık deterministik SAE Seviye-4 otonom sürüş motoru, 3D NDT LiDAR SLAM haritalama, Pure Pursuit lateral kontrolcü ve CAN-FD araç kontrol sürücüleri geliştirmiştir. T.C. Savunma Sanayii Başkanlığı Yapay Zeka Değerlendirmesi'nden 100/100 Tam Puan tescili almış ve RTA Dubai'nin 1.2M$ ödüllü otonom araç yarışmasına Türkiye'den resmi proje sunmuştur.",
        styles['Body']
    ))

    story.append(Paragraph("TEKNİK DERİNLİK & DİLLER", styles['H1']))
    story.append(Paragraph(
        "• <b>Diller & Kütüphaneler:</b> Modern C++ (C++17/20), Python 3.11, CUDA, TensorRT, ROS2 Humble, Eigen3, PCL (Point Cloud Library).<br/>"
        "• <b>Otonomi & Kontrol:</b> Hybrid A* kinematik yol planlama, Extended Kalman Filter (ESKF), Pure Pursuit, Model Predictive Control (MPC).<br/>"
        "• <b>Donanım Protokolleri:</b> Kvaser CAN-FD, SocketCAN, Ethernet UDP/PTP, GMSL2 HDR Kameralar, Ouster OS2-128, Livox Mid-360.<br/>"
        "• <b>Güvenlik & Emniyet:</b> ISO 26262 ASIL-D, Minimal Risk Maneuver (MRM), SOTIF, Zero-Trust CAN-FD Ağ Güvenliği.",
        styles['Body']
    ))

    story.append(Paragraph("RESMİ BAŞARILAR & TESCİLLER", styles['H1']))
    story.append(Paragraph(
        "• <b>SSB Yapay Zeka Değerlendirmesi 100/100 Tam Puan:</b> T.C. Savunma Sanayii Başkanlığı tarafından verilen resmi yetkinlik belgesi (L2zPtN4X1ZJ).<br/>"
        "• <b>Dubai World Challenge for Self-Driving Transport ($1.2M):</b> RTA Dubai resmi meydan okuma başvurusu tamamlandı (Entry: MOweBqdp).<br/>"
        "• <b>İTO BTM Fulya Kampüsü Yerleşik Girişimcisi:</b> İstanbul Ticaret Odası 2026-II. Dönem sözleşmeli girişimcisi.<br/>"
        "• <b>KOSGEB İleri Girişimci:</b> Sanayi ve Teknoloji Bakanlığı resmi onaylı genç ileri girişimci belgesi.<br/>"
        "• <b>TÜBİTAK ARBİS Milli Araştırmacı:</b> Türkiye Bilimsel ve Teknolojik Araştırma Kurumu araştırmacı sicili.<br/>"
        "• <b>Startups.watch:</b> Doğrulanmış girişim profili ve ana sayfa #1 numara sıralama.",
        styles['Body']
    ))

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 7. DUBAI WORLD CHALLENGE RESMI DOSYASI (07)
# -------------------------------------------------------------
def generate_dubai_challenge_dossier(out_path):
    styles = get_corporate_styles()
    story = []

    story.append(Paragraph("DUBAI WORLD CHALLENGE FOR SELF-DRIVING TRANSPORT", styles['Title']))
    story.append(Paragraph("RTA Dubai 5th Edition ($1,200,000 USD Prize Pool)  •  Official Entry Submission Dossier", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    sub_data = [
        [Paragraph("Metrik / Parametre", styles['TableHead']), Paragraph("Resmi Başvuru Detayı", styles['TableHead'])],
        [Paragraph("Yarışma Otoritesi", styles['TableCellBold']), Paragraph("Government of Dubai — Roads and Transport Authority (RTA)", styles['TableCell'])],
        [Paragraph("Yarışma Sezonu & Teması", styles['TableCellBold']), Paragraph("Dubai Autonomous Transport World Challenge 2027 — Smart Integrated Infrastructure", styles['TableCell'])],
        [Paragraph("Toplam Nakit Ödül Havuzu", styles['TableCellBold']), Paragraph("<b>$1,200,000 USD (Yaklaşık 42 Milyon TL)</b>", styles['TableCellBold'])],
        [Paragraph("Katılımcı / Girişim Adı", styles['TableCellBold']), Paragraph("Trustia AI (Murat Furkan Bayram)", styles['TableCell'])],
        [Paragraph("Kategori", styles['TableCellBold']), Paragraph("1. Çözüm Sağlayıcılar (Solution Providers / Bireysel Varlık)", styles['TableCell'])],
        [Paragraph("Başvuru Durumu", styles['TableCellBold']), Paragraph("<b>GÖNDERİLDİ / SUBMITTED (2 Eylül 2026) — Doğrulandı</b>", styles['Badge'])],
        [Paragraph("Bir Sonraki Aşama", styles['TableCellBold']), Paragraph("<b>Kasım 2026: RTA Uluslararası Jürisi Tarafından Finalistlerin İlanı</b>", styles['TableCellBold'])],
        [Paragraph("Canlı Test & Büyük Final", styles['TableCellBold']), Paragraph("Eylül 2027: Dubai World Congress for Self-Driving Transport (Ödül Töreni)", styles['TableCell'])],
    ]
    t_sub = Table(sub_data, colWidths=[65*mm, 117*mm])
    t_sub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_sub)
    story.append(Spacer(1, 10))

    story.append(Paragraph("RTA DUBAI'YE SUNULAN TEKNİK VE OPERASYONEL ÇÖZÜM", styles['H1']))
    story.append(Paragraph(
        "<b>Kullanım Senaryoları (Use Cases):</b><br/>"
        "• <b>UC-01:</b> Hyundai Ioniq 5 E-GMP platformu üzerine inşa edilmiş, tak-çalıştır SAE Seviye-4 otonom taksi kiti.<br/>"
        "• <b>UC-06:</b> Çift yönlü savunmasız yol kullanıcısı (VRU - yaya, e-scooter, bisikletli) emniyeti (50ms reaksiyon süreli acil frenleme).<br/>"
        "• <b>UC-07:</b> Otomatik Vale Park Hizmeti (AVP) ve DEWA şarj istasyonlarına otonom yanaşma.<br/>"
        "• <b>Diğer:</b> Talep üzerine (on-demand) sürücüsüz kentsel robotaksi filosu ve ilk/son kilometre banliyö servisleri.<br/><br/>"
        "<b>Çöl Koşullarına Dayanıklılık (50°C):</b><br/>"
        "Ouster ve Livox LiDAR'larımız IP68/IP69K sızdırmazlık standardında olup; NVIDIA Orin işlemcisi basınçlı hava kanallı özel termal soğutma tepsisinde barındırılmaktadır. Continental 77GHz radarları kum fırtınasında görüşü korur.",
        styles['Body']
    ))

    build_pdf(out_path, story)

# -------------------------------------------------------------
# 8. MASTER INVESTOR PITCH DECK (00)
# -------------------------------------------------------------
def generate_master_pitch_deck(out_path):
    styles = get_corporate_styles()
    story = []

    # Slide 1: Cover
    story.append(Paragraph("TRUSTIA AI — RESMİ YATIRIMCI SUNUMU (MASTER PITCH DECK 2026)", styles['Title']))
    story.append(Paragraph("Elektrikli Araçlar İçin Tak-Çalıştır Seviye-4 Otonom Sürüş Kiti ve Deterministik Seyrüsefer Mimarisi", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=C_SECONDARY, spaceBefore=0, spaceAfter=8))

    cover_box = [
        [
            Paragraph("<b>Kurucu & Sistem Mimarı:</b><br/>Murat Furkan Bayram (17 Yaşında, %80 Hisse)<br/>"
                      "<b>Yönetici Ortak & COO:</b><br/>Doğukan Bayram (%20 Hisse, Şirket Müdürü)<br/>"
                      "<b>Donanım Entegrasyon:</b><br/>Denizcan Özcan (ASELSAN Aday Müh., TEKNOFEST Finalisti)", styles['TableCell']),
            Paragraph("<b>Hedef Yatırım Turu:</b><br/>500.000$ USD Pre-Seed (5M$ Cap SAFE)<br/>"
                      "<b>Yerleşke & Kuluçka:</b><br/>İTO BTM Fulya Kampüsü (Polat Tower Rezidans)<br/>"
                      "<b>Doğrulanmış Sıralama:</b><br/>Startups.watch Resmi Onaylı Girişim (#1)", styles['TableCell']),
            Paragraph("<b>T.C. Savunma Tescili:</b><br/>SSB 100/100 Tam Puan (L2zPtN4X1ZJ)<br/>"
                      "<b>KOSGEB & TÜBİTAK:</b><br/>İleri Girişimci & ARBİS Tescilli<br/>"
                      "<b>Küresel Yarış:</b><br/>Dubai World Challenge 1.2M$ (Gönderildi)", styles['TableCell'])
        ]
    ]
    t_c = Table(cover_box, colWidths=[60*mm, 62*mm, 60*mm])
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 1, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_c)
    story.append(Spacer(1, 10))

    # Slide 2: Problem & Fırsat
    story.append(Paragraph("1. PAZAR PROBLEMİ VE DEVASA FIRSAT", styles['H1']))
    story.append(Paragraph(
        "<b>Problem:</b> Küresel mobilite şirketleri (Waymo, Cruise, Zoox), özel tasarım sürücüsüz araç üretmek için araç başına <b>250.000$ - 350.000$</b> harcamaktadır. Yüksek sermaye ihtiyacı (CAPEX) ve aşırı amortisman nedeniyle bu araçlar geniş kitlelere yayılamamaktadır. Öte yandan taksi filoları şoför maliyetleri, kaza riskleri ve regülasyon baskısı altındadır.<br/>"
        "<b>Pazar Büyüklüğü:</b> Küresel otonom ulaşım pazarı 2030'da <b>118 Milyar Dolara</b> ulaşmaktadır. Dubai Devleti 2030'a kadar tüm ulaşımın %25'ini sürücüsüz yapmayı kanunlaştırmıştır.",
        styles['Body']
    ))

    # Slide 3: Çözüm
    story.append(Paragraph("2. TRUSTIA ÇÖZÜMÜ: MODÜLER RETROFIT DÖNÜŞÜM KİTİ", styles['H1']))
    story.append(Paragraph(
        "Trustia AI; sıfırdan araç üretmek yerine seri üretim elektrikli araçları (Hyundai Ioniq 5 E-GMP) <b>48 saat içinde 35.000 dolarlık tak-çalıştır donanım ve yazılım kitiyle SAE Seviye-4 otonom Robotaksi'ye</b> dönüştürür. Aracın orijinal şasi ve kablo tesisatı delinmez; Kvaser U100 CAN-FD arayüzü ile doğrudan Drive-by-Wire sürüş komutları enjekte edilir.",
        styles['Body']
    ))

    # Slide 4: Teknoloji ve Deterministik Yazılım
    story.append(Paragraph("3. DERİN TEKNOLOJİ: 16.000 SATIR DETERMINİSTİK ÇEKİRDEK", styles['H1']))
    story.append(Paragraph(
        "• <b>Matematiksel Güvenlik:</b> Güvenilmez kara kutu yapay zekalar yerine Ackermann araç dinamiğini 50ms altında çözen <b>Hibrit A* (Hybrid A*) kinematik yol planlayıcı</b>.<br/>"
        "• <b>GNSS Olmadan 5cm Hassasiyet:</b> 400Hz ESKF + 3D NDT LiDAR SLAM haritalama motoru ile tünellerde ve gökdelen vadilerinde kesintisiz konumlandırma.<br/>"
        "• <b>1.301 Otomatik Test:</b> CI/CD hatlarında %100 başarıyla çalışan birim ve entegrasyon test mimarisi.<br/>"
        "• <b>ASIL-D Emniyet:</b> ISO 26262 Minimal Risk Maneuver (MRM) ile sensör körlüğünde otomatik güvenli yol kenarına çekme protokolü.",
        styles['Body']
    ))

    # Slide 5: Donanım Mimarisi
    story.append(Paragraph("4. DONANIM VE SENSÖR MİMARİSİ", styles['H1']))
    story.append(Paragraph(
        "• <b>LiDAR:</b> 1x Ouster OS2-128 Rev7 (Çatı, 360° 128 lazer) + 2x Livox Mid-360 (Ön/Arka kör nokta).<br/>"
        "• <b>Radar & Kamera:</b> 2x Continental ARS 408-21 77GHz radar + 4x Sony IMX390 HDR GMSL2 otomotiv kamera.<br/>"
        "• <b>İşlemci:</b> NVIDIA Jetson AGX Orin 64GB (275 TOPS AI işlem gücü, Seeed J501 endüstriyel taşıyıcı).<br/>"
        "• <b>Bağlantı:</b> Teltonika RUTX50 5G/V2X + Kvaser U100 CAN-FD galvanik izolasyonlu kontrol köprüsü.",
        styles['Body']
    ))

    # Slide 6: İş Modeli & Gelir Akışları
    story.append(Paragraph("5. İŞ MODELİ VE KÂRLILIK MATRİSİ", styles['H1']))
    story.append(Paragraph(
        "<b>Çift Katmanlı Gelir Modeli:</b><br/>"
        "1. <b>Kit Satışı (CAPEX):</b> Araç başı 35.000$ dönüşüm kiti satışı (%35 brüt kâr marjı).<br/>"
        "2. <b>Autonomy-as-a-Service (AaaS - Yıllık Düzenli Gelir):</b> Kilometre başı 0.18$ veya araç başı aylık 450$ yazılım lisansı ve filo telemetri aboneliği.<br/>"
        "• <b>Filo ROI:</b> Dönüştürülen her araç filo sahibine yılda 55.500$ net tasarruf ve kâr sağlar; 14 ayda maliyetini amorti eder.",
        styles['Body']
    ))

    # Slide 7: Yatırım Teklifi & Fon Kullanımı
    story.append(Paragraph("6. YATIRIM TEKLİFİ VE 18 AYLIK YOL HARİTASI", styles['H1']))
    story.append(Paragraph(
        "<b>Aranan Yatırım:</b> <b>500.000$ USD (Pre-Seed / 5M$ Cap SAFE)</b>.<br/>"
        "• <b>%45 Donanım & Sensör:</b> İlk 2 adet Hyundai Ioniq 5 test filosunun dönüşümü ve sensör stok alımı.<br/>"
        "• <b>%35 Mühendislik Kadrosu:</b> Gömülü yazılım, SLAM ve donanım test mühendislerinin istihdamı.<br/>"
        "• <b>%15 Pist ve Saha Testleri:</b> Bilişim Vadisi ve Dubai proving ground pist test operasyonları.<br/>"
        "• <b>%5 Emniyet & Patent:</b> ISO 26262 ASIL-D validasyon ve küresel fikri mülkiyet tescilleri.<br/>"
        "<b>Hedef Çıktı:</b> 18 ay içinde BAE ve Türkiye'de ilk 100 ticari robotaksinin sahaya indirilmesi.",
        styles['Body']
    ))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>İletişim & Demo Talebi:</b> Murat Furkan Bayram (Kurucu & CEO) | +90 537 064 0460 | kariyer@trustia.com.tr | İTO BTM Fulya Kampüsü, Beşiktaş / İstanbul", styles['Callout']))

    build_pdf(out_path, story)

def main():
    cikti_dir = r"C:\Users\Murat\Desktop\Çıktı"
    btm_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\BTM_Gorusme_Cikti_Dosyasi"
    pitch_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Pitch_Decks"
    kanvas_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Is_Plani_ve_Kanvas"
    fin_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Finansal_Tablolar"

    for d in [cikti_dir, btm_dir, pitch_dir, kanvas_dir, fin_dir]:
        os.makedirs(d, exist_ok=True)

    # 0. Master Pitch Deck
    p0 = os.path.join(cikti_dir, "00_Trustia_AI_Master_Yatirimci_Sunumu_Pitch_Deck_2026.pdf")
    generate_master_pitch_deck(p0)
    shutil.copy(p0, os.path.join(pitch_dir, "00_Trustia_AI_Master_Yatirimci_Sunumu_Pitch_Deck_2026.pdf"))
    shutil.copy(p0, os.path.join(btm_dir, "00_Trustia_AI_Master_Yatirimci_Sunumu_Pitch_Deck_2026.pdf"))

    # 1. Executive One Pager
    p1 = os.path.join(cikti_dir, "01_Trustia_AI_Executive_One_Pager_2026.pdf")
    generate_one_pager(p1)
    shutil.copy(p1, os.path.join(btm_dir, "01_Trustia_AI_Executive_One_Pager_2026.pdf"))
    shutil.copy(p1, os.path.join(pitch_dir, "01_Trustia_AI_Executive_One_Pager_2026.pdf"))

    # 2. Is Modeli Kanvasi
    p2 = os.path.join(cikti_dir, "02_Trustia_AI_Is_Modeli_Kanvasi_ve_Gelir_Plani_2026.pdf")
    generate_business_model_canvas(p2)
    shutil.copy(p2, os.path.join(btm_dir, "02_Trustia_AI_Is_Modeli_Kanvasi_ve_Gelir_Plani_2026.pdf"))
    shutil.copy(p2, os.path.join(kanvas_dir, "02_Trustia_AI_Is_Modeli_Kanvasi_ve_Gelir_Plani_2026.pdf"))

    # 3. BTM Gorusme & Yatirimci Rehberi
    p3 = os.path.join(cikti_dir, "03_Trustia_AI_BTM_Fulya_Gorusme_ve_Yatirimci_Rehberi_2026.pdf")
    generate_btm_investor_guide(p3)
    shutil.copy(p3, os.path.join(btm_dir, "03_Trustia_AI_BTM_Fulya_Gorusme_ve_Yatirimci_Rehberi_2026.pdf"))

    # 4. Resmi Akreditasyonlar
    p4 = os.path.join(cikti_dir, "04_Trustia_AI_Resmi_Devlet_Tescilleri_ve_Akreditasyonlar_2026.pdf")
    generate_accreditations_dossier(p4)
    shutil.copy(p4, os.path.join(btm_dir, "04_Trustia_AI_Resmi_Devlet_Tescilleri_ve_Akreditasyonlar_2026.pdf"))

    # 5. Finansal Model ve Cap Table
    p5 = os.path.join(cikti_dir, "05_Trustia_AI_Finansal_Model_ve_Cap_Table_2026.pdf")
    generate_financials_dossier(p5)
    shutil.copy(p5, os.path.join(fin_dir, "05_Trustia_AI_Finansal_Model_ve_Cap_Table_2026.pdf"))

    # 6. Murat Furkan Bayram CV
    p6 = os.path.join(cikti_dir, "06_Murat_Furkan_Bayram_CV_Resume_2026.pdf")
    generate_founder_cv(p6)
    shutil.copy(p6, os.path.join(btm_dir, "06_Murat_Furkan_Bayram_CV_Resume_2026.pdf"))
    shutil.copy(p6, r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Murat_Furkan_Bayram_CV_Resume.pdf")

    # 7. Dubai World Challenge Resmi Basvuru Ozeti
    p7 = os.path.join(cikti_dir, "07_Trustia_AI_Dubai_World_Challenge_Resmi_Basvuru_Ozeti_2026.pdf")
    generate_dubai_challenge_dossier(p7)
    shutil.copy(p7, os.path.join(pitch_dir, "07_Trustia_AI_Dubai_World_Challenge_Resmi_Basvuru_Ozeti_2026.pdf"))

    # 8. Copy Denizcan Ozcan CV & Robotaxi Master Plan if present
    robotaxi_source = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Teknik_ve_Organizasyon\06_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf"
    if os.path.exists(robotaxi_source):
        dst_robotaxi = os.path.join(cikti_dir, "08_Trustia_AI_Hyundai_Ioniq5_Seviye4_Robotaksi_Master_Plan.pdf")
        if os.path.abspath(robotaxi_source) != os.path.abspath(dst_robotaxi):
            shutil.copy(robotaxi_source, dst_robotaxi)

    denizcan_candidates = [
        r"C:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\BTM_Gorusme_Cikti_Dosyasi\05_Aday_Muhendis_Denizcan_Ozcan_CV.pdf",
        r"C:\Users\Murat\Desktop\Çıktı\09_Aday_Muhendis_Denizcan_Ozcan_CV.pdf"
    ]
    for cand in denizcan_candidates:
        if os.path.exists(cand):
            dst_denizcan = os.path.join(cikti_dir, "09_Aday_Muhendis_Denizcan_Ozcan_CV.pdf")
            if os.path.abspath(cand) != os.path.abspath(dst_denizcan):
                shutil.copy(cand, dst_denizcan)
            dst_btm = os.path.join(btm_dir, "09_Aday_Muhendis_Denizcan_Ozcan_CV.pdf")
            if os.path.abspath(cand) != os.path.abspath(dst_btm):
                shutil.copy(cand, dst_btm)
            break

    print("[SUCCESS] All corporate dossiers updated flawlessly!")

if __name__ == "__main__":
    main()
