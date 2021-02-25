from initialize_driver import DeriverInitialized


class HomePage:
    """
    Test class for select elemets of home page and perform operations.
    """

    def access_web_application(self,url=None):
        # opening the web appliction home page. 
        self.driver.get("https://techracers1.greythr.com/uas/portal/auth/login?login_challenge=e2bf61d640cf4957962ebc50a3ffe13a")
    
    
