# 列表推导式（有python的特色）
# 类似于数学的集合推导式
# set dic tuple 都可以被推导
a = {1,2,3,4,5,6,7,8}

b = {i * i for i in a}  # 变成集合set了
print(b)

# 如果对列表中的元素有条件筛选的时候比较推荐使用列表推导式

c = [i * i for i in a if i % 2 == 0]
print(c)