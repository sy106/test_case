#coding=utf-8

import unittest, login,quit,set_up

class test_ODU_login(unittest.TestCase):

     def test_login(self):
         u"""ODU登录"""
         set_up.setUp(self)
         driver = self.driver

         driver.get(self.base_url + "/")
         login.login(driver)
         quit.quit(driver)

if __name__ == "__main__":
    unittest.main()