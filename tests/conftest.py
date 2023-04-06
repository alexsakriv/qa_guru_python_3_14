import os

import pytest
from dotenv import load_dotenv
from qa_guru_python_3_14.utils.base_session import BaseSession
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene.support.shared import browser


load_dotenv()


@pytest.fixture(scope="session")
def demowebshop():
    api_url = os.getenv("API_URL")
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

    return BaseSession(api_url)


@pytest.fixture(scope="session")
def reqresin():
    api_url = os.getenv("API_URL_PART_1")
    return BaseSession(api_url)