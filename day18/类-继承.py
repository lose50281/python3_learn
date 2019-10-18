
'''
类的分类：
    新式类
    经典类

区别，新式类基类默认会使用Object类，而经典类不会
新式类在python3中是默认类型
经典类在python2中是默认类型

类的继承顺序：

不管新式类、经典类对于单参是深度优先
对于多参，在新式类中使用广度优先，经典类使用深度优先。
'''


class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def speak(self):
        print('%s 说: 我 %d 岁。' % (self.name, self.age))


class Student(People):
    grade = ''

    def __init__(self, name, age, sex, grade):
        People.__init__(self, name, age, sex)
        self.grade = grade

    def speak(self):
        print('%s 说：我 %s 岁了，我在读 %s 年级' % (self.name, self.age, self.grade))


s = Student('lose', 18, 'man', 3)
s.speak()






# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
# s = people('lose',18,130)
# s.speak()
