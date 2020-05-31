# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月31日15:07:49
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :函数测试（完善test_07_while_input.py的书籍管理系统）
#    FileName       :test_08_book_management.py
#    Modify         :2020年5月31日18:13:06
#                        使用Python的collections库OrderedDict类优化
#                    2020年5月31日23:12:37
#                         使用json优化文件操作
#***********************************************************************
import json
from collections import OrderedDict

global g_book_set
global g_json_file_name
g_json_file_name = r"book_management_system.json"

#-----------------------------------------------------------------------
#浮点数和整数有效性判断函数
#-----------------------------------------------------------------------
def tool_str_is_type(value_str = '', type_str = ''):
    if not value_str or not type_str:
        return False
        
    if type_str == 'float':
        try:
            value = float(value_str)
            return True
        except ValueError:
            print(type_str + ' : ' + value_str)
            return False
            
    if type_str == 'ufloat':
        try:
            value = float(value_str)
            if value != abs(value):
                return False
            return True
        except ValueError:
            print(type_str + ' : ' + value_str)
            return False
            
    if type_str == 'int':
        try:
            value = int(value_str)
            return True
        except ValueError:
            print(type_str + ' : ' + value_str)
            return False

    if type_str == 'uint':
        try:
            value = int(value_str)
            if value != abs(value):
                return False
            return True
        except ValueError:
            print(type_str + ' : ' + value_str)
            return False

    return True
#-----------------------------------------------------------------------
#数据初始化定义（正常为空，为了测试简单初始化了两本书作为模板）
#Modify：2020年5月31日23:52:56，使用json后不需要手动初始化数据库
#-----------------------------------------------------------------------
g_book_set  = OrderedDict({
    '新华书店':[
#        {
#            '检索号':'XH_1234567',
#            '书名':'《新华书店管理手册》',
#            '出版社':'新华出版社',
#            '出版时间':'2020-05-30',
#            '类别':'管理类',
#            '定价':"20.00",
#            '作者':'佚名',
#            '余量':"100",
#        },
#        {
#            '检索号':'XH_1234568',
#            '书名':'《三国演义》',
#            '出版社':'中华书局',
#            '出版时间':'2010-03-10',
#            '类别':'文学小说类',
#            '定价':"30.00",
#            '作者':'罗贯中',
#            '余量':"10",
#        },
    ],
    
    '新华文轩书店':[],
    
    '钟楼书店':[],
    
    '1小时书屋':[],
    
    '伴清晨诗文':[],
    
    '考研辅导资料专卖':[],
    
    '博库书店':[],
})

#系统主菜单
select_menu_sys = OrderedDict({
    '0': "系统菜单",
    '1': "书籍遍历",
    '2': "书籍入库",
    '3': "借用书籍",
    '4': "书籍检索",
    '5': "书籍信息修正",
    '6': "退出图书管理系统",
})

#书店列表
book_store = [
    '新华书店',
    '新华文轩书店',
    '钟楼书店',
    '1小时书屋',
    '伴清晨诗文',
    '考研辅导资料专卖',
    '博库书店',
]

#书本属性列表
book_attr = [
    '检索号',
    '书名',
    '出版社',
    '出版时间',
    '类别',
    '定价',
    '作者',
    '余量',
]

#-----------------------------------------------------------------------
#功能函数：系统总菜单
#-----------------------------------------------------------------------
def book_menu_sys():
    print("--------------------------------------------------------")
    for choose in select_menu_sys.keys():
        print("\t" + str(choose) + " : " + str(select_menu_sys[choose]))
    print("--------------------------------------------------------")

#-----------------------------------------------------------------------
#功能函数：显示一本书的信息
#-----------------------------------------------------------------------
def book_display_one(book, store=""):
    if store:
        print("书店：" + store)
    for attr_name in book_attr:
        if attr_name in book.keys():
            print("\t" + attr_name + " : " + str(book[attr_name]))
    print("-------------------------------------")
    
#-----------------------------------------------------------------------
#功能函数：遍历指定书店的所有书并显示
#-----------------------------------------------------------------------
def book_traversal_store(store_lib=[]):
    if not isinstance(store_lib, list):
        print("无效的书店书库信息")
        return False
    for book in store_lib:
        book_display_one(book)
    return True    
    
#-----------------------------------------------------------------------
#功能函数：书店书籍遍历，系统总入口
#-----------------------------------------------------------------------
def book_traversal_sys():
    global g_book_set
    book_set = g_book_set
    print("-------------------------------------")
    for book_store_name in book_store:
        if book_store_name in book_set.keys():
            book_store_lib = book_set[book_store_name]
            print(book_store_name + ":")
            print("-------------------------------------")
            book_traversal_store(book_store_lib)
    print("-------------------------------------")

#-----------------------------------------------------------------------
#功能函数：新书入库执行函数
#-----------------------------------------------------------------------
def book_new_add(store = [], book = {}):
    if not isinstance(store, list):
        print("无效的书店")
        return False    
    if not isinstance(book, dict):
        print("无效的书籍")
        return False    
        
    if not isinstance(book["检索号"], str):
        print("无效的检索号")
        return False
    if not isinstance(book["书名"], str):
        print("无效的书名")
        return False
    if not isinstance(book["出版社"], str):
        print("无效的出版社")
        return False
    if not isinstance(book["出版时间"], str):
        print("无效的出版时间")
    if not isinstance(book["类别"], str):
        print("无效的类别")
        return False
    if not tool_str_is_type(book["定价"], 'ufloat'):
        print("无效的定价：" + book["定价"])
        return False    
    if not isinstance(book["类别"], str):
        print("无效的作者")
        return False
    #if not tool_str_is_type(book["余量"], 'uint'):
    if not book["余量"].isdigit():
        print("无效的余量：" + book["余量"])
        return False
        
    store.append(book)
    return True
#-----------------------------------------------------------------------
#功能函数：书店书籍添加入库，指定书籍到指定库
#-----------------------------------------------------------------------
def book_add_to_store(store='', book={}):
    if not store or store not in book_store:
        print("无效的书店" + store)
        return False
        
    if not book or not isinstance(book, dict):
        print("无效的书籍")
        return False
        
    global g_book_set    
    book_set = g_book_set            
    #简单起见，遍历索引号，根据索引号确定是新增书籍还是原有书籍统计增加
    for book_ref in book_set[store]:
        #已有书籍本数增加即可（其他参数不关心不修改）
        if book["检索号"] in book_ref.values():
            if book["余量"].isdigit():
                book_cur_num = int(book_ref["余量"])
                book_add_num = int(book["余量"])
                book_ref["余量"] = str(book_cur_num + book_add_num)
                return True
            else:
                print("无效的数量,入库数量:" + str(book["余量"]))
                return False
    #新书入库
    return book_new_add(book_set[store], book)
    
#-----------------------------------------------------------------------
#功能函数：书店书籍添加入库，系统总入口
#-----------------------------------------------------------------------
def book_add_sys():
    new_book = {}
    print("-------------------------------------")
    print("书籍入库,请按照提示信息录入书籍信息：")
    for attr in book_attr:
         new_book[attr] = input(str(attr) + ":").strip()
         
    store = input("请输入要将该书籍入库的书店名称：").strip()
    print("新的要添加的书籍信息为:")
    print("书店:" + store)
    for attr in new_book.keys():
        print(str(attr) + " : " + str(new_book[attr]))
    choose = input("请确认添加与否(Y/N)：").strip()
    if choose.upper() == 'Y':
        book_add_to_store(store, new_book)
    else:
        print("书籍加入人为终止，退出!")
    print("-------------------------------------")
    
#-----------------------------------------------------------------------
#功能函数：指定书店、指定检索号的书籍借用
#-----------------------------------------------------------------------
def book_borrow_store_with_search_num(store='', search_seq=''):
    if not search_seq:
        print("Invalid search_seq")
        return False
        
    if not store or store not in book_store:
        print("invalid book store" + store)
        return False
        
    global g_book_set    
    book_set = g_book_set
    #遍历指定书店的所有书，找到指定检索号的书
    books = book_set[store]
    for book_ref in books:
        if book_ref["检索号"] == search_seq:
            print("请检查所检索的书籍是否是需要借用的书籍:")
            book_display_one(book_ref, store)
            choose = input("是否是需要借用的书籍(Y/N):").strip()
            if choose.upper() == 'Y':
                while True:
                    num = input("请输入要借用的本/册数：").strip()
                    if int(num) > int(book_ref["余量"]):
                        print("余量不足！！余量：" + book_ref["余量"])
                        continue
                    else:
                        break

                sure = "要借用的册数为" + num + "(Y/N):"
                choose = input(sure).strip()
                if choose.upper() == 'Y':
                    old_num = int(book_ref["余量"])
                    new_num = old_num - int(num)
                    book_ref["余量"] = str(new_num)
                    success = book_ref["书名"] + ":" + num + " 本/册！"
                    print("借书成功，" + success)
                    return True
                else:
                    print("用户终止借书流程！")
                    return True
            else:
                print("用户终止借书流程！")
                return True
        else:
            continue
    #未找到对应书籍
    print("未找到对应书籍，检索号请核对：" + search_seq)
    return False

#-----------------------------------------------------------------------
#功能函数：书店书籍借用，系统总入口
#-----------------------------------------------------------------------
def book_borrow_sys():
    print("-------------------------------------")
    print("书籍借用（只能根据书籍检索号借用，可进行书籍检索以获取）：")
    store_name = input("请输入书店名：").strip()
    search_seq = input("请输入检索号：").strip()
    book_borrow_store_with_search_num(store_name, search_seq)
    print("-------------------------------------")
    
#-----------------------------------------------------------------------
#功能函数：从指定书店检索指定属性的书籍
#-----------------------------------------------------------------------
def book_find_from_store_with_attr(store='', attr='', value=''):
    if not store or store not in book_store:
        print("invalid book store" + store)
        return False

    if not attr or attr not in book_attr:
        print("invalid book attr" + attr)
        return False
        
    global g_book_set
    count = 0
    book_set = g_book_set
    #遍历指定书店的所有书，找到指定属性的所有书
    books = book_set[store]
    for book_ref in books:
        if book_ref[attr] == value:
            count += int(book_ref["余量"])
            book_display_one(book_ref, store)

    if count > 0:
        print("检索到书籍[" + attr + "]" 
            + "=[" + value + "]的总余量为：" 
            + str(count) + "（本/册）")
        return True
    else:
        #遍历完统计为0则未找到
        print("未检索到书籍[" + attr + "]" + "=[" + value + "]")
        return False

#-----------------------------------------------------------------------
#功能函数：书店书籍检索，系统总入口
#-----------------------------------------------------------------------
def book_find_sys():
    print("-------------------------------------")
    store_name = input("请输入书店名：").strip()
    print(book_attr)
    attr = input("请从以上属性中选择书籍检索类型：").strip()
    value = input("请输入要检索类型对应的名字/值：").strip()
    if attr in book_attr:
        book_find_from_store_with_attr(store_name, attr, value)
    else:
        print("无效的输入:" + choose)
    print("-------------------------------------")
    
#-----------------------------------------------------------------------
#功能函数：书店书籍信息修正
#-----------------------------------------------------------------------
def book_modify_store(store='', search_seq=''):
    if not search_seq:
        print("Invalid search_seq")
        return False
        
    if not store or store not in book_store:
        print("invalid book store" + store)
        return False

    #遍历指定书店的所有书，找到指定检索号的书
    global g_book_set
    book_set = g_book_set
    books = book_set[store]
    for book_ref in books:
        if book_ref["检索号"] == search_seq:
            print("请检查所检索的书籍是否是需要修改的书籍:")
            book_display_one(book_ref, store)
            choose = input("是否是需要修改的书籍(Y/N):").strip()
            if choose.upper() == 'Y':
                print("请按照提示信息修改书籍信息（不修改的属性直接回车）：")
                for attr in book_attr:
                    new_attr = ""
                    new_attr = input(str(attr) + ":").strip()
                    if new_attr != "":
                        book_ref[attr] = new_attr
            else:
                print("不修改信息，退出！")
            return True
    #遍历完毕没有匹配的检索号，则表示检索号错误
    print("Invalid Search number:" + search_seq)
    return False
    
#-----------------------------------------------------------------------
#功能函数：书店书籍信息修改，系统总入口
#-----------------------------------------------------------------------
def book_modify_sys():
    print("-------------------------------------")
    print("书籍信息修正（只能根据书籍检索号修正）：")
    store_name = input("请输入书店名：").strip()
    search_seq = input("请输入检索号：").strip()
    book_modify_store(store_name, search_seq)
    print("-------------------------------------")
    
#-----------------------------------------------------------------------
#功能函数：退出书店，系统总入口
#-----------------------------------------------------------------------
def book_quit_sys(customer_name, file_name):
    global g_book_set
    book_set = g_book_set
    try:
        with open(file_name, 'w', encoding='utf-8') as file_object:
            print("-------------------------------------")
            print(customer_name + "正在退出图书管理系统，请稍等!")
            json.dump(book_set, file_object)
            print("-------------------------------------")
            print("json dump dictionary to " + file_name + " succeed!")
    except FileNotFoundError:
        print(file_name + "file or dirctory is not exist")

#-----------------------------------------------------------------------
#功能函数：进入书店，初始化系统总入口
#-----------------------------------------------------------------------       
def book_system_init(customer_name='', file_name=''):
    global g_book_set
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            print("-------------------------------------")
            print(customer_name + "正在初始化图书管理系统，请稍等!")
            print("-------------------------------------")
            
            json_str = file_object.read()
            if len(json_str) > 0:
                g_book_set = json.loads(json_str)
                print("json load dictionary to " + file_name + " succeed!")
            else:
                print("没有库存数据!!")
                return True
    except FileNotFoundError:
        print(file_name + "file or dirctory is not exist")
        
#-----------------------------------------------------------------------
#主菜单入口，系统菜单处理逻辑
#-----------------------------------------------------------------------
def book_main(customer_name=''):
    if not customer_name:
        customer_name = '游客'
    print(customer_name + "，欢迎进入全国书籍检索网")

    #系统初始化
    book_system_init(customer_name, g_json_file_name)

    #系统菜遍历范围计算
    start_select = 0
    end_select = len(select_menu_sys) - 1
    range_str = '(' + str(start_select) + '~' + str(end_select) + '):'

    #系统菜单
    book_menu_sys()
    menu_choose = True
    while menu_choose:
        choose = input("请输入你要选择的操作" + range_str).strip()
        print("-------------------------------------")
        if choose == "":
            continue
        elif choose not in select_menu_sys.keys():
            print("无效的输入，请在有效范围内输入操作编号！")
            continue
            
        #choose有效
        print("choose is " + str(choose) + ": " + str(select_menu_sys[choose]))
        
        if select_menu_sys[choose] == "系统菜单":
            book_menu_sys()
        elif select_menu_sys[choose] == "书籍遍历":
            book_traversal_sys()
        elif select_menu_sys[choose] == "书籍入库":
            book_add_sys()
        elif select_menu_sys[choose] == "借用书籍":
            book_borrow_sys()
        elif select_menu_sys[choose] == "书籍检索":
            book_find_sys()
        elif select_menu_sys[choose] == "书籍信息修正":
            book_modify_sys()
        elif select_menu_sys[choose] == "退出图书管理系统":
            book_quit_sys(customer_name, g_json_file_name)
            menu_choose = False
#入口函数         
book_main()
