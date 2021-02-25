import pytest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

    
# def test_myntra():
#     driver = webdriver.Chrome()
#     driver.get("https://www.djangoproject.com/")
#     time.sleep(4)
#     title = driver.find_element_by_class_name("logo").text
#     assert title =="Django"

class TestSeleniumPytest():
    
    @pytest.fixture
    def setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield
        time.sleep(5)
        driver.close()
        driver.quit()

    def test_web(self,setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def test_login(self,setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        username = driver.find_element_by_id("txtUsername").send_keys("Admin")
        time.sleep(3)
        password = driver.find_element_by_id("txtPassword").send_keys("admin123")
        time.sleep(2)
        login = driver.find_element_by_id("btnLogin").click()
    
    def test_scroll(self,setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        last_pixel = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0,{last_pixel})")

    def test_dashboard(self,setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        username = driver.find_element_by_id("txtUsername").send_keys("Admin")
        time.sleep(3)
        password = driver.find_element_by_id("txtPassword").send_keys("admin123")
        time.sleep(2)
        login = driver.find_element_by_id("btnLogin").click()
        profile = driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
        assert profile == "Dashboar1d"


