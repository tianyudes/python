# 正则表达式 是一个特殊的字符序列帮助我们检测，一个字符串
# 是否与我们所设定的字符序列相匹配，实现快速检索文本，实现文本操作的功能

# 1. 一串数字是否是电话号码
# 2. 检测一组，一个字符串是否符合email的标准

'''
例一
'''
a = 'C0C++1Java2c#4Python6Javascript7thon'

print(a.index('Python')>-1)
print('Python' in a)
# 优先选择内置函数

import re

# re中的findall函数 findall([pattern],str) 第一个参数表示的是正则表达式的格式，str是字符串
r = re.findall('Python',a)
print(r)
# 返回的结果是一个列表，因为我们的函数名是findall，所以经常会出现不只找到一个的情况。所以采用列表。 列表中的就是我们需要的字符串
# 正则表达式的优势在于他可以制定规则，使得拿来检测的str满足规则
