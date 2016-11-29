#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import login,set_up,quit,os
import unittest, time,datetime


class radio_on_off(unittest.TestCase):

    def test_login(self):
        u"""升级版本"""

        # TIME = datetime.datetime.now()
        set_up.setUp(self)
        driver = self.driver
        driver.get(self.base_url + "/")
        login.login(driver)

        driver.find_element_by_link_text("System").click()
        driver.find_element_by_link_text("Maintenance").click()

        driver.switch_to_frame("mainifr")
        # driver.find_element_by_link_text("OFF").click()
        driver.find_element_by_id("btnRadio").click()
        # if i%2==0:
        #     print'按off'
        # else:
        #     print'按on'
        driver.refresh
        # driver.switch_to_frame("mainifr")
        driver.switch_to_default_content()
        driver.find_element_by_link_text("Network").click()
        driver.find_element_by_link_text("LTE Settings").click()
        driver.refresh
        driver.switch_to_frame("mainifr")
        time.sleep(10)
        driver.refresh
        time.sleep(10)
        driver.refresh
        time.sleep(5)
        text1 = driver.find_element_by_id("currStatus").text
        # driver.refresh
        # time.sleep(10)
        # driver.refresh
        # text1 = driver.find_element_by_class_name('content_item_right').text
        # print text1
        if text1 =='No Service':
            # print '第%s次连接状态为：No Service!'%(i+1)
            print "turn_off !now the status is：No Service!"
            # driver.find_element_by_link_text("System").click()
            # driver.find_element_by_link_text("Maintenance").click()
            #
            # # driver.switch_to_frame("mainifr")
            # driver.switch_to_default_content()
            # # driver.find_element_by_link_text("ON").click()
            # driver.find_element_by_id("btnRadio").click()
            # driver.refresh
            # time.sleep(5)
            # driver.find_element_by_link_text("Network").click()
            # driver.find_element_by_link_text("LTE Settings").click()
            # text2 = driver.find_element_by_id("currStatus").text
            # if text2 =='Connected':
            #     print'连接状态为：Connected!'
            #     driver.quit()
        elif text1 == 'Connected':
            # print'第%s次连接状态为：Connected!'%(i+1)
            print "turn_on!now the status is：Connected!"
        else:
            # print '第%s次连接状态为状态为：>>%s'%(i+1,text1)
            print'abnormal !now the status is：>>%s'%text1
        driver.quit()


if __name__ == "__main__":
    unittest.main()



