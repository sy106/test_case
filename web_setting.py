#coding=utf-8
from selenium import webdriver

import login,set_up,quit
import unittest, time,webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class http(unittest.TestCase):
    def test_http(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_id("a14").click()
        driver.find_element_by_id("a22").click()
        driver.switch_to_frame("mainifr")

        https = driver.find_element_by_id("https_wan")
        https.click()
        time.sleep(2)

        fresh=driver.find_element_by_id("refresh")
        fresh.clear()
        fresh.send_keys("5")
        time.sleep(2)


        ip=driver.find_element_by_id("session")
        ip.clear()
        ip.send_keys("1440")
        time.sleep(2)

        language=driver.find_element_by_id("language")
        language.find_element_by_xpath("//option[@value='zh']").click()

        #print subbtn.text
        subbtn = driver.find_element_by_id("submit")
        subbtn.click()

        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)

        driver.quit()

if __name__ == "__main__":
    unittest.main()
