import os
import time
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

try:
    #Filling email
    email_or_number = driver.find_element_by_id("identifierId")
    email_or_number.send_keys("sochoudhary@deqode.com")

    #Submitting email
    submit_email = driver.find_element_by_class_name("VfPpkd-RLmnJb")
    submit_email.click()
    time.sleep(3)
  
    

    #Filling password
    password = driver.find_element_by_class_name("whsOnd")
    password.send_keys("sourabh321")

    #Submitting password
    submit_password = driver.find_element_by_class_name("VfPpkd-RLmnJb")
    submit_password.click()

    #To maximize window
    driver.maximize_window()
    time.sleep(3)

    #clicking on compose email
    click_compose = driver.find_element_by_class_name("T-I-KE")
    click_compose.click()
    time.sleep(4)

    #mail sending to:
    to = driver.find_element_by_class_name("vO")
    to.send_keys("sparashar@deqode.com")
    time.sleep(6)

    #Filling in Subject
    subject = driver.find_element_by_class_name("aoT")
    subject.send_keys("Python script that sends automated mail")
    time.sleep(6)

    #Filling in mail body
    fill_body = driver.find_element_by_class_name("Am")
    fill_body.send_keys("Hello Sir ,I have attached these 2 files one is python script that\
    sends the email and other is image file")
    time.sleep(6)
  
    # Clicking attach button
    # click_attach = driver.find_element_by_id(":df").click()
   
    # time.sleep(10)
    
    # sending email
    # send_email = driver.find_element_by_id(":bp")
    # send_email.send_keys(Keys.RETURN)
except:
    print("Exception occurred")
finally:
    time.sleep(10)
    driver.quit()
    