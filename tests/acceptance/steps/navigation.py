from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@then('the User can see "(.*)" icon')
def step_impl(context, element):
    if element == 'icon':
        page = HomePage(context.driver)
        assert page.logo.is_displayed()


@step('the User clicks "(.*)" (.*)')
def step_impl(context, element, element_type):
    if element_type == 'button':
        context.driver.find_element_by_xpath("//button[text()='" + element + "']").click()
    elif element_type == 'link':
        context.driver.find_element_by_xpath("//a[text()='" + element + "']").click()


@step('the User is on the "(.*)"')
def step_impl(context, page_name):
    page = HomePage(context.driver)
    base_page = BasePage(context.driver)  # not required to do like this, but just showing
    if page_name == 'home_page':
        assert context.driver.current_url == page.url
        assert base_page.email
    elif page_name == 'cookies_page':
        WebDriverWait(context.driver, 10).until(
            expected_conditions.url_matches(page.cookies_link))
        assert context.driver.current_url == page.cookies_link
        assert base_page.email
