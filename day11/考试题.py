a = [1,2,3]
a.extend('apple')
a.append('apple')
print(a)


b = a[:]
print(id(a))
print(id(b))


