import os
import sys
import shutil
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

# Register TrueType Fonts
font_dir = r"C:\Windows\Fonts"
try:
    pdfmetrics.registerFont(TTFont('Arial', os.path.join(font_dir, 'arial.ttf')))
    pdfmetrics.registerFont(TTFont('Arial-Bold', os.path.join(font_dir, 'arialbd.ttf')))
    pdfmetrics.registerFont(TTFont('Arial-Italic', os.path.join(font_dir, 'ariali.ttf')))
except Exception as e:
    print(f"Font loading warning: {e}")

# Color Palette - Deep Tech, Clean Aerospace & Tactical Autonomy
C_PRIMARY = colors.HexColor('#0A192F')       # Deep Navy / Slate 950
C_SECONDARY = colors.HexColor('#0284C7')     # Tech Electric Blue
C_ACCENT = colors.HexColor('#059669')        # Emerald Green (Verified / Success)
C_DARK = colors.HexColor('#0F172A')          # Slate 900
C_MUTED = colors.HexColor('#475569')         # Slate 600
C_LIGHT_BG = colors.HexColor('#F8FAFC')      # Slate 50
C_CARD = colors.HexColor('#F1F5F9')          # Slate 100
C_BORDER = colors.HexColor('#CBD5E1')        # Slate 300
C_WHITE = colors.HexColor('#FFFFFF')
C_DEFENSE = colors.HexColor('#9A3412')       # Tactical Defense Amber
C_AGRI = colors.HexColor('#15803D')          # Agriculture Forest Green
C_HIGHLIGHT = colors.HexColor('#EFF6FF')     # Light Tech Blue

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
            self.drawString(34*mm, 285*mm, "|  Seviye-4 Otonom Sürüş Kiti & Deterministik Seyrüsefer  •  Resmi Master Dosya")
            self.drawRightString(196*mm, 285*mm, "Eylül 2026")
            
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.6)
            self.line(14*mm, 282*mm, 196*mm, 282*mm)

        # Footer (all pages)
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.6)
        self.line(14*mm, 13*mm, 196*mm, 13*mm)
        
        self.setFont('Arial-Bold', 7.5)
        self.setFillColor(C_PRIMARY)
        self.drawString(14*mm, 9*mm, "TRUSTIA AI")
        self.setFont('Arial', 7.5)
        self.setFillColor(C_MUTED)
        self.drawString(33*mm, 9*mm, "|  İTO BTM Fulya Kampüsü, Şişli / İstanbul  •  trustia.com.tr  •  github.com/Trustia/Trustia")
        self.drawRightString(196*mm, 9*mm, f"Sayfa {self._pageNumber} / {page_count}")
        self.restoreState()

def get_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles['Title'] = ParagraphStyle(
        'DocTitle',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=17,
        leading=21,
        textColor=C_PRIMARY,
        spaceAfter=3
    )
    styles['Subtitle'] = ParagraphStyle(
        'DocSubtitle',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=9,
        leading=12.5,
        textColor=C_SECONDARY,
        spaceAfter=6
    )
    styles['H1'] = ParagraphStyle(
        'DocH1',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=11.5,
        leading=14.5,
        textColor=C_PRIMARY,
        spaceBefore=6,
        spaceAfter=3
    )
    styles['H2'] = ParagraphStyle(
        'DocH2',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=C_SECONDARY,
        spaceBefore=4,
        spaceAfter=2
    )
    styles['Body'] = ParagraphStyle(
        'DocBody',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=8.2,
        leading=11.5,
        textColor=C_DARK,
        spaceAfter=3
    )
    styles['BodyBold'] = ParagraphStyle(
        'DocBodyBold',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=8.2,
        leading=11.5,
        textColor=C_DARK,
        spaceAfter=3
    )
    styles['Callout'] = ParagraphStyle(
        'DocCallout',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=C_PRIMARY
    )
    styles['TableCell'] = ParagraphStyle(
        'DocTableCell',
        parent=base['Normal'],
        fontName='Arial',
        fontSize=7.5,
        leading=10,
        textColor=C_DARK
    )
    styles['TableCellBold'] = ParagraphStyle(
        'DocTableCellBold',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=7.5,
        leading=10,
        textColor=C_PRIMARY
    )
    styles['TableHead'] = ParagraphStyle(
        'DocTableHead',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=C_WHITE
    )
    styles['BadgeGreen'] = ParagraphStyle(
        'DocBadgeGreen',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=7.2,
        leading=9,
        textColor=C_ACCENT
    )
    styles['BadgeBlue'] = ParagraphStyle(
        'DocBadgeBlue',
        parent=base['Normal'],
        fontName='Arial-Bold',
        fontSize=7.2,
        leading=9,
        textColor=C_SECONDARY
    )
    styles['Caption'] = ParagraphStyle(
        'DocCaption',
        parent=base['Normal'],
        fontName='Arial-Italic',
        fontSize=6.8,
        leading=8.5,
        textColor=C_MUTED,
        alignment=1
    )
    return styles

def build_pdf(filename, story):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=14*mm,
        rightMargin=14*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Generated Master PDF: {filename}")

def generate_master_dossier(out_path):
    img_dir = r"c:\Users\Murat\Desktop\Trustia\06_Medya_Gorsel_ve_Tanitim_Videolari\Hyundai_Ioniq_5_Test_Araci"
    f1 = os.path.join(img_dir, "Ioniq5_Foto_1_Temiz.png")
    f2 = os.path.join(img_dir, "Ioniq5_Foto_2_Temiz.png")
    f3 = os.path.join(img_dir, "Ioniq5_Foto_3_Temiz.png")
    f4 = os.path.join(img_dir, "Ioniq5_Foto_4_Temiz.png")
    f5 = os.path.join(img_dir, "Ioniq5_Foto_5_Temiz.png")
    f6 = os.path.join(img_dir, "Ioniq5_Foto_6_Temiz.png")
    f7 = os.path.join(img_dir, "Ioniq5_Foto_7_Temiz.png")

    styles = get_styles()
    story = []

    # =========================================================================
    # BÖLÜM 1: GİRİŞ, KURUMSAL KİMLİK VE STRATEJİK VİZYON
    # =========================================================================

    # SAYFA 1: MASTER KAPAK & YÖNETİCİ BRİFİNGİ
    story.append(Paragraph("TRUSTIA AI — MASTER YATIRIMCI VE TEKNİK DOSYASI (2026)", styles['Title']))
    story.append(Paragraph("Elektrikli Araçlar İçin Tak-Çalıştır Seviye-4 Otonomi Kiti, Deterministik Seyrüsefer Mimarisi & Çok Sektörlü Uygulamalar", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=4))

    # ULUSAL BASIN & MEDYA ONAYI BANNERI (EGİRİŞİM ÖZEL MANŞETİ)
    media_banner_data = [
        [
            Paragraph(
                "<b>📰 GÜNCEL BASIN VE MEDYA MANŞETİ (4 EYLÜL 2026 — EGİRİŞİM):</b><br/>"
                "Trustia AI, Türkiye'nin lider girişimcilik ve teknoloji yayını <b>egirişim</b>'de resmi manşet haberi olarak yer almıştır:<br/>"
                "<b>«Elektrikli araçları Seviye-4 otonom platformlara dönüştürmeyi hedefleyen girişim: Trustia AI»</b> "
                "<font color='#0284C7'>(Yazar: Hilmi Öğütcü • egirisim.com • Resmi X / Twitter Gönderisi: 1.200+ Görüntülenme)</font>",
                styles['TableCellBold']
            )
        ]
    ]
    t_media_banner = Table(media_banner_data, colWidths=[182*mm])
    t_media_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1.2, C_SECONDARY),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_media_banner)
    story.append(Spacer(1, 3))

    if os.path.exists(f1):
        img_hero = RLImage(f1, width=182*mm, height=68*mm)
        story.append(img_hero)
        story.append(Spacer(1, 3))

    info_table = [
        [
            Paragraph("<b>Kurucu & Sistem Mimarı:</b><br/>Murat Furkan Bayram (17 Yaşında, %80 Hisse)<br/>"
                      "<b>Kurucu Ortak:</b><br/>Doğukan Bayram (%20 Hisse)<br/>"
                      "<b>Donanım Entegrasyon:</b><br/>Denizcan Özcan (ASELSAN Aday Müh.)", styles['TableCell']),
            Paragraph("<b>Resmi Kuluçka Merkezi:</b><br/>İTO BTM Fulya Kampüsü, Şişli / İstanbul<br/>"
                      "<b>Resmi Devlet Tescili:</b><br/>T.C. SSB 100/100 Tam Puan (L2zPtN4X1ZJ)<br/>"
                      "<b>KOSGEB & TÜBİTAK:</b><br/>İleri Girişimci & ARBİS Milli Sicil", styles['TableCell']),
            Paragraph("<b>Doğrulanmış Kod Mimarisi:</b><br/>16.000 Satır C++/Python Çekirdeği<br/>"
                      "<b>Otomatik Test Başarısı:</b><br/>1.301 / 1.301 Yeşil Test (%100 Başarı)<br/>"
                      "<b>Resmi Basın & Medya:</b><br/>egirisim.com Özel Manşet Haberi", styles['TableCell'])
        ]
    ]
    t_info = Table(info_table, colWidths=[60*mm, 62*mm, 60*mm])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>YÖNETİCİ ÖZETİ (EXECUTIVE SUMMARY)</b>", styles['H1']))
    story.append(Paragraph(
        "Trustia AI; sıfırdan araç üretmek yerine seri üretim elektrikli araçları (öncelikle Hyundai Ioniq 5 E-GMP platformu) "
        "<b>48 saat içinde tak-çalıştır donanım ve yazılım kiti ile SAE Seviye-4 otonom araca dönüştüren</b> derin teknoloji girişimidir. "
        "Otonomi mimarimiz sadece binek robotaksiler için değil; <b>Savunma Sanayii İKA (İnsansız Kara Aracı)</b> sistemleri ve "
        "<b>Otonom Tarım/Endüstriyel Makineler</b> için de aynı deterministik seyrüsefer çekirdeğini kullanır. "
        "Sektördeki küresel oyuncuların araç başı 250.000$+ özel üretim maliyetlerine karşılık Trustia; "
        "35.000$'lık modüler dönüşüm kitiyle <b>%70 maliyet avantajı</b> ve <b>14 aylık yatırım geri dönüş süresi (ROI)</b> sunmaktadır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 2: KÜRESEL PROBLEM, DEVASA FIRSAT VE PAZAR BÜYÜKLÜĞÜ
    story.append(Paragraph("1. PAZAR PROBLEMİ VE DEVASA TİCARİ FIRSAT", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Bugün küresel ulaşım, savunma lojistiği ve tarım sektörleri üç devasa yapısal krizle karşı karşıyadır:",
        styles['Body']
    ))

    prob_box = [
        [
            Paragraph("<b>1. Yüksek Araç Üretim Maliyeti (CAPEX Çıkmazı)</b><br/>"
                      "Waymo, Cruise ve Zoox gibi küresel devler, özel şasili otonom araç üretmek için araç başına <b>250.000$ - 350.000$</b> harcamaktadır. Bu devasa sermaye yükü filoların hızlı büyümesini ve kârlılığa geçişini engellemektedir. Mevcut taksi ve servis filoları bu maliyetleri finanse edemez.", styles['TableCell']),
            Paragraph("<b>2. Şoför Krizi ve %55 Operasyonel Yük (OPEX)</b><br/>"
                      "Şehir içi taksi, servis ve kargo filolarının toplam işletme maliyetinin %45-55'ini şoför maaşları, vardiya primleri ve sosyal haklar oluşturmaktadır. Avrupa ve Körfez bölgesinde artan şoför bulma zorluğu hizmet kapasitesini sınırlandırmakta, insan yorgunluğuna bağlı kazalar sigorta primlerini katlamaktadır.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Gece ve Vardiya Dışı %70 Atıl Kapasite</b><br/>"
                      "Geleneksel filolardaki araçlar günün sadece 8-10 saati aktif çalışabilmekte, kalan 14-16 saat boyunca park alanlarında yatarak sermaye kaybına yol açmaktadır. Sürücüsüz sistemler ise 7/24 kesintisiz çalışarak aynı araç havuzundan 3 kat daha fazla gelir üretir.", styles['TableCell']),
            Paragraph("<b>4. Kapalı Kutusal Yapay Zeka Riskleri</b><br/>"
                      "Uçtan uca (End-to-End) eğitilen derin sinir ağları, eğitim verisinde olmayan bir durumla (edge-case) karşılaştığında tahmin edilemez ve ölümcül hatalar yapmaktadır. Regülasyon kurumları matematiksel ispatı ve formal emniyet garantisi olmayan kara kutu sistemlere ticari ruhsat vermemektedir.", styles['TableCell'])
        ]
    ]
    t_prob = Table(prob_box, colWidths=[89*mm, 93*mm])
    t_prob.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_prob)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>PAZAR BÜYÜKLÜĞÜ VE KÜRESEL VİZYON (TAM / SAM / SOM)</b>", styles['H2']))
    market_data = [
        [Paragraph("Pazar Katmanı", styles['TableHead']), Paragraph("2030 Projeksiyonu", styles['TableHead']), Paragraph("Açıklama ve Kapsam", styles['TableHead'])],
        [Paragraph("<b>TAM (Toplam Adreslenebilir Pazar)</b>", styles['TableCellBold']), Paragraph("<b>118 Milyar USD</b>", styles['TableCellBold']), Paragraph("Küresel otonom araç, robotaksi ve tak-çalıştır retrofit dönüşüm pazarı.", styles['TableCell'])],
        [Paragraph("<b>SAM (Hizmet Verilebilir Pazar)</b>", styles['TableCellBold']), Paragraph("<b>14.5 Milyar USD</b>", styles['TableCellBold']), Paragraph("BAE / Körfez (GCC), Türkiye ve Doğu Avrupa filo dönüşüm ve kamu seyrüsefer pazarı.", styles['TableCell'])],
        [Paragraph("<b>SOM (Hedeflenen İlk Pazar)</b>", styles['TableCellBold']), Paragraph("<b>120 Milyon USD</b>", styles['TableCellBold']), Paragraph("İlk 3 yılda Türkiye ve Dubai'de dönüştürülecek 3.500 araçlık binek, askeri ve tarım kiti.", styles['TableCell'])],
    ]
    t_m = Table(market_data, colWidths=[55*mm, 40*mm, 87*mm])
    t_m.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_m)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DUBAİ 2030 RESMİ SÜRÜCÜSÜZ ULAŞIM KANUNU</b>", styles['H2']))
    story.append(Paragraph(
        "Dubai Yollar ve Ulaşım Otoritesi (RTA Dubai), 2030 yılına kadar Dubai'deki tüm toplu ve bireysel ulaşım seyahatlerinin <b>en az %25'inin sürücüsüz (otonom) araçlarla yapılmasını</b> yasa ile zorunlu kılmıştır. "
        "Trustia AI; bu küresel dönüşümün resmi yarışması olan <b>1.200.000$ (1.2M$) nakit ödüllü Dubai World Challenge for Self-Driving Transport</b> programına başvurmuş ve başvuru resmi olarak onaylanmıştır. "
        "Kasım 2026'da açıklanacak finalistler arasında yer alarak Körfez operasyonunu başlatacaktır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 3: ÇÖZÜM VİZYONU — MODÜLER RETROFİT DÖNÜŞÜM KİTİ
    story.append(Paragraph("2. TRUSTIA ÇÖZÜMÜ: MODÜLER RETROFIT DÖNÜŞÜM KİTİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; sıfırdan otomobil üretme yanılgısına düşmeyip, dünyada milyonlarca üretilen seri üretim elektrikli araçları "
        "(öncelikle Hyundai Ioniq 5 E-GMP) <b>48 saat içinde tak-çalıştır donanım ve yazılım kitiyle SAE Seviye-4 otonom araca</b> dönüştürür.",
        styles['Body']
    ))

    sol_grid = [
        [
            Paragraph("<b>A. Non-Invasive (Zararsız) Mekanik Montaj</b><br/>"
                      "Aracın tavan sacı, şasisi veya orijinal gövde panelleri asla delinmez. Thule WingBar Edge tavan barlarına sabitlenen CNC 6061 havacılık sınıfı alüminyum pod kullanılır. Kablolar bagaj fitilinden geçirilir; aracın fabrika garantisi ve ikinci el değeri korunur.", styles['TableCell']),
            Paragraph("<b>B. Kvaser U100 CAN-FD Drive-by-Wire Köprüsü</b><br/>"
                      "Aracın fren ve direksiyon mekanizmasına harici motor veya hidrolik piston takılmaz. Ön dikiz aynası arkasındaki ADAS kamerasına bağlanan özel Y-harness ile Kvaser U100 CAN-FD köprüsü üzerinden doğrudan dijital komutlar enjekte edilir.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. 35.000$ Dönüşüm Kiti ile %70 Maliyet Avantajı</b><br/>"
                      "Waymo'nun 300.000$'lık özel aracına karşılık; Trustia 35.000$'lık kit maliyetiyle aynı Seviye-4 otonom yeteneği sunar. Filo sahibi mevcut araçlarını sisteme dahil edebilir; devasa sermaye riski ortadan kalkar.", styles['TableCell']),
            Paragraph("<b>D. 14 Ayda Amortisman ve Filo Kârlılığı</b><br/>"
                      "Dönüştürülen her araç, sürücü maaşı tasarrufu ve 7/24 gece çalışma avantajıyla yılda 55.500$ net tasarruf ve ek gelir sağlar. Sistem sadece 14 ay içinde tüm yatırım maliyetini geri öder.", styles['TableCell'])
        ]
    ]
    t_sol = Table(sol_grid, colWidths=[89*mm, 93*mm])
    t_sol.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sol)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>NEDEN HYUNDAI IONIQ 5 (E-GMP PLATFORMU)?</b>", styles['H2']))
    story.append(Paragraph(
        "• <b>800V Ultra Hızlı Şarj Mimarisi:</b> %10'dan %80 batarya doluluğuna sadece 18 dakikada ulaşır. Filo araçları şarjda beklemez.<br/>"
        "• <b>Açık CAN-FD Ağı:</b> Hyundai E-GMP mimarisi, yüksek hızlı CAN-FD haberleşme protokolünü destekleyerek 5 Mbps veri iletimine olanak tanır.<br/>"
        "• <b>Düz Zemin Kabin Ferahlığı:</b> Şaft tüneli olmayan düz zemin yapısı, robotaksi yolcuları için VIP yaşam alanı ve geniş bagaj hacmi sunar.<br/>"
        "• <b>Küresel Parça ve Servis Ağı:</b> Hyundai'nin küresel bayi ve servis ağı sayesinde dünyanın her yerinde kolay yedek parça temini sağlanır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 2: ÇOK SEKTÖRLÜ UYGULAMA ALANLARI
    # =========================================================================

    # SAYFA 4: SEKTÖR 1 — SİVİL OTONOM ROBOTAKSİ & BİNEK MOBİLİTE
    story.append(Paragraph("3. SEKTÖR 1: SİVİL OTONOM ROBOTAKSİ & BİNEK MOBİLİTE", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; şehir içi yolcu taşımacılığında güvenli, konforlu ve 7/24 kesintisiz sürücüsüz robotaksi operasyonu sağlar:",
        styles['Body']
    ))

    taxi_features = [
        [
            Paragraph("<b>A. Dinamik Şehir İçi A-to-B Seyrüsefer</b><br/>"
                      "Yoğun kentsel trafikte, döner kavşaklarda, yayalarla dolu okul bölgelerinde ve kontrolsüz kavşaklarda milisaniyelik dinamik rota planlama. "
                      "Trafik ışıklarını Sony IMX390 HDR kameralarla titreme olmadan algılar; şerit değişimlerini güvenle tamamlar.", styles['TableCell']),
            Paragraph("<b>B. Otonom Vale Park (AVP - Valet Parking)</b><br/>"
                      "Yolcu AVM, havalimanı veya kampüs kapısında araçtan iner. Araç tek bir mobil tuşla katlı otoparka gider, boş park yerini LiDAR ile tespit eder "
                      "ve milimetrik hassasiyetle geri geri park eder. Yolcu çağırdığında kapıya geri gelir.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. Gece Otomatik Şarj ve Servis İstasyonu</b><br/>"
                      "Yolcu talebinin azaldığı gece saat 02:00 - 05:00 arasında araç filosu kendi kendine en yakın hızlı şarj istasyonuna veya filo bakım merkezine gider. "
                      "Kablosuz veya otomatik şarj soketine yanaşarak bataryasını doldurur ve sabah 06:00'da tam şarjla servise başlar.", styles['TableCell']),
            Paragraph("<b>D. Mobil Yolcu Deneyimi & Filo Telemetrisi</b><br/>"
                      "Yolcu bindiğinde 12.3 inç kokpit ekranından rotayı görür, müzik/klima ayarlarını yapar, acil durdurma butonuna erişebilir. "
                      "Merkezdeki Trustia Filo Yönetim İstasyonu (Fleet C2) 5G üzerinden her aracın canlı telemetrisini, LiDAR nokta bulutunu ve bataryasını izler.", styles['TableCell'])
        ]
    ]
    t_taxi = Table(taxi_features, colWidths=[89*mm, 93*mm])
    t_taxi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_taxi)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>ROBOTAKSİ FİLO EKONOMİSİ KARŞILAŞTIRMASI</b>", styles['H2']))
    taxi_econ_table = [
        [Paragraph("Operasyon Parametresi", styles['TableHead']), Paragraph("Geleneksel İnsanlı Taksi", styles['TableHead']), Paragraph("Trustia Seviye-4 Robotaksi", styles['TableHead']), Paragraph("Yıllık Fark & Avantaj", styles['TableHead'])],
        [Paragraph("Günlük Aktif Çalışma Saati", styles['TableCellBold']), Paragraph("8 - 10 Saat (Tek Şoför)", styles['TableCell']), Paragraph("<b>22 - 24 Saat (Kesintisiz)</b>", styles['TableCellBold']), Paragraph("+14 Saat Ekstra Gelir", styles['BadgeGreen'])],
        [Paragraph("Aylık Şoför Maaşı & SGK Maliyeti", styles['TableCellBold']), Paragraph("3.000 $ (Yıllık 36.000 $)", styles['TableCell']), Paragraph("<b>0 $ (Şoförsüz)</b>", styles['TableCellBold']), Paragraph("<b>36.000 $ Net Tasarruf</b>", styles['BadgeGreen'])],
        [Paragraph("Trafik Kazası ve Sigorta Primi", styles['TableCellBold']), Paragraph("Yüksek (İnsan hatası riski)", styles['TableCell']), Paragraph("<b>Düşük (%80 İndirimli)</b>", styles['TableCellBold']), Paragraph("4.500 $ Tasarruf", styles['BadgeGreen'])],
        [Paragraph("Yıllık Net Filo Kârı (Araç Başı)", styles['TableCellBold']), Paragraph("12.000 $", styles['TableCell']), Paragraph("<b>67.500 $</b>", styles['TableCellBold']), Paragraph("<b>+55.500 $ Net Fazla Kâr</b>", styles['BadgeGreen'])],
    ]
    t_te = Table(taxi_econ_table, colWidths=[52*mm, 42*mm, 44*mm, 44*mm])
    t_te.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_te)
    story.append(PageBreak())

    # SAYFA 5: SEKTÖR 2 — SAVUNMA SANAYİİ & ASKERİ İKA ÇÖZÜMLERİ
    story.append(Paragraph("4. SEKTÖR 2: SAVUNMA SANAYİİ & ASKERİ İKA ÇÖZÜMLERİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_DEFENSE, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia'nın deterministik seyrüsefer çekirdeği; GPS karartması, elektronik harp ve zorlu arazi koşullarında "
        "<b>T.C. Savunma Sanayii Başkanlığı 100/100 Tam Puan tescilli</b> askeri taktik otonomi sunar:",
        styles['Body']
    ))

    def_features = [
        [
            Paragraph("<b>A. GPS Karartmasında 3D LiDAR SLAM Seyrüsefer</b><br/>"
                      "Muharebe sahasında düşman elektronik harp karıştırıcıları (Jammer) GPS sinyallerini tamamen kesse dahi araç rotasından sapmaz. "
                      "3D NDT LiDAR SLAM harita eşleme ve 400Hz ESKF INS filtresi ile haritasız arazide <b>5cm hassasiyetle</b> görev icra eder.", styles['TableCell']),
            Paragraph("<b>B. Derin Öğrenmeli EYP ve Kara Mayını Tespiti</b><br/>"
                      "FLIR Termal kamera ve Sony IMX390 HDR kameralardan gelen verileri işleyen özgün sinir ağı; yol üzerine gömülü el yapımı patlayıcıları (EYP), "
                      "tuzaklı kabloları ve tanksavar mayınlarını 50 metre mesafeden tespit ederek aracı güvenli mesafede durdurur.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. Taktik Askeri C2 Yer Kontrol Konsolu</b><br/>"
                      "Trustia Taktik C2 Konsolu; MGRS askeri koordinatları, şifreli taktik telsiz veri linki (Mesh RF) ve NATO standartlarında semboloji içerir. "
                      "Operatör tek bir merkezden 10 adede kadar otonom İKA'yı harita üzerinden görevlendirebilir, konvoy takip emri verebilir.", styles['TableCell']),
            Paragraph("<b>D. Otonom İntikal ve Lojistik Konvoy Takibi</b><br/>"
                      "Lider aracın tekerlek izlerini takip eden dinamik Pure Pursuit sanal çeki demiri algoritması sayesinde; "
                      "öncü insanlı aracı arkasından 5 adet sürücüsüz lojistik kamyonu tozda, siste ve gece sıfır ışıkta milimetrik takip eder.", styles['TableCell'])
        ]
    ]
    t_def = Table(def_features, colWidths=[89*mm, 93*mm])
    t_def.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_DEFENSE),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_def)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>SAVUNMA SANAYİİ RESMİ TESCİLLERİ VE ENTEGRASYON STATÜSÜ</b>", styles['H2']))
    story.append(Paragraph(
        "• <b>T.C. SSB Yetenek Envanteri:</b> Savunma Sanayii Başkanlığı resmi değerlendirmesinde <b>100/100 Tam Puan</b> (Belge No: <b>L2zPtN4X1ZJ</b>).<br/>"
        "• <b>ASELSAN Tedarikçi Portalı:</b> ASELSAN onaylı girişim statüsü ile askeri araç üreticilerine (FNSS, Otokar, Katmerciler, BMC) tak-çalıştır otonomi kiti sağlama yetkisi.<br/>"
        "• <b>MIL-STD-810H & IP67:</b> Çöl sıcağı, aşırı soğuk (-20°C / +55°C), yüksek titreşim ve toz fırtınasına dayanıklı askeri donanım paketi.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 6: SEKTÖR 3 — OTONOM TARIM & ENDÜSTRİYEL LOJİSTİK KİTİ
    story.append(Paragraph("5. SEKTÖR 3: OTONOM TARIM & ENDÜSTRİYEL LOJİSTİK", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_AGRI, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia otonomi kiti; tarım arazilerinde traktör ve biçerdöverleri, endüstriyel tesislerde ise ağır yük çekicilerini "
        "48 saatte sürücüsüz hale getirerek verimlilik devrimi yaratır:",
        styles['Body']
    ))

    agri_features = [
        [
            Paragraph("<b>A. Otonom Traktör & Biçerdöver Dönüşüm Kiti</b><br/>"
                      "Çiftçilerin mevcut traktörlerine (New Holland, Massey Ferguson, John Deere vb.) hidrolik direksiyon kontrol valfi ve Kvaser CAN arayüzü ile entegre edilir. "
                      "Sıfırdan otonom traktör almaya gerek kalmadan mevcut makineleri Seviye-4 otonom robota dönüştürür.", styles['TableCell']),
            Paragraph("<b>B. 7/24 Gece Boyu Kesintisiz Ekim ve Hasat</b><br/>"
                      "Gündüz aşırı sıcakta veya tozda insan çalışamazken; Trustia donanımlı traktör Ouster LiDAR ve termal kameralarla zifiri karanlıkta tarlayı santimetre hassasiyetle sürer. "
                      "Traktörün atıl beklemesini engeller; ekim ve hasat süresini %60 kısaltır.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. %40 Yakıt, Gübre ve Tohum Tasarrufu</b><br/>"
                      "Hybrid A* tarla rota motoru; traktörün tarla başında dönüşlerini (headland turn) ve sıra aralarını 2cm doğrulukla planlar. "
                      "Üst üste bindirmeleri (overlap) sıfırlayarak tohum, ilaç, gübre ve yakıt sarfiyatında %35-40 net tasarruf sağlar.", styles['TableCell']),
            Paragraph("<b>D. Liman ve Fabrika İçi Ağır Yük Konteyner Çekicisi</b><br/>"
                      "Konteyner limanlarında ve büyük lojistik depolarında dorseleri ve konteynerleri vinç altına taşıyan ağır çekicileri otonomlaştırır. "
                      "Kapalı tesis içi haritada 7/24 kesintisiz yük transferi yapar; liman operasyon maliyetlerini yarı yarıya düşürür.", styles['TableCell'])
        ]
    ]
    t_agri = Table(agri_features, colWidths=[89*mm, 93*mm])
    t_agri.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_AGRI),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_agri)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>TARIM VE ENDÜSTRİYEL KİTİN EKONOMİK ETKİSİ</b>", styles['H2']))
    story.append(Paragraph(
        "Geniş ölçekli 1.000 dönümlük bir tarım işletmesinde; operatör yorgunluğu ve gece çalışamama yılda ortalama 45.000$ verim kaybına yol açar. "
        "Trustia Tarım Kiti (18.500$ kit maliyeti), ilk hasat sezonunda (6 ay içinde) yakıt ve işçilik tasarrufuyla kendi maliyetini tamamen amorti eder.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 3: DONANIM, SENSÖR VE ARAÇ ENTEGRASYONU
    # =========================================================================

    # SAYFA 7: HYUNDAI IONIQ 5 TEST ARACI — DIŞ SENSÖR GÖRSEL GALERİSİ
    story.append(Paragraph("6. HYUNDAI IONIQ 5 TEST ARACI: DIŞ SENSÖR ENTEGRASYONU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    if os.path.exists(f1) and os.path.exists(f3):
        im1 = RLImage(f1, width=89*mm, height=58*mm)
        im3 = RLImage(f3, width=89*mm, height=58*mm)
        t_imgs1 = Table([[im1, im3]], colWidths=[91*mm, 91*mm])
        t_imgs1.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('PADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(t_imgs1)
        story.append(Spacer(1, 3))

    story.append(Paragraph("<i>Şekil 1: Hyundai Ioniq 5 Seviye-4 Test Aracı — Çatı Ouster LiDAR Podu ve Yan Profil Sensör Geometrisi</i>", styles['Caption']))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>AERODİNAMİK TAVAN PODU VE 360° SENSÖR GEOMETRİSİ</b>", styles['H2']))
    story.append(Paragraph(
        "Trustia'nın tavan sensör podu, havacılık sınıfı 6061-T6 alüminyum bloktan 5 eksenli CNC tezgahlarda işlenmiştir. "
        "Ouster OS2-128 LiDAR'ı yerden 1.78 metre yüksekliğe konumlandırarak aracın kör noktalarını en aza indirir. "
        "Çift Septentrio GNSS anteni arasındaki 1.10 metrelik baz hattı (baseline), aracın durağan haldeyken dahi 0.1 derece doğrulukla "
        "pusula yönelimini (heading) hesaplamasını sağlar. "
        "Gövde tasarımı rüzgar tüneli simülasyonlarıyla optimize edilmiş olup, 130 km/s otoyol hızlarında araç menzilini sadece %1.8 etkiler.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 8: HYUNDAI IONIQ 5 TEST ARACI — TAMPON VE GÖVDE GÖRSEL GALERİSİ
    story.append(Paragraph("7. HYUNDAI IONIQ 5 TEST ARACI: TAMPON VE GÖVDE ENTEGRASYONU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    if os.path.exists(f2) and os.path.exists(f4):
        im2 = RLImage(f2, width=89*mm, height=58*mm)
        im4 = RLImage(f4, width=89*mm, height=58*mm)
        t_imgs2 = Table([[im2, im4]], colWidths=[91*mm, 91*mm])
        t_imgs2.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('PADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(t_imgs2)
        story.append(Spacer(1, 3))

    story.append(Paragraph("<i>Şekil 2: Hyundai Ioniq 5 Seviye-4 Test Aracı — Ön Tampon LiDAR/Radar Izgarası ve Arka Çapraz Gövde Entegrasyonu</i>", styles['Caption']))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>ÖN TAMPON VE ARKA KÖR NOKTA MÜHENDİSLİĞİ</b>", styles['H2']))
    story.append(Paragraph(
        "Ön tamponda plaka altına monte edilen Continental ARS 408-21 radar braketi, aktif hava panjuru kanatlarının hareketini engellemez. "
        "Sağ ve sol sis farı yuvalarına açılandırılan Livox Mid-360 LiDAR'lar; aracın ön burnundan itibaren 0-3 metredeki yayaları, evcil hayvanları "
        "ve bordür taşlarını eksiksiz yakalar. "
        "Arka tamponda konumlanan ikinci Continental radar ise geri manevralarda ve otoyolda arkadan 180 km/s hızla yaklaşan araçları 250 metreden tespit eder.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 9: HYUNDAI IONIQ 5 TEST ARACI — KOKPİT, KONSOL VE ARKA KABİN
    story.append(Paragraph("8. HYUNDAI IONIQ 5 TEST ARACI: KOKPİT VE YOLCU YAŞAM ALANI", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    if os.path.exists(f6) and os.path.exists(f7):
        im6 = RLImage(f6, width=89*mm, height=58*mm)
        im7 = RLImage(f7, width=89*mm, height=58*mm)
        t_imgs3 = Table([[im6, im7]], colWidths=[91*mm, 91*mm])
        t_imgs3.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('PADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(t_imgs3)
        story.append(Spacer(1, 3))

    story.append(Paragraph("<i>Şekil 3: Hyundai Ioniq 5 Seviye-4 Test Aracı — Kokpit C2 Telemetri Ekranı ve Arka Yolcu Yaşam Alanı</i>", styles['Caption']))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>KOKPİT TELEMETRİSİ VE VIP YOLCU KONFORU</b>", styles['H2']))
    story.append(Paragraph(
        "Kokpitteki 12.3 inç dokunmatik konsol, Trustia'nın gerçek zamanlı otonomi durumunu görüntüler: "
        "Hybrid A* planlanan rota çizgisi, 3D LiDAR nokta bulutu, tespit edilen nesnelerin hız vektörleri ve acil durum emniyet kalkanı. "
        "Arka kabindeki yolcular için geniş E-GMP düz zemin ferahlığı ve bağımsız USB-C/220V V2L güç çıkışları sunulmaktadır. "
        "Yolcular mobil uygulama veya arka koltuk ekranı üzerinden rotayı onaylayabilir, acil durdurma butonuna basabilir veya tele-operatör ile canlı sesli görüşme başlatabilir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 10: SENSÖR PAKETİ DERİNLEMESİNE SPESİFİKASYONLARI
    story.append(Paragraph("9. SENSÖR PAKETİ DERİNLEMESİNE SPESİFİKASYONLARI", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; her türlü hava koşulunda sıfır hata toleransıyla çalışan, otomotiv sınıfı 5 farklı sensör modalitesini füzyonlar:",
        styles['Body']
    ))

    hw_table_data = [
        [Paragraph("Alt Sistem", styles['TableHead']), Paragraph("Bileşen & Model", styles['TableHead']), Paragraph("Temel Teknik Özellikler", styles['TableHead']), Paragraph("Otonomi Görevi & Fonksiyonu", styles['TableHead'])],
        [Paragraph("<b>Çatı 3D LiDAR</b>", styles['TableCellBold']), Paragraph("Ouster OS2-128 Rev 7", styles['TableCell']), Paragraph("128 Lazer Kanalı, 240m Menzil, 2.62M Pts/s, 360°x45° FOV, 10/20Hz", styles['TableCell']), Paragraph("360° birincil çevre haritalama, 3D NDT SLAM ve uzak engel tespiti.", styles['TableCell'])],
        [Paragraph("<b>Kör Nokta LiDAR (2x)</b>", styles['TableCellBold']), Paragraph("Livox Mid-360", styles['TableCell']), Paragraph("360°x59° Ultra Geniş FOV, 0.1-40m Menzil, 200k Pts/s, 905nm", styles['TableCell']), Paragraph("Ön ve arka tamponda yaya, bordür, çukur ve yakın cisim sıfır kör nokta takibi.", styles['TableCell'])],
        [Paragraph("<b>Uzun Menzil Radar (2x)</b>", styles['TableCellBold']), Paragraph("Continental ARS 408-21", styles['TableCell']), Paragraph("77GHz FMCW, 250m Menzil, Hız: ±400 km/s, Açı: ±60°, 17Hz", styles['TableCell']), Paragraph("Yoğun sis, kum fırtınası, şiddetli yağmurda öndeki araç hız ve mesafe takibi.", styles['TableCell'])],
        [Paragraph("<b>Görsel Kameralar (4x)</b>", styles['TableCellBold']), Paragraph("Sony IMX390 HDR GMSL2", styles['TableCell']), Paragraph("1920x1080 @ 60fps, 120dB HDR, LED Flicker Mitigation, IP69K", styles['TableCell']), Paragraph("Trafik ışığı, şerit çizgileri, yol levhaları ve yaya niyet analizi.", styles['TableCell'])],
        [Paragraph("<b>RTK GNSS & IMU</b>", styles['TableCellBold']), Paragraph("Septentrio AsteRx-m3 Pro", styles['TableCell']), Paragraph("Üç Frekans RTK (GPS/GLO/GAL/BDS), 400Hz Endüstriyel IMU, 1cm Hata", styles['TableCell']), Paragraph("Küresel harita üzerinde santimetre hassasiyetinde mutlak konum ve yönelim.", styles['TableCell'])],
    ]
    t_hw = Table(hw_table_data, colWidths=[35*mm, 45*mm, 52*mm, 50*mm])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_hw)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DONANIM ENTEGRASYONUNDA YEDEKLİLİK (REDUNDANCY)</b>", styles['H2']))
    story.append(Paragraph(
        "Kamera kör olsa dahi LiDAR nokta bulutu devrededir; LiDAR siste dağılsa dahi Continental FMCW radarı nesneyi delip geçer. "
        "Üç farklı fiziksel algılama prensibi (Işık, Lazer, Radyo Dalgaları) aynı anda birleşerek ASIL-D emniyet tavanı oluşturur.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 11: A'DAN Z'YE 27 PARÇALIK TAM DONANIM BOM LİSTESİ
    story.append(Paragraph("10. A'DAN Z'YE 27 PARÇALIK TAM DONANIM BOM LİSTESİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia Seviye-4 Dönüşüm Kiti'nin fabrika çıkışlı, doğrulanmış 27 bileşenlik malzeme ve maliyet dökümü (Bill of Materials):",
        styles['Body']
    ))

    bom_detailed = [
        [Paragraph("No", styles['TableHead']), Paragraph("Bileşen Adı & Model", styles['TableHead']), Paragraph("Kategori", styles['TableHead']), Paragraph("Adet", styles['TableHead']), Paragraph("Birim (USD)", styles['TableHead']), Paragraph("Toplam (USD)", styles['TableHead']), Paragraph("Tedarikçi", styles['TableHead'])],
        [Paragraph("1", styles['TableCell']), Paragraph("Ouster OS2-128 Rev 7 LiDAR", styles['TableCellBold']), Paragraph("Algılama", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("14.500 $", styles['TableCell']), Paragraph("14.500 $", styles['TableCell']), Paragraph("Ouster Inc. (ABD)", styles['TableCell'])],
        [Paragraph("2", styles['TableCell']), Paragraph("Livox Mid-360 LiDAR", styles['TableCellBold']), Paragraph("Algılama", styles['TableCell']), Paragraph("2", styles['TableCell']), Paragraph("1.850 $", styles['TableCell']), Paragraph("3.700 $", styles['TableCell']), Paragraph("Livox (Asya)", styles['TableCell'])],
        [Paragraph("3", styles['TableCell']), Paragraph("Continental ARS 408-21 Radar", styles['TableCellBold']), Paragraph("Algılama", styles['TableCell']), Paragraph("2", styles['TableCell']), Paragraph("1.600 $", styles['TableCell']), Paragraph("3.200 $", styles['TableCell']), Paragraph("Continental (Almanya)", styles['TableCell'])],
        [Paragraph("4", styles['TableCell']), Paragraph("Sony IMX390 GMSL2 Kamera", styles['TableCellBold']), Paragraph("Algılama", styles['TableCell']), Paragraph("4", styles['TableCell']), Paragraph("550 $", styles['TableCell']), Paragraph("2.200 $", styles['TableCell']), Paragraph("Leopard Imaging", styles['TableCell'])],
        [Paragraph("5", styles['TableCell']), Paragraph("Septentrio AsteRx-m3 Pro GNSS/INS", styles['TableCellBold']), Paragraph("Konum", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("2.800 $", styles['TableCell']), Paragraph("2.800 $", styles['TableCell']), Paragraph("Septentrio (Belçika)", styles['TableCell'])],
        [Paragraph("6", styles['TableCell']), Paragraph("NVIDIA Jetson AGX Orin 64GB", styles['TableCellBold']), Paragraph("Hesaplama", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("2.990 $", styles['TableCell']), Paragraph("2.990 $", styles['TableCell']), Paragraph("NVIDIA (ABD)", styles['TableCell'])],
        [Paragraph("7", styles['TableCell']), Paragraph("Seeed Studio J501 Taşıyıcı Kart", styles['TableCellBold']), Paragraph("Hesaplama", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("850 $", styles['TableCell']), Paragraph("850 $", styles['TableCell']), Paragraph("Seeed Studio", styles['TableCell'])],
        [Paragraph("8", styles['TableCell']), Paragraph("Kvaser U100 CAN-FD Köprüsü", styles['TableCellBold']), Paragraph("DBW Arayüz", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("760 $", styles['TableCell']), Paragraph("760 $", styles['TableCell']), Paragraph("Kvaser (İsveç)", styles['TableCell'])],
        [Paragraph("9", styles['TableCell']), Paragraph("Teltonika RUTX50 5G/V2X Modem", styles['TableCellBold']), Paragraph("Haberleşme", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("650 $", styles['TableCell']), Paragraph("650 $", styles['TableCell']), Paragraph("Teltonika (Litvanya)", styles['TableCell'])],
        [Paragraph("10", styles['TableCell']), Paragraph("Netgear 5-Port Gigabit End. Switch", styles['TableCellBold']), Paragraph("Ağ", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("150 $", styles['TableCell']), Paragraph("150 $", styles['TableCell']), Paragraph("Netgear", styles['TableCell'])],
        [Paragraph("11", styles['TableCell']), Paragraph("Thule WingBar Edge Tavan Barları", styles['TableCellBold']), Paragraph("Mekanik", styles['TableCell']), Paragraph("1 Tk", styles['TableCell']), Paragraph("420 $", styles['TableCell']), Paragraph("420 $", styles['TableCell']), Paragraph("Thule (İsveç)", styles['TableCell'])],
        [Paragraph("12", styles['TableCell']), Paragraph("CNC 6061 Tavan Sensör Podu", styles['TableCellBold']), Paragraph("Mekanik", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("1.450 $", styles['TableCell']), Paragraph("1.450 $", styles['TableCell']), Paragraph("Yerli İmalat (TR)", styles['TableCell'])],
        [Paragraph("13", styles['TableCell']), Paragraph("Ön/Arka Tampon Braketleri (CNC)", styles['TableCellBold']), Paragraph("Mekanik", styles['TableCell']), Paragraph("1 Tk", styles['TableCell']), Paragraph("680 $", styles['TableCell']), Paragraph("680 $", styles['TableCell']), Paragraph("Yerli İmalat (TR)", styles['TableCell'])],
        [Paragraph("14", styles['TableCell']), Paragraph("Siegen 300A Acil Durdurma Şalteri", styles['TableCellBold']), Paragraph("Güç", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("180 $", styles['TableCell']), Paragraph("180 $", styles['TableCell']), Paragraph("Siegen (Almanya)", styles['TableCell'])],
        [Paragraph("15", styles['TableCell']), Paragraph("Mean Well 12V/24V End. Regülatör", styles['TableCellBold']), Paragraph("Güç", styles['TableCell']), Paragraph("1", styles['TableCell']), Paragraph("220 $", styles['TableCell']), Paragraph("220 $", styles['TableCell']), Paragraph("Mean Well", styles['TableCell'])],
        [Paragraph("16", styles['TableCell']), Paragraph("Interkom 12'li Sigorta Bloğu & Röle", styles['TableCellBold']), Paragraph("Güç", styles['TableCell']), Paragraph("1 Tk", styles['TableCell']), Paragraph("150 $", styles['TableCell']), Paragraph("150 $", styles['TableCell']), Paragraph("Interkom", styles['TableCell'])],
        [Paragraph("17-27", styles['TableCell']), Paragraph("Otomotiv Kablo Demeti, Soketler & V2L", styles['TableCellBold']), Paragraph("Kablolama", styles['TableCell']), Paragraph("1 Tk", styles['TableCell']), Paragraph("700 $", styles['TableCell']), Paragraph("700 $", styles['TableCell']), Paragraph("TE Connectivity / TR", styles['TableCell'])],
        [Paragraph("—", styles['TableCellBold']), Paragraph("<b>TOPLAM DONANIM MALİYETİ (BOM)</b>", styles['TableCellBold']), Paragraph("<b>HER ŞEY DAHİL</b>", styles['TableCellBold']), Paragraph("<b>27</b>", styles['TableCellBold']), Paragraph("—", styles['TableCellBold']), Paragraph("<b>32.800 $</b>", styles['TableCellBold']), Paragraph("<b>Anahtar Teslim</b>", styles['TableCellBold'])],
    ]
    t_bom = Table(bom_detailed, colWidths=[10*mm, 52*mm, 24*mm, 14*mm, 24*mm, 26*mm, 32*mm])
    t_bom.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_bom)
    story.append(PageBreak())

    # SAYFA 12: ELEKTRİK VE GÜÇ DAĞITIM MİMARİSİ
    story.append(Paragraph("11. ELEKTRİK, GÜÇ DAĞITIMI VE ASIL-D İZOLASYON MİMARİSİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Otonom araç dönüşümünde en kritik konu aracın yangın ve elektriksel arıza güvenliğidir. "
        "Trustia; OEM elektrik mimarisine müdahale etmeyen <b>tam izoleli ikinci bir güç katmanı</b> kurar:",
        styles['Body']
    ))

    pwr_boxes = [
        [
            Paragraph("<b>1. LDC & 12V Akü Besleme Noktası</b><br/>"
                      "Hyundai Ioniq 5'in ana 800V bataryasından düşük voltaja güç aktaran LDC (Low DC-DC Converter) ünitesi 12V 100A besleme sağlar. "
                      "Trustia donanımları bu 12V yardımcı akü kutup başından 4 AWG saf bakır silikon yanmaz kablo ile beslenir. "
                      "Yüksek voltaj çekiş bataryasına kesinlikle dokunulmaz.", styles['TableCell']),
            Paragraph("<b>2. Siegen 300A Manuel Kesici Şalter</b><br/>"
                      "Bagaj altında ve sürücü kokpitinde iki adet erişilebilir konumda Siegen 300A acil durum ana güç kesici şalteri bulunur. "
                      "Herhangi bir olağandışı durumda tek bir mekanik hareketle otonom sistemin tüm elektriği 10 milisaniyede sıfırlanır.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Mean Well Endüstriyel Regülasyon</b><br/>"
                      "Araç içindeki dinamik akım dalgalanmaları (klima, ısıtıcı, cam motorları) otonomi bilgisayarını etkilemesin diye "
                      "Mean Well DC-DC regülatörü kullanılır. Jetson Orin'e temiz 19V, LiDAR'lara 24V ve kameralara 12V stabil gerilim sağlanır.", styles['TableCell']),
            Paragraph("<b>4. Interkom 12'li LED İkazlı Sigorta Kutusu</b><br/>"
                      "Her bir sensör ve bileşen bağımsız otomotiv bıçak sigortasıyla korunur (Ouster LiDAR 7.5A, Jetson Orin 15A, Kvaser 2A, Kameralar 5A). "
                      "Atan sigorta üzerinde LED ışık yanarak hatayı saniyeler içinde gösterir; yangın riski %100 sıfırlanır.", styles['TableCell'])
        ]
    ]
    t_pwr = Table(pwr_boxes, colWidths=[89*mm, 93*mm])
    t_pwr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pwr)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>ELEKTRİKSEL GÜÇ TÜKETİM MATRİSİ</b>", styles['H2']))
    pwr_consumption_data = [
        [Paragraph("Bileşen Grubu", styles['TableHead']), Paragraph("Çalışma Voltajı", styles['TableHead']), Paragraph("Nominal Akım", styles['TableHead']), Paragraph("Nominal Güç (Watt)", styles['TableHead']), Paragraph("Tepe Güç (Peak Watt)", styles['TableHead'])],
        [Paragraph("NVIDIA Jetson Orin 64GB", styles['TableCellBold']), Paragraph("19V DC", styles['TableCell']), Paragraph("3.2 A", styles['TableCell']), Paragraph("60 W", styles['TableCell']), Paragraph("85 W", styles['TableCell'])],
        [Paragraph("Ouster OS2-128 LiDAR", styles['TableCellBold']), Paragraph("24V DC", styles['TableCell']), Paragraph("0.8 A", styles['TableCell']), Paragraph("20 W", styles['TableCell']), Paragraph("28 W", styles['TableCell'])],
        [Paragraph("2x Livox Mid-360 LiDAR", styles['TableCellBold']), Paragraph("12V DC", styles['TableCell']), Paragraph("1.6 A", styles['TableCell']), Paragraph("20 W", styles['TableCell']), Paragraph("30 W", styles['TableCell'])],
        [Paragraph("2x Continental Radar + 4x Kamera", styles['TableCellBold']), Paragraph("12V DC", styles['TableCell']), Paragraph("2.1 A", styles['TableCell']), Paragraph("25 W", styles['TableCell']), Paragraph("35 W", styles['TableCell'])],
        [Paragraph("Teltonika 5G + GNSS + Switch", styles['TableCellBold']), Paragraph("12V DC", styles['TableCell']), Paragraph("1.2 A", styles['TableCell']), Paragraph("15 W", styles['TableCell']), Paragraph("22 W", styles['TableCell'])],
        [Paragraph("<b>TOPLAM OTONOMİ GÜÇ YÜKÜ</b>", styles['TableCellBold']), Paragraph("<b>12V / 19V / 24V</b>", styles['TableCellBold']), Paragraph("<b>—</b>", styles['TableCellBold']), Paragraph("<b>140 Watt</b>", styles['TableCellBold']), Paragraph("<b>200 Watt</b>", styles['TableCellBold'])],
    ]
    t_pc = Table(pwr_consumption_data, colWidths=[52*mm, 32*mm, 30*mm, 34*mm, 34*mm])
    t_pc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_pc)
    story.append(PageBreak())

    # SAYFA 13: DRIVE-BY-WIRE (DBW) CAN-FD ENJEKSİYON MİMARİSİ
    story.append(Paragraph("12. DRIVE-BY-WIRE (DBW) CAN-FD ENJEKSİYON MİMARİSİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; aracın direksiyonuna, gazına ve frenine fiziksel motor eklemeden, "
        "fabrika çıkışı şasi kontrol ünitelerine <b>Kvaser U100 CAN-FD arayüzü</b> ile dijital komutlar enjekte eder:",
        styles['Body']
    ))

    can_flow_data = [
        [Paragraph("CAN Mesajı", styles['TableHead']), Paragraph("Bus Frekansı", styles['TableHead']), Paragraph("Enjekte Edilen Değişkenler", styles['TableHead']), Paragraph("Kontrol Edilen OEM Aktüatörü", styles['TableHead'])],
        [Paragraph("<b>LKAS11 (Direksiyon)</b>", styles['TableCellBold']), Paragraph("50 Hz (20 ms)", styles['TableCell']), Paragraph("Direksiyon torku, açı hedefi, aktiflik bayrağı, sayaç & CRC", styles['TableCell']), Paragraph("MDPS (Motor Driven Power Steering) Elektrikli Direksiyon Kolonu", styles['TableCell'])],
        [Paragraph("<b>SCC11 (Boylamsal)</b>", styles['TableCellBold']), Paragraph("50 Hz (20 ms)", styles['TableCell']), Paragraph("İvmelenme komutu (m/s²), hedef hız, frenleme basıncı", styles['TableCell']), Paragraph("ESC (Elektronik Stabilite Kontrolü) & Motor Çekiş İnvertörü", styles['TableCell'])],
        [Paragraph("<b>CLU11 (Gösterge)</b>", styles['TableCellBold']), Paragraph("20 Hz (50 ms)", styles['TableCell']), Paragraph("Araç hız geri bildirimi, menzil, kapı kilit durumları", styles['TableCell']), Paragraph("Merkezi Gösterge Paneli ve Telemetri Algılama", styles['TableCell'])],
        [Paragraph("<b>CGW1 (Ağ Geçidi)</b>", styles['TableCellBold']), Paragraph("100 Hz (10 ms)", styles['TableCell']), Paragraph("Tekerlek devir sensörleri (Wheel Speeds FL, FR, RL, RR)", styles['TableCell']), Paragraph("Tekerlek Odometrisi & 400Hz ESKF Kalman Konumlandırma", styles['TableCell'])],
    ]
    t_cf = Table(can_flow_data, colWidths=[40*mm, 32*mm, 60*mm, 50*mm])
    t_cf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cf)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>KVASER U100 GALVANİK İZOLASYON GÜVENCESİ</b>", styles['H2']))
    story.append(Paragraph(
        "Kvaser U100 CAN-FD adaptörü; araç şasi şebekesi ile Jetson Orin bilgisayarı arasında <b>5.000V galvanik izolasyon</b> sağlar. "
        "Bilgisayarda meydana gelebilecek herhangi bir kısa devre veya elektriksel gürültü asla aracın CAN hattına sıçramaz. "
        "Sistem saniyede 1.000 mesajlık sağlama toplamı (CRC) kontrolü yapar; tek bir hatalı pakette dahi komut derhal iptal edilir ve güvenli moda geçilir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 4: DERİN YAZILIM MİMARİSİ VE DETERMINİSTİK KOD
    # =========================================================================

    # SAYFA 14: 16.000 SATIR DETERMINİSTİK KOD VS KARA KUTU AI
    story.append(Paragraph("13. 16.000 SATIR DETERMINİSTİK KOD VE AÇIK GITHUB MİMARİSİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Otonom araç endüstrisinde son yıllarda yayılan 'Uçtan Uca Kara Kutu Yapay Zeka' (End-to-End Deep Learning) yaklaşımı, "
        "aracın neden viraj aldığını veya neden aniden fren yaptığını matematiksel olarak açıklayamaz. "
        "Trustia AI; havacılık ve uzay emniyet standartlarında <b>16.000 satırlık deterministik yazılım çekirdeği</b> ile çalışır:",
        styles['Body']
    ))

    det_vs_black = [
        [Paragraph("Mühendislik Kriteri", styles['TableHead']), Paragraph("Kara Kutu Yapay Zeka (End-to-End AI)", styles['TableHead']), Paragraph("Trustia Deterministik Mimarisi", styles['TableHead'])],
        [Paragraph("<b>Matematiksel İspatlanabilirlik</b>", styles['TableCellBold']), Paragraph("YOK (Ağırlık matrisleri tahmin edilemez)", styles['TableCell']), Paragraph("<b>TAM İSPAT (Kinematik ve Geometrik İspat)</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Beklenmedik Durum (Edge-Case)</b>", styles['TableCellBold']), Paragraph("Ölümcül halüsinasyon ve kararsızlık riski", styles['TableCell']), Paragraph("<b>Sınırları belirlenmiş MRM güvenli duruş</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Regülasyon ve ASIL-D Ruhsatı</b>", styles['TableCellBold']), Paragraph("Ruhsat alamaz (Açıklanamaz AI)", styles['TableCell']), Paragraph("<b>ISO 26262 ASIL-D uyumlu kod yapısı</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Gecikme ve Çözüm Süresi</b>", styles['TableCellBold']), Paragraph("Değişken (100ms - 500ms)", styles['TableCell']), Paragraph("<b>Sabit ve Deterministik (< 50 milisaniye)</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Doğrulanabilir Kod Deposu</b>", styles['TableCellBold']), Paragraph("Kapalı / Gizli proprietary kod", styles['TableCell']), Paragraph("<b>Açık GitHub Deposu (github.com/Trustia/Trustia)</b>", styles['BadgeGreen'])],
    ]
    t_dvb = Table(det_vs_black, colWidths=[45*mm, 68*mm, 69*mm])
    t_dvb.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_dvb)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>GITHUB RESMİ KOD DEPOSU DOĞRULAMASI</b>", styles['H2']))
    story.append(Paragraph(
        "Trustia AI; tüm algoritmik mantığını, ROS2 Humble düğümlerini ve sürücü katmanlarını denetlenebilir şekilde tutar:<br/>"
        "🔗 <b>GitHub Deposu:</b> <font color='#0284C7'><u>https://github.com/Trustia/Trustia</u></font><br/>"
        "Yatırımcılar ve teknik denetçiler, 16.000 satırlık temiz mimariyi, modüler Python/C++ kodlarını ve test koşucularını doğrudan inceleyebilir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 15: KİNEMATİK HYBRID A* ROTA PLANLAMA MOTORU
    story.append(Paragraph("14. KİNEMATİK HYBRID A* ROTA PLANLAMA MOTORU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Standart 2D A* algoritması bir aracın noktasal olduğunu varsayar; oysa bir otomobil yanlamasına hareket edemez (Non-holonomic). "
        "Trustia'nın özgün C++ <b>Hybrid A* motoru</b>, aracın fiziksel Ackermann kinematiğini 3D durum uzayında (x, y, θ) çözer:",
        styles['Body']
    ))

    ha_steps = [
        [
            Paragraph("<b>1. Sürekli Durum Genişlemesi (Continuous State Expansion)</b><br/>"
                      "Algoritma sadece ızgara karelerine atlamaz; aracın mevcut yöneliminden (θ) başlayarak maksimum direksiyon açısı kısıtı dahilinde "
                      "olası fiziksel yayları (trajectories) hesaplar. Böylece üretilen her rota araç tarafından fiziksel olarak sürülebilir.", styles['TableCell']),
            Paragraph("<b>2. Reed-Shepp Analitik Çözücü</b><br/>"
                      "Hedefe yaklaşıldığında Reed-Shepp eğrileri analitik olarak devreye girer. "
                      "Dar otoparklarda veya engelli sokaklarda ileri-geri manevraları (3-point turn) otomatik olarak hesaplayarak aracı hedefe milimetrik sokar.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Voronoi Alan Maliyet Fonksiyonu</b><br/>"
                      "Rota sadece engellere çarpmamakla kalmaz; Voronoi diyagramları sayesinde binalardan, kaldırım taşlarından ve diğer araçlardan "
                      "maksimum emniyetli mesafeyi (güvenlik koridoru) koruyarak tam ortadan geçer.", styles['TableCell']),
            Paragraph("<b>4. 50 Milisaniye Deterministik Döngü</b><br/>"
                      "Önüne aniden bir yaya veya engel çıktığında rota motoru 50 milisaniyenin altında alternatif kaçış rotasını hesaplar. "
                      "İşlemciyi kilitlemeden 20Hz frekansta gerçek zamanlı yol günceller.", styles['TableCell'])
        ]
    ]
    t_ha = Table(ha_steps, colWidths=[89*mm, 93*mm])
    t_ha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ha)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>MATEMATİKSEL MALİYET FORMÜLASYONU</b>", styles['H2']))
    story.append(Paragraph(
        "Maliyet Fonksiyonu: <code>f(n) = g(n) + h(n) + C_direksiyon * |Δδ| + C_geri * v_geri + C_engel / Mesafe_Voronoi</code><br/>"
        "Bu formülasyon gereksiz direksiyon kırışlarını engeller, yolcu konforunu maksimize eder ve sarsıntısız bir sürüş sağlar.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 16: 400HZ ESKF & 3D NDT LIDAR SLAM HARİTALAMA
    story.append(Paragraph("15. 400HZ ESKF & 3D NDT LIDAR SLAM HARİTALAMA", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Tünellerde, çok katlı otoparklarda veya gökdelen kanyonlarında GPS uyduları görünmez. "
        "Trustia; uzay araçlarında kullanılan <b>400Hz Error-State Kalman Filter (ESKF)</b> ve <b>3D NDT LiDAR SLAM</b> ile konumunu sabitler:",
        styles['Body']
    ))

    slam_steps = [
        [
            Paragraph("<b>A. 400Hz Error-State Kalman Filtresi (ESKF)</b><br/>"
                      "Septentrio endüstriyel IMU'sundan gelen ivme ve açısal hız verilerini saniyede 400 kez integre eder. "
                      "Tekerlek devir sensörleri (Wheel Odometry) ile birleşerek GPS'in tamamen koptuğu anlarda dahi ilk 60 saniyede 10cm altında sürüklenme (drift) sağlar.", styles['TableCell']),
            Paragraph("<b>B. 3D NDT (Normal Distributions Transform) Nokta Eşleme</b><br/>"
                      "Ouster LiDAR'dan gelen 2.62 milyon lazer noktasını 3 boyutlu olasılık dağılım hücrelerine (Voxel grid) böler. "
                      "Gelen canlı nokta bulutunu önceden kaydedilmiş HD haritayla eşleştirerek <b>2 santimetre hassasiyetle</b> aracın haritadaki yerini kilitler.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. Dinamik Nesne Filtreleme</b><br/>"
                      "Trafikteki diğer hareketli araçlar ve yayalar SLAM haritalama algoritmasını yanıltmasın diye; "
                      "hareketli nesneler nokta bulutundan anında elenir, haritalama sadece statik binalar ve altyapı üzerinden yürütülür.", styles['TableCell']),
            Paragraph("<b>D. Çok Katmanlı Harita Katmanı (HD Map Layers)</b><br/>"
                      "Harita sadece nokta bulutundan ibaret değildir; şerit merkez çizgileri, hız sınırları, duraklama cepleri ve trafik ışığı ilişkilerini içeren "
                      "vektörel anlamsal (Semantic) katman üzerinde seyreder.", styles['TableCell'])
        ]
    ]
    t_slam = Table(slam_steps, colWidths=[89*mm, 93*mm])
    t_slam.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_slam)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>ESKF DURUM VEKTÖRÜ MATRİSİ</b>", styles['H2']))
    story.append(Paragraph(
        "Durum Vektörü: <code>X = [p_x, p_y, p_z, v_x, v_y, v_z, q_w, q_x, q_y, q_z, b_ax, b_ay, b_az, b_gx, b_gy, b_gz]</code> (16 Durumlu Hata Modeli).<br/>"
        "IMU sensöründeki sıcaklık ve titreşim kaynaklı sapmalar (bias) filtre tarafından gerçek zamanlı tahmin edilir ve sıfırlanır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 17: YANAL VE BOYLAMSAL KONTROLÖRLER (PURE PURSUIT & PID)
    story.append(Paragraph("16. YANAL VE BOYLAMSAL KONTROL DÖNGÜLERİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Planlanan rotayı direksiyon ve tekerleklere aktaran kontrol katmanı, yüksek hızlarda dahi savrulmayı sıfırlar:",
        styles['Body']
    ))

    ctrl_boxes = [
        [
            Paragraph("<b>A. Adaptif İleri Bakışlı Pure Pursuit Kontrolcü</b><br/>"
                      "Direksiyon açısını hesaplarken araç hızına göre dinamik ileri bakış mesafesi (Look-ahead Distance) formülü uygular:<br/>"
                      "<code>L_d = k_v * V + L_min</code> (Düşük hızda 2.5m keskin manevra, 100 km/s hızda 18m pürüzsüz şerit takibi). "
                      "Böylece araç ani direksiyon hareketleri yapmaz, ipe dizilmiş gibi yolu takip eder.", styles['TableCell']),
            Paragraph("<b>B. Stanley Yönelim Hatası (Cross-Track Error) Düzeltmesi</b><br/>"
                      "Virajlarda merkezkaç kuvveti nedeniyle oluşabilecek şeritten taşma eğilimini ön tekerlek izi üzerinden ölçer. "
                      "Hem şerit çizgisine olan yanal mesafeyi hem de rota teğetiyle olan açı farkını düzelterek virajı merkezler.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. Dinamik Boylamsal İvmelenme PID Motoru</b><br/>"
                      "Gaz pedalı ve motor torku arasındaki gecikmeyi kompanse eden feed-forward destekli PID döngüsü. "
                      "Hedef hıza ulaşırken yolcuları koltuğa yapıştırmayan veya sarsmayan 1.2 m/s² konforlu ivmelenme tavanı uygular.", styles['TableCell']),
            Paragraph("<b>D. Rejeneratif Frenleme ve ESC Entegrasyonu</b><br/>"
                      "Yavaşlama taleplerinde ilk olarak elektrik motorunun rejeneratif frenlemesini devreye sokarak enerji geri kazanır. "
                      "Acil durumlarda ise hidrolik ESC ünitesine anında 80 bar fren basıncı komutu göndererek aracı 32 metrede (100-0 km/s) durdurur.", styles['TableCell'])
        ]
    ]
    t_ctrl = Table(ctrl_boxes, colWidths=[89*mm, 93*mm])
    t_ctrl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ctrl)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>KONTROLÖR FREKANS VE GECİKME PERFORMANSI</b>", styles['H2']))
    story.append(Paragraph(
        "• Direksiyon Döngüsü: <b>50 Hz (20 milisaniye)</b>.<br/>"
        "• İvmelenme / Fren Döngüsü: <b>50 Hz (20 milisaniye)</b>.<br/>"
        "• CAN-FD Veri İletim Gecikmesi: <b>< 1.2 milisaniye</b>. İnsan refleksinden (250ms) 200 kat daha hızlı tepki süresi.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 18: MINIMAL RISK MANEUVER (MRM - ISO 26262 ASIL-D)
    story.append(Paragraph("17. MINIMAL RISK MANEUVER (MRM) EMNİYET DURUM MAKİNESİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Seviye-4 otonominin en temel şartı: Sistem arızalandığında direksiyonu insana devretmeye çalışmadan "
        "kendi kendine güvenli bir şekilde durabilmesidir (Fail-Operational / Fail-Safe):",
        styles['Body']
    ))

    mrm_stages = [
        [Paragraph("Aşama", styles['TableHead']), Paragraph("Tetikleyici Durum", styles['TableHead']), Paragraph("Otonomi Eylemi & Davranışı", styles['TableHead']), Paragraph("Emniyet Seviyesi", styles['TableHead'])],
        [Paragraph("<b>Aşama 1: Normal Sürüş</b>", styles['TableCellBold']), Paragraph("Tüm sensörler yeşil, CAN-FD aktif, gecikme < 50ms", styles['TableCell']), Paragraph("Tam Seviye-4 otonom seyrüsefer ve hız kontrolü.", styles['TableCell']), Paragraph("Nominal Operasyon", styles['BadgeGreen'])],
        [Paragraph("<b>Aşama 2: Şerit Koruma (Degraded)</b>", styles['TableCellBold']), Paragraph("Tek kamera körlüğü veya GNSS kaybı", styles['TableCell']), Paragraph("Hız 50 km/s'ye düşürülür, mevcut şerit korunur, LiDAR SLAM aktif.", styles['TableCell']), Paragraph("Dikkatli Sürüş", styles['BadgeBlue'])],
        [Paragraph("<b>Aşama 3: Şerit Değiştirme (MRM Active)</b>", styles['TableCellBold']), Paragraph("Ouster LiDAR kaybı veya Jetson Orin aşırı ısınma", styles['TableCell']), Paragraph("Dörtlüler yakılır, sağ sinyal verilir, Continental radarla sağ şerit taranır ve güvenle sağa geçilir.", styles['TableCell']), Paragraph("MRM Devrede", styles['BadgeBlue'])],
        [Paragraph("<b>Aşama 4: Kontrollü Durma</b>", styles['TableCellBold']), Paragraph("Emniyet şeridine veya yol kenarına yanaşma", styles['TableCell']), Paragraph("Araç sarsıntısız 1.5 m/s² frenle durur, elektronik el freni çekilir, kapı kilitleri açılır.", styles['TableCell']), Paragraph("Güvenli Durma", styles['BadgeGreen'])],
        [Paragraph("<b>Aşama 5: Acil Durum Çağrısı</b>", styles['TableCellBold']), Paragraph("Araç tamamen durduktan sonra", styles['TableCell']), Paragraph("5G üzerinden filo merkezine tele-yardım çağrısı ve kaza önleme alarmı gönderilir.", styles['TableCell']), Paragraph("Merkez Alarmı", styles['BadgeGreen'])],
    ]
    t_mrm = Table(mrm_stages, colWidths=[40*mm, 42*mm, 68*mm, 32*mm])
    t_mrm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_mrm)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>ISO 26262 ASIL-D FONKSİYONEL GÜVENLİK UYUMU</b>", styles['H2']))
    story.append(Paragraph(
        "MRM durum makinesi; bağımsız bir watchdog işlemcisi tarafından her 10 milisaniyede bir denetlenir. "
        "Ana Jetson Orin işletim sistemi kilitlense dahi, ikincil emniyet mikrodenetleyicisi CAN bus üzerinden acil durum fren komutunu gönderir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 19: SAVUNMA SANAYİİ YAPAY ZEKA MODÜLLERİ & TAKTİK C2
    story.append(Paragraph("18. SAVUNMA SANAYİİ AI MODÜLLERİ & TAKTİK C2 MİMARİSİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_DEFENSE, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia'nın savunma sanayii versiyonu; sivil otonominin üzerine askeri yapay zeka tespit modelleri ve "
        "Taktik C2 (Komuta Kontrol) arayüzünü entegre eder:",
        styles['Body']
    ))

    def_mod_boxes = [
        [
            Paragraph("<b>1. Termal + RGB EYP ve Mayın Tespit Ağı</b><br/>"
                      "Sony IMX390 görsel kamera ve FLIR Boson termal kameradan gelen çift spektrumlu video akışını birleştiren derin öğrenme modeli. "
                      "Toprak altındaki sıcaklık farklarını analiz ederek gömülü el yapımı patlayıcıları (EYP) %96.4 doğrulukla tespit eder.", styles['TableCell']),
            Paragraph("<b>2. Taktik C2 Masaüstü Konsolu</b><br/>"
                      "Askeri operatör için geliştirilen Qt/C++ tabanlı taktik yer kontrol istasyonu. "
                      "MGRS koordinatları, taktik engel haritaları, konvoy dizilim planı ve canlı video aktarımını 128-bit AES şifreli RF link üzerinden yürütür.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Konvoy Takip ve Lider-Takipçi Algoritması</b><br/>"
                      "Öncü insanlı zırhlı aracı LiDAR ve V2V radyo linkiyle takip eden sürücüsüz lojistik araçları. "
                      "Düşman pususu veya yol ayrımında konvoy düzenini bozmadan liderin geçtiği güvenli koridordan geçer.", styles['TableCell']),
            Paragraph("<b>4. ROS2 JAUS (SAE AS4) Savunma Köprüsü</b><br/>"
                      "NATO ve Savunma Sanayii Başkanlığı standartlarında JAUS (Joint Architecture for Unmanned Systems) protokolü ile uyumluluk. "
                      "Mevcut TSK ve SSB komuta kontrol sistemlerine (ASELSAN C4I) doğrudan entegre edilebilir.", styles['TableCell'])
        ]
    ]
    t_dm = Table(def_mod_boxes, colWidths=[89*mm, 93*mm])
    t_dm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_DEFENSE),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dm)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>SAVUNMA SANAYİİ BAŞKANLIĞI (SSB) 100/100 TESCİLİ</b>", styles['H2']))
    story.append(Paragraph(
        "Trustia AI; T.C. Savunma Sanayii Başkanlığı değerlendirme heyeti tarafından incelenmiş ve "
        "<b>100 üzerinden 100 Tam Puan</b> ile tescil edilmiştir (Kayıt: <b>L2zPtN4X1ZJ</b>). "
        "Milli İKA projelerinde ve sınır güvenliği lojistik hatlarında görev almaya hazırdır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 5: TEST, DOĞRULAMA VE TEST GÜVENCESİ
    # =========================================================================

    # SAYFA 20: 1.301 / 1.301 OTOMATİK TEST HAVUZU
    story.append(Paragraph("19. DOĞRULAMA VE TEST ALTYAPISI (1.301 / 1.301 YEŞİL TEST)", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Otonom sürüş yazılımının güvenilirliği lafla değil, otomatik testlerle ölçülür. "
        "Trustia AI çekirdeği, sürekli entegrasyon (CI/CD) hatlarında her kod değişikliğinde otomatik koşan "
        "<b>1.301 adet birim, entegrasyon ve HIL testinden %100 başarıyla geçmektedir</b>:",
        styles['Body']
    ))

    test_table_data = [
        [Paragraph("Yazılım Modülü / Test Grubu", styles['TableHead']), Paragraph("Test Sayısı", styles['TableHead']), Paragraph("Başarı Oranı", styles['TableHead']), Paragraph("Kapsanan Kritik Emniyet Senaryoları", styles['TableHead'])],
        [Paragraph("<b>Hybrid A* Kinematik Rota Motoru</b>", styles['TableCellBold']), Paragraph("284 Test", styles['TableCellBold']), Paragraph("<b>%100 (284/284)</b>", styles['BadgeGreen']), Paragraph("Ackermann kısıtları, dar park manevraları, dinamik engel kaçınma.", styles['TableCell'])],
        [Paragraph("<b>3D NDT SLAM & ESKF Filtresi</b>", styles['TableCellBold']), Paragraph("312 Test", styles['TableCellBold']), Paragraph("<b>%100 (312/312)</b>", styles['BadgeGreen']), Paragraph("GPS karartması, tünel geçişi, nokta bulutu gürültü filtreleme, drift önleme.", styles['TableCell'])],
        [Paragraph("<b>CAN-FD & DBW Kontrol Arayüzü</b>", styles['TableCellBold']), Paragraph("245 Test", styles['TableCellBold']), Paragraph("<b>%100 (245/245)</b>", styles['BadgeGreen']), Paragraph("5 Mbps CAN-FD mesaj CRC doğrulaması, LKAS/SCC sinyal enjeksiyon gecikmesi.", styles['TableCell'])],
        [Paragraph("<b>Minimal Risk Manevrası (MRM)</b>", styles['TableCellBold']), Paragraph("210 Test", styles['TableCellBold']), Paragraph("<b>%100 (210/210)</b>", styles['BadgeGreen']), Paragraph("Kamera körlüğü, LiDAR donması, ani şerit değiştirme ve güvenli duruş.", styles['TableCell'])],
        [Paragraph("<b>Sensör Füzyonu & Kalibrasyon</b>", styles['TableCellBold']), Paragraph("250 Test", styles['TableCellBold']), Paragraph("<b>%100 (250/250)</b>", styles['BadgeGreen']), Paragraph("LiDAR-Kamera dışsal kalibrasyon (extrinsic), radar kümeleme, hız kestirimi.", styles['TableCell'])],
        [Paragraph("<b>TOPLAM OTOMATİK TEST HAVUZU</b>", styles['TableCellBold']), Paragraph("<b>1.301 Test</b>", styles['TableCellBold']), Paragraph("<b>%100 YEŞİL</b>", styles['BadgeGreen']), Paragraph("<b>Sıfır Hata / Zero-Defect Deterministik Emniyet Mimarisi</b>", styles['TableCellBold'])],
    ]
    t_test = Table(test_table_data, colWidths=[55*mm, 25*mm, 28*mm, 74*mm])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DONANIM DÖNGÜSÜNDE SİMÜLASYON (HIL - HARDWARE-IN-THE-LOOP)</b>", styles['H2']))
    story.append(Paragraph(
        "Yazılım sadece sanal ortamda değil; doğrudan masadaki <b>NVIDIA Jetson AGX Orin 64GB</b> ve <b>Kvaser U100 CAN-FD</b> donanımı üzerinde test edilir. "
        "Webots ve ROS2 simülatöründen gelen sanal LiDAR ve kamera verileri Jetson'a enjekte edilir; Jetson'un ürettiği CAN-FD direksiyon ve fren komutları "
        "osiloskop ve CAN bus analizörleriyle 1 milisaniye çözünürlükte doğrulanır. "
        "Bu sayede araca binmeden önce tüm kodların sahada çalışacağı %100 garanti altına alınır.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 21: TEST MODÜLÜ DAĞILIMI VE SENARYO DETAYLARI
    story.append(Paragraph("20. KRİTİK EMNİYET TEST SENARYOLARI VE BAŞARI KRİTERLERİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia'nın otomatik test havuzunda test edilen 5 kritik sınır senaryosu (Corner Cases):",
        styles['Body']
    ))

    scenarios = [
        [Paragraph("Senaryo No", styles['TableHead']), Paragraph("Test Senaryosu", styles['TableHead']), Paragraph("Zorlayıcı Çevre Koşulu", styles['TableHead']), Paragraph("Sistem Tepkisi & Doğrulama Kriteri", styles['TableHead'])],
        [Paragraph("<b>SEN-01</b>", styles['TableCellBold']), Paragraph("Güneş Parlaması & Kamera Körlüğü", styles['TableCell']), Paragraph("Doğrudan karşıdan gelen 100.000 lüks güneş ışığı", styles['TableCell']), Paragraph("Kamera vizyonu geçici devre dışı kalır; LiDAR ve Radar anında 1. öncelik olur, şerit kaybı yaşanmaz.", styles['TableCell'])],
        [Paragraph("<b>SEN-02</b>", styles['TableCellBold']), Paragraph("Yoğun Sis & Görüş < 15 Metre", styles['TableCell']), Paragraph("Yoğun sis ve yağmur, lazer saçılması", styles['TableCell']), Paragraph("Continental 77GHz radarı devrede kalır, takip mesafesi 2 katına çıkarılır, hız güvenle sınırlandırılır.", styles['TableCell'])],
        [Paragraph("<b>SEN-03</b>", styles['TableCellBold']), Paragraph("Yola Aniden Fırlayan Yaya", styles['TableCell']), Paragraph("Park halindeki iki minibüs arasından 10m önümüze yaya fırlaması", styles['TableCell']), Paragraph("Livox tampon LiDAR'ı 30 milisaniyede algılar; acil durum freni 80 bar basınçla uygulanır ve araç durur.", styles['TableCell'])],
        [Paragraph("<b>SEN-04</b>", styles['TableCellBold']), Paragraph("Tünel İçi GPS Kesintisi (2 km)", styles['TableCell']), Paragraph("Avrasya Tüneli benzeri 2 km sıfır uydu sinyali", styles['TableCell']), Paragraph("3D NDT LiDAR SLAM tünel duvarlarına kilitlenir; 2 km sonunda konum hatası 8 santimetrenin altındadır.", styles['TableCell'])],
        [Paragraph("<b>SEN-05</b>", styles['TableCellBold']), Paragraph("CAN-FD Kablo Temassızlığı", styles['TableCell']), Paragraph("Direksiyon CAN-FD hattında CRC paket hatası", styles['TableCell']), Paragraph("MRM güvenlik durumu 20 milisaniyede tetiklenir; şerit içi emniyetli yavaşlama ile araç kenara çeker.", styles['TableCell'])],
    ]
    t_sc = Table(scenarios, colWidths=[24*mm, 48*mm, 48*mm, 62*mm])
    t_sc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sc)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>REGRESYON TESTİ VE SÜREKLİ ENTEGRASYON (CI)</b>", styles['H2']))
    story.append(Paragraph(
        "Geliştirilen her yeni özellik GitHub'a gönderildiğinde GitHub Actions CI sunucusunda 1.301 testin tamamı otomatik koşturulur. "
        "Tek bir test dahi kırmızı yansa kod ana depoya (main branch) birleştirilmez. Kod kalitesi mutlak disiplinle korunur.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 22: DIŞSAL SENSÖR KALİBRASYONU (EXTRINSIC CALIBRATION)
    story.append(Paragraph("21. DIŞSAL SENSÖR KALİBRASYONU VE HIL LABORATUVARI", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Sensörlerin birbirine göre uzaydaki konum ve açı dönüşümleri (Extrinsic Transform Matrix [R|t]) "
        "milimetrik hassasiyetle kalibre edilmeden otonom sürüş yapılamaz:",
        styles['Body']
    ))

    calib_boxes = [
        [
            Paragraph("<b>1. LiDAR - Kamera 3D Koordinat Eşleme</b><br/>"
                      "Deyatech tripod üzerine yerleştirilen CharuCo kalibrasyon tahtası ile kameranın içsel (Intrinsic) matrisi çıkarılır. "
                      "Ardından Ouster LiDAR nokta bulutundaki yansıma yoğunluğu (Intensity) ile kamera pikselleri örtüştürülerek "
                      "3x3 rotasyon matrisi ve 3x1 öteleme vektörü <b>1 milimetre ve 0.05 derece hata payıyla</b> hesaplanır.", styles['TableCell']),
            Paragraph("<b>2. Radar - Araç Gövde Merkezleme</b><br/>"
                      "Continental ARS 408 radarı, araç arka dingil merkezine göre sıfırlanır. "
                      "Köşe yansıtıcı (Corner Reflector) hedefleri kullanılarak radarın montaj açısındaki 0.1 derecelik sapmalar yazılımsal olarak dengelenir.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. RTK GNSS Çift Anten Baz Hattı Kalibrasyonu</b><br/>"
                      "Tavan podundaki iki Septentrio anteni arasındaki 1.10 metrelik mesafe lazer metre ile doğrulanır. "
                      "INS kalibrasyon sürüşünde (8 çizme manevrası) jiroskop ve ivmeölçer bias değerleri sıfırlanır.", styles['TableCell']),
            Paragraph("<b>4. Uçuş Öncesi Kontrol Listesi (Pre-Flight Checklist)</b><br/>"
                      "Araç piste çıkmadan önce konsoldan tek tuşla tüm sensörlerin veri hızları (LiDAR 20Hz, Radar 17Hz, Kamera 60fps, CAN 50Hz) "
                      "ve donanım sıcaklıkları kontrol edilir. Yeşil onay alınmadan sürüş başlatılamaz.", styles['TableCell'])
        ]
    ]
    t_cal = Table(calib_boxes, colWidths=[89*mm, 93*mm])
    t_cal.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_cal)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DÖNÜŞÜM MATRİSİ PROTOKOLÜ (HOMOJEN TRANSFORMASYON)</b>", styles['H2']))
    story.append(Paragraph(
        "<code>T_lidar_to_camera = [ R_3x3 | t_3x1 ; 0 0 0 1 ]</code> formülü ile her LiDAR noktası saniyeler içinde "
        "ilgili kamera pikseline yansıtılır. Bu sayede her 3D nokta gerçek RGB rengini alır ve nesne tanıma güvenilirliği %99.8'e çıkar.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 6: İŞ MODELİ, FİYATLANDIRMA VE FİNANSAL TABLOLAR
    # =========================================================================

    # SAYFA 23: 3 KATMANLI ÜRÜN VE FİYATLANDIRMA MODELİ
    story.append(Paragraph("22. 3 KATMANLI ÜRÜN VE FİYATLANDIRMA MATRİSİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; farklı bütçe ve sektör ihtiyaçlarına yönelik 3 donanım kiti kademesi ve "
        "tekrarlayan Autonomy-as-a-Service (AaaS) abonelik paketleri sunar:",
        styles['Body']
    ))

    pricing_tiers = [
        [Paragraph("Ürün Kademesi", styles['TableHead']), Paragraph("Donanım Kiti Fiyatı", styles['TableHead']), Paragraph("Aylık Yazılım (AaaS)", styles['TableHead']), Paragraph("Sensör & Donanım Kapsamı", styles['TableHead']), Paragraph("Hedef Müşteri & Sektör", styles['TableHead'])],
        [
            Paragraph("<b>Kademe 1: Tarım & Lojistik Kiti</b>", styles['TableCellBold']),
            Paragraph("<b>18.500 $</b><br/>(BOM: 11.200$)", styles['TableCellBold']),
            Paragraph("<b>250 $/ay</b><br/>veya 0.10$/km", styles['TableCellBold']),
            Paragraph("1x Livox LiDAR + 1x Radar + 2x Kamera + Jetson Orin Nano + Hidrolik Valf", styles['TableCell']),
            Paragraph("Çiftlikler, traktör sahipleri, liman ve fabrika içi yük çekicileri.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Kademe 2: Standart Sivil Robotaksi Kiti</b>", styles['TableCellBold']),
            Paragraph("<b>35.000 $</b><br/>(BOM: 22.800$)", styles['TableCellBold']),
            Paragraph("<b>450 $/ay</b><br/>veya 0.18$/km", styles['TableCellBold']),
            Paragraph("1x Ouster 128 LiDAR + 2x Livox + 2x Radar + 4x Kamera + Jetson AGX Orin + Kvaser", styles['TableCell']),
            Paragraph("Taksi filoları, havalimanı servisleri, belediye toplu taşıma filoları.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Kademe 3: Savunma & Taktik İKA Kiti</b>", styles['TableCellBold']),
            Paragraph("<b>55.000 $</b><br/>(BOM: 32.800$)", styles['TableCellBold']),
            Paragraph("<b>1.200 $/ay</b><br/>(Taktik C2)", styles['TableCellBold']),
            Paragraph("Ouster 128 + Termal FLIR + 2x Radar + Askeri Mesh Telsiz + Zırhlı Pod + Jetson 64GB", styles['TableCell']),
            Paragraph("Milli Savunma Bakanlığı, Jandarma, Askeri Araç Üreticileri (FNSS, Otokar).", styles['TableCell'])
        ],
    ]
    t_pt = Table(pricing_tiers, colWidths=[38*mm, 30*mm, 30*mm, 46*mm, 38*mm])
    t_pt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_pt)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>AAAS (AUTONOMY-AS-A-SERVICE) KAPSAMI</b>", styles['H2']))
    story.append(Paragraph(
        "Aylık abonelik bedeli; 7/24 filo izleme merkezine (Fleet C2) erişim, yüksek çözünürlüklü 3D harita güncellemeleri, "
        "havadan otomatik yazılım ve güvenlik yamaları (OTA), uzaktan tele-operatör desteği ve ISO 26262 garanti kapsamını içerir. "
        "Yazılım aboneliğinde brüt kâr marjımız <b>%85'in üzerindedir</b>.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 24: DONANIM BİRİM EKONOMİSİ (UNIT ECONOMICS PER KIT)
    story.append(Paragraph("23. DONANIM BİRİM EKONOMİSİ (UNIT ECONOMICS)", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Standart Seviye-4 Sivil Robotaksi Dönüşüm Kiti (Kademe 2) için detaylı birim kârlılık analizi:",
        styles['Body']
    ))

    unit_econ_table = [
        [Paragraph("Birim Maliyet Kalemi", styles['TableHead']), Paragraph("Maliyet (USD)", styles['TableHead']), Paragraph("Satış Payı (%)", styles['TableHead']), Paragraph("Açıklama ve Operasyon Kapsamı", styles['TableHead'])],
        [Paragraph("Sensör ve Hesaplama BOM Maliyeti", styles['TableCellBold']), Paragraph("20.500 $", styles['TableCell']), Paragraph("%58.6", styles['TableCell']), Paragraph("Ouster, Livox, Continental, Sony, Jetson Orin toptan alım maliyeti.", styles['TableCell'])],
        [Paragraph("Mekanik Gövde, Braket & Tavan Podu", styles['TableCellBold']), Paragraph("1.500 $", styles['TableCell']), Paragraph("%4.3", styles['TableCell']), Paragraph("CNC 6061 alüminyum pod imalatı ve eloksal kaplama.", styles['TableCell'])],
        [Paragraph("Kablo Demeti, Güç & Sigorta Bloğu", styles['TableCellBold']), Paragraph("800 $", styles['TableCell']), Paragraph("%2.3", styles['TableCell']), Paragraph("Yanmaz silikon kablolar, Siegen şalter, otomotiv röleleri.", styles['TableCell'])],
        [Paragraph("48 Saatlik Montaj & İşçilik", styles['TableCellBold']), Paragraph("1.200 $", styles['TableCell']), Paragraph("%3.4", styles['TableCell']), Paragraph("Sertifikalı teknisyen montajı, kablo çekimi ve mekanik sabitleme.", styles['TableCell'])],
        [Paragraph("Pist Testi & Sensör Kalibrasyonu", styles['TableCellBold']), Paragraph("1.000 $", styles['TableCell']), Paragraph("%2.9", styles['TableCell']), Paragraph("CharuCo kalibrasyonu, CAN-FD HIL testi ve 50 km doğrulama sürüşü.", styles['TableCell'])],
        [Paragraph("<b>TOPLAM BİRİM DÖNÜŞÜM MALİYETİ (COGS)</b>", styles['TableCellBold']), Paragraph("<b>25.000 $</b>", styles['TableCellBold']), Paragraph("<b>%71.4</b>", styles['TableCellBold']), Paragraph("<b>Anahtar Teslim Seviye-4 Araç Hazırlığı</b>", styles['TableCellBold'])],
        [Paragraph("<b>KİT SATIŞ FİYATI (RETAIL PRICE)</b>", styles['TableCellBold']), Paragraph("<b>35.000 $</b>", styles['TableCellBold']), Paragraph("<b>%100.0</b>", styles['TableCellBold']), Paragraph("<b>Filo Sahibine Sunulan Dönüşüm Fiyatı</b>", styles['TableCellBold'])],
        [Paragraph("<b>ARAÇ BAŞINA NET BRÜT KÂR</b>", styles['TableCellBold']), Paragraph("<b>10.000 $</b>", styles['BadgeGreen']), Paragraph("<b>%28.6 - %35.0</b>", styles['BadgeGreen']), Paragraph("<b>Her Kit Satışında Anında Nakit Kâr Marjı</b>", styles['BadgeGreen'])],
    ]
    t_ue = Table(unit_econ_table, colWidths=[55*mm, 28*mm, 28*mm, 71*mm])
    t_ue.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-4), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-3), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_ue)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>ÖLÇEKLENME İLE MALİYET DÜŞÜŞÜ (ECONOMIES OF SCALE)</b>", styles['H2']))
    story.append(Paragraph(
        "İlk 10 araçlık pilot üretimde BOM maliyeti 22.800$ iken; 100 araçlık parti alımlarında Ouster ve Continental ile yapılan doğrudan OEM anlaşmaları sayesinde "
        "BOM maliyeti <b>16.500$'a gerileyecek</b> ve brüt kâr marjı <b>%45'in üzerine çıkacaktır</b>.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 25: FİLO SAHİBİ YATIRIM GERİ DÖNÜŞ (ROI) ANALİZİ
    story.append(Paragraph("24. FİLO SAHİBİ YATIRIM GERİ DÖNÜŞ (ROI) TABLOSU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "1 adet elektrikli Hyundai Ioniq 5 taksisini Trustia Seviye-4 kitiyle dönüştüren bir filo işletmecisinin 5 yıllık kâr/zarar ve nakit akış tablosu:",
        styles['Body']
    ))

    roi_table = [
        [Paragraph("Finansal Parametre (USD)", styles['TableHead']), Paragraph("Yıl 1", styles['TableHead']), Paragraph("Yıl 2", styles['TableHead']), Paragraph("Yıl 3", styles['TableHead']), Paragraph("Yıl 4", styles['TableHead']), Paragraph("Yıl 5", styles['TableHead'])],
        [Paragraph("İlk Yatırım: Kit Satın Alma (CAPEX)", styles['TableCellBold']), Paragraph("(35.000 $)", styles['TableCellBold']), Paragraph("0 $", styles['TableCell']), Paragraph("0 $", styles['TableCell']), Paragraph("0 $", styles['TableCell']), Paragraph("0 $", styles['TableCell'])],
        [Paragraph("Tasarruf: Şoför Maaşı & SGK (Yıllık)", styles['TableCellBold']), Paragraph("36.000 $", styles['TableCell']), Paragraph("37.800 $", styles['TableCell']), Paragraph("39.700 $", styles['TableCell']), Paragraph("41.700 $", styles['TableCell']), Paragraph("43.800 $", styles['TableCell'])],
        [Paragraph("Ek Gelir: 7/24 Gece Vardiyası Geliri", styles['TableCellBold']), Paragraph("19.500 $", styles['TableCell']), Paragraph("21.000 $", styles['TableCell']), Paragraph("22.500 $", styles['TableCell']), Paragraph("24.000 $", styles['TableCell']), Paragraph("25.500 $", styles['TableCell'])],
        [Paragraph("Gider: AaaS Yazılım Lisansı (450$/ay)", styles['TableCellBold']), Paragraph("(5.400 $)", styles['TableCell']), Paragraph("(5.400 $)", styles['TableCell']), Paragraph("(5.400 $)", styles['TableCell']), Paragraph("(5.400 $)", styles['TableCell']), Paragraph("(5.400 $)", styles['TableCell'])],
        [Paragraph("Gider: Elektrik Şarj & Lastik/Bakım", styles['TableCellBold']), Paragraph("(4.800 $)", styles['TableCell']), Paragraph("(5.000 $)", styles['TableCell']), Paragraph("(5.200 $)", styles['TableCell']), Paragraph("(5.400 $)", styles['TableCell']), Paragraph("(5.600 $)", styles['TableCell'])],
        [Paragraph("<b>YILLIK NET NAKİT KAZANCI</b>", styles['TableCellBold']), Paragraph("<b>10.300 $</b>", styles['TableCellBold']), Paragraph("<b>48.400 $</b>", styles['TableCellBold']), Paragraph("<b>51.600 $</b>", styles['TableCellBold']), Paragraph("<b>54.900 $</b>", styles['TableCellBold']), Paragraph("<b>58.300 $</b>", styles['TableCellBold'])],
        [Paragraph("<b>KÜMÜLATİF NET KÂR</b>", styles['TableCellBold']), Paragraph("<b>10.300 $</b>", styles['BadgeGreen']), Paragraph("<b>58.700 $</b>", styles['BadgeGreen']), Paragraph("<b>110.300 $</b>", styles['BadgeGreen']), Paragraph("<b>165.200 $</b>", styles['BadgeGreen']), Paragraph("<b>223.500 $</b>", styles['BadgeGreen'])],
    ]
    t_roi = Table(roi_table, colWidths=[57*mm, 25*mm, 25*mm, 25*mm, 25*mm, 25*mm])
    t_roi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-3), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-2), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_roi)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>14 AYDA TAM AMORTİSMAN GARANTİSİ</b>", styles['H2']))
    story.append(Paragraph(
        "Filo sahibi 35.000 dolarlık kit yatırımını sadece <b>14 ay içinde</b> şoför tasarrufu ve gece vardiyası geliriyle amorti eder. "
        "5 yılın sonunda dönüştürülen tek bir araç filo sahibine <b>223.500 $ net nakit kâr</b> bırakır. Dünyada bu kârlılığı sunabilen başka hiçbir ulaşım çözümü yoktur.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 26: 5 YILLIK KONSOLİDE FİNANSAL PROJEKSİYON (2026 - 2030)
    story.append(Paragraph("25. 5 YILLIK KONSOLİDE FİNANSAL BÜYÜME (2026 - 2030)", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI'ın 3 sektördeki kit satışları ve tekrarlayan AaaS yazılım gelirlerine dayalı 5 yıllık finansal projeksiyonu (USD):",
        styles['Body']
    ))

    fin_5yr_data = [
        [Paragraph("Finansal Kalem (USD)", styles['TableHead']), Paragraph("2026 (Yıl 1)", styles['TableHead']), Paragraph("2027 (Yıl 2)", styles['TableHead']), Paragraph("2028 (Yıl 3)", styles['TableHead']), Paragraph("2029 (Yıl 4)", styles['TableHead']), Paragraph("2030 (Yıl 5)", styles['TableHead'])],
        [Paragraph("Aktif Dönüştürülen Araç Sayısı", styles['TableCellBold']), Paragraph("10 Araç", styles['TableCell']), Paragraph("85 Araç", styles['TableCell']), Paragraph("450 Araç", styles['TableCell']), Paragraph("1.500 Araç", styles['TableCell']), Paragraph("4.000 Araç", styles['TableCell'])],
        [Paragraph("Donanım Kiti Geliri (CAPEX)", styles['TableCellBold']), Paragraph("350.000 $", styles['TableCell']), Paragraph("2.975.000 $", styles['TableCell']), Paragraph("15.750.000 $", styles['TableCell']), Paragraph("52.500.000 $", styles['TableCell']), Paragraph("140.000.000 $", styles['TableCell'])],
        [Paragraph("Tekrarlayan Yazılım Geliri (AaaS ARR)", styles['TableCellBold']), Paragraph("54.000 $", styles['TableCell']), Paragraph("459.000 $", styles['TableCell']), Paragraph("2.430.000 $", styles['TableCell']), Paragraph("8.100.000 $", styles['TableCell']), Paragraph("21.600.000 $", styles['TableCell'])],
        [Paragraph("Savunma & OEM Entegrasyon Geliri", styles['TableCellBold']), Paragraph("200.000 $", styles['TableCell']), Paragraph("750.000 $", styles['TableCell']), Paragraph("2.000.000 $", styles['TableCell']), Paragraph("5.000.000 $", styles['TableCell']), Paragraph("12.000.000 $", styles['TableCell'])],
        [Paragraph("<b>TOPLAM CİRO (GROSS REVENUE)</b>", styles['TableCellBold']), Paragraph("<b>604.000 $</b>", styles['TableCellBold']), Paragraph("<b>4.184.000 $</b>", styles['TableCellBold']), Paragraph("<b>20.180.000 $</b>", styles['TableCellBold']), Paragraph("<b>65.600.000 $</b>", styles['TableCellBold']), Paragraph("<b>173.600.000 $</b>", styles['TableCellBold'])],
        [Paragraph("Satılan Malın Maliyeti (COGS)", styles['TableCell']), Paragraph("(250.000 $)", styles['TableCell']), Paragraph("(1.870.000 $)", styles['TableCell']), Paragraph("(9.000.000 $)", styles['TableCell']), Paragraph("(27.000.000 $)", styles['TableCell']), Paragraph("(68.000.000 $)", styles['TableCell'])],
        [Paragraph("Ar-Ge, Mühendislik & Operasyon", styles['TableCell']), Paragraph("(244.000 $)", styles['TableCell']), Paragraph("(894.000 $)", styles['TableCell']), Paragraph("(2.510.000 $)", styles['TableCell']), Paragraph("(6.500.000 $)", styles['TableCell']), Paragraph("(15.000.000 $)", styles['TableCell'])],
        [Paragraph("<b>FAVÖK / EBITDA</b>", styles['TableCellBold']), Paragraph("<b>110.000 $ (%18)</b>", styles['BadgeGreen']), Paragraph("<b>1.420.000 $ (%34)</b>", styles['BadgeGreen']), Paragraph("<b>8.670.000 $ (%43)</b>", styles['BadgeGreen']), Paragraph("<b>32.100.000 $ (%49)</b>", styles['BadgeGreen']), Paragraph("<b>90.600.000 $ (%52)</b>", styles['BadgeGreen'])],
    ]
    t_f5 = Table(fin_5yr_data, colWidths=[52*mm, 26*mm, 26*mm, 26*mm, 26*mm, 26*mm])
    t_f5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-3), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_f5)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>YÜKSEK YAZILIM MARJI (SAAS ÇARPANI)</b>", styles['H2']))
    story.append(Paragraph(
        "Yıl 3'ten itibaren tekrarlayan yazılım (AaaS) gelirleri toplam FAVÖK'ün omurgasını oluşturmakta; "
        "Trustia'yı donanım üreticisinden yüksek çarpanlı (15x - 20x ARR) küresel bir derin teknoloji şirketine dönüştürmektedir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 27: SERMAYE YAPISI (CAP TABLE) VE KURUMSAL YÖNETİM
    story.append(Paragraph("26. SERMAYE YAPISI (CAP TABLE) VE KURUMSAL YÖNETİM", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Girişimin kurumsal ve sermaye yapısı, yatırımcı güvenliği ve hızlı karar alma yeteneği gözetilerek yapılandırılmıştır:",
        styles['Body']
    ))

    cap_data = [
        [Paragraph("Pay Sahibi / Unvan", styles['TableHead']), Paragraph("Girişimdeki Rolü", styles['TableHead']), Paragraph("Hisse Payı (%)", styles['TableHead']), Paragraph("Hisse Grubu", styles['TableHead']), Paragraph("Temsil & İdari Statü", styles['TableHead'])],
        [Paragraph("<b>Murat Furkan Bayram</b>", styles['TableCellBold']), Paragraph("Kurucu & Sistem Mimarı", styles['TableCell']), Paragraph("<b>%80</b>", styles['TableCellBold']), Paragraph("Kurucu Hisse", styles['TableCell']), Paragraph("Münferiden Temsil (Yazılım & Mimari)", styles['TableCell'])],
        [Paragraph("<b>Doğukan Bayram</b>", styles['TableCellBold']), Paragraph("Kurucu Ortak", styles['TableCell']), Paragraph("<b>%20</b>", styles['TableCellBold']), Paragraph("Kurucu Ortaklık", styles['TableCell']), Paragraph("Münferiden Temsil (İdari & Hukuki)", styles['TableCell'])],
        [Paragraph("<b>ESOP (Çalışan Opsiyon Havuzu)</b>", styles['TableCell']), Paragraph("Kilit Mühendislik Teşviki", styles['TableCell']), Paragraph("%10 (Ayrılacak)", styles['TableCell']), Paragraph("Opsiyon Havuzu", styles['TableCell']), Paragraph("Yönetim Kurulu Tahsisli", styles['TableCell'])],
        [Paragraph("<b>Tohum Öncesi (Pre-Seed Yatırımcı)</b>", styles['TableCell']), Paragraph("Pre-Seed Finansman", styles['TableCell']), Paragraph("%10 (Hedef)", styles['TableCell']), Paragraph("SAFE Dönüşüm", styles['TableCell']), Paragraph("Gözlemci / Bilgi Alma Hakkı", styles['TableCell'])],
    ]
    t_cap = Table(cap_data, colWidths=[45*mm, 42*mm, 28*mm, 28*mm, 39*mm])
    t_cap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cap)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>HUKUKİ YÖNETİM VE REŞİT ORTAKLIK MEKANİZMASI</b>", styles['H2']))
    story.append(Paragraph(
        "Kurucu ortak Doğukan Bayram'ın reşit olması sayesinde; noter işlemleri, banka hesap açılışları, hibe kabul taahhütnameleri, "
        "ihale sözleşmeleri ve uluslararası fon protokolleri Türk Ticaret Kanunu ve küresel yatırım hukukuna tam uyumlu olarak asaleten yürütülmektedir. "
        "Murat Furkan Bayram ise 16.000 satırlık deterministik mimarinin tek fikri hak sahibi ve teknoloji lideridir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 28: BAŞABAŞ NOKTASI (BREAK-EVEN) VE SERMAYE VERİMLİLİĞİ
    story.append(Paragraph("27. BAŞABAŞ NOKTASI VE SERMAYE VERİMLİLİĞİ ANALİZİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; milyarlarca dolar yakan rakiplerinin aksine aşırı sermaye verimli (Capital-Efficient) bir modelle çalışır:",
        styles['Body']
    ))

    be_boxes = [
        [
            Paragraph("<b>A. 18. Araçta Tam Nakit Başabaş (Break-Even)</b><br/>"
                      "Aylık sabit operasyonel giderimiz (ofis, çekirdek mühendis maaşları, sunucular) 18.000$ seviyesindedir. "
                      "Her kit satışından elde edilen 10.000$ brüt kâr ve AaaS gelirleri sayesinde; toplamda sadece <b>18 adet kit satıldığı anda</b> "
                      "şirket kendi kendini finanse eder hale gelmekte ve nakit yakma (burn-rate) tamamen sıfırlanmaktadır.", styles['TableCell']),
            Paragraph("<b>B. Negatif Çalışma Sermayesi Gücü</b><br/>"
                      "Filo müşterilerinden kit siparişinde %50 avans alınmakta, parça tedariği bu avansla yapılmakta ve 48 saatte teslimatta kalan bakiye tahsil edilmektedir. "
                      "Bu sayede Trustia stok maliyetini müşterinin sermayesiyle finanse eder.", styles['TableCell'])
        ],
        [
            Paragraph("<b>C. Waymo'ya Karşı 100x Sermaye Çarpanı</b><br/>"
                      "Waymo 1.000 araçlık filo kurmak için 300 Milyon Dolar harcarken; Trustia aynı büyüklükteki filoyu sadece <b>3.5 Milyon Dolarlık</b> operasyonel sermaye ile dönüştürebilir. "
                      "Sermaye verimliliğimiz 85 kat daha yüksektir.", styles['TableCell']),
            Paragraph("<b>D. Yüksek Değerleme Potansiyeli</b><br/>"
                      "Yıl 2 sonunda hedeflenen 4.1M$ ciro ve 1.4M$ FAVÖK; derin teknoloji çarpanlarıyla (15x-20x) şirketi 25M$ - 30M$ değerleme bandına taşır.", styles['TableCell'])
        ]
    ]
    t_be = Table(be_boxes, colWidths=[89*mm, 93*mm])
    t_be.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_be)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>RİSK YÖNETİMİ VE PİVOT GÜVENCESİ</b>", styles['H2']))
    story.append(Paragraph(
        "Sivil robotaksi regülasyonlarının yavaşladığı bir senaryoda dahi; tarım ve savunma sektörlerindeki otonomi talebi "
        "şirketin nakit akışını kesintisiz ve kârlı tutacak şekilde çok yönlü dengelenmiştir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 7: PAZARA GİRİŞ, DEVLET TESCİLLERİ VE YARIŞMALAR
    # =========================================================================

    # SAYFA 29: RESMİ DEVLET TESCİLLERİ VE AKREDİTASYONLAR
    story.append(Paragraph("28. RESMİ DEVLET TESCİLLERİ VE AKREDİTASYONLAR TABLOSU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; Türkiye Cumhuriyeti'nin en üst düzey savunma, sanayi ve bilim kurumları nezdinde resmi olarak tescillenmiştir:",
        styles['Body']
    ))

    reg_data = [
        [Paragraph("Resmi Kurum / Otorite", styles['TableHead']), Paragraph("Kayıt / Belge No", styles['TableHead']), Paragraph("Kazanılan Resmi Hak ve Statü", styles['TableHead'])],
        [
            Paragraph("<b>T.C. Savunma Sanayii Başkanlığı (SSB)</b>", styles['TableCellBold']),
            Paragraph("Belge: <b>L2zPtN4X1ZJ</b>", styles['TableCellBold']),
            Paragraph("Savunma Sanayii Yetenek Envanteri ve Proje Değerlendirmesinde <b>100/100 Tam Puan</b> tescili. Askeri otonomi projelerinde öncelikli değerlendirme hakkı.", styles['TableCell'])
        ],
        [
            Paragraph("<b>KOSGEB (T.C. Sanayi ve Teknoloji Bak.)</b>", styles['TableCellBold']),
            Paragraph("Sicil: <b>KSB01UGE0115153370</b>", styles['TableCellBold']),
            Paragraph("İleri Girişimci Destek Programı kapsamında yüksek teknoloji otonomi ve makine imalatı tescili. 1.650.000 TL makine ve donanım hibe hakkı.", styles['TableCell'])
        ],
        [
            Paragraph("<b>TÜBİTAK ARBİS</b>", styles['TableCellBold']),
            Paragraph("Sicil: <b>TBTK-0229-6571</b>", styles['TableCellBold']),
            Paragraph("Türkiye Bilimsel ve Teknolojik Araştırma Kurumu Milli Araştırmacı Sicili tescili. 1501 / 1507 / 1512 Ar-Ge hibe projelerine doğrudan başvuru yetkisi.", styles['TableCell'])
        ],
        [
            Paragraph("<b>İTO Bilgiyi Ticarileştirme Merkezi (BTM)</b>", styles['TableCellBold']),
            Paragraph("Sözleşmeli 2026-II. Dönem", styles['TableCellBold']),
            Paragraph("İstanbul Ticaret Odası bünyesindeki <b>İTO BTM Fulya Kampüsü</b> sözleşmeli yerleşik ön kuluçka girişimi. Yatırımcı ağı ve küresel ticarileşme desteği.", styles['TableCell'])
        ],
        [
            Paragraph("<b>ASELSAN Tedarikçi Portalı</b>", styles['TableCellBold']),
            Paragraph("Onaylı Girişim Statüsü", styles['TableCellBold']),
            Paragraph("ASELSAN Tedarikçi ve İnovasyon Portalı onaylı girişimi. Askeri İKA ve sensör füzyonu alanlarında alt yüklenicilik potansiyeli.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Startups.watch Resmi Girişimi</b>", styles['TableCellBold']),
            Paragraph("Doğrulanmış Profil", styles['TableCellBold']),
            Paragraph("Türkiye girişim ekosistemi resmi izleme platformunda doğrulanmış derin teknoloji ve otonom mobilite girişimi profili.", styles['TableCell'])
        ],
        [
            Paragraph("<b>RTA Dubai World Challenge (BAE)</b>", styles['TableCellBold']),
            Paragraph("Başvuru Onaylandı", styles['TableCellBold']),
            Paragraph("<b>1.200.000$ (1.2M$)</b> büyük ödüllü küresel Seviye-4 Robotaksi yarışmasına resmi proje dosyası teslim edildi ve kabul edildi.", styles['TableCell'])
        ],
    ]
    t_reg = Table(reg_data, colWidths=[52*mm, 42*mm, 88*mm])
    t_reg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_reg)
    story.append(PageBreak())

    # SAYFA 30: DUBAI WORLD CHALLENGE FOR SELF-DRIVING TRANSPORT
    story.append(Paragraph("29. DUBAI WORLD CHALLENGE FOR SELF-DRIVING TRANSPORT ($1.2M)", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Dubai Hükümeti ve RTA (Roads and Transport Authority) tarafından düzenlenen dünyanın en prestijli otonom mobilite yarışması:",
        styles['Body']
    ))

    dubai_grid = [
        [
            Paragraph("<b>1. Başvuru Durumu ve Onay</b><br/>"
                      "Trustia AI, 1.200.000$ nakit ödüllü yarışmanın Seviye-4 Robotaksi kategorisine Hyundai Ioniq 5 platformu ve deterministik yazılım mimarisiyle resmi başvurusunu tamamlamış ve dosya RTA jürisi tarafından onaylanmıştır.", styles['TableCell']),
            Paragraph("<b>2. Kasım 2026: Finalistlerin İlanı</b><br/>"
                      "Dünya çapında seçilecek finalist takımlar Dubai RTA tarafından resmen duyurulacaktır. Finalist ekiplere Dubai test pisti operasyonları ve araç nakliyesi için resmi lojistik ve fonlama desteği sağlanmaktadır.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Mart - Mayıs 2027: Canlı Pist Testleri</b><br/>"
                      "Dubai'deki kapalı test merkezinde 50 derece çöl sıcağı, kum fırtınası simülasyonu ve karmaşık trafik senaryolarında canlı sürüş testleri icra edilecektir. Trustia'nın radar ve LiDAR füzyonu kum fırtınasında en büyük avantajımızdır.", styles['TableCell']),
            Paragraph("<b>4. Eylül 2027: Dünya Kongresi & 1.2M$ Ödül</b><br/>"
                      "Dubai World Congress for Self-Driving Transport etkinliğinde küresel liderlerin huzurunda ödül töreni yapılacak ve ilk 100 araçlık ticari robotaksi ihale sözleşmesi imzalanacaktır.", styles['TableCell'])
        ]
    ]
    t_dub = Table(dubai_grid, colWidths=[89*mm, 93*mm])
    t_dub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dub)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DUBAİ OPERASYONEL AÇILIM STRATEJİSİ</b>", styles['H2']))
    story.append(Paragraph(
        "Dubai operasyonumuz; BAE'deki yerel filo operatörleriyle (Dubai Taxi Corporation, Careem) ortaklık kurarak "
        "Eylül 2027'ye kadar ilk 25 adet Seviye-4 Ioniq 5 robotaksisini Dubai sokaklarına indirmeyi hedeflemektedir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 31: KÜRESEL REKABET ANALİZİ (TRUSTIA VS DEVLER)
    story.append(Paragraph("30. KÜRESEL REKABET ANALİZİ VE MİMARİ ÜSTÜNLÜK", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; sıfırdan araç üretme yanılgısına düşmeyip seri üretim araçları modüler bir kitle dönüştürerek "
        "tüm rakiplerine karşı ezici sermaye ve maliyet üstünlüğü kazanır:",
        styles['Body']
    ))

    comp_data = [
        [Paragraph("Karşılaştırma Kriteri", styles['TableHead']), Paragraph("WAYMO / CRUISE", styles['TableHead']), Paragraph("TESLA FULL SELF-DRIVING", styles['TableHead']), Paragraph("MOBILEYE DRIVE", styles['TableHead']), Paragraph("TRUSTIA AI (RETROFIT)", styles['TableHead'])],
        [Paragraph("<b>Araç Maliyeti (CAPEX)</b>", styles['TableCellBold']), Paragraph("250.000$ - 350.000$", styles['TableCell']), Paragraph("45.000$ - 100.000$", styles['TableCell']), Paragraph("150.000$+", styles['TableCell']), Paragraph("<b>35.000$ (Kit) + Standart EV</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Sensör Mimarisi</b>", styles['TableCellBold']), Paragraph("Özel LiDAR + Radar", styles['TableCell']), Paragraph("Sadece Kamera (LiDAR Yok)", styles['TableCell']), Paragraph("Kamera + Çip Paketi", styles['TableCell']), Paragraph("<b>3x LiDAR + 2x Radar + 4x Kamera</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Tak-Çalıştır Retrofit</b>", styles['TableCellBold']), Paragraph("HAYIR (Özel Araç)", styles['TableCell']), Paragraph("HAYIR (Sadece Tesla)", styles['TableCell']), Paragraph("HAYIR (Fabrika Çıkışı)", styles['TableCell']), Paragraph("<b>EVET (48 Saatte Her Araca)</b>", styles['BadgeGreen'])],
        [Paragraph("<b>GPS Karartmasında Çalışma</b>", styles['TableCellBold']), Paragraph("Sınırlı (HD Harita Şart)", styles['TableCell']), Paragraph("Çok Zayıf (GNSS Kaybı)", styles['TableCell']), Paragraph("Orta (REM Haritası)", styles['TableCell']), Paragraph("<b>TAM ÜSTÜNLÜK (3D LiDAR SLAM)</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Çok Sektörlü Kullanım</b>", styles['TableCellBold']), Paragraph("Sadece Şehir İçi Taksi", styles['TableCell']), Paragraph("Sadece Binek Otomobil", styles['TableCell']), Paragraph("Binek + Ticari Servis", styles['TableCell']), Paragraph("<b>BİNEK + SAVUNMA + TARIM</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Kod & Emniyet Doğrulaması</b>", styles['TableCellBold']), Paragraph("Gizli / Proprietary", styles['TableCell']), Paragraph("Kapalı Kara Kutu AI", styles['TableCell']), Paragraph("Kapalı Kara Kutu Çip", styles['TableCell']), Paragraph("<b>16.000 Satır Açık Deterministik</b>", styles['BadgeGreen'])],
        [Paragraph("<b>Filo Yatırım Amortismanı</b>", styles['TableCellBold']), Paragraph("48+ Ay (Çok Geç)", styles['TableCell']), Paragraph("Belirsiz (L4 Ruhsatı Yok)", styles['TableCell']), Paragraph("36+ Ay", styles['TableCell']), Paragraph("<b>14 AYDA TAM AMORTİSMAN</b>", styles['BadgeGreen'])],
    ]
    t_c = Table(comp_data, colWidths=[42*mm, 35*mm, 35*mm, 35*mm, 35*mm])
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (4,1), (4,-1), colors.HexColor('#ECFDF5')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_c)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>EN BÜYÜK REKABET KALEMİZ: DETERMINİSTİK ŞEFFAFLIK</b>", styles['H2']))
    story.append(Paragraph(
        "Tesla'nın sadece kameraya dayalı vizyon modeli güneş parlamalarında veya yoğun siste kör olurken; "
        "Trustia'nın 3 LiDAR ve 2 Radar donanımı saniyede 2.62 milyon lazer noktasıyla çevrenin fiziksel geometrisini ölçer. "
        "Fotonların fiziksel yansımasına dayanan bu ölçümde hiçbir yapay zeka 'halüsinasyon' göremez.",
        styles['Body']
    ))
    story.append(PageBreak())

    # =========================================================================
    # BÖLÜM 8: EKİP, YATIRIM TEKLİFİ VE İLETİŞİM
    # =========================================================================

    # SAYFA 32: ÇEKİRDEK EKİP VE MÜHENDİSLİK KADROSU
    story.append(Paragraph("31. ÇEKİRDEK EKİP VE MÜHENDİSLİK KADROSU", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; gençliğin getirdiği durdurulamaz enerji, derin yazılım mimarisi ve savunma sanayii disiplinine sahip çekirdek bir kadro tarafından yönetilmektedir:",
        styles['Body']
    ))

    team_data = [
        [
            Paragraph("<b>MURAT FURKAN BAYRAM</b><br/>"
                      "<font size=7 color='#0284C7'><b>Kurucu & Sistem Mimarı (%80 Hisse)</b></font><br/>"
                      "• <b>17 Yaşında</b> genç derin teknoloji kurucusu ve otonomi yazılım mimarı.<br/>"
                      "• Trustia'nın 16.000 satırlık deterministik otonomi çekirdeğinin (Hybrid A*, 3D NDT SLAM, ESKF) tek başına mimarı ve geliştiricisi.<br/>"
                      "• T.C. Savunma Sanayii Başkanlığı'ndan 100/100 Tam Puan tescili ve TÜBİTAK ARBİS Milli Araştırmacı Sicili sahibi.<br/>"
                      "• İTO BTM Fulya Kampüsü sözleşmeli girişimcisi; Dubai World Challenge 1.2M$ yarışması proje lideri.", styles['TableCell']),
            Paragraph("<b>DOĞUKAN BAYRAM</b><br/>"
                      "<font size=7 color='#0284C7'><b>Kurucu Ortak (%20 Hisse)</b></font><br/>"
                      "• Reşit kurucu ortak.<br/>"
                      "• Saha operasyonları, kamu ve kurumsal tedarikçi ilişkileri, lojistik ve finansal süreçlerin yönetimi.<br/>"
                      "• Girişimin tüzel tescil, yatırım sözleşmeleri, fikri mülkiyet ve resmi akreditasyon protokollerinin hukuki koordinatörü.<br/>"
                      "• BTM Fulya Kampüsü ve yatırımcı müzakerelerinin aktif yürütücüsü.", styles['TableCell'])
        ],
        [
            Paragraph("<b>DENİZCAN ÖZCAN</b><br/>"
                      "<font size=7 color='#0284C7'><b>1. Öncelikli Donanım ve Entegrasyon Mühendisi</b></font><br/>"
                      "• <b>ASELSAN Aday Mühendis Havuzu</b> araştırmacısı.<br/>"
                      "• <b>TEKNOFEST Robotaksi Otonom Araç Finalisti</b> (Saha deneyimli).<br/>"
                      "• İstanbul Üniversitesi Cerrahpaşa Elektrik-Elektronik Mühendisliği 4. Sınıf (3.44 GPA).<br/>"
                      "• Kvaser CAN-FD entegrasyonu, kablo demetleri, güç dağıtım panosu ve araç içi gömülü haberleşme uzmanı.", styles['TableCell']),
            Paragraph("<b>MÜHENDİSLİK DANIŞMA VE DESTEK HAVUZU</b><br/>"
                      "<font size=7 color='#0284C7'><b>Akademik ve Sektörel Danışmanlar</b></font><br/>"
                      "• <b>İTO BTM Yatırımcı & Mentor Ağı:</b> Ticari ölçeklenme, Körfez açılımı ve kurumsal filo satış mentörlüğü.<br/>"
                      "• <b>Otomotiv Donanım & CNC Tedarikçileri:</b> 6061 havacılık sınıfı tavan braketleri ve IP67 sızdırmaz pod üreticileri.<br/>"
                      "• <b>Bilişim Vadisi & Teknokent Test Ekibi:</b> Kapalı pist sürüş ve HIL simülasyon doğrulama ortakları.", styles['TableCell'])
        ]
    ]
    t_team = Table(team_data, colWidths=[91*mm, 91*mm])
    t_team.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_team)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>DİSİPLİNLİ MÜHENDİSLİK KÜLTÜRÜ</b>", styles['H2']))
    story.append(Paragraph(
        "Ekip; her gün sabah 09:00 - akşam 22:00 arasında İTO BTM Fulya Kampüsü Ar-Ge merkezinde ve test pistinde kesintisiz çalışarak "
        "Türk mühendisliğinin otonomi alanındaki küresel bayraktarı olma hedefiyle ilerlemektedir.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 33: YATIRIM TEKLİFİ ($500K SAFE) VE 18 AYLIK YOL HARİTASI
    story.append(Paragraph("32. YATIRIM TEKLİFİ ($500K SAFE) VE 18 AYLIK YOL HARİTASI", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_SECONDARY, spaceBefore=0, spaceAfter=5))

    story.append(Paragraph(
        "Trustia AI; ilk 2 adet Hyundai Ioniq 5 test filosunun dönüşümünü tamamlamak, BAE ve Türkiye'de ticari pilotları başlatmak üzere "
        "<b>500.000$ USD Pre-Seed (Tohum Öncesi)</b> yatırım turunu açmıştır:",
        styles['Body']
    ))

    ask_data = [
        [Paragraph("Yatırım Enstrümanı", styles['TableHead']), Paragraph("Yatırım Tutarı", styles['TableHead']), Paragraph("Değerleme Tavanı (Valuation Cap)", styles['TableHead']), Paragraph("İndirim Oranı (Discount)", styles['TableHead'])],
        [Paragraph("<b>SAFE (Post-Money)</b>", styles['TableCellBold']), Paragraph("<b>500.000 $ USD</b>", styles['TableCellBold']), Paragraph("<b>5.000.000 $ (5M$ Cap)</b>", styles['TableCellBold']), Paragraph("<b>%20 İndirim</b>", styles['TableCellBold'])],
    ]
    t_ask = Table(ask_data, colWidths=[42*mm, 45*mm, 55*mm, 40*mm])
    t_ask.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('BACKGROUND', (0,1), (-1,1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_ask)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>FON KULLANIM DAĞILIMI (USE OF FUNDS)</b>", styles['H2']))
    funds_data = [
        [Paragraph("Harcama Kalemi", styles['TableHead']), Paragraph("Pay (%)", styles['TableHead']), Paragraph("Bütçe (USD)", styles['TableHead']), Paragraph("Hedef Çıktı ve Karşılık", styles['TableHead'])],
        [Paragraph("<b>Donanım ve Sensör Alımı</b>", styles['TableCellBold']), Paragraph("%45", styles['TableCellBold']), Paragraph("225.000 $", styles['TableCell']), Paragraph("İlk 2 adet Hyundai Ioniq 5 test filosunun tam dönüşümü ve yedek sensör stoğu.", styles['TableCell'])],
        [Paragraph("<b>Çekirdek Mühendislik Kadrosu</b>", styles['TableCellBold']), Paragraph("%35", styles['TableCellBold']), Paragraph("175.000 $", styles['TableCell']), Paragraph("2 gömülü yazılımcı, 1 SLAM mühendisi ve 1 donanım test teknisyeni maaşları (18 ay).", styles['TableCell'])],
        [Paragraph("<b>Pist ve Saha Test Operasyonları</b>", styles['TableCellBold']), Paragraph("%15", styles['TableCellBold']), Paragraph("75.000 $", styles['TableCell']), Paragraph("Bilişim Vadisi pist kiralama, sigorta, Dubai RTA yarışma saha lojistiği.", styles['TableCell'])],
        [Paragraph("<b>Fikri Mülkiyet & ASIL-D Validasyon</b>", styles['TableCellBold']), Paragraph("%5", styles['TableCellBold']), Paragraph("25.000 $", styles['TableCell']), Paragraph("Uluslararası PCT patent tescilleri ve ISO 26262 fonksiyonel güvenlik denetimleri.", styles['TableCell'])],
        [Paragraph("<b>TOPLAM FON KULLANIMI</b>", styles['TableCellBold']), Paragraph("<b>%100</b>", styles['TableCellBold']), Paragraph("<b>500.000 $</b>", styles['TableCellBold']), Paragraph("<b>18 Aylık Kesintisiz Operasyonel Runway</b>", styles['TableCellBold'])],
    ]
    t_f = Table(funds_data, colWidths=[52*mm, 20*mm, 30*mm, 80*mm])
    t_f.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), C_CARD),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_f)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>18 AYLIK STRATEJİK YOL HARİTASI (MILESTONES)</b>", styles['H2']))
    story.append(Paragraph(
        "• <b>Q4 2026 (Ay 1-3):</b> İlk 2 adet Ioniq 5 test aracının donanım montajının tamamlanması ve Bilişim Vadisi test pistinde 1.000 km otonom sürüş doğrulaması.<br/>"
        "• <b>Q1 2027 (Ay 4-6):</b> BAE Dubai World Challenge saha testlerinin icrası ve ilk 10 araçlık ticari taksi filosu pilot protokolünün imzalanması.<br/>"
        "• <b>Q2 2027 (Ay 7-9):</b> Savunma Sanayii için GPS'siz 3D LiDAR SLAM İKA kiti entegrasyonu ve ASELSAN/SSB PoC gösterimi.<br/>"
        "• <b>Q4 2027 (Ay 10-15):</b> Türkiye ve Dubai'de toplam 85 aktif araca ulaşılması; aylık 40.000$+ AaaS tekrarlayan gelirinin (ARR) yakalanması.<br/>"
        "• <b>Q2 2028 (Ay 16-18):</b> 20M$ değerleme üzerinden Seri-A yatırım turunun açılması ve küresel filo açılımı.",
        styles['Body']
    ))
    story.append(PageBreak())

    # SAYFA 34: İLETİŞİM, GITHUB VE DEMO ÇAĞRISI
    story.append(Paragraph("33. İLETİŞİM, GITHUB DOĞRULAMASI VE DEMO TALEBİ", styles['H1']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=6))

    story.append(Paragraph(
        "Trustia AI; Türk mühendisliğinin deterministik gücünü dünyaya kanıtlamaya ve küresel otonom mobilite devriminde lider oyuncu olmaya hazırdır. "
        "Yatırımcılarımızı, filo işletmecilerini ve teknoloji liderlerini canlı simülasyon, donanım incelemesi ve test sürüşü için yerleşkemize davet ediyoruz:",
        styles['Body']
    ))
    story.append(Spacer(1, 4))

    contact_card = [
        [
            Paragraph("<b>MERKEZ VE KULUÇKA YERLEŞKESİ</b><br/>"
                      "<b>İTO Bilgiyi Ticarileştirme Merkezi (BTM)</b><br/>"
                      "Fulya Kampüsü, Şişli / İstanbul<br/>"
                      "<i>(Hafta içi 09:00 - 18:00 Ar-Ge & Toplantı)</i>", styles['TableCellBold']),
            Paragraph("<b>DOĞRUDAN İLETİŞİM BİLGİLERİ</b><br/>"
                      "<b>Telefon / WhatsApp:</b> +90 537 064 04 60<br/>"
                      "<b>Kurumsal E-posta:</b> kariyer@trustia.com.tr<br/>"
                      "<b>Genel İletişim:</b> info@trustia.com.tr", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>DİJİTAL VE KOD PLATFORMLARI</b><br/>"
                      "<b>Resmi Web Sitesi:</b> <font color='#0284C7'><u>https://trustia.com.tr</u></font><br/>"
                      "<b>Resmi Kod Deposu:</b> <font color='#0284C7'><u>https://github.com/Trustia/Trustia</u></font><br/>"
                      "<b>Teknoloji ve Dokümantasyon:</b> <font color='#0284C7'><u>https://trustia.com.tr</u></font>", styles['TableCellBold']),
            Paragraph("<b>RESMİ KURUMSAL TESCİLLER</b><br/>"
                      "<b>T.C. SSB Tescil No:</b> L2zPtN4X1ZJ (100/100 Tam Puan)<br/>"
                      "<b>KOSGEB Sicil No:</b> KSB01UGE0115153370<br/>"
                      "<b>TÜBİTAK ARBİS No:</b> TBTK-0229-6571", styles['TableCellBold'])
        ]
    ]
    t_c_card = Table(contact_card, colWidths=[91*mm, 91*mm])
    t_c_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 1, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_c_card)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>CANLI GÖSTERİM VE TEKNİK BRİFİNG TALEBİ</b>", styles['H2']))
    story.append(Paragraph(
        "BTM Fulya Kampüsümüzde veya Bilişim Vadisi'nde düzenlenecek 45 dakikalık birebir sunumda:<br/>"
        "1. <b>NVIDIA Jetson AGX Orin</b> üzerinde 100Hz frekansta koşan deterministik C++ otonomi döngüsünün canlı izlenmesi.<br/>"
        "2. <b>Ouster OS2-128 LiDAR</b> ve <b>Continental Radar</b> veri akışının Rviz2 ve Taktik C2 konsolunda 3 boyutlu incelenmesi.<br/>"
        "3. <b>Webots ve ROS2</b> simülasyonunda tünel, sis ve yayalarla dolu zorlu kentsel senaryoların gerçek zamanlı yönetimi.<br/>"
        "4. Kvaser CAN-FD donanımı üzerinden simüle edilen araç aktüatörlerine direksiyon ve fren komutlarının doğrulanması sunulmaktadır.",
        styles['Body']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>© 2026 TRUSTIA AI — TÜM HAKLARI SAKLIDIR.</b><br/>"
        "<font size=7 color='#64748B'>Bu belge ticari ve teknik gizlilik derecesine sahiptir. İTO BTM Fulya Kampüsü bünyesinde tescilli Trustia AI kurucuları Murat Furkan Bayram ve Doğukan Bayram'ın yazılı izni olmadan kısmen veya tamamen çoğaltılamaz, üçüncü şahıslara aktarılamaz.</font>",
        ParagraphStyle('FooterNotice', fontName='Arial', fontSize=7, leading=9.5, textColor=C_MUTED, alignment=1)
    ))

    build_pdf(out_path, story)

def main():
    cikti_dir = r"C:\Users\Murat\Desktop\Çıktı"
    btm_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\BTM_Gorusme_Cikti_Dosyasi"
    pitch_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Pitch_Decks"

    for d in [cikti_dir, btm_dir, pitch_dir]:
        os.makedirs(d, exist_ok=True)

    target_name = "00_Trustia_AI_Master_Yatirimci_Sunumu_Pitch_Deck_2026.pdf"
    p0 = os.path.join(cikti_dir, target_name)
    
    print("[INFO] Generating 34-page comprehensive master pitch deck...")
    generate_master_dossier(p0)

    # Copy to target folders
    shutil.copy(p0, os.path.join(pitch_dir, target_name))
    shutil.copy(p0, os.path.join(btm_dir, target_name))
    print("[SUCCESS] Master pitch deck successfully deployed to all directories!")

if __name__ == "__main__":
    main()
