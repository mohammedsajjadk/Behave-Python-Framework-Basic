from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def cookies_link(self):
        return 'https://www.facebook.com/policies/cookies/'

    @property
    def logo(self):
        return self.driver.find_element(*HomePageLocators.LOGO)
