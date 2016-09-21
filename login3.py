#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
from selenium import webdriver

def Btn(self):
    driver = self.driver
    driver.find_element_by_class_name("login_button").click()
