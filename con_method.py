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
        driver.find_element_by_link_text("Network").click()
        driver.find_element_by_link_text("Scan Mode").click()
        driver.switch_to_frame("mainifr")

        con_method=driver.find_element_by_id("method")
        con_method.find_element_by_xpath("//option[@value='0']").click()

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)

        time.sleep(5)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)

        con = driver.find_element_by_id("manualBtn")
        con.click()
        time.sleep(5)

        con_method = driver.find_element_by_id("method")
        con_method.find_element_by_xpath("//option[@value='1']").click()

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)

        driver.quit()

if __name__ == "__main__":
    unittest.main()