
from playwright.sync_api import Page, expect


def test_text_input_and_keyboard_actions(page: Page):
    # 1. Open a practice website
    page.goto("https://www.saucedemo.com/")

    # 2. Locate the username input
    username = page.locator("#user-name")

    # 3. Enter data using fill()
    username.fill("standard_user")

    # Validate the entered value
    expect(username).to_have_value("standard_user")
    print("Username entered successfully")

    # 4. Use press() to perform a keyboard action
    username.press("Enter")
    print("Enter key pressed")

    # 5. Clear the existing value
    username.fill("")

    # 6. Replace it with a new value
    username.fill("problem_user")

    # 7. Demonstrate a keyboard shortcut: Ctrl+A
    username.press("Control+A")

    # Replace the selected text
    username.fill("standard_user")

    # 8. Validate the final input value
    expect(username).to_have_value("standard_user")

    print("Final username:", username.input_value())
    print("All input and keyboard actions completed")
