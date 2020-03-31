from selenium.webdriver.common.by import By


class BbcHomePage:

    BBC_HOME_PAGE_URL = "https://www.bbc.co.uk/"
    SIGN_IN_LINK = (By.ID, "idcta-link")

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.BBC_HOME_PAGE_URL)
