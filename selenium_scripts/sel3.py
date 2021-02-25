from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("file:///home/deqode/Desktop/testing_selenium/test/test.html")

username = driver.find_element_by_id("username")
# You should also be careful when using XPATH in WebDriver. If there’s more 
# than one element that matches the query, then only the first will be returned.
username = driver.find_element_by_xpath("//input[@id='username']")
password = driver.find_element_by_id("password")


username.send_keys("virat")
password.send_keys("sourabh321")
#for selecting values from dropdown
select = Select(driver.find_element_by_name("cars"))
select.select_by_value("audi")
# can be done like this too:
# select.select_by_index(index)
# select.select_by_visible_text("text")

#To take screenshot:
driver.save_screenshot('screenshot.png')

#used to switch between windows
# driver.switch_to_window("windowName") #points to the target value of a tag

#Ways to submit the form:

post = driver.find_element_by_name("submit")

# post.send_keys(Keys.RETURN)

# click(): waits only if any explicit wait condition is provided
# post.click()

# submit(): submit() does not wait.
# post.submit()

alert = driver.switch_to.alert
print(alert)

