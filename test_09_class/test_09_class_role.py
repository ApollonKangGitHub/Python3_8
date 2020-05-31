# "coding:utf-8"
#
#***********************************************************************
#    Time           :2020年5月31日17:59:43
#    Author         :Kangruojin
#    Email          :mailbox_krj@163.com
#    Compile        :Python3.8
#    version        :1.1
#    Description    :类的模块化--角色类
#    FileName       :test_09_class_role.py
#***********************************************************************
from test_09_class_equip import Equipment

#-----------------------------------------------------------------------
#类的创建与使用:角色类
#-----------------------------------------------------------------------
class Role():
    global g_role_count
    g_role_count = 0
    
    #对象创建初始化函数,函数名是__init__()
    #必须放在第一个并且
    def __init__(self, 
                name='invalid', 
                blood_volume=300, 
                attack=10, 
                defense=10):
        self.name = name
        self.blood = blood_volume
        self.attack = attack
        self.defense = defense
        
        global g_role_count
        g_role_count += 1
        if g_role_count == 1:
            print("1st Role instance create succcess.")
        elif g_role_count == 2:
            print("2nd Role instance create succcess.")
        elif g_role_count == 3:
            print("3rd Role instance create succcess.")
        else:
            print(str(g_role_count) + "th Role instance create succcess.")
    
    #获取角色属性
    def get_attr_info(self):
        print(self.name.title() 
            + "的血量为：" + str(self.blood)
            + ",攻击力为：" + str(self.attack)
            + ",防御力为：" + str(self.defense))

    #更新角色血量
    def update_attr_blood(self, blood):
        self.blood = blood

    #获取角色总数
    def common_get_role_member_number(self):
        return g_role_count

#-----------------------------------------------------------------------
#类的继承：
#    1、B继承A则必须保证A在B之前声明
#    2、父类A也称为超类（supercalss），因此在子类的__init__()中，
#    应该调用super().__init__()先完成对父类的初始化，再初始化子类自己
#    3、类名用驼峰命名法，函数用下划线命名法
#
#    4、python3.8父类和子类创建语法：
#    class Father():
#        def __init__(self, pa, pb, pc)
#        ......
#    class Son(Father):
#        def __init__(self, pa, pb, pc, pd, pe)
#            super().__init__(pa, pb, pc)
#        ......
#
#    5、python2.7父类和子类创建语法:
#        (创建子类会给父类传递self，帮助python把父子类关联起来)：
#    class Father(object):
#        def __init__(self, pa, pb, pc)
#            ......
#    class Son(Father):
#        def __init__(self, pa, pb, pc, pd, pe)
#            super(Son, self).__init__(pa, pb, pc)
#            ......
#-----------------------------------------------------------------------
class HeroesRole(Role):
    #子类‘英雄角色’继承自父类Role
    def __init__(self, 
                name='invalid', 
                blood_volume=300, 
                attack=10, 
                defense=10,
                camp='unknown'):
        super().__init__(name, blood_volume, attack, defense)
        self.camp = camp
        #装备类的实例作为英雄的一个属性
        self.equip = Equipment(weapon="多兰剑")
        
    #获取英雄阵营
    def get_hero_camp(self):
        return self.camp
        
    #父类方法重写
    def get_attr_info(self):
        print(self.camp + self.name.title() 
            + "的血量为：" + str(self.blood)
            + ",攻击力为：" + str(self.attack)
            + ",防御力为：" + str(self.defense)
            + ",武器为：" + str(self.equip.weapon))
