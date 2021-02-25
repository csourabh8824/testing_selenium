import home_page


class LoginPage:
    """
    Select login page element and perform some operations.
    """

    def get_locator_of_login_page(self,driver):
        
        #locator for username field.
        self.username = driver.find_element_by_id("username")

        #locator for password field.
        self.password = driver.find_element_by_id("password")

    def enter_values(self,username,password):
                    
        # set value of username.
        self.username.send_keys(username)
        
        # set value of password.
        self.password.send_keys(password)

    def submit_login_form(self,driver):

        # submit login form
        driver.find_element_by_xpath("/html/body/app-root/uas-portal/div/div[2]/main/div/o-auth/section/div/app-login/section/div/div/form/div[3]/button").click()

    
        

