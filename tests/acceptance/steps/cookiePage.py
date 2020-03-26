from behave import *
from selenium import webdriver

from tests.acceptance.page_model.cookies_page import CookiesPage

use_step_matcher('re')
"""Above will allow our steps to receive arguments from the feature file"""


@given('the User navigates to the cookiepage')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\BehaveFramework\drivers\chromedriver.exe")
    page = CookiesPage(context.driver)
    context.driver.get(page.url)


@when('the User can see cookie text')
def step_impl(context):
    page = CookiesPage(context.driver)
    assert page.cookie_text.is_displayed()
