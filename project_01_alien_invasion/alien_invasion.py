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
from game_stat import GameStats
from surface import surface_screen_color_draw
from button import Button

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

    status = GameStats(settings)
    new_ship = game.create_new_ship(screen, settings)
    
    #创建PLAY按钮
    button_attr = settings.button
    button_attr["text_msg"] = "PLAY"
    play_bubtton = Button(screen, button_attr)
    
    button_attr["text_msg"] = "STOP"
    stop_bubtton = Button(screen, button_attr)
        
    #游戏主循环
    while True:
        #屏幕背景色颜色绘制
        screen_attr = settings.screen.copy() 
        surface_screen_color_draw(screen, screen_attr["color"])
        
        #处理pygame系统事件
        game.event_traverl_deal(screen, new_ship, play_bubtton, status)
        
        #暂停（提示，按钮不可按）
        if status.game_stop:
            stop_bubtton.__draw__()
            pygame.display.flip()
            continue
        
        if not status.game_over:
            #处理外星人、子弹、飞船在屏幕中的位置以及相关逻辑
            game.update_game_status(screen, settings, new_ship, status)
        
        #游戏结束则绘制按钮并处理一些统计信息等数据
        if status.game_over:
            status.___reset_game_status__()
            new_ship.__ship_reset__()
            play_bubtton.__draw__()
                     
        #绘制最新屏幕（刷新）
        pygame.display.flip()

#启动游戏
aline_invasion_game_handle()
