# 枚举和普通类相比的优势

# 普通类

a = {'yellow':1,'red':2}
# 最贴近枚举类型
a['yellow'] = 3
# 可以轻易的修改


class TypeDiamond():
    yellow = 1
    red = 2


print(a)

# 以上两种方式的缺陷：首先是可变，可以轻易地修改他的值
# 其次是没有防止相同标签的功能


