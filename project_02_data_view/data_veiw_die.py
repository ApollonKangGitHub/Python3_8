# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月14日16:31:10
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :pygal与掷骰子点数可视化
#    FileName       :data_view_die.py
#***********************************************************************

from matplotlib import pyplot as plt
from random_die import RandomDie
import pygal

global g_save_path
global g_save_tail
g_save_path = r'./saveFig/pygal/'
g_save_tail = '.svg'

def one_die_result_test():
    die = RandomDie()
    results = []
    frequencies = []
    save_path_name = g_save_path + 'D6' + g_save_tail
    
    #获取100000个随机的骰子点数
    times = 100000
    for roll_num in range(times):
        results.append(die.roll())
    #计算各个点数的频率
    for value in range(1, die.num_sides + 1):
        frequencies.append(results.count(value))
    
    #可视化
    hist = pygal.Bar()
    hist.x_labels = []
    for index in range(1, die.num_sides):
        hist.x_labels.append(str(index))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    #指定渲染标签和对象列表
    hist.add('D6', frequencies)    
    #渲染为svg文件
    hist.render_to_file(save_path_name)
    
def one_die_result_test():
    die_1 = RandomDie()
    die_2 = RandomDie()
    results = []
    frequencies = []
    save_path_name = g_save_path + 'D6_add' + g_save_tail
    max_num = die_1.num_sides + die_2.num_sides
    
    #获取100000个随机的骰子点数
    times = 100000
    for roll_num in range(times):
        results.append(die_1.roll() + die_2.roll())
    #计算各个点数和的频率
    for value in range(1, max_num + 1):
        frequencies.append(results.count(value))
    
    #可视化
    hist = pygal.Bar()
    hist.x_labels = []
    for index in range(1, max_num):
        hist.x_labels.append(str(index))
    hist.x_title = "Result of rolling two D6 dice " + str(times) + " times."
    hist.y_title = "Frequency of Result"
    
    #指定渲染标签和对象列表
    hist.add('D6 + D6', frequencies)    
    #渲染为svg文件
    hist.render_to_file(save_path_name)
    
def random_die_test():
    one_die_result_test()
    one_die_result_test()
    
random_die_test()
