# TRUSTIA SERTİFİKASYON UYGUNLUK RAPORU — AŞAMA 6

- **Tarih:** 2026-08-18
- **Depo:** C:\Users\Murat\Desktop\Trustia\01_Trustia_Otonom_Yazilim_Core
- **Amaç:** TÜR/EYDEP/KÜL/TSE başvuru kanıt seti (PLAN 2.2)

## 1. YERLİ KATKI DENETİMİ (TÜR)

| Ölçüt | Değer |
|---|---|
| Taranan Python dosyası | 129 |
| Kullanılan standart kütüphane modülü | 30 |
| Ürün harici bağımlılık | 1 |
| Harici modüller | controller |
| Geliştirme araçları (üründe yok) | numpy, pytest |
| Yerli katkı oranı | %0 |

Kullanılan standart modüller: __future__, abc, argparse, ast, collections, concurrent, dataclasses, datetime, enum, hashlib, heapq, hmac, html, io, itertools, json, math, os, pickle, random, re, statistics, struct, subprocess, sys, threading, time, tkinter, typing, uuid.

## 2. KOD VE TEST KANITI

| Metrik | Değer |
|---|---|
| Kod satırı (Python) | 15493 |
| Otomatik test sayısı | 1276 |
| 1.000+ test şartı | SAĞLANDI |

## 3. TEKNİK ŞART KONTROL LİSTESİ

| Şart | Kanıt | Durum |
|---|---|---|
| %100 yerli yazılım (TÜR) | 3. taraf bağımlılık yok, saf Python | EKSİK |
| 1.000+ otomatik test (Sistem 7) | pytest koleksiyon sayısı | SAĞLANDI |
| JAUS/STANAG uyumu (AS6009/6091) | integration/jaus.py | SAĞLANDI |
| Acil durma / güvenli durma | security/estop.py | SAĞLANDI |
| Denetim izi (kim-ne-zaman) | security/audit.py | SAĞLANDI |
| GPS'siz odometri (sertifika farkı) | simulation/gps-koridor + core odometri | SAĞLANDI |
| Komut doğrulama (güvenlik süzgeci) | security/validate.py | SAĞLANDI |
| Arazi sınıflandırma (Sistem 9) | ai/traversability.py | SAĞLANDI |
| Veri kaydı / görev raporu | record/recorder.py | SAĞLANDI |

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

Teknik şartlarda 8/9 sağlandı. Eksikler başvuru öncesi giderilir.

Bu rapor, PLAN.md Bölüm 2.2 tablosundaki belgelerin her biri için kanıt girişidir.
