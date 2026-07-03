# Whisper Deprem — Ürün Gereksinimler Belgesi (PRD)

**Sürüm:** 1.0  
**Tarih:** 03 Temmuz 2026  
**Proje:** Whisper Deprem — Türkiye Deprem Takip ve Analiz Sistemi  
**Teknoloji:** Vite + Vanilla JS + Leaflet.js + Tailwind CSS  
**URL:** http://localhost:5173 (geliştirme)

---

## 1. Ürün Özeti

Whisper Deprem, Türkiye'deki deprem aktivitelerini gerçek zamanlı olarak izleyen, arşiv verileri üzerinden analiz yapabilen ve kullanıcıları yeni depremlerden anında haberdar eden bir web uygulamasıdır. Kandilli Rasathanesi API'si ve USGS verileriyle beslenmektedir.

---

## 2. Hedef Kitle

- Türkiye'de yaşayan ve deprem riskini takip etmek isteyen bireyler
- Deprem araştırmacıları ve jeoloji meraklıları
- Acil durum yönetimi ve haberdar olma ihtiyacı duyan kurumsal kullanıcılar

---

## 3. Temel Özellikler

### 3.1 Etkileşimli Deprem Haritası

| Özellik | Açıklama | Durum |
|---|---|---|
| Karanlık harita modu | CartoDB Dark All tile katmanı | ✅ Mevcut |
| Uydu harita modu | Esri World Imagery + label katmanı | ✅ Mevcut |
| Deprem marker'ları | Büyüklüğe göre renk kodlu, animasyonlu noktalar | ✅ Mevcut |
| En son deprem animasyonu | Dalga yayan, nabız atan marker | ✅ Mevcut |
| Kullanıcı konum pini | Animasyonlu altın rengi iğne | ✅ Mevcut |
| Popup bilgi kartı | Deprem detayları (yer, mag, derinlik, saat) | ✅ Mevcut |
| Türkiye / Bölge sınırları | GeoJSON ile çizilen parıldayan sınır çizgileri | ✅ Mevcut |
| Fay hatları katmanı | Türkiye + Dünya tektonik plaka fay hatları (uydu modunda) | ✅ Mevcut |
| Harita üzerine zoom | `flyTo()` ile animasyonlu zoom | ✅ Mevcut |
| Özel radar imleci | Hedef/crosshair tarzı SVG imleç | ✅ Mevcut |
| Uydu modu özel imleç | Dönen halkalı animasyonlu imleç | ✅ Mevcut |

### 3.2 Deprem Listesi (Depremler Sekmesi)

| Özellik | Açıklama | Durum |
|---|---|---|
| Canlı deprem kartları | Büyüklük, yer, saat, derinlik bilgisi | ✅ Mevcut |
| Büyüklük filtresi | Tümü / M2+ / M3+ / M4+ chip butonları | ✅ Mevcut |
| Kapsam seçici | Bölge / Tüm TR toggle butonları | ✅ Mevcut |
| Tarih navigasyonu | ◀ ▶ ile son 7 güne gidebilme (arşiv modu) | ✅ Mevcut |
| Depreme tıklama | Seçilen depreme haritada zoom, popup açılır | ✅ Mevcut |
| Renk kodlu kartlar | Büyüklüğe göre sol border rengi | ✅ Mevcut |

### 3.3 Analiz & Grafikler Sekmesi

| Özellik | Açıklama | Durum |
|---|---|---|
| En büyük deprem kartı | Büyüklük, yer, zaman | ✅ Mevcut |
| Ortalama büyüklük kartı | Seçili kapsama göre | ✅ Mevcut |
| M4+ sayısı kartı | Güçlü deprem adedi | ✅ Mevcut |
| Ortalama derinlik kartı | km cinsinden | ✅ Mevcut |
| Sismograf grafiği | Son 30 deprem SVG çizgisi (interaktif tooltip) | ✅ Mevcut |
| Günlük bar grafiği | Son 7 günlük aktivite çubuk grafiği | ✅ Mevcut |

### 3.4 Arama ve Konum

| Özellik | Açıklama | Durum |
|---|---|---|
| Şehir/bölge arama | Otomatik tamamlamalı arama kutusu | ✅ Mevcut |
| 81 il desteği | Tüm Türkiye illeri dahil | ✅ Mevcut |
| Rastgele şehir | "Şansıma bırak" tarzı rastgele il seçimi | ✅ Mevcut |
| Konum kalıcılığı | localStorage ile son konum saklanır | ✅ Mevcut |

### 3.5 Bildirim Sistemi

| Özellik | Açıklama | Durum |
|---|---|---|
| Toast bildirimi | Sol alt köşeden kayan animasyonlu kart | ✅ Mevcut |
| Tarayıcı push bildirimi | M4+ için sistem bildirimi (Notification API) | ✅ Mevcut |
| Ses alarmı | Büyüklüğe göre değişen bip sesi (Web Audio API) | ✅ Mevcut |
| Sadece canlı modda bildirim | Geçmiş günlere gidince bildirim gelmiyor | ✅ Düzeltildi |
| Toast tıklaması → Bugüne dön | Geçmiş gündeyken bildirime tıklayınca bugüne geçer | ✅ Düzeltildi |
| Tıklama → Harita zoom | Bildirime tıklanınca depremin konumuna flyTo yapılır | ✅ Düzeltildi |
| 30 saniyede bir yenileme | Sadece canlı modda otomatik veri çekimi | ✅ Mevcut |

### 3.6 UI / UX

| Özellik | Açıklama | Durum |
|---|---|---|
| Karanlık tema | Tam karanlık renk paleti | ✅ Mevcut |
| Grid arka plan | 24px grid çizgi deseni | ✅ Mevcut |
| Glassmorphism kartlar | Blur + şeffaf arka plan | ✅ Mevcut |
| Türkiye saati (UTC+3) | Header'da gerçek zamanlı saat | ✅ Mevcut |
| Yükleme ekranı | Spinner overlay ile yükleniyor durumu | ✅ Mevcut |
| Hata toast'ı | API hata durumunda bilgilendirme | ✅ Mevcut |
| Responsive tasarım | Mobil (dikey) + Masaüstü (yan yana) | ✅ Mevcut |
| Footer bilgi çubuğu | Tespit edilen bölge + istatistik özeti | ✅ Mevcut |

---

## 4. Veri Kaynakları

| Kaynak | Kullanım Amacı |
|---|---|
| Kandilli API (orhanaydogdu.com.tr) | Türkiye canlı ve arşiv deprem verileri |
| USGS FDSNWS | Türkiye dışı yedek kaynak + küresel veriler |
| CartoDB Dark Tiles | Karanlık harita tile katmanı |
| Esri World Imagery | Uydu harita tile katmanı |
| turkey-faults-full.json | Türkiye fay hattı GeoJSON verisi |
| world-faults.json | Dünya tektonik plaka sınırları |
| tr-cities-utf8.json | Türkiye şehir koordinat veritabanı |

---

## 5. Teknik Mimari

```
whisper-deprem/
├── index.html          # Tek sayfa uygulama (HTML + Tailwind)
├── src/
│   ├── earthquake.js   # Ana uygulama mantığı (~2300 satır)
│   ├── tr-cities-utf8.json
│   ├── turkey-faults-full.json
│   └── world-faults.json
├── dist/               # Vite build çıktısı
├── vite.config.js
└── package.json
```

### Anahtar Değişkenler

| Değişken | Açıklama |
|---|---|
| `selectedDateOffset` | 0=bugün (canlı), 1-7=geçmiş günler |
| `allSourceQuakes` | API'dan gelen ham deprem listesi |
| `allQuakes` | Filtrelenmiş/hesaplanmış deprem listesi |
| `seenEarthquakeIds` | Daha önce bildirim gönderilen deprem ID'leri |
| `isFirstLoad` | İlk yüklemede bildirimleri bastırır |
| `currentScope` | 'region' veya 'all' |
| `currentMinMag` | Aktif büyüklük filtresi |

---

## 6. Test Gereksinimleri

### 6.1 Fonksiyonel Testler

#### Harita
- [ ] Sayfa yüklenince harita görünür ve tile'lar yüklenir
- [ ] Karanlık → Uydu modu geçişi çalışır
- [ ] Uydu modunda fay hatları butonu görünür
- [ ] Fay hatları toggle açılıp kapanır
- [ ] Sınır toggle çalışır (Türkiye / Bölge sınırı)
- [ ] Deprem markerlarına tıklanınca popup açılır
- [ ] Depreme tıklanınca harita o noktaya zoom yapar
- [ ] Radar imleci harita üzerinde görünür

#### Deprem Listesi
- [ ] Depremler kartlar halinde listelenir
- [ ] Büyüklük filtresi (Tümü/M2+/M3+/M4+) çalışır
- [ ] Bölge / Tüm TR geçişi çalışır
- [ ] Bir önceki güne gidilebilir
- [ ] Bugüne geri dönülebilir
- [ ] Listedeki depreme tıklanınca haritada gösterilir

#### Analiz Sekmesi
- [ ] Max büyüklük, ortalama, M4+ sayısı, derinlik kartları dolur
- [ ] Sismograf SVG çizgisi render olur
- [ ] Günlük bar grafiği render olur
- [ ] Grafik tooltip çalışır (hover)

#### Arama
- [ ] Arama kutusuna yazınca sonuçlar belirir
- [ ] Sonuca tıklanınca o şehire geçilir
- [ ] X butonu arama kutusunu temizler

#### Bildirim Sistemi (Kritik Test Alanı)
- [ ] Geçmiş güne gidince bildirim/toast GELMEZ
- [ ] Geçmiş gündeyken yeni canlı deprem gelirse toast GELİR
- [ ] Toast'a tıklanınca bugünün tarihine geçiş yapılır
- [ ] Toast tıklaması depremin haritadaki konumuna zoom yapar
- [ ] Tarayıcı push bildirimi izin alındıktan sonra M4+ için gönderilir
- [ ] Ses alarmı büyüklüğe göre farklı çalar

#### Genel UI
- [ ] Yükleme spinner başlangıçta görünür, veri gelince kapanır
- [ ] Header'da Türkiye saati canlı güncellenir
- [ ] Footer bilgileri görünür
- [ ] Responsive: mobilde alt alta, masaüstünde yan yana görünüm

### 6.2 Hata Durumu Testleri
- [ ] Kandilli API yanıt vermezse USGS'e fallback yapılır
- [ ] USGS de yanıt vermezse hata mesajı gösterilir

---

## 7. Performans Gereksinimleri

| Metrik | Hedef |
|---|---|
| İlk yükleme süresi | < 3 saniye |
| API yanıt + render | < 2 saniye |
| Otomatik yenileme aralığı | 30 saniye |
| Harita tile yükleme | Leaflet lazy loading |

---

## 8. Tarayıcı Uyumluluğu

| Tarayıcı | Destek |
|---|---|
| Chrome 90+ | Tam destek |
| Firefox 88+ | Tam destek |
| Safari 14+ | Tam destek |
| Edge 90+ | Tam destek |
| Mobil Chrome / Safari | Responsive |

---

## 9. Bilinen Kısıtlamalar

- Kandilli API'si bazen gecikmeli yanıt döndürebilir
- Web Audio API bazı tarayıcılarda kullanıcı etkileşimi gerektirmeden ses çalınmasını engeller
- Tarayıcı push bildirimleri için kullanıcı izni gereklidir
- Fay hattı verisi büyük JSON dosyası (~517KB) olduğundan yüklenme süresi artabilir

---

## 10. Gelecek Özellikler (Backlog)

- [ ] PWA desteği (çevrimdışı mod, ana ekrana ekleme)
- [ ] Kişisel bildirim eşiği ayarı (hangi büyüklükten alarm gelsin)
- [ ] Türkiye dışı şehir araması
- [ ] Deprem geçmişi CSV/Excel export
- [ ] Dark/Light tema geçişi
- [ ] Çoklu dil desteği (TR/EN)
- [ ] Deprem tahmin risk haritası overlay
