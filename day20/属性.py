
class XiaoQu:
    def __init__(self, name, age):
        self.name = name
        if type(age) is int:
            self.__age = age
        else:
            print('垃圾')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a1):
        if type(a1) is int:
            self.__age = a1
        else:
            print('弱爆了')

p1 = XiaoQu('zhang', 20)
print(p1.age)
p1.age = '18'
print(p1.age)



