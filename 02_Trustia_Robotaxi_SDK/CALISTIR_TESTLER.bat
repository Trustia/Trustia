@echo off
title TRUSTIA L4 ROBOTAXI — OTOMATIK DOGRULAMA TESTI
color 0A
cd /d "%~dp0"
python tests\test_sdk.py
echo.
pause
