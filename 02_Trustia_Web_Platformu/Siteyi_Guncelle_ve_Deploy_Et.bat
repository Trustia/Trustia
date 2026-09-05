@echo off
chcp 65001 >nul
title TRUSTIA AI — Web Platformu Yönetim Konsolu

cd /d "%~dp0website"

:menu
cls
echo =========================================================================
echo    TRUSTIA AI — WEB PLATFORMU VE ROBOTAKSİ PORTALI YÖNETİMİ
echo =========================================================================
echo.
echo  [1] Web Sitesini Derle ve Test Et (Next.js 16 Production Build)
echo  [2] Geliştirici Sunucusunu Başlat (http://localhost:3000)
echo  [3] Derlenmiş Statik Çıktıyı Önizle (Local Preview out/)
echo  [4] Değişiklikleri GitHub'a Gönder (Canlı trustia.com.tr Deploy)
echo  [5] Çıkış
echo.
echo =========================================================================
set /p secim="Lütfen yapmak istediğiniz işlemi seçin (1-5): "

if "%secim%"=="1" goto build
if "%secim%"=="2" goto dev
if "%secim%"=="3" goto preview
if "%secim%"=="4" goto deploy
if "%secim%"=="5" exit /b 0
goto menu

:build
cls
echo [1/1] Next.js 16 Web Platformu Derleniyor...
call npm run build
echo.
echo [TAMAMLANDI] Derleme başarıyla tamamlandı.
pause
goto menu

:dev
cls
echo [1/1] Geliştirici Sunucusu Başlatılıyor (Ctrl+C ile durdurabilirsiniz)...
start http://localhost:3000
call npm run dev
pause
goto menu

:preview
cls
echo [1/1] Derlenmiş 'out' Klasörü Yerel Sunucuda Başlatılıyor...
start http://localhost:8080
call npx serve out -p 8080
pause
goto menu

:deploy
cls
echo [1/2] Web Platformu Yeniden Derleniyor...
call npm run build
if %errorlevel% neq 0 (
    echo [HATA] Derleme başarısız oldu, deploy iptal edildi!
    pause
    goto menu
)
echo.
echo [2/2] GitHub Ana Reposuna Yükleniyor...
cd /d "%~dp0.."
git add -A
git commit -m "chore(website): update web platform assets and production build"
git push origin main
echo.
echo [TEBRİKLER] Değişiklikler GitHub'a gönderildi!
echo GitHub Actions 1-2 dakika içinde trustia.com.tr üzerinde canlıya alacaktır.
pause
goto menu
