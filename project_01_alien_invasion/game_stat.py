# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月7日13:44:28
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :游戏相关统计信息的类
#    FileName       :game_stat.py
#***********************************************************************
class GameStats():
    def __init__(self, settings):
        self.game_attr = settings.game
        self.ships_limit = self.game_attr["ship_limit"]
        self.get_away_limit = self.game_attr["get_away_limit"]
        self.game_score_highest = 0
        
        self.___reset_game_status__()
        
    def ___reset_game_status__(self):
        self.ships_death = 0
        self.alien_get_away_count = 0
        self.game_over = True
        self.game_stop = False        #暂停（按钮为s）
        self.game_score = 0
        self.kill_cnt = 0
        return True
    
    #根据杀死外星人时的坐标计算不同分数
    def __kill_scoret_cnt__(self, posy=0):
        self.kill_cnt += 1
        self.game_score += (1 * int(posy))
        if self.game_score_highest < self.game_score:
            self.game_score_highest = self.game_score
