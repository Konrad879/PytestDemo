import pytest
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage
from pages.checkout_pages import CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage


def test_full_purchase_flow(page_fixture, config):
    
    # initialize all pages
    login_page = LoginPage(page_fixture)
    product_list_page = ProductListPage(page_fixture)
    cart_page = CartPage(page_fixture)
    checkout_step1 = CheckoutStepOnePage(page_fixture)
    checkout_step2 = CheckoutStepTwoPage(page_fixture)
    checkout_complete = CheckoutCompletePage(page_fixture)

    # action
    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])

    expected_price = product_list_page.get_backpack_price()
    expected_price_float = float(expected_price.split("$")[1])
    print(f"Price on PLP: {expected_price}")

    product_list_page.add_backpack_to_cart()
    product_list_page.go_to_cart()

    cart_page.click_checkout()
    
    checkout_step1.fill_details(config["first_name"], config["last_name"], config["postal_code"])
    cart_price = checkout_step2.get_subtotal_label()
    cart_price_float = float(cart_price.split("$")[1])

    print(f"Price in Cart: {cart_price}")
    assert expected_price_float == cart_price_float, \
        f"The price from Product List Page ({expected_price}) does not match the Cart price ({cart_price})"

    checkout_step2.click_finish()

    message = checkout_complete.get_result_message()
    assert "Thank you for your order!" in message