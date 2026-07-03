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
        
        # -> Sağ listedeki 'CUMALI-KINIK (IZMIR)' deprem kartının sağ ok düğmesine tıklayın ve haritanın o konuma odaklandığını doğrulayın.
        # chevron_right
        elem = page.locator('xpath=/html/body/main/aside/div[2]/div/div/div/span')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the live earthquake list is displayed
        # Assert: The 'Depremler' sidebar tab is visible, confirming the earthquake list area is shown.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[1]/button[1]").nth(0)).to_have_text("Depremler", timeout=15000), "The 'Depremler' sidebar tab is visible, confirming the earthquake list area is shown."
        
        # --> Verify the map is displayed with earthquake markers
        await page.locator("xpath=/html/body/main/section/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The map container is visible on the page.
        await expect(page.locator("xpath=/html/body/main/section/div[1]").nth(0)).to_be_visible(timeout=15000), "The map container is visible on the page."
        # Assert: An earthquake marker icon ('location_on') is present on the map.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[4]/div/div/div[2]/span").nth(0)).to_have_text("location_on", timeout=15000), "An earthquake marker icon ('location_on') is present on the map."
        
        # --> Verify the live data view is displayed
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The live-data filter chip 'Tümü' is visible in the sidebar.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[1]").nth(0)).to_be_visible(timeout=15000), "The live-data filter chip 'T\u00fcm\u00fc' is visible in the sidebar."
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[2]").nth(0).scroll_into_view_if_needed()
        # Assert: The magnitude filter 'M2.0+' chip is visible, showing live data controls.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[2]").nth(0)).to_be_visible(timeout=15000), "The magnitude filter 'M2.0+' chip is visible, showing live data controls."
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[3]").nth(0).scroll_into_view_if_needed()
        # Assert: The magnitude filter 'M3.0+' chip is visible, confirming live data view controls are shown.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[3]").nth(0)).to_be_visible(timeout=15000), "The magnitude filter 'M3.0+' chip is visible, confirming live data view controls are shown."
        await page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[4]").nth(0).scroll_into_view_if_needed()
        # Assert: The magnitude filter 'M4.0+' chip is visible, indicating the live data view is displayed.
        await expect(page.locator("xpath=/html/body/main/aside/div[1]/div[2]/div[3]/button[4]").nth(0)).to_be_visible(timeout=15000), "The magnitude filter 'M4.0+' chip is visible, indicating the live data view is displayed."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    