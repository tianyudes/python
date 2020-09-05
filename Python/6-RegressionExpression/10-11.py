import re
# re.findall('pattern',str, flag) 最后一个参数表示的是匹配的模式
a = 'PythonC#JavaC#'

r = re.findall('c#', a)
print(r)  # []

r1 = re.findall('c#', a, re.I)
print(r1)  # ['C#', 'C#']
# re.I 可以忽略大小写
# re.S 表示匹配所有的字符包括换行符
# 多个模式之间用| 连接

a1 = 'PythonC#\nJavaC#'
s = re.findall('c#.{1}', a1, re.I) # .不包括换行符
print(s)  # 输出[]

s1 = re.findall('c#.{1}', a1, re.I | re.S)
print(s1)  # 输出：['C#\n']

# ----------------------------re下面的其他函数--------------------------

r = re.sub('C#','GO',a)  # 等效于r = re.sub('C#','GO',a, 0) 这个0表示的就是无限制的被替换下去
print(r)  # 输出： PythonGOJavaGO

r1 = re.sub('C#','GO',a, 1)
print(r1)  # 输出：PythonGOJavaC#，只有第一个换了。

# 介绍一个内置的替换的函数
r2 = a.replace('C#','GO')
print(r2)

# 接下来是这节课的重点，就是上面sub的第二个参数：替换成的字符串可以是一个函数：下面是例子


def convert(value):
    # return '!!'+value+'!!' 报错，说明并不是那么简单的直接当作参数直接被传进来的
    # 打印一次value看看是什么
    print(value)  # 输出：<_sre.SRE_Match object; span=(6, 8), match='C#'>
    # <_sre.SRE_Match object; span=(12, 14), match='C#'>
    # 被调用两次，因为有两个c# 传给函数的值不仅仅是c#，还有c#在原来的函数中的位置span=(6, 8) 6 -> 前面有6个，占用的是7，8
    matched = value.group()  # 调用group方法
    return '!!'+matched + '!!'


r = re.sub('C#', convert, a)

# c#被匹配之后就会直接被作为参数，也就是说c#会被作为value 送到convert函数中，而convert
# 函数的输出将被用来替换原来的c#, 那么这个传进来的参数以什么样
# 形式传进来 函数的输出是什么？ 包括span和match两个参数
# sre.SRE_Match object; span=(6, 8), match='C#'
# 由于之前没有
print(r)

# 意义：如果我们替换的不是常量，而是根据匹配的结果做各种
# 各样的操做，那么就需要函数的支持，所以把函数作为参数传到
# sub的参数列表中，实现业务交给自己来处理 就是开放一个接口，传给我这样的函数然后再输出出去


