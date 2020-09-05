# 闭包解决问题
# 旅行者的长度，通过调用函数
# 代码大学2这本书里面强调尽量少用全局变量
# 工厂模式


def pace_pre(x):

    def pave(y):
        nonlocal x  # 这个地方要想到设置x不是局部变量
        x = x + y
        return x

    return pave


# 闭包具有记忆性，要记住
f = pace_pre(0)
print(f(3))
print(f(5))
print(f(6))