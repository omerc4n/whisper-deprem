import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:5173")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Type 'İzmir, İzmir' into the city search field and wait for autocomplete suggestions to appear.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("\u0130zmir, \u0130zmir")
        
        # -> Arama kutusuna 'İzmir, İzmir' yaz ve otomatik tamamlama önerilerinin görünmesini bekle (görünürse sonraki adımda öneriyi seçilecek hâle getir).
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("\u0130zmir, \u0130zmir")
        
        # -> Arama girişine odaklanın (üstteki arama kutusu) ve Enter tuşuna basarak 'İzmir, İzmir' aramasını gönderin; öneriler görünürse öneriyi seçin.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.click(timeout=10000)
        
        # -> Arama kutusuna 'İzmir, İzmir' yaz ve otomatik tamamlama önerilerinin görünmesini bekle.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.click(timeout=10000)
        
        # -> Arama kutusuna 'İzmir, İzmir' yaz ve otomatik tamamlama önerilerinin görünmesini bekle.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("\u0130zmir, \u0130zmir")
        
        # -> Clear the search box using the 'close' button, type 'Izmir, Izmir' into the search field, and wait for autocomplete suggestions to appear.
        # close button
        elem = page.locator('[id="search-clear-btn"]')
        await elem.click(timeout=10000)
        
        # -> Clear the search box using the 'close' button, type 'Izmir, Izmir' into the search field, and wait for autocomplete suggestions to appear.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("Izmir, Izmir")
        
        # -> Arama kutusuna 'İzmir, İzmir' yaz ve otomatik tamamlama önerilerinin görünmesini 3 saniye boyunca bekle.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("\u0130zmir, \u0130zmir")
        
        # -> Type 'Izmir' into the search field and wait for autocomplete suggestions to appear.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("Izmir")
        
        # -> Click the 'İzmir' suggestion from the autocomplete list to select that location.
        # İzmir İzmir TR button
        elem = page.get_by_role('button', name='İzmir İzmir TR', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify earthquake results for the selected location are displayed
        # Assert: Search input shows the selected location 'Izmir'.
        await expect(page.locator("xpath=/html/body/header/div[2]/input").nth(0)).to_have_value("Izmir", timeout=15000), "Search input shows the selected location 'Izmir'."
        # Assert: An earthquake notification toast saying 'Türkiye'de Deprem Oldu!' is visible.
        await expect(page.locator("xpath=/html/body/div[4]/div[1]/div[2]/div[2]").nth(0)).to_contain_text("T\u00fcrkiye'de Deprem Oldu!", timeout=15000), "An earthquake notification toast saying 'T\u00fcrkiye'de Deprem Oldu!' is visible."
        # Assert: The earthquake toast shows the magnitude 'M4.2'.
        await expect(page.locator("xpath=/html/body/div[4]/div[1]/div[2]/div[3]/span[1]").nth(0)).to_have_text("M4.2", timeout=15000), "The earthquake toast shows the magnitude 'M4.2'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    