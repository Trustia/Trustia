@echo off
title TRUSTIA L4 ROBOTAXI — CAN-FD AKTÜATÖR SÜRÜŞ DÖNGÜSÜ (100 Hz)
color 0E
cd /d "%~dp0"
python robotaxi_cli.py drive
echo.
pause
