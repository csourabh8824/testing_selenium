from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pdb

class GoogleSearch:
    def __init__(self, driver):   
        self.driver = driver   
        self.action = ActionChains(self.driver)
        
    
    def search(self): 
        self.driver.get("https://www.google.com/")
        fill_data = self.driver.find_element_by_xpath("//input[@title='Search']")
        fill_data.send_keys("dog")
        fill_data.send_keys(Keys.ENTER)
        time.sleep(5)
        
        #all the images 
        img = self.driver.find_element_by_link_text('Images')
        img.get_attribute('href')
        img.click()

        #to download the very first image, context_click is used to right click on image
        get_images = self.driver.find_elements_by_class_name("rg_i")
        get_images[0].click()
        
        time.sleep(3)
        self.action.context_click(get_images[0]).perform()

search_text = GoogleSearch(webdriver.Firefox())
search_text.search()

