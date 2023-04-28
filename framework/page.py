from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class Page:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find_element(self, element_id: str) -> WebElement:
        return self.driver.find_element(by=AppiumBy.ID, value=element_id)

    @staticmethod
    def click_element(element: WebElement) -> None:
        element.click()

    def sign_out(self) -> None:
        side_bar = self.find_element(element_id="com.ajaxsystems:id/menuDrawer")
        self.click_element(element=side_bar)

        settings = self.find_element(element_id="com.ajaxsystems:id/settings")
        self.click_element(element=settings)

        sign_out_button = self.find_element(element_id="com.ajaxsystems:id/accountInfoLogoutNavigate")
        self.click_element(sign_out_button)
