@echo off
chcp 65001 > nul
title TRUSTIA v2.4 - Seviye-4 Otonomi & Taktik C2 Kontrol Merkezi
cls
echo ===============================================================================
echo    TRUSTIA v2.4 — SEVİYE-4 DUAL-USE OTONOM MOBİLİTE & TAKTİK C2 SİSTEMİ
echo    Kurucu: Murat Furkan Bayram (17 Yaş, %%80) • Tescil: AB PIC #861711529
echo ===============================================================================
echo.
echo  [1] Taktik C2 Masaüstü Konsolunu Başlat (MIL-STD-2525 / STANAG 4586 GUI)
echo  [2] 1.301 Otomatik Test Validasyonunu Çalıştır (%%100 Yeşil Test Kütüphanesi)
echo  [3] Yapay Zeka Tehdit, EYP ve KHKN Algılama Motorunu Çalıştır
echo  [4] Yerli Mimari, AB PIC ve NATO Uygunluk Sertifikasyon Denetimini Koştur
echo  [5] Hyundai Ioniq 5 Seviye-4 CAN-FD Otonom Sürüş Döngüsünü Başlat
echo  [6] Kurumsal Kimlik, Devlet Tescilleri ve Akreditasyonları Görüntüle
echo  [7] Canlı 3D WebGL Dijital İkiz Kokpitini Başlat (Port 8090 / Tarayıcı)
echo  [8] MetaDrive 3D Masaüstü Otonom Sürüş Simülasyonunu Başlat (Panda3D / Sokak & Trafik)
echo.
echo ===============================================================================
set /p secim="Lütfen çalıştırmak istediğiniz işlem numarasını giriniz (1-8): "

if "%secim%"=="1" python trustia_cli.py gui
if "%secim%"=="2" python trustia_cli.py test
if "%secim%"=="3" python trustia_cli.py threats
if "%secim%"=="4" python trustia_cli.py audit
if "%secim%"=="5" python trustia_cli.py robotaxi
if "%secim%"=="6" python trustia_cli.py info
if "%secim%"=="7" (
    start "" "http://localhost:8090"
    python trustia_live_engine.py
)
if "%secim%"=="8" python trustia_metadrive_bridge.py

pause

