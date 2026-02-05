import pytest
from pages.login_page import LoginPage

def test_valid_login(page_fixture, config):
    login_page = LoginPage(page_fixture)
    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])

    assert "inventory" in page_fixture.url

def test_invalid_login(page_fixture, config):
    login_page = LoginPage(page_fixture)
    login_page.open(config["base_url"])

    login_page.login("incorrect_user", "incorrect_password")

    error_text = login_page.get_error_message()
    assert "Epic sadface" in error_text