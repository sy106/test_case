#coding=utf-8
from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class test_sim_lock(unittest.TestCase):
    def test_login(self):
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)
        driver.find_element_by_link_text("Network").click()
        driver.find_element_by_link_text("SIM Lock").click()

        driver.switch_to_frame("mainifr")

        #mcc=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[3]/div[1]/div[2]/input")
        mcc=driver.find_element_by_id("mcc")
        mcc.clear()
        mcc.send_keys("460")

        #mnc = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[3]/div[2]/div[2]/input")
        mnc = driver.find_element_by_id("mnc")
        mnc.clear()
        mnc.send_keys("11")
        time.sleep(3)
        #btn = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[3]/div[3]/label/span[1]/span/span/span")
        btn = driver.find_element_by_id("submit")

        #btn.submit()
        btn.click()
        time.sleep(3)
        # 获取网页上的警告信息
        alert = driver.switch_to_alert()
        # 接收警告信息
        alert.accept()


        self.driver.quit()

if __name__ == "__main__":
    unittest.main()