# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月1日22:59:07
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :set功能的类，增加set功能，直接对set类增加函数
#    FileName       :setting.py
#***********************************************************************
class Setting():
    def __init__(self):
        #屏幕设置
        self.screen = {
            "width"            :1200,
            "height"           :800,
            "color"            :"灰色",
        }

        #飞船速率
        self.ship_speed = 1.1
        self.ship_bullets_group_num = 2
        
        #子弹,修改子弹余量、宽度、长度、发射间隔就可以产生大招
        #可以根据蓄能，临时修改子弹相关参数（在子弹对象中修改）
        #发射完大招后再恢复该默认的子弹参数
        self.bullet = {
            "speed"            :0.5,        #子弹速度
            "width"            :2,          #子弹宽度
            "height"           :10,         #子弹高度
            "color"            :"红色",     #子弹颜色
            "limit"            :10,         #弹药库容量
            "interval"         :150,        #发射间隔
            "pos_diff"         :15          #子弹和飞船中心的坐标差
        }
        
        #外星人属性
        self.alien = {
            "speed_x"          :0.8,       #外星人横向速度
            "speed_y"          :0.5,       #外星人纵向速度
            "pos_x"            :0.1,       #外星人x坐标
            "pos_y"            :0.1,       #外星人y坐标
            "interval"         :50,        #移动周期
        }
    def get_screen_size(self):
        return (self.screen["width"], self.screen["height"])
