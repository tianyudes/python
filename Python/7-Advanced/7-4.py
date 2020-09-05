# 枚举之间的比较

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    BLACK = 2
    GREEN = 3
    RED = 4


print(VIP.BLACK == 2)  # 输出的是 False
print(VIP.BLACK == VIP.RED)
print(VIP.RED == VIP.RED)
# print(VIP.RED > VIP.BLACK)  # 枚举类型不能比大小，但是可以等值和归属比较
print(VIP.RED is VIP.RED)
