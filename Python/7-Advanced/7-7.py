# 闭包

a = 0


def step_pre(pos):

# 把原来的全局变量变成只修改局部变量，声明了不是局部变量
    def step(x):
        nonlocal pos
        step_num = pos + x
        pos = step_num
        return pos

    # a = step(x)
    return step


tourist = step_pre(a)
print(tourist(3))
print(tourist(4))