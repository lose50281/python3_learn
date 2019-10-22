import sys as sy
from datetime import datetime

def lose (*args, **kwargs):
    a = args
    b = kwargs
    # print(type(a))
    # print(type(b))
    print(a)
    print(b)
    return '1234hello'

c = lose()
print(c)
# lose(11, 22, a=1, cc=2)
# lose(a = 1)

sy.exit(0)


