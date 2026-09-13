@echo off
chcp 65001 > nul
title TRUSTIA v2.4 - Taktik C2 Masaüstü Komuta Kontrol Konsolu
cd /d "%~dp0"
python -m command.tactical_gui
pause
