import  re

# 概括字符集 例如上面的\d = [0-9] \D = [^0-9]
# \w = [A-Za-z0-9_]数字加字母 & 匹配不出来 \W 可以匹配非单词的字符
# \s 空白字符 \S 非空白字符换行符之外的所有字符。
# . 表示除换行符之外的所有的字符 \n
# 这写只能匹配单一的字符只能一个字符一个字符这样匹配
a = 'python1111java678php0swift'
b =  'python 1111&\njava6\t78p\rhp'
c = re.findall('\D',b)
print(c)
d = re.findall('\w',b)
print(d)
e =re.findall('\s',b)
print(e) # 不会输出&
s = re.findall('[0-9]',a)
print(s)
# ——————————————————————————数量词-----------------------------------
# 上面的输出都是按照字符拆开的不是按照单词的顺序排列好的。
# 所以引入数量词[char]{3,6} 长度为3到6的都会被输出
r = re.findall('[a-z]{3,6}',a)
print(r)
# 上面的明明匹配到2可以结束了为什么要一直匹配呢？什么时候能停止
# -> 贪婪与非贪婪(往往是bug出现的地方)
# python的贪婪机制就是满足条件的基础上往下进行 在数量词后面加上？ 就会变成非贪婪 满足3个就输出
# jav a后面不满足就没有输出 如果是swift应该只输出swi 是的
v = re.findall('[a-z]{3,6}?',a)
print(v)