# 关键字参数


def add(x, y):
    return x + y


a = add(y=3, x=1)
print(a)


# 默认参数

def print_student_files(name, gender = '男', age = '18', college = 'NJUST'): # 非默认参数一定要向前放
    print('我叫' + name)
    print('我今年' + age)
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_student_files('田雨','男','25','NJUST')
# 这么该不对 print_student_files('ttytyty',,'66',)
# 关键字参数，这里的关键字参数可以不按照顺序写
print_student_files('tytytyty', age = '66')
# 但是对于学校来说这个，是没有必要每个人都一个一个得输入学校得。 所以就要有一个默认值
