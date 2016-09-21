#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import userinfo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

us,pw = userinfo.fun()

def login(self):
    driver = self.driver
    driver.find_element_by_id("username").send_keys(us)
    driver.find_element_by_id("userpassword").send_keys(pw)
    driver.find_element_by_class_name("login_button").click()