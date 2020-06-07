# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月7日15:02:55
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :按钮相关类
#    FileName       :button.py
#***********************************************************************

import pygame
from surface import surface_color_convert as color_convert

class Button():
    def __init__(self, screen, button_attr):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.attr = button_attr
        
        #设置按钮尺寸和其他属性
        self.width = self.attr["button_width"]
        self.height = self.attr["button_height"]
        self.button_color = color_convert(self.attr["button_color"])
        self.text_color = color_convert(self.attr["text_color"])
        self.text_msg = self.attr["text_msg"]
        self.font = pygame.font.SysFont(None, self.attr["text_size"])
        
        #创建按钮surface对象，使其居中
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #按钮标签只创建一次
        self.prep_msg__(self.text_msg)

    #字符串文本渲染为图像进行处理
    def prep_msg__(self, msg):
        self.msg_image = self.font.render(msg, \
            True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #绘制button
    def __draw__(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
