import random
import time


# 定义一个装饰器
def date_time (args):
    def wrapper (*args,**kwargs):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return args(*args,**kwargs)
    return wrapper




    # 定义一个读取文件内容加工后输出到随机文件中
def func (file):
    a = open(file, 'r+')
    c = random.choice('lose')
    d = open(c, 'w+')
    for i in a.readlines():
        d.write('test %s' %(i))
    a.close()
    d.close()


func("key_11.txt")






