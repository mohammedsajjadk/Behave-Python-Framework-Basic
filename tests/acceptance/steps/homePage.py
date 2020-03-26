from behave import *
from selenium import webdriver

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')
"""Above will allow our steps to receive arguments from the feature file"""


@given('the User navigates to the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\BehaveFramework\drivers\chromedriver.exe")
    page = HomePage(context.driver)
    context.driver.get(page.url)
