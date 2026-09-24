import os
import shutil
from PIL import Image, ImageDraw, ImageFont

bg_dir = r'C:\Users\Murat\Desktop\Trustia\Kurumsal\Sunumlar\clean_backgrounds'
out_dir = r'C:\Users\Murat\Desktop\Trustia\Kurumsal\Sunumlar\customized_pages'
os.makedirs(out_dir, exist_ok=True)

font_bold_path = r'C:\Windows\Fonts\segoeuib.ttf'
font_reg_path = r'C:\Windows\Fonts\segoeui.ttf'

def get_font(size, bold=False):
    return ImageFont.truetype(font_bold_path if bold else font_reg_path, size)

NAVY = (11, 37, 69)
GREEN = (3, 151, 102)
SLATE = (71, 85, 105)
WHITE = (255, 255, 255)
LIGHT_GREEN = (74, 222, 128)
MINT_LIGHT = (240, 253, 244)
DARK_BLUE_TEMPLATE = (32, 41, 79)
LIGHT_GREEN_TEMPLATE = (162, 211, 117)

# ==========================================
# PAGE 1: KAPAK
# ==========================================
p1 = Image.open(f'{bg_dir}/bg_page_1.png')
d1 = ImageDraw.Draw(p1)
d1.text((220, 420), 'TRUSTIA AI', font=get_font(105, True), fill=NAVY)
d1.text((220, 560), 'Yerli ve Bağımsız Seviye-4 Otonom Sürüş İşletim Sistemi', font=get_font(44, True), fill=GREEN)
d1.text((220, 630), 'Ticari Araç ve Robotaksi Filoları için Tak-Çalıştır Otonomi Çekirdeği', font=get_font(32, False), fill=SLATE)
d1.line([(220, 695), (1450, 695)], fill=GREEN, width=4)
d1.text((220, 725), 'Murat Furkan Bayram  •  Kurucu & CEO / Sistem Mimarı (%100 Hisse)', font=get_font(34, True), fill=NAVY)
d1.text((220, 785), 'Denizcan Özcan  •  Baş Donanım ve Entegrasyon Mühendisi', font=get_font(30, False), fill=SLATE)
d1.text((220, 860), 'ASIL-D Emniyet   |   16.000+ Kod   |   1.301 Test   |   ASELSAN Adayı', font=get_font(30, True), fill=GREEN)
d1.text((220, 930), 'TİM-TEB Girişim Evi Denizli Start Up Jüri Sunumu  •  25 Eylül 2026', font=get_font(26, False), fill=(100, 116, 139))
p1.save(f'{out_dir}/page_1.png')

# ==========================================
# PAGE 2: PROBLEM
# ==========================================
p2 = Image.open(f'{bg_dir}/bg_page_2.png')
d2 = ImageDraw.Draw(p2)
d2.text((516, 168), 'Problem', font=get_font(80, True), fill=NAVY)
left_text_2 = (
    'Küresel mobilite ve lojistik sektörü 3 kritik darboğazla karşı karşıya:\n\n'
    '• Sürücü yorgunluğu ve insan kaynaklı kazalar (yüksek can/mal kaybı riski),\n\n'
    '• Şoför bulma krizi ve %60\'ı aşan filo operasyon maliyetleri,\n\n'
    '• Otonom araç yazılımında yabancı tekellere tam dışa bağımlılık.\n\n'
    'Trustia, bu darboğazları yerli derin teknoloji otonomi çekirdeği ile çözmektedir.'
)
d2.text((510, 360), left_text_2, font=get_font(32, False), fill=SLATE, spacing=10)

# Capsule 1: White circle at (1767, 392), Green text at x=1900
d2.text((1767, 392), '1', font=get_font(64, True), fill=NAVY, anchor="mm")
d2.text((1900, 340), '%94 İnsan Hatası & Kaza Riski', font=get_font(34, True), fill=WHITE)
d2.text((1900, 395), 'Ölümcül kazaların %94\'ü yorgunluk\nve dikkatsizlik kaynaklıdır.', font=get_font(24, False), fill=MINT_LIGHT, spacing=4)

# Capsule 2: White circle at (1918, 670), Green text at x=2050
d2.text((1918, 670), '2', font=get_font(64, True), fill=NAVY, anchor="mm")
d2.text((2050, 620), 'Şoför Açığı & %60 Filo Maliyeti', font=get_font(34, True), fill=WHITE)
d2.text((2050, 675), 'Lojistikte en büyük gider kalemi\nsürücü maaşları ve duruşlardır.', font=get_font(24, False), fill=MINT_LIGHT, spacing=4)

# Capsule 3: White circle at (1880, 948), Green text at x=2010
d2.text((1880, 948), '3', font=get_font(64, True), fill=NAVY, anchor="mm")
d2.text((2010, 895), 'Yazılım Tekeli & Dışa Bağımlılık', font=get_font(34, True), fill=WHITE)
d2.text((2010, 950), 'Yerli araçlarımızın (TOGG, Karsan, BMC)\nbağımsız yazılıma ihtiyacı var.', font=get_font(24, False), fill=MINT_LIGHT, spacing=4)
p2.save(f'{out_dir}/page_2.png')

# ==========================================
# PAGE 3: ÜRÜN / HİZMET
# ==========================================
p3 = Image.open(f'{bg_dir}/bg_page_3.png')
d3 = ImageDraw.Draw(p3)
d3.text((516, 144), 'Ürün / Hizmet', font=get_font(80, True), fill=NAVY)
p3_desc = (
    'Trustia Full-Stack Otonom Sürüş İşletim Sistemi\n\n'
    'Mevcut ticari filoları sıfırdan araç üretmeye gerek kalmadan,\n'
    '48 saatte tak-çalıştır donanım ve yazılım kitiyle Seviye-4 otonom hale getiriyoruz.\n\n'
    '• 16.000+ Satır C++ & Python Çekirdek Kod Tabanı\n'
    '• 1.301 Otomatik Doğrulama Testi (%100 Başarı)\n'
    '• ASIL-D Otomotiv Güvenlik Mimarisi (5ms Override)'
)
d3.text((516, 320), p3_desc, font=get_font(30, False), fill=SLATE, spacing=8)

# Clear laptop screen and paste Trustia Autonomous Driving platform banner
d3.rectangle([2130, 128, 2744, 527], fill=(20, 20, 20))
banner_path = r'C:\Users\Murat\Desktop\Trustia\Kurumsal\Medya\Banner.jpg'
if os.path.exists(banner_path):
    banner = Image.open(banner_path)
    w_crop = int(banner.height * (614 / 399)) # 1662
    crop_box = (0, 0, w_crop, banner.height)
    laptop_img = banner.crop(crop_box).resize((614, 399), Image.Resampling.LANCZOS)
    p3.paste(laptop_img, (2130, 128))

# 3 Solution cards: vertically centered with the circular icons
d3.text((500, 905), 'Çözüm 1: Otonomi Çekirdeği', font=get_font(30, True), fill=GREEN)
d3.text((500, 950), '16.000+ satır C++/Python,\n1.301 birim testle doğrulanmış\ntam bağımsız Seviye-4 yazılım.', font=get_font(24, False), fill=SLATE, spacing=5)

d3.text((1325, 960), 'Çözüm 2: LiDAR SLAM', font=get_font(30, True), fill=GREEN)
d3.text((1325, 1005), 'GPS olmayan tünel, maden\nve depolarda santimetre\nhassasiyetinde haritalama & sürüş.', font=get_font(24, False), fill=SLATE, spacing=5)

d3.text((2175, 880), 'Çözüm 3: 5ms ASIL-D Emniyet', font=get_font(30, True), fill=GREEN)
d3.text((2175, 925), 'Sürücü dokunduğu an 5ms\'de devralma,\n200ms bağımsız watchdog emniyet kilidi.', font=get_font(24, False), fill=SLATE, spacing=5)
p3.save(f'{out_dir}/page_3.png')

# ==========================================
# PAGE 4: BUGÜNE KADAR
# ==========================================
p4 = Image.open(f'{bg_dir}/bg_page_4.png')
d4 = ImageDraw.Draw(p4)
d4.text((515, 158), 'Bugüne Kadar', font=get_font(80, True), fill=NAVY)
p4_desc = (
    'Trustia Gelişim ve Mühendislik Süreci:\n\n'
    'Türkiye\'nin bağımsız otonom araç yazılımı vizyonuyla yola çıkıldı.\n\n'
    'Yoğun Ar-Ge neticesinde 16.000 satırlık deterministik otonomi çekirdeği\n'
    've 1.301 birim test sıfır hata ile tamamlandı.\n\n'
    'Bugün ASELSAN tedarikçi onayından BTM ve Teknopark İstanbul\n'
    'kuluçkasına uzanan güçlü kurumsal altyapı tesis edildi.'
)
d4.text((515, 380), p4_desc, font=get_font(30, False), fill=SLATE, spacing=10)

# Clear "SALE" tag inside Circle 3
d4.ellipse([1565, 1020, 1690, 1145], fill=DARK_BLUE_TEMPLATE)
# Draw clean star inside Circle 3
d4.text((1628, 1083), '★', font=get_font(52, True), fill=WHITE, anchor="mm")

# 3 Phases to the right of circles (starting at x=1820)
d4.text((1820, 450), '1. Faz: Otonomi Çekirdeği (2026)', font=get_font(36, True), fill=GREEN)
d4.text((1820, 510), '16.000+ satır C++/Python otonomi çekirdeği, ROS2\nve simülasyon testlerinin sıfırdan geliştirilmesi.', font=get_font(26, False), fill=SLATE, spacing=6)

d4.text((1820, 720), '2. Faz: Doğrulama & Emniyet (2026)', font=get_font(36, True), fill=NAVY)
d4.text((1820, 780), '1.301 birim test (%100 başarı), ISO 26262 ASIL-D\n5ms sürücü devralma ve 200ms watchdog tamamlandı.', font=get_font(26, False), fill=SLATE, spacing=6)

d4.text((1820, 1020), '3. Faz: Kurumsal Onaylar (2026)', font=get_font(36, True), fill=GREEN)
d4.text((1820, 1080), 'ASELSAN potansiyel tedarikçi kabulü, İTO BTM Fulya,\nTeknopark İstanbul HASAT ve NATO NCAGE tescili.', font=get_font(26, False), fill=SLATE, spacing=6)
p4.save(f'{out_dir}/page_4.png')

# ==========================================
# PAGE 5: BAŞARI GÖSTERGELERİ
# ==========================================
p5 = Image.open(f'{bg_dir}/bg_page_5.png')
d5 = ImageDraw.Draw(p5)
d5.text((516, 120), 'Başarı\nGöstergeleri', font=get_font(80, True), fill=NAVY, spacing=10)

# All 4 pills have WHITE text, centered
d5.text((526, 851), '16.000+ Kod', font=get_font(36, True), fill=WHITE, anchor="mm")
d5.text((526, 930), 'Satır C++ / Python', font=get_font(26, False), fill=SLATE, anchor="mm")

d5.text((1125, 851), '1.301 Test', font=get_font(36, True), fill=WHITE, anchor="mm")
d5.text((1125, 930), '%100 Başarı Oranı', font=get_font(26, False), fill=SLATE, anchor="mm")

d5.text((1723, 851), '5 ms Emniyet', font=get_font(36, True), fill=WHITE, anchor="mm")
d5.text((1723, 930), 'ASIL-D Fail-Safe', font=get_font(26, False), fill=SLATE, anchor="mm")

d5.text((2322, 851), '5+ Akreditasyon', font=get_font(36, True), fill=WHITE, anchor="mm")
d5.text((2322, 930), 'Resmi Kurum Tescili', font=get_font(26, False), fill=SLATE, anchor="mm")

# Bottom section: NO EMOJIS! Clean professional bullets
d5.text((1440, 1140), 'Resmi Akreditasyon ve Kurumsal Ortaklarımız:', font=get_font(32, True), fill=NAVY, anchor="mm")
d5.text((1440, 1200), 'ASELSAN Tedarikçi Adayı  •  İTO BTM Fulya  •  Teknopark İstanbul HASAT', font=get_font(28, True), fill=SLATE, anchor="mm")
d5.text((1440, 1250), 'Avrupa Komisyonu PIC: 861711529  •  EIT Urban Mobility: CUS15554  •  NATO NCAGE: TR26258467723', font=get_font(26, False), fill=SLATE, anchor="mm")
p5.save(f'{out_dir}/page_5.png')

# ==========================================
# PAGE 6: HEDEF PAZAR
# ==========================================
p6 = Image.open(f'{bg_dir}/bg_page_6.png')
d6 = ImageDraw.Draw(p6)
d6.text((520, 167), 'Hedef Pazar', font=get_font(80, True), fill=NAVY)
p6_desc = (
    'Hitap Ettiğimiz Müşteriler & Sektörler:\n\n'
    '• Yerli Otomotiv OEM\'leri:\n  Karsan, BMC, Otokar, Ford Otosan\n\n'
    '• Ağır Sanayi, Liman ve Açık Madenler:\n  Sürücüsüz hafriyat ve konteyner taşıma\n\n'
    '• Fabrika İçi ve E-Ticaret Depoları:\n  Dar koridorlarda otonom AMR/AGV filoları\n\n'
    '• Belediyeler, Kampüsler & Havalimanları:\n  7/24 sürücüsüz ring ve servis hatları'
)
d6.text((200, 420), p6_desc, font=get_font(30, False), fill=SLATE, spacing=8)

d6.text((1440, 340), '1. Kapalı Alan & Ağır Sanayi (Maden, Liman, OSB)', font=get_font(36, True), fill=WHITE)
d6.text((1440, 410), 'Toz, çamur ve tünel koşullarında çalışan ağır araçların sürücüsüzleştirilmesi.\nSıfır iş kazası, 7/24 kesintisiz operasyon ve %50 bakım tasarrufu.', font=get_font(26, False), fill=MINT_LIGHT, spacing=8)

d6.text((1440, 745), '2. Şehir İçi Robotaksi & Kampüs Ring Servisleri', font=get_font(36, True), fill=WHITE)
d6.text((1440, 815), 'Havalimanı yer hizmetleri, tatil köyleri ve üniversite kampüslerinde yolcu transferi.\nDinamik rota optimizasyonu ve mobil çağrı aplikasyonu entegrasyonu.', font=get_font(26, False), fill=MINT_LIGHT, spacing=8)
p6.save(f'{out_dir}/page_6.png')

# ==========================================
# PAGE 7: PAZAR BÜYÜKLÜĞÜ
# ==========================================
p7 = Image.open(f'{bg_dir}/bg_page_7.png')
d7 = ImageDraw.Draw(p7)
d7.text((516, 167), 'Pazar Büyüklüğü', font=get_font(80, True), fill=NAVY)

# Pill 1: Navy
d7.text((572, 565), '$1.2 Trilyon', font=get_font(40, True), fill=WHITE, anchor='mm')
d7.text((398, 650), 'TOTAL AVAILABLE MARKET (TAM) - 2030 Küresel Otonomi', font=get_font(22, True), fill=DARK_BLUE_TEMPLATE)

# Pill 2: Green like original template!
d7.rounded_rectangle([398, 730, 747, 878], radius=25, fill=GREEN)
d7.text((572, 804), '$48 Milyar', font=get_font(40, True), fill=WHITE, anchor='mm')
d7.text((398, 895), 'SERVICEABLE AVAILABLE MARKET (SAM) - MENA, TR & Doğu Avrupa', font=get_font(22, True), fill=GREEN)

# Pill 3: Navy
d7.text((572, 1040), '$25 Milyon', font=get_font(40, True), fill=WHITE, anchor='mm')
d7.text((398, 1130), 'SERVICEABLE OBTAINABLE MARKET (SOM) - 3 Yılda Hedef Lisans', font=get_font(22, True), fill=DARK_BLUE_TEMPLATE)

# Right chart
d7.text((2230, 360), 'Küresel Otonomi Pazar Hacmi ($ Milyar)', font=get_font(26, True), fill=NAVY, anchor='mm')
d7.text((1700, 1255), '0', font=get_font(22, False), fill=SLATE, anchor='rm')
d7.text((1700, 1050), '10', font=get_font(22, False), fill=SLATE, anchor='rm')
d7.text((1700, 840), '20', font=get_font(22, False), fill=SLATE, anchor='rm')
d7.text((1700, 630), '30', font=get_font(22, False), fill=SLATE, anchor='rm')
d7.text((1700, 420), '40', font=get_font(22, False), fill=SLATE, anchor='rm')

d7.text((1851, 1315), '2026', font=get_font(26, True), fill=SLATE, anchor='mm')
d7.text((2072, 1315), '2027', font=get_font(26, True), fill=SLATE, anchor='mm')
d7.text((2334, 1315), '2028', font=get_font(26, True), fill=SLATE, anchor='mm')
d7.text((2596, 1315), '2030', font=get_font(26, True), fill=SLATE, anchor='mm')
p7.save(f'{out_dir}/page_7.png')

# ==========================================
# PAGE 8: REKABET AVANTAJLARI
# ==========================================
p8 = Image.open(f'{bg_dir}/bg_page_8.png')
d8 = ImageDraw.Draw(p8)
d8.text((480, 160), 'Rekabet Avantajları', font=get_font(80, True), fill=NAVY)
d8.text((480, 300), 'Neden Trustia\'yı Tercih Edecekler?', font=get_font(36, True), fill=GREEN)
p8_desc = (
    '• %60 Maliyet Avantajı:\n'
    '  Yabancı tekellere kıyasla erişilebilir lisanslama ve dönüşüm maliyeti.\n\n'
    '• %100 Yerli ve Bağımsız Çekirdek:\n'
    '  Savunma ve ticari filo verileri tamamen yurt içinde kalır, dışa bağımlılık biter.\n\n'
    '• 48 Saatte Tak-Çalıştır Entegrasyon:\n'
    '  Sıfırdan araç üretmeden mevcut filoları Seviye-4 otonom hale getirir.\n\n'
    '• ASIL-D Otomotiv Güvenlik Seviyesi:\n'
    '  5ms anında sürücü müdahalesi ve 200ms bağımsız watchdog donanım kilidi.'
)
d8.text((480, 400), p8_desc, font=get_font(28, False), fill=SLATE, spacing=8)

d8.text((2100, 1080), '%65 Ağır Sanayi, Liman ve Maden Filoları', font=get_font(24, True), fill=GREEN)
d8.text((1740, 400), '%25 Şehir İçi Robotaksi & Ring Hatları', font=get_font(24, True), fill=NAVY)
d8.text((2350, 290), '%10 Özel Güvenlik & Savunma', font=get_font(24, True), fill=NAVY)
p8.save(f'{out_dir}/page_8.png')

# ==========================================
# PAGE 9: AVANTAJ MATRİSİ (SWOT)
# ==========================================
p9 = Image.open(f'{bg_dir}/bg_page_9.png')
d9 = ImageDraw.Draw(p9)
# Quadrant 1 (Green, Top-Left)
d9.text((460, 180), 'Avantaj 1: Donanım-Agnostik Mimari', font=get_font(38, True), fill=WHITE)
d9.text((460, 260), 'Her marka ve model elektrikli/hibrit araca (CAN-FD\nprotokolü üzerinden) 48 saatte entegre edilebilir.\nSıfırdan araç üretimi gerektirmez, mevcut filoyu dönüştürür.', font=get_font(28, False), fill=MINT_LIGHT, spacing=12)

# Quadrant 2 (White, Top-Right)
d9.text((1750, 180), 'Avantaj 2: ASIL-D Emniyet Standardı', font=get_font(38, True), fill=NAVY)
d9.text((1750, 260), 'Otomotivde en üst güvenlik seviyesi olan ISO 26262\nASIL-D prensiplerine uygun mimari.\n5ms anında sürücü müdahalesi ve 200ms bağımsız watchdog.', font=get_font(28, False), fill=SLATE, spacing=12)

# Quadrant 3 (White, Bottom-Left)
d9.text((460, 860), 'Avantaj 3: 1.301 Test ile Doğrulanmış Çekirdek', font=get_font(38, True), fill=GREEN)
d9.text((460, 940), '16.000 satırlık deterministik kod tabanı;\nsimülasyon ve yol testlerinde %100 doğrulukla\ndoğrulanmış, hataya toleranslı hibrit karar algoritmaları.', font=get_font(28, False), fill=SLATE, spacing=12)

# Quadrant 4 (Navy, Bottom-Right)
d9.text((1750, 860), 'Zorluk & Yönetim Stratejimiz', font=get_font(38, True), fill=WHITE)
d9.text((1750, 940), 'Türkiye\'de kamu yollarında otonomi mevzuatı gelişmektedir.\n\nStratejimiz: İzin gerektirmeyen kapalı maden, liman\nve OSB özel sahalarında ticarileşerek ilk günden nakit akışı.', font=get_font(28, False), fill=(226, 232, 240), spacing=12)
p9.save(f'{out_dir}/page_9.png')

# ==========================================
# PAGE 10: GELİR MODELİ
# ==========================================
p10 = Image.open(f'{bg_dir}/bg_page_10.png')
d10 = ImageDraw.Draw(p10)
d10.text((493, 167), 'Gelir Modeli', font=get_font(80, True), fill=NAVY)
p10_desc = (
    'Yüksek Brüt Kâr Marjlı (%85+) Gelir Mimarisi:\n\n'
    'B2B ve B2G odaklı, tekrarlayan ve hızla ölçeklenebilir\n'
    '3 temel gelir kanalı kurgulanmıştır:\n\n'
    '1. Yıllık Yazılım Lisanslama (SaaS / SDK):\n'
    '   Araç başı yıllık otonomi yazılım lisansı ve OTA güncellemeleri.\n\n'
    '2. Otonom Dönüşüm Kiti Satışı:\n'
    '   Mevcut filolara tak-çalıştır Drive-by-Wire ve sensör entegrasyonu.\n\n'
    '3. Sefer Başı Komisyon Paylaşımı (TaaS):\n'
    '   Robotaksi ve özel saha operasyonlarında sefer başına pay.'
)
d10.text((340, 420), p10_desc, font=get_font(30, False), fill=SLATE, spacing=10)

# Circle 1 (Green, Center: 1800, 665)
d10.text((1800, 635), 'Lisans', font=get_font(36, True), fill=WHITE, anchor="mm")
d10.text((1800, 685), 'SaaS / SDK', font=get_font(24, False), fill=MINT_LIGHT, anchor="mm")
d10.text((1800, 930), 'Hedef: $1.5M', font=get_font(28, True), fill=GREEN, anchor="mm")
d10.text((1800, 970), 'Yıllık Lisans', font=get_font(22, False), fill=SLATE, anchor="mm")

# Circle 2 (Light Green, Center: 2224, 699)
d10.text((2224, 665), 'Dönüşüm Kiti', font=get_font(34, True), fill=NAVY, anchor="mm")
d10.text((2224, 715), 'Donanım & Entegrasyon', font=get_font(22, False), fill=NAVY, anchor="mm")
d10.text((2224, 930), 'Birim: $45.000', font=get_font(28, True), fill=NAVY, anchor="mm")
d10.text((2224, 970), 'Tak-Çalıştır Kit', font=get_font(22, False), fill=SLATE, anchor="mm")

# Circle 3 (Navy, Center: 2554, 665)
d10.text((2554, 635), 'Sefer Payı', font=get_font(32, True), fill=WHITE, anchor="mm")
d10.text((2554, 685), 'TaaS Model', font=get_font(22, False), fill=(226, 232, 240), anchor="mm")
d10.text((2554, 930), 'Pay: %15 - %20', font=get_font(28, True), fill=DARK_BLUE_TEMPLATE, anchor="mm")
d10.text((2554, 970), 'Komisyon Oranı', font=get_font(22, False), fill=SLATE, anchor="mm")
p10.save(f'{out_dir}/page_10.png')

# ==========================================
# PAGE 11: GİRİŞİMCİ TAKIM (MURAT'S REAL PHOTO & ZERO CARTOON!)
# ==========================================
p11 = Image.open(f'{bg_dir}/bg_page_11.png')
d11 = ImageDraw.Draw(p11)

# 1. COMPLETELY WIPE OUT THE 3 CARTOON GIRLS
d11.rectangle([1400, 50, 2800, 1350], fill=WHITE)

d11.text((507, 150), 'Girişimci Takım', font=get_font(80, True), fill=NAVY)
p11_desc = (
    'Ağır Siklet Derin Teknoloji Ekibi:\n\n'
    '• 16.000+ satırlık deterministik otonomi çekirdeğini,\n'
    '  algoritma ve mimariyi sıfırdan geliştiren kurucu liderlik.\n\n'
    '• Donanım entegrasyonu, Drive-by-Wire aktüatörleri ve\n'
    '  CAN-FD kontrolünde ASELSAN ve TEKNOFEST tecrübesi.\n\n'
    '• Sıfır dış bağımlılık, çevik geliştirme döngüsü ve\n'
    '  sahada anında teknik müdahale kabiliyeti.'
)
d11.text((480, 460), p11_desc, font=get_font(30, False), fill=SLATE, spacing=10)

# Card 1: Murat Furkan Bayram
avatar_path = r'C:\Users\Murat\Desktop\Trustia\Kurumsal\Medya\murat_avatar.png'
if os.path.exists(avatar_path):
    avatar = Image.open(avatar_path).resize((250, 250))
    p11.paste(avatar, (1510, 480), mask=avatar)

d11.rounded_rectangle([1800, 440, 2720, 780], radius=20, fill=NAVY)
d11.text((1830, 470), 'Murat Furkan Bayram', font=get_font(38, True), fill=LIGHT_GREEN)
d11.text((1830, 525), 'Kurucu & CEO / Sistem Mimarı (%100 Hisse)', font=get_font(26, True), fill=WHITE)
d11.text((1830, 575), 'Trustia Seviye-4 otonomi işletim sisteminin tek mimarı.\n16.000+ satır C++/Python çekirdek kod tabanı, 1.301 birim test,\nASIL-D fail-safe emniyet kilidi, ROS2 ve C2 arayüzü geliştiricisi.', font=get_font(22, False), fill=(203, 213, 225), spacing=5)

# Card 2: Denizcan Özcan Circular Badge & Card
d11.ellipse([1510, 870, 1760, 1120], fill=GREEN, outline=NAVY, width=4)
d11.text((1635, 995), 'DÖ', font=get_font(72, True), fill=WHITE, anchor='mm')

d11.rounded_rectangle([1800, 830, 2720, 1170], radius=20, fill=GREEN)
d11.text((1830, 860), 'Denizcan Özcan', font=get_font(38, True), fill=WHITE)
d11.text((1830, 915), 'Baş Donanım ve Entegrasyon Mühendisi', font=get_font(26, True), fill=MINT_LIGHT)
d11.text((1830, 965), 'ASELSAN Aday Havuzu & TEKNOFEST Robotaksi Finalisti.\nCAN-FD veri yolu kontrolü, Drive-by-Wire aktüatör mimarisi,\ngüç dağıtım sistemleri ve araç üstü donanım entegrasyonu sorumlusu.', font=get_font(22, False), fill=MINT_LIGHT, spacing=5)
p11.save(f'{out_dir}/page_11.png')

# ==========================================
# PAGE 12: GELECEK YOL HARİTASI
# ==========================================
p12 = Image.open(f'{bg_dir}/bg_page_12.png')
d12 = ImageDraw.Draw(p12)
d12.text((384, 127), 'Gelecek Yol Haritası', font=get_font(80, True), fill=NAVY)
p12_desc = (
    'Önümüzdeki 2 Yıllık Büyüme ve Ölçeklenme Planı:\n\n'
    '• Faz 1: ASELSAN & BTM Pilot Saha Doğrulaması\n\n'
    '• Faz 2: İlk Ticari Filo Dönüşüm Kiti Teslimatları\n\n'
    '• Faz 3: TİM Destekli Körfez (Katar/Doha) İhracatı\n\n'
    '• Faz 4: 100+ Araçlık Seviye-4 Otonom Filo Yönetimi'
)
d12.text((384, 300), p12_desc, font=get_font(32, False), fill=SLATE, spacing=12)

# Step 1: right of Pin 1, above dashed line
d12.text((2000, 330), 'Step 1 (Q4 2026)', font=get_font(32, True), fill=NAVY)
d12.text((2000, 375), 'Pilot Saha Testleri & ASELSAN', font=get_font(24, False), fill=SLATE)

# Step 2: right of Pin 2
d12.text((2220, 660), 'Step 2 (Q2 2027)', font=get_font(32, True), fill=GREEN)
d12.text((2220, 705), 'Ticari Lansman & OSB Limanlar', font=get_font(24, False), fill=SLATE)

# Step 3: in open white space between dashed lines
d12.text((2050, 930), 'Step 3 (Q4 2027)', font=get_font(32, True), fill=NAVY)
d12.text((2050, 975), 'Körfez İhracatı (Katar & BAE)', font=get_font(24, False), fill=SLATE)

# Step 4: right of Pin 4
d12.text((2160, 1140), 'Step 4 (Q2 2028)', font=get_font(32, True), fill=GREEN)
d12.text((2160, 1185), 'Seri Robotaksi & 100+ Filo', font=get_font(24, False), fill=SLATE)
p12.save(f'{out_dir}/page_12.png')

# ==========================================
# PAGE 13: TİM-TEB'DEN NE BEKLİYORUZ
# ==========================================
p13 = Image.open(f'{bg_dir}/bg_page_13.png')
d13 = ImageDraw.Draw(p13)
d13.text((480, 150), 'TİM-TEB Girişim Evi’nden Ne Bekliyoruz', font=get_font(72, True), fill=GREEN)
d13.text((480, 260), 'Trustia\'nın Büyüme ve Ölçeklenme Sürecinde Stratejik Ortaklık:', font=get_font(32, True), fill=NAVY)
p13_desc = (
    '1. Start Up To Corporate (S2C) Kurumsal Eşleştirmeler:\n'
    '   TİM-TEB ekosistemindeki büyük otomotiv OEM\'leri (Ford Otosan, Karsan, BMC)\n'
    '   ve lojistik filolarıyla doğrudan pilot proje (PoC) görüşmeleri.\n\n'
    '2. Uluslararası Ticaret Heyetleri & Küresel Fuarlar:\n'
    '   TİM koordinasyonunda düzenlenen yurt dışı ticaret heyetleri (Körfez, Avrupa)\n'
    '   ve küresel teknoloji fuarlarında Türkiye\'yi temsil.\n\n'
    '3. İhracat ve Büyüme Mentörlüğü:\n'
    '   Derin teknoloji yazılım lisansı ihracatı, sınır ötesi sözleşmeler,\n'
    '   uluslararası patent koruması ve regülasyon uyumu.\n\n'
    '4. Stratejik Yatırımcı Ağları & Fon Buluşmaları:\n'
    '   Mobilite ve derin teknoloji odaklı kurumsal girişim sermayesi (CVC)\n'
    '   ve melek yatırımcı ağlarıyla tohum yatırım süreçlerinin yönetimi.'
)
d13.text((480, 340), p13_desc, font=get_font(28, False), fill=SLATE, spacing=8)
p13.save(f'{out_dir}/page_13.png')

# ==========================================
# PAGE 14: TEŞEKKÜRLER!
# ==========================================
p14 = Image.open(f'{bg_dir}/bg_page_14.png')
d14 = ImageDraw.Draw(p14)

# Erase leftover underlines inside navy circle
d14.rectangle([500, 590, 1000, 800], fill=(32, 41, 79))

d14.text((520, 320), 'Teşekkürler!', font=get_font(90, True), fill=WHITE)
d14.text((520, 470), 'Murat Furkan Bayram', font=get_font(44, True), fill=LIGHT_GREEN)
d14.text((520, 530), 'Kurucu & CEO / Sistem Mimarı', font=get_font(28, False), fill=(226, 232, 240))
d14.line([(520, 590), (1050, 590)], fill=GREEN, width=3)
d14.text((520, 630), 'Tel: 0537 064 04 60', font=get_font(34, True), fill=WHITE)
d14.text((520, 690), 'E-Posta: kariyer@trustia.com.tr', font=get_font(34, True), fill=WHITE)
d14.text((520, 750), 'Web: https://trustia.com.tr', font=get_font(34, True), fill=LIGHT_GREEN)
d14.text((520, 830), 'Sorularınızı yanıtlamaktan memnuniyet duyarız.', font=get_font(26, False), fill=(203, 213, 225))
p14.save(f'{out_dir}/page_14.png')

# ==========================================
# COMPILE MASTER PDF
# ==========================================
final_images = [Image.open(f'{out_dir}/page_{i}.png') for i in range(1, 15)]
master_pdf = r'C:\Users\Murat\Downloads\Trustia_TIM_TEB_Sunumu.pdf'
final_images[0].save(master_pdf, save_all=True, append_images=final_images[1:], resolution=100.0)
shutil.copy2(master_pdf, r'C:\Users\Murat\Desktop\Trustia\Kurumsal\Sunumlar\Trustia_TIM_TEB_Sunumu.pdf')
print('SUCCESS: All 14 pages generated and compiled to master PDF!')
