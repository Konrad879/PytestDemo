from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)
    
    def get_title(self) -> str:
        return self.page.title()