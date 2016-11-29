#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_sim_lock(unittest.TestCase):
    def test_login(self):
        for i in range(10):
            set_up.setUp(self)
            driver = self.driver
            driver.get(self.base_url + "/")
            login.login(driver)
            driver.find_element_by_link_text("Wi-Fi").click()
            driver.find_element_by_link_text("WLAN Settings").click()

            driver.switch_to_frame("mainifr")


            box2 = driver.find_element_by_id("wlanEnabled")
            box2.click()
            time.sleep(2)


            # btn = driver.find_element_by_link_text("Submit")
            btn = driver.find_element_by_class_name("button_center")
            #btn.submit()
            btn.click()
            time.sleep(3)
            # 获取网页上的警告信息
            alert = driver.switch_to_alert()
            # 接收警告信息
            alert.accept()


            self.driver.quit()
            print"this is time %s "%(i+1)

if __name__ == "__main__":
    unittest.main()