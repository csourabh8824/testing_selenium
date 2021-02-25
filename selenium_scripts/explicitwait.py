#Expicit Wait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Firefox()
driver.get("file:///home/deqode/Desktop/testing_selenium/test/test.html")
#When we want our driver to wait for some seconds, we use expicit waits so that 
# if some dynamic conditions are there it can get implemented.If the element is 
# present it returns us the answer and if not we can run exception "TimeoutException"  
try:
    element1 = driver.find_element_by_id("username")
    element1.send_keys("sourabh")
    element2 = WebDriverWait(driver,10).until(
         EC.presence_of_element_located((By.NAME, "password")))
    # element = WebDriverWait(driver,10).until(
    #      EC.presence_of_element_located((By.NAME, "1q")))
    element2.send_keys("selenium")
    time.sleep(3)
    element3 = driver.find_element_by_xpath("//input[@name='submit']") 
    element3.send_keys(Keys.RETURN)
except TimeoutException:
    print("Failed to load search bar")
finally:
    # driver.quit()
    pass


#Implicit waits: In this,wait tells webdriver to poll(wait) for certain amt of time
#This is basically used before we call the get method



