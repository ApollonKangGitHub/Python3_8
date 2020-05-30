# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月30日12:45:56
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :python的字典语法与操作测试
#                    （可以把字典理解成结构体，列表理解成链表，
#                    而列表嵌列表、字典嵌字典、字典嵌列表、列表嵌字典，
#                    各种嵌套的数据结构也就是类似的）
#    FileName       :test_06_dictionary.py
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

#***********************************************************************
#字典定义使：用key-vlaue的数据组织形式，用大括号"{}"括起来
#key是唯一的，而不同key的value是可以相同的
#value可以是任何对象（数字、字符串、列表、字典等）
#通常都是定义空字典 dict = {}，使用过程中态增删键值对
#eg:定义空列表，列表元素为字典，字典数据为战机信息则可以动态更新游戏数据
#***********************************************************************
title_test("dictionary values with key")
dictionary = {
	'color':['green','yellow','red','black'],
	'point':[(1,2), (3,4), (5,6), (3,9), (7,9), (11,2), (5,8)],
	'blood':[blood ** 2 for blood in range(10,25)],
}

print("color: " + str(dictionary['color']))
print("point: " + str(dictionary['point']))
print("blood: " + str(dictionary['blood']))
#如上字典的key-value其格式都不一样，但是理论上同类别的key-value
#放在一个字典里才是合适的，有共同点才更容易组织处理，逻辑也更容易理解

#***********************************************************************
#字典遍历：
#	遍历key-vlaue键值对--> for k,v in dict.items():
#	遍历key-->             for k in dict.keys():
#	遍历value-->           for v in set(dict.values()):
#我们可以用
#	if xxx not in dict.keys(): 
#	if xxx in dict.keys():
#	来确定某个key是否在字典的现有key里
#	因为dict.keys()、dict.values()实际上都是获取一个列表
#set()内置函数用来提供一个集合，集合中所有元素都是唯一的，即剔除重复值
#***********************************************************************
menu = {
	'start       '	:'Restart the game.',
	'sign out    '	:'Quit the game.',
	'cancellation'	:'Quit the game.',
	'league table'	:'Player information and points table.',
	'difficulty  '	:'Choose the difficulty of the game to play.',
	'snapshot    '	:'Pause saved game progress information.',
}
title_test("menu info traversal and display")
for name,description in menu.items():
	print(" \t" + str(name) + "\t: " + str(description))
	
title_test("menu info reverse sort traversal and display")
for name in sorted(menu.keys(), reverse=True):
	print(" \t" + str(name) + "\t: " + str(menu[name]))

title_test("menu info reverse clear sort traversal and display")
for descritpion in set(sorted(menu.values(), reverse=True)):
	print(" \t" + str(descritpion))
	
#***********************************************************************
#字典应用：
#    1、数据增、删、改、查
#    2、数据嵌套灵活应用（初始化，区间遍历，条件处理）
#***********************************************************************

#-----------------------------------------------------------------------
#飞机字典存储数据key列表
#-----------------------------------------------------------------------
global aircraft_attr
aircraft_attr = [
	'seq', 
	'color',
	'x_point',
	'y_point',
	'speed',
	'live',
	'blood',
	#'invalid and last' 
]

#-----------------------------------------------------------------------
#飞机字典存储数据输出函数
#-----------------------------------------------------------------------
def aircraft_print(aircraft):
	global aircraft_attr
	print("\taircraft info:")
	
	#遍历属性列表，将飞机字典中属性key对应的key-value遍历出来
	for index in range(0, len(aircraft_attr)):
		if aircraft_attr[index] in aircraft.keys():
			print("\t" + str(aircraft_attr[index])
				+ "\t:" + str(aircraft[aircraft_attr[index]]))
			
			#如果含有血量属性，根据血量属性判断飞机安全状态
			if 'blood' == aircraft_attr[index]:
				if aircraft[aircraft_attr[index]] < 100000:
					print("\tAircraft position and blood volume dangerous!")
				else:
					print("\tAircraft position and blood volume safe.")
	print(g_title_str)

#-----------------------------------------------------------------------
#飞机字典存储数据、修改数据、增加数据、删除数据测试
#-----------------------------------------------------------------------
title_test("Aircraft position and blood volume")
aircraft = {
	"seq"       :1,
	'color'     :'green',
	'x_point'   :0,
	'y_point'   :0,
	'blood'     :10000,
}

aircraft_print(aircraft)

del aircraft['seq']

aircraft['blood'] -= 9999
aircraft['live'] = True
aircraft['speed'] = 100
aircraft['x_point'] += 0
if 'speed' in aircraft:
	aircraft['y_point'] += aircraft['speed']

aircraft_print(aircraft)

#***********************************************************************
#飞机字典和列表嵌套（字典作为列表成员）测试
#一个字典是一个属性集合，有多个相同的属性集合作为列表元素
#***********************************************************************

title_test("aircrafts sets info init and traversal")
#初始化10000000架飞机
aircrafts = []
print("init aircrafts, please wait....")
for new_index in range(1,10000000):
	if (new_index % 2):
		new_aircraft = {
			"seq"       :new_index,
			'color'     :'green',
			'x_point'   :new_index * 2,
			'y_point'   :0,
			'blood'     :1000000,
			'speed'     :10,
			'live'      :True,
		}
	else:
		new_aircraft = {
			"seq"       :new_index,
			'color'     :'read',
			'x_point'   :new_index * 2,
			'y_point'   :100,
			'blood'     :10000,
			'speed'     :1000,
			'live'      :True,
		}
	aircrafts.append(new_aircraft)
print("init aircrafts succeed!")

#遍历前五架飞机
for aircraft_instance in aircrafts[:5]:
	aircraft_print(aircraft_instance)
