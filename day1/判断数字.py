

#a = input('判断你输入的是否数字，快来试试：')


def is_number (s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


print(is_number('ff'))
print(is_number(6))
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True




