# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月31日17:59:43
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :类的模块化--装备类
#    FileName       :test_09_class_equip.py
#***********************************************************************
#-----------------------------------------------------------------------
#类的创建与使用:装备类
#-----------------------------------------------------------------------
class Equipment():
    def __init__(self,
                jacket='背心',
                trousers='七分裤',
                hat='太阳帽',
                pets='皮卡丘',
                weapon='多兰盾'):
        self.jacket = jacket
        self.trousers = trousers
        self.hat = hat
        self.pets = pets
        self.weapon = weapon
        
    def get_equipment(self):
        print(jacket)
