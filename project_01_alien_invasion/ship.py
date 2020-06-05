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

class Ship():
	#初始化飞船并设置初始位置
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		
		#加载飞船图像，并获取其位置范围（外接矩形）以及屏幕范围
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#每艘飞船初始化位置（屏幕中央）
		self.rect.centerx = self.screen_rect.centerx 	#屏幕中间
		self.rect.bottom = self.screen_rect.bottom		#屏幕底部
		
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
		
		print("ship half_width :" + str(self.half_width))
		print("ship half_height:" + str(self.half_height))
		print("ship left       :" + str(self.rect.left))
		print("ship right      :" + str(self.rect.right))	
		print("ship top        :" + str(self.rect.top))
		print("ship bottom     :" + str(self.rect.bottom))
		print("ship centerx    :" + str(self.rect.centerx))
		print("ship centery    :" + str(self.rect.centery))
		print("screen left     :" + str(self.screen_rect.left))
		print("screen right    :" + str(self.screen_rect.right))	
		print("screen top      :" + str(self.screen_rect.top))
		print("screen bottom   :" + str(self.screen_rect.bottom))
		print("screen centerx  :" + str(self.screen_rect.centerx))
		print("screen centery  :" + str(self.screen_rect.centery))
		
	#绘制飞船
	def __blitme__(self):
		self.screen.blit(self.image, self.rect)
	
	#飞船移动
	def __move__(self, left=False, right=False, up=False, down=False):
		self.move_left = left
		self.move_right = right
		self.move_up = up
		self.move_down = down

	#飞船移动更新
	def __update__(self):
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

