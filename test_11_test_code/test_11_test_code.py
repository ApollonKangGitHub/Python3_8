# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年6月1日19:52:27
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :测试代码与测试类、测试对象
#    FileName       :test_11_test_code.py
#***********************************************************************

import unittest
from book_management import \
    book_find_from_store_set_with_attr as book_find

#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
global g_title_test_count
global g_title_st
g_title_test_count = 0
g_title_str = "--------------------------------------------------------"

def title_test(test_title_str = "default test"):
    global g_title_test_count
    g_title_test_count += 1
    print("\n" + g_title_str)
    print(str(g_title_test_count) + "、" + test_title_str.lower() + ":")
    print(g_title_str)

#-----------------------------------------------------------------------
#图书管理系统的简单测试用例
#核实结果为 a == b    :assertEqual(a,b)
#核实结果为 a != b    :assertNotEqual(a,b)
#核实结果为 True    :assertTrue(a)
#核实结果为 False    :assertFalse(a)
#核实item在list中    :assertIn(item,list)
#核实item不再list中    :assertNotIn(item,list)
#每一个函数都可以创建多个用例，避免程序修改后需要手动一个个去测试
#但是这种测试方法是白盒测试，针对函数/类，可以直接访问程序的数据
#-----------------------------------------------------------------------
class BookManagementTestCase(unittest.TestCase):
    '''setUp()提前创建测试，然后在测试用例中直接检查结果'''
    def setUp(self):
        self.ret_find_ok =  book_find(attr='出版社', value='三秦出版社')
        self.ret_find_err = book_find(attr='作者ERR', value='老舍')
        
    '''测试book_management.py'''
    
    def test_find_book(self):
        ret = book_find(attr='出版社', value='中华书局')
        self.assertEqual(ret, True)
    
    def test_find_book_2(self):
        ret = book_find(attr='作者', value='路遥')
        self.assertNotEqual(ret, False)
        
    def test_find_book_err_false(self):
        ret = book_find(attr='类别')
        self.assertFalse(ret)

    def test_find_book_err_true(self):
        ret = book_find(attr='类别')
        self.assertTrue(ret) 
        
    def test_setup_ret_1(self):
        self.assertTrue(self.ret_find_ok) 
    def test_setup_ret_2(self):
        self.assertTrue(self.ret_find_err)  

#测试父类在程序退出后开始测试               
unittest.main()
