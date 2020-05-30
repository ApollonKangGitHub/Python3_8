# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月30日10:33:46
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python的if条件语句测试
#    FileName       :test_05_if_elif_else.py
#***********************************************************************

#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
global g_title_test_count
global g_title_str
g_title_test_count = 0
g_title_str = "--------------------------------------------------------"
def title_test(test_title_str):
	global g_title_test_count
	g_title_test_count += 1
	print("\n" + g_title_str)
	print(str(g_title_test_count) + "、" + test_title_str.lower() + ":")
	print(g_title_str)


#-----------------------------------------------------------------------
#条件测试语句格式(每个条件语句的核心都是一条结果为True/Flase的表达式)：
#    1、if xxx:
#    2、if xxx is yyy:
#    3、if xxx elif yyy else
#    4、if xxx == yyy
#Notes：
#    1、elif在一个if后面可以多次使用
#    2、python可以允许if ... elif ... 不包含else分支
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#if ... elif ... else ... 测试
#-----------------------------------------------------------------------
str_1 = "AABB12345"
str_2 = "AAbb12345"
str_3 = "aabb12345"

title_test("test \"if ... elif ... else ...\" and \"==\"")
if str_1 == str_2:
	print("str_1:" + str_1 + " equals str_2:" + str_2)
elif str_1 == str_3:
	print("str_1:" + str_1 + " equals str_3:" + str_3)
else:
	print("str_1:" + str_1 
		+ " no equals str_2:" + str_2 
		+ " and not equals str_3:" + str_3)
if (str_1.upper() == str_2.upper()) \
	and (str_1.upper() == str_3.upper()):
	print("str_1.upper():" + str_1.upper()
		+ " equals str_2.upper():" + str_2.upper() 
		+ " and equals str_3.upper():" + str_3.upper())

#-----------------------------------------------------------------------
#is 、 and 、 not ... is ...测试
#关于is和==的用法区别
#"=="表示对象等，即对象value相等
#"is"表示对象是，即对象id相同
#注：Python中对象三个基本要素，分别是：
#    id(身份标识)、type(数据类型)和value(值)
#-----------------------------------------------------------------------
list_1 = list(range(1,3,1))
list_2 = list_1
list_3 = list_1[:]	

title_test("test \"is\" 、\"and\" 、\"not xxx is yyy\"")
print("list\t value\t id")
print("list_1" + "\t " + str(list_1) + "\t " + str(hex(id(list_1))))
print("list_2" + "\t " + str(list_2) + "\t " + str(hex(id(list_2))))
print("list_3" + "\t " + str(list_3) + "\t " + str(hex(id(list_3))))

if list_1 is list_2:
	print("list_1:" + str(list_1) + " is list_2:" + str(list_2))
if not str_1 is list_3:
	print("list_1:" + str(list_1) + " not is list_3:" + str(list_3))
if list_1 is list_2 and not list_1 is list_3:
	print("list_1:" + str(list_1) 
		+ " is list_2:" + str(list_2) 
		+ " and not is list_3:" + str(list_3))

#-----------------------------------------------------------------------
#in 、not in 测试，要判断一个元素是否在列表中不用手动遍历列表
#直接使用in [list]或者not in [list]来判断即可
#-----------------------------------------------------------------------
data = list(range(1,10,2))
title_test("test \"in\"")
for index in range(0,20,4):
	if index in data:
		print(str(index) + " in list " + str(data))
	if index not in data:
		print(str(index) + " not in list " + str(data))

#-----------------------------------------------------------------------
#True、False 测试(找出100以内能被7整除的数)
#-----------------------------------------------------------------------
title_test("test \"Ture\" and \"Flase\"")
result_lower_100 = True
for index in range(0,1000,1):
	if (index % 7 == 0):
		print("choose index:" + str(index) 
			+ ", result_lower_100: " + str(result_lower_100))

	if (index >= 100):
		result_lower_100 = False
		print("over index:" + str(index)
			+ ", result_lower_100: " + str(result_lower_100))

	if not result_lower_100:
		break;
