from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = By.XPATH, "//i[starts-with(@class,'fb_logo ')]"

    """above variable hold tuple, it is equal to (By.XPATH, "//input[@type='search']")"""
