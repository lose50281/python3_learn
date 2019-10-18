import os

f = open("key_result.txt", "r+")
b = open("key_11.txt", "w+")


for i in f:
    # i = i.strip('\n')
    # print("etcdctl get --prefix %s" %(i))
    b.write("etcdctl get --prefix %s" %(i))

os.system('ps -ef | grep mysql')

# c = os.popen('ps -ef | grep mysql', 'r')
# print(c.read())

f.seek(0)
print(f.readlines())



b.close()
f.close()







