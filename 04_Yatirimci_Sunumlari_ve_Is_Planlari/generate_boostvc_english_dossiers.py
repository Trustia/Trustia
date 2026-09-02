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
font_regular = 'C:/Windows/Fonts/arial.ttf'
font_bold = 'C:/Windows/Fonts/arialbd.ttf'
font_italic = 'C:/Windows/Fonts/ariali.ttf'

pdfmetrics.registerFont(TTFont('Arial', font_regular))
pdfmetrics.registerFont(TTFont('Arial-Bold', font_bold))
pdfmetrics.registerFont(TTFont('Arial-Italic', font_italic))

# Silicon Valley Dark & Clean Palette
C_PRIMARY = colors.HexColor('#0A192F')   # Deep Navy
C_ACCENT = colors.HexColor('#0284C7')    # Electric Tech Blue
C_CYAN = colors.HexColor('#0EA5E9')      # Vibrant Sky
C_DARK = colors.HexColor('#0F172A')      # Slate 900
C_MUTED = colors.HexColor('#64748B')     # Slate 500
C_LIGHT_BG = colors.HexColor('#F8FAFC') # Slate 50
C_CARD = colors.HexColor('#F1F5F9')      # Slate 100
C_BORDER = colors.HexColor('#CBD5E1')    # Slate 300
C_SUCCESS = colors.HexColor('#059669')   # Emerald Green
C_WHITE = colors.white

class NumberedCanvasEN(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvasEN, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super(NumberedCanvasEN, self).showPage()
        super(NumberedCanvasEN, self).save()

    def draw_decorations(self, page_count):
        self.saveState()
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont('Arial-Bold', 8)
            self.setFillColor(C_PRIMARY)
            self.drawString(14*mm, 285*mm, "TRUSTIA AI")
            self.setFont('Arial', 8)
            self.setFillColor(C_MUTED)
            self.drawString(34*mm, 285*mm, "|  SAE Level-4 Autonomous Mobility  •  Confidential Investor Dossier")
            self.drawRightString(196*mm, 285*mm, "September 2026")
            
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.6)
            self.line(14*mm, 282*mm, 196*mm, 282*mm)

        # Footer (all pages)
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.6)
        self.line(14*mm, 14*mm, 196*mm, 14*mm)
        
        self.setFont('Arial-Bold', 7.5)
        self.setFillColor(C_PRIMARY)
        self.drawString(14*mm, 10*mm, "TRUSTIA AI TECHNOLOGIES")
        self.setFont('Arial', 7.5)
        self.setFillColor(C_MUTED)
        self.drawString(56*mm, 10*mm, "|  Autonomous Vehicle Retrofit Stack  •  trustia.com.tr")
        self.drawRightString(196*mm, 10*mm, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def get_styles_en():
    base = getSampleStyleSheet()
    styles = {}
    styles['Title'] = ParagraphStyle(
        'TitleEN', parent=base['Normal'], fontName='Arial-Bold', fontSize=18, leading=22, textColor=C_PRIMARY, spaceAfter=4
    )
    styles['Subtitle'] = ParagraphStyle(
        'SubEN', parent=base['Normal'], fontName='Arial', fontSize=9.5, leading=13.5, textColor=C_ACCENT, spaceAfter=10
    )
    styles['H1'] = ParagraphStyle(
        'H1EN', parent=base['Normal'], fontName='Arial-Bold', fontSize=11, leading=15, textColor=C_PRIMARY, spaceBefore=8, spaceAfter=4
    )
    styles['H2'] = ParagraphStyle(
        'H2EN', parent=base['Normal'], fontName='Arial-Bold', fontSize=9, leading=12, textColor=C_ACCENT, spaceBefore=6, spaceAfter=2
    )
    styles['Body'] = ParagraphStyle(
        'BodyEN', parent=base['Normal'], fontName='Arial', fontSize=8, leading=11.5, textColor=C_DARK, spaceAfter=4
    )
    styles['Badge'] = ParagraphStyle(
        'BadgeEN', parent=base['Normal'], fontName='Arial-Bold', fontSize=7.5, leading=10, textColor=C_SUCCESS
    )
    styles['TableCell'] = ParagraphStyle(
        'CellEN', parent=base['Normal'], fontName='Arial', fontSize=7.5, leading=10, textColor=C_DARK
    )
    styles['TableCellBold'] = ParagraphStyle(
        'CellBoldEN', parent=base['Normal'], fontName='Arial-Bold', fontSize=7.5, leading=10, textColor=C_PRIMARY
    )
    styles['TableHead'] = ParagraphStyle(
        'HeadEN', parent=base['Normal'], fontName='Arial-Bold', fontSize=7.5, leading=10, textColor=C_WHITE
    )
    styles['Caption'] = ParagraphStyle(
        'CapEN', parent=base['Normal'], fontName='Arial-Bold', fontSize=6.5, leading=8.5, textColor=C_PRIMARY, alignment=1
    )
    return styles

# =====================================================================
# 1. MASTER INVESTOR PITCH DECK (ENGLISH)
# =====================================================================
def generate_pitch_deck_en(out_path):
    styles = get_styles_en()
    story = []

    # Title & Metadata
    story.append(Paragraph("TRUSTIA AI — MASTER INVESTOR PITCH DECK (2026)", styles['Title']))
    story.append(Paragraph("Turnkey SAE Level-4 Autonomous Driving Retrofit Kit & Deterministic Autonomy Stack for Commercial EVs", styles['Subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_ACCENT, spaceBefore=0, spaceAfter=8))

    # Highlights Box
    grid_data = [
        [
            Paragraph("<b>Founder & Chief Architect:</b><br/>Murat Furkan Bayram (Age 17, 80% Equity)<br/>"
                      "<b>Hardware & Integration Lead:</b><br/>Denizcan Ozcan (ASELSAN Candidate Eng., TEKNOFEST Finalist)", styles['TableCell']),
            Paragraph("<b>The Pre-Seed Ask:</b><br/><b>$500,000 USD</b> on a $5M Post-Money Cap SAFE<br/>"
                      "<b>Core Entity & Incubation:</b><br/>Trustia AI (ITO BTM Fulya Campus Resident)", styles['TableCell']),
            Paragraph("<b>Engineering Maturity:</b><br/>16,000 LOC C++/Python, <b>1,301/1,301 Tests (100%)</b><br/>"
                      "<b>Global Track Record:</b><br/>Dubai RTA $1.2M Challenge Official Entry (Submitted)", styles['TableCell'])
        ]
    ]
    t_grid = Table(grid_data, colWidths=[62*mm, 62*mm, 58*mm])
    t_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_grid)
    story.append(Spacer(1, 6))

    # 1. The Problem & Market
    story.append(Paragraph("1. THE $118B PROBLEM: BESPOKE ROBOTAXIS ARE TOO EXPENSIVE TO SCALE", styles['H1']))
    story.append(Paragraph(
        "<b>The Flaw in Waymo & Cruise:</b> Industry giants spend <b>$250,000 to $350,000+</b> manufacturing bespoke autonomous pods from scratch. Because of massive capital expenditure (CAPEX) and punishing vehicle depreciation, driverless fleets cannot scale commercially to emerging markets, taxi operators, or campus shuttles.<br/>"
        "<b>Market Urgency:</b> The global autonomous vehicle market will reach <b>$118 Billion by 2030</b>. Major municipalities (such as Dubai's legal mandate for 25% driverless transport by 2030) urgently need low-cost, rapidly deployable autonomous solutions.",
        styles['Body']
    ))

    # 2. The Solution
    story.append(Paragraph("2. THE TRUSTIA SOLUTION: $35,000 MODULAR RETROFIT IN 48 HOURS", styles['H1']))
    story.append(Paragraph(
        "Trustia AI turns mass-produced electric passenger vehicles (specifically the <b>Hyundai Ioniq 5 E-GMP platform</b>) into commercial SAE Level-4 Robotaxis in under 48 hours. By interfacing directly with the vehicle's CAN-FD drive-by-wire system without cutting or modifying the structural chassis, Trustia delivers a <b>70% CAPEX reduction</b> and a full <b>14-month payback period</b> for fleet operators.",
        styles['Body']
    ))

    # 3. Deep Tech Software
    story.append(Paragraph("3. PROPRIETARY TECHNOLOGY: 16,000 LOC DETERMINISTIC CORE (ZERO BLACK BOX)", styles['H1']))
    story.append(Paragraph(
        "While traditional end-to-end neural nets suffer from hallucination and unpredictability, Trustia employs a mathematically provable, deterministic architecture:<br/>"
        "• <b>Kinematic Hybrid A* Path Planning:</b> Solves non-holonomic vehicle dynamics (Ackermann steering constraints, curvature, slip angles) in <b>under 40ms</b>.<br/>"
        "• <b>GPS-Denied Centimeter SLAM:</b> 400Hz Error-State Kalman Filter (ESKF) fused with 3D Normal Distributions Transform (NDT) LiDAR SLAM provides 5cm localization in urban canyons, tunnels, and GPS-jammed zones.<br/>"
        "• <b>1,301 Automated Tests:</b> Rigorous CI/CD test suite spanning unit algorithms, hardware-in-the-loop (HIL) simulators, and CAN-FD fault injections at 100% pass rate.<br/>"
        "• <b>ISO 26262 ASIL-D Safety:</b> Hardware E-Stop and automated Minimal Risk Maneuver (MRM) ensures safe curbside pulling in case of sensor degradation.",
        styles['Body']
    ))

    # 4. Hardware BOM
    story.append(Paragraph("4. PRODUCTION-READY SENSOR & COMPUTE SUITE", styles['H1']))
    hw_table_data = [
        [Paragraph("Subsystem", styles['TableHead']), Paragraph("Component / Model", styles['TableHead']), Paragraph("Key Specifications & Function", styles['TableHead'])],
        [Paragraph("Roof 3D LiDAR", styles['TableCellBold']), Paragraph("Ouster OS2-128 Rev 7", styles['TableCell']), Paragraph("128 laser channels, 240m range, 2.62M pts/sec, 360° primary point cloud", styles['TableCell'])],
        [Paragraph("Blind Spot LiDAR (2x)", styles['TableCellBold']), Paragraph("Livox Mid-360", styles['TableCell']), Paragraph("360°x59° FOV, front/rear bumper zero blind-spot curb & pedestrian tracking", styles['TableCell'])],
        [Paragraph("Long-Range Radars (2x)", styles['TableCellBold']), Paragraph("Continental ARS 408-21 (77GHz)", styles['TableCell']), Paragraph("250m range, FMCW all-weather penetration (heavy fog, dust storms, desert heat)", styles['TableCell'])],
        [Paragraph("Perception Cameras (4x)", styles['TableCellBold']), Paragraph("Leopard Sony IMX390 GMSL2", styles['TableCell']), Paragraph("120dB HDR automotive grade, LED flicker mitigation, 360° vision", styles['TableCell'])],
        [Paragraph("Central AI Compute", styles['TableCellBold']), Paragraph("NVIDIA Jetson AGX Orin 64GB", styles['TableCell']), Paragraph("275 TOPS INT8, Seeed J501 industrial carrier, 100Hz real-time deterministic loop", styles['TableCell'])],
        [Paragraph("Drive-by-Wire Bridge", styles['TableCellBold']), Paragraph("Kvaser U100 CAN-FD", styles['TableCell']), Paragraph("5 Mbps high-speed CAN-FD, galvanic isolation, LKAS/SCC steering & brake injection", styles['TableCell'])],
    ]
    t_hw = Table(hw_table_data, colWidths=[38*mm, 52*mm, 92*mm])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.8, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_hw)
    story.append(Spacer(1, 6))

    # 5. Unit Economics
    story.append(Paragraph("5. UNIT ECONOMICS & DUAL-LAYER REVENUE MODEL", styles['H1']))
    story.append(Paragraph(
        "<b>1. Hardware Kit Sales (Upfront CAPEX):</b> $35,000 per retrofit kit (35% gross profit margin).<br/>"
        "<b>2. Autonomy-as-a-Service (AaaS Recurring ARR):</b> $0.18/km or $450/month per vehicle for tele-operations, continuous OTA updates, and HD map syncing.<br/>"
        "<b>Fleet ROI Impact:</b> Each retrofitted vehicle generates <b>$55,500/year in net operating savings</b> by eliminating driver shift costs, achieving full capital payback in 14 months.",
        styles['Body']
    ))

    # 6. Investment Ask
    story.append(Paragraph("6. THE INVESTMENT ASK: $500,000 PRE-SEED", styles['H1']))
    story.append(Paragraph(
        "We are raising <b>$500,000 USD on a $5M Post-Money Cap SAFE</b> to fund our 18-month operational runway:<br/>"
        "• <b>45% Hardware & Sensor Procurement:</b> Full conversion of our first 2 Hyundai Ioniq 5 proving ground test vehicles.<br/>"
        "• <b>35% Core Engineering Talent:</b> Embedded systems, SLAM, and ROS2 engineers.<br/>"
        "• <b>15% Proving Ground & Track Testing:</b> Live validation on closed courses in Silicon Valley and Dubai RTA proving grounds.<br/>"
        "• <b>5% ISO 26262 ASIL-D Certification & IP:</b> Global patent filings and safety audits.",
        styles['Body']
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Contact:</b> Murat Furkan Bayram (Founder & CEO) | kariyer@trustia.com.tr | +90 537 064 0460 | trustia.com.tr", styles['Badge']))

    doc = SimpleDocTemplate(out_path, pagesize=A4, leftMargin=14*mm, rightMargin=14*mm, topMargin=16*mm, bottomMargin=16*mm)
    doc.build(story, canvasmaker=NumberedCanvasEN)
    print(f"[OK] Generated: {out_path}")

# =====================================================================
# 2. HYUNDAI IONIQ 5 LEVEL-4 PHOTO MASTER PLAN (ENGLISH)
# =====================================================================
def generate_photo_master_plan_en(out_path):
    img_base = r"c:\Users\Murat\Desktop\Trustia\06_Medya_Gorsel_ve_Tanitim_Videolari\Hyundai_Ioniq_5_Test_Araci"
    img1 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_1.png")
    img2 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_2.png")
    img3 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_3.png")
    img4 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_4.png")
    img5 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_5.png")
    img6 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_6.png")
    img7 = os.path.join(img_base, "Hyundai_Ioniq5_Foto_7.png")

    styles = get_styles_en()
    story = []

    # Header
    header_data = [
        [
            Paragraph("<b>TRUSTIA AI</b><br/><font size=6.5 color='#0284C7'>AUTONOMOUS SYSTEMS & DEEP TECH</font>", styles['Body']),
            Paragraph("<b>DOC ID:</b> TRUSTIA-ENG-IONIQ5-L4-EN<br/><b>DATE:</b> September 2, 2026<br/><b>STATUS:</b> OFFICIAL INVESTOR & TECH DOSSIER", ParagraphStyle('MetaHEN', fontName='Arial', fontSize=6.5, leading=9, alignment=2, textColor=C_MUTED))
        ]
    ]
    t_head = Table(header_data, colWidths=[100*mm, 82*mm])
    t_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_head)
    story.append(Spacer(1, 1.5*mm))
    story.append(HRFlowable(width="100%", thickness=1.2, color=C_ACCENT, spaceBefore=0, spaceAfter=2.5*mm))

    story.append(Paragraph("HYUNDAI IONIQ 5 LEVEL-4 ROBOTAXI RETROFIT MASTER PLAN", styles['Title']))
    story.append(Paragraph("E-GMP Architecture Integration, 27-Component Validated BOM, CAN-FD Drive-by-Wire & Field Engineering Handbook", styles['Subtitle']))
    story.append(Spacer(1, 2*mm))

    # KPI Bar
    kpi_data = [
        [
            Paragraph("<font size=5.5 color='#64748B'>AUTONOMY ENGINE</font><br/><b>16,000 Lines</b><br/><font size=5.5 color='#059669'>100% Custom C++/Python</font>", styles['Body']),
            Paragraph("<font size=5.5 color='#64748B'>VALIDATION SUITE</font><br/><b>1,301 / 1,301</b><br/><font size=5.5 color='#059669'>100% CI Zero Defect</font>", styles['Body']),
            Paragraph("<font size=5.5 color='#64748B'>RETROFIT HARDWARE BOM</font><br/><b>$32,800 USD</b><br/><font size=5.5 color='#0284C7'>Complete Turnkey Kit</font>", styles['Body']),
            Paragraph("<font size=5.5 color='#64748B'>TURNKEY ROBOTAXI</font><br/><b>$88,000 USD</b><br/><font size=5.5 color='#0A192F'>Vehicle + Sensor Suite</font>", styles['Body'])
        ]
    ]
    t_kpi = Table(kpi_data, colWidths=[45.5*mm, 45.5*mm, 45.5*mm, 45.5*mm])
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.6, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.4, C_BORDER),
        ('PADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_kpi)
    story.append(Spacer(1, 2.5*mm))

    # Hero Image & Overview
    hero_img = RLImage(img1, width=72*mm, height=52*mm)
    summary_text = Paragraph(
        "<b>1. EXECUTIVE SUMMARY & PLATFORM SELECTION</b><br/>"
        "This master specification outlines the physical and algorithmic integration of the <b>Trustia AI</b> SAE Level-4 autonomy stack onto the <b>Hyundai Ioniq 5 (E-GMP)</b> electric platform.<br/><br/>"
        "<b>Global Validation:</b> The Hyundai Ioniq 5 is the premier platform chosen by the world's leading autonomous operators: <b>Motional (Hyundai & Aptiv JV)</b> and <b>Alphabet's Waymo</b> for their commercial robotaxi fleets. Trustia's hardware architecture, sensor positioning, and CAN-FD actuator controls match Motional and Waymo deployment standards with 100% fidelity.",
        styles['Body']
    )
    hero_table = Table([[summary_text, [hero_img, Paragraph("Figure 1: Hyundai Ioniq 5 Matte Grey Advance Test Platform", styles['Caption'])]]], colWidths=[106*mm, 76*mm])
    hero_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(hero_table)
    story.append(Spacer(1, 2*mm))

    # Core Specs Table
    spec_data = [
        [Paragraph("Architectural Layer", styles['TableHead']), Paragraph("Selected Hardware & Vendor", styles['TableHead']), Paragraph("Core Function & Protocol", styles['TableHead'])],
        [Paragraph("Central AI Compute", styles['TableCellBold']), Paragraph("NVIDIA Jetson AGX Orin 64GB + Seeed J501", styles['TableCell']), Paragraph("275 TOPS INT8, 100Hz real-time deterministic control, GMSL2 PoC", styles['TableCell'])],
        [Paragraph("Ultra-Fast Logging", styles['TableCellBold']), Paragraph("Samsung 990 PRO 4TB M.2 NVMe SSD", styles['TableCell']), Paragraph("7,450 MB/s read, 350 MB/sec continuous rosbag2 black-box telemetry", styles['TableCell'])],
        [Paragraph("Primary 3D SLAM", styles['TableCellBold']), Paragraph("Ouster OS2-128 Rev 7 3D LiDAR (128 Channels)", styles['TableCell']), Paragraph("240m range, 2.62M pts/sec, 360° point cloud, 3D NDT pose graph", styles['TableCell'])],
        [Paragraph("Blind-Spot & Curb", styles['TableCellBold']), Paragraph("2x Livox Mid-360 3D LiDAR (Front/Rear Bumper)", styles['TableCell']), Paragraph("360°x59° ultra-wide FOV, zero blind spots for curbs and pedestrians", styles['TableCell'])],
        [Paragraph("360° Vision", styles['TableCellBold']), Paragraph("4x Leopard Sony IMX390 GMSL2 HDR Cameras", styles['TableCell']), Paragraph("120dB dynamic range, LED flicker mitigation, IP67 waterproof", styles['TableCell'])],
        [Paragraph("All-Weather Radar", styles['TableCellBold']), Paragraph("2x Continental ARS 408-21 77GHz FMCW", styles['TableCell']), Paragraph("250m range, robust tracking through sandstorms, rain, and heavy fog", styles['TableCell'])],
        [Paragraph("Centimeter RTK GNSS", styles['TableCellBold']), Paragraph("Septentrio mosaic-go Heading + 2x TOP500", styles['TableCell']), Paragraph("Dual-antenna heading, stationary compass fix, RTK centimeter accuracy", styles['TableCell'])],
        [Paragraph("Drive-by-Wire Bridge", styles['TableCellBold']), Paragraph("Kvaser U100 CAN-FD + 120Ω Terminator", styles['TableCell']), Paragraph("100Hz LKAS_FD steering angle & 50Hz SCC_FD throttle/brake injection", styles['TableCell'])],
        [Paragraph("Hardware E-Stop", styles['TableCellBold']), Paragraph("Schneider Electric E-Stop + ELO 80A Relay", styles['TableCell']), Paragraph("Instant 10ms mechanical power cutoff, ASIL-D functional safety", styles['TableCell'])],
    ]
    t_spec = Table(spec_data, colWidths=[38*mm, 72*mm, 72*mm])
    t_spec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.4, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('PADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_spec)

    story.append(PageBreak())

    # ================= PAGE 2: VEHICLE EXTERIOR SENSOR MOUNTING =================
    story.append(Paragraph("2. PHYSICAL SENSOR INTEGRATION & EXTERIOR MOUNTING", styles['H1']))
    story.append(Paragraph(
        "Sensor placement on the Hyundai Ioniq 5 is optimized for comprehensive 360-degree overlapping coverage, zero structural drilling, and streamlined aerodynamics.",
        styles['Body']
    ))
    story.append(Spacer(1, 1.5*mm))

    img_f2 = RLImage(img2, width=88*mm, height=58*mm)
    img_f3 = RLImage(img3, width=88*mm, height=58*mm)
    grid_ext = Table([
        [
            [img_f2, Paragraph("Figure 2: Front 3/4 Perspective — Roof LiDAR & Grille Radar Integration", styles['Caption'])],
            [img_f3, Paragraph("Figure 3: Side Profile — 3.00m Wheelbase Roof Rack Crossbars & GMSL2 Mirrors", styles['Caption'])]
        ]
    ], colWidths=[91*mm, 91*mm])
    grid_ext.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(grid_ext)
    story.append(Spacer(1, 2.5*mm))

    img_f4 = RLImage(img4, width=88*mm, height=58*mm)
    img_f5 = RLImage(img5, width=88*mm, height=58*mm)
    grid_rear = Table([
        [
            [img_f4, Paragraph("Figure 4: Rear 3/4 View — Bumper Livox Mid-360 & Septentrio Dual GNSS Antennas", styles['Caption'])],
            [img_f5, Paragraph("Figure 5: Rear Straight View — Tailgate GMSL2 Camera & Sub-Trunk Compute Routing", styles['Caption'])]
        ]
    ], colWidths=[91*mm, 91*mm])
    grid_rear.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(grid_rear)
    story.append(Spacer(1, 2*mm))

    story.append(Paragraph("3. CABIN & PASSENGER EXPERIENCE ARCHITECTURE", styles['H1']))
    img_f6 = RLImage(img6, width=88*mm, height=56*mm)
    img_f7 = RLImage(img7, width=88*mm, height=56*mm)
    grid_int = Table([
        [
            [img_f6, Paragraph("Figure 6: Front Cockpit — Dual 12.3-inch Displays, E-Stop Button & HUD", styles['Caption'])],
            [img_f7, Paragraph("Figure 7: Rear Passenger Space — 10.1-inch Interactive Passenger Ride Terminal", styles['Caption'])]
        ]
    ], colWidths=[91*mm, 91*mm])
    grid_int.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(grid_int)

    story.append(PageBreak())

    # ================= PAGE 3: DRIVE-BY-WIRE & TESTING ROADMAP =================
    story.append(Paragraph("4. CAN-FD DRIVE-BY-WIRE (DBW) REVERSE-ENGINEERING", styles['H1']))
    story.append(Paragraph(
        "Lateral and longitudinal control is commanded over the Hyundai Ioniq 5 CAN-FD bus via the <b>Kvaser U100</b> interface with 120Ω bus termination:<br/>"
        "• <b>Lateral Steering Injection:</b> `LKAS11` / `LKAS_FD` bus messages broadcast at 100Hz with dynamic checksum calculation and rolling counters.<br/>"
        "• <b>Longitudinal Acceleration & Braking:</b> `SCC11` / `ACC_FD` messages broadcast at 50Hz for smooth target jerk and velocity tracking.<br/>"
        "• <b>Driver Override Handshake:</b> Instant capacitive steering wheel torque sensors automatically disengage autonomous actuation if human operator applies >1.5 Nm.",
        styles['Body']
    ))
    story.append(Spacer(1, 2*mm))

    story.append(Paragraph("5. 4-PHASE PROVING GROUND TEST PROTOCOL", styles['H1']))
    test_data = [
        [Paragraph("Phase", styles['TableHead']), Paragraph("Operational Domain", styles['TableHead']), Paragraph("Test Scope & Criteria", styles['TableHead']), Paragraph("Safety Benchmark", styles['TableHead'])],
        [Paragraph("<b>Phase 1</b> (Sim/HIL)", styles['TableCellBold']), Paragraph("Webots & CARLA", styles['TableCell']), Paragraph("500+ hours simulation matrix with edge-case pedestrian jaywalking and synthetic sensor noise", styles['TableCell']), Paragraph("Zero collisions, 100% pass", styles['Badge'])],
        [Paragraph("<b>Phase 2</b> (Static)", styles['TableCellBold']), Paragraph("Laboratory Bench", styles['TableCell']), Paragraph("LiDAR-to-Camera CharuCo extrinsic calibration, RTK heading lock, 12V thermal regulation", styles['TableCell']), Paragraph("Extrinsics error < 2cm", styles['TableCell'])],
        [Paragraph("<b>Phase 3</b> (Closed Track)", styles['TableCellBold']), Paragraph("Bilisim Vadisi / Dubai Test Track", styles['TableCell']), Paragraph("Obstacle slalom at 60 km/h, emergency stops from 80 km/h, roundabout navigation", styles['TableCell']), Paragraph("ISO 26262 ASIL-D MRM", styles['Badge'])],
        [Paragraph("<b>Phase 4</b> (Public Pilot)", styles['TableCellBold']), Paragraph("Commercial Robotaxi Pilot", styles['TableCell']), Paragraph("Commercial pilot deployment with safety driver in urban mixed traffic", styles['TableCell']), Paragraph("Permitted Autonomous Pilot", styles['TableCell'])],
    ]
    t_test = Table(test_data, colWidths=[28*mm, 42*mm, 80*mm, 32*mm])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.4, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT_BG]),
        ('PADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 4*mm))

    # Sign-off box
    sign_box = [
        [
            Paragraph("<b>CHIEF ARCHITECT & CEO</b><br/>Murat Furkan Bayram<br/><font size=5.5 color='#64748B'>Founder & Systems Architect<br/>Trustia AI</font>", styles['Body']),
            Paragraph("<b>HARDWARE & TEST LEAD</b><br/>Denizcan Ozcan<br/><font size=5.5 color='#64748B'>Hardware & Integration Engineer<br/>ASELSAN & TEKNOFEST Finalist</font>", styles['Body']),
            Paragraph("<b>INSTITUTIONAL ACCREDITATION</b><br/>SSB & ITO BTM Verified<br/><font size=5.5 color='#64748B'>SSB 100/100 Score • Dubai World Challenge<br/>TUBITAK National Researcher</font>", styles['Body'])
        ]
    ]
    t_sign = Table(sign_box, colWidths=[60.6*mm, 60.6*mm, 60.6*mm])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CARD),
        ('BOX', (0,0), (-1,-1), 0.8, C_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.4, C_BORDER),
        ('PADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_sign)

    doc = SimpleDocTemplate(out_path, pagesize=A4, leftMargin=14*mm, rightMargin=14*mm, topMargin=16*mm, bottomMargin=16*mm)
    doc.build(story, canvasmaker=NumberedCanvasEN)
    print(f"[OK] Generated: {out_path}")

def main():
    cikti_dir = r"C:\Users\Murat\Desktop\Çıktı"
    pitch_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Pitch_Decks"
    tech_dir = r"c:\Users\Murat\Desktop\Trustia\04_Yatirimci_Sunumlari_ve_Is_Planlari\Teknik_ve_Organizasyon"

    # File 1: Master Investor Pitch Deck (EN)
    p1 = os.path.join(cikti_dir, "Trustia_AI_Master_Investor_Pitch_Deck_2026_EN.pdf")
    generate_pitch_deck_en(p1)
    shutil.copy(p1, os.path.join(pitch_dir, "Trustia_AI_Master_Investor_Pitch_Deck_2026_EN.pdf"))

    # File 2: Hyundai Ioniq 5 Level-4 Photo Master Plan (EN)
    p2 = os.path.join(cikti_dir, "Trustia_AI_Hyundai_Ioniq5_Level4_Photo_Master_Plan_EN.pdf")
    generate_photo_master_plan_en(p2)
    shutil.copy(p2, os.path.join(tech_dir, "Trustia_AI_Hyundai_Ioniq5_Level4_Photo_Master_Plan_EN.pdf"))
    shutil.copy(p2, os.path.join(pitch_dir, "Trustia_AI_Hyundai_Ioniq5_Level4_Photo_Master_Plan_EN.pdf"))

    print("[SUCCESS] Both English dossiers generated flawlessly!")

if __name__ == "__main__":
    main()
