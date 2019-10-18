
import time


def data_time (hello):
    def wrapper ():
        b = time.time()
        result = hello()
        d = time.time()
        print(b, d, result)
        return result
    return wrapper


@data_time
def hello ():
    print('hello world')
    return


hello()




