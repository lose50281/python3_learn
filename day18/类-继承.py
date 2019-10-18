
# 类分为


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
