#coding=utf-8
from selenium import webdriver

import login,set_up,quit
import unittest, time,webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ping(unittest.TestCase):
    def test_ping(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_link_text("System").click()
        driver.find_element_by_link_text("Diagnostics").click()
        driver.switch_to_frame("mainifr")

        ip=driver.find_element_by_id("id_pingTarget")
        ip.clear()
        ip.send_keys("www.baidu.com")
        time.sleep(2)

        subbtn=driver.find_element_by_id("id_btnPingExcute")
        # subbtn = driver.find_element_by_class_name("button_center")
        #print subbtn.text
        subbtn.click()

        detail = driver.find_element_by_id("id_pingDetail")
        detail.click()
        txt=detail.get_attribute("value")
        time.sleep(3)
        print txt
        time.sleep(3)

        driver.quit()

if __name__ == "__main__":
    unittest.main()
