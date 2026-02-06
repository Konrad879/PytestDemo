import pytest
from datetime import datetime
import json
from playwright.sync_api import sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page_fixture", None)
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"
            page.screenshot(path=screenshot_name)
            print(f"\nZrobiono screenshot: {screenshot_name}")


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