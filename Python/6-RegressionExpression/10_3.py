# 字符集
import re
a = 'abc,acc,adc,aec,afc,ahc'
s = re.findall('a[fc]c',a) # [cf]就是c和f都可以，中括号表示或
# ac这样的普通字符一般都是用来定界的，从一个很长的字符串中找到这个满足条件的小字符串
print(s)
t = re.findall('a[^ac]c',a)
print(t)
r = re.findall('a[^a-c]c', a)
print(r)

# []表示或，^ 表示除了 - 表示从一个到另一个