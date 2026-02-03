import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page_fixture():
    # will run automatically before any test that requires 'page_fixture' parameter
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        yield page 

        browser.close()