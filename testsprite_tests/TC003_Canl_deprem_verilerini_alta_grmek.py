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
        
        # --> Assertions to verify final state
        
        # --> Verify recent earthquake entries are displayed
        await page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[1]/div[2]/h3").nth(0).scroll_into_view_if_needed()
        # Assert: The recent earthquake card 'CUMALI-KINIK (IZMIR)' is visible in the list.
        await expect(page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[1]/div[2]/h3").nth(0)).to_be_visible(timeout=15000), "The recent earthquake card 'CUMALI-KINIK (IZMIR)' is visible in the list."
        await page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[2]/div[2]/h3").nth(0).scroll_into_view_if_needed()
        # Assert: The recent earthquake card 'CALDERE-BIGADIC (BALIKESIR)' is visible in the list.
        await expect(page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[2]/div[2]/h3").nth(0)).to_be_visible(timeout=15000), "The recent earthquake card 'CALDERE-BIGADIC (BALIKESIR)' is visible in the list."
        await page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[3]/div[2]/h3").nth(0).scroll_into_view_if_needed()
        # Assert: The recent earthquake card 'MIDILLI ADASI (EGE DENIZI)' is visible in the list.
        await expect(page.locator("xpath=/html/body/main/aside/div[2]/div[1]/div/div[3]/div[2]/h3").nth(0)).to_be_visible(timeout=15000), "The recent earthquake card 'MIDILLI ADASI (EGE DENIZI)' is visible in the list."
        
        # --> Verify the map is displayed
        await page.locator("xpath=/html/body/main/section/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: Map container is visible on the page.
        await expect(page.locator("xpath=/html/body/main/section/div[1]").nth(0)).to_be_visible(timeout=15000), "Map container is visible on the page."
        await page.locator("xpath=/html/body/main/section/div[1]/div[2]/div[2]/div/a[1]").nth(0).scroll_into_view_if_needed()
        # Assert: Map zoom-in control (+) is visible, indicating map controls are rendered.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[2]/div[2]/div/a[1]").nth(0)).to_be_visible(timeout=15000), "Map zoom-in control (+) is visible, indicating map controls are rendered."
        # Assert: Map attribution contains 'Leaflet', confirming the Leaflet/OpenStreetMap map is displayed.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[2]/div[4]/div").nth(0)).to_contain_text("Leaflet", timeout=15000), "Map attribution contains 'Leaflet', confirming the Leaflet/OpenStreetMap map is displayed."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    