import sys
sys.setrecursionlimit(1000)
# 设置最多迭代次数


def add(a,b):
    return a + b


def print_code(code):
    print(code)
    # 这个是自己调用自己，和内置函数同名就会引起无限递归


a = add(2, 3)
b = print_code('python') # 这个不会返回任何数据直接打印的话就会输出 None


print(a,b)

