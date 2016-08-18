#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_APN(unittest.TestCase):
    def test_APN(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_link_text("Network").click()
        driver.find_element_by_id("APN Management").click()
        driver.switch_to_frame("mainifr")

        APN_NUM=driver.find_element_by_id("select")
        APN_NUM.find_element_by_xpath("//option[@value='2']").click()
        box2=driver.find_element_by_id("enable")
        box2.click()
        time.sleep(2)

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(3)

        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)

        APN_NUM = driver.find_element_by_id("select")
        APN_NUM.find_element_by_xpath("/html/body/form/div/div[2]/div[1]/div[2]/div[2]/select/option[3]").click()
        box3 = driver.find_element_by_id("enable")
        box3.click()
        time.sleep(2)

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(2)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(5)

        APN_NUM = driver.find_element_by_id("select")
        APN_NUM.find_element_by_xpath("//option[@value='4']").click()
        box4 = driver.find_element_by_id("enable")
        box4.click()
        time.sleep(5)

        sub = driver.find_element_by_id("SubmitBtn")
        sub.click()
        time.sleep(5)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()
        time.sleep(2)


if __name__ == "__main__":
        unittest.main()
