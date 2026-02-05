from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page) #initialize constructor of a parent class
        self.base_url = "https://www.saucedemo.com/"
        
        # selectors
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open(self):
        self.navigate(self.base_url)

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)