from behave import *

from tests.acceptance.page_model.help_page import HelpPage

use_step_matcher('re')
"""Above will allow our steps to receive arguments from the feature file"""


@then('the User can see the Questions Text')
def step_impl(context):
    page = HelpPage(context.driver)
    assert page.questions_text.is_displayed()
