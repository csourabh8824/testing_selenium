import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Automation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        

 
    def test_title(self):
        self.driver.get("http://testautomationpractice.blogspot.com/")
        title = self.driver.find_element(By.CLASS_NAME,"title").text
        self.assertEqual("Automation Testing Practice",title)
        
 
    def test_search(self):
        self.driver.get("http://testautomationpractice.blogspot.com/")
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Wikipedia1_wikipedia-search-input"))
        ).send_keys("Hrithik Roshan",Keys.ENTER)
 
    def tearDown(self):
        # print("tearDown Executed")
        self.driver.close()
        self.driver.quit()
 
   