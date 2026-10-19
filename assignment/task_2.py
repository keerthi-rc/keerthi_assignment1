
import pytest
from playwright.sync_api import expect


@pytest.fixture
def my_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def my_page(my_context):
    page = my_context.new_page()
    yield page
    page.close()


def test_using_my_page(my_page):
    my_page.goto("https://www.python.org/")
    expect(my_page).to_have_title(
        "Welcome to Python.org"
    )


def test_first_context(my_page):
    my_page.goto("https://www.python.org/")

    my_page.evaluate(
        "localStorage.setItem('name', 'keerthi')"
    )

    assert my_page.evaluate(
        "localStorage.getItem('name')"
    ) == "keerthi"


def test_second_context(my_page):
    my_page.goto("https://www.python.org/")

    assert my_page.evaluate(
        "localStorage.getItem('name')"
    ) is None                          #Browser, context and page fixtures
