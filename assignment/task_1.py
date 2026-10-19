
import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_page_title():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Open the website
        await page.goto(
            "https://example.com/",
            wait_until="domcontentloaded"
        )

        # Get the page title
        title = await page.title()
        print("Page title:", repr(title))
        print("Current URL:", page.url)

        # Validate the page title
        assert title == "Example Domain", (
            f"Expected 'Example Domain', but got {title!r}"
        )

        print("Page title validation passed!")

        await browser.close() # open website and check  titile
