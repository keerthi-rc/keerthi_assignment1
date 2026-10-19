
from playwright.sync_api import expect


def test_page_timeout(page):
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(15000)

    page.goto("https://www.python.org/")

    expect(page).to_have_title("Welcome to Python.org")
