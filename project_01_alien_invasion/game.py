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
import pygame
import sys
import bullet
from pygame.sprite import Group
from time import sleep

#自定义模块
import ship
from bullet import Bullet
from alien import Alien

#弹药库和外星人列表
global bullets_group
global g_aliens
global g_mouse_play_down
g_mouse_play_down = False
bullets_group = []
g_aliens = Group()

#-----------------------------------------------------------------------
#按键按下处理
#-----------------------------------------------------------------------
def event_keydown_check(event, ship, screen, game_status):
    if event.key == pygame.K_LEFT:
        ship.__move__(left=True)
    elif event.key == pygame.K_RIGHT:
        ship.__move__(right=True)
    elif event.key == pygame.K_UP:
        ship.__move__(up=True)
    elif event.key == pygame.K_DOWN:
        ship.__move__(down=True)
    elif event.key == pygame.K_SPACE:
        for bullets in ship.bullets_group:
            ship.__fire__(bullets, True) 
    elif event.key == pygame.K_q:
        sys.exit()   
    elif event.key == pygame.K_s:
        game_status.game_stop = not game_status.game_stop
#-----------------------------------------------------------------------
#按键松开处理
#-----------------------------------------------------------------------
def event_keyup_check(event, ship, screen):
    if event.key == pygame.K_LEFT:
        ship.__move__(left=False)
    elif event.key == pygame.K_RIGHT:
        ship.__move__(right=False)
    elif event.key == pygame.K_UP:
        ship.__move__(up=False)
    elif event.key == pygame.K_DOWN:
        ship.__move__(down=False)
    elif event.key == pygame.K_SPACE:
        for bullets in ship.bullets_group:
            ship.__fire__(bullets, False)         
#-----------------------------------------------------------------------
#事件遍历与处理
#-----------------------------------------------------------------------
def check_mouse_down_pos(status, button, pos_x, pos_y):
    if button.rect.collidepoint(pos_x, pos_y):
        global g_mouse_play_down
        if status.game_over:
            g_mouse_play_down = True

#-----------------------------------------------------------------------
#事件遍历与处理
#-----------------------------------------------------------------------
def event_traverl_deal(screen, ship, button, status):
    #遍历pygame事件，处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #按下根据按下具体键值更新移动标志
        elif event.type == pygame.KEYDOWN:
            event_keydown_check(event, ship, screen, status)
        #按下根据按下具体键值更新移动标志
        elif event.type == pygame.KEYUP:
            event_keyup_check(event, ship, screen)
        #鼠标点下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x ,mouse_y = pygame.mouse.get_pos()
            check_mouse_down_pos(status, button, mouse_x, mouse_y) 
        #鼠标松开
        elif event.type == pygame.MOUSEBUTTONUP:
            global g_mouse_play_down
            if g_mouse_play_down:
                g_mouse_play_down = False
                status.game_over = False
#-------------------------------------------------------------------
#新飞船创建
#-------------------------------------------------------------------
def create_new_ship(screen, settings):
    #弹药库创建（可根据游戏难度，修改弹药库个数）
    for index in range(0, settings.ship["bullets_group"]):
        bullets_group.append(Group())

    #在screen上创建一个飞船
    new_ship = ship.Ship(settings, screen, bullets_group)
    return new_ship

#-------------------------------------------------------------------
#飞船弹药库子弹发射
#-------------------------------------------------------------------
def bullet_fire(ship, screen, bullet_attr):
    #遍历每个发射器
    group = ship.bullets_group
    for group_idx in range(0, len(group)):
        bullets = group[group_idx]
        #根据子弹库的弹药发射周期进行每个弹药库子弹位置计算和添加
        if ship.__fire_status__(bullets):
            #注意：用副本（防止数据修改对其他子弹始化情况有影响）
            bullet = bullet_attr.copy()
            if (len(group) % 2 == 1) and (group_idx == 0):
                delta = 0
            elif group_idx % 2 == 0:
                delta = -bullet["pos_diff"]
            else:
                delta = bullet["pos_diff"]
            
            bullet["pos_diff"] = delta * (group_idx / 2 + 1)
            
            #创建新子弹，并将新子弹放进对应子弹库
            new_bullet = Bullet(bullet, screen, ship)
            
            #如果飞船强化器到来，则强化子弹
            if ship.__is_intensify__():
                bullet = new_bullet.__bullet_intensify__()
                new_bullet.__modify_bullet_attr__(ship, bullet)
            bullets["bullets"].add(new_bullet)
            
#-------------------------------------------------------------------
#飞船发射器弹药库子弹更新（删除）和绘制
#-------------------------------------------------------------------
def bullet_update(ship):
    #遍历每个发射器
    group = ship.bullets_group
    for bullets in group:   
        #更新子弹位置信息：子弹类要覆写pygame.sprite父类的update函数
        bullets["bullets"].update()
        #绘制子弹到screen
        for bullet in bullets["bullets"].sprites():
            #销毁离开屏幕的子弹
            if bullet.__need_destroy__():
                bullets["bullets"].remove(bullet)
            bullet.__draw__()
            
#-------------------------------------------------------------------
#检查飞船离开屏幕则销毁飞船(并统计逃离的外星人个数，超过指定个数则游戏结束)
#-------------------------------------------------------------------
def check_aliens_leave_screen(aliens, screen, game_status):
    screen_rect = screen.get_rect()
    limit = game_status.get_away_limit
    for alien in aliens:
        if alien.rect.top >= screen_rect.bottom:
            game_status.alien_get_away_count += 1
            aliens.remove(alien)
            if limit <= game_status.alien_get_away_count:
                game_status.game_over = True
            
#-----------------------------------------------------------------------
#外星人群创建
#-----------------------------------------------------------------------
def create_aliens(screen, aliens, screen_attr, alien_attr):
    if len(aliens) == 0:
        #生成临时外星人，让获取外星人width和height
        alien = Alien(alien_attr, screen)
        width = alien.rect.width
        height = alien.rect.height
        
        #根据屏幕大小和外星人大小计算可容纳的合适的外星人个数
        col_num = int(screen_attr["width"] / (width * 2))   #列数
        row_num = int(screen_attr["height"] / (height * 2)) #行数

        #创建外星人并加入到aliens的外星人组中去
        for col_idx in range(0,col_num):
            for row_idx in range(0,row_num):
                alien_attr["pos_x"] = float((2 * col_idx + 1) * width)
                alien_attr["pos_y"] = float((row_idx + 1) * height)
                new_alien = Alien(alien_attr, screen)
                aliens.add(new_alien)

        #删除临时的外星人
        del alien
        
#-----------------------------------------------------------------------
#外星人移动和在屏幕上绘制
#-----------------------------------------------------------------------
def updata_aliens(aliens, screen):
    for alien in aliens.sprites():
        alien.__move__()
        alien.__blitme__()

#-----------------------------------------------------------------------
#飞船与外星人相撞
#-----------------------------------------------------------------------      
def ship_hit_handle(settings, game_status, screen, ship, aliens):
    game_status.ships_death += 1
    print("@@death:" + str(game_status.ships_death))
    if game_status.ships_limit >= game_status.ships_death:
        print("##death:" + str(game_status.ships_death))
        #清空子弹
        for bullets in ship.bullets_group:
            bullets["bullets"].empty()
            
        #清空外星人
        aliens.empty()
        
        #飞船恢复中间位置
        ship.__ship_reset__()
        sleep(0.5)
    else:
        game_status.game_over = True
        
#-----------------------------------------------------------------------
#处理外星人、子弹、飞船在屏幕中的位置以及相关逻辑
#-----------------------------------------------------------------------
def update_game_status(screen, settings, ship, game_status):
    global g_aliens
    
    #注意：用副本（但也只是一级深拷贝，对于二级依旧是引用）
    screen_attr = settings.screen.copy()
    alien_attr = settings.alien.copy()
    bullet_attr = settings.bullet.copy()

    #更新飞船坐标更信息
    ship.update()
    #绘制飞船到screen
    ship.__blitme__()
    
    #新增子弹发射（屏幕新增子弹判断处理）
    bullet_fire(ship, screen, bullet_attr)
    #子弹状态更新（超出屏幕销毁，否则绘制到screen）
    bullet_update(ship)
    
    #外星人和子弹相撞检测（返回子弹和外星人相撞的字典，清除子弹，清除外星人）
    for bullets in ship.bullets_group:
        collisions = pygame.sprite.groupcollide( \
            bullets["bullets"], g_aliens, True, True)
        #杀死外星人统计
        ship.__kill_object_cnt__(len(collisions))
        
    #创建外星人
    create_aliens(screen, g_aliens, screen_attr, alien_attr)
    #外星人状态更新（移动、判断状态、外星人绘制到screen覆盖在子弹上面）
    updata_aliens(g_aliens, screen)
    
    #检测外星人和飞船之间是否碰撞,发现一个alien和ship像素有重合
    #则停止遍历返回True,否则遍历完成返回False
    if pygame.sprite.spritecollideany(ship, g_aliens):
        ship_hit_handle(settings, game_status, screen, ship, g_aliens)

    #检查外星人是否撞到屏幕底部
    check_aliens_leave_screen(g_aliens, screen, game_status)
