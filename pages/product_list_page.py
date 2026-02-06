from pages.base_page import BasePage

class ProductListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_backpack_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"
        self.backpack_price = "(//div[@class='inventory_item_price'])[1]"

    def add_backpack_to_cart(self):
        self.click(self.add_backpack_to_cart_button)

    def get_cart_badge(self) -> str:
        return self.get_text(self.cart_badge)
    
    def go_to_cart(self):
        self.click(self.cart_badge)

    def get_backpack_price(self):
        return self.get_text(self.backpack_price)