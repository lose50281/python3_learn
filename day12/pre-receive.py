import sys
import os
import fileinput

a = '9e738e6d83672538061f4425aff26e91b53ff32f ee53bb747692fd2fa008885e0b01cbe6c985e99f refs/heads/test'
a = a.split()
print(a[0])
print(a[1])

filter = 'tapd'

# lis = []
#
# for line in fileinput.input():
#     lis = lis.append(line)
#
# print "pre-receive: Trying to push ref: %s" % (lis)
# sys.exit(1)


# b = os.popen('git log %s..%s --oneline' % (a[0], a[1]) ).readlines()

print(os.path.abspath('pre-receive.py'))