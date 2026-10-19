


import pytest


@pytest.fixture
def custom_context(browser):
    context = browser.new_context()
    yield context
    context.close()





@pytest.fixture
def app_url():
    return "https://www.saucedemo.com/"