from behave import *

use_step_matcher('re')


@step('the User can see the total of (.*) products')
def step_impl(context, expected_total):
    products_list = context.driver.find_elements_by_css_selector('.products-wrapper .products .product')
    assert len(products_list) == int(expected_total)
