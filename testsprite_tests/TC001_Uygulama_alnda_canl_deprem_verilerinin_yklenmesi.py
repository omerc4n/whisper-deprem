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
        
        # -> Click the first earthquake card 'CUMALI-KINIK (IZMIR)' in the list to verify the map focuses on that event.
        # chevron_right
        elem = page.locator('xpath=/html/body/main/aside/div[2]/div/div/div/span')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify live deprem entries are displayed
        # Assert: The live earthquake 'CUMALI-KINIK (IZMIR)' is visible in the map/list.
        await expect(page.locator("xpath=/html/body/main/section/div[1]").nth(0)).to_contain_text("CUMALI-KINIK (IZMIR)", timeout=15000), "The live earthquake 'CUMALI-KINIK (IZMIR)' is visible in the map/list."
        await page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[4]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert: An earthquake marker element is visible on the map, confirming live deprem entries are displayed.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[4]/div[2]").nth(0)).to_be_visible(timeout=15000), "An earthquake marker element is visible on the map, confirming live deprem entries are displayed."
        
        # --> Verify the map and list show the same deprem set
        # Assert: The earthquake list shows 'CUMALI-KINIK (IZMIR)'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]").nth(0)).to_contain_text("CUMALI-KINIK (IZMIR)", timeout=15000), "The earthquake list shows 'CUMALI-KINIK (IZMIR)'. "
        # Assert: The map popup shows 'CUMALI-KINIK (IZMIR)'.
        await expect(page.locator("xpath=/html/body/main/section/div[1]/div[1]/div[6]/div").nth(0)).to_contain_text("CUMALI-KINIK (IZMIR)", timeout=15000), "The map popup shows 'CUMALI-KINIK (IZMIR)'. "
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    