from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')
"""Above will allow our steps to receive arguments from the feature file"""


@then('the User can see the following')
def step_impl(context):
    expected_values = [i['Navigation bar'] for i in context.table]
    """context.table will return a table. You can use the header and retrieve the values.
    Example: above I have used 'Navigation bar' which is the header 
    and when iterating it will return all the values inside the table"""
    actual_values = [i.text for i in
                     context.driver.find_elements(By.XPATH, "//div[contains(@id,'global_nav_menu_')]/div[1]")]
    set1 = set(expected_values)
    set2 = set(actual_values)
    assert set1.issubset(set2)
