# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月1日20:06:13
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :偶遇外星人主要初始化逻辑和主循环
#    FileName       :alien_invasion.py
#***********************************************************************

#-----------------------------------------------------------------------
#前期工作：确保python安装、pygame安装
#升级pip（不升级也可以，只要确保安装了pip即可）
#    python -m pip install --upgrade pip
#查看version
#    python -m pip --version
#执行下载安装pygame模块操作
#    python -m pip install pygame
#-----------------------------------------------------------------------

#系统/标准模块导出
import time
import pygame
from pygame.sprite import Group

#自定义模块、类、函数导出
import ship
import game
from setting import Setting

#弹药库
global bullets_group
bullets_group = []

#-----------------------------------------------------------------------
#游戏初始化和处理主逻辑
#-----------------------------------------------------------------------
def aline_invasion_game_handle():
    #创建默认设置对象（获取默认设置参数）
    settings = Setting()
    screen_size = settings.get_screen_size()
    
    #初始化pygame模块、创建一个屏幕对象、设置标题栏标题
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("疯狂外星人")

    #弹药库创建（可根据游戏难度，修改弹药库个数）
    for index in range(0, settings.ship_bullets_group_num):
        bullets_group.append(Group())

    #在screen上创建一个飞船
    new_ship = ship.Ship(settings, screen, bullets_group)

    #游戏主循环
    while True:
        #处理pygame系统事件
        game.event_traverl_deal(screen, new_ship)

        #处理屏幕与飞船绘制
        game.update_screen(screen, settings, new_ship)
#启动游戏
aline_invasion_game_handle()
