import re

s = '13B2C3D23E42F5G7'
r = re.match('\d',s) # None
# match 从开始就匹配，第一个是A所以返回的是None，删除第一个A，结果和search一样了
print(r.span())
r1 = re.search('\d',s)
# search是搜索整个字符串，一旦找到满足正则表达式的就会返回输出
print(r1.group())

# 上面的两个函数返回的是对象,返回得到之后立刻停止，这个是和findall相比最大的不同
print('--------------------组-------------------')
# 插播一个
# 组的概念

s = 'life is short, I use python, I love python'
# 提取life和python之间的内容
r = re.search('life.python',s)
print(r)  # 这个输出一定是什么都没有的因为上面的正则表达式只能匹配一个字符。要加上*才行
r = re.search('life.*python',s)
print(r.group())  # life is short, I use python

# 上面的多出来了两边的，不想要life和python
# 上面的r.group()参数里面是有数字的，传进去的是一个组号。

r = re.search('life(.*)python',s)
print(r.group(0))  # 这个0永远是完整的表达结果
print(r.group(1))  # 这个才是刚才我们想要的结果
r = re.search('life(.*)python(.*)python',s)
print(r.groups())
r = re.findall('life(.*)python',s)
print(r)

# 在网上找人家写好的正则表达式。

