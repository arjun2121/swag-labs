import pytest
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page:Page):
        self.page=page

    def click_on_item(self,item_name):
        self.page.locator(f"text={item_name}").click()

    def add_item_to_cart(self):
        self.page.click("text=Add to cart")

    def go_to_cart(self):
        self.page.click('//div[@id="shopping_cart_container"]')