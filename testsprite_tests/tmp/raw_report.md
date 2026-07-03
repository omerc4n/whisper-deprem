
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** whisper-deprem
- **Date:** 2026-07-03
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001 Uygulama açılışında canlı deprem verilerinin yüklenmesi
- **Test Code:** [TC001_Uygulama_alnda_canl_deprem_verilerinin_yklenmesi.py](./TC001_Uygulama_alnda_canl_deprem_verilerinin_yklenmesi.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/61f7f232-2b3b-464b-9f17-e154b777dca4
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002 Canlı veriler açılışta yüklenir
- **Test Code:** [TC002_Canl_veriler_alta_yklenir.py](./TC002_Canl_veriler_alta_yklenir.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/4e9ac90e-e5a7-4a51-aeec-15beb2ae1a0a
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003 Canlı deprem verilerini açılışta görmek
- **Test Code:** [TC003_Canl_deprem_verilerini_alta_grmek.py](./TC003_Canl_deprem_verilerini_alta_grmek.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/de4ae81e-2af9-44ed-a487-f2ab5b634138
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC004 Ana görünümde canlı deprem verilerini yükleme
- **Test Code:** [TC004_Ana_grnmde_canl_deprem_verilerini_ykleme.py](./TC004_Ana_grnmde_canl_deprem_verilerini_ykleme.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/ec515f28-19b0-47c4-9a9a-52df8464ef8b
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005 Deprem kartı seçildiğinde haritanın ilgili noktaya odaklanması
- **Test Code:** [TC005_Deprem_kart_seildiinde_haritann_ilgili_noktaya_odaklanmas.py](./TC005_Deprem_kart_seildiinde_haritann_ilgili_noktaya_odaklanmas.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/83f05210-2ce6-44ca-80f4-61af25258b6b
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC006 Yeni veri geldiğinde listenin güncellenmesi
- **Test Code:** [TC006_Yeni_veri_geldiinde_listenin_gncellenmesi.py](./TC006_Yeni_veri_geldiinde_listenin_gncellenmesi.py)
- **Test Error:** TEST FAILURE

The automatic live earthquake list did not refresh while the page was left open and after remounting the UI.

Observations:
- The right panel displays 'Bölgede Toplam: 5 | Listelenen: 0' and it remained unchanged after multiple checks.
- Three 60-second waits and a switch to 'Analiz & Grafikler' then back to 'Depremler' were performed; no new list entries or timestamps appeared.
- Map and UI controls (tabs, filters, layer toggle) are present and map markers are visible, but no automatic data refresh was observed.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/70603226-a593-4e0d-afeb-607340c0a816
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC007 Listeden deprem seçip haritada odağı görmek
- **Test Code:** [TC007_Listeden_deprem_seip_haritada_oda_grmek.py](./TC007_Listeden_deprem_seip_haritada_oda_grmek.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/631b5d66-1f0f-4826-b0d1-e5abb1f2d390
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC008 Bir deprem seçilince odak ayrıntısı gösterilir
- **Test Code:** [TC008_Bir_deprem_seilince_odak_ayrnts_gsterilir.py](./TC008_Bir_deprem_seilince_odak_ayrnts_gsterilir.py)
- **Test Error:** TEST FAILURE

Selecting an earthquake from the map does not show its details in the right-hand panel; the UI remains on the 'Seçilen tarihte deprem bulunamadı.' message after marker selection.

Observations:
- The page displays 'Seçilen tarihte deprem bulunamadı.' and footer counts show 'Bölgede Toplam: 0 | Listelenen: 0'.
- A yellow 'location_on' marker is visible on the map but clicking it (multiple attempts, including a recorded successful click) did not populate the right-hand details panel.
- The map did not visibly re-center or show an explicit focused detail view after selection.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/00fabee4-11c7-47eb-b4f3-d742528fd489
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009 Deprem seçince harita ve detay odağını güncelleme
- **Test Code:** [TC009_Deprem_seince_harita_ve_detay_odan_gncelleme.py](./TC009_Deprem_seince_harita_ve_detay_odan_gncelleme.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/b78a6869-60f7-4389-a5a1-eda358f7e0f5
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010 Harita işaretçisi seçildiğinde deprem detaylarının listede görünmesi
- **Test Code:** [TC010_Harita_iaretisi_seildiinde_deprem_detaylarnn_listede_grnmesi.py](./TC010_Harita_iaretisi_seildiinde_deprem_detaylarnn_listede_grnmesi.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/5d432b43-297f-48ed-b658-81583788af05
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC011 Ana kaynak uygun olmadığında yedek kaynağın gösterilmesi
- **Test Code:** [TC011_Ana_kaynak_uygun_olmadnda_yedek_kaynan_gsterilmesi.py](./TC011_Ana_kaynak_uygun_olmadnda_yedek_kaynan_gsterilmesi.py)
- **Test Error:** TEST FAILURE

Birincil veri kaynağı yerine yedek kaynaktan deprem listesinin sunulduğu doğrulanamadı — uygulama açık bir 'yedek' gösterge veya yedekten alınan deprem kartlarını göstermiyor.

Observations:
- Sayfa, 'Seçilen tarihte deprem bulunamadı.' metnini gösteriyor ve deprem listesi boş gözüküyor.
- Sayfada 'CANLI VERİ AKTİF' etiketi görünürken 'yedek' kelimesi veya görünür bir yedek kaynak etiketi yok; yalnızca "Kandilli API" bağlantısı mevcut.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/b7f9b07e-59df-46e9-bc4a-71e80f1b83b5
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC012 Haritadaki işaretten deprem detayına ulaşmak
- **Test Code:** [TC012_Haritadaki_iaretten_deprem_detayna_ulamak.py](./TC012_Haritadaki_iaretten_deprem_detayna_ulamak.py)
- **Test Error:** TEST FAILURE

Selecting a map marker did not display the earthquake details in the right-hand detail panel as expected.

Observations:
- A yellow earthquake marker is visible on the map and was clicked.
- The right panel displays 'Seçilen tarihte deprem bulunamadı.' after selection.
- No earthquake details (magnitude, time, or location) appeared in the detail panel after clicking the marker.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/24791249-4987-4e99-842f-cccfeccc3b85
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC013 Bugünün verilerine geri dönme
- **Test Code:** [TC013_Bugnn_verilerine_geri_dnme.py](./TC013_Bugnn_verilerine_geri_dnme.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/79f2d30d-6d8e-4fce-8cf2-97513fff3bc7
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC014 Bugünün canlı görünümüne geri dönme
- **Test Code:** [TC014_Bugnn_canl_grnmne_geri_dnme.py](./TC014_Bugnn_canl_grnmne_geri_dnme.py)
- **Test Error:** TEST FAILURE

Bugün görünümüne geri dönüldüğünde liste ve harita senkronize olmuyor — liste boş görünürken haritada en az bir deprem marker'ı gösteriliyor.

Observations:
- Sayfa başlığı olarak 'Canlı Yayın (Bugün) (03.07.2026)' görüntülendi.
- Sağ panelde "Seçilen tarihte deprem bulunamadı." mesajı (liste: 0 olay) bulundu.
- Harita üzerinde sarı bir marker görünüyor ve DOM'da marker ile ilişkili interaktif elemanlar mevcut.

Sonuç: Beklenen davranış (Bugün moduna döndüğünde güncel deprem listesi ile haritanın birlikte güncellenmesi ve senkronize görüntülenmesi) sağlanmadı. Test bu nedenle FAIL olarak raporlanmaktadır.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/d66aa698-9b20-4823-8d6d-7448571dbb60
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC015 Son yedi gün içinde tarih değiştirerek arşiv gezintisi
- **Test Code:** [TC015_Son_yedi_gn_iinde_tarih_deitirerek_ariv_gezintisi.py](./TC015_Son_yedi_gn_iinde_tarih_deitirerek_ariv_gezintisi.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/b345ecb1-c769-4a4b-ab58-f0a287a2136e
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC016 Bugünün canlı görünümüne geri dönmek
- **Test Code:** [TC016_Bugnn_canl_grnmne_geri_dnmek.py](./TC016_Bugnn_canl_grnmne_geri_dnmek.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/402529d3-c7f5-420e-a37d-c8730145727d
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC017 Şehir aramasıyla öneri seçilip görünümün güncellenmesi
- **Test Code:** [TC017_ehir_aramasyla_neri_seilip_grnmn_gncellenmesi.py](./TC017_ehir_aramasyla_neri_seilip_grnmn_gncellenmesi.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/ccc915fe-41a7-4812-bff1-c4388230f294
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC018 Tüm depremler görünümüne dönülür
- **Test Code:** [TC018_Tm_depremler_grnmne_dnlr.py](./TC018_Tm_depremler_grnmne_dnlr.py)
- **Test Error:** TEST FAILURE

Selecting the full-scope option did not display all earthquakes in the list as expected.

Observations:
- The map displays at least one earthquake marker (visible on the map).
- The right panel shows 'Seçilen tarihte deprem bulunamadı.' and the footer shows 'Bölgedeki Toplam: 0 | Listelenen: 0'.
- The 'TÜM TÜRKİYE' scope and 'Tümü' magnitude filter are selected, but the list remains empty (inconsistent behaviour).
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/d3804551-8a79-4199-8b14-d2c93ef13fb5
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC019 Şehir aramasıyla yerel depremleri filtrelemek
- **Test Code:** [TC019_ehir_aramasyla_yerel_depremleri_filtrelemek.py](./TC019_ehir_aramasyla_yerel_depremleri_filtrelemek.py)
- **Test Error:** TEST FAILURE

Search autocomplete did not surface suggestions and selecting a city did not filter results to that location.

Observations:
- The 'Bölge veya şehir ara' field contains 'İzmir, İzmir' but no autocomplete list appeared after multiple attempts.
- The right panel and map remained showing 'Bölge: Osmaniye, Osmaniye' and 'Bölgede Toplam: 0 Olay' — results were not filtered to İzmir.
- A DOM search found no suggestion elements (no listbox/options or suggestion items were present).

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/b5aadd6f-86df-4ef1-98ec-6ad3ecbf901a
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC020 Şehir aramasıyla yerel deprem sonuçlarını filtreleme
- **Test Code:** [TC020_ehir_aramasyla_yerel_deprem_sonularn_filtreleme.py](./TC020_ehir_aramasyla_yerel_deprem_sonularn_filtreleme.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/918f2e53-9b7a-4fbb-9858-f2828b8070c4
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC021 Önceki gün arşiv verilerine geçilir
- **Test Code:** [TC021_nceki_gn_ariv_verilerine_geilir.py](./TC021_nceki_gn_ariv_verilerine_geilir.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/f0e80c6e-5a18-41c2-9056-b047f4f0c838
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC022 Son 7 gün içinde tarih gezintisi yapma
- **Test Code:** [TC022_Son_7_gn_iinde_tarih_gezintisi_yapma.py](./TC022_Son_7_gn_iinde_tarih_gezintisi_yapma.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/281cb145-13f6-47c9-91ef-30548522696a
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC023 Büyüklük filtresiyle deprem listesini daraltma
- **Test Code:** [TC023_Byklk_filtresiyle_deprem_listesini_daraltma.py](./TC023_Byklk_filtresiyle_deprem_listesini_daraltma.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/b9239212-e695-4be0-af15-50df65d45ed2
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC024 M2 ve üzeri depremler filtrelenir
- **Test Code:** [TC024_M2_ve_zeri_depremler_filtrelenir.py](./TC024_M2_ve_zeri_depremler_filtrelenir.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/1b4e5535-02ea-44fe-a7ff-51bbc23be2c7
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC025 Büyüklük ve kapsam filtreleriyle listeyi daraltmak
- **Test Code:** [TC025_Byklk_ve_kapsam_filtreleriyle_listeyi_daraltmak.py](./TC025_Byklk_ve_kapsam_filtreleriyle_listeyi_daraltmak.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/90e698af-38ed-4401-8d96-9651f3e9dd07
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC026 Arşiv günleri arasında ileri gidilerek bugüne dönülür
- **Test Code:** [TC026_Ariv_gnleri_arasnda_ileri_gidilerek_bugne_dnlr.py](./TC026_Ariv_gnleri_arasnda_ileri_gidilerek_bugne_dnlr.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/0117467f-cc3c-42c6-9dab-aee039ee1dd2
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC027 Büyüklük filtresiyle sonuçları daraltma
- **Test Code:** [TC027_Byklk_filtresiyle_sonular_daraltma.py](./TC027_Byklk_filtresiyle_sonular_daraltma.py)
- **Test Error:** TEST BLOCKED

Test çalıştırılamadı — doğrulama için gereken deprem listesi mevcut değil, bu yüzden büyüklük filtresinin etkisi gözlemlenemiyor.

Observations:
- Sağ panelde "Seçilen tarihte deprem bulunamadı." mesajı gösteriliyor.
- Sayfada "Bölgedeki Toplam: 0 Olay" ve "Bölgede Toplam: 0 | Listelenen: 0" metinleri mevcut, yani listede 0 kayıt var.

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/1d34e79e-56a9-4508-a2da-0839edfe35f8
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC028 Harita modları arasında geçiş yapılması
- **Test Code:** [TC028_Harita_modlar_arasnda_gei_yaplmas.py](./TC028_Harita_modlar_arasnda_gei_yaplmas.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/97a2d1e7-4b97-4fb5-88d8-897b9ce78b64
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC029 Aramayı temizleyip tüm Türkiye görünümüne dönmek
- **Test Code:** [TC029_Aramay_temizleyip_tm_Trkiye_grnmne_dnmek.py](./TC029_Aramay_temizleyip_tm_Trkiye_grnmne_dnmek.py)
- **Test Error:** TEST FAILURE

Clearing the city search did not remove the region filter and the full Türkiye view was not restored.

Observations:
- The sidebar still shows 'Bölge: Osmaniye, Osmaniye' after multiple clear attempts.
- The search input at the top remains populated with 'Osmaniye, Osmaniye'.
- Clicking the 'Tüm TR' button and using keyboard clear methods (including Ctrl+A + Backspace) did not change the filter state or return the UI to a full Türkiye view.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/1cd89087-992e-432f-bd1d-c8ce0c87352e
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC030 Kapsam seçiciyle bölge ve tüm Türkiye arasında geçiş
- **Test Code:** [TC030_Kapsam_seiciyle_blge_ve_tm_Trkiye_arasnda_gei.py](./TC030_Kapsam_seiciyle_blge_ve_tm_Trkiye_arasnda_gei.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/2997c1a7-10c6-4962-8cc2-4a97dc8c4621/8be28329-33f5-4646-b0a1-088913f48eaa
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **70.00** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---