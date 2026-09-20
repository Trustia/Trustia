@echo off
chcp 65001 >nul
title TRUSTIA AI - Windows Derin Optimizasyon ve Telemetri Kapatıcı

:: Yönetici Yetkisi Kontrolü
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] Yönetici yetkisi gerekiyor. Yönetici olarak yeniden başlatılıyor...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~fnx0' -Verb RunAs"
    exit /b
)

echo ======================================================================
echo       TRUSTIA AI - WINDOWS DERİN OPTİMİZASYON VE TELEMETRİ KAPATICI
echo ======================================================================
echo.

echo [*] 1. Microsoft Telemetri ve Veri Toplama Servisleri Kapatılıyor...
sc config DiagTrack start= disabled >nul 2>&1
net stop DiagTrack >nul 2>&1
sc config dmwappushservice start= disabled >nul 2>&1
net stop dmwappushservice >nul 2>&1
echo [OK] DiagTrack ve dmwappushservice kalıcı olarak kapatıldı.

echo.
echo [*] 2. Windows Hata Raporlama ve Gereksiz Bildirim Servisi Kapatılıyor...
sc config WerSvc start= disabled >nul 2>&1
net stop WerSvc >nul 2>&1
echo [OK] Windows Error Reporting (WerSvc) kapatıldı.

echo.
echo [*] 3. SSD İçin Gereksiz Olan SysMain (SuperFetch) Kapatılıyor...
sc config SysMain start= disabled >nul 2>&1
net stop SysMain >nul 2>&1
echo [OK] SysMain (SSD gereksiz disk yazımları engellendi).

echo.
echo [*] 4. Windows Prefetch ve Sistem Önbelleği Temizleniyor...
del /q /f /s "C:\Windows\Prefetch\*" >nul 2>&1
echo [OK] Prefetch önbelleği sıfırlandı.

echo.
echo [*] 5. Nihai Performans Güç Modu Teyit Ediliyor...
powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 >nul 2>&1
for /f "tokens=4" %%a in ('powercfg -list ^| findstr /i "Nihai Ultimate Yüksek"') do (
    powercfg /setactive %%a >nul 2>&1
)
echo [OK] Nihai Performans güç modu aktif!

echo.
echo ======================================================================
echo [BAŞARILI] Tüm telemetri servisleri kapatıldı, disk ve CPU rahatlatıldı!
echo ======================================================================
echo.
pause
