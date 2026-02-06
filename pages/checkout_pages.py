from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"

    def fill_details(self, first: str, last: str, zip_code: str):
        self.fill(self.first_name_input, first)
        self.fill(self.last_name_input, last)
        self.fill(self.postal_code_input, zip_code)
        self.click(self.continue_button)


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.finish_button = "#finish"
        self.subtotal_label = ".summary_subtotal_label"

    def get_subtotal_label(self):
        return self.get_text(self.subtotal_label)
    
    def click_finish(self):
        self.click(self.finish_button)


class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.complete_header = ".complete-header"

    def get_result_message(self):
        return self.get_text(self.complete_header)