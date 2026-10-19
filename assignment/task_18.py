
from playwright.sync_api import Page, expect, TimeoutError


def test_login_and_add_to_cart(page: Page):
    app_url = "https://www.saucedemo.com/"

    username = "standard_user"
    password = "secret_sauce"

    # 1. Open website
    page.goto(app_url)

    # 2. Login
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    # 3. Verify inventory page
    page.wait_for_url("**/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

    # 4. Verify product count
    products = page.locator(".inventory_item_name")
    expect(products).to_have_count(6)

    # 5. Demonstrate first, last, and nth locators
    print("First:", products.first.inner_text())
    print("Last:", products.last.inner_text())
    print("Third:", products.nth(2).inner_text())

    # 6. Add Backpack to cart
    backpack = page.locator(".inventory_item").filter(
        has_text="Sauce Labs Backpack"
    )
    backpack.get_by_role("button", name="Add to cart").click()

    # 7. Verify cart badge
    try:
        page.locator(".shopping_cart_badge").wait_for(
            state="visible",
            timeout=5000
        )
    except TimeoutError:
        raise AssertionError("Cart badge did not appear.")

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # 8. Open cart and verify product
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_contain_text(
        "Sauce Labs Backpack"
    )

    print("Test passed!")


def test_browser_fixture(browser):
    assert browser.version
    print("Browser version:", browser.version)
