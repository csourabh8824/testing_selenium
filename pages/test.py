import unittest
import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from home_page import HomePage
from login_page import LoginPage
from student_registration import UserRegistrationFrom


class UserTest(unittest.TestCase):
    """
    Test case for test user login page.
    """

    def setUp(self,url=None):
        # initialization of webdriver
        
        
        self.driver = webdriver.Chrome()
        
        
        # create login page object.
        self.login_page = LoginPage()

       


    def test_login_process(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        self.driver.get("https://techracers1.greythr.com/uas/portal/auth/login?login_challenge=e2bf61d640cf4957962ebc50a3ffe13a")
        self.driver.maximize_window()



        # get username and password element from login page.
        self.login_page.get_locator_of_login_page(self.driver)

        # set username and password values into element
        self.login_page.enter_values("EC/INDB/226","sourabh@54321")

        # submit login form.
        self.login_page.submit_login_form(self.driver)


    # def test_validate_user_login_data(self):
        
    #     print("###############################3332")
    #     # access home page of web application.
    #     self.driver.get("https://www.demoqa.com/books")

    #     # click on login button to open login page from home page.
    #     self.home_page.click_on_login_btn(self.driver)

    #     # get username and password element from loging page.
    #     self.login_page.get_locator_of_login_page(self.driver)

    #     # set username and password values into element
    #     self.login_page.enter_values("testuser","admin")

    #     # submit login form.
    #     self.login_page.submit_login_form(self.driver)

    #     # stop the script execution on a particular condition for a specified duration.
    #     self.driver.implicitly_wait(10);
    #     # WebDriverWait(self.driver, 10).until(driver.find_element_by_id("name"))

    #     # get validation message.
    #     message = self.login_page.check_validation(self.driver)

    #     self.assertEqual(message,"Invalid username or password!")

    
    # def test_user_registration_form(self):
        
    #     self.driver.get("https://www.demoqa.com/books")
    #     self.driver.maximize_window()

    #     el = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/div/div/div[5]/span/div")
    #     import pdb
    #     pdb.set_trace()
    #     # action = webdriver.ActionChains(self.driver).move_to_element(el).click(el )
    #     action = webdriver.ActionChains(self.driver)
    #     action.click(on_element=el)
    #     # action.move_to_element(self.driver.find_element_by_xpath("//*[@id='item-0']/span")).click()
    #     action.perform()
    #     time.sleep(10)
        
    #     # fill user registration form.
    #     # self.user_registration.select_user_registration_from_elemnets(self.driver)

    #     # upload a file.
    #     # self.user_registration.upload_file(self.driver)

    #     # Submit user registration form. 
    #     # self.user_registration.submit_registration_form(self.driver)
               


# execute the script.
if __name__ == "__main__":
    import sys
    unittest.main()