# "coding:utf-8"
# 
#***********************************************************************
#    Time           :2020年5月31日16:14:44
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :类的语法测试
#    FileName       :test_09_class.py
#***********************************************************************

#-----------------------------------------------------------------------
#导入模块中的类和导入模块中的函数语法一致
#同样当导入整个模块时，模块中类的访问也需要加"moduole."
#-----------------------------------------------------------------------

#标准库类导出
from collections import OrderedDict

#自定义库类导出
from test_09_class_role import Role, HeroesRole


#-----------------------------------------------------------------------
#测试标题打印函数
#-----------------------------------------------------------------------
global g_title_test_count
global g_title_str
g_title_test_count = 0
g_title_str = "--------------------------------------------------------"

def title_test(test_title_str = "default test"):
    global g_title_test_count
    g_title_test_count += 1
    print("\n" + g_title_str)
    print(str(g_title_test_count) + "、" + test_title_str.lower() + ":")
    print(g_title_str)

#-----------------------------------------------------------------------
#自定义类测试入口
#-----------------------------------------------------------------------
def game_test_main():
    title_test("Role class simple test")
    role_akl = Role("阿卡丽", 450)
    role_akl.get_attr_info()
    role_akl.update_attr_blood(400)
    role_akl.get_attr_info()
    
    role_nss = Role("内瑟斯", 500)
    role_ryjs = Role("熔岩巨兽", 450)
    role_swscz = Role("死亡颂唱者", 350)

    role_hero_mlps = HeroesRole("麦林炮手", 350, camp="约德尔人")
    print(role_hero_mlps.name + " 是 " + role_hero_mlps.get_hero_camp())
    role_hero_mlps.get_attr_info()
    
#-----------------------------------------------------------------------
#python库类测试入口
#----------------------------------------------------------------------- 
def python_lib_test_main():
    title_test("OrderedDict class simple test")
    book = OrderedDict()
    book['检索号'] = 'PYTHON_09_202005311816'
    book['书名'] = '《平凡的世界》'
    book['作者'] = '路遥'
    book['出版社'] = '三秦出版社'
    book['出版'] = '2020-05-31'
    book['零售价'] = 75.5
    book['库存量'] = 100
    
    for attr, info in book.items():
        entry = attr + "\t:" + str(info)
        print(entry)
    
#测试入口调用    
game_test_main()
python_lib_test_main()
