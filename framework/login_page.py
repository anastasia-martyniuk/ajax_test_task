import time
from typing import List

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException, StaleElementReferenceException

from .page import Page
from utils.android_utils import android_get_desired_capabilities


class LoginPage(Page):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver=driver)

    def find_elements(self, class_name: str) -> List[WebElement]:
        elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value=class_name)
        return elements

    @staticmethod
    def send_key(element: WebElement, key: str) -> None:
        element.send_keys(key)

    def log_in(self, email: str, password: str) -> bool:
        self.driver.implicitly_wait(10)

        log_in = self.find_elements(class_name="android.widget.Button")[0]
        log_in.click()
        self.driver.implicitly_wait(10)

        email_and_password = self.find_elements(class_name="android.widget.EditText")
        self.send_key(element=email_and_password[0], key=email)
        self.send_key(element=email_and_password[1], key=password)

        button = self.find_elements(class_name="android.widget.Button")[1]
        button.click()
        time.sleep(6)

        try:
            self.find_element(element_id="com.ajaxsystems:id/agreement")

        except (NoSuchElementException, StaleElementReferenceException):
            return True
        else:
            self.find_element(element_id="com.ajaxsystems:id/back").click()
            return False


if __name__ == "__main__":
    page = LoginPage(driver=webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities()))
    page.log_in(email="qa.ajax.app.automation@gmail.com", password="password")
