# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月14日14:03:54
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :数据可视化随机漫步
#    FileName       :data_veiw_random.py
#***********************************************************************

from matplotlib import pyplot as plt
from random_walk import RandomWalk

global g_save_path
global g_save_tail
g_save_path = r'./saveFig/randWalk/'
g_save_tail = '.png'

#-----------------------------------------------------------------------
#图片保存
#-----------------------------------------------------------------------
def save_draw_picture(plt, name):
    global g_save_path
    global g_save_tail
    
    save_path_name = g_save_path + name + g_save_tail
    
    try:
        #bbox_inches='tight'裁剪掉多余的白边框
        plt.savefig(save_path_name, bbox_inches='tight')
    except:
        print("save " + save_path_name + " falied!!")

def rand_walk_scatter(range_list, rw, subplot, index):
    #以point_num_list即以[x_pos,y_pos]产生的先后顺序关系映射colormap
    subplot.scatter(rw.x_pos, rw.y_pos, s=1, c=range_list, cmap=plt.cm.Greens)
    subplot.set_title("colormap with random walk test " + str(index)
                        + ", point num:" + str(rw.num_points))
    subplot.set_xlabel("x_pos", fontsize=14)
    subplot.set_ylabel("y_pos", fontsize=14)
    
    #重新绘制终点和起点以突出显示
    subplot.scatter(rw.x_pos[0], rw.y_pos[0], s=50, c='blue')
    subplot.scatter(rw.x_pos[-1], rw.y_pos[-1], s=50, c='red')

    #隐藏坐标轴
    subplot.get_xaxis().set_visible(False)
    subplot.get_yaxis().set_visible(False)   
    
def rand_walk_x_plot(range_list, x_pos, subplot, index):
    subplot.plot(range_list, x_pos, linewidth=1, c='red')
    subplot.set_title("x_pos range change picture " + str(index))
    subplot.set_xlabel("range_list", fontsize=14)
    subplot.set_ylabel("x_pos", fontsize=14)
    
def rand_walk_y_plot(range_list, y_pos, subplot, index):
    subplot.plot(range_list, y_pos, linewidth=1, c='blue')
    subplot.set_title("y_pos range change picture " + str(index))
    subplot.set_xlabel("range_list", fontsize=14)
    subplot.set_ylabel("y_pos", fontsize=14)
        
def rand_walk_test():
    index = 0
    num_points = 100
    rw = RandomWalk(num_points)

    while True:
        index += 1
        num_points *= 2
        
        #清空数据、填充数据
        rw.modify_num_points(num_points)
        rw.clear_walk()
        rw.fill_walk()
        
        point_list = list(range(rw.num_points))
    
        #绘制窗口尺寸创建subplot，数据点过多时，使用dpi指定每英寸像素点个数
        fig = plt.figure(dpi=154, figsize=(20,12))
        
        #'111'表示'1×1网格，第一子图'，'122'表示'1x2网格，第二子图'
        sub_211 = fig.add_subplot(211)
        sub_223 = fig.add_subplot(223)
        sub_224 = fig.add_subplot(224)
        
        #散点图
        rand_walk_scatter(point_list, rw, sub_211, index)
        #x坐标变化
        rand_walk_x_plot(point_list, rw.x_pos, sub_223, index)
        #y坐标变化
        rand_walk_y_plot(point_list, rw.y_pos, sub_224, index)
        
        #保存图片、屏幕绘制图片             
        save_draw_picture(plt, "rand_walk_colormap_" + str(index))
        plt.show()
        
        keep_walk = input("continue walking(Y/N):")
        if keep_walk == 'N':
            break
        else:
            continue
    
rand_walk_test()
