import pytest
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage

def test_add_product_to_cart(page_fixture, config):
    login_page = LoginPage(page_fixture)
    product_list_page = ProductListPage(page_fixture)

    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])
    product_list_page.add_backpack_to_cart()

    assert product_list_page.get_cart_badge() == "1"