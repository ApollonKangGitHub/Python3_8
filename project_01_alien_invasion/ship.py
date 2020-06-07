# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月2日22:09:29
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :飞船类
#    FileName       :ship.py
#***********************************************************************

#导出pygame模块
import pygame
from bullet import Bullet

class Ship():
    #初始化飞船并设置初始位置
    def __init__(self, settings, screen, groups):
        self.screen = screen
        self.ship_attr = settings.ship
        self.bullet_attr = settings.bullet
        
        #开火状态、弹药统计、发射频率等参数
        if 1 > self.bullet_attr["interval"]:
            interval = 1
        else :        
            interval = self.bullet_attr["interval"] 
        
        #多个发射器组的子弹库信息
        self.bullets_group = []
        for bulltes in groups:
            bulltes_tmp = {
                "bullets":bulltes,
                "fire_status":False,        #请求发射状态
                "fire_sleep":False,         #发射间隔状态
                "fire_count":0,             #请求发射次数
                "interval":interval,        #发射周期
                "bullet_max":self.bullet_attr["limit"],
            }
            self.bullets_group.append(bulltes_tmp)

        self.__ship_reset__()
    
    def __ship_reset__(self):
       #加载飞船图像，并获取其位置范围（外接矩形）以及屏幕范围
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #每艘飞船初始化位置（屏幕底部中央）
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
                
        #飞船位置为小数值
        self.posx = float(self.rect.centerx)
        self.posy = float(self.rect.bottom)

        #飞机半宽和半高(速率过高时会用到)
        self.half_width = self.rect.width / 2
        self.half_height = self.rect.height / 2
                
        #杀死外星人统计、武器强化标记、强化剩余时间
        self.kill_count = 0
        self.intensify = False
        self.intens_time = 0
        
        #可移动标志
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
    #-------------------------------------------------------------------
    #飞船绘制
    #-------------------------------------------------------------------
    def __blitme__(self):
        self.screen.blit(self.image, self.rect)
    
    #-------------------------------------------------------------------
    #飞船移动状态更新
    #-------------------------------------------------------------------
    def __move__(self, left=False, right=False, up=False, down=False):
        self.move_left = left
        self.move_right = right
        self.move_up = up
        self.move_down = down

    #-------------------------------------------------------------------
    #飞船移动状态处理(父类函数复写)
    #-------------------------------------------------------------------
    def update(self):
        if self.move_left \
        and self.rect.left > 0:
            self.posx -= self.ship_attr["speed"]

        elif self.move_up \
        and self.rect.top > 0:
            self.posy -= self.ship_attr["speed"]
            
        elif self.move_right \
        and self.rect.right < self.screen_rect.right:
            self.posx += self.ship_attr["speed"]
                    
        elif self.move_down \
        and self.rect.bottom < self.screen_rect.bottom:
            self.posy += self.ship_attr["speed"]
        
        self.rect.centerx = self.posx
        self.rect.bottom = self.posy
    
    #-------------------------------------------------------------------
    #飞船开火状态设置
    #-------------------------------------------------------------------
    def __fire__(self, bullets, status=False):
        bullets["fire_status"] = status
    
    #-------------------------------------------------------------------
    #根据飞船开火周期和弹药库容量获取实际发射状态
    #-------------------------------------------------------------------
    def __fire_status__(self, bullets):
        #一个bullets发射器，在space按下interval次发射一枚子弹
        if bullets["fire_count"] % bullets["interval"] == 0:
            bullets["fire_sleep"] = False
        else:
            bullets["fire_sleep"] = True
        bullets["fire_count"] += 1
        
        #发射间隔期间不发射
        if bullets["fire_sleep"]:
            return False
        #如果弹药库还有余量则继续发射
        elif len(bullets["bullets"]) < bullets["bullet_max"]:
            return bullets["fire_status"]
        #弹药库无余量
        else:
            return False

    #-------------------------------------------------------------------
    #飞船弹药库子弹统计
    #-------------------------------------------------------------------
    def __kill_object_cnt__(self, count=0):
        self.kill_count += count
        cycle = self.ship_attr["intensify_cycle"]
        if (self.kill_count > 0) and (self.kill_count % cycle == 0):
            self.intensify = True
            self.intens_time = 20
            
    #-------------------------------------------------------------------
    #强化标志获取
    #-------------------------------------------------------------------
    def __is_intensify__(self):
        if self.intensify:
            if self.intens_time > 0:
                self.intens_time -= 1
            else:
                self.intensify = False
                self.intens_time = 0
        
        #print("kill_count  = " + str(self.kill_count))
        #print("intensify   = " + str(self.intensify))
        #print("intens_time = " + str(self.intens_time))
        #print("------------------------------------------")
        return self.intensify

