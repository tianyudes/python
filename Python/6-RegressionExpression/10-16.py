# JSON是一种轻量级（XML）的数据交换格式，可以跟每一种语言中的一种数据结构进行数据转换的，跨语言交换数据
# python 和 JSON 进行数据交互
# 数据的载体就是一个字符串
json__str = "{name: qiyue, age:18}"  # 这个不符合规范
json_str = '{"name": "qiyue", "age":18}'  # 这个符合规范 json和语言无关，有json自己的格式标准，要求用双引号表示字符串
# 在任何一个语言中都可以找到对应的一个数据类型与json对应
# 在python中有一个模块叫json

import json
# json.loads()可以帮助我们转换成相应的数据结构
student = json.loads(json_str)
# jason字符串的要求：所有的字母都要括在双引号里面，外部是单引号

print(type(student))  # 类型是字典，要记住
print(student)  # 内容是单引号括起来的 这个跟json无关已经转到了python里面
print(student['name'])
print(student['age'])

# 不同的语言可能转换成不同的数据类型 上面的是Json的对象转成了
# 字典

# JSON字符串的数组
json_array = '[{"name": "qiyue", "age":18, "flag":false},{"name": "qiyue", "age":18}]'

student = json.loads(json_array)
# jason字符串的要求：所有的字母都要括在双引号里面，外部是单引号
# 这样的从json的数据类型到python的数据类型，这样的变化叫反序列化
print(type(student)) # 类型是list 列表 ，要记住
print(student) # 内容是单引号括起来的
#print(student['age'])