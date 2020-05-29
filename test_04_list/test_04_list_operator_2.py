# coding=gbk
#		Error: Non-UTF-8 code starting with '\xc4'�����������ļ���ͷ����
# 		"# coding=gbk" ���� "coding:utf-8"����
#
#-----------------------------------------------------------------------
#    Time           :2020��5��29��19:22:12
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python�б�������ѧϰ����
#    FileName       :test_04_list_operator_2.py
#-----------------------------------------------------------------------

Week = [
	["Monday   ",	"����һ",	"1st"],
	["Tuesday  ",	"���ڶ�",	"2nd"],
	["Wednesday",	"������",	"3rd"],
	["Thursday ",	"������",	"4th"],
	["Friday   ",	"������",	"5th"],
	["Saturday ",	"������",	"6th"],
	["Sunday   ",	"������",	"7th"]
];
#-----------------------------------------------------------------------
#ע�⣺
#1������ȫ�ֱ�������ֱ�Ӹ�ֵ��ֱ�ӵĸ�ֵ��������Ϊ�Ƕ���ֲ�����
#2���ڸ�ֵʱ�����������֮ǰ�Ѿ�����Ϊȫ�֣�����Ϊ��ȫ�ֱ�����ֵ
#3�������ڲ���ȫ�ֱ��������ı����ᱻ��Ϊ�Ǿֲ�����
#4�������ڲ�ҪҪʹ��ȫ�ֱ�������Ҫ����global
#5��Ϊ�˺;ֲ��������ֿ��������������⣬ȫ�ֱ�����ü���g_xxxx�ı�־
#-----------------------------------------------------------------------
global g_title_test_count
g_title_test_count = 0

#-----------------------------------------------------------------------
#���Ա����ӡ����
#-----------------------------------------------------------------------
title_str = "----------------------------------------------------------"
def title_test(test_title_str):
	global g_title_test_count
	g_title_test_count += 1
	print("\n" + title_str)
	print(str(g_title_test_count) + "��" + test_title_str.title())
	print(title_str)

#-----------------------------------------------------------------------
#�б����
#1��forѭ������е�һ�б��������Զ�Ӧfor
#2�������п�����ʱѡ��������
#3����һ����ʼ�����������У�������ǰһ��û��for��while��if��def������������
#-----------------------------------------------------------------------
title_test("Two dimensional list traversal all test")
for day in Week:
	today = str(day) + ":";
	today += "\t today".title() + " is " + day[0].title();
	today += "\t ������" + day[1];
	today += "\t The " + day[2] + " day of the week!!";
	print(today)

title_test("Two dimensional list traversal last test")
for day in Week:
	today = str(day) + ":";
today += "\t today".title() + " is " + day[0].title();
today += "\t ������" + day[1];
today += "\t The " + day[2] + " day of the week!!";
print(today)


#-----------------------------------------------------------------------
#range()���ú�����ʹ��
#ͨ�������������ӿ���֪����value��range()��ȡֵ����������Ϊfor��index
#range(start,end<,length>),ָ������Ϊlength
#-----------------------------------------------------------------------
title_test("range number test1")
value_str = ""
count = 0
#��range list��������һ���б�
#�������еȼ��ڣ�
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
#��range list��������һ���б�ָ������Ϊ2
range_list = list(range(100,260,2))
for value2 in range_list:
	count += 1
	value2 = 1000
	value_str += str(value2) + " "
	if (count % 16 == 0):
		value_str += "\n"
print(value_str)

#-----------------------------------------------------------------------
#min()��max()��sum()��range()�����ú������������
#-----------------------------------------------------------------------
#����range������������б�
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

#����range()��forѭ���������߼��ı�ʾʽֱ�ӹ����б�
#�÷�ʽ��Ϊ�б����
title_test("range number test4")
squares = [(value ** value + value) for value in range(1,10,2)]
print(squares)

squares = list(range(1, 1000000+1))
print(str(min(squares)) + " + ... + " + str(max(squares)) + " = " + str(sum(squares)))

#-----------------------------------------------------------------------
#��ȡ����Ƭ���б�ָ����Χ��Ԫ��
#-----------------------------------------------------------------------
title_test("section list number test")
section_list = list(range(1,100,3))
#ָ����Χ���б���Ƭ
print("section_list[pos1:pos2]")
print("\t" + str(section_list[4:10]))
print("\t" + str(section_list[(len(section_list) - 12):(len(section_list) - 5)]))
#Ĭ�ϴ�0��ָ������λ�ö��б���Ƭ
print("section_list[<start>:pos2]")
print("\t" + str(section_list[:10]))
print("\t" + str(section_list[:-15]))
#Ĭ�ϴ�ָ����ʼλ�õ��������б���Ƭ
print("section_list[pos1:<end>]")
print("\t" + str(section_list[(len(section_list) - 12):]))
print("\t" + str(section_list[-15:]))

title_test("section list number traversal and operator")
for value in section_list[-10:]:
	print("\t" + str(value) + "^2=" + str(value**2))

#-----------------------------------------------------------------------
#�б���������C++�ġ�ǳ�������͡�������ĸ��
#-----------------------------------------------------------------------
#ǳ����������list������ͬһ���б�Ĳ�ͬ����
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

#������ڶ���list�����˵�һ��list����ȫ����
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
#Ԫ����ԣ�Ԫ�鼴���ɱ���б���С������������
#-----------------------------------------------------------------------
title_test("tuple list test")
tuple_list = (0,1,2,3)
print("tuple_list data:" + str(tuple_list))
print("tuple_list addr[:" + str(hex(id(tuple_list))) + "]")

#Ԫ���Ԫ���ǲ����޸ģ���/ɾ/�ģ��ģ���������²����ǷǷ���
#for value in range(1,10,1):
#	tuple_list.append(value)
#for index in range(1,len(tuple_list)):
#	del tuple_list[0]
#for index in range(1,len(tuple_list)):
#	tuple_list[index] = tuple_list[0]

#����Ԫ�����ֱ�������޸�
#��ʵ��Ԫ��������¶������ʼ����ͬ�����ǲ�ͬ��ַ������������
#����ԭ�ȵ�ͬ�������洢�ռ��Ƿ���Ч���ռ䲻�ᱻ���գ����ɣ�
tuple_list = (0,1,2,3,4,5)
print("tuple_list data:" + str(tuple_list))
print("tuple_list addr:[" + str(hex(id(tuple_list))) + "]")

#-----------------------------------------------------------------------
#�Ƿ���б�ı���Ҳ����ˣ��޸�ֵ����idҲ��仯�������Խ��������ˣ�
#-----------------------------------------------------------------------
title_test("tuple value test")
tuple_value = 1
print("tuple_value data:" + str(tuple_value))
print("tuple_value addr[:" + str(hex(id(tuple_value))) + "]")
tuple_value = 2
print("tuple_value data:" + str(tuple_value))
print("tuple_value addr[:" + str(hex(id(tuple_value))) + "]")
