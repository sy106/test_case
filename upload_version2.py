#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

from selenium import webdriver
import login2,login3,set_up
import unittest, time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_up_version(unittest.TestCase):
    def test_login(self):
        for i in range(100):
            set_up.setUp(self)
            driver = self.driver
            driver.get(self.base_url)
            login2.login(self)
            login3.Btn(self)
            driver.switch_to_frame("top")

            driver.find_element_by_link_text("Advance").click()

            driver.refresh
            time.sleep(2)

            driver.switch_to_default_content()
            driver.switch_to_frame("main")

            driver.find_element_by_xpath("/html/body/div/div/div/ul/li[4]/span").click()

            driver.find_element_by_link_text("Device Information").click()

            driver.switch_to_frame("ifm")

            test= driver.find_element_by_xpath("/html/body/form/div/div/ul/div/table/tbody/tr[6]/td[2]").text
            if test == "4.1.1.1 [25754]" :
                driver.refresh
                time.sleep(2)
                driver.switch_to_default_content()
                driver.switch_to_frame("main")
                driver.find_element_by_link_text("Firmware Upgrade").click()
                driver.switch_to_frame("ifm")
                driver.find_element_by_xpath("/html/body/form/div/div[2]/ul/li[1]/div/ul[2]/li[2]/input").click()
                os.system("C:\\Users\shenyuan\Documents\upfile1.exe")
            else:
                driver.refresh
                time.sleep(2)
                driver.switch_to_default_content()
                driver.switch_to_frame("main")
                driver.find_element_by_link_text("Firmware Upgrade").click()
                driver.switch_to_frame("ifm")
                driver.find_element_by_xpath("/html/body/form/div/div[2]/ul/li[1]/div/ul[2]/li[2]/input").click()
                os.system("C:\\Users\shenyuan\Documents\upfile2.exe")


            time.sleep(2)

            sub = driver.find_element_by_name("isSubmit")
            sub.click()
            time.sleep(450)

        # time.sleep(5)

            driver.quit()


if __name__ == "__main__":
    unittest.main()
