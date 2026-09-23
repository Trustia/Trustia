import os

logo_path = "file:///" + os.path.abspath("Kurumsal/Medya/Logo.png").replace("\\", "/")
car_path = "file:///" + os.path.abspath("Kurumsal/Medya/Arac_Lidar.png").replace("\\", "/")

html_path_1 = "Kurumsal/Sunumlar/Trustia_ASELSAN_Sunumu.html"
html_path_2 = r"C:\Users\Murat\Downloads\Trustia_ASELSAN_Sunumu.html"

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trustia AI - ASELSAN Tanışma Sunumu</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}
        body {{
            background-color: #0F172A;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
            color: #1E293B;
        }}
        .deck-container {{
            width: 100vw;
            height: 100vh;
            max-width: 1280px;
            max-height: 720px;
            background: #FFFFFF;
            position: relative;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            border-radius: 12px;
            overflow: hidden;
        }}
        .slide {{
            display: none;
            width: 100%;
            height: 100%;
            padding: 40px 60px;
            flex-direction: column;
            justify-content: space-between;
            position: absolute;
            top: 0;
            left: 0;
            background: #FFFFFF;
        }}
        .slide.active {{
            display: flex;
        }}
        .slide-header {{
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }}
        .slide-tag {{
            font-size: 11px;
            font-weight: 800;
            color: #0056B3;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }}
        .slide-title {{
            font-size: 26px;
            font-weight: 800;
            color: #0B2545;
            line-height: 1.2;
        }}
        .content-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 16px;
            justify-content: center;
        }}
        .card {{
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px 20px;
        }}
        .card-blue {{
            border-left: 4px solid #0056B3;
        }}
        .card-red {{
            border-left: 4px solid #DC2626;
        }}
        .card-title {{
            font-size: 16px;
            font-weight: 700;
            color: #0B2545;
            margin-bottom: 6px;
        }}
        .card-desc {{
            font-size: 13.5px;
            color: #475569;
            line-height: 1.5;
        }}
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            flex: 1;
        }}
        .grid-2x2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 16px;
            flex: 1;
        }}
        .grid-3 {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 16px;
            flex: 1;
        }}
        .grid-4 {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr;
            gap: 14px;
            flex: 1;
        }}
        table.matrix-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 5px;
            border-radius: 8px;
            overflow: hidden;
        }}
        table.matrix-table th {{
            background: #0B2545;
            color: #FFFFFF;
            padding: 12px 14px;
            font-size: 13px;
            font-weight: 700;
            text-align: left;
        }}
        table.matrix-table td {{
            padding: 11px 14px;
            font-size: 13.5px;
            border-bottom: 1px solid #E2E8F0;
        }}
        table.matrix-table tr:nth-child(even) {{
            background: #F8FAFC;
        }}
        .val-good {{ color: #16A34A; font-weight: 700; }}
        .val-bad {{ color: #DC2626; font-weight: 600; }}
        .val-mid {{ color: #D97706; font-weight: 600; }}

        .two-cols {{
            display: flex;
            gap: 25px;
            flex: 1;
        }}
        .col-left {{
            flex: 1.3;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .col-right {{
            flex: 1;
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .deck-controls {{
            position: fixed;
            bottom: 20px;
            display: flex;
            align-items: center;
            gap: 14px;
            background: rgba(15, 23, 42, 0.9);
            padding: 10px 20px;
            border-radius: 30px;
            backdrop-filter: blur(8px);
            z-index: 100;
        }}
        .btn {{
            background: #0056B3;
            color: #FFF;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn:hover {{
            background: #003D80;
            transform: scale(1.03);
        }}
        .slide-counter {{
            color: #94A3B8;
            font-size: 13px;
            font-weight: 600;
            min-width: 60px;
            text-align: center;
        }}
    </style>
</head>
<body>

<div class="deck-container" id="presentationContainer">

    <!-- SLIDE 1: KAPAK -->
    <div class="slide active" style="justify-content: center; align-items: flex-start; padding: 60px 80px; background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
            <img src="{logo_path}" alt="Trustia Logo" style="height: 60px; object-fit: contain;">
        </div>
        <div style="font-size: 13px; font-weight: 700; color: #0056B3; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px;">
            TRUSTIA TEKNOLOJİ
        </div>
        <h1 style="font-size: 34px; font-weight: 900; color: #0B2545; line-height: 1.2; margin-bottom: 12px;">
            Milli Otonom Sürüş Yazılımı & İnsansız Araç Beyni
        </h1>
        <p style="font-size: 18px; color: #475569; margin-bottom: 40px; font-weight: 500;">
            Uydudan Bağımsız Lazerle Harita Çıkaran ve Sinyal Kesilmesinden Etkilenmeyen Yerli Sistem
        </p>
        
        <div style="border-top: 2px solid #E2E8F0; padding-top: 20px; width: 100%; display: flex; justify-content: space-between; font-size: 13px; color: #64748B;">
            <div>
                <strong style="color: #0B2545;">Başvuru:</strong> ASELSAN Girişimcilik Merkezi (Axcelerate)<br>
                <strong style="color: #0B2545;">Yerleşke:</strong> İTO BTM Fulya Kampüsü | <strong>Tedarikçi No:</strong> 0050569
            </div>
            <div style="text-align: right;">
                <strong style="color: #0B2545;">Sunucu:</strong> Murat Furkan Bayram (Kurucu & Sistem Mimarı)<br>
                <strong style="color: #0B2545;">Donanım:</strong> Denizcan Özcan (ASELSAN Aday Mühendis Havuzu)
            </div>
        </div>
    </div>

    <!-- SLIDE 2: PROBLEM -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">PROBLEM: Askeri Sahada Yaşanan 3 Büyük Zorluk</div>
        </div>
        <div class="content-body">
            <div class="card card-red">
                <div class="card-title">1. Uydu (GPS) Sinyalinin Kesilmesi</div>
                <div class="card-desc">Savaş ve operasyon alanlarında sinyal bozucular uydu bağlantısını tamamen keser. Pazardaki standart insansız araçlar uydu bağlantısı koptuğunda yönünü kaybedip durur ve açık hedef haline gelir.</div>
            </div>
            <div class="card card-red">
                <div class="card-title">2. Uzaktan Kumanda (Telsiz) Bağlantısının Kopması</div>
                <div class="card-desc">Uzaktan kumandayla yönlendirilen araçlarda telsiz bağı koptuğunda araç olduğu yerde donup kalır. Ayrıca sinyalin gecikmeli gitmesi ani engellerde kazalara yol açar.</div>
            </div>
            <div class="card card-red">
                <div class="card-title">3. Yabancı Otonom Yazılımlara Bağımlılık</div>
                <div class="card-desc">Piyasadaki hazır otonom sistemler yabancı kaynaklıdır. Güvenlik açıkları taşır ve Türk savunma sanayii sistemleriyle doğrudan haberleşemez.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 3: ÇÖZÜM -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ÇÖZÜM: Trustia Yerli Otonom Sürüş Çekirdeği</div>
        </div>
        <div class="content-body">
            <div class="card card-blue">
                <div class="card-title">1. Uydu Olmadan Lazer Gözlerle (LiDAR) Haritalama</div>
                <div class="card-desc">Uydu sinyali tamamen kesilse bile; araç üzerindeki 3 boyutlu lazer tarayıcılar sayesinde araç kendi haritasını arazide kendisi çıkarır ve yolundan şaşmadan ilerler.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Bağlantı Koptuğunda Kendi Başına Üsse Dönüş</div>
                <div class="card-desc">Kumanda veya telsiz bağlantısı koptuğu anda araç panik yapmaz. Hafızasındaki lazer haritayı takip ederek güvenli başlangıç noktasına kendi kendine geri döner.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. %100 Yerli Kod ve ASELSAN Sistemlerine Tam Uyum</div>
                <div class="card-desc">Yazılımın tüm satırları sıfırdan yerli olarak yazılmıştır. Askeri haberleşme kurallarına ve ASELSAN kara sistemlerine doğrudan bağlanabilir.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 4: ÜRÜN -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ÜRÜN: Trustia Otonomi Beyni ve Kontrol Ekranı</div>
        </div>
        <div class="two-cols">
            <div class="col-left">
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Akıllı Sürüş ve Rota Çizici</div>
                    <div class="card-desc" style="font-size: 13px;">Lazer sensörlerle çevreyi tarar; yoldaki çukurları, kayaları ve hareketli engelleri anında görüp etrafından dolaşır.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Askeri Tehlike Algılama Modülü</div>
                    <div class="card-desc" style="font-size: 13px;">Yoldaki mayın ve patlayıcı şüpheli cisimleri tespit eder, aracı güvenli mesafede durdurur.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Taktik Komuta Ekranı</div>
                    <div class="card-desc" style="font-size: 13px;">Askeri harita destekli kontrol ekranı. Operatör ekran üzerinden tek dokunuşla araca hedef verir veya anında durdurur.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• 1.301 Test ile Kanıtlanmış Güvenlik</div>
                    <div class="card-desc" style="font-size: 13px;">16 bin satırlık yazılım çekirdeği 1.301 farklı zorlu arazi senaryosunda test edilmiş ve tamamını hatasız geçmiştir.</div>
                </div>
            </div>
            <div class="col-right">
                <img src="{car_path}" alt="Trustia Otonomi Platformu" style="width: 100%; max-height: 180px; object-fit: contain; margin-bottom: 12px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 8px;">TEKNİK UYUMLULUK</div>
                <div style="font-size: 12.5px; line-height: 1.6; color: #1E293B; width: 100%;">
                    ✓ Haberleşme: Askeri ve Robotik Standartlara Tam Uyumlu<br>
                    ✓ Bilgisayar: Nvidia Jetson ve Araç İçi Bilgisayarlarla Uyumlu<br>
                    ✓ Sensörler: Her Marka Lazer (LiDAR) ve Kamerayla Çalışabilir<br>
                    ✓ Tepki Hızı: 5 Milisaniyede (Göz Kırpmasından Hızlı) Müdahale<br>
                    ✓ Durum: Yazılım Hazır, 1.301 Testten Geçti
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 5: ALTYAPILAR -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ALTYAPILAR: Çalışma Merkezimiz ve Belgelerimiz</div>
        </div>
        <div class="grid-2x2">
            <div class="card card-blue">
                <div class="card-title">İTO BTM Fulya Kampüsü</div>
                <div class="card-desc">İstanbul Ticaret Odası bünyesindeki Fulya Derin Teknoloji Kampüsü'nde yerleşik merkezimiz. Ar-Ge, yazılım ve çalışma alanımız buradadır.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">Donanım Bağımsız Yazılım Altyapısı</div>
                <div class="card-desc">Biz yazılım şirketiyiz. Kodlarımız donanım bağımsızdır; ASELSAN'ın araçlarındaki her marka lazer (LiDAR), kamera ve araç bilgisayarına doğrudan tak-çalıştır bağlanır.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">1.301 Testli Sanal Test Odası</div>
                <div class="card-desc">Gerçek araziye çıkmadan önce yazılımımızı 1.301 farklı sanal senaryoda (sis, çamur, gece, karıştırma) 43 saniyede otomatik test eden sistemimiz aktiftir.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">Resmi Belgelerimiz ve Onaylarımız</div>
                <div class="card-desc">ASELSAN Tedarikçi Portalı Yazılım Ön Onayı (SAP: FZQHEXGFMTJU), NATO Tedarikçi Kodu Başvurusu, TÜBİTAK ARBİS Kaydı ve Savunma Sanayii Sertifikalarımız.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 6: PAZAR -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">PAZAR BÜYÜKLÜĞÜ: Askeri İnsansız Araçlar Pazarı</div>
        </div>
        <div class="grid-3">
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 25px 20px;">
                <div>
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">DÜNYA PAZARI</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">15.8 Milyar $</div>
                </div>
                <div class="card-desc">Dünyadaki askeri insansız kara araçları ve taktik otonomi sistemlerinin toplam yıllık pazar büyüklüğü.</div>
            </div>
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 25px 20px;">
                <div>
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">BÖLGEMİZDEKİ PAZAR</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">1.2 Milyar $</div>
                </div>
                <div class="card-desc">Türkiye, NATO ve bölge ülkelerindeki sınır güvenliği, otonom konvoy ve taktik araç yazılımları pazarı.</div>
            </div>
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 25px 20px;">
                <div>
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">BİZİM HEDEFİMİZ</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">45 Milyon $</div>
                </div>
                <div class="card-desc">ASELSAN ve yerli kara araçlarının otonomlaştırılması projelerinde ilk 3 yılda hedeflediğimiz yerli yazılım payı.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 7: RAKİP ANALİZİ -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">FARKIMIZ: Sahadaki Çözümlerle Karşılaştırma</div>
        </div>
        <div class="content-body">
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th>Özellik ve Yetenek</th>
                        <th style="background: #0056B3; text-align: center;">TRUSTIA (Yerli Yazılım)</th>
                        <th style="text-align: center;">Klasik Kumandalı Araçlar</th>
                        <th style="text-align: center;">Yabancı Açık Kaynaklar</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Uydusuz Lazerle Harita Çıkarma</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tam Uyumlu (Lazerle Gider)</td>
                        <td style="text-align: center;" class="val-bad">✗ Yok (Uydu Şart)</td>
                        <td style="text-align: center;" class="val-mid">△ Şehir Haritası İster</td>
                    </tr>
                    <tr>
                        <td><strong>Askeri Standartlara Uyum</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tam Uyumlu</td>
                        <td style="text-align: center;" class="val-mid">△ Sadece Telsiz</td>
                        <td style="text-align: center;" class="val-bad">✗ Askeri Standart Yok</td>
                    </tr>
                    <tr>
                        <td><strong>%100 Yerli Kod Güvencesi</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tamamen Yerli</td>
                        <td style="text-align: center;" class="val-mid">△ Parçalara Bağımlı</td>
                        <td style="text-align: center;" class="val-bad">✗ Yabancıya Bağımlı</td>
                    </tr>
                    <tr>
                        <td><strong>Bağlantı Kopunca Eve Dönüş</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Kendi Kendine Döner</td>
                        <td style="text-align: center;" class="val-bad">✗ Araç Olduğu Yerde Kalır</td>
                        <td style="text-align: center;" class="val-mid">△ Belirsiz</td>
                    </tr>
                    <tr>
                        <td><strong>1.301 Testten Geçmiş Sistem</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Test Edilmiş & Hazır</td>
                        <td style="text-align: center;" class="val-mid">△ Deneme Aşamasında</td>
                        <td style="text-align: center;" class="val-mid">△ Sivil Testler</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- SLIDE 8: İŞ MODELİ -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">İŞ MODELİ: Savunma Odaklı Yazılım Lisanslama</div>
        </div>
        <div class="content-body">
            <div class="card card-blue">
                <div class="card-title">1. Araç Başına Yazılım Lisansı Satışı</div>
                <div class="card-desc">ASELSAN'ın ürettiği veya modernize ettiği her insansız araç başına yazılım lisans bedeli faturalandırılması.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. İlave Güvenlik Paketleri</div>
                <div class="card-desc">Temel sürüşe ek olarak; Mayın Arama Paketi, Gaz Kaçınma Paketi veya Sürü Halinde İlerleme Paketi gibi ilave yazılım modülleri satışı.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Araç Montajı, Saha Testi ve Yıllık Bakım</div>
                <div class="card-desc">Yeni araçlara sensör ve yazılım bağlama desteği, arazide test desteği ve yıllık yazılım güncelleme/bakım sözleşmeleri.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 9: PAZARA GİRİŞ STRATEJİSİ -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">PAZARA GİRİŞ: Adım Adım Büyüme Planımız</div>
        </div>
        <div class="content-body">
            <div class="card card-blue">
                <div class="card-title">1. Aşama: ASELSAN Araçlarında Saha Denemesi (2026)</div>
                <div class="card-desc">ASELSAN Girişimcilik Merkezi (Axcelerate) desteğiyle ASELSAN taktik kara araçlarında yazılımımızı arazide denemek ve ilk ortak başarıyı yakalamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Aşama: Türk Savunma Sanayii Araçlarına Yayılma (2027)</div>
                <div class="card-desc">ASELSAN onaylı tedarikçi gücüyle; yerli zırhlı araç üreticilerinin araçlarına otonom devriye ve konvoy yazılımı sağlamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Aşama: Dost Ülkelere İhracat (2027-2028)</div>
                <div class="card-desc">NATO tedarikçi kodumuz ve tescillerimizle, dost ülke ordularının projelerine yerli yazılımımızı ihraç etmek.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 10: YOL HARİTASI -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">YOL HARİTASI: 2026 - 2028 Hedeflerimiz</div>
        </div>
        <div class="grid-4">
            <div class="card card-blue" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 6px;">ŞU AN</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Çalışır Sistem</div>
                <div class="card-desc" style="font-size: 12.5px;">16 bin satır yerli kod, 1.301 test ile doğrulandı. ASELSAN Tedarikçi Portalı Yazılım Ön Onayı alındı.</div>
            </div>
            <div class="card card-blue" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 6px;">YIL SONU</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Saha Denemesi</div>
                <div class="card-desc" style="font-size: 12.5px;">Axcelerate programı ile ASELSAN taktik aracında kapalı alanda ve arazide ilk sürüş denemesinin yapılması.</div>
            </div>
            <div class="card" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #64748B; margin-bottom: 6px;">2027 İLK YARI</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Seri Lisanslama</div>
                <div class="card-desc" style="font-size: 12.5px;">İlk 10 taktik kara aracı için seri yazılım lisans teslimatı ve kontrol ekranı tam uyumu.</div>
            </div>
            <div class="card" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #64748B; margin-bottom: 6px;">2027 - 2028</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Sürü ve İhracat</div>
                <div class="card-desc" style="font-size: 12.5px;">Araçların sürü halinde birlikte hareket etmesi ve dost ülkelere yazılım satışı.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 11: EKİP -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">EKİP: Vizyonumuz ve Mühendislik Gücümüz</div>
        </div>
        <div class="grid-2">
            <div class="card card-blue" style="padding: 24px;">
                <div style="font-size: 20px; font-weight: 800; color: #0B2545;">Murat Furkan Bayram</div>
                <div style="font-size: 14px; font-weight: 700; color: #0056B3; margin: 4px 0 14px 0;">Kurucu & CEO / Sistem Mimarı</div>
                <div class="card-desc" style="font-size: 13.5px; line-height: 1.7;">
                    • İleri yapay zeka araçlarıyla 16.000 satırlık otonomi çekirdeğini inşa eden Sistem Mimarı.<br>
                    • 1.301 otomatik güvenlik testinin tasarımcısı ve yöneticisi (%100 başarı).<br>
                    • TÜBİTAK ARBİS, BTK Savunma ve KOSGEB İleri Girişimci tescilleri sahibi.<br>
                    • Yapay Zeka Destekli Yazılım ve Algoritma Lideri.
                </div>
            </div>
            <div class="card card-blue" style="padding: 24px;">
                <div style="font-size: 20px; font-weight: 800; color: #0B2545;">Denizcan Özcan</div>
                <div style="font-size: 14px; font-weight: 700; color: #0056B3; margin: 4px 0 14px 0;">Baş Donanım ve Entegrasyon Mühendisi</div>
                <div class="card-desc" style="font-size: 13px; line-height: 1.65;">
                    • <strong>ASELSAN Aday Mühendislik Havuzu Üyesi.</strong><br>
                    • <strong>İstanbul Üniversitesi-Cerrahpaşa (İÜC)</strong> Elektrik-Elektronik Mühendisliği (3.44 GPA / Onur Derecesi).<br>
                    • <strong>TEKNOFEST Robotaksi</strong> Binek Otonom Araç Yarışması Finalisti.<br>
                    • Lazer tarayıcılar (LiDAR), sensörler, gömülü bilgisayarlar ve araç haberleşmesi uzmanı.<br>
                    • Donanım Kurulumu ve Saha Testleri Lideri.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 12: BEKLENTİLER -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ASELSAN'DAN BEKLENTİLERİMİZ: Birlikte Neler Yapabiliriz?</div>
        </div>
        <div class="grid-2x2">
            <div class="card card-blue">
                <div class="card-title">1. ASELSAN Araçlarında Ortak Saha Denemesi</div>
                <div class="card-desc">ASELSAN'ın mevcut insansız kara araçlarında yazılımımızı araca yükleyip arazide birlikte denemek.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Gerçekçi Askeri Test Alanı Desteği</div>
                <div class="card-desc">GPS uydularının kapalı olduğu kontrollü askeri test alanlarında yazılımımızın gücünü resmi olarak kanıtlamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Yerli Yazılım Tedarikçi Anlaşması</div>
                <div class="card-desc">Ön onayı tamamlanan Yazılım Geliştirme başvurumuzla birlikte ASELSAN'ın onaylı yazılım tedarikçisi olmak ve araç başı lisans modeliyle çalışmak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">4. Askeri Standartlar ve Uzman Desteği</div>
                <div class="card-desc">Askeri çevre koşullarına ve güvenlik kurallarına uyum sürecinde ASELSAN uzmanlarının tecrübesinden faydalanmak.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 13: KAPANIŞ -->
    <div class="slide" style="justify-content: center; align-items: flex-start; padding: 60px 80px; background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);">
        <div style="font-size: 14px; font-weight: 700; color: #0056B3; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px;">
            TEŞEKKÜR EDERİZ
        </div>
        <h1 style="font-size: 36px; font-weight: 900; color: #0B2545; line-height: 1.2; margin-bottom: 12px;">
            Milli Otonomi, Güçlü Savunma.
        </h1>
        <p style="font-size: 18px; color: #475569; margin-bottom: 40px; font-weight: 500;">
            ASELSAN ile birlikte sahada Mehmetçiğin can güvenliğini yerli otonomiyle korumak için hazırız.
        </p>
        
        <div style="border-top: 2px solid #E2E8F0; padding-top: 20px; width: 100%; font-size: 14px; color: #334155; line-height: 1.8;">
            <div><strong style="color: #0B2545;">Murat Furkan Bayram</strong> — Kurucu & Sistem Mimarı</div>
            <div><strong>E-posta:</strong> murat@trustia.com.tr | kariyer@trustia.com.tr  •  <strong>Telefon:</strong> +90 537 064 04 60</div>
            <div><strong>Web:</strong> trustia.com.tr  •  <strong>Merkez:</strong> İTO BTM Fulya Kampüsü, Şişli / İstanbul</div>
        </div>
    </div>

</div>

<!-- Navigation Controls -->
<div class="deck-controls">
    <button class="btn" onclick="prevSlide()">◀ Önceki</button>
    <div class="slide-counter" id="slideCounter">1 / 13</div>
    <button class="btn" onclick="nextSlide()">Sonraki ▶</button>
    <button class="btn" style="background: #10B981;" onclick="toggleFullScreen()">⛶ Tam Ekran</button>
</div>

<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const counter = document.getElementById('slideCounter');

    function showSlide(index) {{
        slides.forEach(s => s.classList.remove('active'));
        slides[index].classList.add('active');
        counter.textContent = (index + 1) + ' / ' + slides.length;
    }}

    function nextSlide() {{
        if (currentSlide < slides.length - 1) {{
            currentSlide++;
            showSlide(currentSlide);
        }}
    }}

    function prevSlide() {{
        if (currentSlide > 0) {{
            currentSlide--;
            showSlide(currentSlide);
        }}
    }}

    function toggleFullScreen() {{
        if (!document.fullscreenElement) {{
            document.documentElement.requestFullscreen();
        }} else {{
            if (document.exitFullscreen) {{
                document.exitFullscreen();
            }}
        }}
    }}

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {{
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
            nextSlide();
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
            prevSlide();
        }}
    }});
</script>

</body>
</html>
"""

with open(html_path_1, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(html_path_2, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated with ultra-clean Turkish text without tongue-twisters!")
