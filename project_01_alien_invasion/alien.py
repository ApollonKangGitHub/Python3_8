# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月6日23:10:51
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :外星人类
#    FileName       :alien.py
#***********************************************************************
import pygame
from pygame.sprite import Sprite
from random import randint

from surface import g_screen_color_dict as color
from setting import Setting

class Alien(Sprite):
    #外星人初始化
    def __init__(self, alien_attr, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r"images\alien.bmp")
        self.rect = self.image.get_rect()
        
        #初始化坐标
        self.x = self.rect.centerx = alien_attr["pos_x"]
        self.y = self.rect.top = alien_attr["pos_y"]
        self.init_x = alien_attr["pos_x"]
        
        #初始化移动速率
        self.speed_x = alien_attr["speed_x"]
        self.speed_y = alien_attr["speed_y"]
        
        #初始化移动统计和频率
        self.move_freq = alien_attr["interval"]
        self.move_count = 0

    #绘制外星人
    def __blitme__(self):
        #print(self.rect)
        self.screen.blit(self.image, self.rect)
        
    def __move__(self):
        limit = self.rect.width / 2
        self.move_count += 1
        if (self.move_count % self.move_freq == 0):
            self.x = self.init_x + self.speed_x * randint(-limit, limit)
            self.y = self.y + self.speed_y
            self.rect.centerx = int(self.x)
            self.rect.top = int(self.y)
