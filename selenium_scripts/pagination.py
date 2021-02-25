import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MyntraPagination:
    def __init__(self,driver):
        self.driver = driver
        time.sleep(5)
        

    def forward_paginate(self):
        self.driver.get("https://www.myntra.com/")
        self.driver.maximize_window()
        time.sleep(3)
        search_bar = self.driver.find_element_by_class_name("desktop-searchBar")
        search_bar.send_keys("hrx",Keys.RETURN)
        pages = self.driver.find_elements_by_class_name("pagination-number")
        
        no_of_pages = len(pages)
        print(no_of_pages)
        time.sleep(5)        

        for page in pages:
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,4900)")
            time.sleep(2)
            next_page = self.driver.find_element(By.XPATH,"//li[@class='pagination-next']/a[1]")
            next_page.click()
        self.driver.execute_script("window.scrollTo(0,4900)")

    def backward_paginate(self):
        pages = self.driver.find_elements_by_class_name("pagination-number")
        for page in reversed(pages):
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,4900)")
            previous_page = self.driver.find_element(By.XPATH,"//li[@class='pagination-prev']/a[1]")
            time.sleep(3)
            previous_page.click()        

    def paginate_to_specific_page(self):
        page_no = input("Which page number you want to see ?")
        # time.sleep(3)
        search_bar = self.driver.find_element_by_class_name("desktop-searchBar")
        search_bar.send_keys("hrx",Keys.RETURN)
        time.sleep(5)
        # pages = self.driver.find_elements_by_class_name("pagination-number")
        page = self.driver.find_element_by_link_text(page_no)
        time.sleep(5)       
        page.click()
            
           
 
           
       

display_page = MyntraPagination(webdriver.Chrome())
display_page.forward_paginate()
time.sleep(3)
display_page.backward_paginate()
time.sleep(3)
display_page.paginate_to_specific_page()