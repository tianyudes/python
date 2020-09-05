# 枚举的比较运算

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1  # 如果值相同那么后面出现的就是别名
    GREEN = 3
    RED = 4


# 在定义时如果出现两个标签的值相同，则意味着第二个标签是1的别名
# 打印的时候任然按照第一个打印，并没有被算作是一个独立的标签
print(VIP.GREEN)

for v in VIP:
    print(v)

    # 结果第二个仍然是yellow，如果我打的是yellow_alias则 后面的不会出现
    # 只有三个

# 如果想全部输出的话就要访问他的成员
for v in VIP.__members__.items():
    print(v)
    # 输出四个成员 items 结果是元组，内容全都输出了

for v in VIP.__members__:  # 结果比较精简
    print(v)