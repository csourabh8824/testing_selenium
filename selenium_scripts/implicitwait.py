from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("file:///home/deqode/Desktop/testing_selenium/test/test.html")
element1 = driver.find_element_by_id("username")
element1.send_keys("sourabh")
element2 = driver.find_element_by_id("password")
element2.send_keys("password")