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
        self.settings = settings
        
        #加载飞船图像，并获取其位置范围（外接矩形）以及屏幕范围
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #每艘飞船初始化位置（屏幕中央）
        self.rect.centerx = self.screen_rect.centerx     #屏幕中间
        self.rect.bottom = self.screen_rect.bottom       #屏幕底部
         
        #开火状态、弹药统计、发射频率等参数
        if 1 > settings.bullet["interval"]:
            fire_freq = 1
        else :        
            fire_freq = settings.bullet["interval"] 
        
        #多个发射器组的子弹库信息
        self.bullets_group = []
        for bulltes in groups:
            bulltes_tmp = {
                "bullets":bulltes,
                "fire_status":False,        #请求发射状态
                "fire_sleep":False,         #发射间隔状态
                "fire_count":0,             #请求发射次数
                "fire_freq":fire_freq,
                "bullet_cnt":0,             #屏幕上该弹药库现存
                "bullet_max":settings.bullet["limit"],
            }
            self.bullets_group.append(bulltes_tmp)
        
        #可移动标志
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
        #飞机半宽和半高(速率过高时会用到)
        self.half_width = self.rect.width / 2
        self.half_height = self.rect.height / 2
        
        #飞船位置为小数值
        self.posx = float(self.rect.centerx)
        self.posy = float(self.rect.bottom)

    #-------------------------------------------------------------------
    #飞船绘制
    #-------------------------------------------------------------------
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    #-------------------------------------------------------------------
    #飞船移动状态更新
    #-------------------------------------------------------------------
    def move(self, left=False, right=False, up=False, down=False):
        self.move_left = left
        self.move_right = right
        self.move_up = up
        self.move_down = down

    #-------------------------------------------------------------------
    #飞船移动状态处理
    #-------------------------------------------------------------------
    def update(self):
        if self.move_left \
        and self.rect.left > 0:
            self.posx -= self.settings.ship_speed

        elif self.move_up \
        and self.rect.top > 0:
            self.posy -= self.settings.ship_speed
            
        elif self.move_right \
        and self.rect.right < self.screen_rect.right:
            self.posx += self.settings.ship_speed
                    
        elif self.move_down \
        and self.rect.bottom < self.screen_rect.bottom:
            self.posy += self.settings.ship_speed
        
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
        #一个bullets发射器，在space按下fire_freq次发射一枚子弹
        if bullets["fire_count"] % bullets["fire_freq"] == 0:
            bullets["fire_sleep"] = False
        else:
            bullets["fire_sleep"] = True
        bullets["fire_count"] += 1
        
        #发射间隔期间不发射
        if bullets["fire_sleep"]:
            return False
        #如果弹药库还有余量则继续发射
        elif bullets["bullet_cnt"] < bullets["bullet_max"]:
            return bullets["fire_status"]
        #弹药库无余量
        else:
            return False
    #-------------------------------------------------------------------
    #飞船弹药库子弹统计
    #-------------------------------------------------------------------
    def bullet_allowance(self, bullets, count=0):
        bullets["bullet_cnt"] += count

    #-------------------------------------------------------------------
    #飞船弹药库子弹发射
    #-------------------------------------------------------------------
    def bullet_fire(self, screen, bullet_attr):
        #遍历每个发射器
        group = self.bullets_group
        for group_idx in range(0, len(group)):
            bullets = group[group_idx]
            #根据子弹库的弹药发射周期进行每个弹药库子弹位置计算和添加
            if self.__fire_status__(bullets):
                #注意：用副本（防止数据修改对其他子弹始化情况有影响）
                bullet = bullet_attr.copy()
                if (len(group) % 2 == 1) and (group_idx == 0):
                    delta = 0
                elif group_idx % 2 == 0:
                    delta = -bullet["pos_diff"]
                else:
                    delta = bullet["pos_diff"]
                
                bullet["pos_diff"] = delta * (group_idx / 2 + 1)
                
                #创建新子弹，并将新子弹放进对应子弹库
                new_bullet = Bullet(bullet, screen, self)
                bullets["bullets"].add(new_bullet)
                self.bullet_allowance(bullets, 1)
                
    #-------------------------------------------------------------------
    #飞船发射器弹药库子弹更新（删除）和绘制
    #-------------------------------------------------------------------
    def bullet_update(self):
        #遍历每个发射器
        group = self.bullets_group
        for bullets in group:   
            #更新子弹位置信息：子弹类要覆写pygame.sprite父类的update函数
            bullets["bullets"].update()
            #绘制子弹到screen
            for bullet in bullets["bullets"].sprites():
                #销毁离开屏幕的子弹
                if bullet.need_destroy():
                    bullets["bullets"].remove(bullet)
                    self.bullet_allowance(bullets, -1)
                bullet.draw()
