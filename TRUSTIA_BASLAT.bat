@echo off
title TRUSTIA v2.0 - Milli Otonomi Platformu Yonetim Konsolu
cls
echo =========================================================================
echo    TRUSTIA v2.0 - MILLI OTONOMI PLATFORMU KURUMSAL YONETIM KONSOLU
echo =========================================================================
echo.
echo [1] Taktik Masaustu Konsolunu Baslat (C2 Desktop App)
echo [2] %%100 Yerli Katki AST Sertifikasyon Denetimini Calistir
echo [3] 1.273 Adet Birim ve Entegrasyon Testini Kostur
echo [4] Askeri EYP, Mayin ve KHKN Tehdit Analizini Calistir
echo.
set /p secim="Lutfen calistirmak istediginiz islem numarasini girin (1-4): "

if "%secim%"=="1" python trustia_cli.py gui
if "%secim%"=="2" python trustia_cli.py audit
if "%secim%"=="3" python trustia_cli.py test
if "%secim%"=="4" python trustia_cli.py threats

pause
