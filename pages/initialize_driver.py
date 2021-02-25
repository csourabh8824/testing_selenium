import unittest

class DeriverInitialized(unittest.TestCase):
    """
    test class for select elemets of home page and perform operations.
    """
    def setUp(self):
      
        self.driver = webdriver.Chrome()
        
        # self.driver = webdriver.Chrome(executable_path="/home/deqode/projects/automation/chromedriver_linux64/chromedriver",chrome_options=self.chrome_options)
      