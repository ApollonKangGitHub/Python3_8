# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月1日22:59:07
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :set功能的类，增加set功能，直接对set类增加函数
#    FileName       :setting.py
#***********************************************************************
class Setting():
	def __init__(self):
		#屏幕设置
		self.screen_width = 800
		self.screen_high = 500
		self.screen_color = "灰色"
		
		#飞船速率
		self.ship_speed = 2.5
		
	def get_screen_size(self):
		return (self.screen_width, self.screen_high)
	
	def get_screen_color(self):
		return self.screen_color
