# 🌋 Whisper Deprem Takip & Analiz Sistemi

> Türkiye geneli gerçek zamanlı sismik hareket takip, interaktif harita görselleştirme ve detaylı sismik analiz portalı. Stitch tasarımından ve modern glassmorphic temalardan esinlenilmiştir.

🌐 **Canlı Site (Vercel):** [https://whisper-deprem.vercel.app/](https://whisper-deprem.vercel.app/)

---

## ✨ Özellikler

### 🌋 Gerçek Zamanlı Deprem Takip & Analiz
- 📡 **Anlık Deprem Akışı:** Kandilli Rasathanesi API'si (ve yedek olarak USGS API) üzerinden Türkiye ve yakın çevresindeki son depremleri canlı listeleme.
- 🗺️ **İnteraktif Sismik Harita (Leaflet.js):** 
  - Son depremler büyüklüklerine göre renklendirilmiş halkalar ile gösterilir:
    - 🟢 Yeşil: <2.5 (Hafif)
    - 🟡 Sarı: 2.5 - 4.0 (Hissedilebilir)
    - 🟠 Turuncu: 4.0 - 5.5 (Orta)
    - 🔴 Kırmızı: >=5.5 (Kritik)
  - **En Son Deprem Dalgası:** Haritadaki en son depremin etrafında dışa doğru yayılan konsantrik sismik dalga animasyonları bulunur.
  - **Premium Konum İğnesi:** Seçilen şehri/merkezi gösteren, havada asılı kalıp yumuşakça süzülen (bobbing) ve altında dairesel dalgalar yayan altın sarısı animasyonlu bir konum iğnesi bulunur.
  - **İnteraktif Harita İmleçleri:** Harita üzerinde gezerken radar hedefi imleci, haritayı sürüklerken kilitlenmiş hedef imleci, depremlerin üzerine gelindiğinde ise sismik uyarı halkası imleci devreye girer.
  - **Harita Sınırları & Fay Hatları:** Karanlık ve uydu harita modlarında Türkiye sınırlarını veya fay hatlarını açıp kapatabilen kontrol butonları.
- 📊 **Detaylı İstatistikler & Grafikler:**
  - Bölgedeki en büyük depremin şiddeti, konumu, gerçekleşme tarihi ve saati.
  - Ortalama büyüklük, M4.0+ üzeri kritik deprem sayıları ve ortalama derinlik kartları.
  - **Son 30 Deprem Sismografı:** Son sismik aktivitelerin grafiksel dağılımı.
  - **Adaptif Saatlik/Günlük Dağılım:** Veri seti 36 saatten daha az bir süreyi kapsıyorsa (örn: bölgesel dar aramalar) 3'er saatlik aralıklarla **Saatlik Dağılım**, 36 saatten fazla ise **Son 7 Günlük Dağılım** bar grafiği otomatik olarak çizilir.
- 🗺️ **Sınır Dışı Depremler Projeksiyonu:** Sınır dışı/uluslararası bir deprem seçildiğinde, en yakın Türkiye il merkezine olan mesafesi (örn. `SINIR DIŞI (İzmir'e 80 km)`) otomatik hesaplanır ve "Bölgesel Analiz" sekmesinde bu en yakın bölgenin sismik verileri/istatistikleri listelenir.
- 📍 **Akıllı Konum Algılama:** IP tabanlı konum tespiti (`freeipapi` -> `ipapi.co` -> `db-ip` ardışık yedekli sistemi). Sistem başarısız olursa "Ankara, Türkiye" varsayılanına güvenli geçiş yapar.

---

## 🛠️ Teknoloji Stack

- **Frontend:** Pure JavaScript (Framework bağımsız, modern vanilla ES6)
- **Styling:** Tailwind CSS + Custom Tailwind CSS tokens + Glassmorphism & Keyframe Animations
- **Icons:** Google Material Symbols
- **Maps:** Leaflet.js
- **Builder:** Vite
- **APIs:**
  - 📡 **Kandilli Rasathanesi API** (orhanaydogdu.com.tr yansısı)
  - 🌍 **USGS Earthquake API** (Uluslararası sismik veriler)
  - 📍 **freeipapi.com**, **ipapi.co** & **db-ip.com** (Yedekli konum algılama)
  - 🗺️ **Open-Meteo Geocoding** (Şehir/İlçe arama motoru)

---

## 🚀 Kurulum & Çalıştırma

### Gereksinimler
- Node.js (v18+)
- npm veya yarn

### Adımlar

```bash
# Projeyi çalıştırın
cd whisper-deprem

# Bağımlılıkları kur
npm install

# Geliştirici sunucusunu (Vite) başlat
npm run dev
```

Tarayıcınızda terminalde belirtilen adresi (varsayılan: `http://localhost:5173`) açın.

---

## 📦 Production Build (Dağıtım)

Projeyi derlemek ve statik dosya paketini hazırlamak için:

```bash
# Production derlemesi oluştur
npm run build

# Yerel sunucuda derlemeyi önizle
npm run preview
```

Derleme sonrasında oluşan `/dist` klasörünü Vercel, Netlify veya GitHub Pages gibi dilediğiniz bir statik barındırma platformuna doğrudan yükleyebilirsiniz.

---

## 🤝 Katkıda Bulunma

Katkılarınız ve önerileriniz memnuniyetle karşılanır!

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.
