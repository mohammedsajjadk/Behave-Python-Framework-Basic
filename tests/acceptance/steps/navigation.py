from behave import *
from page_model.cookies_page import CookiesPage
from page_model.help_page import HelpPage
from page_model.location_page import LocationPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@given('the User navigates to the "(.*)"')
def step_impl(context, page_name):
    if page_name == 'home page':
        home_page = HomePage(context.driver)
        context.driver.get(home_page.url)
    elif page_name == 'location page':
        location_page = LocationPage(context.driver)
        context.driver.get(location_page.url)
    elif page_name == 'cookies page':
        cookies_page = CookiesPage(context.driver)
        context.driver.get(cookies_page.url)
    elif page_name == 'help page':
        help_page = HelpPage(context.driver)
        context.driver.get(help_page.url)
    # class_name = eval(''.join([i[0].upper() + i[1::] for i in page_name.split(' ')]))
    # context.driver.get(class_name(context.driver).url)


@step('the User can see "(.*)" (.*)')
def step_impl(context, element, element_type):
    if element_type == 'icon':
        page = HomePage(context.driver)
        assert page.logo.is_displayed()
    elif element_type == 'textbox':
        page = HomePage(context.driver)
        assert page.text_box(element).is_displayed()


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
        assert base_page.email.is_displayed()
    elif page_name == 'cookies_page':
        WebDriverWait(context.driver, 10).until(
            expected_conditions.url_matches(page.cookies_link))
        assert context.driver.current_url == page.cookies_link
        assert base_page.email.is_displayed()
