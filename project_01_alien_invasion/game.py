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

import sys
import surface
import pygame

#-----------------------------------------------------------------------
#事件遍历与处理
#-----------------------------------------------------------------------
def event_traverl_deal(ship):
	#遍历pygame事件，处理事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#按下根据按下具体键值更新移动标志
		elif event.type == pygame.KEYDOWN:
			#print(event.key)
			if event.key == pygame.K_LEFT:
				ship.__move__(left=True)
			elif event.key == pygame.K_RIGHT:
				ship.__move__(right=True)
			elif event.key == pygame.K_UP:
				ship.__move__(up=True)
			elif event.key == pygame.K_DOWN:
				ship.__move__(down=True)
		#松开，更新所有移动标志位False
		elif event.type == pygame.KEYUP:
				ship.__move__()			

#-----------------------------------------------------------------------
#飞船绘制与屏幕更新
#-----------------------------------------------------------------------
def update_screen_ship(screen, screen_color, ship):
	#屏幕背景色颜色绘制
	surface.surface_screen_color_draw(screen, screen_color)
	#绘制飞船到screen
	ship.__blitme__()
	#绘制最新屏幕（刷新）
	pygame.display.flip()
		
