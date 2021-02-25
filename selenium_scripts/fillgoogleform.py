from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class FillGoogleForm:
    def __init__(self,driver):
        self.driver = driver
    
    def get_and_fill_form(self):
        
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3PZLvGWrGgEjGiSfWrnRr4ZW9jqZPbRTj9B2bnlzOOIOZJA/viewform")    
        time.sleep(3)
        self.driver.maximize_window()
     
        #can be used like this: here we are traversing node by node in html but it's a long process
        # get_name = self.driver.find_element(By.XPATH,"//form[@id='mG61Hd']/div[2]/div[1]/div[2]/div[3]")
        get_name = self.driver.find_element_by_xpath("//div[@class='quantumWizTextinputPaperinputInputArea']/input[1]")
        get_name.send_keys("Sourabh choudhary")

        time.sleep(2)
        

        get_email = self.driver.find_element_by_xpath("//div[@class='quantumWizTextinputPaperinputInputArea']/input[@type='email']")
        get_email.send_keys("sochoudhary@deqode.com")

        time.sleep(2)

        #Below given line of code is used to scroll upto the given element
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.TAG_NAME,'textarea')).perform()
        #filling address
        get_address = self.driver.find_element(By.TAG_NAME, 'textarea')
        get_address.send_keys("85/4 vallabh nagar ,Indore")
        
        
        #below line of code will scroll to down
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
        
        # get_phone_number = self.driver.find_element_by_xpath("//div[@class='freebirdFormviewerComponentsQuestionTextShort']/div[1]/div[1]/div[1]/div[1]/input[1]")
        #Above line of code is not working so i tried below given code and that worked
        phone_input = self.driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")[2]        
        phone_input.send_keys("9039994596")
        time.sleep(2)

        #fill_comment
        comments = self.driver.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")[1]
        comments.send_keys("Hey Selenium is used for automated testing")

        time.sleep(1)
        submit = self.driver.find_element_by_xpath("//span[text()='Submit']")
        submit.click()
    

form = FillGoogleForm(webdriver.Chrome())
form.get_and_fill_form()


