# 形参：位置参数，关键参数
# 实参：位置参数，默认参数，不定长参数

def nn(a, b, c, sex='man'):
    print(a, b, c, sex)


nn(1, 2, 3, sex='woman')





# 不定长参数
# def nn(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return 'Successful'
#
#
# a = nn
# a(1, 2, 3)
