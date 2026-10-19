
from playwright.sync_api import Page, expect


def test_open_website(page: Page):
    page.goto("https://www.google.com")

    expect(page).to_have_title(
        __import__("re").compile("Google")
    )

    print(f"Browser test passed: {page.title()}")
