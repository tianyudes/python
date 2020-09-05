import re
# 这个是我练习的函数
s = 'tianyushideyi@q.com'

r = re.search('(\d*)@(\w*)',s)


def check(r):
    if str(r) in ['qq','gmail','sina','icloud']:
        print("可以继续")
    else:
        print("重新输入")


check(r.group(2))

a = '12121212121'

r = re.search('\d*',a)


def qq_check(r):
    if len(r)>10:
        print( "没有这么多位qq")
    else:
        print ("欢迎成为用户")


qq_check(r.group())

m = '04122597736'
r = re.findall('\d{4}(\d*)',m)
print(r)