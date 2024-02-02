import pytest
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page=page

    def navigate_to_url(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self,username):
        self.page.locator('//input[@id="user-name"]').fill(username)

    def enter_password(self,password):
        self.page.locator('//input[@id="password"]').fill(password)

    def click_login_button(self):
        self.page.locator('//input[@id="login-button"]').click()

@pytest.fixture
def login_flow(page):
    login_page = LoginPage(page)
    login_page.navigate_to_url()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    assert page.is_visible('text=Products')
    yield
    page.close()