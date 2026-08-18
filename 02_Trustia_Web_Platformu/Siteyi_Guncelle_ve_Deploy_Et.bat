@echo off
chcp 65001 >nul
title TRUSTIA AI — Web Sitesi Derleme ve Canliya Deploy Araci

echo ========================================================
echo   TRUSTIA AI - WEB SITESI CANLIYA AKTARMA (DEPLOY)
echo ========================================================
echo.

cd /d "%~dp0website"

echo [1/3] Next.js 16 Web Sitesi Derleniyor (npm run build)...
call npm run build
if %errorlevel% neq 0 (
    echo.
    echo [HATA] Derleme basarisiz oldu!
    pause
    exit /b %errorlevel%
)

echo.
echo [2/3] CNAME ve Dagitim Dosyalari Hazirlaniyor...
copy /y "%~dp0CNAME" "%~dp0website\out\CNAME" >nul 2>&1

set DEPLOY_DIR=%TEMP%\trustia_deploy_temp
if exist "%DEPLOY_DIR%" rmdir /s /q "%DEPLOY_DIR%"
mkdir "%DEPLOY_DIR%"

echo.
echo [3/3] GitHub Reposuna Yukleniyor (git push)...
git clone --depth 1 https://github.com/Trustia/Trustia.git "%DEPLOY_DIR%"
if %errorlevel% neq 0 (
    echo.
    echo [HATA] GitHub reposuna erisilemedi! Lutfen internet baglantinizi ve GitHub izinlerinizi kontrol edin.
    pause
    exit /b %errorlevel%
)

xcopy /s /e /y "%~dp0website\out\*" "%DEPLOY_DIR%\" >nul

cd /d "%DEPLOY_DIR%"
git config user.name "Trustia AI"
git config user.email "kariyer@trustia.com.tr"
git add -A
git commit -m "Deploy complete TR/EN bilingual website with language toggle"
git push origin main

echo.
echo ========================================================
echo   [TEBRIKLER] Web sitesi basariyla GitHub'a yuklendi!
echo   1-2 dakika icinde trustia.com.tr uzerinde canliya gececektir.
echo ========================================================
echo.
pause
