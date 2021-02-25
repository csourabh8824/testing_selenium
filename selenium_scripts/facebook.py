import time
import json
import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

  
class Facebook:
    def __init__(self,driver):
        self.json_data = open("credentials_load.json")
        self.driver = driver

    def convert_json_to_dict(self):
        self.python_data = json.load(self.json_data)
        print(self.python_data)

    def get_facebook_page(self):
        self.driver.get("https://www.facebook.com/")
    
    def login_facebook(self):
        email = self.driver.find_element_by_id("email")
        email.send_keys(self.python_data["Email Address"])

        password = self.driver.find_element_by_id("pass")
        password.send_keys(self.python_data["Password"])

        login = self.driver.find_element_by_id("u_0_d")
        login.send_keys(Keys.RETURN)

    def logout_facebook(self):
        pdb.set_trace()
        logout = self.driver.find_element_by_xpath("//span[text()='Log Out']")
        logout.send_keys(Keys.RETURN)        
 


def run():
    obj1 = Facebook(webdriver.Firefox())
    obj1.convert_json_to_dict()
    obj1.get_facebook_page()
    time.sleep(3)
    obj1.login_facebook()
    time.sleep(5)
    obj1.logout_facebook()

if __name__ == "__main__": 
    run()
