from tests.acceptance.locators.cookies_page import CookiesPageLocators
from tests.acceptance.page_model.base_page import BasePage


class CookiesPage(BasePage):
    @property
    def url(self):
        return super(CookiesPage, self).url + '/policies/cookies/'

    @property
    def cookie_text(self):
        return self.driver.find_element(*CookiesPageLocators.COOKIE_TEXT)

    def total_links(self):
        return self.driver.find_elements(*CookiesPageLocators.SIDE_LINKS)