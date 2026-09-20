@echo off
chcp 65001 >nul
title TRUSTIA AI - NVIDIA GeForce GT 740 Sürücü ve Kurulum Yöneticisi

:MENU
cls
echo ======================================================================
echo       TRUSTIA AI - NVIDIA GEFORCE GT 740 SÜRÜCÜ VE KURULUM YÖNETİCİSİ
echo ======================================================================
echo.
echo  Mevcut Kart:  NVIDIA GeForce GT 420 (Eski)
echo  Yeni Kart:    Seclife NVIDIA GeForce GT 740 4GB (Kepler GK107)
echo.
echo  [1] Resmi NVIDIA GT 740 Sürücüsünü İndir (v472.12 WHQL - En Stabil)
echo  [2] Eski GT 420 Sürücüsünü Kaldırma Rehberi (Çakışma Önleyici)
echo  [3] GPU-Z İndir (Yeni Kartın Orijinalliğini Doğrulama)
echo  [4] Çıkış
echo.
echo ======================================================================
set /p SECIM="Seçiminiz (1-4): "

if "%SECIM%"=="1" goto INDIR
if "%SECIM%"=="2" goto REHBER
if "%SECIM%"=="3" goto GPUZ
if "%SECIM%"=="4" exit
goto MENU

:INDIR
cls
echo [*] Resmi NVIDIA GeForce v472.12 WHQL sürücüsü tarayıcınızda açılıyor...
start https://tr.download.nvidia.com/Windows/472.12/472.12-desktop-win10-win11-64bit-international-dch-whql.exe
echo.
echo [!] İndirme başladıktan sonra dosyayı kurabilirsiniz.
echo.
pause
goto MENU

:REHBER
cls
echo ======================================================================
echo           KART DEĞİŞİMİ VE TEMİZ KURULUM ADIMLARI
echo ======================================================================
echo.
echo 1. Bilgisayarı kapatın ve fişten çekin.
echo 2. Eski GT 420 kartını vidadan söküp mandalını açarak nazikçe çıkarın.
echo 3. Yeni GT 740 kartını PCI-e x16 yuvasına oturtup vidalayın.
echo 4. Monitör kablosunu (HDMI veya VGA) yeni GT 740'a takın.
echo 5. Bilgisayarı açın ve [1] seçeneğinden indirdiğiniz NVIDIA sürücüsünü
echo    "Özel Kurulum" -> "Temiz Kurulum Yap" kutucuğunu işaretleyerek kurun!
echo.
pause
goto MENU

:GPUZ
cls
echo [*] TechPowerUp Resmi GPU-Z indirme sayfası açılıyor...
start https://www.techpowerup.com/download/techpowerup-gpu-z/
echo.
pause
goto MENU
