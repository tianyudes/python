# 如果列表推导式的对象是字典要怎么写
students = {
    'xuxu' : 18,
    'yyuu' : 20,
    'yytt' : 23
}
# b = [key for key,value in students]  # for前面是返回的内容 但是现在还不能被调用，会报错。
b = [key for key,value in students.items()]
print(b)
c = {value: key for key, value in students.items()}  # 键值颠倒
print(c)
d = (key for key,value in students.items())  # d 不能直接被打印原因就是元组和其他的不一样是不可变得，这里尽量不要用元组
for x in d:
    print(x)
