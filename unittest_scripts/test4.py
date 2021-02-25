import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SimpleTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://testautomationpractice.blogspot.com/")

    def test_webpage(self):
        
        title = self.driver.find_element_by_class_name("title").text    
        self.assertEqual("Automation Testing Practice",title) 

    def test_search_bar(self):
        
        self.driver.implicitly_wait(5)
        element=self.driver.find_element_by_id("Wikipedia1_wikipedia-search-input").\
            send_keys("hrithik roshan",Keys.RETURN)
        self.driver.find_element_by_link_text("Hrithik Roshan").click()

    def test_alert(self):

        self.driver.implicitly_wait(5)
        self.driver.get("http://testautomationpractice.blogspot.com/")
        self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
        self.driver.switch_to.alert.accept()
    
    def test_datepicker(self):

        self.driver.implicitly_wait(3)
        self.driver.get("http://testautomationpractice.blogspot.com/")
        self.driver.find_element_by_id("datepicker").send_keys("29/11/1970")
      
    def test_double_click(self):

        self.driver.implicitly_wait(3)
        self.driver.get("http://testautomationpractice.blogspot.com/")
        self.driver.find_element_by_id("field1").clear()
        time.sleep(3)
        self.driver.find_element_by_id("field1").send_keys("deqode",Keys.ENTER)
        self.dblclick =self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
        action = ActionChains(self.driver)
        action.double_click(self.dblclick).perform()
        time.sleep(1)
       
    def tearDown(self):
        
        self.driver.close()
        self.driver.quit()
    

if __name__ == "__main__":   
    unittest.main()
