#coding=UTF-8
from selenium import webdriver
import login,set_up,quit,os
import unittest, time,datetime
from selenium.webdriver.common.keys import Keys


FILE_DIR = 'test_FOTA.txt'
class test_FOAT(unittest.TestCase):

    def test_login(self):
        u"""升级版本"""
        for i in range(130):
            # TIME = datetime.datetime.now()
            set_up.setUp(self)
            driver = self.driver
            driver.get(self.base_url + "/")
            login.login(driver)
            driver.find_element_by_link_text("System").click()
            driver.find_element_by_link_text("Version Manager").click()

            driver.switch_to_frame("mainifr")
            test = driver.find_element_by_id("fwinfo").text
            print("now the version is :",test)
            if test == "CLARO_PER_WF820+_V1.0.0B09":

                driver.refresh
                time.sleep(2)
                driver.switch_to_default_content()
                driver.find_element_by_link_text("System").click()
                driver.find_element_by_link_text("FOTA").click()


                #os.system("D:\\Python27\\test_case\upfile.exe")

                driver.switch_to_frame("mainifr")
                # box = driver.find_element_by_id("enable")
                # box.click()
                url = driver.find_element_by_id("folder")
                url.clear()
                url.send_keys("http://172.16.34.120/IDU/Fota_CLARO_F.xml")
                time.sleep(2)
            else:
                driver.refresh
                time.sleep(2)
                driver.switch_to_default_content()
                driver.find_element_by_link_text("System").click()
                driver.find_element_by_link_text("FOTA").click()


                #os.system("D:\\Python27\\test_case\upfile.exe")

                driver.switch_to_frame("mainifr")
                # box = driver.find_element_by_id("enable")
                #
                # box.click()
                url = driver.find_element_by_id("folder")
                url.clear()
                url.send_keys("http://172.16.34.120/IDU/Fota_CLARO.xml")
                time.sleep(2)
            sub=driver.find_element_by_id("submit")
            sub.click()
            time.sleep(2)
            # 获取网页上的警告信息
            alert = driver.switch_to_alert()
            # 接收警告信息
            alert.accept()

            driver.switch_to_default_content()
            driver.find_element_by_link_text("System").click()
            driver.find_element_by_link_text("Version Manager").click()
            time.sleep(2)
            driver.switch_to_frame("mainifr")
            driver.find_element_by_id("check").click()
            time.sleep(2)
            # 获取网页上的警告信息
            alert = driver.switch_to_alert()
            # 接收警告信息
            alert.accept()

            time.sleep(330)

            driver.quit()
            j = i + 1
            driver.refresh
            print str(datetime.datetime.now())+'update success，this is %s times success'%j
            j=i+1
            # j = i + 1
            # driver.refresh
            # print str(datetime.datetime.now())+'update success，this is %s times success'%j
            # j=i+1
            # with open(FILE_DIR, 'a+') as f:
            #     f.write(str(datetime.datetime.now())+'update success，this is %s times success'%j)
            #     f.write('\n')



if __name__ == "__main__":
    unittest.main()



