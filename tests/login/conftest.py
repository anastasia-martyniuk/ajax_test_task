import pytest
from appium.webdriver.webdriver import WebDriver

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver: WebDriver) -> LoginPage:
    yield LoginPage(driver)
