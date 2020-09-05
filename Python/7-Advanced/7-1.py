# 枚举类型,枚举就是一个类
from enum import Enum
# 从模块中导入类


class VIP(Enum):  # VIP继承Enum枚举类
    YELLOW = 1
    BLACK = 2
    GREEN = 3
    RED = 4


print(VIP.BLACK)  # VIP.BLACK
# 输出的是标签，对于很多情况下来说，人们并不需要标签下的
# 具体数值，而是这个标签，利于这人开了什么样的服务
# 增加了程序的可读性。
