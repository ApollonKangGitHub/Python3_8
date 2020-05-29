#-----------------------------------------------------------------------
#    Time           :2020年5月28日20:38:12
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python列表学习测试
#    FileName       :test_04_list_operator_1.py
#-----------------------------------------------------------------------

#列表用[]来表示，用逗号分割元素
#-----------------------------------------------------------------------
#数据定义
#-----------------------------------------------------------------------
prog_language = [
	"C", 
	"C++", 
	"Python",
	"JAVA", 
	"CSS", 
	"HTML", 
	"XML", 
	"JAVAScript", 
	"SHELL",
	"PHP"
];
list_int = [10,2,3,5,7,32,5,3,71,9]
title = "-----------------------------------------------------------------------------------------"

#-----------------------------------------------------------------------
#测试：
#1、输出列表，直接指定列表名字，输出时包含中括号一起输出
#2、索引输出，支持反向索引（从列表尾部开始索引，负号表示逆向索引）
#-----------------------------------------------------------------------
print(title)
print("language list:".title())
print(title)

#print直接遍历
print(prog_language)

#print反向遍历，reverse()方法永久把列表倒转过来，再调用一次即可恢复
#prog_language.reverse()作用于prog_language对象，
#整个表达式不能误以为返回一个反转后的临时对象，作为参数传给print
prog_language.reverse()
print(prog_language)
prog_language.reverse()

#-----------------------------------------------------------------------
#手动正向遍历与操作
#-----------------------------------------------------------------------
print(title)
print("forward traversal".title())
print(title)
index = 0
language_str = ""
language_all_str = ""
while(index < len(prog_language)):
	language_str = prog_language[index].lower() + " "
	language_str += prog_language[index].upper() + " "
	language_str += prog_language[index].title()
	language_all_str += prog_language[index].title() + " "
	
	print("list[" + str(index) + "]:")
	print("\t" + language_str)
	print("\t" + language_all_str)
	index += 1

#-----------------------------------------------------------------------
#手动反向遍历与操作
#-----------------------------------------------------------------------
print(title)
print("reverse traversal".title())
print(title)
index = - 1
count = 0
language_all_str = ""
while(count < len(prog_language)):
	language_str = prog_language[index].lower() + " "
	language_str += prog_language[index].upper() + " "
	language_str += prog_language[index].title()
	language_all_str += prog_language[index].title() + " "
	
	print("list[" + str(index) + "]:")
	print("\t" + language_str)
	print("\t" + language_all_str)
	index -= 1
	count += 1

#-----------------------------------------------------------------------
#搜索修改列表元素，直接索引并赋值即可
#-----------------------------------------------------------------------
find_language = "python"
print(title)
print("find language".title() + find_language.title())
print(title)
index = 0
while(index < len(prog_language)):
	if ((prog_language[index] == find_language.title())
	or (prog_language[index] == find_language.upper())
	or (prog_language[index] == find_language.lower())):
		print(prog_language[index] + " is found!!")
		prog_language[index] = prog_language[index] + "3.8";
		break;
	index += 1

print(title)
print("Modify " + find_language + " and print list".title())
print(title)
print(prog_language)

#-----------------------------------------------------------------------
#列表元素追加
#-----------------------------------------------------------------------
print(title)
print("append language test".title())
print(title)
print("prog_language:\n\t" + str(prog_language))
append_language = []
insert_language = "assembly"
index = -1
count = 0
while(count < len(prog_language)):
	append_language.append(prog_language[index])
	print("append_language append " + prog_language[index] + ":\n\t" + str(append_language))
	index -= 1
	count += 1

#-----------------------------------------------------------------------
#列表元素插入
#-----------------------------------------------------------------------
print(title)
print("insert language test".title())
print(title)
append_language.insert(0, insert_language.upper())
print("append_language insert " + insert_language.title() + ":\n\t" + str(append_language))

#-----------------------------------------------------------------------
#列表元素删除（删除指定位置元素用'del'关键字）
#列表元素获取并删除用pop方法
#pop()默认获取并删除列表末尾元素
#pop(index)可以获取并删除指定列表位置元素
#根据值/内容来删除元素使用remove()方法
#remove()一次只能删除一个元素，不能自动删除所有指定内容相同的元素
#-----------------------------------------------------------------------
print(title)
print("delete language test".title())
print(title)
index = 0
pop_del = ""
len_delete = len(append_language)
#注意len_append要实时更新，虽然可以直接在while里用"len(append_language)"
#但是对于这种我们不确定解析器行为的语句尽量自行保证
while(index < len_delete):
	len_delete = len(append_language)
	if (index % 2 == 0):
		del append_language[index]
		print("[index:" + str(index) + " < len:" + str(len_delete) + "]")
		print("\t append_language delete " + append_language[index].title() + ":\n\t" + str(append_language))
	else:
		pop_del = append_language.pop()
		print("[index:" + str(index) + " < len:" + str(len_delete) + "]")
		print("\t append_language pop " + pop_del.title() + ":\n\t" + str(append_language))
	index += 1

print(title)
print("love append and not love remove language test".title())
print(title)
love_language = "Perl"
not_love_language = "Perl"
append_language.append(love_language)
print("love append " + love_language + ":\n\t" + str(append_language))
append_language.remove(not_love_language)
print("not love remove " + not_love_language + ":\n\t" + str(append_language))

#-----------------------------------------------------------------------
#列表排序：
#1、列表排临时正向排序
#2、列表排临时逆向排序
#3、列表无法恢复的正向排序
#4、无列表法恢复的逆向排序
#-----------------------------------------------------------------------
print(title)
print("integer sort test temporary".title())
print(title)
print("原始数据        	：" + str(list_int))

#临时排序，内置方法返回临时对象，不修改原始对象
print("正向排序临时数据 	：" + str(sorted(list_int)))
print("原始数据        	：" + str(list_int))
print("反向排序临时数据	：" + str(sorted(list_int, reverse=True)))
print("原始数据      		：" + str(list_int))

print(title)
print("integer sort test forever".title())
print(title)
#对象的方法不产生临时对象，而是修改对象本身
list_int.sort()
print("无法恢复的正向排序	：" + str(list_int))
print("原始数据        	：" + str(list_int))
list_int.sort(reverse=True)
print("无法恢复的逆向排序	：" + str(list_int))
print("原始数据        	：" + str(list_int))
