# 🌐 02_Trustia_Web_Platformu

> **Trustia AI Kurumsal Web ve 3D Telemetri Platformu (Next.js 16 / React 19 — v4.4 Enterprise)**

Bu dizin, [trustia.com.tr](https://trustia.com.tr) üzerinde yayında olan kurumsal web sitesini, Three.js 3D WebGL telemetri kokpitini ve uluslararası kurumsal politika portallarını barındırır.

---

## 🛠️ Teknoloji Yığını
- **Framework:** Next.js 16 (App Router, Statik HTML Çıktısı - `output: export`)
- **Arayüz Kütüphanesi:** React 19
- **Stil & Tasarım:** Tailwind CSS & Lucide Icons
- **Çoklu Dil (i18n):** Türkçe ve İngilizce tam metin desteği
- **3D Telemetri:** Three.js WebGL dijital ikiz kokpiti
- **SEO & AI Optimizasyonu:** JSON-LD Schema.org, `robots.txt`, `sitemap.xml`, `/llms.txt`

---

## 🚀 Geliştirme ve Derleme Komutları

```bash
cd website

# Bağımlılıkları yükleyin
npm install

# Yerel geliştirme sunucusunu başlatın (http://localhost:3000)
npm run dev

# Canlı dağıtım için statik derleme çıktısı alın
npm run build
```

---

## 🚢 CI/CD ve Dağıtım Hattı
GitHub `main` dalına yapılan her push işlemi, `.github/workflows/deploy.yml` üzerinden tetiklenir; Next.js projesini otomatik derleyerek Cloudflare korumalı GitHub Pages (`gh-pages`) dalına ve [trustia.com.tr](https://trustia.com.tr) etki alanına canlıya alır.

---
*© 2026 Trustia AI Technologies. Tüm hakları saklıdır.*
