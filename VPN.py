#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os


class test_vpn(unittest.TestCase):
    def test_VPN(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_link_tex("VPN").click()

        driver.switch_to_frame("mainifr")

        #box=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[2]/div[2]/input")
        box=driver.find_element_by_id("vpnEnable")
        box.click()
        time.sleep(2)
        vpn_ser=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[1]/div[2]/input")

        vpn_ser.clear()
        vpn_ser.send_keys("zmtel.com")
        time.sleep(2)
        username=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[2]/div[2]/input")
        username.clear()
        username.send_keys("yuanshen")
        time.sleep(2)
        password=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[3]/div[2]/input")
        password.clear()
        password.send_keys("TDtech994106")
        time.sleep(2)

        sub=driver.find_element_by_id("SubmitBtn")
        sub.click()

        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        time.sleep(2)
        # 接收警告信息
        alert.accept()

if __name__ == "__main__":
    unittest.main()