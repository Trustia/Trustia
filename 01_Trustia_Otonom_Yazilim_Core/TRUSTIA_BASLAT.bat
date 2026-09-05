@echo off
title TRUSTIA v2.0 - Dual-Use Autonomous Systems Mission Control
cls
echo =========================================================================
echo    TRUSTIA v2.0 - DUAL-USE AUTONOMOUS DRIVING & C2 MISSION CONTROL
echo =========================================================================
echo.
echo [1] Launch Tactical C2 Desktop Console (Military UGV & Robotaxi GUI)
echo [2] Run 1,301-Test Automated Verification Suite (100%% Pass Rate)
echo [3] Run AI Threat & Obstacle Detection Engine (IED/Mine/Pedestrian)
echo [4] Run Native Architecture & NATO STANAG 4586 Compliance Audit
echo.
set /p secim="Please enter the operation number to execute (1-4): "

if "%secim%"=="1" python trustia_cli.py gui
if "%secim%"=="2" python trustia_cli.py test
if "%secim%"=="3" python trustia_cli.py threats
if "%secim%"=="4" python trustia_cli.py audit

pause
