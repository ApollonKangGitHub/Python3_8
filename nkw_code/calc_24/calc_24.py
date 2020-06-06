# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年6月5日21:09:45
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :扑克的24点运算
#    FileName       :calc_24.py
#***********************************************************************

def jia(a,b):
    return (a+b)
def jian(a,b):
    return (a-b)
def cheng(a,b):
    return (a*b)
def chu(a,b):
    return (a/b)
    
#------------------------------------------------------------
# 主函数
#------------------------------------------------------------
global valid
global listv
global oper
valid = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':11,
    'Q':12,
    'K':13,
    'joker':0,
    'JOKER':0
}
listv = []
oper = ['+','-','*','/']

#-----------------------------------------------------------
#最后一步计算
#-----------------------------------------------------------
def calc_3(v1,v2,o1):
    if o1 == '+':
        if jia(v1,v2) == float(24):
            return True
        else:
            return False
    elif o1 == '-':
        if jian(v1,v2) == float(24):
            return True
        else:
            return False
    elif o1 == '*':
        if cheng(v1,v2) == float(24):
            return True
        else:
            return False
    elif o1 == '/':
        if chu(v1,v2) == float(24):
            return True
        else:
            return False
    else:
        return False
#-----------------------------------------------------------
#第二步计算
#-----------------------------------------------------------
def calc_2(v1,v2,v3,o1,o2):
    if o1 == '+':
        return calc_3(jia(v1,v2), v3, o2)
    elif o1 == '-':
        return calc_3(jian(v1,v2), v3, o2)
    elif o1 == '*':
        return calc_3(cheng(v1,v2), v3, o2)
    elif o1 == '/':
        return calc_3(chu(v1,v2), v3, o2)
    else:
        return False
#-----------------------------------------------------------
#前两个值计算
#-----------------------------------------------------------
def calc_1(v1,v2,v3,v4,o1,o2,o3):
    if o1 == '+':
        return calc_2(jia(v1,v2), v3, v4, o2, o3)
    elif o1 == '-':
        return calc_2(jian(v1,v2), v3, v4, o2, o3)
    elif o1 == '*':
        return calc_2(cheng(v1,v2), v3, v4, o2, o3)
    elif o1 == '/':
        return calc_2(chu(v1,v2), v3, v4, o2, o3)
    else:
        return False
    
#-----------------------------------------------------------
#主调，运算规则：
#输入四张牌，以空格分开，能算出24则输出符合的一条算式即可，结果不关心原有顺序，
#算式的四个值顺序，可不符合输入顺序，大小王joker/JOKER不能运算，返回ERROR
#没有符合结果24的组合则返回NONE，算式运算规则从左到右依次运算，不采用数学优先级
# J、Q、K、A分别代表数字11、12、13、1，2~10分别代表数字2~10
#如：
#输入"A 8 A A" 返回 "1+1+1*8=24"
#输入"A A A A" 返回 "NONE"
#输入"A JOKER A A" 返回 "ERROR"
#-----------------------------------------------------------
def main(tmp):
    global valid
    global listv
    global oper
#    tmp = input().strip()
    listv = tmp.split(' ')
    
    if len(listv) != 4:
        return tmp + " NONE"

    for val in listv:
        if (val == 'joker' or val == 'JOKER'):
            return tmp + " ERROR"
            
               
    v1 = float(valid[listv[0]])
    v2 = float(valid[listv[1]])
    v3 = float(valid[listv[2]])
    v4 = float(valid[listv[3]])
    s1 = str(valid[listv[0]])
    s2 = str(valid[listv[1]])
    s3 = str(valid[listv[2]])
    s4 = str(valid[listv[3]])

    for op1 in oper:
        for op2 in oper:
            for op3 in oper:
                if calc_1(v1, v2, v3, v4, op1, op2, op3):
                    return s1+op1+s2+op2+s3+op3+s4+'=24'

    return tmp + " NONE"
    
#main(v1+' '+v2+' '+v3+' '+v4)
