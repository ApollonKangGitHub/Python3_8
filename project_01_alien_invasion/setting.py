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
            "width"            :500,
            "height"           :800,
            "color"            :"灰色",
        }
        
        self.save_file_path = "dump_info.txt"

        #飞船速率、弹药发射器个数、强化周期
        self.ship = {
            "bullets_group"    :4,     #子弹发射器个数
            "intensify_num"    :400,   #一波强化射击次数
        }

        #子弹,修改子弹余量、宽度、长度、发射间隔就可以产生大招
        #可以根据蓄能，临时修改子弹相关参数（在子弹对象中修改）
        #发射完大招后再恢复该默认的子弹参数
        self.bullet = {
            "width"            :5,          #子弹高度
            "height"           :10,         #子弹高度
            "color"            :"绿色",      #子弹颜色
            "limit"            :10,         #弹药库容量
            "pos_diff"         :15,         #子弹和飞船中心的坐标差
        }
        
        #外星人属性
        self.alien = {
            "pos_x"            :0.1,       #外星人x坐标
            "pos_y"            :0.1,       #外星人y坐标
            "interval"         :50,        #移动周期
        }
        
        #游戏全局的一些属性
        self.game = {
            "ship_limit"       :3,         #飞船补给量
            "get_away_limit"   :20,        #外星人逃离上限
        }
        
        #按钮的属性
        self.button = {
            "button_color"     :"深灰",     #按钮颜色
            "button_width"     :100,       #按钮宽度
            "button_height"    :50,        #按钮高度
            "text_size"        :40,        #按钮文字大小 
            "text_msg"         :"Play",    #按钮文字信息
            "text_color"       :"绿色",     #按钮文字颜色
        }
        
        self.score_board = {
            "background_color" :"灰色",
            "text_size"        :30,
            "text_color"       :"黑色",
        }
        
        #初始化速率属性
        self.__init_speed_attr__()
        self.__init_interval_attr__()
        
    def get_screen_size(self):
        return (self.screen["width"], self.screen["height"])

    #难度递增
    def increase_difficulty_attr(self):
        if self.ship["speed"] < self.ship["speed_max"]:
            self.ship["speed"] *= self.ship["speed_scale"]
        if self.bullet["speed"] < self.bullet["speed_max"]:
            self.bullet["speed"] *= self.bullet["speed_scale"]
        if self.alien["speed_x"] < self.alien["speed_x_max"]:
            self.alien["speed_x"] *= self.alien["speed_x_scale"]
        if self.alien["speed_y"] < self.alien["speed_y_max"]:
            self.alien["speed_y"] *= self.alien["speed_y_scale"]

        #更新大招周期
        self.__update_interval()

    def __init_speed_attr__(self):
        #初始化速率
        self.ship["speed"] = 1.1
        self.bullet["speed"] = 1.2
        self.alien["speed_x"] = 0.8
        self.alien["speed_y"] = 1.1

        #初始化速率难度递增倍数
        self.ship["speed_scale"] = 1.2
        self.bullet["speed_scale"] = 1.5
        self.alien["speed_x_scale"] = 1.2
        self.alien["speed_y_scale"] = 1.1
        
        #最大速率
        self.ship["speed_max"] = 2.6
        self.bullet["speed_max"] = 3.6
        self.alien["speed_x_max"] = 2.6
        self.alien["speed_y_max"] = 5.6
            
    def __init_interval_attr__(self):
        self.ship["intensify_cycle"] = 500
        self.ship["cycle_min"] = 300
        self.bullet["interval"] = 200
        self.bullet["interval_min"] = 50
        
    def __update_interval(self):
        if self.ship["intensify_cycle"] > self.ship["cycle_min"]:
            self.ship["intensify_cycle"] -= 10
        if self.bullet["interval"] > self.bullet["interval_min"]:
            self.bullet["interval"] -= 5
