# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月14日14:03:54
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :数据可视化随机漫步类
#    FileName       :random_walk.py
#***********************************************************************

from random import choice

#一个生成随机漫步数据的类
class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_pos = [0]
        self.y_pos = [0]
        
    def modify_num_points(self, num_points):
        if num_points < self.num_points:
            for pointIdx in range(num_points, self.num_points-1):
                del self.x_pos[pointIdx]
                del self.y_pos[pointIdx]
        self.num_points = num_points
        
    def fill_walk(self):
        while len(self.x_pos) < self.num_points:
            x_dir = choice([1,-1])
            x_dis = choice([0,1,2,3,4,])
            x_step = x_dir * x_dis
            
            y_dir = choice([1,-1])
            y_dis = choice([0,1,2,3,4,])
            y_step = y_dir * y_dis            

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #根据最后一个点计算下一个点的位置
            next_x = self.x_pos[-1] + x_step
            next_y = self.y_pos[-1] + y_step
            
            self.x_pos.append(next_x)
            self.y_pos.append(next_y)
    
    def clear_walk(self):
        while len(self.x_pos) > 1:
            del self.x_pos[-1]
            del self.y_pos[-1]
