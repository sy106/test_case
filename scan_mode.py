#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_method(unittest.TestCase):
    def test_login(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_id("Network").click()
        driver.find_element_by_id("a4").click()
        driver.switch_to_frame("mainifr")

        con_method=driver.find_element_by_id("scan_mode")
        con_method.find_element_by_xpath("//option[@value='freqpreferred']").click()

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)

        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)

        con_method = driver.find_element_by_id("scan_mode")
        con_method.find_element_by_xpath("//option[@value='celllock']").click()

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)

        con_method = driver.find_element_by_id("scan_mode")
        con_method.find_element_by_xpath("//option[@value='fullband']").click()

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)



        driver.quit()

if __name__ == "__main__":
    unittest.main()