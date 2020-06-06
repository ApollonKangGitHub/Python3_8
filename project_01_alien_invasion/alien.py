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
from surface import g_screen_color_dict as color
from pygame.sprite import Sprite

class Alien(Sprite):
    #外星人初始化
    def __init__(self, alien, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r"images\alien.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.height = self.rect.height
        self.x = float(self.rect.x)
        self.height = float(self.rect.height)
        
    #绘制外星人
    def __blitme__(self):
        self.screen.blit(self.image, self.rect)
