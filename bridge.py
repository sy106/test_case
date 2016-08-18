#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test2_bridge(unittest.TestCase):
    def test_login(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_id("a1").click()
        driver.find_element_by_id("a2").click()
        driver.switch_to_frame("mainifr")
        mode=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[2]/div[1]/div[2]/select")
        mode.find_element_by_xpath("//option[@value='bridge']").click()
        time.sleep(3)
        sub=driver.find_element_by_id("submit")
        sub.click()
        time.sleep(2)

        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
if __name__ == "__main__":
    unittest.main()