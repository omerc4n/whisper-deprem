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
        
        # -> Click the 'Bölge' button to switch to the regional view and verify the regional earthquake view is displayed.
        # Bölge button
        elem = page.locator('[id="scope-region"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' button to switch to the all-Turkey view and verify the all-Turkey deprem view is displayed.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button to switch to the all‑Turkey view and then verify the UI updates to show the all‑Turkey view (e.g., 'TÜM TÜRKİYE' active or regional label removed).
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button to switch to the all‑Turkey view and verify the UI updates to show the all‑Turkey scope.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button and verify the UI updates to the all‑Turkey view (regional label removed or 'TÜM TÜRKİYE' shown active).
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Arama alanına 'Türkiye' yaz ve öneri açılırsa bekle (Bölge veya şehir ara alanını kullan).
        # Bölge veya şehir ara search field
        elem = page.locator('[id="search-input"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("T\u00fcrkiye")
        
        # -> Click the 'Türkiye Cumhuriyeti' suggestion from the search dropdown to switch the app to the all‑Turkey view.
        # Türkiye Cumhuriyeti TR button
        elem = page.get_by_role('button', name='Türkiye Cumhuriyeti TR', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the regional deprem view is displayed
        # Assert: The region search input contains 'Osmaniye, Osmaniye', confirming the regional view is displayed.
        await expect(page.locator("xpath=/html/body/header/div[2]/input").nth(0)).to_have_value("Osmaniye, Osmaniye", timeout=15000), "The region search input contains 'Osmaniye, Osmaniye', confirming the regional view is displayed."
        
        # --> Verify the all-Turkey deprem view is displayed
        # Assert: The header displays 'Türkiye Cumhuriyeti', indicating the all‑Turkey scope was selected.
        await expect(page.locator("xpath=/html/body/header/div[2]").nth(0)).to_contain_text("T\u00fcrkiye Cumhuriyeti", timeout=15000), "The header displays 'T\u00fcrkiye Cumhuriyeti', indicating the all\u2011Turkey scope was selected."
        # Assert: The 'Tüm TR' scope button is visible, confirming the all‑Turkey scope control is shown.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[1]/div[2]/button[2]").nth(0)).to_contain_text("T\u00fcm", timeout=15000), "The 'T\u00fcm TR' scope button is visible, confirming the all\u2011Turkey scope control is shown."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    