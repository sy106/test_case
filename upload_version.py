#coding=UTF-8
from selenium import webdriver
import login,set_up,quit,os
import unittest, time
from selenium.webdriver.common.keys import Keys



class test_up_version(unittest.TestCase):

    def test_login(self):
        u"""升级版本"""
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)

        driver.find_element_by_link_text("System").click()
        driver.find_element_by_link_text("Version Manager").click()

        driver.switch_to_frame("mainifr")
        #brow=driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[4]/div[2]/div[2]/input")
        brow=driver.find_element_by_id("file")
        brow.click()

        os.system("C:\\Users\shenyuan\Documents\upfile.exe")
        #os.system("D:\\Python27\\test_case\upfile.exe")
        """
        filePath='F:\\version\MT-23425-1.2.3-R2-Smart-20160721.tgz'
        upload=driver.find_element_by_xpath("//input[@type='file']")
        upload.send_keys(filePath)
        """

        
        time.sleep(2)

        sub = driver.find_element_by_id("btnUlVersion")
        sub.click()
        time.sleep(240)

        #time.sleep(5)

        driver.quit()



if __name__ == "__main__":
    unittest.main()



