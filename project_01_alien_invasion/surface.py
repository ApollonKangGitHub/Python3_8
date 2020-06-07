# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月1日22:40:39
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :pygame.surface的屏幕操作
#    FileName       :surface.py
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

#导出pygame模块
import pygame

#-----------------------------------------------------------------------
#全局数据定义
#-----------------------------------------------------------------------
#屏幕背景色元组字典
global g_screen_color_dict
#屏幕背景色列表
global g_screen_color_list

g_screen_color_dict = {
    "灰色":(230,    230,    230),
    "红色":(255,      0,      0),
    "绿色":(  0,    255,      0),
    "蓝色":(  0,      0,    255),
    "黄色":(255,    255,      0),
    "紫色":(255,      0,    255),
    "青色":(  0,    255,    255),
    "白色":(255,    255,    255),
    "黑色":(  0,      0,      0),
    "橙色":(255,    150,      0),
    "深灰":(127,    127,    127),
    "黑灰":( 77,     77,     77),
}

g_screen_color_list = [
    "灰色",    "红色",
    "绿色",    "蓝色",
    "黄色",    "紫色",
    "青色",    "黑色",
    "白色",    "橙色",
    "深灰",    "黑灰",
]

#-----------------------------------------------------------------------
#屏幕surface颜色设置，可以指定不同颜色
#-----------------------------------------------------------------------
def surface_screen_color_draw(surface, color =""):
    if type(surface) != pygame.Surface:
        print("无效的surface对象")
        return False
    
    #指定默认颜色
    if not color or color not in g_screen_color_list:
        if len(g_screen_color_list) > 0:
            color = g_screen_color_list[0]
        else:
            return False

    if color in g_screen_color_dict.keys():
        surface.fill(g_screen_color_dict[color])
        return True
    else:
        return False

#-----------------------------------------------------------------------
#根据颜色名字转换RGB元组
#-----------------------------------------------------------------------    
def surface_color_convert(color_description):
    if color_description in g_screen_color_dict.keys():
        return g_screen_color_dict[color_description]
    else:
        return g_screen_color_dict["黑色"]
