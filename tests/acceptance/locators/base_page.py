from selenium.webdriver.common.by import By


class BasePageLocators:
    EMAIL = By.XPATH, "//input[@id='email']"  # this is a tuple
