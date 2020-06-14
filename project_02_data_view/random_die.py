# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月14日16:59:49
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :数据可视化骰子类
#    FileName       :random_die.py
#***********************************************************************

from random import randint

#一个生成骰子随机点数的类
class RandomDie():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    #从1到num_sides中返回一个随机点数
    def roll(self):
        return randint(1, self.num_sides)
