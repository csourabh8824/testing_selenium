from selenium.webdriver.common.by import By

class Locator:
    
    #Locators for wikipedia
    wikipedia_inputbox = (By.ID,"Wikipedia1_wikipedia-search-input")
    wikipedia_button = (By.CLASS_NAME,"wikipedia-search-button")