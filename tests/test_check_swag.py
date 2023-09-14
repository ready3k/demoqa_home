from conftest import browser
from pages.swag_labs import SwagLabs


def test_sauce(browser):
    page_saucedemo = SwagLabs(browser)
    page_saucedemo.visit()
    assert page_saucedemo.exist_icon()
    assert page_saucedemo.find_element('#user-name')
    assert page_saucedemo.find_element('#password')
