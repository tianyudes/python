# 枚举转换 在我们将枚举类型存到数据库中
# 对于这样的存储就有两种方案： 存标签名还有存数字，推荐用数字代替标签
# 枚举类不能被实例化，是一个单例模式
from enum import Enum  # 可以是str
from enum import IntEnum, unique  # 每个数值一定是数字
# unique是一个装饰器，可以如果有相同的值会直接报错。


@unique  # 这样就可以实现在出现重复的时候被报错
class VIP(Enum):
    YELLOW = 1
    BLACK = 1  # 这样后面就会报错。
    GREEN = 3
    RED = 4


# 23种设计模式 上面的是 单例模式
a = 1
a = VIP(a)  # 输出

if a == VIP.YELLOW:  # 这里表示现在已经用了使用数值表示枚举类型的实例，不是真的类型转换。
    print("a")
print(VIP.BLACK)


# 上面的枚举类所对应的值可以是数字也可以是字符串
# 下面就介绍了一个值只能是数字的枚举类

class VIP1(IntEnum):
    YELLOW = 1
    BLACK = 2
    GREEN = 3
    RED = 4


# 这里的值不能是除了数字之外的任何数据类型