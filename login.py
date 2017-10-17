
import userinfo

us,pw = userinfo.fun()

def login(self):

    self.find_element_by_name("username").send_keys(us)
    self.find_element_by_name("password").send_keys(pw)
    self.find_element_by_id("button").click()
    # self.find_element_by_link_text("Login").click()
    # self.find_element_by_name("submit").click()

"""
def login(self):
    self.find_element_by_id("ioc_login").click()
    self.find_element_by_class_name("theme-popover").find_element_by_name("username").send_keys(us)
    self.find_element_by_class_name("theme-popover").find_element_by_name("password").send_keys(pw)
    self.find_element_by_name("submit").click()
"""


