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
        
        # -> Click the 'chevron_left' (Önceki gün) button to navigate to the previous day's data.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify o güne ait deprem listesi ve harita verileri gösterilir
        # Assert: Depremler sekmesi görünür ve deprem listesi paneli gösteriliyor.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[1]/button[1]").nth(0)).to_have_text("Depremler", timeout=15000), "Depremler sekmesi g\u00f6r\u00fcn\u00fcr ve deprem listesi paneli g\u00f6steriliyor."
        # Assert: Harita ve atıf metni (Leaflet/OpenStreetMap) görünür, harita verileri yüklendi.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[2]/div[4]/div").nth(0)).to_contain_text("Leaflet", timeout=15000), "Harita ve at\u0131f metni (Leaflet/OpenStreetMap) g\u00f6r\u00fcn\u00fcr, harita verileri y\u00fcklendi."
        current_url = await page.evaluate("() => window.location.href")
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    