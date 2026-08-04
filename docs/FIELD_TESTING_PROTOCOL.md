# 🚜 TRUSTIA — SAHA VE DONANIM TEST PROTOKOLÜ

**Doküman Tarihi:** Ağustos 2026  
**Amaç:** İnsansız Kara Aracı (İKA) fiziksel saha sürüş ve güvenlik kalibrasyonu prosedürleri.

---

## 1. SAHA TESTİ ÖNCESİ GÜVENLİK KONTROL LİSTESİ

1. **Fiziksel E-Stop Butonu Kontrolü**: Araç üzerindeki mantar E-Stop anahtarının motor gücünü kestiği doğrulanmalı.
2. **Telsiz / Wi-Fi Sinyal Kontrolü**: Komuta merkezi ile araç arasındaki haberleşme sinyali test edilmeli.
3. **Sensör Aynaları ve Lazer Temizliği**: LiDAR aynalarının tozsuz ve temiz olduğu kontrol edilmeli.

---

## 2. SAHA SÜRÜŞ VE GÜVENLİK ADIMLARI

1. **Adım 1: Düşük Hız Manuel Sürüş (5 km/h)**: CAN-Bus direksiyon açısı ile fiziksel tekerlek açısının birebir çakıştığı doğrulanır.
2. **Adım 2: Engel Önünde Otonom Durma Testi**: Araç önüne 1.5 metre kala mukavva kutu koyularak otonom fren testi yapılır.
3. **Adım 3: LinkLoss Telsiz Kesintisi Testi**: İletişim bilerek kesilerek otonom eve dönüş (RTH) testi icra edilir.
