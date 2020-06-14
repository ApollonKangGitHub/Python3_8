# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月14日17:25:36
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :csv数据解析与可视化
#    FileName       :data_veiw_csv.py
#***********************************************************************

from matplotlib import pyplot as plt
from datetime import datetime
import csv

global g_save_path
global g_save_tail
global g_load_path
global g_load_tail
global g_csv_file 

#-----------------------------------------------------------------------
#全局数据定义
#-----------------------------------------------------------------------  
g_save_path = r"./saveFig/csvWeather/"
g_save_tail = '.png'
g_load_path = r'./loadCsv/'
g_load_tail = '.csv'
g_csv_file = [
    {
        "filename"       :'sitka_weather_07-2014',
        "max_temperature":'Max TemperatureF',
        "min_temperature":'Min TemperatureF',
        "date"           :"AKDT",
    },
    {
        "filename"       :'sitka_weather_2014',
        "max_temperature":'Max TemperatureF',
        "min_temperature":'Min TemperatureF',
        "date"           :"AKST",
    },
    {
        "filename"       :'death_valley_2014',
        "max_temperature":'Max TemperatureF',
        "min_temperature":'Min TemperatureF',
        "date"           :"PST",
    },
]

#-----------------------------------------------------------------------
#图片保存
#-----------------------------------------------------------------------
def save_draw_picture(plt, path_name):
    try:
        plt.savefig(path_name)
    except:
        print("save " + save_path_name + " falied!!")
        
#-----------------------------------------------------------------------
#csv_read_print: 读取CSV文件第一行并解析、打印相关信息
#
#next(iterator[, default])，内置函数，iterator为可迭代对象
#    default可选，用于设置在没有下一个元素时返回该默认值，
#    未设置default且无下一个元素时会触发 StopIteration 异常。

#enumerate(sequence, [start=0])，内置函数，从一个序列返回一个枚举对象
#-----------------------------------------------------------------------
def csv_read_print(file_name, max_temp_title, date_title):
    high_temperature_index = -1
    with open(file_name) as csv_obj:
        print("--------------------------------------------------------")
        print(file_name + " title info:")
        print("--------------------------------------------------------")
        #读取CSV文件，以','分割元素
        try:
            reader = csv.reader(csv_obj)
            header_row = next(reader)
        except StopIteration:
            print("no have option" + max_temp_title)
            return False
            
        #解析文件头找到最高温度的列数
        for index, column_header in enumerate(header_row):
            print(index, column_header)
            if (max_temp_title == column_header):
                high_temperature_index = index
         
        #解析文件内容，根据最高温度列数获取最高温度列
        print("--------------------------------------------------------")
        print("Max Temperature(F) of " + file_name)
        print("--------------------------------------------------------")
        high_temps = []
        for row in reader:
            high_temps.append(row[high_temperature_index])
        for date, temperature in enumerate(high_temps):
            print(date, temperature)
            
#-----------------------------------------------------------------------
#csv_read_max_temperature:读取指定csv文件的每天最高温度、最低温度列表
#-----------------------------------------------------------------------       
def csv_read_max_temperature(file_name, min_title, max_title, date_title):
    low_index = -1
    high_index = -1
    date_index = -1
    dates, lows, highs = [],[],[]
    
    with open(file_name) as csv_obj:
        try:
            reader = csv.reader(csv_obj)
            header_row = next(reader)
        except StopIteration:
            return dates, lows, highs
            
        #解析文件头找到最高温度的列数
        for index, column_header in enumerate(header_row):
            if (min_title == column_header):
                low_index = index
            elif (max_title == column_header):
                high_index = index
            elif (date_title == column_header):
                date_index = index
               
        if (low_index < 0) or (high_index < 0) or date_index < 0:
            return dates, lows, highs
 
        for row in reader:
            try:
                low = int(row[low_index])
                high = int(row[high_index])
                cur_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            except ValueError:
                print(str(cur_date) + " miss data")
            else:
                #注意，这里的温度必须是int型，否则绘制时y坐标的坐标系标码会混乱
                lows.append(low)
                highs.append(high)
                dates.append(cur_date)
        return dates, lows, highs
        
#-----------------------------------------------------------------------
#temperature_fig_show:最高/最低温度图表化显示
#使用datetime模块格式化日期信息
#strptime('xxxx-x-x', '%?-%?-%？')
#    %A:单词表示星期名
#    %B:单词表示月份名
#    %m:数字表示月份
#    %d:数字表示天数
#    %Y:四位数表示年份
#    %y:两位数表示年份
#    %H:24小时制的小时数
#    %I:12小时制的小时数
#    %p:am或pm
#    %M:分钟数
#    %S:秒数
#----------------------------------------------------------------------- 
def temperature_fig_show(filename, dates, lowest, highest, save_name):
    if len(highest) > 0 \
    and len(dates) == len(lowest) \
    and len(dates) == len(highest):
        fig = plt.figure(dpi=128, figsize=(10,6))
        
        #绘制最高和最低气温
        plt.plot(dates, highest, c='red', alpha=0.8)
        plt.plot(dates, lowest, c='green', alpha=0.5)
        plt.fill_between(dates, highest, lowest, facecolor='orange', alpha=0.3)
        
        #标题、坐标属性设置
        plt.title("Daily highest/lowest temperature of " + filename, fontsize=20)
        plt.xlabel("Date", fontsize=16)
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=8)
        
        #设置xdate格式自适应
        fig.autofmt_xdate()
        save_draw_picture(plt, save_name)
        plt.show()   
        
#-----------------------------------------------------------------------
#csv_test:测试入口
#-----------------------------------------------------------------------         
def csv_test():
    for fileObj in g_csv_file:
        filename = fileObj["filename"]
        max_title = fileObj["max_temperature"]
        min_title = fileObj["min_temperature"]
        date_title = fileObj["date"]
    
        file_name = g_load_path + filename + g_load_tail
        save_name = g_save_path + filename + g_save_tail
        csv_read_print(file_name, max_title, date_title)
        
        #获取scv数据
        dates, lowest, highest = csv_read_max_temperature( \
                        file_name, min_title, max_title, date_title)
        #绘制csv数据
        temperature_fig_show(filename, dates, lowest, highest, save_name)

            
csv_test()
