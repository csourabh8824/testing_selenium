#Brief intro about selenium  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Special keys can be sent using Keys
#step1: create object of webdriver
driver = webdriver.Firefox()
print(driver)

#step2: get the web
driver.get("http://www.python.org")
print(driver.title)

assert "Python" in driver.title 
#assert used in debugging purpose, returns boolean value.If any error is there returns 
# AssertionError


#find_element_by_name is used to find the html element by name there are many other locating elements
#other locating elements :https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
elem = driver.find_element_by_name("q") #here in elem we get search input from the python.org
# elem.clear()
elem.send_keys("pycon") #this line is used to send the keys.It will set the value(pycon) in search input
elem.send_keys(Keys.RETURN) #Special keys are sent with the help of Keys class Here RETURN is special key
assert "No results found." not in driver.page_source #doubt
driver.close()