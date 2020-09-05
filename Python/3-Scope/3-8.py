# import module_name
# python是解释型语言要先导入
import c7
print(c7.a)
# import t.c7 as m 可以简化模块命名空间
'''
好处：明显的看清出自哪一个包下面
缺点：长
'''
# from module import variable 从模块直接导入变量 * 表示全部导入，但是不是很推荐，因为没有很明确
# 在导入包的时候会自动执行下面的__init__.py文件 在init中可以定义__all__ 决定哪些模块可以被导出。


from c7 import *
print(a)
print(b)
print(c)

