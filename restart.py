#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test2_restart(unittest.TestCase):
    def test_login(self):
        for i in range(270):
            set_up.setUp(self)
            driver = self.driver
            driver.get(self.base_url + "/")
            login.login(driver)
            driver.find_element_by_link_text("System").click()
            driver.find_element_by_link_text("Maintenance").click()
            driver.switch_to_frame("mainifr")

            reboot=driver.find_element_by_id("btnReboot")

            reboot.click()


            # 获取网页上的警告信息
            alert = driver.switch_to_alert()
            # 接收警告信息
            alert.accept()

            time.sleep(75)
            driver.quit()
if __name__ == "__main__":
    unittest.main()