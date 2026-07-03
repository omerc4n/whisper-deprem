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
        
        # -> Click the 'M3.0+' magnitude filter button to filter the earthquake list by magnitude.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button to filter the earthquake list by magnitude.
        # Bölge button
        elem = page.locator('[id="scope-region"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter and verify the earthquake list's 'Listelenen' count and the scope label 'Bölge: Osmaniye, Osmaniye' reflect the applied filter.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and then click the 'Bölge' scope button to apply the region scope, then verify the 'Listelenen:' count is updated.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and then click the 'Bölge' scope button to apply the region scope, then verify the 'Listelenen:' count is updated.
        # Bölge button
        elem = page.locator('[id="scope-region"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous date) button to move to the previous day and reveal any earthquakes for that date.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous date) button to move to the previous day and reveal any earthquakes for that date.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'chevron_left' (previous date) button to move to the previous day and refresh the event list view.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'M3.0+' magnitude filter button and observe the 'Bölgede Toplam' and 'Listelenen' counts in the right panel to verify the filter effect.
        # M3.0+ button
        elem = page.locator('[id="filter-m3"]')
        await elem.click(timeout=10000)
        
        # -> Click the 'Bölge' scope button to ensure region scope is selected, then inspect the right-panel texts 'Bölgede Toplam' and 'Listelenen' to verify the UI reflects scope and filter state.
        # Bölge button
        elem = page.locator('[id="scope-region"]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the earthquake list is filtered by magnitude
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[3]").nth(0).scroll_into_view_if_needed()
        # Assert: The M3.0+ magnitude filter button is visible.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[3]").nth(0)).to_be_visible(timeout=15000), "The M3.0+ magnitude filter button is visible."
        # Assert: The M3.0+ filter button has the active class indicating the magnitude filter is applied.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[3]").nth(0)).to_have_attribute("class", "px-3 py-1 rounded-full border font-label-md text-[11px] hover:border-primary-container whitespace-nowrap bg-primary-container text-on-primary-container border-primary-container active-filter", timeout=15000), "The M3.0+ filter button has the active class indicating the magnitude filter is applied."
        
        # --> Verify the selected scope is reflected in the view
        # Assert: The selected scope is shown in the search input as 'Osmaniye, Osmaniye'.
        await expect(page.locator("xpath=/html/body/header/div[2]/input").nth(0)).to_have_value("Osmaniye, Osmaniye", timeout=15000), "The selected scope is shown in the search input as 'Osmaniye, Osmaniye'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    