#Navigation: History and location
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time
#By is used with 2 private methods to get element i.e find_element(),find_elements()

driver = webdriver.Firefox()
driver.get("file:///home/deqode/Desktop/testing_selenium/test/test.html")


# use of find_element
element = driver.find_element(By.ID, 'username')
element.send_keys("sourabh")

try:
    element1 = driver.find_element_by_id("username")
    element1.send_keys("sourabh123")
    time.sleep(5)
    
    element2 = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    element3 = driver.find_element_by_id("password")
    element3.send_keys("sourabh")
finally:
    pass

# use of find_elements
element1 = driver.find_elements(By.XPATH, '//form[@id="loginForm"]')
for elm in element1:
    print(elm.text)