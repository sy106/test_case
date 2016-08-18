#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Data_time(unittest.TestCase):
    def test_time(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_id("a24").click()
        driver.find_element_by_id("a29").click()
        driver.switch_to_frame("mainifr")

        enable=driver.find_element_by_name("timeSetupMode")
        enable.click()
        time.sleep(2)

        btnSyn=driver.find_element_by_id("btnSynLocal")
        btnSyn.click()

        sub = driver.find_element_by_id("submitBtn")
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
