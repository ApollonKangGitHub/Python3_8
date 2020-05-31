# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年5月31日21:30:56
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :异常处理语法测试
#    FileName       :test_10_exception.py
#***********************************************************************

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
#python异常使用如下语法操作:
#    try:
#        [正常处理]
#    except:
#        [捕获异常处理]
#    else:
#        [依赖于try成功的代码]
#比如：除零异常、值异常等
#    try中的语句执行时，如果发生错误，则会被except对应的异常类型捕获
#    如果未发生任何错误，则except的代码不会执行。
#    一个try当其可能产生多种异常，但是不确定会为哪种异常，
#    则可以一个try为其写多个except语句
#    异常捕获处理中可以是打印提示信息，也可以是逻辑处理，还可以是pass
#    pass表示异常不traceback，也不进行其他任何操作
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#常见异常类型测试
#-----------------------------------------------------------------------
def some_exception_test():
	try:
		5/0
	except ZeroDivisionError:
		print("ZeroDivisionError exception")

	try:
		int("aaaa")
	except ValueError:
		print("ValueError exception")
		
	try:
		print("1" + 1)
	except TypeError:
		print("TypeError exception")

	try:
		obj = open(aaaa)
	except NameError:
		print("file name is valid")
	else:
		close(obj)
		
	try:
		obj = open("aaaa")
	except FileNotFoundError:
		print("file not exist")
	else:
		close(obj)
		
	try:
		num = (5/2)
	except ZeroDivisionError:
		print("ZeroDivisionError exception")
	except TypeError:
		print("TypeError exception")
	else:
		print(num)

#-----------------------------------------------------------------------
#异常的应用，文件读取、文件内容split与单词统计
#-----------------------------------------------------------------------
global file_list 
file_list = [
	r"exception_tets\alice.txt",
	r"exception_tets\exception_1.txt",
	r"exception_tets\little_women.txt",
	r"exception_tets\exception_2.txt",
	r"exception_tets\siddhartha.txt",
	r"exception_tets\moby_dict.txt",
]

def file_deal_exception_test():
	global file_list 
	#遍历要操作的文件
	for file in file_list:
		contents = ''
		words = []
		try:
			with open(file) as file_obj:
				contents = file_obj.read()
		except FileNotFoundError:
			print(file + "is not exist")
			pass
		else:
			#split()将字符串拆成单词的列表
			words = contents.split()
			num_words = len(words)
			print(file + " have " + str(num_words) + " words")
#-----------------------------------------------------------------------
#测试接口调用
#-----------------------------------------------------------------------
some_exception_test()
file_deal_exception_test()
