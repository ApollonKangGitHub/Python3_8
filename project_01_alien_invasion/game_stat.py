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
        self.___reset_game_status__()

    def ___reset_game_status__(self):
        self.ships_death = 0
        self.alien_get_away_count = 0
        self.game_over = True
        self.game_stop = False        #暂停（按钮为s）
        return True
