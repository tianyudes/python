import re

# 正则表达式就是由一系列的普通字符(python)和元字符(\d)的组合构成的
# \d 表示的是所有的数字
# \D 表示的是除了0-9之外的字符
a = 'c0c++5python6c#9java7javascript3'

s = re.findall('\d',a)
r = re.findall('\D',a)
print(s)
print(r)