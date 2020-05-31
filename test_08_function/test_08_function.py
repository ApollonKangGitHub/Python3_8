# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月30日21:50:32
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :函数测试
#    FileName       :test_08_function.py
#***********************************************************************

#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
global g_title_test_count
global g_title_str
g_title_test_count = 0
g_title_str = "--------------------------------------------------------"

#num = 0是给形参指定默认值
def title_test(num = 0, test_title_str = "default function"):
	global g_title_test_count
	g_title_test_count += 1
	if num > 0:
		g_title_test_count = num
	print("\n" + g_title_str)
	print(str(g_title_test_count) + "、" + test_title_str.lower() + ":")
	print(g_title_str)
#-----------------------------------------------------------------------
#可以使用形参默认值，也可以直接指定形参的值（关键字形参），而不需要考虑顺序
#但是如果要是使用默认形参，必须确保默认形参的相对位置是正确的
#-----------------------------------------------------------------------
title_test()
title_test(8)
title_test(10, "test function")
title_test(num = 1, test_title_str = "test function")
title_test(test_title_str = "test function", num = -1)
#title_test("error function")

#-----------------------------------------------------------------------
#带返回值的函数
#-----------------------------------------------------------------------
def my_upper(string):
	return str(string).upper()
def my_lower(string):
	return str(string).lower()

print(my_upper(1234))
print(my_lower("abcde"))
print(my_upper("axcsd"))
print(my_lower("xxcds"))

#-----------------------------------------------------------------------
#默认形参的作用
#-----------------------------------------------------------------------
title_test(1, 'default parameter test')
def get_all_name(pre_name, last_name, mid_name=''):
	full_name = ''
	if mid_name:
		full_name = pre_name + '' + mid_name + '' + last_name
	else:
		full_name = pre_name + '' + last_name
	return full_name.title()

#返回值为字典
def get_person_info(pre_name, last_name, mid_name='', age=0):
	person = {
		"first_name":pre_name,
		"mid_name":mid_name,
	}
	if mid_name:
		person["last_name"] = last_name
	if age:
		person["age"] = age
	return person
	
print(get_all_name('王', '麻'))
print(get_all_name('王', '子', '麻'))	
print(get_person_info('王','麻',age=6))
print(get_person_info('王','子','麻', 23))

#-----------------------------------------------------------------------
#只读的参数列表测试，一般不建议传递副本，拷贝太耗时间，尤其对于大的列表
#-----------------------------------------------------------------------
title_test(test_title_str = 'read only list parameter test')
def print_list(para_list = []):
	list_str = ''
	if para_list:
		for index in range(0,len(para_list)):
			para_list[index] = 'a'
			list_str += para_list[index]
	print(list_str)

test_list1 = list("ABCDEFG")
test_list2 = list("ABCDEFG")
print_list(test_list1)
print(test_list1)
print_list(test_list2[:])
print(test_list2)

#-----------------------------------------------------------------------
#可变个数参数列表
#通过"*para_list"来实现，通过元组将可变参数列表封装并传递
#判断参数类型的内置函数：
#    isinstance(<value>, <type>)
#    type(<value>, <type>)
#    如:isinstance(10,int)判断10是否是int的整数，返回True
#    isinstance和type的区别在：
#    1、type是用来获取类型的，isinstance是用来判断类型的；
#    2、type() 不会认为子类是一种父类类型，不考虑继承关系，
#    而isinstance() 会认为子类是一种父类类型，考虑继承关系
#-----------------------------------------------------------------------
title_test(test_title_str = 'variable parameter list test')
def variable_para_list(list_type, *para_list):
	print(str(list_type) + ' : ')
	list_str = ''
	for value in para_list:
		if isinstance(value, str) or isinstance(value, int):
			list_str += str(value) + ' '
		else:
			print('\t' + str(value))
	if isinstance(value, str) or isinstance(value, int):
		print('\t' + list_str)

name_list = {
	'赵'		:"我爱",
	'钱'		:"我喜欢",
	'孙'		:"我讨厌",
}

info_list = {
	'数字'	:[1,2,3],
	'动物'	:['狗', '猫'],
	'学科'	:['英语', '政治'],
}
variable_para_list("str and int", "I love numer", 1, 2, 3)
variable_para_list("dictionaries", name_list, info_list)

#-----------------------------------------------------------------------
#参数类型不定的可变参数列表使用（用于字典）
#-----------------------------------------------------------------------
title_test(test_title_str = 'dictionary variable parameter list test')
def create_person(name, **para):
	person = {}
	if not isinstance(name, str):
		return person
	person["名字"] = name;
	for key, value in para.items():
		person[key] = value
	return person

def print_person(person = {}):
	if not isinstance(person, dict):
		print("无效的person" + str(person))
		return False
	for attr, value in person.items():
		print(str(attr) + " \t: " + str(value))
		
	return True
		
person_kang = create_person("王麻子", 年龄='24', 家乡='陕西·咸阳', 工作地='四川·成都')
print_person(person_kang)

#-----------------------------------------------------------------------
#模块导入、函数导入：
#    有一个文件：module_name.py
#    "import module_name" 即可导入该文件（模块）
#    "module_name.function()"来使用其中的函数
#    要是指向导入部分函数，则可以使用:
#    "from import module_name fun1, fun2, fun3, ..."
#    按如上方式导入个别函数，则可以直接使用函数名，不需要"module_name." 
#    若导入个别函数与本文件函数名冲突，
#    可在导入的时候用as关键字为该导入的函数指定别名，
#    如果不想用"module_name."调用函数，但是所有函数都要导出，
#    不可能一个个导出，则使用:"import module_name *"来导出所有函数
#    同样可以给模块指定别名，以更合适的名字来操作模块中的函数
#    指定别名后，原名字不能直接使用，除非重新导入原名字
#    规范：import尽量放在文件开头（不包括开头注释等）
#-----------------------------------------------------------------------
import test_08_book_management as fun_test
from time import sleep as fun_sleep

title_test(test_title_str = 'bookstore system test')
print("进入图书管理系统，请稍等...")
print("--------------------------------------------------------")
fun_sleep(2)

fun_test.book_main("王麻子")

import time 
print("退出图书管理系统，请稍等...")
time.sleep(2)
