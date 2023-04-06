import os
import time

import allure
from selene import have
from selene.support.shared import browser
from dotenv import load_dotenv

load_dotenv()

WEB_URL = os.getenv("WEB_URL")
EMAIL = os.getenv('EMAIL')

browser.config.base_url = WEB_URL


def test_login(demowebshop):
    browser.open("")

    with allure.step("Verify successful authorization"):
        browser.element(".account").should(have.text(EMAIL))


def test_add_product_to_cart(demowebshop):
    with allure.step("Add prodict to cart"):
        demowebshop.post("/addproducttocart/catalog/13/1/1")

    with allure.step("Open shopping cart"):
        browser.open("/cart")

    with allure.step("Verify successful add product to cart"):
        browser.element(".product-name").should(have.text('Computing and Internet'))
        time.sleep(1)


def test_add_product_to_wishlist(demowebshop):
    with allure.step("Add product to wishlist"):
        demowebshop.post("/addproducttocart/details/14/2")

    with allure.step("Open wishlist"):
        browser.open("/wishlist")

    with allure.step("Verify successful add product to wishlist"):
        browser.element(".wishlist-content").should(have.text('Black & White Diamond Heart'))
        time.sleep(1)


def test_customer_info(demowebshop):
    browser.open("/customer/info")

    with allure.step("Verify Customer info"):
        browser.element("#FirstName").should(have.value('alex'))
        browser.element("#LastName").should(have.value('kriv'))
        browser.element("#Email").should(have.value(EMAIL))


def test_logout(demowebshop):
    browser.open("")

    with allure.step("Click 'Log out'"):
        browser.element("[class*='logout']").click()

    with allure.step("Verify successful logout"):
        browser.element("[class*='login']").should(have.text('Log in'))
