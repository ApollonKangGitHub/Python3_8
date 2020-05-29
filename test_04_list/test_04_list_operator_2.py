# coding=gbk
#		Error: Non-UTF-8 code starting with '\xc4'报错解决，在文件开头加上
# 		"# coding=gbk" 或者 "coding:utf-8"即可
#
#-----------------------------------------------------------------------
#    Time           :2020年5月29日19:22:12
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python列表灵活操作学习测试
#    FileName       :test_04_list_operator_2.py
#-----------------------------------------------------------------------

Week = [
	["Monday   ",	"星期一",	"1st"],
	["Tuesday  ",	"星期二",	"2nd"],
	["Wednesday",	"星期三",	"3rd"],
	["Thursday ",	"星期四",	"4th"],
	["Friday   ",	"星期五",	"5th"],
	["Saturday ",	"星期六",	"6th"],
	["Sunday   ",	"星期日",	"7th"]
];
#-----------------------------------------------------------------------
#注意：
#1、定义全局变量不能直接赋值，直接的赋值操作被认为是定义局部变量
#2、在赋值时，如果变量在之前已经声明为全局，则认为是全局变量赋值
#3、函数内部和全局变量重名的变量会被认为是局部变量
#4、函数内部要要使用全局变量，需要声明global
#5、为了和局部变量区分开，避免以上问题，全局变量最好加上g_xxxx的标志
#-----------------------------------------------------------------------
global g_title_test_count
g_title_test_count = 0

#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
title_str = "----------------------------------------------------------"
def title_test(test_title_str):
	global g_title_test_count
	g_title_test_count += 1
	print("\n" + title_str)
	print(str(g_title_test_count) + "、" + test_title_str.title())
	print(title_str)

#-----------------------------------------------------------------------
#列表遍历
#1、for循环后多行第一行必须缩进以对应for
#2、其他行可以随时选择不再缩进
#3、第一个开始不再缩进的行，其后的行前一行没有for、while、if、def等则不能再缩进
#-----------------------------------------------------------------------
title_test("Two dimensional list traversal all test")
for day in Week:
	today = str(day) + ":";
	today += "\t today".title() + " is " + day[0].title();
	today += "\t 今天是" + day[1];
	today += "\t The " + day[2] + " day of the week!!";
	print(today)

title_test("Two dimensional list traversal last test")
for day in Week:
	today = str(day) + ":";
today += "\t today".title() + " is " + day[0].title();
today += "\t 今天是" + day[1];
today += "\t The " + day[2] + " day of the week!!";
print(today)


#-----------------------------------------------------------------------
#range()内置函数的使用
#通过以下两个例子可以知道，value从range()中取值，而不是作为for的index
#range(start,end<,length>),指定步长为length
#-----------------------------------------------------------------------
title_test("range number test1")
value_str = ""
count = 0
#将range list化，赋给一个列表
#以下两行等价于：
#for value2 in range(100,260):
range_list = list(range(100,260))
for value1 in range_list:
	count += 1
	value_str += str(value1) + " "
	value1 = 1000
	if ((count % 16) is 0):
		value_str += "\n"
print(value_str)

title_test("range number test2")
value_str = ""
count = 0
#将range list化，赋给一个列表，指定步长为2
range_list = list(range(100,260,2))
for value2 in range_list:
	count += 1
	value2 = 1000
	value_str += str(value2) + " "
	if (count % 16 == 0):
		value_str += "\n"
print(value_str)

#-----------------------------------------------------------------------
#min()、max()、sum()、range()等内置函数的灵活运用
#-----------------------------------------------------------------------
#利用range和运算符构造列表
title_test("range number test3")
squares = []
for value in range(1,20,2):
	squares.append(value**2)
	print(squares)
	print(sorted(squares, reverse=True))
	print("max num:" + str(min(squares)))
	print("min num:" + str(max(squares)))
	print("sum num:" + str(sum(squares)))
	print("----------------------------------------------")

#利用range()、for循环和运算逻辑的表示式直接构造列表
#该方式称为列表解析
title_test("range number test4")
squares = [(value ** value + value) for value in range(1,10,2)]
print(squares)

squares = list(range(1, 1000000+1))
print(str(min(squares)) + " + ... + " + str(max(squares)) + " = " + str(sum(squares)))

#-----------------------------------------------------------------------
#获取（切片）列表指定范围的元素
#-----------------------------------------------------------------------
title_test("section list number test")
section_list = list(range(1,100,3))
#指定范围对列表切片
print("section_list[pos1:pos2]")
print("\t" + str(section_list[4:10]))
print("\t" + str(section_list[(len(section_list) - 12):(len(section_list) - 5)]))
#默认从0到指定结束位置对列表切片
print("section_list[<start>:pos2]")
print("\t" + str(section_list[:10]))
print("\t" + str(section_list[:-15]))
#默认从指定开始位置到结束对列表切片
print("section_list[pos1:<end>]")
print("\t" + str(section_list[(len(section_list) - 12):]))
print("\t" + str(section_list[-15:]))

title_test("section list number traversal and operator")
for value in section_list[-10:]:
	print("\t" + str(value) + "^2=" + str(value**2))

#-----------------------------------------------------------------------
#列表拷贝（借助C++的‘浅拷贝’和‘深拷贝’的概念）
#-----------------------------------------------------------------------
#浅拷贝，两个list类似于同一个列表的不同别名
list_1 = [(value ** 2) for value in range(1,20,2)]
title_test("list copy test for light copy")
list_2 = list_1
print("list_1:" + str(list_1))
print("list_2:" + str(list_2))
list_1.append(11111)
list_2.append(22222)
print("list_1:" + str(list_1))
print("list_2:" + str(list_2))
print("id of list_1: [" + str(hex(id(list_1))) + "]")
print("id of list_2: [" + str(hex(id(list_2))) + "]")

#深拷贝，第二个list创建了第一个list的完全副本
title_test("list copy test for deep copy")
list_3 = [(value ** 2) for value in range(1,20,2)]
list_4 = list_3[:]
print("list_3:" + str(list_3))
print("list_4:" + str(list_4))
list_3.append(33333)
list_4.append(44444)
print("list_3:" + str(list_3))
print("list_4:" + str(list_4))
print("id of list_3: [" + str(hex(id(list_3))) + "]")
print("id of list_4: [" + str(hex(id(list_4))) + "]")

#-----------------------------------------------------------------------
#元组测试（元组即不可变的列表，用小括号括起来）
#-----------------------------------------------------------------------
title_test("tuple list test")
tuple_list = (0,1,2,3)
print("tuple_list data:" + str(tuple_list))
print("tuple_list addr[:" + str(hex(id(tuple_list))) + "]")

#元组的元素是不可修改（增/删/改）的，因此像如下操作是非法的
#for value in range(1,10,1):
#	tuple_list.append(value)
#for index in range(1,len(tuple_list)):
#	del tuple_list[0]
#for index in range(1,len(tuple_list)):
#	tuple_list[index] = tuple_list[0]

#但是元组可以直接整体修改
#其实是元组变量重新定义与初始化（同名但是不同地址的两个变量）
#但是原先的同名变量存储空间是否还有效，空间不会被回收？存疑！
tuple_list = (0,1,2,3,4,5)
print("tuple_list data:" + str(tuple_list))
print("tuple_list addr:[" + str(hex(id(tuple_list))) + "]")

#-----------------------------------------------------------------------
#是否非列表的变量也是如此，修改值，其id也会变化？？测试结果果真如此！
#-----------------------------------------------------------------------
title_test("tuple value test")
tuple_value = 1
print("tuple_value data:" + str(tuple_value))
print("tuple_value addr[:" + str(hex(id(tuple_value))) + "]")
tuple_value = 2
print("tuple_value data:" + str(tuple_value))
print("tuple_value addr[:" + str(hex(id(tuple_value))) + "]")
