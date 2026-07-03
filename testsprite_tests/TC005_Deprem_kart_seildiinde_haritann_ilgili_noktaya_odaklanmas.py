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
        
        # -> Click the 'CUMALI-KINIK (IZMIR)' earthquake card in the right-hand Depremler list to open its details.
        # chevron_right
        elem = page.locator('xpath=/html/body/main/aside/div[2]/div/div/div/span')
        await elem.click(timeout=10000)
        
        # -> Click the 'Depremler' tab to show the earthquake list so a deprem card (e.g., 'CUMALI-KINIK (IZMIR)') can be clicked.
        # Depremler button
        elem = page.locator('[id="tab-btn-events"]')
        await elem.click(timeout=10000)
        
        # -> Click the highlighted yellow marker on the map to open the earthquake details and cause the map to focus on that location.
        # Depremler button
        elem = page.locator('[id="tab-btn-events"]')
        await elem.click(timeout=10000)
        
        # -> Click the highlighted yellow map marker to open the earthquake details and focus the map on that location.
        # location_on button
        elem = page.get_by_role('button', name='location_on', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the previous-date ('chevron_left') button to load earthquakes from the prior date so that earthquake cards can appear.
        # chevron_left button
        elem = page.locator('[id="date-prev"]')
        await elem.click(timeout=10000)
        
        # -> Click the earthquake card '23 km SSE of Karpathos, Greece' in the right panel to open its details and verify the map recenters on that event.
        # chevron_right
        elem = page.locator('xpath=/html/body/main/aside/div[2]/div/div/div/span')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the selected deprem details are shown
        # Assert: The selected earthquake popup displays the magnitude 'M 5.2'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("M 5.2", timeout=15000), "The selected earthquake popup displays the magnitude 'M 5.2'."
        # Assert: The selected earthquake popup shows the location '23 km SSE of Karpathos, Greece'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("23 km SSE of Karpathos, Greece", timeout=15000), "The selected earthquake popup shows the location '23 km SSE of Karpathos, Greece'."
        # Assert: The selected earthquake popup includes the depth '10.0 km'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("10.0 km", timeout=15000), "The selected earthquake popup includes the depth '10.0 km'."
        
        # --> Verify the map focuses on the selected deprem location
        # Assert: Map popup displays '23 km SSE of Karpathos, Greece', confirming the map focused on the selected event.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("23 km SSE of Karpathos, Greece", timeout=15000), "Map popup displays '23 km SSE of Karpathos, Greece', confirming the map focused on the selected event."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    