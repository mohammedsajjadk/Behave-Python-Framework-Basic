from pathlib import Path

from selenium import webdriver


def before_all(context):
    print("before_all")


def after_all(context):
    print("after_all")


def before_feature(context, feature):
    if "Facebook's Home Page and Cookie Page" in str(feature):
        print("before_feature")


def after_feature(context, feature):
    if "Facebook's Home Page and Cookie Page" in str(feature):
        print("after_feature")


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path=f"{Path(__file__).parent.parent.parent}\drivers\chromedriver.exe")
    """Path(__file__).parent.parent.parent ==> This will give the project root path
    I have traversed to the root path using 'parent' """

    if "User checks the cookie text and navigation links" in str(scenario):
        print("before_scenario")


def after_scenario(context, scenario):
    context.driver.quit()
    if "User checks the cookie text and navigation links" in str(scenario):
        print("after_scenario")


def before_step(context, step):
    if "the User navigates to the cookie page" in str(step):
        print("before_step")


def after_step(context, step):
    if "the User navigates to the cookie page" in str(step):
        print("after_step")
