
# 类方法
class A:
    def first(self):
        print(self)

    @classmethod
    def second(cls):
        print(cls())


a1 = A()




a1.first()

A.second()
print(A())

print(a1)



