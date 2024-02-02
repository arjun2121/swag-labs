import logging

from Pages.LoginPage import login_flow
from Pages.HomePage import HomePage
import pytest

@pytest.mark.dd
def test_dd(login_flow,page):
    home_page=HomePage(page)
    item_name= "Sauce Labs Backpack"
    home_page.click_on_item(item_name)
    home_page.add_item_to_cart()
    home_page.go_to_cart()
    cart_item=page.locator('.inventory_item_name').inner_text()
    assert item_name==cart_item, f"Expected cart item: {item_name}, Actual cart item: {cart_item}"
