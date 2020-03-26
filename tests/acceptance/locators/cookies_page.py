from selenium.webdriver.common.by import By


class CookiesPageLocators:
    SIDE_LINKS = By.XPATH, "//div[@role='presentation']/a"
    COOKIE_TEXT = By.XPATH, "//div[contains(@class,'cookiesPolicy')]//h2"
