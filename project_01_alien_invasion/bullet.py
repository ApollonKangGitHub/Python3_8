# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月6日16:14:29
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :子弹类
#    FileName       :Bullet.py
#***********************************************************************
import pygame
from surface import surface_color_convert as color_convert
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, bullet, screen, ship):
        #父类构造函数，python2.7和python3.8都支持的语法
        super(Bullet, self).__init__()
        self.screen = screen
        self.new_bullet__(ship, bullet)
        
    def new_bullet__(self, ship, bullet):
        #在（0,0）处创建一个子弹，再根据飞船位置设置子弹正确位置
        self.rect = pygame.Rect(0,0,bullet["width"],bullet["height"])
        centerx = ship.rect.centerx
        self.rect.centerx = centerx + bullet["pos_diff"]
        self.rect.bottom = ship.rect.top
        
        #保存子弹信息
        self.posx = float(self.rect.x)
        self.posy = float(self.rect.y)
        self.color = color_convert(bullet["color"])
        self.speed = bullet["speed"]

    #子弹移动函数（覆写父类函数）
    def update(self):
        self.posy -= self.speed
        self.posx -= 0
        self.rect.y = self.posy
    

    #子弹绘制函数
    def __draw__(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    #判断子弹是否需要销毁
    def __need_destroy__(self):
        if self.rect.bottom <= 0:
            return True
        else:
            return False

    #获取子弹默认强化属性(速率不能过高，可能坐标会跳过设计目标，但是可以修改发射间隔)
    def __bullet_intensify__(self):
        bullet_attr = {
            "width":10,
            "height":400,
            "pos_diff":15,
            "color":"红色",
            "speed":40.0,
            "interval":4,
        }
        return bullet_attr
    
    #修改子弹属性
    def __modify_bullet_attr__(self, ship, bullet_attr):
        self.new_bullet__(ship, bullet_attr)
