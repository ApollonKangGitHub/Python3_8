# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年5月31日19:10:23
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :文件操作语法测试
#    FileName       :test_10_file.py
#***********************************************************************

#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
global g_title_test_count
global g_title_str
g_title_test_count = 0
g_title_str = "--------------------------------------------------------"

def title_test(test_title_str = "default test"):
    global g_title_test_count
    g_title_test_count += 1
    print("\n" + g_title_str)
    print(str(g_title_test_count) + "、" + test_title_str.lower() + ":")
    print(g_title_str)
    
#-----------------------------------------------------------------------
#Windows中绝对路径的字符串前加上r，确保路径被正确解析
#若未指定路径，默认文件在python程序文件所在目录下查找
#否则Windows中的路径符号'\'可能会被识别为转义符号，或者自行对'\'进行转义
#-----------------------------------------------------------------------
global g_pi_part_1
global g_pi_part_2
global g_pi_million
global g_python
global g_python_replace
g_pi_part_1 = r"fil_operator\pi_digits_1.txt"
g_pi_part_2 = r"fil_operator\pi_digits_2.txt"
g_pi_million = "fil_operator\\pi_million_digits.txt"
g_python = "fil_operator\\python.txt"
g_python_replace = "fil_operator\\python_replace.txt"

#-----------------------------------------------------------------------
#打开一个文件读取数据并显示
#    1、obj = open()用来打印一个指定的文件并返回一个对象
#    2、obj.read()用来读取文件obj,返回一个字符串
#    3、obj.close()
#    4、"with open() as obj"用来指示python当前代码只关心打开，
#    不负责关闭，python会在何时的实际关闭obj，obj还能在with代码块内使用
#-----------------------------------------------------------------------
def file_test_with_open_read(path_file):
    with open(path_file) as obj:
        contents = obj.read()
        print(contents)

def file_test_open_read_close(path_file):
    obj = open(path_file)
    print(obj.read())
    obj.close()

#-----------------------------------------------------------------------
#按行读取文件
#    1、按行读取时，每行都会多一个换行（文件一个换行，print()自带一个）
#    2、除了"for <contexts> in obj"方式遍历每一行
#    还可使用"lines = readlines()"方法与"for line in lines"来遍历每一行
#    readlines()返回一个列表，列表每个元素的内容为文件的每行内容
#    注意read()和readlines()的区别，前者返回字符串，后者返回列表
#-----------------------------------------------------------------------
def file_test_with_open_for_in_obj(path_file):
    with open(path_file) as obj:
        print("with open as obj\t:" + str(type(obj)))
        print("read()\t\t\t:" + str(type(obj.read())))
        print("readlines()\t\t:" + str(type(obj.readlines())))
        for line in obj:
            print(line.rstrip() + "\t\t:" + str(type(line)))


def file_test_with_open_readlines(path_file):
    with open(path_file) as obj:
        lines = obj.readlines()
        print("readlines() return\t:" + str(type(lines)))
        for line in lines:
            print(line.rstrip() + "\t\t:" + str(type(line)))

#-----------------------------------------------------------------------
#读取100万的数据，并查找自己的生日
#-----------------------------------------------------------------------
def file_test_read_1000000_info(path_name):
    count = 0
    read_str = ""
    with open(path_name) as obj:
        while True:
            line = obj.readline()
            print(line.rstrip())
            read_str += line.strip()
            
            #读取到文件末尾，则读取到的行位''
            if (line == ''):
                print("read over, read len = " + str(len(read_str)))
                break;
                
            count += 1
            if (count % 100 == 0):
                read_again = input("继续读取（Y/N）：").strip()
                if read_again.upper() == 'Y':
                    continue
                else:
                    break;

        print("read line = " + str(len(read_str)))
        
        #1000000中没有找到不代表圆周率中不存在，指示前1000000中不存在
        birthday = input("请输入生日，以确认在圆周率中存在：").strip()
        if birthday in read_str:
            print("你的生日序列[" + birthday + "在圆周率中能够被找到！")
        else:
            print("没有找到你的生日序列[" + birthday + "]")

#-----------------------------------------------------------------------
#打开文件读取每一行，将匹配内容修改并创建新的文件后把修改内容写入新文件
#    1、write()只能写字符串
#    2、open()默认打开为'r'，其他参数为'+'、'w'、'a'等
#    3、open(path, 'w')文件不存在则会创建文件
#    4、open(path, 'w')文件已经存在，则会在返回文件对象前清除原文件
#    5、replace()方法替换返回的str是在原str的副本上操作的，不影响原str
#-----------------------------------------------------------------------
def file_test_read_replace_create_write(path_name, replace_name):
    write_str = ''
    with open(path_name) as obj:
        while True:
            line = obj.readline()

            #读取到文件末尾，则读取到的行位''
            if (line == ''):
                print("read over, write len = " + str(len(write_str)))
                break
            
            if "python" in line:
                new_line = line.replace("python", "C and C++")
            elif "PYTHON_2.7" in line:
                new_line = line.replace("PYTHON_2.7", "Java")
            else:
                new_line = line
            write_str += new_line
            
    with open(replace_name, "w") as obj:
        obj.write(write_str)

#-----------------------------------------------------------------------
#调用测试

#圆周率前一部分的两个文件读取
title_test("read file by read() function")
file_test_with_open_read(g_pi_part_1)
file_test_open_read_close(g_pi_part_2)

#读取行测试
title_test("read file by \"for <contexts> in obj\" loop")
file_test_with_open_for_in_obj(g_pi_part_1)
title_test("read file by readlines() function")
file_test_with_open_readlines(g_pi_part_1)

#读取大文件测试
title_test("read file million info")
file_test_read_1000000_info(g_pi_million)

#读取文件替换内容并写入新文件
title_test("read file replace and write newv file")
file_test_read_replace_create_write(g_python, g_python_replace)
