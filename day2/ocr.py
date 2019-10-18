import time

def is_decorator(func):
    def wrapper():
        aa = func()
        print('hello world')
        return aa
    return wrapper

@is_decorator
def date():
    a = time.time()
    time.sleep(1)
    b = time.time()
    print('running time is {result}' .format(result=b-a))
    return

date()



