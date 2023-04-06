import os

import pytest
from dotenv import load_dotenv
from qa_guru_python_3_14.utils.base_session import BaseSession
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene.support.shared import browser
from qa_guru_python_3_14.utils import attach


load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope="session")
def demowebshop():
    api_url = os.getenv("API_URL")
    yield BaseSession(api_url)


@pytest.fixture(scope="function", autouse=True)
def app(demowebshop):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    WEB_URL = os.getenv("WEB_URL")
    browser.config.base_url = WEB_URL
    response = demowebshop.post("/login", json={"Email": EMAIL, "Password": PASSWORD}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

    browser.quit()

