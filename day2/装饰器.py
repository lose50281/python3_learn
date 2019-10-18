import time
import random

def timmer(func):
    """
    :param func: 被装饰的函数
    :return: 一个计算函数运行时间的函数
    """
    def wrapper(*args, **kwargs):
        """
        :param args:收集被装饰函数的参数
        :param kwargs:收集被装饰函数的关键字参数
        :return:
        """
        start_time = time.time()
        # 调用被装饰的函数
        result = func(*args, **kwargs)
        stop_time = time.time()
        print("{func} spend {time} ".format(func = func.__name__, time = stop_time - start_time))
        return result
    return wrapper

@timmer
def fff (file):
    a = open(file, 'r+')
    c = random.choice('lose')
    d = open(c, 'w+')
    for i in a.readlines():
        d.write('test %s' %(i))
    a.close()
    d.close()

fff(file="key_11.txt")





