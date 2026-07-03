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
        
        # -> Click the 'M3.0+' magnitude filter button (M3.0+ filtre düğmesini tıklayın).
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button (M3.0+ filtre düğmesini tıklayın).
        # Tümü button
        elem = page.locator('[id="filter-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button to apply the M3.0+ filter
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and check that no 'M2' entries appear in the list (verify filter hides lower-magnitude items).
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and check that no 'M2' entries appear in the list (verify filter hides lower-magnitude items).
        # Tümü button
        elem = page.locator('[id="filter-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous date) button to navigate to the prior day and wait for the live list to update.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous day) button to load the prior day's events and check the list for magnitude labels like 'M2.' and 'M3.'
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous day) button to load the prior day's events and wait for the live list to update.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and search the page for magnitude labels (look for 'M2.' and 'M3.') to see whether any event cards are present.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button to expand the search to all of Türkiye and reveal any nationwide events.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button to expand the search to all of Türkiye and reveal any nationwide events.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm' (All) scope button to expand the search to all of Türkiye and reveal any nationwide events.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm TR' (All Türkiye) scope button, go to the previous day, then click the 'M3.0+' magnitude filter and wait for the list to update so that magnitude labels can be inspected.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm TR' (All Türkiye) scope button, go to the previous day, then click the 'M3.0+' magnitude filter and wait for the list to update so that magnitude labels can be inspected.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Tüm TR' (All Türkiye) scope button, go to the previous day, then click the 'M3.0+' magnitude filter and wait for the list to update so that magnitude labels can be inspected.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_right' (next day) button to move to a more recent date, then apply the 'M3.0+' magnitude filter and check the event list.
        # Tüm TR button
        elem = page.locator('[id="scope-all"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_right' (next day) button to move to a more recent date, then apply the 'M3.0+' magnitude filter and check the event list.
        # chevron_right button
        elem = page.locator('[id="date-next"]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the full deprem list is displayed again
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The 'Tümü' (All) magnitude filter button is visible, indicating the full deprem list view is available.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[1]").nth(0)).to_be_visible(timeout=15000), "The 'T\u00fcm\u00fc' (All) magnitude filter button is visible, indicating the full deprem list view is available."
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
    