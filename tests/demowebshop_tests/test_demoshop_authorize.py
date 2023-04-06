import os

import allure
from selene import have
from selene.support.shared import browser
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')
print(f"API_URL={API_URL}")
WEB_URL = os.getenv("WEB_URL")
print(f"WEB_URL={WEB_URL}")
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

browser.config.base_url = WEB_URL


def test_login(demowebshop):
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD},
                                allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("")

    with allure.step("Verify successful authorization"):
        browser.element(".account").should(have.text(EMAIL))


def test_add_product_to_cart(demowebshop):
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD},
                                allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/books")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    with allure.step("Add prodict to cart"):
        demowebshop.post("/addproducttocart/catalog/13/1/1")

    with allure.step("Open shopping cart"):
        browser.open("/cart")

    with allure.step("Verify successful add product to cart"):
        browser.element(".product-name").should(have.text('Computing and Internet'))


def test_add_product_to_wishlist(demowebshop):
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD},
                                allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/black-white-diamond-heart")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    with allure.step("Add prodict to wishlist"):
        demowebshop.post("/addproducttocart/details/14/2")

    with allure.step("Open wishlist"):
        browser.open("/wishlist")

    with allure.step("Verify successful add product to wishlist"):
        browser.element(".wishlist-content").should(have.text('Black & White Diamond Heart'))


def test_customer_info(demowebshop):
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD},
                                allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("/customer/info")

    with allure.step("Verify Customer info"):
        browser.element("#FirstName").should(have.value('alex'))
        browser.element("#LastName").should(have.value('kriv'))
        browser.element("#Email").should(have.value(EMAIL))


def test_logout(demowebshop):
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD},
                                allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("")

    with allure.step("Click 'Log out'"):
        browser.element("[class*='logout']").click()

    with allure.step("Verify successful logout"):
        browser.element("[class*='login']").should(have.text('Log in'))
