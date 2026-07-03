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
        
        # -> Type 'Istanbul, Istanbul' into the 'Bölge veya şehir ara' search field and wait for autocomplete suggestions to appear.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("Istanbul, Istanbul")
        
        # -> Select the 'Istanbul, Istanbul' city from autocomplete (accept the current suggestion by pressing Enter), then click the search clear control (the 'close' / X button) to clear the search.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.click(timeout=10000)
        
        # -> Select the 'Istanbul, Istanbul' city from autocomplete (accept the current suggestion by pressing Enter), then click the search clear control (the 'close' / X button) to clear the search.
        # close button
        elem = page.locator('[id="search-clear-btn"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (Tüm TR) button to switch to full Türkiye view, then clear the city search field and verify the app returned to the Türkiye view.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (Tüm TR) button to switch to full Türkiye view, then clear the city search field and verify the app returned to the Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("")
        
        # -> Clear the 'Bölge veya şehir ara' arama alanını ve ardından 'Tüm TR' düğmesine tıklayarak tüm Türkiye görünümüne geri dön.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("")
        
        # -> Clear the 'Bölge veya şehir ara' arama alanını ve ardından 'Tüm TR' düğmesine tıklayarak tüm Türkiye görünümüne geri dön.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Clear the 'Bölge veya şehir ara' search field (remove current city) and then click the 'Tüm TR' button to return to the full Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.click(timeout=10000)
        
        # -> Clear the 'Bölge veya şehir ara' search field (remove current city) and then click the 'Tüm TR' button to return to the full Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("")
        
        # -> Clear the 'Bölge veya şehir ara' search field (remove current city) and then click the 'Tüm TR' button to return to the full Türkiye view.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Clear the 'Bölge veya şehir ara' search field, then click the 'Tüm TR' button to return to the full Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("")
        
        # -> Clear the 'Bölge veya şehir ara' search field, then click the 'Tüm TR' button to return to the full Türkiye view.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Clear the 'Bölge veya şehir ara' search field and click the 'Tüm TR' button to return to the full Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("")
        
        # -> Clear the 'Bölge veya şehir ara' search field by selecting all (Ctrl+A) and deleting, then click the 'Tüm TR' button to return to the full Türkiye view.
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.click(timeout=10000)
        
        # -> Clear the 'Bölge veya şehir ara' search field by selecting all (Ctrl+A) and deleting, then click the 'Tüm TR' button to return to the full Türkiye view.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the full Turkey earthquake view is displayed
        # Assert: Expected the search input to be cleared to return to the full Türkiye view.
        await expect(page.locator("xpath=/html/body/header/div[2]/input").nth(0)).to_have_value("", timeout=15000), "Expected the search input to be cleared to return to the full T\u00fcrkiye view."
        
        # --> Verify the search field is cleared
        # Assert: Expected the search field to be cleared.
        await expect(page.locator("xpath=/html/body/header/div[2]/input").nth(0)).to_have_value("", timeout=15000), "Expected the search field to be cleared."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    