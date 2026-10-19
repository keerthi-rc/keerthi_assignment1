
from playwright.sync_api import Page, expect


def test_retrieve_text_and_attributes(page: Page):
    # Open the website
    page.goto("https://www.saucedemo.com/")

    # 1. Locate a heading and retrieve its text
    heading = page.locator(".login_logo")
    heading_text = heading.text_content()

    print("Heading text:", heading_text)
    assert heading_text == "Swag Labs"

    # 2. Retrieve inner text from a container with multiple elements
    # Use the login form container, which contains multiple elements
    container = page.locator("#login_credentials")
    container_text = container.inner_text()

    print("Container inner text:", container_text)
    assert "Accepted usernames" in container_text
    assert "standard_user" in container_text

    # 3. Retrieve an input field's value
    username = page.locator("#user-name")
    username.fill("standard_user")

    input_value = username.input_value()

    print("Username input value:", input_value)
    assert input_value == "standard_user"

    # 4. Read HTML attributes
    placeholder = username.get_attribute("placeholder")
    input_class = username.get_attribute("class")

    login_button = page.locator("#login-button")
    button_value = login_button.get_attribute("value")

    print("Username placeholder:", placeholder)
    print("Username class:", input_class)
    print("Login button value:", button_value)

    # 5. Assertions for important extracted values
    assert placeholder == "Username"
    assert input_class is not None
    assert button_value == "Login"

    print("All text, value, and attribute assertions passed.")
