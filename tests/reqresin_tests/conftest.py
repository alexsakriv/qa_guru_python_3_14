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
def reqresin():
    api_url = os.getenv("API_URL_PART_1")
    return BaseSession(api_url)