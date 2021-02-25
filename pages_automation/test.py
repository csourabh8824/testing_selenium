import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from home_page import HomePage

class TestWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.homepage = HomePage

    def test_webpage(self):
        self.driver.get("http://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        self.homepage.search_wikipedia(self,self.driver)
        self.homepage.insert_text(self,"Hrithik roshan")
        self.homepage.searching(self,self.driver)
        time.sleep(14)
        