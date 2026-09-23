import os

html_path_1 = r"C:\Users\Murat\Downloads\Trustia_ASELSAN_Sunumu.html"
html_path_2 = r"C:\Users\Murat\Desktop\Trustia\Kurumsal\Sunumlar\Trustia_ASELSAN_Sunumu.html"
logo_path = r"c:/Users/Murat/Desktop/Trustia/Kurumsal/Medya/Logo.png"
car_path = r"c:/Users/Murat/Desktop/Trustia/Kurumsal/Medya/Arac_Lidar.png"

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TRUSTIA AI — ASELSAN Girişimcilik Merkezi Sunumu</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}
        body {{
            background: #0B192C;
            color: #1E293B;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }}
        .deck-container {{
            width: 1200px;
            height: 675px;
            background: #FFFFFF;
            border-radius: 12px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        .slide {{
            display: none;
            width: 100%;
            height: 100%;
            padding: 40px 55px;
            flex-direction: column;
            position: relative;
        }}
        .slide.active {{
            display: flex;
        }}
        .slide-header {{
            margin-bottom: 24px;
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 12px;
        }}
        .slide-tag {{
            font-size: 11px;
            font-weight: 700;
            color: #0056B3;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }}
        .slide-title {{
            font-size: 24px;
            font-weight: 800;
            color: #0B2545;
        }}
        .content-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .card {{
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px 20px;
        }}
        .card.card-blue {{ border-left: 5px solid #0056B3; }}
        .card.card-red {{ border-left: 5px solid #DC2626; }}
        .card-title {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 6px;
        }}
        .card.card-blue .card-title {{ color: #0B2545; }}
        .card.card-red .card-title {{ color: #991B1B; }}
        .card-desc {{
            font-size: 14px;
            line-height: 1.55;
            color: #334155;
        }}
        .grid-2x2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
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
            font-size: 14px;
            font-weight: 600;
            border-radius: 20px;
            cursor: pointer;
            transition: 0.2s;
        }}
        .btn:hover {{ background: #0070E0; }}
        .slide-counter {{
            color: #FFF;
            font-size: 13px;
            font-weight: 600;
            min-width: 80px;
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
            TRUSTIA TEKNOLOJİ A.Ş.
        </div>
        <h1 style="font-size: 34px; font-weight: 900; color: #0B2545; line-height: 1.2; margin-bottom: 12px;">
            Milli Otonom Sürüş Platformu & İnsansız Kara Aracı Beyni
        </h1>
        <p style="font-size: 18px; color: #475569; margin-bottom: 40px; font-weight: 500;">
            GPS Olmadan Lazerle Haritalama Yapan ve Elektronik Karıştırmadan Etkilenmeyen Yerli Yazılım
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
                <div class="card-title">1. GPS Sinyalinin Kesilmesi veya Yanıltılması</div>
                <div class="card-desc">Savaş ve operasyon bölgelerinde düşman sinyal bozucuları (jamming) GPS'i tamamen kesmektedir. Pazardaki standart otonom araçlar uydu bağlantısı koptuğunda haritayı ve rotayı kaybedip hareketsiz kalmakta ve vurulmaya açık hedef olmaktadır.</div>
            </div>
            <div class="card card-red">
                <div class="card-title">2. Uzaktan Kumanda (Telsiz) Bağlantısının Kopması</div>
                <div class="card-desc">Uzaktan kumandayla yönlendirilen insansız araçların telsiz bağı koptuğunda araç olduğu yerde kilitlenmektedir. Ayrıca sinyalin gecikmeli gitmesi ani tehlikelerde kazalara yol açmaktadır.</div>
            </div>
            <div class="card card-red">
                <div class="card-title">3. Yabancı Otonomi Yazılımlarına Bağımlı Olunması</div>
                <div class="card-desc">Piyasadaki hazır otonom yazılımlar yabancı menşeilidir. Bu yazılımlar askeri savunma standartlarına uyum sağlamaz, siber güvenlik açıkları taşır ve Türk savunma sistemlerine doğrudan bağlanamaz.</div>
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
                <div class="card-title">1. GPS Olmadan Lazer (LiDAR) ile 3 Boyutlu Haritalama</div>
                <div class="card-desc">GPS uydusu tamamen kapansa bile; araç üzerindeki 3 boyutlu lazer tarayıcı (LiDAR) ve hareket sensörleri sayesinde araç kendi haritasını santim santim kendisi çıkarır ve rotasında kaybolmadan ilerler.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Telsiz Bağlantısı Koptuğunda Otonom Eve Dönüş</div>
                <div class="card-desc">Kumanda veya telsiz bağlantısı koptuğu anda araç panik yapmaz. Hafızasındaki lazer haritayı takip ederek güvenli başlangıç noktasına (üs bölgesine) kendi kendine geri döner.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. %100 Yerli Kod ve ASELSAN Sistemlerine Tam Uyum</div>
                <div class="card-desc">Yazılımın tüm kodları sıfırdan yerli olarak geliştirilmiştir. Askeri haberleşme kurallarına ve ASELSAN kara sistemlerine doğrudan tak-çalıştır şeklinde bağlanabilir.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 4: ÜRÜN -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ÜRÜN: Trustia Otonomi Beyni ve Taktik Kontrol Konsolu</div>
        </div>
        <div class="two-cols">
            <div class="col-left">
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Akıllı Sürüş ve Rota Planlayıcı</div>
                    <div class="card-desc" style="font-size: 13px;">Lazer sensörlerle çevreyi tarar, yoldaki çukurları, kayaları ve hareketli hedefleri anında algılayıp etrafından güvenle dolaşır.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Askeri Tehlike Algılama Modülleri</div>
                    <div class="card-desc" style="font-size: 13px;">Yoldaki mayın veya el yapımı patlayıcı şüpheli cisimleri tespit eder ve 30 metre geriden aracı durdurup güvenli bölgeye alır.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• Taktik Komuta Konsolu (Ekran)</div>
                    <div class="card-desc" style="font-size: 13px;">Askeri harita destekli komuta ekranı. Operatör tablet üzerinden tek tıkla araca hedef verir veya acil durumda anında durdurur.</div>
                </div>
                <div class="card card-blue" style="padding: 12px 16px;">
                    <div class="card-title" style="font-size: 14px;">• 1.301 Test ile Kanıtlanmış Güvenlik</div>
                    <div class="card-desc" style="font-size: 13px;">16.000 satırlık yazılım çekirdeği 1.301 farklı zorlu kaza ve arazi senaryosunda test edilmiş ve %100 başarıyla tamamlanmıştır.</div>
                </div>
            </div>
            <div class="col-right">
                <img src="{car_path}" alt="Trustia Otonomi Platformu" style="width: 100%; max-height: 180px; object-fit: contain; margin-bottom: 12px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 8px;">TEKNİK ÖZELLİKLER</div>
                <div style="font-size: 12.5px; line-height: 1.6; color: #1E293B; width: 100%;">
                    ✓ Haberleşme: Askeri ve Robot Standartları Uyumlu<br>
                    ✓ Bilgisayar: Nvidia Jetson ve Endüstriyel PC'ler<br>
                    ✓ Sensörler: 3D Lazer (LiDAR), Kamera, Hareket Sensörü<br>
                    ✓ Tepki Hızı: 5 Milisaniyede Müdahale Edebilme<br>
                    ✓ Durum: Çalışır Prototip, Teste Hazır
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 5: ALTYAPILAR -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">ALTYAPILAR: Test Parkımız ve Resmi Tescillerimiz</div>
        </div>
        <div class="grid-2x2">
            <div class="card card-blue">
                <div class="card-title">İTO BTM Fulya Kampüsü</div>
                <div class="card-desc">İstanbul Ticaret Odası bünyesindeki Fulya Derin Teknoloji Kampüsü'nde sözleşmeli kuluçka merkezimiz. Ar-Ge, yazılım ve laboratuvar altyapımız buradadır.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">Yazılım ve Donanım Test Cihazları</div>
                <div class="card-desc">Yapay zeka araç bilgisayarları (Jetson Orin), 3 boyutlu lazer tarayıcılar (LiDAR), açı ölçer sensörler ve araç içi elektronik bağlantı kablolama ekipmanlarımız mevcuttur.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">1.301 Testli Sanal Test Odası</div>
                <div class="card-desc">Gerçek dünyaya çıkmadan önce yazılımımızı 1.301 farklı simülasyon senaryosunda (sis, çamur, gece, radar karıştırması) 43 saniyede otomatik test eden sistemimiz aktiftir.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">Resmi Akreditasyonlar</div>
                <div class="card-desc">ASELSAN Potansiyel Tedarikçi Onayı (SAP: FZQHEXGFMTJU), NATO Askeri Tedarikçi Başvurusu (NCAGE), TÜBİTAK ARBİS Kaydı ve Savunma Sanayii Sertifikalarımız.</div>
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
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">DÜNYA PAZARI (TAM)</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">15.8 Milyar $</div>
                </div>
                <div class="card-desc">Dünyadaki askeri insansız kara araçları ve taktik otonomi sistemlerinin toplam yıllık pazar büyüklüğü.</div>
            </div>
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 25px 20px;">
                <div>
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">BÖLGESEL PAZAR (SAM)</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">1.2 Milyar $</div>
                </div>
                <div class="card-desc">Türkiye, NATO ve dost ülkelerdeki sınır güvenliği, otonom konvoy ve taktik araç yazılımları pazarı.</div>
            </div>
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 25px 20px;">
                <div>
                    <div style="font-size: 13px; font-weight: 700; color: #64748B;">BİZİM HEDEFİMİZ (SOM)</div>
                    <div style="font-size: 32px; font-weight: 900; color: #0056B3; margin: 15px 0;">45 Milyon $</div>
                </div>
                <div class="card-desc">ASELSAN ve TSK kara araçlarının otonomlaştırılması projelerinde ilk 3 yılda hedeflediğimiz yerli yazılım payı.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 7: RAKİP ANALİZİ -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">RAKİP ANALİZİ: Taktik Saha İhtiyaçları Karşılaştırması</div>
        </div>
        <div class="content-body">
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th>Özellik / Yetenek</th>
                        <th style="background: #0056B3; text-align: center;">TRUSTIA AI (Yerli)</th>
                        <th style="text-align: center;">Klasik Uzaktan Kumanda</th>
                        <th style="text-align: center;">Yabancı Açık Kaynaklar</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>GPS Olmadan Haritalama (Lazerle)</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tam Uyumlu</td>
                        <td style="text-align: center;" class="val-bad">✗ Yok (GPS Şart)</td>
                        <td style="text-align: center;" class="val-mid">△ Şehir Haritası Şart</td>
                    </tr>
                    <tr>
                        <td><strong>Askeri ve NATO Standartlarına Uyum</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tam Uyumlu</td>
                        <td style="text-align: center;" class="val-mid">△ Standartsız Telsiz</td>
                        <td style="text-align: center;" class="val-bad">✗ Askeri Uyum Yok</td>
                    </tr>
                    <tr>
                        <td><strong>%100 Yerli Kod Bağımsızlığı</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Tamamen Yerli</td>
                        <td style="text-align: center;" class="val-mid">△ Donanıma Bağımlı</td>
                        <td style="text-align: center;" class="val-bad">✗ Yabancı Bağımlı</td>
                    </tr>
                    <tr>
                        <td><strong>Bağlantı Kopunca Kendi Kendine Dönüş</strong></td>
                        <td style="text-align: center;" class="val-good">✓ Otonom Eve Dönüş</td>
                        <td style="text-align: center;" class="val-bad">✗ Araç Olduğu Yerde Kalır</td>
                        <td style="text-align: center;" class="val-mid">△ Belirsiz</td>
                    </tr>
                    <tr>
                        <td><strong>1.301 Testli Doğrulanmış Prototip</strong></td>
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
                <div class="card-desc">ASELSAN'ın ürettiği veya modernize ettiği her bir insansız kara aracı başına otonomi yazılımı lisans bedeli faturalandırılması.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Özel Görev Modülleri Satışı</div>
                <div class="card-desc">Temel sürüşe ek olarak; Mayın Tespit Paketi, Zehirli Gaz Kaçınma Paketi veya Sürü Halinde İlerleme Paketi gibi ilave yazılım modülleri satışı.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Entegrasyon, Saha Testi ve Yıllık Bakım Anlaşmaları</div>
                <div class="card-desc">Yeni zırhlı araçlara sensör ve yazılım bağlama mühendisliği, arazide test desteği ve yıllık yazılım güncelleme/bakım sözleşmeleri.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 9: PAZARA GİRİŞ STRATEJİSİ -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">PAZARA GİRİŞ STRATEJİSİ: Adım Adım Büyüme Planımız</div>
        </div>
        <div class="content-body">
            <div class="card card-blue">
                <div class="card-title">1. Aşama: ASELSAN Araçlarında Saha Testi (2026)</div>
                <div class="card-desc">ASELSAN Girişimcilik Merkezi (Axcelerate) desteğiyle ASELSAN'ın taktik kara araçlarında yazılımımızı arazide test edip ilk ortak başarıyı yakalamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Aşama: Türk Savunma Sanayii Araçlarına Yayılım (2027)</div>
                <div class="card-desc">ASELSAN onaylı tedarikçi gücüyle; zırhlı araç üreticilerinin (FNSS, BMC, vb.) tekerlekli ve paletli araçlarına otonom devriye ve konvoy beyni sağlamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Aşama: Dost ve Müttefik Ülkelere İhracat (2027-2028)</div>
                <div class="card-desc">NATO tedarikçi kodumuz ve uluslararası patent korumamızla, dost ülke ordularının insansız araç projelerine milli yazılımımızı ihraç etmek.</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 10: YOL HARİTASI -->
    <div class="slide">
        <div class="slide-header">
            <div class="slide-tag">ASELSAN GİRİŞİMCİLİK MERKEZİ BAŞVURU SUNUMU</div>
            <div class="slide-title">PLANLANAN YOL HARİTASI: 2026 - 2028 Hedeflerimiz</div>
        </div>
        <div class="grid-4">
            <div class="card card-blue" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 6px;">ŞU ANKİ DURUM</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Çalışır Prototip</div>
                <div class="card-desc" style="font-size: 12.5px;">16.000 satır yerli kod, 1.301 birim test ile doğrulandı. ASELSAN Tedarikçi Portalı Yazılım Ön Onayı alındı.</div>
            </div>
            <div class="card card-blue" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #0056B3; margin-bottom: 6px;">YIL SONU HEDEFİ</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">ASELSAN Saha Testi</div>
                <div class="card-desc" style="font-size: 12.5px;">Axcelerate kabulü ile ASELSAN taktik aracında kapalı alanda ve arazide ilk gerçek saha sürüş testinin yapılması.</div>
            </div>
            <div class="card" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #64748B; margin-bottom: 6px;">2027 İLK YARI</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Seri Lisanslama</div>
                <div class="card-desc" style="font-size: 12.5px;">İlk 10 taktik kara aracı için seri yazılım lisans teslimatı ve komuta ekranı tam entegrasyonu.</div>
            </div>
            <div class="card" style="padding: 16px;">
                <div style="font-size: 13px; font-weight: 700; color: #64748B; margin-bottom: 6px;">2027 - 2028</div>
                <div style="font-size: 15px; font-weight: 700; color: #0B2545; margin-bottom: 8px;">Sürü ve İhracat</div>
                <div class="card-desc" style="font-size: 12.5px;">Çoklu araçların sürü halinde birlikte hareket etmesi ve dost/müttefik ülkelere yazılım ihracatı.</div>
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
                    • 16.000 satırlık Trustia Otonomi Çekirdeğinin mimarı ve yazarı.<br>
                    • 1.301 otomatik test senaryosunun geliştiricisi (%100 başarı).<br>
                    • TÜBİTAK ARBİS, BTK Savunma ve KOSGEB İleri Girişimci tescilleri sahibi.<br>
                    • Çekirdek Yazılım, Rota Planlama ve Algoritma Lideri.
                </div>
            </div>
            <div class="card card-blue" style="padding: 24px;">
                <div style="font-size: 20px; font-weight: 800; color: #0B2545;">Denizcan Özcan</div>
                <div style="font-size: 14px; font-weight: 700; color: #0056B3; margin: 4px 0 14px 0;">Baş Donanım ve Entegrasyon Mühendisi</div>
                <div class="card-desc" style="font-size: 13.5px; line-height: 1.7;">
                    • <strong>ASELSAN Aday Mühendislik Havuzu Üyesi.</strong><br>
                    • TEKNOFEST Robotaksi Finalisti.<br>
                    • Lazer tarayıcılar (LiDAR), sensörler, gömülü bilgisayarlar ve araç içi CAN haberleşme uzmanı.<br>
                    • Donanım Entegrasyonu ve Saha Testleri Lideri.
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
                <div class="card-title">1. ASELSAN Araçlarında Ortak Saha Testi</div>
                <div class="card-desc">ASELSAN'ın mevcut insansız kara araçlarında (örneğin Aslan veya Ertuğrul) yazılımımızı araca yükleyip arazide birlikte test etmek.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">2. Askeri Test Sahası Desteği</div>
                <div class="card-desc">GPS uydularının kasıtlı olarak karartıldığı kontrollü askeri test sahalarında algoritmalarımızın başarısını resmi olarak kanıtlamak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">3. Yerli Yazılım Tedarikçi Sözleşmesi</div>
                <div class="card-desc">Ön onayı tamamlanan Yazılım Geliştirme başvurumuzla birlikte ASELSAN'ın onaylı yazılım tedarikçisi olmak ve araç başı lisanslama modeliyle çalışmak.</div>
            </div>
            <div class="card card-blue">
                <div class="card-title">4. Askeri Standartlaşma ve Mentorluk</div>
                <div class="card-desc">Askeri çevre koşullarına ve güvenlik standartlarına uyum sürecinde ASELSAN uzmanlarının teknik tecrübesinden faydalanmak.</div>
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
            ASELSAN ile birlikte muharebe sahasında Mehmetçiğin can güvenliğini milli otonomiyle korumak için hazırız.
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

print("Updated with ultra-clean Turkish text!")
