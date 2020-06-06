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
#全排列函数
from itertools import permutations
#全组合函数
from itertools import combinations

class test24(unittest.TestCase):
	#所有值可复用（num^n）
    def test_all_24(self):
        with open("24_success_all.txt", 'w+') as obj_ok:
            with open("24_fail_all.txt", 'w+') as obj_err:
                for v1 in valid.keys():
                    for v2 in valid.keys():
                        for v3 in valid.keys():
                            for v4 in valid.keys():
                                ret = calc_24.main(v1 + ' ' + v2 + ' ' + v3 + ' ' + v4)
                                ret += '\n'
                                if '=' in ret:
                                    obj_ok.write(ret);
                                else:
                                    obj_err.write(ret);
                                    
	#所有值只能用一次（全排列）
    def test_permutations_24(self):
        with open("24_success_permutations.txt", 'w+') as obj_ok:
            with open("24_fail_permutations.txt", 'w+') as obj_err:
                for v1,v2,v3,v4 in permutations(valid.keys(), 4):
                    #print(v1,v2,v3,v4)
                    ret = calc_24.main(v1 + ' ' + v2 + ' ' + v3 + ' ' + v4)
                    ret += '\n'
                    if '=' in ret:
                        obj_ok.write(ret);
                    else:
                        obj_err.write(ret);
                        
	#所有值只能用一次（全组合）
    def test_combinations_24(self):
        with open("24_success_combinations.txt", 'w+') as obj_ok:
            with open("24_fail_combinations.txt", 'w+') as obj_err:
                for v1,v2,v3,v4 in combinations(valid.keys(), 4):
                    #print(v1,v2,v3,v4)
                    ret = calc_24.main(v1 + ' ' + v2 + ' ' + v3 + ' ' + v4)
                    ret += '\n'
                    if '=' in ret:
                        obj_ok.write(ret);
                    else:
                        obj_err.write(ret);                       
#测试父类在程序退出后开始测试               
unittest.main()
