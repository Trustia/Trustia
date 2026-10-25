# TRUSTIA SEVİYE-4 OTONOM SÜRÜŞ ÇEKİRDEĞİ
## ALICI ENTEGRASYON VE HIZLI BAŞLANGIÇ KILAVUZU (v2.4)

Tebrikler! Trustia Seviye-4 Dual-Use Otonom Sürüş Motoru ticari lisanslı dağıtım paketini teslim aldınız. Bu yazılım; 3D LiDAR SLAM, Hybrid A* rota planlama, CAN-FD Drive-by-Wire araç kontrolü ve ISO 26262 ASIL-D emniyet katmanlarını içeren eksiksiz bir otonomi yığınıdır.

---

### 1. KURULUM (2 DAKİKA)

#### Seçenek A: Doğrudan Python Kurulumu (Önerilen)
Sistemde Python 3.11 veya 3.12 yüklü olduğundan emin olun:
```bash
# Paketin kök dizininde çalıştırın:
pip install -e .
```

#### Seçenek B: Docker ile Çalıştırma (İzole Konteyner)
Eğer arabanın bilgisayarında (NVIDIA Drive Orin veya Endüstriyel PC) Docker kullanıyorsanız:
```bash
docker compose up -d
```

---

### 2. TİCARİ LİSANSINIZI DOĞRULAYIN
Paketle birlikte teslim edilen `trustia.lic` dijital lisans anahtarınızı doğrulamak için:
```bash
python trustia_cli.py license
```
Ekranda şirketinizin adı, lisans süresi ve **"LİSANS GEÇERLİ VE ONAYLI"** ibaresi görünecektir.

---

### 3. SİSTEM DOĞRULAMA TESTLERİ (1.307 TEST)
Yazılımın aracınızda veya bilgisayarınızda sıfır hatayla çalıştığını doğrulamak için test paketini çalıştırın:
```bash
python trustia_cli.py test
```
Tüm 1.307 test yaklaşık 20-25 saniyede yeşil olarak tamamlanacaktır.

---

### 4. ARAÇ ÇALIŞTIRMA VE SİMÜLASYON

* **Hyundai Ioniq 5 / CAN-FD Otonom Sürüş Döngüsü:**
  ```bash
  python trustia_cli.py robotaxi
  ```

* **MetaDrive 3D Şehir Simülasyonu:**
  ```bash
  python trustia_metadrive_bridge.py
  ```

* **Canlı 3D Web Kokpiti:**
  ```bash
  python trustia_live_engine.py
  # Tarayıcıda açın: http://localhost:8090
  ```

* **İnteraktif Kontrol Menüsü:**
  Windows üzerinde doğrudan `TRUSTIA_BASLAT.bat` dosyasına çift tıklayarak tüm modülleri menüden yönetebilirsiniz.

---

### 5. DESTEK VE İLETİŞİM
Entegrasyon, sensör kalibrasyonu veya filo genişletme talepleriniz için:
* **Firma:** Trustia AI Technologies
* **Eser Sahibi:** Murat Furkan Bayram
* **E-posta:** iletisim@trustia.com.tr | destek@trustia.com.tr
* **Telefon:** +90 537 064 0460
