
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_smoke(page):
    page.goto("https://www.python.org/")

    downloads_link = page.get_by_label(
        "Main Navigation"
    ).get_by_role("link", name="Downloads")

    expect(downloads_link).to_be_visible()


@pytest.mark.regression
def test_regression(page):
    page.goto("https://www.python.org/")

    navigation = page.get_by_label("Main Navigation")

    about_link = navigation.get_by_role(
        "link", name="About"
    )
    documentation_link = navigation.get_by_role(
        "link", name="Documentation"
    )

    expect(about_link).to_be_visible()
    expect(documentation_link).to_be_visible()  # Pytest configuration and markers
