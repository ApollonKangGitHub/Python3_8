# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月7日19:38:54
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :记分牌类
#    FileName       :score_board.py
#***********************************************************************

import pygame
from pygame.sprite import Group

from ship import Ship
from surface import surface_color_convert as color_convert

class ScoreBoard():
    def __init__(self, screen, settings, status):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score_board = settings.score_board
        self.settings = settings
        self.status = status
        
        self.bg_color = color_convert(self.score_board["background_color"])
        self.text_color = color_convert(self.score_board["text_color"])
        self.text_size = self.score_board["text_size"]
        self.font = pygame.font.SysFont(None, self.text_size)
        
        #准备初始得分图像
        self.__prep_score__()
        self.__prep_high_score__()
        
    #构造得分图像
    def __prep_score__(self):
        score_str = "score:"
        score_str += str(self.status.game_score)
        self.score_image = self.font.render( \
            score_str, True, self.text_color, self.bg_color)
        
        #得分显示在右上方
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 20 + self.text_size
    
    #构造最高得分图像    
    def __prep_high_score__(self):
        score_highest_str = "highest score:"
        score_highest_str += str(self.status.game_score_highest)
        self.score_highest_image = self.font.render( \
            score_highest_str, True, self.text_color, self.bg_color)
            
        #得分显示在右上方
        self.score_highest_rect = self.score_highest_image.get_rect()
        self.score_highest_rect.right = self.screen_rect.right - 20
        self.score_highest_rect.top = self.screen_rect.top + 20
              
    #构造飞船余量图像
    def __prep_ships__(self):  
        self.ships = Group()
        ship_num = self.status.ships_limit - self.status.ships_death
        for ship_num in range(0, ship_num):
            groups = []
            new_ship = Ship(self.settings, self.screen, groups)
            new_ship.rect.x = 10 + ship_num * new_ship.rect.width
            new_ship.rect.y = 10
            self.ships.add(new_ship)

    #绘制的分到screen 
    def __draw_score__(self):
        self.screen.blit(self.score_image, self.score_rect)

    #绘制最高得分到screen
    def __draw_high_score__(self):
        self.screen.blit(self.score_highest_image, self.score_highest_rect)

    #绘制飞船余量到screen
    def __draw_ships__(self):
        self.ships.draw(self.screen) 
