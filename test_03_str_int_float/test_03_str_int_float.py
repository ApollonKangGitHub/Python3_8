#-----------------------------------------------------------------------
#    Time           :2020年5月28日20:20:28
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :字符串、整数、浮点数测试
#    FileName       :test_03_str_int_float.py
#-----------------------------------------------------------------------

python_title = "-----------------------------------------------------------------------"

#-----------------------------------------------------------------------
#字符串的简单用法
#-----------------------------------------------------------------------
#''和""的用法
#要想将'或者"不当做字符串标识而只当做字符，则加上'\'即可
#对于'\'同理，'\\'即为字符'\'
print(python_title)
print("字符串表示方式测试：")
print(python_title)
str_1 = 'Hello Pyton3.8'
str_2 = "Hello Python3.8"
str_3 = "He's name is python3.8"
print(str_1)
print(str_2)
print(str_3)
print("\\\"The Roman is not bulid in a day\\\" someone said" + "\n")

# "单词首字符大写，非首字母小写" 方法、全大写方法、全小写方法
print(python_title)
print("字符串操作方法测试：")
print(python_title)
str_name = "my NAME is pYTHon 3.8"
print(str_name.title())
print(str_name.upper())
print(str_name.lower() + "\n")

#合并/拼接字符串、数字等
my_name = "ruoujin"
my_family = "kang"
my_age = 24
start = "hello"
meet_say = start.title() + ' My name is ' + my_family.upper() + ' '
meet_say += my_name.title() + ', ' + str(my_age) + ' years old!\n'
print(meet_say)

#删除多余空白,lstrip/rstrip/strip删除对象开头/结尾/首尾的多余空格
str_space = "    Hello more space    "
print("start:".upper() + str_space + ":end".upper())
print("\tstart:".upper() + str_space.lstrip() + ":end".upper())
print("\tstart:".upper() + str_space.rstrip() + ":end".upper())
print("\tstart:".upper() + str_space.strip() + ":end".upper())

print("start:".upper() + str_space + ":end".upper())
str_space = str_space.strip()
print("\tstart:".upper() + str_space + ":end".upper() + "\n")

#python2中print是一个关键字，而python3中print是一个函数
#-----------------------------------------------------------------------
#整数的简单用法: 加(+) 减(-) 乘(*) 除(/) 乘方(**) 取余(%)
#python2中'/'是取整合除法的结合运算符,整数运算结果为取整，而整数和小数运算才是除法
#-----------------------------------------------------------------------
int_a = 99;
int_b = 5;
print(python_title)
print("整数运算测试：")
print(python_title)

print(str(int_a) + "+" + str(int_b) + "=" + str(int_a + int_b))
print(str(int_a) + "-" + str(int_b) + "=" + str(int_a - int_b))
print(str(int_a) + "*" + str(int_b) + "=" + str(int_a * int_b))
print(str(int_a) + "/" + str(int_b) + "=" + str(int_a / int_b))
print(str(int_a) + "^" + str(int_b) + "=" + str(int_a ** int_b))
print(str(int_a) + "%" + str(int_b) + "=" + str(int_a % int_b))
print("\r\n")

#-----------------------------------------------------------------------
#浮点数的简单用法: 和整数用起来基本没差别，但是存在精度问题
#-----------------------------------------------------------------------
float_a = 9.222;
float_b = 1.333;
print(python_title)
print("浮点数运算测试：")
print(python_title)

print(str(float_a) + "+" + str(float_b) + "=" + str(float_a + float_b))
print(str(float_a) + "-" + str(float_b) + "=" + str(float_a - float_b))
print(str(float_a) + "*" + str(float_b) + "=" + str(float_a * float_b))
print(str(float_a) + "/" + str(float_b) + "=" + str(float_a / float_b))
print(str(float_a) + "^" + str(float_b) + "=" + str(float_a ** float_b))
print(str(float_a) + "%" + str(float_b) + "=" + str(float_a % float_b))
print("\r\n")

print(python_title)
print("浮点数精度测试：")
print(python_title)

print("0.1+0.2 = " + str(0.1+0.2))
print("3*0.1 = " + str(3*0.1))
print("0.3*1 = " + str(0.3*1))
print("\r\n")

#-----------------------------------------------------------------------
#Python之禅：
#-----------------------------------------------------------------------

print(python_title)
print("Python之禅：")
print(python_title)
import this
print(python_title)
