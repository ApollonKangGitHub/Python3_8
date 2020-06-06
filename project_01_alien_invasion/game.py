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
#飞船绘制、飞船发射处理、与屏幕更新
#-----------------------------------------------------------------------
def update_screen(screen, settings, ship):
    #屏幕背景色颜色绘制
    surface.surface_screen_color_draw(screen, settings.screen_color)
    #更新飞船坐标更信息
    ship.update()
    #绘制飞船到screen
    ship.blitme()
    #新增子弹发射（屏幕新增子弹判断处理）
    ship.bullet_fire(screen, settings)
    #子弹状态更新（超出屏幕销毁，否则绘制到screen）
    ship.bullet_update()
    #创建外星人，绘制外星人（外星人绘制覆盖在子弹上面）
    alien = Alien(settings.alien, screen)
    alien.__blitme__()
    #绘制最新屏幕（刷新）
    pygame.display.flip()
