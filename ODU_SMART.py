#coding=utf-8

import unittest, login,quit,set_up

from selenium import webdriver
import login,set_up,quit
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class test_ODU(unittest.TestCase):

     def test_login(self):
         u"""ODU登录"""
         set_up.setUp(self)
         driver = self.driver

         driver.get(self.base_url + "/")
         login.login(driver)
         driver.quit()

      #ODU连接方式
     def test_method(self):
          u"""LTE连接方式"""
          set_up.setUp(self)
          driver = self.driver
          driver.get(self.base_url + "/")
          login.login(driver)

          driver.find_element_by_link_text("Network").click()
          driver.find_element_by_link_text("Scan Mode").click()
          driver.switch_to_frame("mainifr")

          con_method = driver.find_element_by_id("scan_mode")
          con_method.find_element_by_xpath("//option[@value='freqpreferred']").click()

          sub = driver.find_element_by_id("SubmitBtn")
          sub.click()
          time.sleep(3)

     # 获取网页上的警告信息
          alert = driver.switch_to_alert()
     # 接收警告信息
          alert.accept()
          time.sleep(2)

          con_method = driver.find_element_by_id("scan_mode")
          con_method.find_element_by_xpath("//option[@value='celllock']").click()

          sub = driver.find_element_by_id("SubmitBtn")
          sub.click()
          time.sleep(3)
     # 获取网页上的警告信息
          alert = driver.switch_to_alert()
     # 接收警告信息
          alert.accept()
          time.sleep(2)

          con_method = driver.find_element_by_id("scan_mode")
          con_method.find_element_by_xpath("//option[@value='fullband']").click()

          sub = driver.find_element_by_id("SubmitBtn")
          sub.click()
          time.sleep(3)
     # 获取网页上的警告信息
          alert = driver.switch_to_alert()
     # 接收警告信息
          alert.accept()
          time.sleep(2)
          driver.quit()

     def test_sim_lock(self):
         u"""SIM LOCK"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)

         driver.find_element_by_link_text("Network").click()
         driver.find_element_by_link_text("SIM Lock").click()
         driver.switch_to_frame("mainifr")

         mcc = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[3]/div[1]/div[2]/input")
         mcc.clear()
         mcc.send_keys("460")

         mnc = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[3]/div[2]/div[2]/input")
         mnc.clear()
         mnc.send_keys("11")
         time.sleep(3)

         btn = driver.find_element_by_id("submit")
         btn.click()
         time.sleep(3)

         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         # 接收警告信息
         alert.accept()
         time.sleep(2)
         driver.quit()

     def test_login(self):
         u"""开启防火墙"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("Security").click()
         driver.find_element_by_link_text("Firewall Setting").click()
         driver.switch_to_frame("mainifr")

         box = driver.find_element_by_id("enable")
         box.click()

         sub = driver.find_element_by_id("submitBtn")
         sub.click()
         time.sleep(2)
         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         # 接收警告信息
         alert.accept()

         driver.refresh
         time.sleep(2)

         driver.quit()

     def test_APN(self):
         U"""开启4个APN"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("Network").click()
         driver.find_element_by_link_text("APN Management").click()
         driver.switch_to_frame("mainifr")

         APN_NUM = driver.find_element_by_id("select")
         APN_NUM.find_element_by_xpath("//option[@value='2']").click()
         box2 = driver.find_element_by_id("enable")
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

         driver.quit()

     def test_VPN(self):
         u"""开启VPN"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("VPN").click()

         driver.switch_to_frame("mainifr")

         # box=driver.find_element_by_xpath("/html/body/form/div/div[2]/div[2]/div[2]/input")
         box = driver.find_element_by_id("vpnEnable")
         box.click()
         time.sleep(2)
         vpn_ser = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[1]/div[2]/input")

         vpn_ser.clear()
         vpn_ser.send_keys("zmtel.com")
         time.sleep(2)
         username = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[2]/div[2]/input")
         username.clear()
         username.send_keys("yuanshen")
         time.sleep(2)
         password = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[4]/div[3]/div[2]/input")
         password.clear()
         password.send_keys("TDtech994106")
         time.sleep(2)

         sub = driver.find_element_by_id("SubmitBtn")
         sub.click()

         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         time.sleep(2)
         # 接收警告信息
         alert.accept()

         driver.quit()

     def test_PIN(self):
         u"""PIN码锁住/解锁"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("Network").click()
         driver.find_element_by_link_text("PIN Management").click()
         driver.switch_to_frame("mainifr")

         enable = driver.find_element_by_id("enable_radio")
         enable.click()
         time.sleep(2)

         pin = driver.find_element_by_id("pinpwd")
         pin.send_keys("1234")

         sub = driver.find_element_by_id("SubmitBtn")
         sub.click()
         time.sleep(3)
         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         # 接收警告信息
         alert.accept()
         time.sleep(2)

         disable = driver.find_element_by_id("disable_radio")
         disable.click()
         time.sleep(2)

         pin = driver.find_element_by_id("pinpwd")
         pin.send_keys("1234")

         sub = driver.find_element_by_id("SubmitBtn")
         sub.click()
         time.sleep(3)
         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         # 接收警告信息
         alert.accept()
         time.sleep(2)

         driver.quit()

     def test_time(self):
         u"""同步时间"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("System").click()
         driver.find_element_by_link_text("Date & Time").click()
         driver.switch_to_frame("mainifr")

         enable = driver.find_element_by_name("timeSetupMode")
         enable.click()
         time.sleep(2)

         btnSyn = driver.find_element_by_id("btnSynLocal")
         btnSyn.click()

         sub = driver.find_element_by_id("submitBtn")
         sub.click()
         time.sleep(3)
         # 获取网页上的警告信息
         alert = driver.switch_to_alert()
         # 接收警告信息
         alert.accept()
         time.sleep(2)

         driver.quit()

     def test_ping(self):
         u"""ping 百度"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("System").click()
         driver.find_element_by_link_text("Diagnostics").click()
         driver.switch_to_frame("mainifr")

         ip = driver.find_element_by_id("id_pingTarget")
         ip.clear()
         ip.send_keys("www.baidu.com")
         time.sleep(2)

         subbtn = driver.find_element_by_id("id_btnPingExcute")

         # print subbtn.text
         subbtn.click()

         detail = driver.find_element_by_id("id_pingDetail")
         detail.click()
         txt = detail.get_attribute("value")
         time.sleep(3)
         print txt
         time.sleep(3)

         driver.quit()

     def test_http(self):
         u"""网页设置"""
         set_up.setUp(self)
         driver = self.driver
         driver.get(self.base_url + "/")
         login.login(driver)
         driver.find_element_by_link_text("System").click()
         driver.find_element_by_link_text("WEB Setting").click()
         driver.switch_to_frame("mainifr")

         https = driver.find_element_by_id("https_wan")
         https.click()
         time.sleep(2)

         fresh = driver.find_element_by_id("refresh")
         fresh.clear()
         fresh.send_keys("5")
         time.sleep(2)

         ip = driver.find_element_by_id("session")
         ip.clear()
         ip.send_keys("1440")
         time.sleep(2)

         language = driver.find_element_by_id("language")
         #language.find_element_by_xpath("//option[@value='zh']").click()

         # print subbtn.text
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