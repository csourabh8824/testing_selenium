from initialize_driver import InitializeDriver
from locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def search_wikipedia(self,driver):
        self.wiki = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Locator.wikipedia_inputbox))
        )
    
    def insert_text(self,text):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Locator.wikipedia_inputbox))
        ).send_keys(text)

    def searching(self,driver):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((Locator.wikipedia_button))
        ).click()