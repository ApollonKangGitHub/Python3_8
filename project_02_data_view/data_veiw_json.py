# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年6月15日19:52:17
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :json数据解析与可视化
#    FileName       :data_veiw_json.py
#***********************************************************************
from itertools import groupby

import pygal
import json
import math

global g_file_list
global g_load_path
global g_load_tail 
global g_save_path
global g_save_tail


g_save_path = r"./saveFig/jsonClosePrice/"
g_save_tail = ".svg"
g_load_path = r"./loadJson/"
g_load_tail = ".json"

g_file_list = [
    {
        "filename":"btc_close_2017",
        "date":"date",
        "month":"month",
        "week":"week",
        "weekday":"weekday",
        "close":"close",
    },
]

#-----------------------------------------------------------------------
#save_html_dash_board：将绘制的多个svg放在同一个html中
#-----------------------------------------------------------------------   
def save_html_dash_board(html_file_name, dash_board_list):
    with open(html_file_name, "w", encoding='utf-8') as html_file:
        html_file.write(
                    '<html>'
                        '<head>'
                            '<title>'
                                '收盘价仪表盘'
                            '</title>'
                            '<metacharset=\'utf-8\'>'
                        '</head>'
                        '<boday>\n')
        for svg in dash_board_list:
            html_file.write('<object type="image/svg+xml" '
                            'data="{0}" '
                            'height=500></object>\n'.format(svg))
        html_file.write('<body>'
                    '</html>')
#-----------------------------------------------------------------------
#json_test:测试入口
#-----------------------------------------------------------------------   
def draw_line(x_data,y_data,title,save,y_label):
    xy_map = []
    #x、y轴合并排序并通过groupby分组，计算每组的均值
    for x,y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
        y_list = [v for _,v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    #将x、y轴合并处理后的数据分离
    x_unique, y_mean = [*zip(*xy_map)]
    #分别绘制
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_label, y_mean)
    line_chart.render_to_file(save)
    return line_chart

#-----------------------------------------------------------------------
#json_test:测试入口
#-----------------------------------------------------------------------         
def json_test():
    dash_board_list = []
    for file_instance in g_file_list:
        file_name = file_instance["filename"]
        filename = g_load_path + file_name + g_load_tail
        dates,months,weeks,weekdays,closes = [],[],[],[],[]
        
        with open(filename) as fileObj:
            json_data = json.load(fileObj)
            for dict_data in json_data:
                date = dict_data["date"]
                month = int(dict_data["month"])
                week = int(dict_data["week"])
                weekday = dict_data["weekday"]
                close = int(float(dict_data["close"]))
                
                #-------------------------------------------------------
                #保存获取数轴列表
                #-------------------------------------------------------
                dates.append(date)
                months.append(month)
                weeks.append(week)
                weekdays.append(weekday)
                closes.append(close)
                
                print("{} is month {} week {}, {}, the close price is {} RMB".\
                    format(date, month, week, weekday, close))
        
        #创建Line示例，x坐标的标签顺时针旋转20°，且不用显示所有标签
        chart = pygal.Line(x_label_rotation=-20, show_minor_x_labels=False)
        log_chart = pygal.Line(x_label_rotation=-20, show_minor_x_labels=False)
        #x轴数据为dates
        chart.x_labels = dates
        log_chart.x_labels = dates
        #x坐标标签每隔15个数据显示一次
        chart.x_labels_major = dates[::15]
        log_chart.x_labels_major = dates[::15]
        
        #---------------------------------------------------------------
        #原始数据分析
        #---------------------------------------------------------------
        chart.title = '收盘价（￥）'
        chart.add('收盘价', closes)
        save_file = file_name + g_save_tail
        chart.render_to_file(g_save_path + save_file)
        dash_board_list.append(save_file)
        
        #---------------------------------------------------------------
        #对数据做一些对数变化，消除一些非线性趋势
        #---------------------------------------------------------------
        log_chart.title = "对数收盘价变化（￥）"
        log_closes = [math.log10(price) for price in closes]
        log_chart.add('log收盘价', log_closes)
        save_file = file_name + "_log10" + g_save_tail
        log_chart.render_to_file(g_save_path + save_file)      
        dash_board_list.append(save_file)
        
        #---------------------------------------------------------------
        #月均值处理
        #---------------------------------------------------------------  
        y_label = '月 均值'
        title = "收盘价" + y_label + "（￥）"
        save_file = file_name + '_month_average' + g_save_tail
        months_idx = dates.index('2017-12-11')
        lin_chart_month = draw_line(months[:months_idx], 
            closes[:months_idx], title, g_save_path + save_file, y_label)
        lin_chart_month
        dash_board_list.append(save_file)
        
        #---------------------------------------------------------------
        #周均值处理
        #---------------------------------------------------------------  
        y_label = '周 均值'
        title = "收盘价" + y_label + "（￥）"
        save_file = file_name + '_week_average' + g_save_tail
        week_idx = dates.index('2017-12-11')
        lin_chart_week = draw_line(weeks[1:week_idx], 
            closes[1:week_idx], title, g_save_path + save_file, y_label)
        lin_chart_week
        dash_board_list.append(save_file)
        
        #---------------------------------------------------------------
        #周 日均值处理
        #---------------------------------------------------------------  
        y_label = '周 日均值'
        title = "收盘价" + y_label + "（￥）"
        save_file = file_name + '_week_day_average' + g_save_tail
        weekEn = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
        
        week_idx = dates.index('2017-12-11')
        weekdays_int = [weekEn.index(w) + 1 for w in weekdays[1:week_idx]]
        lin_chart_week_day = draw_line(weekdays_int, 
            closes[1:week_idx], title, g_save_path + save_file, y_label)
        lin_chart_week_day
        dash_board_list.append(save_file)
                       
        #---------------------------------------------------------------
        #html仪表盘绘制  
        #---------------------------------------------------------------
        html_file_name = g_save_path + file_name + "_收盘价仪表盘.html"
        save_html_dash_board(html_file_name, dash_board_list)

json_test()
