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
#
#优化点：
#    根据pygame.mixer进行音效添加处理（爆炸、暴击、射击、背景音乐、结束音等）
#    另外可以给飞船和外星人设置血条，并给外星人设置攻击功能等，哥哥方面都可以优化
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
from score_board import ScoreBoard
from surface import surface_screen_color_draw
from button import Button

#-----------------------------------------------------------------------
#得分等一些显示信息处理
#-----------------------------------------------------------------------
def score_board_draw(score):
    #更新积分牌和最高分牌
    score.__prep_score__()
    score.__draw_score__()
    score.__prep_high_score__()
    score.__draw_high_score__()
    score.__prep_ships__()
    score.__draw_ships__()
    
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

    #初始化游戏状态
    status = GameStats(settings)
    game.game_init_deal(status, settings)
    new_ship = game.create_new_ship(screen, settings)
    
    #创建PLAY按钮
    button_attr = settings.button
    button_attr["text_msg"] = "PLAY"
    play_bubtton = Button(screen, button_attr)
    
    #STOP提示栏
    button_attr["text_msg"] = "STOP"
    stop_bubtton = Button(screen, button_attr)
        
    #计分板
    score = ScoreBoard(screen, settings, status)
    
    #游戏主循环
    while True:
        #屏幕背景色颜色绘制
        screen_attr = settings.screen.copy() 
        surface_screen_color_draw(screen, screen_attr["color"])

        #处理pygame系统事件
        game.event_traverl_deal(settings, \
            screen, new_ship, play_bubtton, status)
        
        #暂停（提示，按钮不可按）
        if status.game_stop:
            stop_bubtton.__draw__()
            score_board_draw(score)
            pygame.display.flip()
            continue
        
        if not status.game_over:
            #处理外星人、子弹、飞船在屏幕中的位置以及相关逻辑
            game.update_game_status(screen, settings, new_ship, status)
        
        #游戏结束则绘制按钮并处理一些统计信息等数据
        game.game_over_check(status, new_ship, play_bubtton, settings)
        
        #绘制最新屏幕（刷新）
        score_board_draw(score)
        pygame.display.flip()

#启动游戏
aline_invasion_game_handle()
