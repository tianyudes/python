a = [1, 2, 3, 4, 5, 6, 7]
# 用for循环的方法
for x in range(0, len(a), 2):
    print(x, end=' | ')

# 还可以用切片

b = a[0:len(a):2]
print(b)


