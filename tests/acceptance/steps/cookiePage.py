from behave import *

from tests.acceptance.page_model.cookies_page import CookiesPage


@when('the User can see cookie text')
def step_impl(context):
    page = CookiesPage(context.driver)
    assert page.cookie_text.is_displayed()


# Passing Parameter to steps using Parse module
@then('the User can see {expected_number_of_links} navigation links')
def step_impl(context, expected_number_of_links):
    page = CookiesPage(context.driver)
    assert len(page.total_links()) == int(expected_number_of_links)
