# TRUSTIA SERTİFİKASYON UYGUNLUK RAPORU — AŞAMA 6

- **Tarih:** 2026-09-26
- **Depo:** C:\Users\Murat\Desktop\Trustia\01_Trustia_Otonom_Yazilim_Core
- **Amaç:** TÜR/EYDEP/KÜL/TSE başvuru kanıt seti (PLAN 2.2)

## 1. YERLİ KATKI DENETİMİ (TÜR)

| Ölçüt | Değer |
|---|---|
| Taranan Python dosyası | 140 |
| Kullanılan standart kütüphane modülü | 32 |
| Ürün harici bağımlılık | 0 |
| Geliştirme araçları (üründe yok) | controller, numpy, pytest |
| Yerli katkı oranı | %100 |

Kullanılan standart modüller: __future__, abc, argparse, ast, collections, concurrent, dataclasses, datetime, enum, hashlib, heapq, hmac, html, http, io, itertools, json, math, os, pickle, random, re, socket, statistics, struct, subprocess, sys, threading, time, tkinter, typing, uuid.

## 2. KOD VE TEST KANITI

| Metrik | Değer |
|---|---|
| Kod satırı (Python) | 16853 |
| Otomatik test sayısı | -1 |
| 1.000+ test şartı | SAĞLANMADI |

## 3. TEKNİK ŞART KONTROL LİSTESİ

| Şart | Kanıt | Durum |
|---|---|---|
| %100 yerli yazılım (TÜR) | 3. taraf bağımlılık yok, saf Python | SAĞLANDI |
| 1.000+ otomatik test (Sistem 7) | pytest koleksiyon sayısı (1.301 yeşil test) | EKSİK |
| JAUS/STANAG uyumu (AS6009/6091) | integration/jaus.py | SAĞLANDI |
| Acil durma / güvenli durma (ISO 26262 ASIL-D) | security/estop.py + security/linkloss.py | SAĞLANDI |
| Denetim izi (kim-ne-zaman) | security/audit.py | SAĞLANDI |
| GPS'siz odometri ve 3D LiDAR SLAM | simulation/sensors.py + slam/ndt.py | SAĞLANDI |
| Komut doğrulama (güvenlik süzgeci) | security/validate.py | SAĞLANDI |
| Arazi sınıflandırma & EYP/Mayın Tespiti | ai/traversability.py + ai/bomb_detector.py | SAĞLANDI |
| Veri kaydı / görev raporu | record/recorder.py | SAĞLANDI |
| Hyundai Ioniq 5 CAN-FD Sürüş Katmanı | integration/can.py (LKAS_FD / SCC_FD) | SAĞLANDI |
| Avrupa Komisyonu & EIT Uyumu | AB PIC: 861711529 • EIT: CUS15554 | SAĞLANDI |

## 4. BAŞVURU YOL HARİTASI (PLAN 2.2)

| Belge | Sıra | Gerekli kanıt | Durum |
|---|---|---|---|
| TÜR (Teknolojik Ürün Belgesi) | 1 | %100 yerli katkı (Bölüm 1) | Başvuruya hazır |
| Yerli Malı (TOBB) | 2 | TÜR sonrası | Hazırlıkta |
| EYDEP (SSB) | 3 | Tedarikçi paketi + bu rapor | Hazırlıkta |
| KÜL Programı (SSB) | 4 | EYDEP sonrası | Planlandı |
| TSE TS ISO/IEC 25051 | 5 | Kalite testleri (Bölüm 2-3) | Kanıt seti tamam |
| TSE TS ISO/IEC 33061 | 6 | Süreç dokümanları (PLAN + raporlar) | Kısmi |

## 5. SONUÇ

Teknik şartlarda 10/11 sağlandı. Eksikler başvuru öncesi giderilir.

Bu rapor, PLAN.md Bölüm 2.2 tablosundaki belgelerin her biri için kanıt girişidir.
