# 上节课json->python 下面反过来、
# 上面两个的数据类型之间的转换， 这个上网自己找吧
import json
student = [{'name':'tianyu','age':18,'flag':False},
           {'name':'tianyu','age':18}
          ]
json_array = json.dumps(student)
print(json_array)
print(type(json_array)) # 列表转换成了序列化
# json字符串大多数情况下还是从python中转化过来的
# Json对象，json，json字符串（就是符合json格式标准的字符串）

# JSON对象：存在，但是是很片面的概念，在python中没有，在javascript中才会有这个概念
# JSON是一种数据交换的标准格式，有自己的数据类型
# rest服务的标准模式就是json
# JSON相当于各种语言之间的翻译


# 题外话 存储序列化的对象用MongoDB

