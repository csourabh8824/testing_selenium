import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import zxing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestWeb:
    
    @pytest.fixture
    def setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield 
        time.sleep(2)
        driver.close()
        driver.quit()
    
 
    
    def test_title(self,setup):
        driver.implicitly_wait(5)
        driver.get("http://testautomationpractice.blogspot.com/")
        title = driver.find_element(By.CLASS_NAME,"title").text
        assert title == "Automation Testing Practice"

    def test_search_bar(self,setup):
        driver.implicitly_wait(5)
        driver.get("http://testautomationpractice.blogspot.com/")
        element=driver.find_element_by_id("Wikipedia1_wikipedia-search-input").\
            send_keys("hrithik roshan",Keys.RETURN)
        driver.find_element_by_link_text("Hrithik Roshan").click()

    def test_alert(self,setup): 
        driver.implicitly_wait(5)
        driver.get("http://testautomationpractice.blogspot.com/")
        driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
        driver.switch_to.alert.accept()

    def test_datepicker(self,setup):
        driver.implicitly_wait(3)
        driver.get("http://testautomationpractice.blogspot.com/")
        driver.find_element_by_id("datepicker").send_keys("29/11/1970")

    def test_double_click(self,setup):
        driver.implicitly_wait(3)
        driver.get("http://testautomationpractice.blogspot.com/")
        driver.find_element_by_id("field1").clear()
        time.sleep(3)
        driver.find_element_by_id("field1").send_keys("deqode",Keys.ENTER)
        dblclick = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
        action = ActionChains(driver)
        action.double_click(dblclick).perform()
        time.sleep(1)
    
    def test_drag_and_drop(self,setup):
        driver.implicitly_wait(3)
        driver.get("http://testautomationpractice.blogspot.com/")
        source = driver.find_element_by_id("draggable")
        destination = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.drag_and_drop(source,destination).perform()
        time.sleep(5)

    def test_sign_up_form(self,setup):
        driver.implicitly_wait(4)
        driver.get("http://testautomationpractice.blogspot.com/")
        time.sleep(10)
        first_name = driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Sourabh")
        time.sleep(1)
        last_name = driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Choudhary")
        time.sleep(1)
        phone_no = driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9826543312")
        time.sleep(1)
        country = driver.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
        time.sleep(1)
        city = driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Indore")
        time.sleep(1)
        email = driver.find_element(By.ID,"RESULT_TextField-6").send_keys("sochoudhary@deqode.com")
        time.sleep(1)
        driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()
        time.sleep(1)
        driver.find_element(By.ID,"RESULT_CheckBox-8_3").click()
        time.sleep(1)
        select = Select(driver.find_element(By.ID,"RESULT_RadioButton-9"))
        select.click()
        time.sleep(2)
        select.select_by_value('Radio-0')
        driver.find_element(By.NAME,"RESULT_FileUpload-10").click()
        time.sleep(7)
        driver.find_element(By.ID,"FSsubmit").click()

    def test_select_menu(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        time.sleep(2)
        select1 = Select(driver.find_element_by_name("speed"))
        for opt in select1.options:
            select1.select_by_visible_text('Faster')
        
        select2 = Select(driver.find_element_by_id("files"))
        time.sleep(2)
        select2.select_by_value("3")

        select3 = Select(driver.find_element_by_name("number"))
        select3.select_by_visible_text("4")

        select4 = Select(driver.find_element_by_id("products"))
        select4.select_by_value("Apple")

        select5 = Select(driver.find_element_by_name("animals"))
        select5.select_by_visible_text("Avatar")


    def test_drag_and_drop_images(self,setup):
       
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML11")
        action = ActionChains(driver)
        time.sleep(2)
        
        driver.execute_script("arguments[0].scrollIntoView();", element)
        
        source1 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/div/ul/li[1]/img")
        destination = driver.find_element_by_id("trash")
        
        source2 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/\
            div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/div/ul/li[2]/img")
        
        action.drag_and_drop(source1,destination).perform()
        action.drag_and_drop(source2,destination).perform()
        time.sleep(5)
    
    def test_slider(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML7")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        slider = driver.find_element_by_id("slider")
        action.click_and_hold(slider).move_by_offset(0, 50).release().perform()

    def test_resize(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML3")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        resize = driver.find_element_by_class_name("ui-resizable-se")
        action.drag_and_drop_by_offset(resize,50, 150).perform()


    def test_html_table(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML1")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)
       
        row = driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/\
            div[2]/div[1]/div/div[1]/table/tbody/tr")
        print(len(row))
        with open('test.odt',mode='w') as my_file:
            for data in row:
                text = my_file.write(str(data.text))

    
    def test_hover(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML8")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        hover_on_element = driver.find_element_by_id("age")
        time.sleep(2)
        perform_hover = action.move_to_element(hover_on_element).perform()
        time.sleep(2)

    def test_reading_qr_code(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_id("HTML4")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        file_path = os.path.abspath("qrcode.png")
        reader = zxing.BarCodeReader()
        qrcode = reader.decode(file_path)
        with open('test.odt',mode='a') as my_file:
            my_file.write(qrcode.raw)

    def test_reading_barcode(self,setup):
        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_elent_by_id("HTML12")
        action = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView();",element)
        time.sleep(2)
        file_path = os.path.abspath("barcode2.gif")
        reader = zxing.BarCodeReader()
        barcode = reader.decode(file_path)
        with open('test.odt',mode='a') as my_file:
            my_file.write(barcode.raw)
