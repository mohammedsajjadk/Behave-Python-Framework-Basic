from tests.acceptance.locators.help_page import HelpPageLocators
from tests.acceptance.page_model.base_page import BasePage


class HelpPage(BasePage):
    @property
    def url(self):
        return super(HelpPage, self).url + '/help'

    @property
    def questions_text(self):
        return self.driver.find_element(*HelpPageLocators.QUESTIONS_TEXT)

