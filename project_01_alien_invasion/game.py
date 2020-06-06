# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020-6-2 22:25:58
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :事件处理、屏幕处理等函数模块
#    FileName       :game.py
#***********************************************************************
from pygame.sprite import Group
import sys
import bullet

#自定义模块
import surface
import pygame
import ship
from bullet import Bullet
from alien import Alien

global g_aliens
g_aliens = Group()
#-----------------------------------------------------------------------
#按键按下处理
#-----------------------------------------------------------------------
def event_keydown_check(event, ship, screen):
    if event.key == pygame.K_LEFT:
        ship.move(left=True)
    elif event.key == pygame.K_RIGHT:
        ship.move(right=True)
    elif event.key == pygame.K_UP:
        ship.move(up=True)
    elif event.key == pygame.K_DOWN:
        ship.move(down=True)
    elif event.key == pygame.K_SPACE:
        for bullets in ship.bullets_group:
            ship.__fire__(bullets, True) 
    elif event.key == pygame.K_q:
        sys.exit()      
#-----------------------------------------------------------------------
#按键松开处理
#-----------------------------------------------------------------------
def event_keyup_check(event, ship, screen):
    if event.key == pygame.K_LEFT:
        ship.move(left=False)
    elif event.key == pygame.K_RIGHT:
        ship.move(right=False)
    elif event.key == pygame.K_UP:
        ship.move(up=False)
    elif event.key == pygame.K_DOWN:
        ship.move(down=False)
    elif event.key == pygame.K_SPACE:
        for bullets in ship.bullets_group:
            ship.__fire__(bullets, False)         

#-----------------------------------------------------------------------
#事件遍历与处理
#-----------------------------------------------------------------------
def event_traverl_deal(screen, ship):
    #遍历pygame事件，处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #按下根据按下具体键值更新移动标志
        elif event.type == pygame.KEYDOWN:
            event_keydown_check(event, ship, screen)
        #按下根据按下具体键值更新移动标志
        elif event.type == pygame.KEYUP:
            event_keyup_check(event, ship, screen)
            
#-----------------------------------------------------------------------
#外星人群创建
#-----------------------------------------------------------------------
def create_aliens(screen, aliens, screen_attr, alien_attr):
    if len(aliens) == 0:
        #生成临时外星人，让获取外星人width和height
        alien = Alien(alien_attr, screen)
        width = alien.rect.width
        height = alien.rect.height
        
        #根据屏幕大小和外星人大小计算可容纳的合适的外星人个数
        col_num = int(screen_attr["width"] / (width * 2))   #列数
        row_num = int(screen_attr["height"] / (height * 2)) #行数

        #创建外星人并加入到aliens的外星人组中去
        for col_idx in range(0,col_num):
            for row_idx in range(0,row_num):
                alien_attr["pos_x"] = float((2 * col_idx + 1) * width)
                alien_attr["pos_y"] = float((row_idx + 1) * height)
                new_alien = Alien(alien_attr, screen)
                aliens.add(new_alien)

        #删除临时的外星人
        del alien
        
#-----------------------------------------------------------------------
#外星人移动和在屏幕上绘制
#-----------------------------------------------------------------------
def updata_aliens(aliens, bullets_group, screen):
    for alien in aliens.sprites():
        alien.__move__()
        alien.__blitme__()
        
#-----------------------------------------------------------------------
#飞船绘制、飞船发射处理、与屏幕更新
#-----------------------------------------------------------------------
def update_screen(screen, settings, ship):
    global g_aliens
    
    #注意：用副本（但也只是一级深拷贝，对于二级依旧是引用）
    screen_attr = settings.screen.copy()
    alien_attr = settings.alien.copy()
    bullet_attr = settings.bullet.copy()
    
    #屏幕背景色颜色绘制
    surface.surface_screen_color_draw(screen, screen_attr["color"])
    
    #更新飞船坐标更信息
    ship.update()
    #绘制飞船到screen
    ship.blitme()
    
    #新增子弹发射（屏幕新增子弹判断处理）
    ship.bullet_fire(screen, bullet_attr)
    #子弹状态更新（超出屏幕销毁，否则绘制到screen）
    ship.bullet_update()
    
    #创建外星人
    create_aliens(screen, g_aliens, screen_attr, alien_attr)
    #外星人状态更新（移动、判断状态、外星人绘制到screen覆盖在子弹上面）
    updata_aliens(g_aliens, ship.bullets_group, screen)
    
    #绘制最新屏幕（刷新）
    pygame.display.flip()
