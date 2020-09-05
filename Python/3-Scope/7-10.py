# 也可以在init文件中直接批量引入内置的库
# 下面这么写会直接报错，因为没有引入sys，但是如果每一个都要引用一大长串的内置库怎么办。这时在t里面的init文件中加入库
# init非常重要的应用
# 然后在引入t
import t
# 但是下面这么写也是不对的，因为没有指出t
# print(sys.path)
print(t.sys.path)
# 成功！

# 包和模块的导入是不会重复导入的，只导入一次

# 避免循环导入from a import b 在a里面还写from b import a

