import unittest

class simpleTest(unittest.TestCase):

    def setUp(self,url=None):
        # initialization of webdriver
        self.tes = "rrrrr"
    
    def test_upper(self):
        print("$$$$$$$$$$$$$$$$$$")
        # self.assertEqual('sourabh'.upper(),"SOURABH","Concept Cleared")
    
    def test_best(self):
        print("########################3")
        # self.assertTrue('SOURABH'.isupper())
        # self.assertTrue('sourabh'.islower())
    

if __name__ == '__main__':
    unittest.main()