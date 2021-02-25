import unittest
from selenium import webdriver

class InitializeDriver(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()