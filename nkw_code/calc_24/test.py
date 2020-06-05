# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年6月5日21:08:48
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :测试24点运算
#    FileName       :test.py
#***********************************************************************

import unittest
from calc_24 import valid
import calc_24

class test24(unittest.TestCase):
    def test_find_24(self):
        with open("24_success.txt", 'w+') as obj_ok:
            with open("24_fail.txt", 'w+') as obj_err:
                for v1 in valid.keys():
                    for v2 in valid.keys():
                        for v3 in valid.keys():
                            for v4 in valid.keys():
                                ret = calc_24.main(str(v1) + ' ' + str(v2) + ' ' + str(v3) + ' ' + str(v4))
                                ret += '\n'
                                if '=' in ret:
                                    obj_ok.write(ret);
                                else:
                                    obj_err.write(ret);
#测试父类在程序退出后开始测试               
unittest.main()
