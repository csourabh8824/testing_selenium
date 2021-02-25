import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDownloadFile:
    def __init__(self,driver):
        self.driver = driver
    
    def download_file(self):
        
        self.driver.get("https://online2pdf.com/convert-odt-to-pdf")
        select_file = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "browse_button"))
        )
        select_file.send_keys(Keys.RETURN)

        time.sleep(4)
        
        convert_to_pdf = self.driver.find_element_by_xpath("//form[@name='form1']/div[3]/button[1]")
        convert_to_pdf.send_keys(Keys.RETURN)



download = SeleniumDownloadFile(webdriver.Firefox())
download.download_file()