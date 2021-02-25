import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pdb
class ScrollByPixel:
    def __init__(self,driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        

    def scroll(self):
        self.driver.get("https://selenium-python.readthedocs.io/navigating.html")
        self.driver.maximize_window()
        pixel1 = 0
        pixel2 = 300
        last_pixel_of_page = self.driver.execute_script("return document.body.scrollHeight")
        print("last_pixel_of_page",last_pixel_of_page)
        while(1):
            if pixel2>last_pixel_of_page:
                break
            self.driver.execute_script(f"window.scrollTo({pixel1}, {pixel2})")
            time.sleep(1)
            pixel1=pixel2
            pixel2+=300
            
            
        #Toscroll to bottom of the page: 
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
        # time.sleep(3)

        #To scroll upto some specific pixel:
        # self.driver.execute_script("window.scrollTo(0, 3400)")


pixel = ScrollByPixel(webdriver.Chrome())
pixel.scroll()
