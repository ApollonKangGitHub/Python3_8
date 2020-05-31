# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年5月31日22:44:33
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :数据存储于JSON（JavaScript Object Notaion）
#    FileName       :test_10_data_save.py
#***********************************************************************

import json
from collections import OrderedDict

global g_json_dump_num_file 
global g_json_dump_dict_file 
global book_set
g_json_dump_num_file = r"json\json_num_list.json"
g_json_dump_dict_file = r"json\json_dict_list.json"

#文件（目录）未找到异常测试
#g_json_dump_num_file = r"json_exception\json_num_list.json"
#g_json_dump_dict_file = r"jsons_exception\json_dict_list.json"

g_book_set  = OrderedDict({
    '新华书店':[
        {
            '检索号':'XH_1234567',
            '书名':'《新华书店管理手册》',
            '出版社':'新华出版社',
            '出版时间':'2020-05-30',
            '类别':'管理类',
            '定价':"20.00",
            '作者':'佚名',
            '余量':"100",
        },
        {
            '检索号':'XH_1234568',
            '书名':'《三国演义》',
            '出版社':'中华书局',
            '出版时间':'2010-03-10',
            '类别':'文学小说类',
            '定价':"30.00",
            '作者':'罗贯中',
            '余量':"10",
        },
    ],
    
    '文轩新华书店':[],
    
    '钟楼书店':[],
    
    '1小时书屋':[],
    
    '伴清晨诗文':[],
    
    '考研辅导资料专卖':[],
    
    '博库书店':[],
})

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
#json.dump()和json.load()数字操作列表
#-----------------------------------------------------------------------
def json_dump_num(file_name):
	numbers = [1,2,3,4,5,6,7]
	try:
		with open(file_name, 'w') as file_object:
			json.dump(numbers, file_object)
			print("json dump numbers to " + file_name + " succeed!")
	except FileNotFoundError:
		print(file_name + "file or dirctory is not exist")

def json_load_num(file_name):
	numbers = []
	try:
		with open(file_name) as file_object:
			numbers = json.load(file_object)
			print("json load numbers from " + file_name + " succeed!")
			print("numbers=" + str(numbers))
	except FileNotFoundError:
		print(file_name + "file or dirctory is not exist")
		
#-----------------------------------------------------------------------
#json.dump()和json.load()操作字典列表
#-----------------------------------------------------------------------		
def json_dump_dict(file_name):
	dict_info = g_book_set
	try:
		with open(file_name, 'w') as file_object:
			json.dump(dict_info, file_object)
			print("json dump dictionary to " + file_name + " succeed!")
	except FileNotFoundError:
		print(file_name + "file or dirctory is not exist")

def json_load_dict(file_name):
	dict_info = {}
	try:
		with open(file_name) as file_object:
			dict_info = json.load(file_object)
			print("json load dictionary from " + file_name + " succeed!")
			print("dictionary info:" + str(dict_info))
	except FileNotFoundError:
		print(file_name + "file or dirctory is not exist")
		
#-----------------------------------------------------------------------
#dump和load测试
#-----------------------------------------------------------------------							
title_test("json dump and load number")
json_dump_num(g_json_dump_num_file)
json_load_num(g_json_dump_num_file)

title_test("json dump and load dictionary")
json_dump_dict(g_json_dump_dict_file)
json_load_dict(g_json_dump_dict_file)
