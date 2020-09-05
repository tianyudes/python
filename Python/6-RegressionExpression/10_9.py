import re

a = 'pythoythonpythonpythonc#'
# 判断这个字符串里面是否有三个python
# 这里想实现的是可以把一个字符串按照一整个字符串的形式重复几次，之前学的是字符的重复。
# 用组，一对括号就是一个组
# 比较[] 和 () [] 每一个字符之间的关系是或，而()每个字符之间的关系是且，必须都要存在。

r = re.findall('(python)',a)

# r = re.find

print(r)