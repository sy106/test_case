#coding=UTF-8
from selenium import webdriver
import login,set_up,quit,os
import unittest, time,datetime
from selenium.webdriver.common.keys import Keys


FILE_DIR = 'test.txt'
class test_up_version(unittest.TestCase):

    def test_login(self):
        u"""升级版本"""
        for i in range(100):
            # TIME = datetime.datetime.now()
            set_up.setUp(self)
            driver = self.driver
            driver.get(self.base_url + "/")
            login.login(driver)

            driver.find_element_by_link_text("System").click()
            driver.find_element_by_link_text("Version Manager").click()


            #os.system("D:\\Python27\\test_case\upfile.exe")
            """
            filePath='F:\\version\MT-23425-1.2.3-R2-Smart-20160721.tgz'
            upload=driver.find_element_by_xpath("//input[@type='file']")
            upload.send_keys(filePath)
            """
            driver.switch_to_frame("mainifr")
            test = driver.find_element_by_id("fwinfo").text
            # test = driver.find_element_by_class_name("content_item_right").text
            print "test",test
            with open(FILE_DIR, 'a+') as f:
                f.write(test)
                f.write('\n')
            if test == "IDU-26392-2.0.3-R9-GP-Umniah":
                driver.refresh
                time.sleep(2)
                # driver.switch_to_frame("mainifr")
                # brow=driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[4]/div[2]/div[2]/input")
                brow = driver.find_element_by_id("file")
                brow.click()

                os.system("C:\\Users\shenyuan\Documents\upfile2.exe")
                print str(datetime.datetime.now())+'升级到R9-f'
                with open(FILE_DIR, 'a+') as f:
                    f.write(str(datetime.datetime.now())+'升级到R9-f')
                    f.write('\n')
            else:
                driver.refresh
                time.sleep(2)
                # driver.switch_to_frame("mainifr")
                # brow=driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[4]/div[2]/div[2]/input")
                brow = driver.find_element_by_id("file")
                brow.click()

                os.system("C:\\Users\shenyuan\Documents\upfile.exe")
                print str(datetime.datetime.now())+'升级到R9'
                with open(FILE_DIR, 'a+') as f:
                    f.write(str(datetime.datetime.now())+'升级到R9')
                    f.write('\n')
            time.sleep(2)

            sub = driver.find_element_by_id("btnUlVersion")
            sub.click()
            time.sleep(340)

            #time.sleep(5)

            driver.quit()
            j = i + 1
            driver.refresh
            print str(datetime.datetime.now())+'这是升级第%s次成功'%j
            j=i+1
            with open(FILE_DIR, 'a+') as f:
                f.write(str(datetime.datetime.now())+'这是升级第%s次成功'%j)
                f.write('\n')



if __name__ == "__main__":
    unittest.main()



