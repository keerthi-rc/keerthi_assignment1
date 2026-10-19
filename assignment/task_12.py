
from playwright.sync_api import Page, expect


def test_page_and_element_assertions(page: Page):
    # Open SauceDemo website
    page.goto("https://www.saucedemo.com/")

    # 1. Verify page title using expect()
    expect(page).to_have_title("Swag Labs")

    # 2. Verify URL using expect()
    expect(page).to_have_url("https://www.saucedemo.com/")

    # 3. Verify element visibility
    logo = page.locator(".login_logo")
    expect(logo).to_be_visible()

    # 4. Verify element text
    expect(logo).to_have_text("Swag Labs")

    # 5. Verify input value
    username = page.locator("#user-name")
    username.fill("standard_user")
    expect(username).to_have_value("standard_user")

    # 6. Verify an element is enabled
    login_button = page.locator("#login-button")
    expect(login_button).to_be_enabled()

    # Verify the password field is enabled
    password = page.locator("#password")
    expect(password).to_be_enabled()

    # 7. Use pytest assert for a calculated/extracted value
    username_value = username.input_value()
    username_length = len(username_value)

    print("Page title:", page.title())
    print("Current URL:", page.url)
    print("Username:", username_value)
    print("Username length:", username_length)

    assert username_length == 13

    print("All assertions passed successfully!")
