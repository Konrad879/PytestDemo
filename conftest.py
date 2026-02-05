import pytest
import json
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def config():
    with open("secret_config.json") as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def page_fixture():
    # will run automatically before any test that requires 'page_fixture' parameter
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        yield page 

        browser.close()