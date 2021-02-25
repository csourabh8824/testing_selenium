from selenium import webdriver
from selenium.webdriver.support.ui import Select


class UserRegistrationFrom:
    """
        Select user registration from elements and set values and perform actions.
    """

    def select_user_registration_from_elemnets(self,driver):
        
        
        # select first name element and send value.
        self.f_name = driver.find_element_by_id("firstName")
        self.f_name.send_keys("test")
        
        # select last name element and send value.
        self.l_name = driver.find_element_by_id("lastName")
        self.l_name.send_keys("user")
        
        # select email element and send value.
        self.email = driver.find_element_by_id("userEmail")
        self.email.send_keys("test@user.com")

        # select radio button element and send value.
        element = driver.find_element_by_css_selector("input#gender-radio-2")
        webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

        #
        self.m_number = driver.find_element_by_id("userNumber")
        self.m_number.send_keys("1239875642")

        
        # select date of brith element and send value.
        self.dob = driver.find_element_by_id("dateOfBirthInput")
        self.dob.send_keys("18 Feb 2021")

        import pdb
        pdb.set_trace()

        # select check box element.
        check_box = driver.find_element_by_xpath("//input[@value='1']")
        webdriver.ActionChains(driver).move_to_element(check_box ).click(check_box ).perform()

        # Get element using id.
        state = Select(driver.find_element_by_id('css-1uccc91-singleValue'))
        state.send_keys("Uttar Pradesh")
        
        # webdriver.ActionChains(driver).move_to_element(check_box ).click(check_box ).perform()
        # state.select_by_visible_text('Uttar Pradesh')

        #
        city = Select(driver.find_element_by_id('city'))
        city.select_by_visible_text('Agra')



    def upload_file(self):

        # select image upload element.
        image_field = find_element_by_id("uploadPicture")
        image_field.send_keys("example.png")

    
    def submit_registration_form(self,driver):

        #
        driver.find_element_by_id("submit").click()
