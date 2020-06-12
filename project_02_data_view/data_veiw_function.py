# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月7日22:55:17
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :数据可视化(简单的函数绘制、格式设置、结果保存)
#    FileName       :data_veiw_function.py
#***********************************************************************

#-----------------------------------------------------------------------
#前期工作：确保python安装、matplotlib安装
#升级pip（不升级也可以，只要确保安装了pip即可）
#    python -m pip install --upgrade pip
#查看version
#    python -m pip --version
#执行下载安装matplotlib模块操作
#    python -m pip install matplotlib
#
#关于matplotlib的使用可参考：
#http://matplotlib.org
#-----------------------------------------------------------------------
from time import sleep
import matplotlib.pyplot as plt
global g_save_path
global g_save_tail
g_save_path = r'./saveFig/'
g_save_tail = '.png'

#-----------------------------------------------------------------------
#图片保存
#-----------------------------------------------------------------------
def save_draw_picture(plt, name):
    global g_save_path
    global g_save_tail
    
    save_path_name = g_save_path + name + g_save_tail
    
    try:
        plt.savefig(save_path_name)
    except:
        print("save " + save_path_name + " falied!!")
        
#-----------------------------------------------------------------------
#划线 matplotlib.pyplot.plot([x_list], <y_list>, [linewidth], [c])
#-----------------------------------------------------------------------
x_range = list(range(-100,100))
y_range = [pow(value,3) for value in x_range]

#绘制线
plt.plot(x_range, y_range, linewidth=2, c='green')
plt.title("function calc")
plt.xlabel("x∈[-10,10]", fontsize=14)
plt.ylabel("y=x^3 - 2x^2", fontsize=14)
plt.tick_params(axis='both', labelsize=10)

#设置坐标范围
plt.axis([-100, 100, -1000000, 1000000])
#保存绘制结果(注意：绘制要在show之前，否则保存的会是一张空白图片)
save_draw_picture(plt, "plot")
#display绘制结果
plt.show()

#-----------------------------------------------------------------------
#划点 matplotlib.pyplot.scatter(<x|x_list>, <y|y_list>, [s], [c|c_list])
#注意：c 参数 可以直接指定颜色名字，也可以指定颜色的rgb值，(r,g,b),但是这里的r、g、b
#范围为[0,1]，值越大表示颜色越深，值越小表示颜色越浅，c可以是一个值页可以是列表
#-----------------------------------------------------------------------
x_range = list(range(-20,20,1))
y_range = [(value**3) for value in x_range]
color = []
for index in range(-20,20):
    if index < 0:
        c=(1, 0, 0)
    elif index > 0:
        c=(0, 1, 0)
    else:
        c=(0, 0, 1)
    color.append(c)
    
#绘制点
plt.scatter(x_range, y_range, c=color, s=10)
plt.title("function calc")
plt.xlabel("x∈[-10,10]", fontsize=20)
plt.ylabel("y=x^3 - 2x^2", fontsize=20)
plt.tick_params(axis='both', labelsize=20)

#设置坐标范围
plt.axis([-20, 20, -8000, 8000])
plt.show()

#-----------------------------------------------------------------------
#plt数据重复使用
#-----------------------------------------------------------------------
for size in range(10,100,20):
    plt.scatter(x_range, y_range, c=color, s=size)
    save_draw_picture(plt, "scatter_size_" + str(size))

#-----------------------------------------------------------------------
#颜色映射
#c=y_range, cmap=plt.cm.Reds
#指定c参数根据y_range从小到大，颜色从浅红色到深红色递增
#-----------------------------------------------------------------------
plt.scatter(x_range, y_range, c=y_range, cmap=plt.cm.Reds, s=200)
save_draw_picture(plt, "scatter_cmap")
plt.show()
