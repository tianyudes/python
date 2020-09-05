# 列表推导式
# 类似于数学的集合推导式
# map()
a = [1,2,3,4,5,6,7,8]

b = [i * i for i in a]
print(b)

# 如果对列表中的元素有条件筛选的时候比较推荐使用列表推导式

c = [i * i for i in a if i % 2 == 0]
print(c)