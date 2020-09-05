import re
# * 星号表示前面的字符可以出现0次或无数次，看下面的例子。
# + 表示匹配1次或无限多次
# ? 表示匹配一次或者0次
a = 'pytho0python1pythonn2'
s =  re.findall('python*',a) # ['pytho', 'python', 'pythonn']
print(s)
t = re.findall('python+',a) # ['python', 'pythonn']
print(t)
r = re.findall('python?',a) # ['pytho', 'python', 'python'] 最后一个多出来的n会被去掉pythonn中前面的部分也是符合要求的，所以直接把这部分输出
# 这个？可以用来实现去重的操做
print(r)

w = re.findall('python{1,2}',a) # 上节课讲的贪婪机制
print(w)

x = re.findall('python{1,2}?',a) # 改成非贪婪 ['python', 'python']
print(x)
