# 关键字参数


def add(x, y):
    return x + y


a = add(y=3, x=1)
print(a)


# default value

def print_student_files(name, gender = '男', age = '18', college = 'NJUST'):
    print('我叫' + name)
    print('我今年' + age)
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_student_files('田雨','男','25','NJUST')
# pay attention to the order in the function.
print_student_files('tytytyty', age = '66')
# There is no need to input the name of the university, so we can set the default value.
