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
        
        # -> Sağ listedeki 'CALDERE-BIGADIC (BALIKESIR)' deprem kartına tıklayın.
        # 1.6 CALDERE-BIGADIC (BALIKESIR)...
        elem = page.locator('xpath=/html/body/main/aside/div[2]/div/div/div[2]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the map is focused on the selected earthquake
        await page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0).scroll_into_view_if_needed()
        # Assert: The earthquake popup on the map is visible, indicating focus on the selected event.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_be_visible(timeout=15000), "The earthquake popup on the map is visible, indicating focus on the selected event."
        # Assert: The map popup displays the magnitude 'M 1.6' for the selected earthquake.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("M 1.6", timeout=15000), "The map popup displays the magnitude 'M 1.6' for the selected earthquake."
        # Assert: The map popup displays the location 'CALDERE-BIGADIC (BALIKESIR)' for the selected earthquake.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("CALDERE-BIGADIC (BALIKESIR)", timeout=15000), "The map popup displays the location 'CALDERE-BIGADIC (BALIKESIR)' for the selected earthquake."
        
        # --> Verify the selected earthquake details are displayed
        # Assert: The selected earthquake popup displays the magnitude 'M 1.6'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("M 1.6", timeout=15000), "The selected earthquake popup displays the magnitude 'M 1.6'."
        # Assert: The selected earthquake popup displays the location 'CALDERE-BIGADIC (BALIKESIR)'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("CALDERE-BIGADIC (BALIKESIR)", timeout=15000), "The selected earthquake popup displays the location 'CALDERE-BIGADIC (BALIKESIR)'."
        # Assert: The selected earthquake popup displays the depth '3.6 km'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("3.6 km", timeout=15000), "The selected earthquake popup displays the depth '3.6 km'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    