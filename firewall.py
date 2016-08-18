#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_firewall(unittest.TestCase):
    def test_login(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)

        driver.find_element_by_link_text("Security").click()
        driver.find_element_by_link_text("Firewall Setting").click()

        driver.switch_to_frame("mainifr")

        box=driver.find_element_by_id("enable")
        box.click()

        sub=driver.find_element_by_id("submitBtn")
        sub.click()
        time.sleep(2)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()

        driver.refresh
        time.sleep(2)

        driver.find_element_by_link_text("Security").click()
        driver.find_element_by_link_text("MAC Filtering").click()
        driver.switch_to_frame("mainifr")
        box2 = driver.find_element_by_id("enable")
        box2.click()
        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(2)


        driver.quit()
if __name__ == "__main__":
    unittest.main()