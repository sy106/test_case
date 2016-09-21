from selenium import webdriver

def setUp(self):

         self.driver = webdriver.Firefox()
         self.driver.implicitly_wait(30)
         self.base_url = "http://192.168.254.254/login.cgi"
         self.verificationErrors = []
         self.accept_next_alert = True