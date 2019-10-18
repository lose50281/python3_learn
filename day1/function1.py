

def hello (a, f=33, b=100):
    print(a, f, b)


hello(f=22, b=1111, a='44')



# def test (a, *kargs):
#     print(a, *kargs)
#
# test(90, 80, 20, 8888)




import time

def echo (lose):
    def wrapper ():
        print('hi lose welcome to beijing')
        return lose()
    return wrapper

@echo
def lose (*args,**kwargs):
    start_time=time.time()
    time.sleep(0.5)
    end_time=time.time()
    sum_time=end_time-start_time
    return sum_time


print(lose())