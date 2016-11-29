#coding=utf-8
#___author____ = 'yuanshen'

import unittest
#这里需要导入测试文件
import firewall,ODU_login,pin,scan_mode,sim_lock,ODU_SMART,reset_to_factory,upload_version_um,radio_um

import os
import HTMLTestRunner,restart,ping
testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(upload_version.test_up_version))
# testunit.addTest(unittest.makeSuite(reset_to_factory.test_factory))
for i in range(10):
      testunit.addTest(unittest.makeSuite(radio_um.radio_on_off))
      testunit.addTest(unittest.makeSuite(ping.ping))

"""
testunit.addTest(unittest.makeSuite(ODU_login.test_ODU_login))
testunit.addTest(unittest.makeSuite(firewall.test_firewall))
testunit.addTest(unittest.makeSuite(pin.test_pin))
testunit.addTest(unittest.makeSuite(scan_mode.test_method))
testunit.addTest(unittest.makeSuite(sim_lock.test_sim_lock))
"""
"""
caselist=os.listdir('D:\\selenium_use_case\\test_case')
for a in caselist:
    s=a.split('.')[1] #选取后缀名为py 的文件
    if s=='py':
#此处执行dos 命令并将结果保存到log.txt
        os.system('D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)
"""
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#定义个报告存放路径，支持相对路径。
filename = 'D:\\Python27\\report\\result2.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
      stream=fp,
      title=u'ODU测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)