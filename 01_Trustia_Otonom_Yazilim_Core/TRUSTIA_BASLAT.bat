@echo off
cd /d "%~dp0"
title TRUSTIA v2.4 - Seviye-4 Otonomi ve Taktik C2 Kontrol Merkezi
cls
echo ===============================================================================
echo    TRUSTIA v2.4 - SEVIYE-4 DUAL-USE OTONOM MOBILITE VE TAKTIK C2 SISTEMI
echo    Kurucu: Murat Furkan Bayram (%%100 Hisse, Kurucu ^& CEO) - Tescil: AB PIC #861711529
echo ===============================================================================
echo.
echo  [1] Taktik C2 Masaustu Konsolunu Baslat (MIL-STD-2525 / STANAG 4586 GUI)
echo  [2] 1.307 Otomatik Test Validasyonunu Calistir (%%100 Yesil Test Kutuphanesi)
echo  [3] Yapay Zeka Tehdit, EYP ve KHKN Algilama Motorunu Calistir
echo  [4] Yerli Mimari, AB PIC ve NATO Uygunluk Sertifikasyon Denetimini Kostur
echo  [5] Hyundai Ioniq 5 Seviye-4 CAN-FD Otonom Surus Dongusunu Baslat
echo  [6] Kurumsal Kimlik, Devlet Tescilleri ve Akreditasyonlari Goruntule
echo  [7] Canli 3D WebGL Dijital Ikiz Kokpitini Baslat (Port 8090 / Tarayici)
echo  [8] MetaDrive 3D Masaustu Otonom Surus Simulasyonunu Baslat (Panda3D)
echo  [9] Ticari Lisans ve Dogrulama Durumunu Goruntule (Commercial License Status)
echo.
echo ===============================================================================
set /p secim="Lutfen calistirmak istediginiz islem numarasini giriniz (1-9): "

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
if "%secim%"=="9" python trustia_cli.py license

pause
