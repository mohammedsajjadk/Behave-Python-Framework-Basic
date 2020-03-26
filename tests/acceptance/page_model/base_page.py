from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.facebook.com'  # notice no '/' at the end

    @property
    def email(self):
        return self.driver.find_element(*BasePageLocators.EMAIL)
