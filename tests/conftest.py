import os

import pytest
from dotenv import load_dotenv
from qa_guru_python_3_14.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def demowebshop():
    api_url = os.getenv("API_URL")
    return BaseSession(api_url)


@pytest.fixture(scope="session")
def reqresin():
    api_url = os.getenv("API_URL_PART_1")
    return BaseSession(api_url)