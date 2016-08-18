#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有case,这里用的是python，
#所在py 文件运行一次后会生成一个pyc 的副本
caselist=os.listdir('D:\\Python27\\test_case')
for a in caselist:
    s=a.split('.')[1] #选取后缀名为py 的文件
    if s=='py':
#此处执行dos 命令并将结果保存到log.txt
        os.system('D:\\Python27\\test_case\\%s 1>>log.txt 2>&1'%a)