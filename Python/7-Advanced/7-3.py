from enum import Enum


class VIP(Enum):
    YELLOW = 1
    BLACK = 2
    GREEN = 3
    RED = 4


print(VIP.BLACK.value)  # 获取标签的数值
# VIP.BLACK = 6 这个执行起来会报错
print(type(VIP.BLACK))  # 输出的类型名 <enum 'VIP'>
print(VIP.BLACK.name)  # 输出的是str，上面11-1里面打印的是枚举类型
# 可以通过.value和.name来得到标签的值和名称
print(VIP['GREEN'])  # 通过名称可以得到枚举类型


# 遍历
for v in VIP:
    print(v)
    print(type(v))  # <enum 'VIP'>

# 区分以下概念
# 枚举类型（就是他包含着两个内容枚举的名字和值），枚举的名字，枚举的值

