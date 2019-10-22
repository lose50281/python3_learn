class XiaoQu:
    def __init__(self, name, local):
        self.name = name
        self.local = local

    def show(self):
        print('你小区名字是 %s 位置在 %s' % (self.name, self.local))


class HaiDian(XiaoQu):
    def __init__(self, name, local, date):
        super(HaiDian, self).__init__(name, local)
        self.date = date

    def show_h(self):
        print('你小区名字是: %s  位置在: %s  购买时间: %s年' % (self.name, self.local, self.date))


class ShangDi(HaiDian, XiaoQu):
    def show_s(self):
        print('你的名字是%s, 房龄是%s' %(self.name, self.date))
        # print(self.name)
        # print(self.local)
        # print(self.date)


p1 = XiaoQu('老冯', '朝阳')
p1.show()

p2 = HaiDian('张武斌', '海淀', 7)
p2.show_h()

p3 = ShangDi('张增玉', '丰台', 22)
p3.show_s()

print(ShangDi.mro())


