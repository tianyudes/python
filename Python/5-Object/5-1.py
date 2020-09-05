# 类的名字尽量用两个大写不要用下划线
# 类的最基本作用就是在封装代码



class Student():
    sum1 = 0 # 这个sum才是跟这个类有关的变量，叫做类变量，他不属于任何一个实例，任何一个实例调用它也是没有意义的。
    # 访问类变量的方式：print(Student.sum1) / print(student1.__class__.sum1) 第二个方式就是找到student1所在的类然后在这个类下面找到类变量
    name = '' # name = 'qiyue' 实际上这样的定义并不是十分合理的因为一个一个类是不应该有名字的，有名字和年龄的应该是实例。
    __age = 0 # 所以这两个变量叫做实例变量，是为了构造实例而创建的变量
    # 在构造函数里面要加上原来的self还有想要构造的时候赋值的变量
    # 类变量 ： 跟类相关联的，上面的两个都是类变量
    # 实例变量 ： 跟实例相关联的，实例是由模板创建来的 'tytyyt'之类的
    # 下面的self是可以变化的，只是系统推荐使用self，写成this也可以。

    def __change_name(self):
        self.name = 'tytyty'

    def __init__(self,name,age):
        self.name = name
        self.age = age


# 对于类内部的方法来说这个一定要加上一个参数self否则就会报错
# 对于一个类来说学生和档案管理之间是没有任何的关系的，对于一个类来说我们要做的就是反应这个类的特征和行为。

    def set_age(self, age):
        self.__age = age


    def print_file(self):
        print('name :' + self.name)
        print('age: ' + str(self.age))

    # 如何定义一个类方法： 首先要把变量从self改成cls,cls表示的就是调用类方法的这个类。
    # 但是改成cls就能说明这个是一个类方法么？ 不能因为上面说了，self的位置上可以换成任何变量，那么怎么区分
    # 在函数定义的前面加上@classmethod 这是一个装饰器, 表明这是一个
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print('当前学生数：' + str(cls.sum1))

    # 静态方法
    # 静态方法的特点： 首先没有强制传入的变量self 和 cls  有 staticmethod装饰器
    # 建议不要经常使用静态方法因为和对象的关系非常的弱。而且可以呗一个类函数代替
    @staticmethod
    def add(x, y):
        # 可以访问类变量
        print(Student.sum1)
        print('this is a static method')

# 可以定义若干个变量
# 实例化
# 对于一个好的程序。类应该是单独存放在一个模块里的，而对他的调用应该放在另一个模块里

# 构造函数里面添加了变量所以这里也要加上


student1 = Student('tyty',22)
student2 = Student('ty',22)
student2.set_age(100)
student1.__class__.plus_sum()
student1.set_age(-10)
student1.__age = -1
print(student1._Student__age)
print(student1.__dict__) # 会出现这样的两个变量 ：  '_Student__age': -10, '__age': -1。 第一个是python存储私有变量的机制，就是直接_+ 类名 + __age
# 所以在student2里面是找不到__age这个变量的，如果我们不直接写student1.__age = -1 这句话就不会有这个变量, 所以python的私有机制就是换个名字，但是实际上
# 如果用户一定要读，读改了名字的变量是可以的，全靠自觉。
#
print(student2.__dict__)
# student1.__change_name()
# print(student2.__age) # 这个时候显示没有__age这个变量，就说明了这个变量是不存在student2中的
# 实例方法：就是所有的实例可以调用的方法。
# 对于所有的实例方法，第一个参数必须是self。但是调用的时候是不用我们程序里面明确写出的，系统会帮忙调用
# self表示的就是当前调用方法的对象，比如student1.print_file()中的student1就是。

print(Student.sum1)


# 如何实现java c++中的public private的效果； 在原来的方法名变量名前面加上__就会变成私有属性
# 对一个私有变量直接访问的时候是可以的，但是对一个私有的方法就会出现报错。
# 什么可以访问什么不可以访问呢
# student1.__age 相当与添加了一个__age的变量的

